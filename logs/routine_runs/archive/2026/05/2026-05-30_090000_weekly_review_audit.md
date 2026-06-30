routine: weekly_review
started_at: '2026-05-30T09:00:00Z'
ended_at: '2026-05-30T09:45:00Z'
duration_seconds: 2700.0
exit_reason: clean
approximate_input_kb: 201
total_subagent_dispatches: 3
subagent_dispatches:
  performance_review: 1
  self_learning: 1
  compliance_safety: 1
files_read:
- path: CLAUDE.md
  bytes: 12273
- path: config/approved_modes.yaml
  bytes: 1350
- path: prompts/routines/weekly_review.md
  bytes: 6932
- path: .claude/agents/orchestrator.md
  bytes: 4241
- path: trades/paper/log.csv
  bytes: 6389
- path: trades/paper/positions.json
  bytes: 3
- path: journals/daily/2026-05-26.md
  bytes: 25322
- path: journals/daily/2026-05-27.md
  bytes: 37926
- path: journals/daily/2026-05-28.md
  bytes: 19796
- path: journals/daily/2026-05-29.md
  bytes: 19961
- path: journals/weekly/2026-21.md
  bytes: 17908
- path: config/risk_limits.yaml
  bytes: 5533
- path: memory/agent_performance/2026-w22.md
  bytes: 3803
- path: memory/strategy_lessons/2026-w21.md
  bytes: 7159
- path: memory/prediction_reviews/2026-05-26.md
  bytes: 7888
- path: memory/market_regimes/current_regime.md
  bytes: 8566
- path: decisions/by_symbol/XOM.md
  bytes: 9338
- path: decisions/by_symbol/GLD.md
  bytes: 11584
artifacts_written:
- journals/weekly/2026-22.md
- reports/learning/weekly_learning_review_2026-05-30.md
- reports/weekly_digest/2026-22.md
- memory/strategy_lessons/2026-w22.md
- memory/agent_performance/2026-w23.md
- decisions/by_symbol/CSCO.md
- decisions/by_symbol/GLD.md
- decisions/by_symbol/GOOGL.md
- decisions/by_symbol/UNH.md
- decisions/by_symbol/XOM.md
- decisions/by_symbol/NVDA.md
commits: []
notes: "W22 review: 4 trading days, 6 closed trades, 2 daily-loss breaches (05-26/05-29\
  \ same crude/Iran driver); STAY_PAPER. self_learning agent hit 529 overloaded \u2014\
  \ lessons written inline. compliance_safety running async."
