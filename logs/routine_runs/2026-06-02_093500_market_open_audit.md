routine: market_open
started_at: '2026-06-02T09:35:00+00:00'
ended_at: '2026-06-02T13:36:51.480529+00:00'
duration_seconds: 14511.48
exit_reason: noop
approximate_input_kb: 2
total_subagent_dispatches: 1
subagent_dispatches:
  orchestrator: 1
files_read:
- path: config/approved_modes.yaml
  bytes: 1350
- path: trades/paper/positions.json
  bytes: 3
- path: memory/daily_snapshots/2026-06-01.md
  bytes: 1154
artifacts_written:
- journals/daily/2026-06-02.md
- logs/routine_runs/20260602_133631_market_open_noop.md
commits: []
notes: 'No open positions; steps 5-8 skipped. Schema validation passed. CB state not
  refreshed (no positions). Stale PENDING_BROKER rows still blocking CB write (operator
  action needed: sync_alpaca_state.py).'
