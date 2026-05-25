# Risk Event — Stale Data (End of Day) — 2026-05-25

**Severity:** INFORMATIONAL (expected on a US market holiday)
**Routine:** `end_of_day`
**Timestamp:** 2026-05-25T20:44:00Z
**Mode:** PAPER_TRADING
**Trigger:** CLAUDE.md rule #5 — data stale beyond `risk_limits.yaml > data.max_data_staleness_seconds` (60 s).

## What happened

The `end_of_day` cron fires Mon–Fri at 16:30 ET. 2026-05-25 is a Monday, but the
US equity market is **CLOSED for Memorial Day**. There is no 2026-05-25 session,
so the deterministic engine's freshest daily bar is the **2026-05-22 (Friday)
close**, and `lib.broker.latest_quotes_for_positions()` re-serves the 05-22
closing prices. Measured staleness on the five open-position quotes is ~**72 h**
versus the 60-second cap — orders of magnitude over the limit.

Per CLAUDE.md rule #5, all affected symbols are forced to **NO_TRADE**. This is
the fourth stale-data gate trigger today after `pre_market` (market_closed),
`market_open`, `midday`, and `pre_close` — all clean NO-OPs holding the
05-22-validated book.

## Stale-data evidence

| Symbol | Last (05-22 close) | Source | Staleness |
|---|---|---|---|
| CSCO | 112.41 | broker re-serve of 05-22 | ~72 h |
| GLD  | 413.55 | broker re-serve of 05-22 | ~72 h |
| GOOGL| 406.80 | broker re-serve of 05-22 | ~72 h |
| UNH  | 370.75 | broker re-serve of 05-22 | ~72 h |
| XOM  | 162.33 | broker re-serve of 05-22 | ~72 h |

Latest deterministic daily bar across the universe = `2026-05-22T00:00:00Z`
(verified via `lib.data.get_bars(..., timeframe="1Day")`).

## Actions taken

- **Entries:** NONE. Signal evaluator produced ENTRY for CSCO/GLD/GOOGL/UNH/WMT/XOM
  on the 05-22 bar, but stale-data gate forbids opening on ~72 h-stale, non-session
  marks. WMT (the only ENTRY not already held) is deferred — re-confirm rank-5 on a
  fresh 05-26 bar.
- **Exits:** NONE. No held position carries an EXIT signal; closing on stale,
  non-session marks would be an uninformed exit. Capital preservation favors
  holding the 05-22-validated book (all five carry continue-to-hold).
- **Circuit-breaker:** State **FULL** (persisted 2026-05-22, DD 2.48%, peak
  $104,090.72). `portfolio_risk.advance()` deliberately NOT called — advancing on
  stale, non-session marks would stamp the breaker with a non-session timestamp.
  Read-only diagnostic reproduces the persisted 2.48% DD, ~5.52 pp headroom to the
  8% FULL→HALF trigger. No transition.
- **Reconciliation:** Clean — `paper_sim.reconcile()` → 5 open, 0 discrepancies
  (alpaca-authoritative); Alpaca-mirror in sync (5 positions match).

## Follow-up

- Renewed proposal (drafts only, `prompts/proposed_updates/` — NOT a config edit):
  a holiday-calendar short-circuit so future holiday Mondays exit before pulling
  stale quotes, across `end_of_day` and the three monitoring routines.
- Next authoritative evaluation + any paper fills run at the **2026-05-26**
  session. Re-pull fresh bars; thinnest stop cushions on the 05-22 marks are UNH
  (~4.86%) and CSCO (~5.79%); re-confirm WMT rank-5 before any entry.
