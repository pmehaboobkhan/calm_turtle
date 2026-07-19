routine: self_learning_review
started_at: '2026-07-19T14:02:03Z'
ended_at: '2026-07-19T14:17:12Z'
duration_seconds: 909.0
exit_reason: clean
approximate_input_kb: 165
total_subagent_dispatches: 2
subagent_dispatches:
  self_learning: 1
  compliance_safety: 1
files_read:
- path: CLAUDE.md
  bytes: 12273
- path: prompts/routines/self_learning_review.md
  bytes: 6944
- path: config/approved_modes.yaml
  bytes: 1350
- path: config/risk_limits.yaml
  bytes: 5533
- path: config/watchlist.yaml
  bytes: 8108
- path: docs/commit_messages.md
  bytes: 1545
- path: .claude/agents/self_learning.md
  bytes: 7689
- path: memory/market_regimes/current_regime.md
  bytes: 17184
- path: memory/prediction_reviews/2026-07-13.md
  bytes: 6498
- path: memory/prediction_reviews/2026-07-14.md
  bytes: 4897
- path: memory/prediction_reviews/2026-07-15.md
  bytes: 4665
- path: memory/prediction_reviews/2026-07-16.md
  bytes: 5931
- path: memory/prediction_reviews/2026-07-17.md
  bytes: 4427
- path: memory/agent_performance/2026-w29.md
  bytes: 9032
- path: memory/agent_performance/2026-w30.md
  bytes: 13750
- path: memory/market_regimes/history/2026-07-17.md
  bytes: 4386
- path: memory/symbol_profiles/JNJ.md
  bytes: 3725
- path: memory/symbol_profiles/UNH.md
  bytes: 6452
- path: memory/symbol_profiles/GOOGL.md
  bytes: 6401
- path: reports/learning/weekly_learning_review_2026-07-11.md
  bytes: 20048
- path: reports/learning/observations_2026-07-19.md
  bytes: 6753
- path: trades/paper/positions.json
  bytes: 250
- path: trades/paper/log.csv
  bytes: 11358
artifacts_written:
- memory/prediction_reviews/2026-07-13.md
- memory/prediction_reviews/2026-07-16.md
- memory/prediction_reviews/2026-07-17.md
- memory/agent_performance/2026-w30.md
- memory/symbol_profiles/JNJ.md
- memory/symbol_profiles/UNH.md
- memory/symbol_profiles/GOOGL.md
- memory/market_regimes/history/2026-07-17.md
- reports/learning/observations_2026-07-19.md
- decisions/by_symbol/JNJ.md
- decisions/by_symbol/UNH.md
- decisions/by_symbol/GOOGL.md
- decisions/by_symbol/NVDA.md
- decisions/by_symbol/CSCO.md
- decisions/by_symbol/XOM.md
- decisions/by_symbol/GLD.md
commits:
- e2c4b75
notes: 'v1 observations-only (PAPER_TRADING; .v2_enabled absent). W29 (07-13->07-17)
  review: 16 observation artifacts, 0 proposals, 0 rejected. 3 closes reconciled (JNJ/UNH
  wins, GOOGL loss); 6 predictions resolved + ~20 inline, 3 groups deferred on ~22d
  feed staleness. RM/Compliance NO DRIFT. Compliance APPROVED. Telegram sent (text+1
  doc). approx_input_kb=165 (cap 200). 2 subagent dispatches (cap 20). Commit e2c4b75
  local; push/PR left to operator per instruction.'
