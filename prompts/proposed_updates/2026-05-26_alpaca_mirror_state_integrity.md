# Proposed update — Alpaca-mirror state integrity: stop persistence + circuit-breaker basis truth

**Author:** Claude (assistant), human-directed (operator asked to "continue with the proposed fix" on 2026-05-26)
**Date:** 2026-05-26
**Status:** DRAFT — awaiting human PR review. No protected file edited; no trade placed.
**Scope:** `lib/` code changes only. Touches no `config/*`, no `.claude/agents/*`, no `prompts/routines/*`.

## Reason

Two silent-safety-degradation defects have been observed on every paper-trading
session since the Alpaca mirror went live (2026-05-18 onward). Both are rooted in
the same place: **`paper_sim.reconcile()` rebuilds local risk state from the Alpaca
mirror, which does not carry our risk metadata.** Neither defect has cost money yet,
but both mean a core risk control is *advertised as active while actually inert or
mis-calibrated*. Evidence is now repeated and quantified (W21 weekly review +
2026-05-26 EOD journal).

### Defect 1 — Automated stops are silently OFF (MUST-FIX)

- **Mechanism:** `reconcile()` ([lib/paper_sim.py:505](../../lib/paper_sim.py)) rebuilds
  `positions.json` from the Alpaca mirror with `stop_loss=None, take_profit=None`
  (see lib/paper_sim.py ~457 and ~495). `portfolio_health._assess_one`
  ([lib/portfolio_health.py:52](../../lib/portfolio_health.py)) treats a null stop as
  "no stop" and skips the breach check at line 73. The deterministic stop monitor is
  therefore **inert on every position, every session.**
- **Evidence:** Flagged in `journals/daily/2026-05-22.md` (market_open/midday/pre_close/EOD
  all note "stop check is inert; advisory-by-hand") and again at `journals/daily/2026-05-26.md`
  EOD. The W21 review lists it MUST-FIX (Mistake 2).
- **Live exposure right now:** As of 2026-05-26 EOD, **UNH is −8.23% unrealized and only
  +2.17% above its $352.02 −10% rotation stop** — the thinnest cushion in the book. If UNH
  gaps through the stop overnight, the automated `portfolio_health` check will NOT fire it;
  it is currently caught only by a human eyeballing the log each routine.

### Defect 2 — Circuit-breaker runs on the wrong equity basis (MUST-FIX / HIGH)

- **Mechanism:** Routines feed `portfolio_risk.advance(current_equity=...)`
  ([lib/portfolio_risk.py:213](../../lib/portfolio_risk.py)) the **sim-basis** equity
  (`paper_sim.portfolio_equity()`, [lib/paper_sim.py:567](../../lib/paper_sim.py)) rather
  than the broker-authoritative equity. `advance()` is basis-agnostic — it trusts whatever
  the caller passes — so the basis choice lives in the routine layer.
- **Evidence (quantified, 2026-05-26 EOD):** CB drawdown read **1.93%** (sim basis
  $102,084.32) while the **broker-authoritative drawdown was 3.42%** (broker equity
  $100,534.81) — a ~$1,549 gap. **The breaker is understating drawdown by ~1.5 percentage
  points**, i.e. it would throttle (FULL→HALF at 8%) later than reality warrants.
- **Related spurious-trip (2026-05-19):** when `PENDING_BROKER` rows exist, the broker
  snapshot shows cash already debited for the order but the position not yet mirrored back
  → a cash-only view read a spurious ~74% drawdown, flipped the CB to HALF, and fired 5
  URGENT notifications for a non-event. (W21 review, Mistake 1.)

## What this changes

| File | Change |
|---|---|
| `lib/paper_sim.py` | New `position_meta.json` side-file: written on `open_position`, **never wiped** by `reconcile()`. `reconcile()` merges meta (stop/target) back into the rebuilt `positions.json`. New helper `pending_broker_count()`. |
| `lib/portfolio_health.py` | `assess_positions()` falls back to `position_meta.json` for stop/target when the live `positions.json` value is null (defense-in-depth: stops work even if the merge is skipped). |
| `prompts/routines/*.md` | **(separate companion PR — routines are PR-only.)** Where each routine calls `portfolio_risk.advance(...)`: pass broker-authoritative equity when `BROKER_PAPER=alpaca`; and skip the CB equity write when `paper_sim.pending_broker_count() > 0`. Documented here, not edited. |
| `CLAUDE.md` "Approved write paths" | Add `trades/paper/position_meta.json` (append/update) to the writable list. |

## Concrete fixes

### Fix 1 — `position_meta.json` side-file (stop/target persistence)

1. On `open_position(...)` ([lib/paper_sim.py:161](../../lib/paper_sim.py)), in addition to
   the log row, upsert `trades/paper/position_meta.json`:
   ```json
   { "UNH": { "stop_loss": 352.017, "take_profit": 488.9125, "entry_basis": 391.9044,
              "opened_at": "2026-05-19T20:42:20Z", "rationale_link": "decisions/.../UNH.json" } }
   ```
2. On `close_position(...)`, delete the symbol's key from the side-file.
3. In `reconcile()` ([lib/paper_sim.py:505](../../lib/paper_sim.py)), after rebuilding
   `positions.json` from the mirror, **merge** `position_meta.json` so `stop_loss`/`take_profit`
   are restored instead of `None`. The mirror remains authoritative for quantity/price; the
   side-file is authoritative for risk metadata.
4. **Defense-in-depth** ([lib/portfolio_health.py:52](../../lib/portfolio_health.py)): if
   `pos["stop_loss"]` is null, look up the symbol in `position_meta.json` before concluding
   "no stop." This keeps stops armed even if step 3 is missed.

### Fix 2 — circuit-breaker basis truth + PENDING_BROKER guard

1. Add `pending_broker_count() -> int` to `lib/paper_sim.py` (count rows with
   `status == "PENDING_BROKER"` not yet closed).
2. **Routine guidance (companion PR to `prompts/routines/*.md`):** before calling
   `portfolio_risk.advance(current_equity=E)`:
   - If `pending_broker_count() > 0`: **skip the CB equity write this run** (or use
     `paper_sim.portfolio_equity()` exclusively, never the broker cash snapshot) — prevents
     the 2026-05-19 spurious-HALF artifact.
   - Else, when `BROKER_PAPER=alpaca`: set `E =` broker-authoritative equity
     (`broker.account_snapshot().equity`) so the CB drawdown matches the number we report to
     the operator. The sim basis may still be logged for the reconciliation gap check, but it
     is no longer the breaker's truth.
3. Add an assertion/log line whenever `abs(sim_equity - broker_equity) > $500` so the
   sim-vs-broker basis gap (currently ~$1,549) is surfaced as a standing reconciliation item
   rather than silently diverging.

## Concrete routine inserts (companion PR — `prompts/routines/*.md` is PR-only)

Only two routines persist circuit-breaker equity — verified with
`grep -rln "portfolio_risk.advance" prompts/routines/` → **`market_open.md`** and
**`end_of_day.md`**. midday/pre_close read CB state read-only (no `advance()` call) and
need no change. Both target routines use the same shape, so apply the same edit to each:

- `prompts/routines/market_open.md` — around lines **50** and **70–71**
- `prompts/routines/end_of_day.md` — around lines **132–135**

**Current** (end_of_day; market_open is identical in shape):
```python
acct = broker.account_snapshot()
quotes = ...
equity = paper_sim.portfolio_equity(quotes, cash_balance=acct["cash"])
result = portfolio_risk.advance(equity, thresholds)
```

**Replace with:**
```python
# Guard 1 — orders in flight: the broker has debited cash for a pending order
# but the position isn't mirrored back yet, so any equity read is skewed.
# Skip the CB write this run (root cause of the 2026-05-19 spurious-HALF).
if paper_sim.pending_broker_count() > 0:
    # journal: "CB equity write skipped: N pending broker order(s) in flight";
    # do NOT call portfolio_risk.advance() — carry the prior CB state forward.
    pass
else:
    acct = broker.account_snapshot()
    quotes = ...
    sim_equity = paper_sim.portfolio_equity(quotes, cash_balance=acct["cash"])
    # Guard 2 — basis truth: under BROKER_PAPER=alpaca the broker account is
    # authoritative. Feeding sim equity understated drawdown on 2026-05-26
    # (CB read 1.93% vs broker 3.42%; ~$1,549 gap).
    equity = acct["equity"] if paper_sim.broker_mode() == "alpaca" else sim_equity
    result = portfolio_risk.advance(equity, thresholds)
    # Surface the basis gap as a standing reconciliation item, not a silent drift.
    if abs(sim_equity - equity) > 500:
        # journal/log: f"sim-vs-broker basis gap = ${sim_equity - equity:,.0f}"
        ...
```

Reviewer notes:
- `pending_broker_count()` and `broker_mode()` already exist in `lib/paper_sim.py` (PR #38).
- `broker.account_snapshot()` exposes both `equity` and `cash` (see `market_open.md:50`;
  equity figures already appear in the daily journals).
- No change to midday/pre_close (read-only CB) and no change to the sim-only path.

## CLAUDE.md approved-write-path addition

`lib.paper_sim` now writes `trades/paper/position_meta.json` beside `positions.json`. Add it
to the "Approved write paths" list so the write is explicitly sanctioned:
```
- `trades/paper/log.csv` (append-only), `trades/paper/positions.json`, and `trades/paper/position_meta.json`
```

## Test plan

- **Unit:** `open_position` → `position_meta.json` has the key with correct stop/target;
  `reconcile()` on a mirror payload with null stops → returned `positions.json` has stops
  restored from meta; `close_position` → key removed.
- **Unit:** `portfolio_health.assess_positions` with `positions.json` stop=null but meta
  present → breach is detected (regression test for the inert-stop bug; would have caught
  UNH).
- **Unit:** `pending_broker_count()` returns N for N PENDING_BROKER rows; 0 after fills.
- **Scenario:** replay 2026-05-19 (PENDING_BROKER rows present) → CB does NOT enter HALF.
- **Scenario:** replay 2026-05-26 close → CB drawdown reads 3.42% (broker basis), not 1.93%.
- All existing tests stay green (`tests/run_schema_validation.py` + suite).

## Out of scope (tracked, not fixed here)

- Stale daily-bar feed (engine ran on 2026-05-22 closes at the 2026-05-26 EOD) — separate
  data-plumbing item; it correctly *blocked* the WMT entry on 05-26 but means signals lag live marks.
- No live VIX feed (regime vol is a 20d realized-vol proxy; blocks `vix_high_observed` live gate).
- `archive_routine_logs.py` legacy-filename tolerance (`20260518_133639Z_*` aborts the archiver).
- De-dupe of the duplicated `regime_diversity_gates` block in `config/risk_limits.yaml` (config = human PR).
