routine: market_open
started_at: '2026-05-20T13:36:20+00:00'
ended_at: '2026-05-20T13:39:26+00:00'
duration_seconds: 186.0
exit_reason: clean
approximate_input_kb: 42
total_subagent_dispatches: 1
subagent_dispatches:
  orchestrator: 1
files_read:
- path: prompts/routines/market_open.md
  bytes: 8721
- path: config/approved_modes.yaml
  bytes: 1145
- path: trades/paper/positions.json
  bytes: 1253
- path: trades/paper/circuit_breaker.json
  bytes: 140
- path: memory/daily_snapshots/2026-05-19.md
  bytes: 897
artifacts_written:
- journals/daily/2026-05-20.md
- trades/paper/circuit_breaker.json
- trades/paper/positions.json
- logs/routine_runs/2026-05-20_133620_start.md
- logs/routine_runs/2026-05-20_133926_end.md
commits: []
notes: "UNH PENDING_BROKER (from 2026-05-19 EOD) confirmed filled at open: 39sh @
  $391.9044. Reconciler added UNH to positions.json (alpaca-authoritative). CB refreshed:
  equity $102,306.89, peak $104,090.72, DD 1.71%, state FULL (no transition). 0 PAPER_CLOSE
  — no invalidation triggers fired across all 6 positions (stop_loss/take_profit all
  null; no overnight gaps >5%). WMT earnings-caution window opens today; pre_close/EOD
  will evaluate exit. Reconcile clean. No Telegram sent (no action aside from reconcile
  fill)."
