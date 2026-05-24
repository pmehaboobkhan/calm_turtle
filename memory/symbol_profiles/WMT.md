# Symbol Profile — WMT

> Descriptive observations only. No advice, no forward recommendations. Append-only per period.

## Week 2026-W20 observations
- Strategy: large_cap_momentum_top5. Entry 2026-05-12 @ $130.116 (46 sh). Held 2026-05-12 → 2026-05-15. Reset-terminated 2026-05-15T00:31:53Z (no signal invalidation).
- Momentum rank: 4/21 throughout. Defensive consumer-staples character; decorrelated the tech-heavy top of the slate.
- Pre-close 2026-05-14 mark $132.01 (+$87.12, +1.46% on entry). Stop $117.081 (~11.3% headroom at the 2026-05-14 mark).
- Late-day reversal on 2026-05-13 ≈ −4.6% from pre_close to EOD; notable but still well above the −10% stop at all points.
- Earnings flag: Q1 FY27 earnings 2026-05-21 BMO. A 7-day advance warning was captured at midday 2026-05-14. The pre_close-2026-05-20 routine would have executed a CSCO-style pre-earnings exit decision had the position still been held; the flag became moot after the 2026-05-15 reset cleared the line.
- April retail-sales release (2026-05-14 BMO) and the 2026-05-12 restructuring announcement were observed during the hold; neither was a thesis-invalidating event for the momentum signal during the window.

## Week 2026-W21 observations
- Strategy: large_cap_momentum_top5. Re-entered the book this week: PAPER_BUY submitted 2026-05-18 @ ref $131.45 (rank 4/21, 6m ~+27.84% at entry), filled 2026-05-19 open @ $132.5397 (+$1.09/sh adverse slip), 116 sh via the alpaca mirror.
- Q1 FY27 earnings BMO 2026-05-21 was a known catalyst flagged at entry. The position entered the holding_earnings_caution_window_days=1 window on 2026-05-20; the pre_close-2026-05-20 routine executed a pre-print exit: CLOSE 116 @ $131.23 (alpaca mirror FILLED), realized −$151.93. The position did NOT carry into the print.
- The 2026-05-21 print: EPS $0.66 (beat $0.65 est), revenue $177.75B (beat ~$174.65B est), Walmart US comps +4.1%. Despite the beat, WMT fell ~8% on the print (sources: Quiver Quantitative, The Motley Fool, Seeking Alpha, 2026-05-21). The pre-print exit avoided that gap-down; held-through counterfactual on the ~$15.2k position would have been roughly −$1,063 to −$1,215 of additional MTM damage on top of the small carry loss.
- This is the second resolved instance of the beat-and-fall earnings pattern observed in the watchlist (CSCO W20, +20% gap UP on its beat; WMT W21, −8% gap DOWN on its beat) where the pre-earnings exit overlay shaped the realized outcome. Descriptive — N=2, no conclusion drawn.
- Post-print: a deterministic ENTRY fired on the 2026-05-20 pre-earnings daily close and was REJECTED by RM at EOD 2026-05-20 (earnings_window); the 2026-05-21 routine declined re-entry (NO_TRADE) on the stale pre-gap signal. On the 2026-05-22 EOD scan WMT was NOT in the top-5 (out post-gap; the top-5 was CSCO/GOOGL/XOM/UNH/NVDA). WMT was not in the book at week-end and was not carried into 2026-05-26.
- Standing observation (descriptive): the ENTRY that fired on 2026-05-20 used a stale pre-event bar; the block was RM-judgment-driven, not a deterministic stale_post_event signal flag (MEDIUM severity in the cycle report).
