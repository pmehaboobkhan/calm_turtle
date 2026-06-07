# Observations — self_learning_review 2026-06-07

> v1 observations-only mode (`prompts/proposed_updates/.v2_enabled` absent; mode PAPER_TRADING, not SAFE_MODE — learning writes permitted). This report records; it does not prescribe. Zero proposals written. Sample sizes remain far below v1 thresholds (≥ 90 trading days AND ≥ 50 paper trades). As of this review: 14 trading days cumulative, 7 all-time closed trades. Any "pattern" here is overwhelmingly likely to be noise. Observations are separated from conclusions; no conclusions drawn.

## Period
- **Self-learning review date:** 2026-06-07 (Sunday)
- **Trading days covered:** 2026-06-01 → 2026-06-05 (W23, 5 trading days)
- **Reconciliation window:** 2026-06-01 → 2026-06-05 (W23 predictions; all prior W22 predictions resolved via observations_2026-05-31 and weekly_learning_review_2026-06-06)
- **Portfolio state at review:** 5 PENDING_BROKER orders (GLD/CSCO/XOM/UNH/NVDA) awaiting 06-08 open fill; 100% cash mark-to-market; equity $100,577.97 (DD 3.38% from all-time peak $104,090.72).
- **Closed trades this cycle:** 0 (no fills executed in W23; all entry orders PENDING_BROKER at week-end)
- **Net realized PnL this cycle:** $0.00
- **Decisions written:** 35 (6 symbols × 4 stale-data sessions = 24; 5 PAPER_BUY + 2 NO_TRADE on 06-05; 4 subsumed GLD-overlay stubs)

## Predictions reconciled this cycle

### Reconciled now (2026-06-07): predictions from 2026-06-01 and 2026-06-02 EOD files
> Note: the weekly_learning_review_2026-06-06 already captured these outcomes in narrative form. This cycle formally appends reconciliation rows to the original prediction_reviews files (append-only).

**From 2026-06-01 (7 predictions): 6 CORRECT / 1 INCORRECT**
- Data freshness (0.60): **INCORRECT** — lag persisted 4 sessions, not 1.
- CB stays blocked until sync (0.85): **CORRECT** — block held; cleared 06-04 by operator sync.
- GLD top-1 (0.70): **CORRECT** — GLD Strategy-A top-1 on 06-05 close.
- CSCO rank-1 (0.75): **CORRECT** — CSCO rank-1 (+70.94% 6m) on 06-05.
- NVDA top-5 (0.65): **CORRECT** — NVDA rank-4 on 06-05.
- UNH top-5 (0.55): **CORRECT** — UNH rank-3 on 06-05.
- AMZN rank-5 boundary fragile (0.50): **CORRECT** — AMZN dropped out by 06-02; ORCL/UNH rotated in.

**From 2026-06-02 (8 predictions): 7 CORRECT / 1 INCORRECT**
- Data freshness persists (0.55): **CORRECT** — lag ran 3 more sessions (06-03, 06-04, 06-05 feed recovery).
- CB stays blocked (0.90): **CORRECT** — block held; cleared 06-04.
- GLD top-1 (0.70): **CORRECT**.
- CSCO rank-1 (0.75): **CORRECT**.
- XOM qualifies (0.60): **CORRECT** — XOM rank-2 on 06-05.
- NVDA top-5 (0.65): **CORRECT**.
- ORCL most fragile (0.55): **INCORRECT** — ORCL held rank-4/5; the rapid-climb prior was wrong.
- GOOGL boundary-fragile (0.50): **CORRECT** — GOOGL dropped to hold-zone within one session.

**Cumulative this cycle:** 13 CORRECT / 2 INCORRECT out of 15 predictions reconciled.

### Predictions still open at review (from 2026-06-05 EOD)
All 6 predictions in `memory/prediction_reviews/2026-06-05.md` remain PENDING:
1. FILL-CONFIRMATION (0.85) — resolves 2026-06-08 open
2. SLATE-HOLD (0.75) — resolves 2026-06-08
3. CSCO-REVERSION-WATCH (0.55) — rolling 1–2 week horizon
4. ORCL-EARNINGS (0.70) — resolves 2026-06-09 pre_close
5. CB-STABLE (0.90) — resolves 2026-06-08
6. XOM-ENERGY-BETA (0.50) — rolling horizon

## Calibration snapshot (raw counts, W23)
> No win-rate or Brier calculation. N=0 closed trades this week; all returns zero. Histograms are descriptive bookkeeping only.

| Confidence bucket | N predictions this cycle | Members | Outcome class |
|---|---|---|---|
| 0.50 | 2 | AMZN boundary (0.50), GOOGL boundary (0.50) | Both CORRECT (boundary swaps materialized as predicted) |
| 0.55–0.60 | 4 | UNH top-5 (0.55), ORCL fragile (0.55), data fresh 06-01 (0.60), data fresh 06-02 (0.55) | 2 CORRECT (UNH, data-06-02), 1 INCORRECT (ORCL), 1 INCORRECT (data-06-01) |
| 0.65–0.70 | 4 | NVDA top-5 (0.65) ×2, GLD top-1 (0.70) ×2 | All CORRECT |
| 0.75 | 2 | CSCO rank-1 ×2 | Both CORRECT |
| 0.85–0.90 | 2 | CB-blocked (0.85), CB-blocked (0.90) | Both CORRECT |

**Calibration notes (descriptive):**
- The 0.85–0.90 bucket (CB process-state predictions) continues its perfect record (5/5 all-time correct). Mechanical/policy-state predictions remain the most reliable.
- The 0.50 boundary predictions landed correctly 2/2 — appropriate coin-flip framing for single-bar boundary instability.
- The data-freshness predictions in the 0.55–0.60 bucket were mixed: the "pessimistic" (lag persists) branch was correctly modeled as likely; however the initial "will self-heal in 1 session" call (06-01) was wrong in magnitude.
- ORCL fragility (0.55) was the only rank prediction to miss this cycle — directionally wrong. The rapid-rank-climb prior appears to be negatively correlated with fragility, not positively.

**Risk Manager / Compliance calibration drift check:** No drift observed. All deterministic staleness-gate refusals (Rule #5, RM check #11) fired correctly. All 5 PAPER_BUY on 06-05 were RM APPROVED + Compliance APPROVED. No HALT_AND_REVIEW warranted.

## Surprises (descriptive, not conclusions)
- **META NaN close** caused a spurious rank-1 in the signal evaluator (06-04 pre_market data) — the first instance of NaN contamination in paper-trading history. The pre_market correctly identified it; the deterministic pipeline silently accepted it. Self-resolved by the 06-05 close.
- **The stale-data streak (4 sessions) is the longest in system history.** The bullish_trend regime was maintained throughout, but the portfolio could not participate. Regime and portfolio experience were fully decoupled by an operational outage.
- **ORCL durability:** ORCL entered the top-5 at rank 20→4 in 12 days (a rapid climb) and stayed there across all 5 W23 sessions on the fresh-bar scans. The "new entrant = fragile" prior (N=1 prior observation, AMZN boundary fragility) does not appear to generalize. ORCL and AMZN behaved oppositely: ORCL climbed and held; AMZN held a thin boundary and slipped.
- **CSCO rank-1 persistence (4 weeks running).** CSCO's 6m return expanded from +54% (W21) to +71% (W23-end) without mean-reversion toward the stop. It now holds the largest momentum lead in the system's history. Whether this is durable leadership or late-cycle extension is unobserved at N=4 weeks.
- **CB write-block resolved without spurious state.** The Guard-1 design (skip write when pending_broker > 0) held perfectly for 17 calendar days without ever recording a false CB state or missing a transition. The recovery was immediate once the operator cleared the block.

## Open observations for future review (revisit at N ≥ 50 closed trades / ≥ 90 trading days)

1. **Rapid-rank-climb fragility.** ORCL (rank 20→4 in 12 days) proved MORE durable than a slower-ascending name (AMZN, rank 6→5, dropped at the first fresh bar). Is momentum-of-momentum (fast rank rise) a positive durability signal? N=2 names, opposite outcomes — no conclusion, but the prior is mis-specified.

2. **CSCO elastic-snap timing.** CSCO at +70.94% 6m is the most-stretched name in paper history (all prior observations: +54–61%). Is there a return threshold above which mean-reversion becomes more likely? The current book opened with CSCO at +71%; W24 will be the first real-time test of the "stretched rank-1" thesis.

3. **Data-provider staleness frequency.** W23 produced the longest stale-data streak (4 EODs). W22 had 2 stale sessions (05-27/28). Prior weeks had zero. Pattern: 2 clusters of staleness in the ~4-week post-reset period. Is this provider-specific (settle-time), weekday-specific, or random? Insufficient N.

4. **XOM energy-beta at LOW sizing.** First test of the W22 memory-driven sizing response. W23 had 0 XOM fills; W24 will be the first live test. Outcome tracked in XOM.md after 06-08 open confirms fill.

5. **GLD halt-exemption policy.** Open since W22: should the permanent GLD overlay be exempt from the all-positions daily-loss halt? W23 produced no new evidence (book was flat). Open question for the N≥50 review.

6. **Staleness streak → escalation threshold.** W23 demonstrated that 4 consecutive stale EODs can pass without an automated operator alert. The only notification was the weekly review email. An intra-week escalation mechanism (URGENT Telegram at N≥3 consecutive stale EODs) would have surfaced this by June 3. Open for operator/engineering action.

## Cycle outputs (all under approved write paths; zero proposals; append-only where applicable)

- Appended reconciliation sections to: `memory/prediction_reviews/2026-06-01.md`, `memory/prediction_reviews/2026-06-02.md` (15 predictions reconciled total).
- Created regime history files: `memory/market_regimes/history/2026-06-01.md` → `2026-06-05.md` (5 new files).
- Created weekly regime summary: `memory/market_regimes/2026-w23.md`.
- This report: `reports/learning/observations_2026-06-07.md`.
- Zero writes to `prompts/proposed_updates/`. `.v2_enabled` absent → proposals pipeline dormant.
- Symbol-profile updates: **none this cycle** (0 closed trades in W23; no new outcome observations for any name).

---

*Generated: 2026-06-07T10:00:00Z by self_learning agent. Mode: PAPER_TRADING.*
*All-time closed trades: 7 (below N≥50 v1 threshold). All-time trading days: 14 (below N≥90 threshold).*
