# Observations — week ending 2026-07-17

> v1 observations-only (`.v2_enabled` absent; `max_self_learning_proposals_per_cycle=0`). Descriptive bookkeeping; no recommendations, no verdicts. Every claim cites source. Sample sizes far below the N≥20 (strategy) / N≥50 (trade) thresholds — treat all as PRELIMINARY.

## Period
- Trading days: **5** (2026-07-13 Mon → 2026-07-17 Fri; all sessions monitored).
- Decisions: **3 PAPER_CLOSE** (JNJ 07-14, UNH 07-15, GOOGL 07-17; all `RISK_AND_COMPLIANCE_APPROVED`) plus recurring NO_TRADE stale-bar re-evaluations for CSCO/GLD/XOM/JNJ/UNH/COST (`decisions/2026-07-13/`…`2026-07-16/`).
- Paper trades opened: **0** (all fresh ENTRY gated NO_TRADE under CLAUDE.md rule #5 — daily bars stale ~06-29 every session; `journals/daily/2026-07-17.md`).
- Paper trades closed: **3** (JNJ +$538.98 est, UNH +$293.81 confirmed, GOOGL −$367.54 est; `trades/paper/log.csv` rows 07-14T19:41, 07-15T19:40, 07-17T16:11).

## Predictions reconciled this week
- **07-13 Prediction 4 — CPI 07-14 forces no stop/target close (conf 0.6):** CONFIRMED. June CPI printed cooler (~3.5% YoY vs ~3.8% exp, `decisions/2026-07-14/1535_JNJ.json`); no held name breached a stop/target; JNJ did not gap into its $290.96 TP (it was closed pre_close for earnings, not on a price trigger). Predicted no-close vs actual no-close.
- **07-13 Prediction 5 — a JNJ/UNH earnings MISS would trigger a momentum-rotation EXIT (conf 0.55):** RESOLVED, tail did not materialize. Predicted the miss branch as the likeliest rotation trigger; actual: both JNJ (07-15 BMO) and UNH (07-16 BMO) BEAT + raised (`journals/daily/2026-07-17.md`), so no miss and no rotation EXIT. Both were instead closed pre-emptively under the earnings-caution overlay (07-14 JNJ, 07-15 UNH) before the beats.
- **07-16 Prediction 4 — GOOGL earnings-date resolves outside the window; no forced earnings de-risk before the confirmed date (conf 0.7):** CONFIRMED. GOOGL earnings confirmed 07-22 AMC (`journals/daily/2026-07-17.md`); no earnings-caution close. Predicted no earnings-date close vs actual none (the 07-17 close was a separate news trigger).
- **07-17 Prediction 2 — SPY holds above stop + no invalidation through EOD 07-17 (conf 0.6):** CONFIRMED. SPY $742.93 at 07-17 pre_close (−0.11%), `stop_breached=false`, `invalidation_triggers=[]`; held overnight into 07-20 (`journals/daily/2026-07-17.md §Pre-close`). Predicted hold vs actual hold.
- **JNJ earnings-caution close (07-14 decision):** reconciled — closed pre-earnings at ~+8.8%/+$538.98 est; JNJ then BEAT + raised. Predicted (implicit): de-risk the overnight binary; actual: binary resolved favorably, position was flat post-close.
- **UNH earnings-caution close (07-15 decision):** reconciled — closed pre-earnings at +5.0%/+$293.81 confirmed; UNH then BEAT + raised. Predicted: de-risk the binary; actual: binary resolved favorably, position flat post-close.
- **07-17 Prediction 1 — GOOGL news-override calibration test (conf 0.45):** STILL DEFERRED — feed stale, rank not recomputable; no fresh forward close. New window = first fresh daily close (`memory/prediction_reviews/2026-07-17.md`).
- **Carried, STILL DEFERRED (3rd consecutive week):** NVDA/CSCO/XOM 2026-07-01 stop-exit reclaim durability; GLD 210d-MA reclaim / A-C conflict — all unverifiable on stale bars (`decisions/by_symbol/{NVDA,CSCO,XOM,GLD}.md`).
- (In addition, the daily P1–P5 cascades resolved ~20 operational feed/CB/pending-broker/archiver items inline across 07-13→07-17; see `memory/agent_performance/2026-w30.md` histogram.)

## Calibration snapshot
Weekly-pass market/operational resolutions (confidence bucket → N → outcome):
- 0.70: N=1 → 1 CONFIRMED (GOOGL earnings-date).
- 0.60: N=2 → 2 CONFIRMED (CPI no-close; SPY hold).
- 0.55: N=1 → tail did not materialize (both beat; no rotation EXIT).
- 0.45: N=1 → STILL OPEN / deferred (GOOGL news-override test).

Daily-cascade operational resolutions (07-13→07-17):
- 0.90: N=8 → 8 CONFIRMED (pending-broker persists ×4; CB stays FULL ×4).
- 0.85: N=4 → 4 CONFIRMED (UNH next-day exposure; GLD A/C conflict; archiver ×2).
- 0.80: N=4 → 4 CONFIRMED (feed still broken ×4).
- 0.75: N=2 → 2 CONFIRMED (IEX basis-gap artifact ×2).
- 0.70: N=1 → 1 CONFIRMED (UNH re-entry refused).
- 0.60: N=2 → 2 CONFIRMED (holds above stops ×2).

Closed-trade outcomes: 2/3 wins (JNJ, UNH); 1 loss (GOOGL). Net realized this week +$465.25 est (JNJ & GOOGL exact PENDING_BROKER). Post-reset cumulative: 7 closed, 2/7 wins, ≈ −$678.82 est. All N far below significance thresholds.

## Surprises
- Both earnings binaries resolved on the benign side (JNJ + UNH both BEAT + raised) — the single largest tail risk the 07-16 regime file flagged did not fire (`journals/daily/2026-07-17.md`). The earnings-caution overlay closed both before the favorable prints.
- CSCO — the stale-bar rank-1 momentum name (+50.25% 6m) — slid −4.2% (07-15) then −3.0% (07-16) on live prints while the deterministic engine still ranked it #1; the divergence was visible only via news_sentiment, not the stale ranks (`journals/daily/2026-07-17.md` pre-market).
- GOOGL closed on a discretionary news trigger (Gemini 3.5 Pro delay) with the deterministic Strategy-B exit rule UNCONFIRMED (stop not breached, top-7 ejection unverifiable on stale bars) — a departure from the backtest-validated deterministic exit set (`decisions/2026-07-17/1206_GOOGL.json`).
- Week-end equity closed below the $100k inception mark ($99,897.35, −0.10%) for the first time in the recent monitoring stretch, despite two winning earnings-caution closes — the realized gains were already in unrealized MTM, while GOOGL's decline drove the net (`memory/agent_performance/2026-w30.md`).
- Pending-broker ledger grew 4→7 as the three closes each added a stale row; CB write skipped via Guard 1 every session (`journals/daily/2026-07-17.md`).

## Open questions for future review
- On the first fresh daily close: would GOOGL have exited on the deterministic top-7 rank rule, and did it recover above the $346.83 exit? (Resolves whether the 07-17 discretionary news override added or destroyed edge — `memory/prediction_reviews/2026-07-17.md` P1.)
- When ≥50 trades / ≥90 days accumulate: does the 1-day earnings-caution overlay help or hurt on net, given both JNJ and UNH were closed ahead of favorable beats this week? (N=2 favorable outcomes here is far too small to judge; record only.)
- Did the NVDA/CSCO/XOM 2026-07-01 stop exits prove durable? (3rd week deferred; needs a trustworthy fresh close.)
- How would the stale-bar bullish_trend / CSCO rank-1 read revise once the daily-bar feed recovers, given the observed CSCO two-day live slide?
