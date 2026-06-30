routine: market_open
started_at: '2026-05-29T13:38:22Z'
ended_at: '2026-05-29T13:39:40Z'
duration_seconds: 78.0
exit_reason: noop
approximate_input_kb: 46
total_subagent_dispatches: 0
subagent_dispatches: {}
files_read:
- path: CLAUDE.md
  bytes: 12273
- path: config/approved_modes.yaml
  bytes: 1350
- path: config/watchlist.yaml
  bytes: 8108
- path: config/risk_limits.yaml
  bytes: 5533
- path: trades/paper/positions.json
  bytes: 1125
- path: trades/paper/log.csv
  bytes: 4532
- path: memory/market_regimes/current_regime.md
  bytes: 8566
- path: journals/daily/2026-05-29.md
  bytes: 4443
- path: logs/routine_runs/20260529T133751Z_market_open_noop.md
  bytes: 1569
artifacts_written:
- logs/routine_runs/20260529T133927Z_market_open_noop.md
commits: []
notes: 'market_open re-run; pure no-op: CB write skipped (pending_broker=2, FULL carried),
  health to_close empty, reconcile clean, 0 closes, no commit'
