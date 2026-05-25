# Risk Event — Stale Market Data (midday routine)

- **Timestamp (UTC):** 2026-05-25T16:05:12+00:00
- **Routine:** midday (monitoring only)
- **Mode:** PAPER_TRADING
- **Severity:** informational (expected on a market holiday; no action taken)
- **Trigger:** CLAUDE.md safety rule #5 — market data staleness beyond
  `config/risk_limits.yaml > data.max_data_staleness_seconds` (60s).

## What happened

2026-05-25 is **Memorial Day — US equity markets are CLOSED**. The `midday`
cron fires Mon–Fri at 12:00 ET, and 2026-05-25 is a Monday, so the routine
launched; but there is no live session and therefore no fresh midday quotes.
This is the second monitoring pass today to hit the stale-data gate — the
earlier `market_open` pass logged the same condition
(`logs/risk_events/2026-05-25_133919_stale_data_market_open.md`).

All five open-position quotes returned by `lib.data.get_latest_quote()` are
stamped from the **last completed session, 2026-05-22 (Friday) 20:00 UTC** —
roughly **68.1 hours stale**, far beyond the 60-second limit:

| Symbol | Last (05-22 close) | quote_ts (UTC) | Staleness |
|---|---|---|---|
| CSCO | 112.41 | 2026-05-22T20:00:02Z | ~68.1 h |
| GLD  | 413.55 | 2026-05-22T20:00:27Z | ~68.1 h |
| GOOGL| 406.80 | 2026-05-22T20:00:00Z | ~68.1 h |
| UNH  | 370.75 | 2026-05-22T20:00:04Z | ~68.1 h |
| XOM  | 162.33 | 2026-05-22T20:00:00Z | ~68.1 h |

`fetched_ts` is current (~16:05 UTC today) but the underlying market data is the
Friday close; the feed simply re-serves the last session on a closed day.

## Decision

Per CLAUDE.md "Handling missing data" — *"Market data stale → NO_TRADE for affected
symbols; log to logs/risk_events/"* — and *"Any missing input is a reason to be more
conservative, never less"*:

- **No news scan acted upon.** A midday news scan requires sourced, fresh material
  that would invalidate a thesis; the routine constraint is explicit — *"No URL →
  no claim → no action."* No fresh session exists and no source URLs are available,
  so no news-driven invalidation is asserted. No `news_sentiment` dispatch produced
  an actionable, sourced item.
- **No health-check close possible.** There is no new session bar to compare against
  any stop/take-profit, so no stop/target invalidation can be detected. Closing on
  stale, non-session marks would be an uninformed exit; capital preservation favors
  holding the validated 05-22 book.
- **No PAPER_CLOSE proposed** (news-driven or stop/target).
- **Circuit-breaker NOT advanced/persisted.** A read-only mark on the stale 05-22
  closes reproduces the already-recorded equity ($101,510.01) and ~2.48% drawdown
  (peak $104,090.72) — well inside the 8% FULL→HALF trigger. Calling
  `portfolio_risk.advance()` would stamp the breaker with a non-session timestamp on
  stale data, so it was deliberately skipped. CB state remains **FULL** as last
  persisted 2026-05-22. No transition.
- **No new positions** (forbidden by routine + monitoring-only mandate regardless).

## Daily-loss limit recheck (midday constraint)

There is **no authoritative session PnL today** — the market is closed, so no
intraday equity path and no today-PnL can be computed. The persisted equity
($101,510.01) is the re-marked Friday close, not a new value. Therefore no
daily-loss breach is computable against `max_daily_loss_usd=$500`,
`max_daily_loss_pct=0.5%`, or `daily_drawdown_halt_pct=2.0%`. The
`halt_after_daily_limit_breach` condition is **not** triggered; no "close all
positions" proposal and no `*_daily_loss.md` event warranted.

## Position context (from last good close, 05-22 — reference only)

All five holdings carried an ENTRY/continue-to-hold signal on the 05-22 evaluation
and none was near its −10% strategy-default stop. Read-only uPnL on the 05-22 marks
vs the alpaca-mirror entry basis in `positions.json`: CSCO −$682.96, GLD +$54.29,
GOOGL +$424.08, UNH −$825.02, XOM +$184.50 (net −$845.10) — informational only;
this is not today's PnL. Reconciliation clean: 5 open, 0 discrepancies
(alpaca-authoritative).

## Next action

No EOD evaluation runs today (closed). The next deterministic evaluation and any
paper fills occur at the **2026-05-26** session. Re-pull fresh bars then; re-confirm
cushions on XOM/GOOGL and the SPY 10-month-SMA trend filter.
