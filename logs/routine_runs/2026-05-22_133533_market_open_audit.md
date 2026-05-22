routine: market_open
started_at: '2026-05-22T13:35:33+00:00'
ended_at: '2026-05-22T13:37:12+00:00'
duration_seconds: 99.0
exit_reason: noop
approximate_input_kb: 59
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
- path: trades/paper/positions.json
  bytes: 1125
- path: trades/paper/circuit_breaker.json
  bytes: 139
- path: reports/pre_market/2026-05-22.md
  bytes: 10924
- path: journals/daily/2026-05-22.md
  bytes: 6865
- path: memory/daily_snapshots/2026-05-21.md
  bytes: 1005
artifacts_written:
- journals/daily/2026-05-22.md
- logs/routine_runs/2026-05-22_133712_market_open_noop.md
commits: []
notes: 'Pure no-op: CB FULL->FULL (DD 2.36%, recovered from 4.34%), 0 positions to
  close, reconcile clean (0 discrepancies). No daily snapshot for 2026-05-22 existed
  so full pre-market report read per snapshot-missing allowance (flagged for snapshot-job
  check). ENTRY signals ignored by design.'
