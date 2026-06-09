routine: market_open
started_at: '2026-06-09T09:35:00-04:00'
ended_at: '2026-06-09T09:37:30-04:00'
duration_seconds: 150.0
exit_reason: noop
approximate_input_kb: 52
total_subagent_dispatches: 0
subagent_dispatches: {}
files_read:
- path: CLAUDE.md
  bytes: 12273
- path: prompts/routines/market_open.md
  bytes: 11053
- path: config/approved_modes.yaml
  bytes: 1350
- path: config/risk_limits.yaml
  bytes: 5533
- path: trades/paper/positions.json
  bytes: 1747
- path: trades/paper/circuit_breaker.json
  bytes: 139
- path: reports/pre_market/2026-06-09.md
  bytes: 16185
- path: memory/daily_snapshots/2026-06-08.md
  bytes: 1318
- path: journals/daily/2026-06-09.md
  bytes: 4425
artifacts_written:
- journals/daily/2026-06-09.md
- logs/routine_runs/20260609T133500_market_open_noop.md
commits: []
notes: 'No-op: CB refresh skipped (1 pending broker order, carry FULL); 0/7 health
  closes; reconcile clean. Today''s daily_snapshot missing -> fell back to pre_market
  report (allowed). No commit, no Telegram.'
