# Observations — week ending 2026-05-24

> v1 observations-only mode (`prompts/proposed_updates/.v2_enabled` absent). This report records; it does not prescribe. Zero proposals. Sample sizes are far below the v1 thresholds (≥ 90 trading days AND ≥ 50 paper trades). With 5 trading days this cycle and exactly 1 closed trade post-reset, any "pattern" here is overwhelmingly likely to be noise. Observations are separated from conclusions, and no conclusions are drawn.

## Period
- Trading days: 5 (2026-05-18 → 2026-05-22). Mon Memorial-Day week; holiday Mon 2026-05-25; next session Tue 2026-05-26.
- Decisions: 18 trade-decision JSON files (7 on 05-18, 7 on 05-19, 2 on 05-20, 1 on 05-21, 1 on 05-22), plus journal-only held-position maintain re-confirms not counted as separate JSON.
- Paper trades opened (filled): 6 (GLD/CSCO/GOOGL/XOM/WMT filled 05-19 open; UNH filled 05-20 open). 1 additional (NVDA) submitted 05-22 EOD, PENDING_BROKER, fills 2026-05-26 — not counted as opened this cycle.
- Paper trades closed: 1 (WMT, 2026-05-20 pre_close, −$151.93).
- Net realized PnL post-reset: −$151.93 (WMT is the only post-reset closed trade). The 2026-05-13 CSCO +$618.90 is pre-reset and excluded from post-reset stats.
- Open positions entering 2026-05-26: CSCO (130), GLD (36), GOOGL (38), UNH (39), XOM (97); NVDA (27) pending fill.

## Predictions reconciled this cycle
> Outcome annotations were appended (append-only, under `## Outcome annotation (self_learning_review 2026-05-24)`) to `memory/prediction_reviews/2026-05-18.md`, `2026-05-19.md`, `2026-05-20.md`, and `2026-05-21.md`. The 2026-05-22 file remains PENDING (its predictions resolve on the 2026-05-26 open) and was deliberately not touched. No original rows were edited.

- **2026-05-18 — 5 PAPER_BUY entries (GLD/CSCO/GOOGL/XOM/WMT) + JNJ NO_TRADE:** Fill leg CORRECT 5/5 (filled 05-19 open; slippage 3 favorable / 2 adverse, all small). 4 of 5 (GLD/CSCO/GOOGL/XOM) remain open at week-end (no rotation/stop/target). WMT subsequently closed pre-earnings 05-20 (−$151.93). JNJ NO_TRADE (max_trades cap) resolved as a costless deferral — JNJ ranked 9/21 (NO_SIGNAL) at week-end, would not have re-qualified.
- **2026-05-19 — UNH PAPER_BUY (rank 5) + 5x maintain + CB-artifact non-recurrence:** UNH fill leg CORRECT (filled 05-20 open, +$0.77/sh adverse, inside the slippage model); still open, firmed rank 5→4, uPnL ~+$146 at week-end; the predicted rank-5-churn EXIT did NOT fire. 5x maintain held for GLD/CSCO/GOOGL/XOM; the WMT branch was the explicitly forward-flagged earnings exception (closed 05-20). CB-artifact-non-recurrence resolved CORRECT for the held book (no recurrence on filled positions; CB stayed FULL all week).
- **2026-05-20 — WMT PAPER_CLOSE (catalyst leg) + WMT EOD ENTRY reject + 5x maintain:** WMT close RESOLVED CORRECT_POLICY + CORRECT_DOLLARS (the 05-21 beat-and-fall print, ~−8%, would have cost roughly −$1,063 to −$1,215 more on the held-through counterfactual). WMT EOD ENTRY REJECTED (earnings_window) RESOLVED CORRECT_POLICY (doubly correct — re-entry would have re-added the overnight risk just removed). 5x maintain held; the flagged late-day-weakness watch (GOOGL −6.89% / XOM −6.77% on 05-20) did NOT progress to a stop trip.
- **2026-05-21 — WMT NO_TRADE post-print + 5x hold + CB stays FULL:** WMT NO_TRADE policy leg already tagged CORRECT by weekly_review_2026-05-23; the directional branch is trending toward CORRECT (WMT did not recover above the pre-gap level and was out of the top-5 by 05-22) but only 1 of the ~5-session window elapsed before the holiday — marked PRELIMINARY-CORRECT, resolution deferred. 5x hold RESOLVED CORRECT for the single-session horizon (no stop, no EXIT, no MA break). CB-stays-FULL RESOLVED CORRECT (no >3.6pp drop; DD fell 4.34% → 2.36%; no FULL→HALF).

## Calibration snapshot (raw counts)
> Histogram of stated confidence vs realized outcome class. Raw counts only — no "overconfident"/"miscalibrated" judgment. Win-rate / Brier is intentionally NOT computed: only 1 post-reset trade is closed; 5 holding-period legs are still OPEN; sample far below the v1 threshold.

| Confidence bucket | N (predictions this cycle) | Members | Outcome class (raw) |
|---|---|---|---|
| 0.50–0.59 | 3 | UNH BUY (0.52), CSCO BUY (0.55), WMT BUY (0.58) | UNH filled+open (firmed rank); CSCO filled+open; WMT filled then closed pre-earnings (−$151.93). 0 conclusions. |
| 0.60–0.69 | 3 | XOM BUY (0.60), GOOGL BUY (0.62), GLD BUY (0.64) | All 3 filled, held all week, open at week-end. No stop/rotation/target. |
| 0.70–0.79 | 2 | WMT post-print NO_TRADE (0.75), 5x hold (0.70) | NO_TRADE PRELIMINARY-CORRECT; 5x hold CORRECT for the predicted horizon. |
| 0.80–0.89 | 2 | WMT pre-earnings CLOSE (0.85), CB stays FULL (0.85) | CLOSE CORRECT_POLICY + CORRECT_DOLLARS; CB CORRECT. |
| ≥ 0.90 | 1 | WMT EOD ENTRY reject — earnings_window (0.92) | CORRECT_POLICY (doubly correct). |

- The ≥ 0.80 buckets remain dominated by mechanical/policy-gate confidence (earnings-window block, CB-state persistence, pre-earnings exit) rather than directional bets — consistent with the dichotomy noted in prior cycles (high routing confidence on hard gates; modest directional confidence on momentum entries clustered 0.52–0.64).
- **Risk Manager / Compliance calibration drift check: none observed.** Every actionable gate fired deterministically and was honored (earnings_window REJECT on the 05-20 WMT re-entry; max_trades cap on JNJ; CB thresholds). No gate was bypassed. No `HALT_AND_REVIEW` recommendation is warranted on calibration grounds. The INTU compliance block was not implicated this cycle (INTU not in any signal/decision).

## Surprises
> Descriptive only. Things that did not match symbol-profile or regime expectation. No conclusions.

- **WMT beat-and-fall (−8% on an EPS + revenue beat, 2026-05-21).** Second resolved instance of the beat-and-fall pattern in the watchlist (CSCO W20 gapped ~+20% UP on its beat; WMT W21 ~−8% DOWN on its beat). The pre-earnings-caution overlay shaped the realized outcome both times. N=2; recorded, no conclusion.
- **Circuit-breaker equity-in-flight defect (HIGH severity).** 2026-05-19 intraday, broker cash was debited for PENDING orders not yet mirrored → spurious 74% DD / HALF state, firing 5 URGENT Telegram alerts for a non-event. Self-corrected at EOD. Apparent root cause: `broker.account_snapshot()["cash"]` evaluated before fill reconcile. Logged at logs/risk_events/2026-05-19_203823_circuit_breaker.md.
- **Stop/target field loss under alpaca-mirror (HIGH severity).** All 5 open positions carried `stop_loss=null, take_profit=null` in positions.json all week (confirmed in the current file); the reconciler does not preserve these fields. Stop monitoring was advisory/manual all week — a silent safety degradation. The intended stops (e.g., CSCO −10% $106.389, GLD $375.561, GOOGL $357.102, XOM $142.128, UNH $352.017) live only in the entry decisions/log, not on the reconciled position.
- **Post-earnings stale signal required RM judgment, not a gate (MEDIUM severity).** The WMT ENTRY fired on the 2026-05-20 pre-earnings bar; WMT then fell ~8% the next morning. The NO_TRADE was RM-judgment-driven; there is no deterministic `stale_post_event` flag on the signal.
- **Rank-5 boundary fragility.** UNH/NVDA/AMZN sat within ~2pp of each other at week-end (NVDA 21.05% vs AMZN 20.63% = 0.42pp). The rank-5 slot changed hands multiple times (UNH 5→4, NVDA 6→5, AMZN holding the buffer). Low-persistence boundary.
- **Two consecutive soft daily-loss breaches without a hard halt.** −1.25% (05-20) + −1.77% (05-21); the hard −2% halt was NOT triggered. Drag was diversified across 4–5 names; no individual position near its −10% stop; the third session reversed the drawdown.
- **NVDA 2-day post-print gate cleared correctly.** Q1 FY27 print 05-20 (strong beat); 1-day caution deferred entry on 05-21; EOD 05-22 cleared the gate (2 sessions elapsed) and promoted NVDA rank 6→5. Policy-correct; the fill resolves next cycle.
- **Regime stayed bullish_trend / medium all week.** SPY above 50d (+6.39% → +6.89%), 200d, and 10m SMA throughout; VIX proxy compressed (~10.5%); GLD maintained its 12m-return lead over SPY and IEF; IEF below its 10m MA (cash floor not active). No label transition, no genuine CB throttle, no MA flip.

## Open questions for future review (revisit at N ≥ 50 closed trades / ≥ 90 trading days)
- Is the pre-earnings-exit overlay's dollar advantage on beat-and-fall prints (CSCO W20, WMT W21) a durable edge or two coincidences? N=2 so far.
- Does the CSCO rank-1 +61.56% 6m momentum (now held 1 full week with no mean-reversion) prove durable, or is it an earnings-gap-extension artifact that reverts later in the holding period?
- Is rank-5 boundary churn (UNH ↔ NVDA ↔ AMZN around the cutoff) a consistent structural pattern or signal jitter? Now ~6 boundary data points across W20–W21.
- Does the GLD 12m-return decay (~−4pp/week vs a rising SPY, now observed across two weeks) become a real rotation/exit signal over the next 4–6 weeks, or remain within-window noise?
- Do the two HIGH-severity infrastructure observations (CB equity-in-flight misread; stop/target field loss under alpaca-mirror) recur once a fresh in-flight window or a stop-monitoring event actually arises? Non-recurrence on a benign week does not retire either defect.
- What is the slippage-vs-quote distribution as the post-reset fill sample grows (6 fills so far: 3 favorable, 2 adverse, 1 ~flat)?
- Will the soft-then-hard daily-loss dynamic behave as designed if a single concentrated name (not a diversified 4–5-name drag) drives the loss?

---

**Cycle outputs (all under approved write paths; zero proposals; append-only where applicable):**
- Appended outcome annotations: `memory/prediction_reviews/2026-05-18.md`, `2026-05-19.md`, `2026-05-20.md`, `2026-05-21.md` (already present from this cycle's annotation pass; verified, not duplicated).
- W21 symbol-profile observations: CSCO, GLD, GOOGL (already present), XOM, WMT, NVDA (appended this pass); UNH (new file).
- Regime history: `memory/market_regimes/history/2026-05-18.md` … `2026-05-22.md` (new).
- Weekly regime summary: `memory/market_regimes/2026-w21.md` (new).
- This report.
