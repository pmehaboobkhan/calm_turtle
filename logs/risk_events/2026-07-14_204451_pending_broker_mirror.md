# Risk Event — Pending-Broker Suppression Persists → CB refresh skipped a 3rd consecutive routine today (2026-07-14)

- **Timestamp:** 2026-07-14T20:44:51Z (16:44 ET)
- **Routine:** end_of_day
- **Severity:** MEDIUM-HIGH (no capital impact — ledger verified intact — but the circuit-breaker has been unable to advance on true equity for ~5 weeks; recommend human inspection)
- **Mode:** PAPER_TRADING · BROKER_PAPER=alpaca

## Summary
`paper_sim.pending_broker_count()` = **5** at EOD, so the circuit-breaker refresh (step 5) hit **Guard 1** and was SKIPPED again — the prior state (FULL, peak_equity $100,792.58) was carried forward with throttle 1.0, no transition, no CB risk event, no CB Telegram, exactly as Guard 1 prescribes. This is now the **third consecutive routine TODAY** to skip the CB write on this ground (midday: pending 4 → pre_close: pending 5 → EOD: pending 5), and the pattern has stood since ~2026-06-11 (~33 days).

## Why the count won't clear (known root cause, documented 2026-07-07)
`lib.paper_sim.confirm_broker_fills()` is a no-op against this broker's status format: `lib.broker.get_order()` returns `status = "OrderStatus.FILLED"`, but `confirm_broker_fills()` tests `status.lower() == "filled"`, which never matches `"orderstatus.filled"`, so every terminal order is misclassified `still_pending`. The stuck `PENDING_BROKER` log rows therefore never decay and `pending_broker_count()` stays elevated, permanently tripping Guard 1. See `logs/risk_events/2026-07-07_204950_pending_broker_mirror.md` for the full trace and the proposed one-line normalization fix (`str(o.get("status") or "").lower().split(".")[-1]`). `lib/` is not an orchestrator write path, so the fix requires a human PR.

## Ledger IS intact this run (distinct from the 2026-07-07 wipe hazard)
Unlike 2026-07-07 (when the broker `get_positions()` view flapped empty and a destructive reconcile was avoided), **today the broker view is consistent**:
- `paper_sim.reconcile()` → `{open_count: 3, discrepancies: [], source: alpaca-authoritative}`.
- Step 8a Alpaca-mirror reconcile → **in sync (3 positions match)**: GOOGL 16, SPY 20, UNH 15 on both local and Alpaca.
So reconciliation PASSED and the routine did not halt. The only casualty of the stuck rows is the CB equity write, which remains frozen at the 2026-07-10 snapshot.

## Impact of the frozen circuit-breaker
- CB state is stuck at FULL / peak $100,792.58 / last-observed $100,480.52 (2026-07-10). It cannot advance on true equity while Guard 1 trips every run.
- Operationally low-risk **right now**: informational sim equity is at/above prior peak (drawdown ~0%), far inside the 8% HALF trigger, and the book is only 3 long ETF/large-cap positions. EXITs are never throttled regardless of CB state, so downside protection via stops/health checks is unaffected.
- **But** the live-trading regime-diversity gate `require_cb_throttle_event` can never be satisfied while the breaker is frozen, and a genuine drawdown would not be detected by the CB until the pending rows clear. This is a latent safety-instrumentation gap.

## Recommended human action (RECOMMENDATION ONLY — no config/lib edited here)
1. Apply the `confirm_broker_fills()` status-normalization fix via human PR (draft referenced in the 2026-07-07 event), OR manually finalize the stale `PENDING_BROKER` rows, so `pending_broker_count()` decays to 0 and the CB can resume writing true equity.
2. Confirm the Alpaca paper sandbox has actually settled the post-2026-06-05/06-08 fills (it appears to have — mirror is in sync — but the local ledger's row-status strings are what's stuck, not the fills themselves).
3. Until then, EOD will keep skipping the CB write via Guard 1 and carrying FULL forward. That is the safe behavior, but it should not be allowed to stand indefinitely.

## Disposition
- CB write SKIPPED (Guard 1, pending=5); FULL carried forward; throttle 1.0. No transition, no CB Telegram.
- Reconcile + mirror both clean → routine proceeds to journal/audit/commit (not a hard halt).
- This event is folded into the single EOD Telegram summary as the run's top concern.
