# WMT — Per-Symbol Decision Log

**Cumulative stats (updated 2026-05-12 EOD):**

- Open paper positions: 1 (qty 46 @ $130.1160, opened 2026-05-12T20:02:25Z)
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL (latest mark): -$1.20 (close $130.09 vs entry $130.116)
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5

## 2026-05-12 — PAPER_BUY (large_cap_momentum_top5)

- Decision file: `decisions/2026-05-12/2000_WMT.json`
- Signal: ENTRY, rank 4/21 by 6m return (+24.30%); SPY trend filter passed.
- Filled: 46 shares @ $130.116
- Stop: $117.081, Target: $162.6125, R/R: 2.5:1
- Sizing: 6% of $100k (Strategy B)
- Routine: end_of_day_2026-05-12, mode PAPER_TRADING, cb_state=FULL, throttle=1.0
- Risk Manager: APPROVED. Compliance: APPROVED.

## 2026-05-12 — EOD re-run (20:40Z, no trade)

- Routine: end_of_day_2026-05-12 (scheduled 16:30 ET re-run)
- Signal: ENTRY re-confirmed (rank 4/21, +24.30% 6m, SPY trend up).
- Position held; no fill, no close.
- Mark (2026-05-07 bar close): $130.24. Unrealized PnL: +$5.70 (+0.10%).
- cb_state=FULL, throttle=1.0.

## 2026-05-13 — EOD held (re-confirm ENTRY, no trade)

- Routine: end_of_day_2026-05-13, mode PAPER_TRADING, cb_state=OUT, throttle=0.0.
- Signal: ENTRY re-confirmed (rank 4/21 +21.29% 6m, SPY trend up).
- Quote at close $125.30 (Alpaca IEX live, 20:00:02Z; pre_close 19:36Z saw $131.34 — sharp late-day reversal).
- Mark vs entry $130.116 → -$221.54 (-3.70%). Stop $117.081 (6.6% headroom).
- Decision: continue holding; no new decision file written.
- Forward risk: April retail sales releases 2026-05-14 BMO; WMT is itself a component of the data series. Pre-market 2026-05-14 must flag the print and any WMT reaction. WMT's own earnings 2026-05-21 BMO (one week out).

## 2026-05-14 — EOD held (re-confirm ENTRY, no trade)

- Routine: end_of_day_2026-05-14, mode PAPER_TRADING, cb_state=OUT, throttle=0.0.
- Signal: ENTRY re-confirmed (rank 4/21 +19.43% 6m, SPY trend up).
- Quote at pre_close (19:41Z in-market): $132.01. Post-close IEX last $137.97 (degraded; bid $124.62 / ask $137.97 — wide spread, discarded as a real mark).
- Mark vs entry $130.116 → **+$87.12 (+1.46%)**. Stop $117.081 (11.3% headroom — recovered vs yesterday's 6.6%).
- Decision: continue holding; no new decision file written.
- **Earnings catalyst flag carried**: WMT Q1 FY27 BMO 2026-05-21 (5 trading days out — outside next-trading-day window today but inside the CSCO-style 1-trading-day window at pre_close-2026-05-20). Restructuring announcement 2026-05-12 (~1,000 corporate roles) was non-thesis-invalidating per news scan.

**Cumulative stats (updated 2026-05-14 EOD):**

- Open paper positions: 1 (qty 46 @ $130.1160)
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL (mark $132.01): +$87.12 (+1.46%)
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5


## 2026-05-18 — EOD ENTRY submitted (PAPER_BUY, large_cap_momentum_top5 rank 4)

- Decision file: `decisions/2026-05-18/2041_WMT.json` (PAPER_BUY, final_status=PAPER_PROPOSED)
- Routine: end_of_day_2026-05-18, mode PAPER_TRADING, cb_state=FULL, throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY — rank 4/21, 6m +27.84%, SPY trend up. Consumer Staples defensive diversifier.
- Order: BUY 116 @ submitted quote $131.45; stop $118.305 (−10%), TP $164.3125 (+25%), R/R 2.5:1. ~14.88% of account; per-trade risk 1.488% < 1.5% cap.
- BROKER_PAPER=alpaca: submitted to Alpaca paper sandbox, status PENDING_BROKER (order_id 3464ba97…). Queues for next-open fill. Not filled today.
- **EARNINGS FLAG: WMT 2026-05-21 BMO** — 3 calendar days out today, OUTSIDE the 1-day caution window → entry permitted; enters the window ~2026-05-20. The 2026-05-20 pre_close/EOD routines MUST re-evaluate hold-through-earnings exposure (a future EOD may propose a pre-print exit).
- Prior pre-reset WMT position (qty 46 @ $130.1160) archived by the 2026-05-15 fresh-start reset; this is a fresh post-reset entry.
- Risk Manager: APPROVED (earnings forward-flagged). Compliance: APPROVED (not a single_stock_earnings_play — deterministic momentum, timing incidental).

**Cumulative stats (updated 2026-05-18 EOD):**

- Open paper positions: 0 filled (1 BUY order PENDING_BROKER for next open)
- Closed paper trades: 0 (post-reset; pre-reset history immutable above)
- Realized PnL: $0.00 (post-reset)
- Unrealized PnL: $0.00 (no filled position)
- Win rate: n/a (no closed trades post-reset)

## 2026-05-19 — EOD fill confirmed + ENTRY maintain (NO_TRADE, large_cap_momentum_top5 rank 4)

- Decision file: `decisions/2026-05-19/2038_WMT.json` (NO_TRADE, reason=already_held_maintain)
- Routine: end_of_day_2026-05-19, mode PAPER_TRADING, cb_state=FULL (recovered HALF→FULL this run), throttle=1.0.
- Fill: 2026-05-18 PENDING_BROKER order filled at 2026-05-19 open via Alpaca mirror — **116 sh @ $132.5397** (reconcile alpaca-authoritative, mirror in sync).
- Signal: large_cap_momentum_top5 ENTRY re-confirmed — rank 4/21, 6m +30.82%, SPY trend up. ENTRY = maintain (already held); no new shares.
- Mark: quote $130.81 vs entry $132.5397 → uPnL **-$200.65 (-1.31%)** (small drawdown; stop $119.286 ≈ -10% from entry).
- EARNINGS FLAG: WMT 2026-05-21 BMO. holding_earnings_caution_window_days=1 → today (2026-05-19) OUTSIDE the 1-day window; window opens 2026-05-20. The 2026-05-20 pre_close/EOD routines MUST re-evaluate hold-through-earnings risk and may propose a pre-print exit.
- Risk Manager: APPROVED (maintain, no new risk; earnings flagged forward). Compliance: APPROVED.

**Cumulative stats (updated 2026-05-19 EOD):**

- Open paper positions: 1 (qty 116 @ $132.5397, filled 2026-05-19 open)
- Closed paper trades: 0 (post 2026-05-15 reset)
- Realized PnL: $0.00 (post-reset)
- Unrealized PnL (mark $130.81): -$200.65 (-1.31%)
- Win rate: n/a (no closed trades post-reset)
- Active strategies: large_cap_momentum_top5

---

### 2026-05-20 pre_close — PAPER_CLOSE (overnight_risk: WMT Q1 FY27 BMO 2026-05-21)

- Routine: pre_close_2026-05-20, mode PAPER_TRADING, cb_state=FULL, dd=2.77%, throttle=1.0.
- Decision: PAPER_CLOSE 116 shares — final_status=PAPER_FILLED (Alpaca paper mirror order_id 5895f9df-727c-4b06-9848-d8b634cc9c39, broker FILLED).
- Reason: WMT Q1 FY27 earnings release scheduled 2026-05-21 BMO — within `holding_earnings_caution_window_days=1`. Single-stock idiosyncratic catalyst; trade was sized as a momentum carry, not an earnings play.
- Quote: $131.23 (IEX, 2026-05-20T19:35:06Z; staleness 24s).
- Approx realized PnL: -$151.93 (mark 131.23 vs entry 132.5397; round-trip slippage ~$2 per fills config).
- Risk Manager: APPROVED (exit-side; no R/R or sizing cap applies; daily PnL well clear of -2% hard halt). Compliance: APPROVED (mode, watchlist, strategy, schema all green).
- Decision file: `decisions/2026-05-20/1935_WMT.json`.

**Cumulative stats (updated 2026-05-20 pre_close):**

- Open paper positions: 0 (closed pre-earnings)
- Closed paper trades: 1 (this close)
- Realized PnL: -$151.93 (this close)
- Active strategies: large_cap_momentum_top5 (eligible for re-entry post-print on EOD signal)
