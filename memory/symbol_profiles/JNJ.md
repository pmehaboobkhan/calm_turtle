# Symbol Profile — JNJ

> Descriptive observations only. No advice, no forward recommendations. Append-only per period.

## Week 2026-W20 observations
- Strategy context: large_cap_momentum_top5. Never entered the book during the window.
- Rank path: rank 5 ENTRY (2026-05-12, +20.17% 6m) → rank 6 NO_SIGNAL (2026-05-13, displaced by AMZN) → rank 7 NO_SIGNAL (2026-05-14) → rank 5 (2026-05-15). A 3-session boundary oscillator around the top-5 cutoff.
- The initial rank-5 ENTRY signal on 2026-05-12 was deferred by the `max_trades_per_day=5` cap (the day's first 5 entries — GLD/GOOGL/XOM/CSCO/WMT — consumed the budget); this was a budget deferral, not a signal-quality rejection.
- Outcome of the deferral: classified benign — JNJ retreated to rank 6 the next session, so the capped entry would have been a boundary oscillator anyway. JNJ returned to rank 5 on 2026-05-15, but the book had already been reset by then.
- No news-driven catalyst observed for JNJ during the window.

## Week 2026-W28 observations
- Strategy: large_cap_momentum_top5. Held all five sessions (07-06 → 07-10); 26 sh from entry @ $232.75. No new trade; no EXIT signal fired.
- Strongest held B-name by unrealized gain: marks ~+12.6% (07-06 open $262.06) to ~+16.9% (07-10 midday $272.06). **Approached but never reached** its +25% take-profit ($290.96); no target-hit CLOSE fired. Well above its $209.49 stop throughout.
- 07-10 pre_close IEX mark was low-confidence (wide 4.6% bid/ask spread, ~$251 mid vs $272 midday) — a thin late-day quote, not a real move; bid $245.10 still far above stop, ask $256.89 far below target, so the "0 closes" conclusion held robustly across the spread.
- News backdrop (descriptive): FDA approval of J&J's Dual-Energy THERMOCOOL SMARTTOUCH SF cardiac-ablation catheter (2026-07-08, bullish; source cited in `journals/daily/2026-07-10.md` midday). Talc settlement vote ongoing (known, deadline ~07-26). No thesis-invalidating event.
- Q2 2026 earnings **2026-07-15** — moved inside the 1-day caution window as the week ended; flagged by pre_close/EOD for a possible take-profit / pre-earnings de-risk consideration on the next fresh-data session (not yet actioned; entries/exits still infrastructure-blocked).
- Momentum rank not computable on fresh data (bars stale ~06-23); 07-10 stale-bar scan placed JNJ in top-5 (+16.74% 126d), descriptive only.

## Week 2026-W29 observations
- Strategy: large_cap_momentum_top5. Held into the week from the 2026-06-08 entry (26 sh @ $232.75). **CLOSED 2026-07-14 pre_close** — overnight earnings-risk action (JNJ Q2 07-15 BMO inside the 1-day earnings-caution window), NOT a stop/target trigger (`decisions/2026-07-14/1535_JNJ.json`: portfolio_health `stop_breached=false`, `target_hit=false`, `invalidation_triggers=[]`). Exit ref ~$253.48; realized **+$538.98 est** (PENDING_BROKER exact; Alpaca e01c2828 FILLED). At close, ~+8.8% vs entry, rank-3 by 6m momentum on stale bars.
- Wide IEX spread at proposal time (~2.26%) tightened to ~0.04% (bid 253.48 / ask 253.58) by execution — the recurring single-stock late-day IEX spread artifact (also seen on UNH); disclosed as a fill-quality note, did not gate the earnings-driven exit.
- Earnings outcome (descriptive): JNJ Q2 07-15 BMO **BEAT + raised** — sales $25.31B (+6.6%), adj EPS $2.90, FY ~$101.1B (per `journals/daily/2026-07-17.md` pre-market news overlay; CNBC/Seeking Alpha/SEC 8-K). The position was closed pre-emptively before this favorable print; post-close the lot was flat so post-beat upside is not measurable from paper marks.
- Momentum rank not computable on fresh data all week (daily bars stale ~06-29); stale-bar scans placed JNJ rank 3 (~+22.37% 6m), descriptive only.

