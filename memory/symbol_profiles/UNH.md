# Symbol Profile — UNH

> SAFE_MEMORY_UPDATE — approved write path per CLAUDE.md
> Descriptive observations only. No advice, no forward recommendations. Append-only per period.

## Week 2026-W21 observations
- First appearance in the book. Strategy: large_cap_momentum_top5. PAPER_BUY submitted at EOD 2026-05-19 @ ref $391.13 (2026-05-18 daily-close basis), filled 2026-05-20 open @ $391.9044 (+$0.77/sh adverse slip, ~−$30 vs ref on 39 sh — inside the modeled slippage assumption), 39 sh via the alpaca mirror. Held through week-end; carried over the Memorial Day weekend into 2026-05-26 (still open).
- Entered as a rank-5 boundary name: at entry it was rank 5/21 (6m +19.34%), directly above NVDA (rank 6) and JNJ (rank 7), with the weakest absolute 6m momentum of that day's top-5 and the thinnest persistence buffer. Entry confidence was logged at 0.52 (lowest of the cohort) for exactly that boundary fragility plus offline news.
- Rank path: rank 5 (2026-05-19/20) → rank 4 on the 2026-05-22 scan (6m +23.75%, ahead of NVDA at rank 5). The predicted "rank-5 boundary churn / fast EXIT round-trip" branch did NOT fire within the window; UNH actually firmed by one rank. Health_Care diversified an otherwise Tech/Energy/Commodity-heavy basket.
- Liquidity watch (descriptive): on 2026-05-20 the bid/ask spread was noted as wide ($33.30) for the rank-5 boundary name; no fill-quality event resulted. uPnL mark ~+$146 at week-end (descriptive).
- Stop/target fields recorded as null on the position all week under the alpaca-mirror reconcile (stop_loss=null, take_profit=null in positions.json) — stop monitoring was advisory/manual; descriptive standing observation (HIGH severity in the cycle report). The intended stop was $352.017 (−10%) / TP $488.9125 (+25%) per the entry decision.
- No earnings or single-stock catalyst in the window. No EXIT signal fired. Holding-period outcome resolution deferred to a future cycle.

## Week 2026-W22 observations
- Strategy: large_cap_momentum_top5. Carried 39 sh from the W21 entry @ $391.9044 into the W22 window (holiday Mon 2026-05-25).
- Closed 2026-05-29 pre_close @ $380.89. Realized PnL: −$430 (−2.81% vs entry). Closed by the all-positions daily-loss halt, NOT by a stop or rotation signal.
- Momentum rank: 4/21 throughout W22 (6m +21–24%). Firmed from the rank-5 boundary in W21 and held rank 4 with a wider margin.
- Stop ($352.71) never breached during W22. Thinnest-cushion readings observed at: 05-27 EOD (+1.97% above stop, $395.00 mark vs $352.71) and 05-29 midday (+7.9% cushion at pre_close close). The thin-cushion-name watch from W21 persisted into W22 but without a stop event.
- Berkshire Q1 13F fully exited UNH (publicly known going into W22) — a smart-money sell signal against the rank-4 momentum thesis. Noted as a bear-thesis entry in all pre_close and EOD records. The UNH mark ended up negative (−$430) but the stop was never close to breaching; the Berkshire exit was a fundamental/sentiment flag, not a near-term price catalyst.
- DOJ Medicare-Advantage probe (cooperative phase since Jul 2025) + Optum antitrust probe: ongoing background risk, no new 05-26→05-29 development. Bernstein PT raise to $492 on 05-29 was partially offsetting.
- Pattern (descriptive): UNH's trajectory from rank-5 boundary in W21 to more secure rank-4 in W22 was correct (no rotation exit), yet the position closed in loss. The tension between "signal says hold" (rank 4, above stop) and "smart-money sells" (Berkshire exit) remained unresolved during the paper window — the halt, not either signal, determined the exit.

## Week 2026-W28 observations
- Strategy: large_cap_momentum_top5. Held all five sessions (07-06 → 07-10); 15 sh from entry @ $398.674. No new trade; no EXIT signal fired. (Note: this profile last carried a W22 block — the 2026-06-08 re-entry and W23–W27 holding history are recorded in `decisions/by_symbol/UNH.md`, not here; this is the W28 review block only.)
- Green all week: marks ~+8.8% (07-06 open $433.88) to ~+6.2% (07-10 pre_close ~$423.20). Well above its $356.82 stop and below its $495.59 target throughout. 07-10 pre_close mark low-confidence (wide 5.9% bid/ask spread) — health conclusion robust across the spread (bid $410.40 ≫ stop).
- News backdrop (descriptive): Morgan Stanley PT $468, Overweight (noted 07-06); ongoing regulatory scrutiny + "fully valued" chatter surfaced 07-10 (source cited in `journals/daily/2026-07-10.md` midday) — neither thesis-invalidating. Consistent with the standing DOJ Medicare-Advantage / Optum background risk from prior weeks.
- Q2 2026 earnings **2026-07-16** — approaching but outside the 1-day caution window at W28 close.
- Momentum rank not computable on fresh data (bars stale ~06-23); 07-10 stale-bar scan placed UNH at rank 2 (+23.99% 126d), descriptive only.

## Week 2026-W29 observations
- Strategy: large_cap_momentum_top5. Held into the week from the 2026-06-08 entry (15 sh @ $398.674). **CLOSED 2026-07-15 pre_close** — overnight earnings-risk action (UNH Q2 07-16 BMO, next trading day, inside the 1-day earnings-caution window), NOT a stop/target trigger (`decisions/2026-07-15/1936_UNH.json`: `stop_breached=false`, `target_hit=false`, `invalidation_triggers=[]`, pnl +5.0% on last IEX print). Exit @ $418.2613; realized **+$293.81 (confirmed vs Alpaca fill)**; mirrors the 07-14 JNJ earnings-caution precedent.
- Very wide IEX spread at close (~5.4%, thin single-stock IEX bid) — last=418.42 used as the execution reference rather than the artefactual bid 395.67; disclosed as fill-quality, did not gate the earnings-driven exit. Consistent with the standing UNH/JNJ late-day IEX spread observation.
- Earnings outcome (descriptive): UNH Q2 07-16 BMO **BEAT + raised** — EPS $6.04 vs $4.91, FY guide $19.50–$20.00 (per `journals/daily/2026-07-17.md` pre-market news overlay; CNBC/GuruFocus/SEC 8-K). Closed pre-emptively before the favorable print; DOJ Medicare-Advantage / Optum antitrust overhang cited as bear-thesis background in the close decision (unchanged standing risk).
- EOD 2026-07-15 REFUSED re-entry (`decisions/2026-07-15/2044_UNH.json`) on both data staleness and the still-open earnings window; re-entry proper deferred to the first fresh post-earnings EOD (still deferred, feed down).
- Momentum rank not computable on fresh data all week (bars stale ~06-29); stale-bar scans placed UNH rank 2 (~+25.19% 6m), descriptive only.

