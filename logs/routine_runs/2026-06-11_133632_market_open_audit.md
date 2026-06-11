routine: market_open
started_at: '2026-06-11T13:36:32Z'
ended_at: '2026-06-11T13:37:56Z'
duration_seconds: 84.0
exit_reason: noop
approximate_input_kb: 18
total_subagent_dispatches: 2
subagent_dispatches:
  orchestrator: 1
  journal: 1
files_read:
- path: prompts/routines/market_open.md
  bytes: 11053
- path: config/approved_modes.yaml
  bytes: 1350
- path: config/risk_limits.yaml
  bytes: 5533
- path: trades/paper/circuit_breaker.json
  bytes: 147
- path: memory/daily_snapshots/2026-06-10.md
  bytes: 1135
artifacts_written:
- journals/daily/2026-06-11.md
- logs/routine_runs/20260611T133756Z_market_open_noop.md
commits: []
notes: No-op monitoring run. CB refresh skipped (1 pending broker order), state FULL
  carried fwd. 7/7 positions healthy, 0 closes, reconcile clean. Opening equity $99,704.43.
