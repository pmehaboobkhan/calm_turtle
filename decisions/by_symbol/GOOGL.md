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

## 2026-05-26 — PAPER_CLOSE PROPOSED (midday daily-loss-limit breach)

- Decision file: `decisions/2026-05-26/1614_GOOGL.json` (final_status `PAPER_PROPOSED` — NOT executed)
- Trigger: portfolio daily-loss limit breached -$569.77 / -0.563% (vs -$500 / -0.5% caps); `halt_after_daily_limit_breach=true`. Risk event: `logs/risk_events/20260526_161452_daily_loss.md`.
- Context: midday 386.29; day -$355.30; +16.80% above -10% rotation stop ($321.39). News bullish (TPU monetization).
- Gates: Risk Manager APPROVED + Compliance APPROVED (PAPER_CLOSE reduces exposure; permitted in PAPER_TRADING).
- Status: position remains OPEN; midday is monitoring-only (no fills). Close/hold escalated to human via URGENT notify; pre_close re-evaluates on close.

## 2026-05-28 — NO_TRADE (maintain — stale bars + already-held) (large_cap_momentum_top5)

- Routine: end_of_day_2026-05-28, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (carried; CB write skipped on pending_broker guard), throttle=1.0.
- ENTRY re-fired (rank 2, 6m +29.93%); 38 sh held. Blocked by stale bars + already-held. Live mark $368.28, uPnL -$1,039.68 (-6.9%; +3.4% above stop — weakest held name).
- Decision file: `decisions/2026-05-28/1630_GOOGL.json`

## 2026-05-29 — PAPER_CLOSE (pre_close de-risk)
- Routine: pre_close_2026-05-29, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (DD 3.36%, no transition).
- CLOSE all positions per daily-loss-limit breach (logs/risk_events/20260529_160920_daily_loss.md; halt_after_daily_limit_breach=true). RM+Compliance APPROVED at midday (1609), executed at pre_close on late-day fill.
- Fill ~$382.62 vs entry $395.6400; realized ~$-494.76 (pre-fee, vs entry basis). Broker flat (0 open), reconcile clean.
- Decision file: decisions/2026-05-29/1609_GOOGL.json (final_status=PAPER_CLOSE).

## 2026-05-29 — EOD ENTRY re-fired, routed NO_TRADE (daily-loss halt active)
- Routine: end_of_day_2026-05-29, mode PAPER_TRADING, cb_state=FULL (CB write skipped, pending_broker=7), throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY re-confirmed — rank 3/21, 6m +22.63%, SPY trend up. News neutral.
- Decision: **NO_TRADE / REJECTED** (`decisions/2026-05-29/2042_GOOGL.json`), reason `daily_loss_halt_active` — no re-entry the same session as the daily-loss halt. Re-entry resets next session (2026-06-01).

**Cumulative stats (updated 2026-05-29 EOD):**

- Open paper positions: 0 (closed at pre_close de-risk)
- Closed paper trades (since 2026-05-18 re-entry): 1 (2026-05-29)
- Realized PnL (2026-05-29 close): -$494.76 (vs entry $395.6400 basis)
- Active strategies: large_cap_momentum_top5 (signal ENTRY today, blocked by daily-loss halt)

## 2026-06-02 — NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-02/2040_GOOGL.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 5, +17.79% 6m — top-5 boundary).
- Outcome: NO_TRADE. RM REJECTED (freshness hard-check #11), Compliance REJECTED (RM != APPROVED).
- Reason: latest daily bar = 2026-06-01 (~44.68h stale, ~2,680x over 60s cap); no 2026-06-02 close in daily feed at EOD (live IEX quote exists; daily-bar provider lags). CLAUDE.md rule #5 -> NO_TRADE.
- Book flat; no position opened. CB write skipped (pending_broker=7); FULL carried, throttle 1.0.

## 2026-06-03 — Pre-market NO_SIGNAL (rank-5 boundary swap fired against)

- No decision file (NO_SIGNAL not in the v1 trade-decision schema enum; recorded for outcome tracking in `memory/prediction_reviews/2026-06-03.md`).
- Signal basis: `data/market/2026-06-03/0630.json`, last bar 2026-06-02.
- Signal: large_cap_momentum_top5 NO_SIGNAL (rank 6 or 7 in hold buffer; **fell out of top-5**). SPY trend filter PASSED; failed "GOOGL in top-5 by 126d return".
- 06-02 basis had GOOGL rank 5 (+17.79% 6m); 06-03 basis has UNH at rank 5 with GOOGL slipping to the buffer. The boundary swap predicted on 06-02 (conf 0.5) materialized.
- Outcome: no action (book flat; nothing held to EXIT). Watch: re-entry to top-5 possible on a single bar.

## 2026-06-08 — PAPER_BUY (large_cap_momentum_top5)

- Decision file: `decisions/2026-06-08/1637_GOOGL.json`
- Signal: ENTRY — rank 4 of 21 by 6m (126d) return +15.46%; SPY trend filter passed.
- Order: 16 shares @ quote $368.53 — PENDING_BROKER (fills at next open).
- Stop: $331.68, Target: $460.66, R/R: 2.5:1. Sized ~6% of account (Strategy B equal-weight top-5).
- Routine: end_of_day_2026-06-08, mode PAPER_TRADING, cb_state=FULL, throttle=1.0.
- Risk Manager: APPROVED. Compliance: APPROVED.

## 2026-07-11 — weekly_review self_learning: prediction reconciliation (W28)
- Reconciles carried-over W27 prediction (`reports/learning/weekly_learning_review_2026-07-04.md` §2, item 2): "GOOGL holds above its $331.68 stop through the NFP-driven 07-06 open" (conf 0.6 — a market-outcome call; GOOGL was the thinnest-cushion name in the book, +2.9% above stop at W27 close).
- **Outcome: RESOLVED — CORRECT.** GOOGL held above its $331.68 stop every session of W28 on live IEX quotes: 07-06 open $360.84 (+8.8% vs stop), 07-10 pre_close mark $356.61 (+7.5% vs stop); intraweek low mark ~$354.32 (midday 07-10) ≈ +6.8% above stop. `positions_to_close()` returned [] all week; no EXIT/stop breach fired. Sources: `journals/daily/2026-07-06.md` (market_open), `journals/daily/2026-07-10.md` (midday/pre_close), `memory/prediction_reviews/2026-07-08.md` P4, `2026-07-09.md` P4.
- Context (descriptive): GOOGL remained the only underwater held name all week (entry $369.80 vs marks ~$354–360). EU Android €4.1B antitrust fine finalized 07-02 (pre-priced, no fresh shock); Q2 earnings 2026-07-22 (outside window). No fresh EOD momentum re-rank possible — daily bars stale all week.
- Note: still held at W28 close; no new trade. This block records the prediction outcome only.

## 2026-07-17 — PAPER_CLOSE (midday, news-driven discretionary)

- Decision file: `decisions/2026-07-17/1206_GOOGL.json` (trigger_type: news_driven_discretionary).
- Trigger: NOT stop/target (portfolio_health should_close=FALSE, triggers=[]; stop $331.68 not breached, last ~$346.83). News-driven per midday.md step 9.
- News: Gemini 3.5 Pro delayed months + underperformed internal coding targets (Bloomberg 07-16, 403 primary; 5 URL-backed secondaries in decision news_context). GOOGL -4% on the news; rank-5 thinnest-buffer name.
- Order: 16 shares CLOSE @ last IEX $346.83 — PENDING_BROKER (Alpaca 658d3242 FILLED; realized PnL settles on reconcile). Entry was $369.80 → ~-6.2% at exit mark.
- Routine: midday_2026-07-17, mode PAPER_TRADING. cb_state=FULL (Guard-1 skip; not refreshed). EXITs never CB-throttled.
- Risk Manager: APPROVED (risk-reducing; -0.27% of account, within daily caps). Compliance: APPROVED (paper close; not a disallowed news_chase ENTRY; GOOGL not blocked).
- Caveat: daily bars stale (06-29) — deterministic top-7 rank ejection unverifiable; close leaned on discretionary news judgment. Calibration logged in `memory/prediction_reviews/2026-07-17.md` P1.
- positions.json after: SPY only (1 open).
