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

## 2026-05-20 — EOD maintain (NO_TRADE; large_cap_momentum_top5 rank 5)

- Routine: end_of_day_2026-05-20, mode PAPER_TRADING, cb_state=FULL (DD 2.62%), throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY re-confirmed — rank 5/21, 6m +22.69%, SPY trend up. ENTRY = maintain (already held); no new shares. Boundary rank persisted today (rank-5 at pre_market and EOD).
- Mark: EOD close $401.42 vs entry $391.9044 → uPnL **+$371.11 (+2.43%)**. Recovery from -$315.68 at pre_close; bid/ask spread (bid 368.12 / ask 401.42) remains wide — last-trade print drives the mark.
- Risk Manager: APPROVED (maintain). Compliance: APPROVED.

**Cumulative stats (updated 2026-05-20 EOD):**

- Open paper positions: 1 (qty 39 @ $391.9044)
- Closed paper trades (all-time): 0
- Realized PnL (all-time): $0.00
- Unrealized PnL (mark $401.42): +$371.11 (+2.43%)
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5

## 2026-05-26 — PAPER_CLOSE PROPOSED (midday daily-loss-limit breach)

- Decision file: `decisions/2026-05-26/1614_UNH.json` (final_status `PAPER_PROPOSED` — NOT executed)
- Trigger: portfolio daily-loss limit breached -$569.77 / -0.563% (vs -$500 / -0.5% caps); `halt_after_daily_limit_breach=true`. Risk event: `logs/risk_events/20260526_161452_daily_loss.md`.
- Context: midday 395.66; day +$146.47; +19.93% above -10% rotation stop ($316.82). News bullish (Q1 beat, PT raises).
- Gates: Risk Manager APPROVED + Compliance APPROVED (PAPER_CLOSE reduces exposure; permitted in PAPER_TRADING).
- Status: position remains OPEN; midday is monitoring-only (no fills). Close/hold escalated to human via URGENT notify; pre_close re-evaluates on close.

## 2026-05-28 — NO_TRADE (maintain — stale bars + already-held) (large_cap_momentum_top5)

- Routine: end_of_day_2026-05-28, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (carried; CB write skipped on pending_broker guard), throttle=1.0.
- ENTRY re-fired (rank 5, 6m +21.76%); 39 sh held. Blocked by stale bars + already-held. Live mark $404.04, uPnL +$473.29 (+14.8% above stop; recovered off prior thin cushion).
- Decision file: `decisions/2026-05-28/1630_UNH.json`

## 2026-05-29 — PAPER_CLOSE (pre_close de-risk)
- Routine: pre_close_2026-05-29, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (DD 3.36%, no transition).
- CLOSE all positions per daily-loss-limit breach (logs/risk_events/20260529_160920_daily_loss.md; halt_after_daily_limit_breach=true). RM+Compliance APPROVED at midday (1609), executed at pre_close on late-day fill.
- Fill ~$380.89 vs entry $391.9044; realized ~$-429.56 (pre-fee, vs entry basis). Broker flat (0 open), reconcile clean.
- Decision file: decisions/2026-05-29/1609_UNH.json (final_status=PAPER_CLOSE).
