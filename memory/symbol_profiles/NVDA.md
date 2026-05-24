# Symbol Profile — NVDA

> Descriptive observations only. No advice, no forward recommendations. Append-only per period.

## Week 2026-W20 observations
- Strategy context: large_cap_momentum_top5. Never entered the book during the window.
- Rank path: rank 7 NO_SIGNAL (2026-05-13) → rank 5 ENTRY (2026-05-14, +18.90% 6m; +3.46pp 6m-return move, displaced AMZN) → rank 7 NO_SIGNAL (2026-05-15). A 2-day boundary promotion that did not persist.
- The single rank-5 ENTRY day (2026-05-14) was blocked at the routing layer by `circuit_breaker_OUT AND data_staleness_breach`; no entry was attempted.
- Outcome of the rank-5 signal: classified benign — boundary noise. The rank-7 → rank-5 → rank-7 path confirms the promotion was 1–2 day jitter, not a sustained signal.
- Descriptive note recorded in the daily reviews: NVDA was the highest-beta name in the watchlist this window and carried the tightest watchlist position cap (10%); rank-5 boundary appearances coincided with single-session 6m-return swings.

## Week 2026-W21 observations
- Strategy context: large_cap_momentum_top5. Did NOT hold a position during the trading week (2026-05-18 → 2026-05-22); a PAPER_BUY was submitted at EOD 2026-05-22 (order ACCEPTED, PENDING_BROKER) and fills at the 2026-05-26 open — so the first NVDA open since the project began lands in the next cycle.
- Q1 FY27 earnings printed 2026-05-20 (a strong beat). The position entered the post-print holding_earnings_caution_window_days=1 window: entry was deferred on 2026-05-21 (1-day caution window active). On 2026-05-22 EOD the gate had cleared (2 sessions elapsed since the print) and the ENTRY was promoted: rank 6 → rank 5 (6m +21.05%), the first net-new open since the 2026-05-19 UNH entry.
- Order: BUY 27 @ ref price; stop $197.559 (−10%) / TP $274.3875 (+25%); order_id 14d3ade1…, status ACCEPTED. Fill, slippage, and holding-period outcome all resolve next cycle (do not reconcile here).
- Rank-5 boundary fragility carried over from W20: at the 2026-05-22 scan NVDA (rank 5, 21.05% 6m) sat only 0.42pp above AMZN (rank 6, 20.63%), and UNH had firmed to rank 4 (23.75%). The top-5 cutoff remained a low-persistence, closely-clustered boundary all week.
- Descriptive note: NVDA continued to be the highest-beta name in the watchlist this window and carries the tightest watchlist position cap (10%). No EXIT signal applicable (no position held during the trading days).
