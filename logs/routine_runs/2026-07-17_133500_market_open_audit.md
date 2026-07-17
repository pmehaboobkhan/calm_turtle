routine: market_open
started_at: '2026-07-17T13:35:00Z'
ended_at: '2026-07-17T13:38:30Z'
duration_seconds: 210.0
exit_reason: noop
approximate_input_kb: 47
total_subagent_dispatches: 0
subagent_dispatches: {}
files_read:
- path: CLAUDE.md
  bytes: 12273
- path: prompts/routines/market_open.md
  bytes: 11053
- path: config/approved_modes.yaml
  bytes: 1350
- path: trades/paper/positions.json
  bytes: 503
- path: trades/paper/circuit_breaker.json
  bytes: 139
- path: reports/pre_market/2026-07-17.md
  bytes: 12799
- path: memory/daily_snapshots/2026-07-16.md
  bytes: 897
- path: memory/daily_snapshots/2026-07-15.md
  bytes: 1000
- path: memory/daily_snapshots/2026-07-14.md
  bytes: 1399
- path: memory/daily_snapshots/2026-07-13.md
  bytes: 972
- path: memory/daily_snapshots/2026-07-09.md
  bytes: 970
- path: journals/daily/2026-07-17.md
  bytes: 4947
artifacts_written:
- journals/daily/2026-07-17.md
- logs/routine_runs/20260717T133752Z_market_open_noop.md
commits: []
notes: Pure no-op. 2 held (SPY/GOOGL), health clean, no closes. CB refresh skipped
  Guard1 (6 pending broker), FULL carried. Reconcile clean 2/2. Snapshot for today
  missing so full pre-market report read (allowed); no raw market dumps or full prior
  journals slurped.
