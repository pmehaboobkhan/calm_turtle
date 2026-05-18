# CSCO — Per-Symbol Decision Log

**Cumulative stats (updated 2026-05-12 EOD):**

- Open paper positions: 1 (qty 65 @ $91.6483, opened 2026-05-12T20:02:25Z)
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL (latest mark): -$1.19 (close $91.63 vs entry $91.6483)
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5

## 2026-05-12 — PAPER_BUY (large_cap_momentum_top5)

- Decision file: `decisions/2026-05-12/2000_CSCO.json`
- Signal: ENTRY, rank 3/21 by 6m return (+25.29%); SPY trend filter passed.
- Filled: 65 shares @ $91.6483
- Stop: $82.467, Target: $114.5375, R/R: 2.5:1
- Sizing: 6% of $100k (Strategy B)
- Routine: end_of_day_2026-05-12, mode PAPER_TRADING, cb_state=FULL, throttle=1.0
- Risk Manager: APPROVED. Compliance: APPROVED.

## 2026-05-12 — EOD re-run (20:40Z, no trade)

- Routine: end_of_day_2026-05-12 (scheduled 16:30 ET re-run)
- Signal: ENTRY re-confirmed (rank 3/21, +25.29% 6m, SPY trend up).
- Position held; no fill, no close.
- Mark (2026-05-07 bar close): $92.14. Unrealized PnL: +$31.96 (+0.54%).
- cb_state=FULL, throttle=1.0.

## 2026-05-13 — PAPER_CLOSE (pre_close, overnight_risk)

- Decision file: `decisions/2026-05-13/1536_CSCO.json`
- Routine: pre_close_2026-05-13, mode PAPER_TRADING, cb_state=OUT (peak inflated artifact; exposure_fraction(OUT) throttles new opens, not closes).
- Reason: `overnight_risk` — Cisco Q3 FY26 earnings scheduled 2026-05-13 AMC (after market close, 4:30 PM ET conference call). Sources: Cisco IR press release, Stocktitan, MarketBeat. Options-implied one-day move ~9.87% (TipRanks). Single-stock idiosyncratic catalyst with no diversifying counterweight; pre-close routine is specifically designed to refuse this kind of asymmetric overnight exposure.
- Quote: $101.19 (Alpaca IEX live, 0.7s staleness).
- Fill: 65 shares CLOSE @ $101.1698 (slippage applied via lib.fills).
- Realized PnL: **+$618.90** (+10.13% on $5,957.14 cost basis).
- Risk Manager: APPROVED (exit-side, no sizing-cap concerns; daily-loss & daily-trades headroom intact). Compliance: APPROVED (PAPER_TRADING permits PAPER_CLOSE; CSCO in watchlist; schema valid; sources cited).
- Position closed. Active strategies: none on CSCO post-close.
- Re-entry rule per the EOD routine: if CSCO remains in the top-5 momentum slate after the earnings print and the SPY trend filter still passes, EOD lib.signals will re-issue ENTRY and the routine can re-open on the EOD price. This close does not lock out re-entry.

## 2026-05-13 — EOD signal still ENTRY, routed NO_TRADE (cb_OUT + earnings)

- Decision file: `decisions/2026-05-13/2050_CSCO.json`
- Routine: end_of_day_2026-05-13, mode PAPER_TRADING, cb_state=OUT, throttle=0.0.
- Signal: ENTRY re-confirmed (rank 3/21, +25.97% 6m, SPY trend up). Same as pre-market and pre-close evaluations.
- Decision: **NO_TRADE** with reason `circuit_breaker_OUT AND earnings_window_open AND data_staleness_breach`. Quote at close $96.36 (down -4.78% vs pre-close $101.19 — late-day weakness ahead of the AMC print).
- Three stacking gates prevented the re-entry: (1) CB OUT throttle=0.0 → mechanically blocks new opens; (2) `holding_earnings_caution_window_days=1` against tonight's AMC print; (3) daily-bar staleness 19d >> 60s. Each is individually disqualifying.
- Cumulative stats refresh: 1 closed paper trade, +$618.90 realized, 100% win rate (1/1). Open position count: 0. The next chance to re-enter is the 2026-05-14 EOD signal after the earnings print clears.

**Cumulative stats (updated 2026-05-13 EOD):**

- Open paper positions: 0
- Closed paper trades: 1
- Realized PnL: +$618.90
- Win rate: 100% (1/1)
- Active strategies: none on CSCO (signal ENTRY today but blocked at EOD)

## 2026-05-14 — EOD signal still ENTRY, routed NO_TRADE (cb_OUT + staleness + post-earnings stale-bar)

- Decision file: `decisions/2026-05-14/2038_CSCO.json`
- Routine: end_of_day_2026-05-14, mode PAPER_TRADING, cb_state=OUT, throttle=0.0.
- Signal: ENTRY re-confirmed (rank 3/21, +25.61% 6m, SPY trend up).
- Decision: **NO_TRADE** with reason `circuit_breaker_OUT AND data_staleness_breach AND post_earnings_no_fresh_evidence`.
- Three stacking gates: (1) CB OUT throttle=0.0 → mechanically blocks new opens; (2) daily-bar staleness 6 calendar days >> 60s (latest bar 2026-05-08 predates yesterday's AMC earnings print); (3) re-entering within 24h of a pre-print exit without fresh post-earnings price evidence inverts the overnight-risk thesis used to capture +$618.90 — needs new evidence.
- IEX post-close last $121.25 (bid $109.35 / ask $121.25 — wide spread; verify quote tightness next-session market hours before any re-entry).
- Intended sizing pre-throttle: ~49 shares (~$5,941 ≈ 5.94% of $100k, Strategy B target 6%). Actual: 0 shares.
- Risk Manager: APPROVED on NO_TRADE (reduces no risk). Compliance: APPROVED.
- Cumulative stats unchanged: 1 closed paper trade, +$618.90 realized, 100% win rate (1/1). Open position count: 0. Re-entry remains conditional on (a) CB FULL/HALF AND (b) fresh post-earnings daily bar AND (c) rank ≤ 5 confirms on that fresh bar.

**Cumulative stats (updated 2026-05-14 EOD):**

- Open paper positions: 0
- Closed paper trades: 1
- Realized PnL: +$618.90
- Win rate: 100% (1/1)
- Active strategies: none on CSCO (signal ENTRY both days but blocked at EOD)


## 2026-05-18 — EOD ENTRY submitted (PAPER_BUY, large_cap_momentum_top5 rank 1)

- Decision file: `decisions/2026-05-18/2041_CSCO.json` (PAPER_BUY, final_status=PAPER_PROPOSED)
- Routine: end_of_day_2026-05-18, mode PAPER_TRADING, cb_state=FULL, throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY — rank 1/21, 6m +61.56%, SPY trend up. Stale→fresh distortion does NOT recur at EOD (both runs fresh) — cleanest read; entry taken per the deterministic signal despite extreme-momentum / post-earnings caution (CSCO earnings 2026-05-13 AMC, now 5 sessions old, fully in fresh bars; > earnings-caution window).
- Order: BUY 130 @ submitted quote $118.21; stop $106.389 (−10%), TP $147.7625 (+25%), R/R 2.5:1. ~14.99% of account; per-trade risk 1.499% < 1.5% cap.
- BROKER_PAPER=alpaca: submitted to Alpaca paper sandbox, status PENDING_BROKER (order_id 378797e1…). Queues for next-open fill. Not filled today.
- Note: prior +$618.90 close (2026-05-13 pre-earnings overnight-risk exit) is the all-time realized win; this is a fresh deterministic momentum re-entry, not a re-chase — prior exit thesis (overnight earnings risk) no longer applies.
- Risk Manager: APPROVED (elevated-monitoring flag carried). Compliance: APPROVED.

**Cumulative stats (updated 2026-05-18 EOD):**

- Open paper positions: 0 filled (1 BUY order PENDING_BROKER for next open)
- Closed paper trades (all-time): 1
- Realized PnL (all-time): +$618.90
- Win rate: 100% (1/1)
