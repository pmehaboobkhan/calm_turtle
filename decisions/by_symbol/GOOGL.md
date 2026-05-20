# GOOGL — Per-Symbol Decision Log

**Cumulative stats (updated 2026-05-12 EOD):**

- Open paper positions: 1 (qty 15 @ $397.9096, opened 2026-05-12T20:02:25Z)
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL (latest mark): -$1.19 (close $397.83 vs entry $397.9096)
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5

## 2026-05-12 — PAPER_BUY (large_cap_momentum_top5)

- Decision file: `decisions/2026-05-12/2000_GOOGL.json`
- Signal: ENTRY, rank 1/21 by 6m return (+35.31%); SPY trend filter passed.
- Filled: 15 shares @ $397.9096
- Stop: $358.047, Target: $497.2875, R/R: 2.5:1
- Sizing: 6% of $100k (Strategy B 30% allocation / 5 names)
- Routine: end_of_day_2026-05-12, mode PAPER_TRADING, cb_state=FULL, throttle=1.0
- Risk Manager: APPROVED. Compliance: APPROVED.

## 2026-05-12 — EOD re-run (20:40Z, no trade)

- Routine: end_of_day_2026-05-12 (scheduled 16:30 ET re-run)
- Signal: ENTRY re-confirmed (rank 1/21, +35.31% 6m, SPY trend up).
- Position held; no fill, no close.
- Mark (2026-05-07 bar close): $397.89. Unrealized PnL: -$0.29 (-0.01%).
- cb_state=FULL, throttle=1.0.

## 2026-05-13 — EOD held (re-confirm ENTRY, no trade)

- Routine: end_of_day_2026-05-13, mode PAPER_TRADING, cb_state=OUT, throttle=0.0.
- Signal: ENTRY re-confirmed (rank 1/21 +36.81% 6m, SPY trend up).
- Quote at close $382.23 (Alpaca IEX live, 20:00:02Z; pre_close 19:36Z saw $402.96 — late-day give-back).
- Mark vs entry $397.9096 → -$235.19 (-3.94%). Stop $358.047 (6.3% headroom).
- Decision: continue holding; no new decision file written. Position is now this session's largest single-name unrealized loss.
- Watch tomorrow: monitor for further give-back. Stop is 6% below close so still ample headroom but tighter than yesterday.

## 2026-05-14 — EOD held (re-confirm ENTRY, no trade)

- Routine: end_of_day_2026-05-14, mode PAPER_TRADING, cb_state=OUT, throttle=0.0.
- Signal: ENTRY re-confirmed (rank 1/21 +38.42% 6m, SPY trend up).
- Quote at pre_close (19:41Z in-market): $401.68. Post-close IEX last $377.65 (degraded; bid $377.65 / ask $0.0 — discarded as a real mark).
- Mark vs entry $397.9096 → **+$56.56 (+0.95%)**. Stop $358.047 (10.9% headroom — recovered vs yesterday's 6.3%).
- Decision: continue holding; no new decision file written.
- News flow this week: Anthropic ~$200B/5yr commitment to Google Cloud (2026-05-11); Googlebook product launch with Acer/ASUS/Dell/HP/Lenovo. Tone neutral-to-bullish. Next earnings 2026-07-22 (outside near-term window).

**Cumulative stats (updated 2026-05-14 EOD):**

- Open paper positions: 1 (qty 15 @ $397.9096)
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL (mark $401.68): +$56.56 (+0.95%)
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5


## 2026-05-18 — EOD ENTRY submitted (PAPER_BUY, large_cap_momentum_top5 rank 2)

- Decision file: `decisions/2026-05-18/2041_GOOGL.json` (PAPER_BUY, final_status=PAPER_PROPOSED)
- Routine: end_of_day_2026-05-18, mode PAPER_TRADING, cb_state=FULL, throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY — rank 2/21, 6m +38.58%, SPY trend up. ~20.6pp clear of cut-off.
- Order: BUY 38 @ submitted quote $396.78; stop $357.102 (−10%), TP $495.975 (+25%), R/R 2.5:1. ~14.71% of account; per-trade risk 1.471% < 1.5% cap.
- BROKER_PAPER=alpaca: submitted to Alpaca paper sandbox, status PENDING_BROKER (order_id daaea20f…). Queues for next-open fill. Not filled today.
- Prior pre-reset GOOGL position (qty 15 @ $397.9096) was archived by the 2026-05-15 fresh-start reset; this is a fresh post-reset entry.
- Risk Manager: APPROVED. Compliance: APPROVED.

**Cumulative stats (updated 2026-05-18 EOD):**

- Open paper positions: 0 filled (1 BUY order PENDING_BROKER for next open)
- Closed paper trades: 0 (post-reset; pre-reset history immutable above)
- Realized PnL: $0.00 (post-reset)
- Unrealized PnL: $0.00 (no filled position)
- Win rate: n/a (no closed trades post-reset)

## 2026-05-19 — EOD fill confirmed + ENTRY maintain (NO_TRADE, large_cap_momentum_top5 rank 2)

- Decision file: `decisions/2026-05-19/2038_GOOGL.json` (NO_TRADE, reason=already_held_maintain)
- Routine: end_of_day_2026-05-19, mode PAPER_TRADING, cb_state=FULL (recovered HALF→FULL this run), throttle=1.0.
- Fill: 2026-05-18 PENDING_BROKER order filled at 2026-05-19 open via Alpaca mirror — **38 sh @ $395.64** (reconcile alpaca-authoritative, mirror in sync).
- Signal: large_cap_momentum_top5 ENTRY re-confirmed — rank 2/21, 6m +42.69%, SPY trend up. ENTRY = maintain (already held); no new shares.
- Mark: quote $409.08 vs entry $395.64 → uPnL **+$510.72 (+3.40%)**.
- Risk Manager: APPROVED (maintain, no new risk). Compliance: APPROVED.

**Cumulative stats (updated 2026-05-19 EOD):**

- Open paper positions: 1 (qty 38 @ $395.64, filled 2026-05-19 open)
- Closed paper trades: 0 (post 2026-05-15 reset)
- Realized PnL: $0.00 (post-reset)
- Unrealized PnL (mark $409.08): +$510.72 (+3.40%)
- Win rate: n/a (no closed trades post-reset)
- Active strategies: large_cap_momentum_top5

## 2026-05-20 — EOD maintain (NO_TRADE; large_cap_momentum_top5 rank 2)

- Routine: end_of_day_2026-05-20, mode PAPER_TRADING, cb_state=FULL (DD 2.62%), throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY re-confirmed — rank 2/21, 6m +40.44%, SPY trend up. ENTRY = maintain (already held); no new shares.
- Mark: EOD close $368.38 vs entry $395.64 → uPnL **-$1,035.88 (-6.89%)**. Largest single-name drawdown of the day; late-day move (pre_close mark was $388.01; closing print -$5.13 below pre_close). Still above per-strategy default stop_loss_pct=-10% ($356.08).
- Risk Manager: APPROVED (maintain — no stop breach, no invalidation; momentum carry thesis intact). Compliance: APPROVED.

**Cumulative stats (updated 2026-05-20 EOD):**

- Open paper positions: 1 (qty 38 @ $395.64)
- Closed paper trades (all-time): 1
- Realized PnL (all-time): +$129.05
- Unrealized PnL (mark $368.38): -$1,035.88 (-6.89%)
- Win rate: 100% (1/1)
- Active strategies: large_cap_momentum_top5
