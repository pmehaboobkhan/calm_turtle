routine: market_open
started_at: '2026-07-09T13:36:34Z'
ended_at: '2026-07-09T13:39:00Z'
duration_seconds: 146.0
exit_reason: noop
approximate_input_kb: 50
total_subagent_dispatches: 0
subagent_dispatches: {}
files_read:
- path: CLAUDE.md
  bytes: 12273
- path: prompts/routines/market_open.md
  bytes: 11053
- path: config/approved_modes.yaml
  bytes: 1350
- path: config/watchlist.yaml
  bytes: 8108
- path: config/risk_limits.yaml
  bytes: 5533
- path: config/strategy_rules.yaml
  bytes: 3803
- path: config/routine_schedule.yaml
  bytes: 2340
- path: trades/paper/positions.json
  bytes: 998
- path: trades/paper/circuit_breaker.json
  bytes: 139
- path: journals/daily/2026-07-09.md
  bytes: 4929
- path: memory/daily_snapshots/2026-07-08.md
  bytes: 981
artifacts_written:
- journals/daily/2026-07-09.md
- logs/routine_runs/20260709T133829Z_market_open_noop.md
commits: []
notes: 'No-op: 4 positions healthy, 0 closes; CB refresh skipped (4 pending broker
  orders, known finalizer bug), FULL carried; reconcile clean. Read snapshot not full
  prior journal per context budget.'
