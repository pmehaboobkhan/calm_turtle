# UNH — Per-Symbol Decision Log

**Cumulative stats (updated 2026-05-19 EOD):**

- Open paper positions: 0 filled (1 BUY order PENDING_BROKER for next open)
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL: $0.00 (not yet filled)
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5

## 2026-05-19 — EOD ENTRY submitted (PAPER_BUY, large_cap_momentum_top5 rank 5)

- Decision file: `decisions/2026-05-19/2038_UNH.json` (PAPER_BUY, final_status=PAPER_PROPOSED)
- Routine: end_of_day_2026-05-19, mode PAPER_TRADING, cb_state=FULL (recovered HALF→FULL this run; see `logs/risk_events/2026-05-19_203823_circuit_breaker.md`), throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY — rank 5/21, 6m +19.34%, SPY trend up. Both confirmations passed. First UNH position (not previously held) — a genuine new open, position #6 of 8 max.
- Order: BUY 39 @ ref $391.13 (2026-05-18 daily close basis; no live UNH quote, daily-bar strategy); stop $352.017 (−10%), TP $488.9125 (+25%), R/R 2.5:1. ~14.65% of account; per-trade risk 1.465% < 1.5% cap. Liquidity 20d ADV ~8.52M > 5M min.
- BROKER_PAPER=alpaca: order submitted to Alpaca paper sandbox, status PENDING_BROKER (order_id d1e522f0…). Market closed at 16:38 ET → queues for next-open fill. Not filled today; positions.json mirror-owned; reconcile alpaca-authoritative (no divergence — "not a position yet").
- Confidence 0.52 (low): rank-5 boundary name (lowest persistence; flagged pre-market), weakest 6m momentum of today's top-5, news feed offline.
- Risk Manager: APPROVED. Compliance: APPROVED.
- Watch: UNH ↔ NVDA (rank 6) ↔ JNJ (rank 7) boundary jitter — a small momentum shift can knock UNH out of top-5 → EXIT at a subsequent EOD. Verify fill + slippage at 2026-05-20 open.
