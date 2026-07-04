routine: weekly_review
started_at: '2026-07-04T13:00:59Z'
ended_at: '2026-07-04T13:45:00Z'
duration_seconds: 2641.0
exit_reason: clean
approximate_input_kb: 263
total_subagent_dispatches: 4
subagent_dispatches:
  orchestrator: 1
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
- path: config/watchlist.yaml
  bytes: 8108
- path: config/risk_limits.yaml
  bytes: 5533
- path: config/strategy_rules.yaml
  bytes: 3803
- path: config/routine_schedule.yaml
  bytes: 2340
- path: docs/commit_messages.md
  bytes: 1545
- path: journals/weekly/2026-23.md
  bytes: 21860
- path: reports/weekly_digest/2026-23.md
  bytes: 4175
- path: journals/daily/2026-06-30.md
  bytes: 18962
- path: journals/daily/2026-07-01.md
  bytes: 18527
- path: journals/daily/2026-07-02.md
  bytes: 18321
- path: journals/daily/2026-07-03.md
  bytes: 24945
- path: journals/daily/2026-06-12.md
  bytes: 4196
- path: trades/paper/positions.json
  bytes: 998
- path: trades/paper/circuit_breaker.json
  bytes: 139
- path: trades/paper/circuit_breaker_history.jsonl
  bytes: 329
- path: trades/paper/log.csv
  bytes: 9847
- path: trades/paper/position_meta.json
  bytes: 843
- path: memory/agent_performance/2026-w24.md
  bytes: 8311
- path: memory/agent_performance/2026-w23.md
  bytes: 15417
- path: memory/agent_performance/2026-w22.md
  bytes: 3803
- path: memory/agent_performance/2026-w21.md
  bytes: 4573
- path: memory/strategy_lessons/2026-w20.md
  bytes: 2435
- path: memory/strategy_lessons/2026-w21.md
  bytes: 7159
- path: memory/strategy_lessons/2026-w22.md
  bytes: 8800
- path: memory/strategy_lessons/2026-w23.md
  bytes: 7637
- path: memory/market_regimes/current_regime.md
  bytes: 6133
- path: decisions/by_symbol/GLD.md
  bytes: 19280
- path: decisions/2026-06-08/1635_GLD.json
  bytes: 3673
- path: logs/routine_runs/2026-06-29_160712_start.md
  bytes: 105
- path: reports/learning/weekly_learning_review_2026-06-06.md
  bytes: 12916
artifacts_written:
- journals/weekly/2026-27.md
- reports/learning/weekly_learning_review_2026-07-04.md
- reports/weekly_digest/2026-27.md
- memory/agent_performance/2026-w28.md
- memory/strategy_lessons/2026-w27.md
- decisions/by_symbol/CSCO.md
- decisions/by_symbol/NVDA.md
- decisions/by_symbol/XOM.md
- memory/symbol_profiles/CSCO.md
- memory/symbol_profiles/NVDA.md
- memory/symbol_profiles/XOM.md
commits: []
notes: 'Mode PAPER_TRADING throughout, no HALT/SAFE_MODE handling needed. Top finding:
  total operational blackout ISO weeks 25-26 (2026-06-15 to 2026-06-26, zero routines
  ran) plus an unreviewed W24 -- flagged MUST-FIX for operator, not actioned (out
  of Claude Code scope). Second MUST-FIX: circuit_breaker.json unwritten since 2026-06-11
  (stuck pending-broker Guard-1, count grown to 4). W27 trading activity: 3 stop-loss
  closes (CSCO/NVDA/XOM, -$1,114.19 realized), 0 new entries (stale daily bars). Corrected
  a performance_review subagent undercount (3 vs actual 4 all-time closed trades post-06-04-reset,
  missing the 06-08 GLD close) directly in memory/agent_performance/2026-w28.md via
  an appended correction note. Compliance verdict: APPROVED (compliance_safety agent,
  8/8 checks pass).'
