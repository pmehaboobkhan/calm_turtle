# Observations — week ending 2026-05-31

> v1 observations-only mode (`prompts/proposed_updates/.v2_enabled` absent; mode PAPER_TRADING, not SAFE_MODE — learning writes permitted). This report records; it does not prescribe. Zero proposals. Sample sizes remain far below the v1 thresholds (≥ 90 trading days AND ≥ 50 paper trades). With 4 trading days this cycle and 6 closed trades this week, any "pattern" here is overwhelmingly likely to be noise. Observations are separated from conclusions, and no conclusions are drawn.

## Period
- Trading days: 4 in the trading window (2026-05-26 → 2026-05-29); Mon 2026-05-25 Memorial Day holiday. Reconciliation window spans 2026-05-21 → 2026-05-29 (7 trading days + the holiday) for prediction outcomes whose horizons closed this cycle.
- Decisions: 05-27 produced 1 trade decision (AMZN PAPER_BUY → REJECTED) + 5 held re-confirms; 05-28 produced 6 NO_TRADE (5 held maintains + AMZN stale-reject) + 1 subsumed note; 05-26 closed NVDA (de-risk) and held 5; 05-29 closed all 5 (halt) + refused EOD re-entries. Held-position maintain re-confirms in journals not counted as separate JSON.
- Paper trades opened (filled): 0 net-new opens this window. (NVDA's open filled 2026-05-26 from a 05-22 submission; counted as a prior-cycle open.) AMZN ENTRY was refused all four sessions (stale bars 05-27/05-28; daily-loss halt 05-29).
- Paper trades closed: 6 — NVDA (05-26 de-risk, +$453 WIN); then CSCO (+$456 WIN), GLD (+$215 WIN), XOM (−$1,461 LOSS), GOOGL (−$495 LOSS), UNH (−$430 LOSS), all 05-29 forced by the all-positions daily-loss halt.
- Net realized PnL this week (6 closes): +$453 +$456 +$215 −$1,461 −$495 −$430 = **−$1,262**. 3 wins / 3 losses by count; the single XOM loss (−$1,461) exceeded the sum of all three wins (+$1,124).
- Equity path (broker-authoritative): 05-26 open $101,149.06 → 05-26 EOD $100,534.81 (−0.607%) → 05-27 EOD $100,512.32 (−0.022%) → 05-28 EOD $100,192.16 (−0.318%) → 05-29 EOD $100,578.03 (+0.384%). Book ended 100% cash, zero overnight risk.
- Open positions entering 2026-06-01: none (full cash). AMZN re-entry pending the daily-loss-limit reset.

## Predictions reconciled this cycle
> Reconciliation sections were appended (append-only, under `## Self-learning review reconciliation 2026-05-31`) to `memory/prediction_reviews/2026-05-27.md` (5 predictions) and `memory/prediction_reviews/2026-05-28.md` (5 predictions). No original rows were edited. 10 predictions reconciled in total.

**2026-05-27 EOD predictions (5):**
- **#1 ENTRY-REFUSAL (AMZN) — RESOLVED CORRECT.** AMZN re-entered the top-5 by 05-29 EOD (rank 5, 6m +21.09%) but the 05-29 daily-loss halt blocked re-entry (`daily_loss_halt_active`). Refusing on the breach-cool-off + stale-bar session did not cost a good entry — the 05-29 halt would have blocked re-entry regardless; capital preserved.
- **#2 HOLD (5 names) — PARTIALLY RESOLVED.** All 5 held above their −10% rotation stops through 05-28 (prediction horizon) — "holds above stops" CORRECT. On 05-29 all 5 were closed by the daily-loss halt, NOT a stop/rotation; the implied "holds until rotation" was superseded by the halt mandate.
- **#3 UNH-STOP-WATCH — RESOLVED CORRECT.** UNH never breached its $352.71 stop (low ~$380; closed $380.89, +8% cushion). The pre_close flip noting XOM as the thinnest cushion was also accurate (XOM thinnest at 05-29 midday).
- **#4 CB-STABLE — RESOLVED CORRECT.** CB stayed FULL all 4 sessions; max DD 4.86% vs the 8% FULL→HALF trigger (3.1pp cushion at worst); no transition.
- **#5 MACRO-EVENT (05-28) — RESOLVED CORRECT.** GDP-2 / Core PCE printed in-line (GDP 1.6% vs 2.0% exp; Core PCE +3.3% YoY); no outsized gap in held names; the book held through the scheduled print by design.

**2026-05-28 EOD predictions (5):**
- **#1 DATA-FEED-STALE — RESOLVED CORRECT.** Daily bars refreshed on 05-29 (confirmed fresh in the EOD journal). The two stale sessions (05-27 ~26h, 05-28 ~44.8h) cleared on the next session, as the dominant branch anticipated.
- **#2 AMZN-DEFERRED-ENTRY — PARTIALLY RESOLVED.** AMZN re-confirmed rank-5 on the 05-29 fresh-bar run (signal re-qualified), but the daily-loss halt blocked execution. The deferral and the halt were both correct; AMZN entry becomes a 2026-06-01 evaluation. Still PENDING at the system level.
- **#3 HOLD (5 names) — PARTIALLY RESOLVED.** All 5 held above their −10% stops through 05-28 (scope); GOOGL (flagged thinnest at 05-28) never breached its $356.08 stop. Closed 05-29 by the halt.
- **#4 GOOGL-DRAWDOWN-WATCH — RESOLVED CORRECT.** GOOGL closed 05-29 at $382.62 vs its $356.08 stop = +7.5% above; the stop was never triggered. The watch tracked relative weakness correctly (GOOGL the 2nd-largest dollar loss, −$495) but the halt, not the stop, was the operative trigger.
- **#5 CB-STABLE — RESOLVED CORRECT.** CB stayed FULL through 05-29 despite DD 4.86% midday; no FULL→HALF transition; state-file write still skipped on the pending_broker artifact.

**Reconciliation tally:** 6 RESOLVED CORRECT, 4 PARTIALLY RESOLVED (the partial cases all share one cause: the 05-29 daily-loss halt superseded the per-name HOLD/entry horizon). 0 RESOLVED INCORRECT.

## Calibration snapshot (raw counts)
> Histogram of stated confidence vs realized outcome class. Raw counts only — no "overconfident"/"miscalibrated" judgment. Win-rate / Brier intentionally NOT computed: 6 closes this week, all forced by exogenous events (de-risk + halt), none allowed to run to a natural rotation/stop; cumulative post-reset closed sample still far below the v1 threshold.

| Confidence bucket | N (predictions this cycle) | Members | Outcome class (raw) |
|---|---|---|---|
| 0.30–0.39 | 2 | AMZN refusal 05-27 (0.35), AMZN refusal 05-28 (0.30) | Both refusals RESOLVED CORRECT (capital preserved; 05-29 halt would have blocked re-entry regardless). Honest low conviction on a stale/unreliable rank. |
| 0.50–0.59 | ~5 (held maintains) | 5x held maintains 05-28 (0.55–0.60) | All held above stops through the prediction horizon (05-28); closed 05-29 by halt, not stop. |
| 0.70–0.79 | 2 | 5x HOLD-horizon (≈0.70), GOOGL/UNH stop-watch (≈0.70–0.75) | HOLD CORRECT for horizon; stop-watch RESOLVED CORRECT (tracked thinnest name; no stop fired). |
| 0.80–0.89 | 2 | CB-STABLE 05-27 (≈0.85), CB-STABLE 05-28 (≈0.85) | Both CORRECT (FULL held; no transition). |

- The higher-confidence buckets again concentrated on mechanical/policy-state predictions (CB-state persistence, stale-bar refusal, halt behavior) rather than directional bets — consistent with the dichotomy noted in prior cycles. Directional/holding predictions clustered 0.50–0.75.
- **Risk Manager / Compliance calibration drift check: none observed.** Every actionable gate fired deterministically and was honored: the daily-loss halt (05-26, 05-29), the stale-bar refusal (05-27, 05-28), the data-fresh re-evaluation (05-29), and the `daily_loss_halt_active` re-entry block (05-29). No gate was bypassed. No `HALT_AND_REVIEW` recommendation is warranted on calibration grounds. The INTU compliance block was not implicated this cycle (INTU in no signal/decision).

## Surprises
> Descriptive only. Things that did not match symbol-profile or regime expectation. No conclusions.

- **First single-name macro shock to drive the daily-loss halt.** Prior cycles' daily-loss pressure was a diversified 4–5-name drag. This week XOM alone (energy beta) was the dominant contributor to TWO breaches (05-26, 05-29), same macro catalyst (US-Iran ceasefire / Strait of Hormuz; WTI ~−10% on the week). At a $160.43 entry on 97 sh, a 5%+ intraday XOM move alone consumes ~$750+ — exceeding the $500 daily-loss budget in isolation. This descriptively (N=1) answers the W21 open question on the soft-then-hard daily-loss dynamic under concentration.
- **Regime label vs portfolio experience diverged.** bullish_trend / medium held structurally all week (SPY never lost the 10mo SMA), yet the book was halted to cash by a commodity-sector shock the equity-trend signal does not capture. The loss was sector-specific, not breadth-driven.
- **No −10% per-name stop was ever breached** — on any of the 5 names, on any session, including the loss day. All closes were halt-forced or de-risk. Stop cushions at the 05-29 close: XOM +2.25%, GOOGL +7.5%, UNH +8.0%, CSCO +2.98%, GLD +1.45%. The daily-loss halt, not the rotation stop, was the operative exit mechanism.
- **GLD behaved as a working hedge at the moment it was liquidated.** On 05-29 GLD marked +1.74% midday (the only genuinely defensive line) while the portfolio was in daily-loss mode; the all-positions halt closed it (+$215 realized) alongside the loss names. (Recorded as a descriptive open policy question on the GLD profile; v1 makes no proposal.)
- **CSCO led the Strategy-B slate for a third consecutive week** (rank 1 throughout W22, 6m +57–61%), closed mid-upgrade cycle (BofA PT raise to $135 on 05-29, +$456 realized). Held through the crude/energy selloff without adverse impact (networking/tech, not energy-correlated).
- **Two consecutive stale-bar sessions** (05-27 ~26h, 05-28 ~44.8h) — not a market event but a recurring feed-health item; recovered fresh on 05-29. Signalled a feed problem, not a one-off.
- **CB equity-write skip persisted** on the pending_broker artifact (stale WMT/NVDA rows) across every session this week — the standing HIGH-severity defect did not clear.

## Open questions for future review (revisit at N ≥ 50 closed trades / ≥ 90 trading days)
- Is single-name energy (XOM) concentration a recurring source of daily-loss-halt risk, or was the twin US-Iran/crude shock a one-off coincidence? N=1 event (two same-driver days).
- Should the GLD permanent overlay be exempt from the all-positions daily-loss halt, given it was the only defensive line during the macro shock? Recorded as a descriptive observation only; needs a larger sample of stress events before any review.
- The W20/W21/W22 CSCO rank-1 persistence question remains open: three weeks of leadership with no mean-reversion toward the stop, but the position has always been closed by exogenous events (reset, then halt), never allowed to run to a natural rotation. Durable edge or unresolved-by-construction?
- Does the daily-loss-halt mechanism (which liquidated 3 winners alongside 3 losers this week) systematically interrupt winners? 6 closes is far too small to assess; revisit at scale.
- Does the recurring data-feed staleness (now 2 sessions this week) recur often enough to be a structural reliability issue vs intermittent?
- Will the CB equity-write skip (pending_broker artifact) ever block a genuine FULL→HALF detection when a real throttle window arrives? Non-recurrence of a genuine throttle this week does not retire the defect.
- What is the post-reset slippage-vs-quote distribution as the closed-trade sample grows?

---

**Cycle outputs (all under approved write paths; zero proposals; append-only where applicable):**
- Appended reconciliation sections: `memory/prediction_reviews/2026-05-27.md`, `memory/prediction_reviews/2026-05-28.md` (10 predictions reconciled; original rows unchanged).
- W22 symbol-profile observations: XOM, CSCO, GLD, GOOGL, UNH (appended; original sections unchanged).
- Regime history: `memory/market_regimes/history/2026-05-26.md` … `2026-05-29.md` (new, one file per session).
- Weekly regime summary: `memory/market_regimes/2026-w22.md` (new).
- This report.
- Zero writes to `prompts/proposed_updates/`. `.v2_enabled` absent → observations-only; the proposal pipeline stays dormant.
