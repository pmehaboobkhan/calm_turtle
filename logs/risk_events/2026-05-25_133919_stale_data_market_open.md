# Risk Event — Stale Market Data (market_open routine)

- **Timestamp (UTC):** 2026-05-25T13:39:19+00:00
- **Routine:** market_open (monitoring only)
- **Mode:** PAPER_TRADING
- **Severity:** informational (expected on a market holiday; no action taken)
- **Trigger:** CLAUDE.md safety rule #5 — market data staleness beyond
  `config/risk_limits.yaml > data.max_data_staleness_seconds` (60s).

## What happened

2026-05-25 is **Memorial Day — US equity markets are CLOSED**. The `market_open`
cron fires Mon–Fri, and 2026-05-25 is a Monday, so the routine launched; but there
is no live session and therefore no fresh opening quotes.

All five open-position quotes returned by `lib.broker.latest_quotes_for_positions()`
are stamped from the **last completed session, 2026-05-22 (Friday) 20:00 UTC** —
roughly **65.6 hours stale**, far beyond the 60-second limit:

| Symbol | Last (05-22 close) | quote_ts (UTC) | Staleness |
|---|---|---|---|
| CSCO | 112.41 | 2026-05-22T20:00:02Z | ~65.65 h |
| GLD  | 413.55 | 2026-05-22T20:00:27Z | ~65.64 h |
| GOOGL| 406.80 | 2026-05-22T20:00:00Z | ~65.65 h |
| UNH  | 370.75 | 2026-05-22T20:00:04Z | ~65.65 h |
| XOM  | 162.33 | 2026-05-22T20:00:00Z | ~65.65 h |

(The exact prices differ slightly from the pre-market report's 05-22 closes because
this routine pulled the latest IEX ask/bid mid rather than the official close; both
are nonetheless the 05-22 session and equally stale for intraday-monitoring purposes.)

## Decision

Per CLAUDE.md "Handling missing data" — *"Market data stale → NO_TRADE for affected
symbols; log to logs/risk_events/"* — and *"Any missing input is a reason to be more
conservative, never less"*:

- **No overnight gap evaluation is possible** — there is no new session bar to compare
  against any stop/take-profit, so no gap can be detected or acted upon.
- **No PAPER_CLOSE proposed.** Closing on stale, non-session marks would be an
  uninformed exit; capital preservation favors holding the validated 05-22 book.
- **Circuit-breaker NOT advanced/persisted.** A read-only mark on the stale 05-22
  closes reproduces the already-recorded equity ($101,510.01) and ~2.48% drawdown
  (peak $104,090.72) — well inside the 8% FULL→HALF trigger. Calling
  `portfolio_risk.advance()` would stamp the breaker with a non-session timestamp on
  stale data, so it was deliberately skipped. CB state remains **FULL** as last
  persisted 2026-05-22.
- **No new positions** (forbidden by routine + monitoring-only mandate regardless).

## Position context (from last good close, 05-22 — reference only)

All five holdings carried an ENTRY/continue-to-hold signal on the 05-22 evaluation and
none was near its −10% strategy-default stop. Thinnest cushions on 05-22 were XOM
(~6.8%) and GOOGL (~7.0%) — both still comfortably above the stop. No invalidation
was pending.

## Next action

No EOD evaluation runs today (closed). The next deterministic evaluation and any
paper fills occur at the **2026-05-26** session. Re-pull fresh bars then; re-confirm
cushions on XOM/GOOGL and the SPY 10-month-SMA trend filter.
