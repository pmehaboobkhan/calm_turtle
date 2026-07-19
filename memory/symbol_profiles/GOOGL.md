# Symbol Profile — GOOGL

> Descriptive observations only. No advice, no forward recommendations. Append-only per period.

## Week 2026-W20 observations
- Strategy: large_cap_momentum_top5. Entry 2026-05-12 @ $397.9096 (15 sh). Held 2026-05-12 → 2026-05-15. Reset-terminated 2026-05-15T00:31:53Z (no signal invalidation).
- Momentum rank: 1/21 all week, the widest margin among the top-5 (+35–38% 6m return; next-ranked XOM ~+27.7%). Most stable rank position in the book.
- Intraday MTM volatility was material on 2026-05-13: pre_close intraday high ≈ $402.96, EOD 2026-05-13 close $382.23 (a sharp same-session reversal). Recovered to $401.68 by 2026-05-14 EOD.
- One-day MTM swing range observed roughly −$159 to +$57 against the position; remained well clear of the −10% stop ($358.05) at all points (headroom 6.3%–10.9% over the window).
- Fundamental backdrop constructive: Q1 2026 earnings already reported (rev $109.9B beat $107.2B; Cloud +63%); positive news flow (Anthropic/Google Cloud deal, Googlebook launch) during the week.

## Week 2026-W21 observations
- Strategy: large_cap_momentum_top5. PAPER_BUY submitted 2026-05-18 @ ref $396.78, filled 2026-05-19 open @ $395.64 (−$1.14/sh favorable slip), 38 sh. Held all week; carried over the Memorial Day weekend into 2026-05-26 (still open).
- Momentum rank: rank 2/21 throughout (6m ~+38.58% at entry, ~+36.55% on the 2026-05-22 scan). Stable rank-2 position; did not slip below the rank-7 hold zone.
- Flagged on 2026-05-20 as one of two late-day-weakness names (intraday mark −6.89%, approaching but NOT breaching the −10% stop $357.102); recovered into week-end as portfolio DD fell from 4.34% (05-21) to 2.36% (05-22). The thin-cushion-name watch did not progress to a stop event.
- Stop/target fields recorded as null on the position all week under the alpaca-mirror reconcile; stop cushion was monitored as an advisory mark only — descriptive standing observation (HIGH severity in the cycle report).
- No earnings or single-stock catalyst in the window. No EXIT signal fired.

## Week 2026-W22 observations
- Strategy: large_cap_momentum_top5. Carried 38 sh from the W21 entry @ $395.64 into the W22 window (holiday Mon 2026-05-25).
- Closed 2026-05-29 pre_close @ $382.62. Realized PnL: −$495 (−3.29% vs entry). Closed by the all-positions daily-loss halt, NOT by a stop or rotation signal.
- Momentum rank: 2/21 through most of W22 (briefly rank 3 on some sessions).
- Weakest-held name on 2026-05-28 EOD (−$1,040 unrealized, +3.4% above stop); flagged as the GOOGL-DRAWDOWN-WATCH name. The stop ($356.08) was never breached — at the 05-29 close GOOGL sat +7.5% above the stop.
- News backdrop: DOJ antitrust behavioral remedies (announced 09-2025) with no new 05-26→05-29 development; Q1 2026 earnings past (April); TPU monetization noted as bullish background. No name-specific invalidation event in W22.
- Pattern (descriptive): GOOGL has been a persistent rank-2 name across W20–W22. The −3.29% W22 loss is well below the thesis-invalidating level; the stop was never close to breaching. The drawdown-watch flag tracked relative weakness correctly (GOOGL was the 2nd-largest dollar loss this week) but did not become the operative exit trigger — the halt did.

## Week 2026-W28 observations
- Strategy: large_cap_momentum_top5. Held all five sessions (07-06 → 07-10); 16 sh from the 2026-06-08 entry @ $369.80. No new trade; no EXIT/stop signal fired.
- Remained the **only underwater held name and the thinnest stop cushion** in the book all week. Reliable tight-spread IEX marks: 07-06 open $360.84 (−2.4%), 07-06 pre_close $367.55 (−0.6%), 07-10 pre_close $356.61 (−3.57%); intraweek low mark ~$354.32 (midday 07-10). Every mark sat +6.8% to +10.9% above the $331.68 stop — never close to a breach.
- The carried-over W27 market-outcome prediction ("GOOGL holds above its stop through the NFP-driven 07-06 open", conf 0.6) resolved **CORRECT** (see `decisions/by_symbol/GOOGL.md` 2026-07-11 block).
- News backdrop (descriptive): EU top court upheld the €4.1B ($4.7B) Android antitrust fine, final appeal lost (07-02) — finality removes uncertainty, treated as pre-priced, not a fresh shock. Q2 2026 earnings 2026-07-22 (outside the 1-day caution window all week). No thesis-invalidating event.
- Momentum re-rank was **not computable on fresh data** all week (daily bars stale ~06-23). The 07-10 pre-market stale-bar scan showed GOOGL re-entering top-5 (rank 5, +12.39% 126d), reversing 07-09 — but on ~06-23 bars, so descriptive only, not an actionable rank.

## Week 2026-W29 observations
- Strategy: large_cap_momentum_top5. Held into the week from the 2026-06-08 entry (16 sh @ $369.8012); remained the **only underwater held name / thinnest stop cushion** in the book, as in prior weeks. **CLOSED 2026-07-17 midday** via a NEWS-DRIVEN DISCRETIONARY trigger (not a deterministic signal): `decisions/2026-07-17/1206_GOOGL.json`, trigger_type `news_driven_discretionary`, confidence 0.45. Exit ~$346.83 last IEX → ~−6.2% at exit mark; realized **−$367.54 est** (PENDING_BROKER exact; Alpaca 658d3242 FILLED).
- Trigger (descriptive): Bloomberg 07-16 (primary paywalled/403, verified via 5 URL-backed secondaries — US News/Reuters, Seeking Alpha, Yahoo Finance, PYMNTS, Android Authority) reported flagship **Gemini 3.5 Pro delayed by months + underperformed internal coding targets**; Alphabet fell >4%. GOOGL was already rank-5 (thinnest buffer) per the 07-16 regime.
- At close the deterministic Strategy-B exit rule was UNCONFIRMED: portfolio_health `should_close=false`, stop $331.68 NOT breached (last ~$346.83–352.75, ~4–6% cushion), SPY above 10m MA; top-7 momentum ejection was **unverifiable on stale daily bars** (bars end 06-29). The close leaned on discretionary news judgment rather than the validated deterministic rule — flagged in-journal as a calibration point (`journals/daily/2026-07-17.md §Lessons-pending`).
- Intraday path (descriptive): 07-17 market_open quote ~$344.56 (−6.83%), midday close ~$346.83. Earnings confirmed 2026-07-22 AMC (reconciling the prior 07-28-vs-07-22 discrepancy). positions.json after close: SPY only.
- Whether the discretionary override added or destroyed edge is STILL DEFERRED (needs a fresh daily close to recompute rank and forward price) — see `memory/prediction_reviews/2026-07-17.md` P1.

