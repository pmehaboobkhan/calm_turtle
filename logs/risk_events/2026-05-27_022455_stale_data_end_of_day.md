# Risk Event — Stale Entry Data (End of Day) — 2026-05-27

**Severity:** INFORMATIONAL (signal evaluator ran; entry gated by staleness)
**Routine:** `end_of_day`
**Timestamp:** 2026-05-27T02:24:55Z
**Mode:** PAPER_TRADING
**Trigger:** CLAUDE.md rule #5 — daily-bar data driving ENTRY signals is stale
beyond `risk_limits.yaml > data.max_data_staleness_seconds` (60 s).

## What happened

The deterministic engine's freshest daily bar across the universe is stamped
**2026-05-26T00:00:00Z** — measured age **~95,062 s (~26 h)** versus the 60-second
cap, three orders of magnitude over the limit. The daily-bar feed is lagging the
live IEX quote feed: live quotes are current and diverge materially from the
05-26 daily closes, confirming the daily bars are not today's marks.

| Symbol | Daily close (05-26) | Live IEX quote | Divergence |
|---|---|---|---|
| AMZN  | 265.29 | 276.08 | +4.1% |
| SPY   | 750.59 | 772.70 | +2.9% |
| CSCO  | 118.33 | 124.34 | +5.1% |
| GLD   | 414.00 | 414.25 | +0.1% |
| GOOGL | 388.88 | 403.57 | +3.8% |
| XOM   | 149.81 | 158.17 | +5.6% |
| UNH   | 376.86 | 359.67 (bid; ask 0.0 glitch) | -4.6% |

Latest deterministic daily bar across the universe = `2026-05-26T00:00:00Z`
(verified via `lib.data.get_bars(..., timeframe="1Day")`).

## Actions taken

- **Entries:** NONE opened. The signal evaluator produced ENTRY for
  CSCO/GLD/GOOGL/UNH/XOM (all already held) and **AMZN** (rank 5, the only ENTRY
  not already held — NVDA slipped to rank 6 / NO_SIGNAL hold-zone). AMZN was
  REJECTED on TWO independent hard checks: (1) the 2026-05-26 close breached the
  daily-loss limit (-$614.25 / -0.607%) so `halts.halt_after_daily_limit_breach`
  + `cool_off_days_after_halt=1` keep today inside the de-risk cool-off window —
  no exposure expansion; (2) this stale-entry-bar gate. Decision:
  `decisions/2026-05-27/0224_AMZN.json` (final_status REJECTED).
- **Exits:** NONE. No held position carries an EXIT signal; closing on stale
  daily marks would be an uninformed exit. All five held names (CSCO/GLD/GOOGL/
  UNH/XOM) re-confirm ENTRY/hold and none breached its -10% rotation stop on the
  original entry basis (UNH thinnest, ~+1.97% above its $352.71 stop on live bid
  359.67). Capital preservation favors holding the validated book.
- **Circuit-breaker:** Equity write SKIPPED this run — `pending_broker_count()=2`
  (see CB-skip note below). Prior state **FULL** (peak $104,090.72) carried
  forward; throttle 1.0. `portfolio_risk.advance()` was NOT committed.
- **Reconciliation:** Clean — `paper_sim.reconcile()` → 5 open, 0 discrepancies
  (alpaca-authoritative); Alpaca-mirror in sync (5 positions match).

## Circuit-breaker skip (pending broker orders)

`pending_broker_count()` returned **2**, so per `end_of_day.md` step 5 the CB
equity write was skipped and the prior FULL state (throttle 1.0) carried forward.
The two "pending" rows are STALE log artifacts, not genuine in-flight orders:
they are the PENDING_BROKER *open* rows for **WMT** (order
`3464ba97...`, FILLED at broker, subsequently CLOSED 05-20) and **NVDA** (order
`14d3ade1...`, FILLED at broker, subsequently CLOSED 05-26). Both symbols are
FLAT at the broker and absent from `positions.json`; the open rows were never
finalized in the local CSV after their round-trips completed. The position-level
ledger reconciles cleanly (5 positions match local + broker), so this is a
cosmetic ledger artifact — but it correctly trips the conservative CB-skip guard
(the 2026-05-19 spurious-HALF protection). No risk event escalation, no Telegram
for the CB; recorded here for the audit trail. A drafts-only follow-up
(`prompts/proposed_updates/`) should propose reconciling stale round-trip
PENDING_BROKER rows to a terminal status so the guard isn't tripped by completed
trades.

## Follow-up

- Drafts-only proposal (`prompts/proposed_updates/` — NOT a config edit): wire a
  daily-bar freshness short-circuit + finalize stale round-trip PENDING_BROKER
  rows to a terminal CLOSED/SUPERSEDED status during reconcile, so completed
  trades stop tripping the CB-skip guard.
- Next authoritative evaluation + any paper fills run at the **2026-05-28**
  session (GDP 2nd release + PCE deflator — a non-benign macro window). Re-pull
  fresh daily bars; re-confirm AMZN rank-5 before any entry; verify the
  daily-loss-breach cool-off has elapsed.
