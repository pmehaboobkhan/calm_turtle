# Risk Event — Stale Market Data (pre_close routine)

- **Timestamp (UTC):** 2026-05-25T19:38:15+00:00
- **Routine:** pre_close (monitoring only)
- **Mode:** PAPER_TRADING
- **Severity:** informational (expected on a market holiday; no trade action taken)
- **Trigger:** CLAUDE.md safety rule #5 — market data staleness beyond
  `config/risk_limits.yaml > data.max_data_staleness_seconds` (60s).

## What happened

2026-05-25 is **Memorial Day — US equity markets are CLOSED**. The `pre_close`
cron fires Mon–Fri at 15:30 ET, and 2026-05-25 is a Monday, so the routine
launched; but there is no live session and therefore no fresh late-day quotes.
This is the **third** monitoring pass today to hit the stale-data gate — the
earlier `market_open` and `midday` passes logged the same condition
(`logs/risk_events/2026-05-25_133919_stale_data_market_open.md`,
`logs/risk_events/2026-05-25_160512_stale_data_midday.md`).

All five open-position quotes returned by `lib.data.get_latest_quote()` are
stamped from the **last completed session, 2026-05-22 (Friday) 20:00 UTC** —
roughly **71.6 hours stale**, far beyond the 60-second limit:

| Symbol | Last (05-22 close) | quote_ts (UTC) | Staleness |
|---|---|---|---|
| CSCO | 112.41 | 2026-05-22T20:00:02Z | ~71.64 h |
| GLD  | 413.55 | 2026-05-22T20:00:27Z | ~71.63 h |
| GOOGL| 406.80 | 2026-05-22T20:00:00Z | ~71.64 h |
| UNH  | 370.75 | 2026-05-22T20:00:04Z | ~71.64 h |
| XOM  | 162.33 | 2026-05-22T20:00:00Z | ~71.64 h |

`fetched_ts` is current (~19:38 UTC today) but the underlying market data is the
Friday close; the feed simply re-serves the last session on a closed day.

## Overnight-risk overlay (run despite stale data — flag-only)

The pre_close mandate is to cap overnight risk on catalysts we can see coming.
Closing on stale, non-session marks is forbidden (uninformed exit), but an
informed overnight-risk *scan* is still valuable for the journal and the EOD
05-26 handoff. The scan covered the next live session (2026-05-26) and is
**clean** of material catalysts on every open name:

**Earnings (next-trading-day window, per `holding_earnings_caution_window_days` ≈ 1):**
- CSCO — last reported 2026-05-13 AMC; next ~Aug 11–14, 2026. No earnings in window.
- GOOGL — reported Q1 late Apr 2026; next ~Jul 23–28, 2026. No earnings in window.
- UNH — reported 2026-04-21; next ~Jul 10, 2026. No earnings in window.
- XOM — reported 2026-05-01; next ~Jul 31, 2026. No earnings in window.
- GLD — gold ETF; no top-holding-earnings concept. N/A.

This **confirms clear** the pre-market journal's flagged "earnings calendar
unconfirmed for the 05-26/05-27 window" — no held name reports next session.

**Macro (calendar-A: FOMC, NFP, CPI, GDP, retail sales), 2026-05-26:**
- Scheduled 05-26: Consumer Confidence, Philly Fed Non-Manufacturing, Dallas Fed
  Manufacturing — none are calendar-A events. No FOMC / NFP / CPI / GDP / retail
  sales on the next trading day.
- GDP 2nd release + PCE land 2026-05-28 (Thursday) — two sessions out, outside
  the next-trading-day window. Noted as a watch-item, not a close trigger.

Sources: marketbeat.com (CSCO/GOOGL/UNH/XOM earnings dates), SEC EDGAR 8-Ks,
investor.cisco.com, investor.exxonmobil.com, bls.gov schedule, tradingeconomics.com
US calendar.

## Decision

Per CLAUDE.md "Handling missing data" — *"Market data stale → NO_TRADE for affected
symbols; log to logs/risk_events/"* — and *"Any missing input is a reason to be more
conservative, never less"*:

- **No PAPER_CLOSE proposed.** Two independent reasons: (1) stale data — closing on
  the re-served Friday close would be an uninformed, non-session exit; (2) the
  overnight-risk scan found **no material catalyst** on any open position for the
  next live session, so no close would be warranted even with fresh data.
- **No new positions** (forbidden by routine + monitoring-only mandate regardless).
- **Circuit-breaker NOT advanced/persisted.** A read-only mark on the stale 05-22
  closes reproduces equity (~$101,510 prior persisted) and ~2.48% drawdown vs peak
  $104,090.72 — well inside the 8% FULL→HALF trigger (~5.5pp headroom). Calling
  `portfolio_risk.advance()` would stamp the breaker with a non-session timestamp on
  stale data, so it was deliberately skipped. CB state remains **FULL** as last
  persisted 2026-05-22. No transition.

## Position context (from last good close, 05-22 — reference only)

All five holdings carried a continue-to-hold signal on the 05-22 evaluation and
none is near its −10% strategy-default stop (thinnest cushions above stop:
UNH +4.86%, CSCO +5.79%). Read-only uPnL on the 05-22 marks vs the alpaca-mirror
entry basis in `positions.json`: CSCO −$682.96, GLD +$54.29, GOOGL +$424.08,
UNH −$825.02, XOM +$184.50 (net −$845.10) — informational only; this is not
today's PnL. Reconciliation clean: 5 open, 0 discrepancies (alpaca-authoritative).

## Next action

No EOD evaluation runs today (closed). The next deterministic evaluation and any
paper fills occur at the **2026-05-26** session. Re-pull fresh bars then; re-confirm
cushions on XOM/GOOGL and the SPY 10-month-SMA trend filter, and re-verify the
overnight calendar before that session's own close.
