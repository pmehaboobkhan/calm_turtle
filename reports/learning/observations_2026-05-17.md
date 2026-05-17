# Observations — week ending 2026-05-17

> v1 observations-only mode (`prompts/proposed_updates/.v2_enabled` absent). This report records; it does not prescribe. Zero proposals. Sample sizes are far below the v1 thresholds (≥ 90 trading days AND ≥ 50 paper trades). With 4 trading days and 1 closed trade, any "pattern" here is overwhelmingly likely to be noise; this document deliberately separates observations from conclusions and draws no conclusions.

## Period
- Trading days: 4 (2026-05-12 → 2026-05-15) — the first ever paper-trading week.
- Decisions: 16 (5 PAPER_BUY + 1 PAPER_CLOSE + 8 NO_TRADE + 2 held-position re-confirms recorded as intermediate, non-win/loss data points).
- Paper trades opened: 5 (GLD, GOOGL, XOM, CSCO, WMT — all 2026-05-12).
- Paper trades closed: 1 (CSCO, 2026-05-13 pre_close, +$618.90, +10.13%).
- Positions reset administratively (not a strategy exit): 4 (GLD, GOOGL, WMT, XOM) by `scripts/sync_alpaca_state.py --reset-fresh-start` at 2026-05-15T00:31:53Z.

## Predictions reconciled this week
> 15 of 16 predictions reconciled this cycle (the 2026-05-15 GLD-overlay NO_TRADE remains pending). Outcome lines were appended (append-only) to `memory/prediction_reviews/2026-05-12.md`, `2026-05-13.md`, `2026-05-14.md`, `2026-05-15.md` under `## Outcome annotation (self_learning_review 2026-05-17)` sections. No original rows were edited.

- `memory/prediction_reviews/2026-05-13.md` P1 — CSCO PAPER_CLOSE (+$618.90, +10.13%): procedurally correct (pre-earnings exit followed the playbook); directionally sub-optimal (post-print IEX last ≈ $121.25 on a wide $109.35/$121.25 spread implied a ~20% gap up; the stock closed below $121 by EOD). Left catalyst-day continuation on the table — the explicit, accepted trade-off of the earnings-exit playbook. No conclusion drawn (N=1).
- `memory/prediction_reviews/2026-05-12.md` P6 — JNJ NO_TRADE (max_trades cap): benign deferral. JNJ slipped to rank 6 (NO_SIGNAL) on 2026-05-13, returned to rank 5 on 2026-05-15 after the reset. The capped entry would have been a boundary oscillator.
- `memory/prediction_reviews/2026-05-13.md` P2 — AMZN NO_TRADE (CB OUT + stale): benign. Rank 5 (2026-05-13) → rank 6 (2026-05-14). 1-day boundary promotion; deferral costless.
- `memory/prediction_reviews/2026-05-14.md` P1 — NVDA NO_TRADE (CB OUT + stale): benign. Rank 7 → rank 5 (2026-05-14) → rank 7 (2026-05-15). 2-day boundary promotion; deferral costless.
- `memory/prediction_reviews/2026-05-12.md` P1–P3, P5 — GLD/GOOGL/XOM/WMT PAPER_BUY: reset-terminated (no signal invalidation). Final marks before reset: GLD ≈ $428 (≈ −$94 unrealized), GOOGL ≈ $401 (≈ +$57), XOM ≈ $153 (≈ +$156), WMT ≈ $132 (≈ +$87). No stop trip, rank-out, or SPY 10m MA break occurred while held. Excluded from win-rate math by design.
- `memory/prediction_reviews/2026-05-12.md` P7 — GLD overlay NO_TRADE (subsumed): subsumed for the full hold; administratively moot post-reset.
- `memory/prediction_reviews/2026-05-13.md` P3 and `2026-05-14.md` P2 — CSCO re-entry NO_TRADE chain: reset-terminated (procedurally consistent). Stacked gates (CB OUT + earnings window + data staleness + post-earnings-stale-bar) never cleared; book reset before any fresh post-earnings bar. Never re-opened before the print resolved.
- `memory/prediction_reviews/2026-05-14.md` P3–P6 — GLD/GOOGL/WMT/XOM held-position re-confirms: held until reset, no invalidation triggered. Intermediate mid-hold marks, not win/loss data points.
- `memory/prediction_reviews/2026-05-15.md` P1 — GLD overlay NO_TRADE (data unavailable): still pending. Data feed not restored as of 2026-05-17. No action this cycle.

## Calibration snapshot
> Histogram of stated confidence vs realized outcome class. Raw counts only — no "overconfident"/"miscalibrated" judgment. Full ledger in `memory/agent_performance/2026-w21.md`.

| Confidence bucket | N | Members | Outcomes (raw) |
|---|---|---|---|
| 0.45–0.55 | 2 | CSCO BUY (0.55), CSCO re-entry NO_TRADE underlying thesis (0.45) | 1 positive (CSCO BUY → +$618.90 exit); 1 reset-terminated |
| 0.55–0.65 | 4 | GOOGL BUY (0.62), GLD BUY (0.62), XOM BUY (0.60), WMT BUY (0.58) | 4 reset-terminated (no win/loss signal extractable) |
| 0.75–0.85 | 4 | CSCO CLOSE (0.85), GLD hold (0.85), GOOGL hold (0.80), XOM hold (0.80) | 1 procedurally correct (CSCO CLOSE); 3 reset-terminated |
| ≥ 0.90 | 5 | AMZN NO_TRADE (0.95), CSCO re-entry NO_TRADE (0.95), NVDA NO_TRADE (0.95), NVDA-day NO_TRADE (0.95), GLD data NO_TRADE (0.98) | 4 benign / 1 pending |

- Win-rate / Brier calibration is intentionally NOT computed: only 4 of 16 predictions have clear non-administrative outcomes; 8 are reset-terminated; 4 pending. N is far below the threshold.
- The ≥ 0.90 bucket is exclusively NO_TRADE routing confidence on mechanical/hard gates (CB OUT, data staleness, total blackout, max_trades cap). The paired underlying-thesis confidences for those same decisions were all ≤ 0.55 by design — an intentional dichotomy documented in the daily prediction-review files.
- Risk Manager / Compliance calibration drift check: none observed. No HALT_AND_REVIEW recommendation warranted on calibration grounds. Every actionable gate fired deterministically and was honored; no gate was bypassed. The 2026-05-15 reset was an administrative script action, not a risk/compliance failure.

## Surprises
> Descriptive only. Things that did not match symbol-profile or regime expectation.

- A circuit-breaker peak-inflation artifact persisted across 7 consecutive routines before the 2026-05-15 reset incidentally resolved it. Operationally it coincided with blocking 4 distinct would-be opens (AMZN ×1, CSCO ×2, NVDA ×1) via the CB-OUT gate.
- Feed step-back on 2026-05-13: daily bars rolled backward from 2026-05-07 to 2026-04-24, which moved the regime label up to `bullish_trend / medium` on an *older* bar. The detector computed correctly for its inputs; the inputs regressed.
- Total data blackout on 2026-05-15 (yfinance host blocked; all 25 symbols failed). The EOD regime degraded honestly to `uncertain / low confidence` rather than carrying a stale label.
- CSCO gapped ≈ 20% post-earnings (IEX-implied; wide spread) — the largest single-session gap surprise of the week. The pre-print exit captured +10.13% before the gap and, by design, did not capture the continuation above the exit price.
- Synchronized late-day reversal across GOOGL / WMT / XOM in the final ~25 minutes on 2026-05-13 (≈ −4% to −6% pre_close→EOD), fully reversed during the 2026-05-14 session. Inconsistent with the day's `bullish_trend / medium` label; recorded without conclusion.

## Open questions for future review (revisit at N ≥ 50 closed trades / ≥ 90 trading days)
- Is the CSCO pre-earnings-exit playbook reliably portable to WMT (Q1 FY27 BMO 2026-05-21)? Currently N=1 sample.
- Is rank-5 boundary churn (JNJ ↔ AMZN ↔ NVDA rotating around the top-5 cutoff) a consistent structural pattern or signal jitter? 3 data points so far.
- Does the observed GLD 12m-return decay pace (≈ −4pp/week) represent a real rotation signal over the next 4–6 weeks, or within-window noise?
- Will data-feed restoration unblock the queued ENTRY candidates (CSCO re-entry, NVDA, the GLD overlay, and any Strategy A/B confirmations), and at what prices relative to the pre-blackout marks?
- Did the CB peak-inflation artifact materially change which signals were actionable, or were all 4 blocked opens boundary noise that would have been benign anyway?
