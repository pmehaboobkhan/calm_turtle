# Symbol Profile — XOM

> Descriptive observations only. No advice, no forward recommendations. Append-only per period.

## Week 2026-W20 observations
- Strategy: large_cap_momentum_top5. Entry 2026-05-12 @ $148.6497 (40 sh). Held 2026-05-12 → 2026-05-15. Reset-terminated 2026-05-15T00:31:53Z (no signal invalidation).
- Momentum rank: 2/21 throughout. Provided energy / commodity diversification against the tech-heavy top of the slate. Oil-complex tailwind cited (Iran/Hormuz).
- Largest single-day MTM swing in the book: worst-MTM on 2026-05-13 (mark $142.12, −4.39%) to best-MTM on 2026-05-14 (mark $152.55, +2.62%). The 2026-05-13 late-day move (≈ −6.1% from pre_close to EOD) was the largest single-session adverse move of the week; still well above the −10% stop ($133.76) at all points.
- Q2 dividend ex-date 2026-05-15 ($1.03/sh, ≈ 0.68% mechanical price adjustment). Mechanical, not a thesis event; the ex-div flag was carried but became moot post-reset.
- Next earnings 2026-07-31 — well outside any window during this period.

## Week 2026-W21 observations
- Strategy: large_cap_momentum_top5. Re-entered the book this week: PAPER_BUY submitted 2026-05-18 @ ref $157.92, filled 2026-05-19 open @ $160.4279 (+$2.51/sh adverse slip — the largest adverse slip of the cohort), 97 sh via the alpaca mirror. Held all week; carried over the Memorial Day weekend into 2026-05-26 (still open).
- Momentum rank: rank 3/21 throughout the week (6m ~+36.68% at entry, ~+32.22% on the 2026-05-22 scan). Provided energy / commodity diversification against the tech-heavy top of the slate, consistent with the W20 character. Did not slip below the rank-7 hold zone.
- Flagged on 2026-05-20 as one of two late-day-weakness names (intraday mark −6.77%, approaching but NOT breaching the −10% stop $142.128; closed −$8.67/sh weaker in the final 30 minutes vs the pre_close mark). Recovered into week-end as portfolio DD fell from 4.34% (05-21) to 2.36% (05-22). The thin-cushion-name watch did not progress to a stop event.
- Stop/target fields recorded as null on the position all week under the alpaca-mirror reconcile (stop_loss=null, take_profit=null in positions.json) — stop monitoring was advisory/manual; descriptive standing observation (HIGH severity in the cycle report).
- No earnings catalyst in the window (next earnings 2026-07-31, well outside any window). No EXIT signal fired.

## Week 2026-W22 observations
- Strategy: large_cap_momentum_top5. Carried 97 sh from the W21 entry @ $160.4279 into the W22 window (holiday Mon 2026-05-25).
- Closed 2026-05-29 pre_close @ $145.37. Realized PnL: −$1,461 (−9.35% vs entry). Closed by the all-positions daily-loss halt, NOT by a stop or rotation signal.
- Momentum rank at close: 2/21 (6m +28.43%) — the momentum thesis persisted to exit; the position was liquidated by the system-level halt while still rank-2.
- Root cause of the loss: macro energy-complex beta. The US-Iran ceasefire / Strait of Hormuz de-escalation narrative drove WTI crude −10%+ on the week → XOM −9.35% entry-to-exit. Intraday low 2026-05-29 $145.37 vs the $142.13 rotation stop = +2.25% cushion; the stop was never breached.
- XOM was the dominant contributor to TWO daily-loss-limit breaches in the 4-session window: 2026-05-26 (−5.5% intraday) and 2026-05-29 (−9.06% intraday). Same macro catalyst both days.
- The operative trigger was the daily-loss limit, not the −10% rotation stop. At a $160.43 entry on 97 sh, a 5%+ intraday move on XOM alone consumes roughly $750+, exceeding the $500 daily-loss budget in isolation.
- Pattern (descriptive): XOM's energy-sector beta makes it a concentrated source of daily-loss risk when crude moves adversely (de-escalation / supply-normalization events). Energy-sector momentum can persist (rank-2 at exit) even as intraday crude moves breach the daily-loss threshold. This is the first paper-period instance of a single-name macro shock — not a diversified multi-name drag — driving the daily-loss halt; it answers (descriptively, N=1) the W21 open question on the soft-then-hard daily-loss dynamic under concentration.
- Q2 ex-dividend ($1.03/sh) fell in a prior period (2026-05-15 ex-date); not applicable to the W22 hold. Next earnings 2026-07-31 — well outside the window; no earnings caution in W22.
