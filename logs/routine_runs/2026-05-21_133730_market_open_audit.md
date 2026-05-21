routine: market_open
started_at: '2026-05-21T13:37:30Z'
ended_at: '2026-05-21T13:39:30Z'
duration_seconds: 120.0
exit_reason: noop
approximate_input_kb: 65
total_subagent_dispatches: 0
subagent_dispatches: {}
files_read:
- path: CLAUDE.md
  bytes: 12237
- path: prompts/routines/market_open.md
  bytes: 9888
- path: config/approved_modes.yaml
  bytes: 1350
- path: config/risk_limits.yaml
  bytes: 5533
- path: config/watchlist.yaml
  bytes: 8108
- path: config/strategy_rules.yaml
  bytes: 3803
- path: config/routine_schedule.yaml
  bytes: 2340
- path: trades/paper/positions.json
  bytes: 1125
- path: trades/paper/circuit_breaker.json
  bytes: 139
- path: reports/pre_market/2026-05-21.md
  bytes: 13776
- path: journals/daily/2026-05-21.md
  bytes: 5131
- path: logs/routine_runs/20260520_134129Z_market_open_noop.md
  bytes: 3806
artifacts_written:
- journals/daily/2026-05-21.md
- logs/routine_runs/20260521_133849Z_market_open_noop.md
commits: []
notes: 'Monitoring no-op: CB FULL->FULL (DD 2.68%), 5 positions all above stops, 0
  closes, reconcile clean. Daily snapshot 2026-05-21.md missing -> read full pre-market
  report (allowed); flag as minor pre-market regression.'
