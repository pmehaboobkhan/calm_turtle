# Proposed update — EOD daily-bar staleness gate + PENDING_BROKER finalizer gap

**Author:** Claude (assistant), human-directed (operator asked to investigate a "stale data issue" on 2026-06-03 EOD)
**Date:** 2026-06-03
**Status:** DRAFT — awaiting human PR review. No protected file edited; no trade placed.
**Scope:** `lib/` code change (Fix 1) + `config/risk_limits.yaml` *or* `prompts/routines/end_of_day.md` change (Fix 2) + `prompts/routines/end_of_day.md` change (Fix 3). All PR-locked; this memo proposes, does not implement.

## Reason

Three concrete defects observed across the last three trading sessions, each
self-documented in `logs/risk_events/` and `logs/routine_runs/`:

1. **Daily-bar staleness gate is structurally unsatisfiable at EOD.** Every
   ENTRY signal on 2026-06-01, 06-02, 06-03 EOD was forced to `NO_TRADE`
   (reason `data_stale`). The trip is correct per CLAUDE.md rule #5, but the
   gate it trips against (`max_data_staleness_seconds: 60`) is designed for
   live quotes and can never be satisfied by a daily-bar feed: by the time the
   provider settles "today's close" into the daily bars, the bar's timestamp
   is already minutes-to-hours old. EOD is now a permanent NO_TRADE for new
   entries, not by design but by configuration mismatch.

2. **`PENDING_BROKER` rows have no finalizer.** Seven BUY breadcrumbs
   accumulated 2026-05-18 → 2026-05-22 while `BROKER_PAPER=alpaca` was active.
   The Alpaca orders themselves have long since settled (positions are
   actually flat, broker confirms 0 positions / $100,577.97 cash, `reconcile()`
   reports `0 discrepancies`). But `paper_sim.pending_broker_count()` still
   returns `7` because the only mechanism that decrements it is a fresh
   `_RESET_` marker. `confirm_moc_fills()` exists for `PENDING_MOC` rows
   (lib/paper_sim.py:467) but no analog exists for `PENDING_BROKER`. Guard-1
   has therefore disabled the CB equity write on every routine since 2026-05-18
   — the portfolio-drawdown safety control reports the carry-forward state
   (`FULL`/throttle `1.0`, peak from 2026-05-29) and never re-evaluates.

3. **EOD prompt doesn't enforce CLAUDE.md's risk-event-log requirement for
   stale data.** CLAUDE.md "Handling missing data" says: "Market data stale
   → `NO_TRADE` for affected symbols; log to `logs/risk_events/`." The
   2026-06-01 and 06-02 EOD runs wrote
   `logs/risk_events/<date>_stale_data_eod.md` voluntarily. The 06-03 EOD
   stamped staleness in the decision file's `data_freshness` field and in the
   audit `notes:` but **did not write a `logs/risk_events/` file** — only the
   journal got it. This is a compliance gap, not a regression: `end_of_day.md`
   currently enumerates explicit triggers for risk-event files (signal
   conflicts, CB transitions, reconcile divergence, mirror divergence) but
   does NOT enumerate stale-data.

### Live exposure right now

- 3 consecutive sessions of zero new entries despite 6+ ENTRY signals per run.
  Strategy capital is sitting in cash, paying no opportunity cost but also
  not deployed against the deterministic signals the system was built to act
  on.
- CB has not refreshed equity since 2026-05-29. If the portfolio re-deploys
  capital before Issue #2 is cleared, the drawdown safety control is operating
  blind on a 5-day-old baseline.
- The 06-03 stale-data event is documented only in the journal — audit-trail
  bookkeeping (`logs/risk_events/`) is incomplete compared to 06-01 and 06-02.

## What this changes

| File | Change | PR class |
|---|---|---|
| `lib/paper_sim.py` | Add `confirm_broker_fills()` — symmetric to `confirm_moc_fills()`, finalizes `PENDING_BROKER` rows by querying broker for terminal status + writing terminal mirror-back row. | `lib/` — direct PR. |
| `prompts/routines/end_of_day.md` (or `market_open.md`) | Call `paper_sim.confirm_broker_fills()` once per session before the Guard-1 check, so pending counts decay naturally as broker fills/cancels arrive. | Prompt — PR-only. |
| `config/risk_limits.yaml` (Option A) | Add `data: max_daily_bar_age_hours: 36` alongside `max_data_staleness_seconds`. Apply the seconds gate to live-quote data, apply the hours gate to daily-bar data. | Config — PR-only. |
| `prompts/routines/end_of_day.md` (Option B, instead of Option A) | Move EOD execution to 17:00 ET so the daily-bar provider has time to settle the same-day close. | Prompt — PR-only. |
| `prompts/routines/end_of_day.md` (Fix 3) | Add explicit step: "if any decision written this run has `reason: data_stale`, write `logs/risk_events/<ts>_stale_data_eod.md` summarizing affected symbols, latest bar date, staleness factor, and CB state." | Prompt — PR-only. |

## Concrete fixes

### Fix 1 — `confirm_broker_fills()` (lib/paper_sim.py)

Mirror the shape of `confirm_moc_fills()` (lib/paper_sim.py:467).

```python
def confirm_broker_fills() -> dict:
    """Resolve PENDING_BROKER rows by querying the broker for terminal status.

    For each PENDING_BROKER row after the latest RESET marker that hasn't
    already been finalized: look up the order at the broker and, if it's in a
    terminal state (filled / canceled / expired / rejected), append a terminal
    mirror-back row recording the outcome. After this runs once per session,
    pending_broker_count() decays naturally as broker orders settle.

    Returns {'confirmed': [...], 'rejected': [...], 'still_pending': [...]}.
    Safe to call in sim mode (no-op).
    """
    summary = {"confirmed": [], "rejected": [], "still_pending": []}
    if broker_mode() != "alpaca":
        return summary
    # ... (read rows after last RESET, find PENDING_BROKER with no terminal
    #      counterpart in notes "broker_confirmed_*" or "broker_rejected_*",
    #      call broker.get_order(oid), branch on status.lower():
    #        - "filled":   append OPEN row (open side) / CLOSED row (close side)
    #                      with broker fill price + realized PnL if applicable;
    #                      update positions.json on open, drop on close.
    #        - "canceled"/"expired"/"rejected":
    #                      append REJECTED row noting the terminal status; do
    #                      NOT touch positions.json (the order never landed).
    #        - else:       append to still_pending.)
```

Notes:
- The function should be **idempotent** — running twice in a row produces no
  double-fills. Use a marker token in `notes:` (`broker_confirmed order_id=...`
  / `broker_rejected order_id=...`), same pattern as `confirm_moc_fills()` uses
  for `moc_confirmed` / `moc_rejected`.
- Care needed for **close-side fills**: a `PENDING_BROKER` `CLOSE` row that
  finalizes as `filled` should produce a `CLOSED` row with realized PnL
  computed against the recorded entry price, and `positions.json` should
  drop the symbol. This matches the sim-mode close path but uses the broker
  fill price.
- In **alpaca mode**, `reconcile()` is already the authoritative position
  source (lib/paper_sim.py:628+). `confirm_broker_fills()` is the journal-side
  catch-up: it writes the log rows that should have been there, so future
  routines see a clean count.

### Fix 2 — daily-bar staleness gate (pick one)

**Option A — split the freshness gate by data class (preferred).**

Add to `config/risk_limits.yaml > data`:

```yaml
data:
  max_data_staleness_seconds: 60      # applies to live quotes (intraday)
  max_daily_bar_age_hours: 36         # applies to daily-bar source basis
```

In the freshness check (Risk Manager hard-check #11 / `lib.data.get_bars`
callers), when the data basis is a *daily bar*, compare against the hours
gate instead of the seconds gate. Rationale: a daily bar can only be as
fresh as the provider's last settlement; 36h covers normal EOD execution and
a single-session provider lag, but trips on a multi-session outage which is
the case the gate is supposed to catch.

**Option B — move EOD execution to 17:00 ET.**

In `prompts/routines/end_of_day.md`, change the recommended cron from ~16:30
to 17:00 (or 17:15) ET. By then most daily-bar providers (yfinance, IEX
end-of-day) have settled the same-day close, so today's daily bar is in the
feed and the existing 60s gate compares against `now() - today_close_ts`,
which is single-digit minutes.

**Trade-off:** A is config-only and surgical. B is operator-friendly but
gives up half an hour of post-close decision time and depends on provider
SLAs we don't control. Recommend A.

### Fix 3 — EOD prompt should enforce CLAUDE.md's stale-data audit rule

In `prompts/routines/end_of_day.md`, after the decisions step, add:

> If any decision written this run has `reason: data_stale`, write
> `logs/risk_events/<YYYY-MM-DD>_<HHMMSS>_stale_data_eod.md` with: trigger
> (latest bar date + age vs gate), affected symbols, decision IDs, and any
> compounding factors (CB write skipped, PENDING_BROKER count). This is
> required by CLAUDE.md "Handling missing data" and is not optional.

This restores parity with the 2026-06-01 and 06-02 voluntary writes and
makes the audit trail consistent.

## Operator action (not in this memo's PR scope)

Independent of the fixes above, the existing 7-row PENDING_BROKER backlog
needs to be cleared once. Until `confirm_broker_fills()` lands, the only
mechanism is `scripts/sync_alpaca_state.py --reset-fresh-start` (writes a
new `_RESET_` marker, which is what `pending_broker_count()` honors). That
script requires `ALPACA_PAPER_KEY_ID` / `ALPACA_PAPER_SECRET_KEY` in the
environment — must be run on the cloud cron env where credentials live, not
a fresh local terminal.

Recommended sequence:
1. In cloud cron env: `python3 scripts/sync_alpaca_state.py` (default
   `--check`, read-only). Confirms Alpaca state matches expectation
   (0 positions, 0 open orders, equity ≈ $100,577.97).
2. If check is clean: `python3 scripts/sync_alpaca_state.py
   --reset-fresh-start`. Cancels any open Alpaca orders (expected: none),
   appends `_RESET_` marker, resets CB `peak_equity` from current Alpaca
   equity (loses the prior $104,090.72 peak — accept, since we've been flat
   since 2026-05-29 and a fresh peak from the current cash baseline is
   defensible).
3. Verify: next routine should log `pending_broker_count() == 0` and resume
   CB equity writes.

## Test plan

- **Unit (Fix 1):** seed a log with one `PENDING_BROKER` BUY whose `oid`
  reports `filled` at the broker → `confirm_broker_fills()` writes an `OPEN`
  row, updates `positions.json`, idempotent on second call. Same shape for
  `canceled`/`rejected`/`expired`.
- **Unit (Fix 1):** `confirm_broker_fills()` in `BROKER_PAPER=sim` → returns
  empty summary, writes nothing.
- **Unit (Fix 2A):** daily bar dated yesterday (~20h old) at 16:40 ET →
  `data_freshness.status` PASSES (under 36h gate); daily bar dated
  2 trading days ago → FAILS. Live quote age `>60s` → still FAILS via the
  seconds gate.
- **Scenario (Fix 3):** simulate a stale-data EOD → confirm the routine
  writes `logs/risk_events/<ts>_stale_data_eod.md` matching the format used
  on 06-01/06-02.
- All existing tests stay green.

## Out of scope (tracked, not fixed here)

- The 2026-05-26 `alpaca_mirror_state_integrity.md` memo's MUST-FIX items
  (stop persistence via `position_meta.json`, CB basis truth). Those are a
  separate PR; this memo does not duplicate them.
- Whether `BROKER_PAPER=alpaca` should be re-enabled at all (per the memory
  note `project_alpaca_moc_blocker.md`, `sim` is the validated interim).
  Fix 1 makes Alpaca-mirror mode safer when it IS active, but the decision to
  flip it on is separate and operator-only.
- Live VIX feed (regime vol still a 20d realized-vol proxy).
- Archive script's tolerance for legacy log filenames (noted in 06-03 EOD
  audit; non-fatal).
