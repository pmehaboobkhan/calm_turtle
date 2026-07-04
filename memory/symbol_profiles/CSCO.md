# Symbol Profile — CSCO

> Descriptive observations only. No advice, no forward recommendations. Append-only per period.

## Week 2026-W20 observations
- Strategy: large_cap_momentum_top5. Entry 2026-05-12 @ $91.6483 (65 sh); exit 2026-05-13 pre_close @ $101.1698. Held 1 day. Realized +$618.90 (+10.13%).
- Exited pre-emptively ahead of Q3 FY26 earnings (AMC 2026-05-13) per the earnings-exit playbook; this was the only closed trade of the first paper-trading week.
- Post-print IEX last ≈ $121.25 with a wide bid/ask ($109.35/$121.25), suggesting a ~20% gap up; the stock closed below $121 by EOD. The exit captured +10.13% but did not capture catalyst-day continuation above the exit price — the expected, accepted trade-off of the earnings-exit strategy.
- Momentum rank: 3/21 sustained throughout the week. Even on the 2026-05-15 data-blackout day, CSCO would have been rank 3 had data been available.
- Post-exit re-entry was blocked every session (CB OUT + data staleness + post-earnings-stale-bar). Re-entry never executed; the chain was reset-terminated on 2026-05-15.
- Largest single-session gap surprise of the week (~20% post-earnings move on IEX).

## Week 2026-W21 observations
- Strategy: large_cap_momentum_top5. Re-entered the book this week: PAPER_BUY submitted 2026-05-18 @ ref $118.21, filled 2026-05-19 open @ $117.6635 (−$0.55/sh favorable slip), 130 sh via the alpaca mirror. Held all week; carried over the Memorial Day weekend into 2026-05-26 (still open).
- Momentum rank: rank 1/21 throughout the week (6m return ~+61.56% at entry, ~+54.42% on the 2026-05-22 scan — the highest in the watchlist all week). The post-earnings-gap-momentum (rank-1) durability question opened in W20 carried into W21 unresolved; no mean-reversion toward the −10% stop ($106.389) observed during the window.
- This is the second consecutive week CSCO led the Strategy-B slate (W20 rank 3 cash-only via reset; W21 rank 1, the durable leader). Old-tier networking-tech leadership noted descriptively in the regime narrative.
- Stop/target fields recorded as null on the position all week under the alpaca-mirror reconcile (stop_loss=null, take_profit=null in positions.json) — stop monitoring was advisory/manual; descriptive standing observation (HIGH severity in the cycle report).
- No earnings catalyst in the window (Q3 FY26 print was 2026-05-13, pre-reset). No EXIT signal fired.

## Week 2026-W22 observations
- Strategy: large_cap_momentum_top5. Carried 130 sh from the W21 entry @ $117.6635 into the W22 window (holiday Mon 2026-05-25).
- Closed 2026-05-29 pre_close @ $121.17. Realized PnL: +$456 (+2.98% vs entry). Closed by the all-positions daily-loss halt, NOT by a stop or rotation signal.
- Momentum rank: remained #1 throughout W22 (6m +57–61%) — the strongest and most persistent name in the book for a third consecutive week.
- The single-name thesis was intact at exit; the position was liquidated by the system-level halt while leading the Strategy-B slate.
- News: BofA price-target raise to $135 (2026-05-29) confirmed ongoing analyst bullishness — closed mid-upgrade cycle.
- No earnings catalyst in the W22 window (Q3 FY26 print was 2026-05-13; next ~2026-08-12).
- Pattern (descriptive): rank-1 persistence is high; CSCO did not rotate out of the top-5 in any W22 session. It held through the crude/energy selloff without adverse impact (CSCO is networking/tech, not energy-correlated) and was one of three W22 winners alongside GLD and the prior NVDA close. The W20/W21 open question on whether CSCO rank-1 momentum durably persists or reverts late in the hold remains open — three weeks of leadership with no mean-reversion toward the stop, but the position was always closed by exogenous events (reset, then halt), never allowed to run to a natural rotation.

## Week 2026-W27 observations
- Strategy: large_cap_momentum_top5. Position (BUY 46 @ entry $123.7893, W23-era entry) was **closed 2026-07-01 market_open** on a deterministic stop-loss breach @ ~$117.18. Realized −$304 (−5.3%). Full gate chain APPROVED.
- Descriptive: this was the run's **marginal / lowest-confidence exit** — on fresh tight-spread prints CSCO straddled the $117.00 stop within ±0.25% (116.85–117.26); an earlier $116.38 sub-stop print was on a dislocated ~5.4% IEX spread. `portfolio_health` (the deterministic authority) flagged the breach and the majority of clean prints were below $117.00; the exit honored the pre-committed stop rather than hoping for reversion.
- Post-exit ex-post correctness of the marginal call is **UNRESOLVED** — no trustworthy fresh close printed 07-01→07-03 (stale bars + holiday); deferred to >= 2026-07-06.
- Context: CSCO had been the most persistent Strategy-B leader (rank-1 across W21/W22) and was a W22 winner (+$456). This is its first stop-loss exit of the paper period; prior closes were exogenous (reset, daily-loss halt). No CSCO-specific thesis break was cited — a mechanical stop honor amid a broad stale-data-frozen entry environment.
- Re-entries blocked all week (07-02 / 07-03 NO_TRADE) by stale daily bars (CLAUDE.md #5), despite CSCO re-firing rank-1 momentum (+53.68% 126d).
