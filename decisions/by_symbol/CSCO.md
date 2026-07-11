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

## 2026-05-19 — EOD fill confirmed + ENTRY maintain (NO_TRADE, large_cap_momentum_top5 rank 1)

- Decision file: `decisions/2026-05-19/2038_CSCO.json` (NO_TRADE, reason=already_held_maintain)
- Routine: end_of_day_2026-05-19, mode PAPER_TRADING, cb_state=FULL (recovered HALF→FULL this run; see risk event), throttle=1.0.
- Fill: 2026-05-18 PENDING_BROKER order filled at 2026-05-19 open via Alpaca mirror — **130 sh @ $117.6635** (positions.json/reconcile alpaca-authoritative, mirror in sync).
- Signal: large_cap_momentum_top5 ENTRY re-confirmed — rank 1/21, 6m +55.29%, SPY trend up. ENTRY = maintain (already held); no new shares (already-held check). Elevated-monitoring flag carried (post Q3 FY26 earnings, cleared 2026-05-13).
- Mark: quote $120.88 vs entry $117.6635 → uPnL **+$418.14 (+2.73%)**.
- Risk Manager: APPROVED (maintain, no new risk). Compliance: APPROVED.

**Cumulative stats (updated 2026-05-19 EOD):**

- Open paper positions: 1 (qty 130 @ $117.6635, filled 2026-05-19 open)
- Closed paper trades (all-time): 1
- Realized PnL (all-time): +$618.90
- Unrealized PnL (mark $120.88): +$418.14 (+2.73%)
- Win rate: 100% (1/1)
- Active strategies: large_cap_momentum_top5

## 2026-05-20 — EOD maintain (NO_TRADE; large_cap_momentum_top5 rank 1)

- Routine: end_of_day_2026-05-20, mode PAPER_TRADING, cb_state=FULL (DD 2.62%), throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY re-confirmed — rank 1/21, 6m +49.52%, SPY trend up. ENTRY = maintain (already held); no new shares.
- Mark: EOD close $121.75 vs entry $117.6635 → uPnL **+$531.25 (+3.47%)**.
- Risk Manager: APPROVED (maintain, no new risk). Compliance: APPROVED.

**Cumulative stats (updated 2026-05-20 EOD):**

- Open paper positions: 1 (qty 130 @ $117.6635)
- Closed paper trades (all-time): 1
- Realized PnL (all-time): +$618.90
- Unrealized PnL (mark $121.75): +$531.25 (+3.47%)
- Win rate: 100% (1/1)
- Active strategies: large_cap_momentum_top5

## 2026-05-26 — PAPER_CLOSE PROPOSED (midday daily-loss-limit breach)

- Decision file: `decisions/2026-05-26/1614_CSCO.json` (final_status `PAPER_PROPOSED` — NOT executed)
- Trigger: portfolio daily-loss limit breached -$569.77 / -0.563% (vs -$500 / -0.5% caps); `halt_after_daily_limit_breach=true`. Risk event: `logs/risk_events/20260526_161452_daily_loss.md`.
- Context: midday 117.71; day +$6.04; +18.66% above -10% rotation stop ($95.75). No name-specific breaking news.
- Gates: Risk Manager APPROVED + Compliance APPROVED (PAPER_CLOSE reduces exposure; permitted in PAPER_TRADING).
- Status: position remains OPEN; midday is monitoring-only (no fills). Close/hold escalated to human via URGENT notify; pre_close re-evaluates on close.

## 2026-05-28 — NO_TRADE (maintain — stale bars + already-held) (large_cap_momentum_top5)

- Routine: end_of_day_2026-05-28, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (carried; CB write skipped on pending_broker guard), throttle=1.0.
- ENTRY re-fired (rank 1, 6m +58.95%); 130 sh held. Blocked by stale bars + already-held. Live mark $124.17, uPnL +$845.85 (+17.3% above stop).
- Decision file: `decisions/2026-05-28/1630_CSCO.json`

## 2026-05-29 — PAPER_CLOSE (pre_close de-risk)
- Routine: pre_close_2026-05-29, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (DD 3.36%, no transition).
- CLOSE all positions per daily-loss-limit breach (logs/risk_events/20260529_160920_daily_loss.md; halt_after_daily_limit_breach=true). RM+Compliance APPROVED at midday (1609), executed at pre_close on late-day fill.
- Fill ~$121.17 vs entry $117.6635; realized ~$+455.85 (pre-fee, vs entry basis). Broker flat (0 open), reconcile clean.
- Decision file: decisions/2026-05-29/1609_CSCO.json (final_status=PAPER_CLOSE).

## 2026-05-29 — EOD ENTRY re-fired, routed NO_TRADE (daily-loss halt active)
- Routine: end_of_day_2026-05-29, mode PAPER_TRADING, cb_state=FULL (CB write skipped, pending_broker=7), throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY re-confirmed — rank 1/21, 6m +57.29%, SPY trend up. Strongest momentum name.
- Decision: **NO_TRADE / REJECTED** (`decisions/2026-05-29/2042_CSCO.json`), reason `daily_loss_halt_active` — EOD ran after pre_close de-risked the book; no re-entry the same session as a daily-loss halt. Re-entry resets next session (2026-06-01).

**Cumulative stats (updated 2026-05-29 EOD):**

- Open paper positions: 0 (closed at pre_close de-risk)
- Closed paper trades (all-time): 2
- Realized PnL (all-time): +$1,074.75 (+$618.90 on 2026-05-13, +$455.85 on 2026-05-29)
- Win rate: 100% (2/2)
- Active strategies: large_cap_momentum_top5 (signal ENTRY today, blocked by daily-loss halt)

## 2026-06-01 — NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-01/1639_CSCO.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 1, +59.49% 6m).
- Outcome: NO_TRADE. RM REJECTED (freshness check #11), Compliance REJECTED (RM != APPROVED).
- Reason: latest daily bar = 2026-05-29 (~92.7h stale); no 2026-06-01 close in feed. CLAUDE.md rule #5 → NO_TRADE.
- Book flat; no position opened. CB write skipped (pending_broker=7); FULL carried, throttle 1.0.

## 2026-06-02 — NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-02/2040_CSCO.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 1, +61.22% 6m).
- Outcome: NO_TRADE. RM REJECTED (freshness hard-check #11), Compliance REJECTED (RM != APPROVED).
- Reason: latest daily bar = 2026-06-01 (~44.68h stale, ~2,680x over 60s cap); no 2026-06-02 close in daily feed at EOD (live IEX quote exists; daily-bar provider lags). CLAUDE.md rule #5 -> NO_TRADE.
- Book flat; no position opened. CB write skipped (pending_broker=7); FULL carried, throttle 1.0.

## 2026-06-03 — Pre-market RESEARCH-ONLY NO_TRADE (routine scope)

- Decision file: `decisions/2026-06-03/0642_CSCO.json`
- Signal basis: `data/market/2026-06-03/0630.json`, last bar 2026-06-02.
- Signal: large_cap_momentum_top5 ENTRY (rank 1/21, 6m return +68.16%, SPY trend up). Rank-1 cushion *widened* — 6m return expanded from +61.22% (06-01 basis) to +68.16% (06-02 basis) in 5 sessions. Fourth consecutive paper-week as Strategy-B leader.
- Outcome: **NO_TRADE / REJECTED on routine scope** (not on freshness or risk; pre_market is RESEARCH_ONLY in v1). RM REJECTED + Compliance REJECTED specifically because the pre_market routine does not produce trade-execution decisions.
- Book flat; no position opened. EOD 2026-06-03 will re-evaluate against the 06-03 close.
- Watch: late-cycle momentum risk now elevated — first paper-trading observation of CSCO >+65% 6m, post-peak decay path unobserved.

## 2026-06-04 — EOD NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-04/2040_CSCO.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 1/21, 6m +68.16%, SPY trend up). Still basket leader.
- Outcome: NO_TRADE. RM REJECTED (rule #5 stale-data), Compliance REJECTED.
- Reason: latest daily bar = 2026-06-03 (~44.7h stale, >60s cap); no 06-04 close in daily feed at the 20:40Z EOD decision point (intraday IEX quote IS fresh; daily-bar provider lags). 4th consecutive stale EOD. CLAUDE.md rule #5 -> NO_TRADE.
- Book flat; no position opened. CB wrote this run (pending_broker cleared via overnight sync_alpaca_state reset): FULL, DD 0.00%, throttle 1.0, no transition.

## 2026-06-05 — EOD ENTRY submitted (PAPER_BUY, large_cap_momentum_top5)

- Decision file: `decisions/2026-06-05/1642_CSCO.json` (PAPER_BUY, final_status=PAPER_PROPOSED)
- Routine: end_of_day_2026-06-05, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (no transition, DD 0.00%), throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY — rank 1 by 126d return (+70.94%), SPY trend filter passed (above 10m MA). Fresh 06-05 close.
- Order: BUY 46 @ ref $130.00; stop $117.00 (-10%), TP $162.50 (+25%), R/R 2.5:1. ~5.95% of account; per-trade risk 0.595% < 1.5% cap.
- Submitted to Alpaca paper sandbox, PENDING_BROKER (order_id 1c9d619e…). Market closed -> next-open fill. reconcile alpaca-authoritative, mirror in sync.
- Risk Manager: APPROVED. Compliance: APPROVED.
- Note: +70.94% 6m is a stretched move (mean-reversion / elastic-snap risk in bear thesis); rank-1 amplifies any reversal.

**Cumulative stats (updated 2026-06-05 EOD):**

- Open paper positions: 0 filled (1 BUY order PENDING_BROKER for next open)
- Active strategies: large_cap_momentum_top5

## 2026-06-30 — EOD NO_TRADE (HELD; stop status indeterminate — data staleness)

- Decision file: `decisions/2026-06-30/2039_CSCO.json` (NO_TRADE, final_status=NO_TRADE)
- Routine: end_of_day_2026-06-30, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (Guard-1 skip; carried forward; DD 0.56%), throttle=1.0.
- Position: BUY 46 @ entry $123.7893, stop $117.00, TP $162.50. Broker unrealized ≈ −$291.15.
- **Outcome: HELD overnight.** Stale EOD quote read $112.76 (would be below $117.00 stop) but is unreliable (ask 0.0, ~37 min stale); last fresh read (pre_close 19:37Z) was $117.58 — 0.50% ABOVE stop. Cannot confirm a true breach on stale data. Daily bars 13 trading days stale (latest 06-11). Engine still ranks CSCO #1 momentum. Resolve stop status on next fresh close.
- Risk Manager: APPROVED. Compliance: APPROVED. Risk event: `logs/risk_events/2026-06-30_203914_data_staleness.md`.

**Cumulative stats (updated 2026-06-30 EOD):**

- Open paper positions: 1 (BUY 46 @ $123.7893; held; stop status indeterminate on stale marks)
- Unrealized PnL (broker mark, stale): ≈ −$291.15
- Win rate: n/a (no new closed trades)
- Active strategies: large_cap_momentum_top5

## 2026-07-01 — market_open: PAPER_CLOSE (EXECUTED)

- Decision file: `decisions/2026-07-01/0939_CSCO.json`
- Routine: market_open_2026-07-01 (~09:39 ET, market OPEN), mode PAPER_TRADING, BROKER_PAPER=alpaca. CB refresh SKIPPED (Guard 1: pending broker order); FULL carried forward — EXITs are never CB-throttled.
- Trigger: `lib.portfolio_health` stop_loss breach — verbatim: "stop_loss breached: BUY entered at 123.7893, stop=117.0000, current=116.5500".
- Gate chain: trade_proposal → Risk Manager APPROVED → Compliance/Safety APPROVED.
- **PAPER_CLOSE executed:** full 46-share BUY position at ~$117.18 (Alpaca IEX last-trade). Entry $123.7893. Est. realized PnL **−$304 (−5.3%)**.
- **MARGINAL call:** on fresh tight-spread prints CSCO straddled the $117.00 stop within ±0.25% (116.85–117.26); the earlier sub-stop print ($116.38) was on a dislocated ~5.4% IEX spread. `portfolio_health` (the deterministic authority) flagged the breach and the majority of clean prints were below $117.00 — decision honored the pre-committed stop per capital-preservation discipline rather than hoping for reversion. Logged transparently; flagged for outcome review at EOD 07-01.
- Reconcile: `discrepancies: []`, alpaca-authoritative, local/Alpaca parity 5==5. CSCO removed from both books.

**Cumulative stats (updated 2026-07-01 market_open):**

- Open paper positions: 0 (closed 2026-07-01 on stop breach)
- Closed paper trades this line: 1 (est. realized −$304)
- Win rate: n/a (single mechanical stop-loss exit)
- Active strategies: none on CSCO post-close (re-entry allowed if CSCO re-enters top-5 momentum on a future EOD signal)

## 2026-07-02 — NO_TRADE (large_cap_momentum_top5 — data staleness)
- Decision file: `decisions/2026-07-02/2038_CSCO.json`
- Fresh ENTRY signal fired but computed on 2026-06-15 daily bars (12 trading days stale; yfinance TLS-blocked, Alpaca free-IEX lag). Per CLAUDE.md rule #5, no entry on stale momentum ranks.
- Not held (closed 2026-07-01). No capital deployed. Re-evaluate on next fresh session.
- Routine: end_of_day_2026-07-02, mode PAPER_TRADING, cb_state=FULL (write skipped, 4 pending broker; throttle 1.0). RM APPROVED / Compliance APPROVED. See logs/risk_events/2026-07-02_203800_data_staleness.md.

## 2026-07-03 — NO_TRADE (large_cap_momentum_top5 — market closed + data staleness)
- Decision file: `decisions/2026-07-03/2042_CSCO.json`
- Routine: end_of_day_2026-07-03 (US market CLOSED — Independence Day observed; no trading session).
- Signal: large_cap_momentum_top5 ENTRY re-fired (rank 1, +53.68% 126d momentum). SPY trend filter intact (above 210d MA).
- Outcome: **NO_TRADE** — stale daily bars (2026-06-16 = ~11 trading days stale) + no session to fill against. Per CLAUDE.md rule #5, no fresh ENTRY on stale momentum ranks without a live session. Re-evaluate on next trading day.
- Risk Manager: APPROVED (NO_TRADE reduces risk). Compliance: APPROVED.

## 2026-07-04 — weekly_review self_learning: prediction reconciliation (W27)
- Reconciles: `memory/prediction_reviews/2026-07-01.md` (market_open) Prediction 2 — "CSCO does NOT durably reclaim and hold >= 117.00 on clean prints through 07-01; the ~117.18 exit did not close a still-valid position." Confidence 0.6 (borderline; the run's lowest-confidence call, explicitly flagged for outcome review).
- **Outcome: UNRESOLVED / DEFERRED.** The resolution window was "EOD 07-01 official close," but no trustworthy fresh close ever printed: 07-01 EOD/07-02 EOD daily bars were stale (anchored 06-15/06-16), and 07-03 was the market holiday. There is no clean 07-01+ close against which to confirm whether the marginal ±0.25%-straddle exit was correct. Carried forward to the next fresh close (>= 2026-07-06). The exit itself was correctly gated and honored the pre-committed stop; only its *ex-post* correctness is unresolvable on stale data.
- Note: the underlying position was already closed on 2026-07-01 (see the market_open block above). This block records only the prediction outcome, not a new trade.

## 2026-07-11 — weekly_review self_learning: prediction reconciliation (W28)
- Carries the W27 open item (see the 2026-07-04 reconciliation block above): "the 2026-07-01 stop exit proves durable — price continues below the stop and does not whipsaw back."
- **Outcome: STILL UNRESOLVED / DEFERRED (2nd consecutive week).** No trustworthy fresh daily close printed anywhere in W28 — the primary daily-bar feed (yfinance TLS-blocked; Alpaca IEX daily bars) stayed anchored to ~2026-06-23 all five sessions (`journals/daily/2026-07-10.md` pre-market: bars end 06-23, ~11–16 trading days stale). The post-exit reclaim question cannot be confirmed on stale bars; carried forward to ≥ 2026-07-13 (W29). CSCO not held (closed 2026-07-01).
- Note: CSCO's stale-bar ENTRY re-fires in W28 (07-10 pre-market scan placed it at top-5 rank 1 (+52.70% on the 07-10 stale-bar scan)) were computed on ~06-23 bars and gated NO_TRADE at every EOD under CLAUDE.md rule #5; they do not constitute fresh confirmation of rank or trend. This block records the prediction status only — no new trade.
