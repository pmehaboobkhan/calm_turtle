routine: self_learning_review
started_at: '2026-05-24T14:01:51+00:00'
ended_at: '2026-05-24T14:15:00+00:00'
duration_seconds: 788.0
exit_reason: clean
approximate_input_kb: 161
total_subagent_dispatches: 2
subagent_dispatches:
  self_learning: 1
  compliance_safety: 1
files_read:
- path: config/approved_modes.yaml
  bytes: 1350
- path: config/risk_limits.yaml
  bytes: 5533
- path: config/watchlist.yaml
  bytes: 8108
- path: trades/paper/log.csv
  bytes: 4181
- path: trades/paper/positions.json
  bytes: 1125
- path: memory/prediction_reviews/2026-05-12.md
  bytes: 9623
- path: memory/prediction_reviews/2026-05-13.md
  bytes: 8722
- path: memory/prediction_reviews/2026-05-14.md
  bytes: 16568
- path: memory/prediction_reviews/2026-05-15.md
  bytes: 5554
- path: memory/prediction_reviews/2026-05-18.md
  bytes: 13301
- path: memory/prediction_reviews/2026-05-19.md
  bytes: 8181
- path: memory/prediction_reviews/2026-05-20.md
  bytes: 8894
- path: memory/prediction_reviews/2026-05-21.md
  bytes: 6640
- path: memory/prediction_reviews/2026-05-22.md
  bytes: 9359
- path: memory/agent_performance/2026-w21.md
  bytes: 4573
- path: memory/agent_performance/2026-w22.md
  bytes: 3803
- path: memory/strategy_lessons/2026-w20.md
  bytes: 2435
- path: memory/strategy_lessons/2026-w21.md
  bytes: 7159
- path: memory/market_regimes/current_regime.md
  bytes: 8566
- path: memory/market_regimes/history/2026-05-12.md
  bytes: 1182
- path: memory/market_regimes/history/2026-05-13.md
  bytes: 1298
- path: memory/market_regimes/history/2026-05-14.md
  bytes: 1190
- path: memory/market_regimes/history/2026-05-15.md
  bytes: 1444
- path: memory/symbol_profiles/CSCO.md
  bytes: 2406
- path: memory/symbol_profiles/GLD.md
  bytes: 2575
- path: memory/symbol_profiles/GOOGL.md
  bytes: 2068
- path: memory/symbol_profiles/NVDA.md
  bytes: 2439
- path: memory/symbol_profiles/WMT.md
  bytes: 3140
- path: memory/symbol_profiles/XOM.md
  bytes: 2415
- path: reports/learning/weekly_learning_review_2026-05-23.md
  bytes: 11540
artifacts_written:
- memory/prediction_reviews/2026-05-18.md
- memory/prediction_reviews/2026-05-19.md
- memory/prediction_reviews/2026-05-20.md
- memory/prediction_reviews/2026-05-21.md
- memory/symbol_profiles/CSCO.md
- memory/symbol_profiles/GLD.md
- memory/symbol_profiles/GOOGL.md
- memory/symbol_profiles/NVDA.md
- memory/symbol_profiles/WMT.md
- memory/symbol_profiles/XOM.md
- memory/symbol_profiles/UNH.md
- memory/market_regimes/2026-w21.md
- memory/market_regimes/history/2026-05-18.md
- memory/market_regimes/history/2026-05-19.md
- memory/market_regimes/history/2026-05-20.md
- memory/market_regimes/history/2026-05-21.md
- memory/market_regimes/history/2026-05-22.md
- reports/learning/observations_2026-05-24.md
commits:
- c6025a2
- 8460ec8
notes: v1 observations-only; 8 observations; 0 proposals (v1 cap); compliance APPROVED;
  2 HIGH-severity infra defects confirmed (CB in-flight, stop/target field loss)
