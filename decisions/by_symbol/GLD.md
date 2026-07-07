# GLD — Per-Symbol Decision Log

**Cumulative stats (updated 2026-05-12 EOD):**

- Open paper positions: 1 (qty 34 @ $430.7861, opened 2026-05-12T20:02:25Z)
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL (latest mark): -$2.93 (close $430.70 vs entry $430.7861)
- Win rate: n/a (no closed trades)
- Active strategies: dual_momentum_taa (primary), gold_permanent_overlay (subsumed)

## 2026-05-12 — PAPER_BUY (dual_momentum_taa)

- Decision file: `decisions/2026-05-12/2000_GLD.json`
- Signal: ENTRY, top-1 risk asset (12m ret +38.56%, above 210d MA)
- Filled: 34 shares @ $430.7861 (quote $430.70 + slippage/half-spread)
- Stop: $387.63, Target: $538.375, R/R: 2.5:1
- Sizing rationale: Strategy A intent was 60%, Strategy C overlay 10%; per-trade risk cap (1.5% / 10% stop) reduced position to 15% of $100k; single line item satisfies both A and C.
- Routine: end_of_day_2026-05-12, mode PAPER_TRADING, cb_state=FULL, throttle=1.0
- Risk Manager: APPROVED. Compliance: APPROVED.

## 2026-05-12 — NO_TRADE (gold_permanent_overlay — subsumed)

- Decision file: `decisions/2026-05-12/2000_GLD_overlay_note.json`
- Rationale: Overlay's 10% allocation is fully covered by Strategy A's 15% GLD position above. No additional shares opened (no double-booking).

## 2026-05-12 — EOD re-run (20:40Z, no trade)

- Routine: end_of_day_2026-05-12 (scheduled 16:30 ET re-run)
- Signal: ENTRY re-confirmed (top-1 in Strategy A; +38.56% 12m; above 210d MA). Strategy C overlay also re-confirms (subsumed).
- Position held; no fill, no close.
- Mark (2026-05-07 bar close): $431.67. Unrealized PnL: +$30.05 (+0.21%).
- cb_state=FULL, throttle=1.0; equity peak $99,992.31 unchanged.

## 2026-05-13 — EOD held (re-confirm ENTRY, no trade)

- Routine: end_of_day_2026-05-13, mode PAPER_TRADING, cb_state=OUT (no transition this run), throttle=0.0.
- Signal: ENTRY re-confirmed for both strategies (dual_momentum_taa top-1; gold_permanent_overlay permanent policy).
- Quote at close $430.55. Mark vs entry $430.7861 → -$8.03 (-0.05%). Stop $387.63 (10.0% headroom).
- Decision: continue holding; no new decision file written (held-position re-confirm; no fill, no close).
- Cumulative: still 1 open position, qty 34 @ $430.7861. Day-1 friction artifact carries forward.

## 2026-05-14 — EOD held (re-confirm ENTRY, no trade)

- Routine: end_of_day_2026-05-14, mode PAPER_TRADING, cb_state=OUT (no transition; 7th consecutive routine on inflated peak), throttle=0.0.
- Signal: ENTRY re-confirmed for both strategies (dual_momentum_taa top-1: 12m +39.53% > SPY +30.88% > IEF +0.54%; gold_permanent_overlay permanent policy).
- Quote at pre_close (19:41Z in-market): $428.01. Post-close IEX last $427.56 (degraded; bid $427.10 / ask $427.56, but quote_ts 20:01Z — kept as reference only).
- Mark vs entry $430.7861 → **-$94.39 (-0.64%)**. Stop $387.63 (9.4% headroom).
- Decision: continue holding; no new decision file written (held-position re-confirm; no fill, no close).

**Cumulative stats (updated 2026-05-14 EOD):**

- Open paper positions: 1 (qty 34 @ $430.7861)
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL (mark $428.01): -$94.39 (-0.64%)
- Win rate: n/a (no closed trades)
- Active strategies: dual_momentum_taa (primary), gold_permanent_overlay (subsumed)

## 2026-05-15 — Fresh-start reset (state re-baseline)

- Event: `scripts/sync_alpaca_state.py --reset-fresh-start` at 2026-05-15T00:31:53Z
  (`logs/risk_events/2026-05-15_003153_state_reset.md`). Local positions.json
  cleared to `{}` to align with Alpaca paper (0 positions, $102,496.62 equity).
  The pre-reset GLD line (qty 34 @ $430.7861) is no longer an open position;
  prior rows above are immutable historical record only.

## 2026-05-15 — NO_TRADE (gold_permanent_overlay)

- Decision file: `decisions/2026-05-15/2041_GLD.json`
- Signal: ENTRY (gold_permanent_overlay permanent-policy; data-free). No
  dual_momentum_taa GLD signal this run — price data unavailable to evaluate
  its 12m-return / 10mo-MA confirmations.
- Routine: end_of_day_2026-05-15, mode PAPER_TRADING, cb_state=FULL (no
  transition; DD 0.00%), throttle=1.0.
- Rejection: market data unavailable for all 25 symbols (yfinance host
  blocked) and latest bar 2026-05-08 (~7 cal days, >> 60s staleness cap).
  Hard NO_TRADE gate per CLAUDE.md rule #5. No fill, no exposure.
- Risk Manager: APPROVED (NO_TRADE adds no risk). Compliance: APPROVED.

**Cumulative stats (updated 2026-05-15 EOD):**

- Open paper positions: 0 (flat post 2026-05-15T00:31:53Z fresh-start reset)
- Closed paper trades: 0 (post-reset); pre-reset history immutable above
- Realized PnL: $0.00
- Unrealized PnL: $0.00 (no open position)
- Win rate: n/a (no closed trades)
- Active strategies: dual_momentum_taa (primary), gold_permanent_overlay (subsumed) — none held; data-blocked


## 2026-05-18 — EOD ENTRY submitted (PAPER_BUY, dual_momentum_taa; subsumes gold_permanent_overlay)

- Decision file: `decisions/2026-05-18/2041_GLD.json` (PAPER_BUY, final_status=PAPER_PROPOSED)
- Subsumed note: `decisions/2026-05-18/2041_GLD_gold_permanent_overlay_subsumed.json` (NO_TRADE, Strategy-C absorbed by Strategy-A line item)
- Routine: end_of_day_2026-05-18, mode PAPER_TRADING, cb_state=FULL, throttle=1.0.
- Signal: dual_momentum_taa ENTRY — top-1 risk asset (12m +42.34% vs SPY +27.24% above MA, IEF +4.09% disqualified below MA, cash +3.98%); above 210d MA.
- Order: BUY 36 @ submitted quote $417.29; stop $375.561 (−10%), TP $521.6125 (+25%), R/R 2.5:1. ~14.66% of account; per-trade risk 1.466% < 1.5% cap.
- BROKER_PAPER=alpaca: order submitted to Alpaca paper sandbox, status PENDING_BROKER (order_id adb6c021…). Market closed at 16:41 ET → queues for next-open fill. Not filled today; positions.json mirror-owned; reconcile alpaca-authoritative (no divergence).
- Risk Manager: APPROVED. Compliance: APPROVED.

**Cumulative stats (updated 2026-05-18 EOD):**

- Open paper positions: 0 filled (1 BUY order PENDING_BROKER for next open)
- Closed paper trades: 0 (post-reset)
- Realized PnL: $0.00 (post-reset)
- Unrealized PnL: $0.00 (no filled position)
- Win rate: n/a (no closed trades post-reset)

## 2026-05-19 — EOD fill confirmed + ENTRY maintain (NO_TRADE, dual_momentum_taa; subsumes gold_permanent_overlay)

- Decision file: `decisions/2026-05-19/2038_GLD.json` (NO_TRADE, reason=already_held_maintain)
- Subsumed note: `decisions/2026-05-19/2038_GLD_gold_permanent_overlay_subsumed.json` (NO_TRADE, Strategy-C absorbed by Strategy-A line item)
- Routine: end_of_day_2026-05-19, mode PAPER_TRADING, cb_state=FULL (recovered HALF→FULL this run; see risk event), throttle=1.0.
- Fill: 2026-05-18 PENDING_BROKER order filled at 2026-05-19 open via Alpaca mirror — **36 sh @ $412.0419** (positions.json/reconcile alpaca-authoritative, mirror in sync).
- Signal: dual_momentum_taa ENTRY re-confirmed — top-1 risk asset (12m +40.49% vs cash +3.97%; SPY 12m +26.53%; IEF disqualified below MA); above 210d MA. ENTRY = maintain (already held); no new shares.
- Mark: quote $411.65 vs entry $412.0419 → uPnL **-$14.11 (-0.10%)** (flat; stop $375.561, 9.7% headroom).
- Risk Manager: APPROVED (maintain, no new risk). Compliance: APPROVED.

**Cumulative stats (updated 2026-05-19 EOD):**

- Open paper positions: 1 (qty 36 @ $412.0419, filled 2026-05-19 open)
- Closed paper trades: 0 (post 2026-05-15 reset)
- Realized PnL: $0.00 (post-reset)
- Unrealized PnL (mark $411.65): -$14.11 (-0.10%)
- Win rate: n/a (no closed trades post-reset)
- Active strategies: dual_momentum_taa (primary), gold_permanent_overlay (subsumed)

## 2026-05-20 — EOD maintain (NO_TRADE; dual_momentum_taa top-1, subsumes gold_permanent_overlay)

- Routine: end_of_day_2026-05-20, mode PAPER_TRADING, cb_state=FULL (DD 2.62%), throttle=1.0.
- Signal: dual_momentum_taa ENTRY re-confirmed — top-1 risk asset (12m +39.85% > cash +3.95%, above 210d MA). Subsumes gold_permanent_overlay ENTRY for same symbol per signal_consolidator.
- ENTRY = maintain (already held); no new shares.
- Mark: EOD close $417.58 vs entry $412.0419 → uPnL **+$199.37 (+1.34%)**.
- Risk Manager: APPROVED (maintain, no new risk). Compliance: APPROVED.

**Cumulative stats (updated 2026-05-20 EOD):**

- Open paper positions: 1 (qty 36 @ $412.0419)
- Closed paper trades (all-time): 0 (post 2026-05-15 reset)
- Realized PnL (all-time): $0.00 (post-reset)
- Unrealized PnL (mark $417.58): +$199.37 (+1.34%)
- Win rate: n/a (no closed trades post-reset)
- Active strategies: dual_momentum_taa, gold_permanent_overlay (subsumed)

## 2026-05-26 — PAPER_CLOSE PROPOSED (midday daily-loss-limit breach)

- Decision file: `decisions/2026-05-26/1614_GLD.json` (final_status `PAPER_PROPOSED` — NOT executed)
- Trigger: portfolio daily-loss limit breached -$569.77 / -0.563% (vs -$500 / -0.5% caps); `halt_after_daily_limit_breach=true`. Risk event: `logs/risk_events/20260526_161452_daily_loss.md`.
- Context: midday 413.48; day +$51.77; +18.25% above -10% rotation stop ($338.00). No material item.
- Gates: Risk Manager APPROVED + Compliance APPROVED (PAPER_CLOSE reduces exposure; permitted in PAPER_TRADING).
- Status: position remains OPEN; midday is monitoring-only (no fills). Close/hold escalated to human via URGENT notify; pre_close re-evaluates on close.

## 2026-05-28 — NO_TRADE (maintain — stale bars + already-held) (dual_momentum_taa (primary); gold_permanent_overlay (subsumed))

- Routine: end_of_day_2026-05-28, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (carried; CB write skipped on pending_broker guard), throttle=1.0.
- ENTRY re-fired (TAA top-1; subsumes gold_permanent_overlay); 36 sh held. Blocked by stale daily bars (~44.8h) AND already-held check. Live mark $412.47, uPnL +$15.41 (+11.2% above stop).
- Decision file: `decisions/2026-05-28/1630_GLD.json (+ 1630_GLD_gold_permanent_overlay_subsumed.json)`

## 2026-05-29 — PAPER_CLOSE (pre_close de-risk)
- Routine: pre_close_2026-05-29, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (DD 3.36%, no transition).
- CLOSE all positions per daily-loss-limit breach (logs/risk_events/20260529_160920_daily_loss.md; halt_after_daily_limit_breach=true). RM+Compliance APPROVED at midday (1609), executed at pre_close on late-day fill.
- Fill ~$418.02 vs entry $412.0419; realized ~$+215.21 (pre-fee, vs entry basis). Broker flat (0 open), reconcile clean.
- Decision file: decisions/2026-05-29/1609_GLD.json (final_status=PAPER_CLOSE).

## 2026-05-29 — EOD ENTRY re-fired, routed NO_TRADE (daily-loss halt active) (dual_momentum_taa primary; gold_permanent_overlay subsumed)
- Routine: end_of_day_2026-05-29, mode PAPER_TRADING, cb_state=FULL (CB write skipped, pending_broker=7), throttle=1.0.
- Signal: dual_momentum_taa ENTRY re-confirmed — GLD top-1 risk asset (12m +35.56% vs cash +3.94%, above 10m MA); subsumes gold_permanent_overlay.
- Decision: **NO_TRADE / REJECTED** (`decisions/2026-05-29/2042_GLD.json` + `_gold_permanent_overlay_subsumed.json`), reason `daily_loss_halt_active`. Open question flagged for weekly review: should the permanent GLD overlay be exempt from daily-loss de-risk? (see memory/prediction_reviews/2026-05-29.md). Re-entry resets next session (2026-06-01).

**Cumulative stats (updated 2026-05-29 EOD):**

- Open paper positions: 0 (closed at pre_close de-risk)
- Closed paper trades (since 2026-05-18 re-entry): 1 (2026-05-29)
- Realized PnL (2026-05-29 close): +$215.21 (vs entry $412.0419 basis)
- Active strategies: dual_momentum_taa + gold_permanent_overlay (signal ENTRY today, blocked by daily-loss halt)

## 2026-06-01 — NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-01/1639_GLD.json`
- Signal: dual_momentum_taa ENTRY (top-1, subsumes gold_permanent_overlay).
- Outcome: NO_TRADE. RM REJECTED (freshness check #11), Compliance REJECTED (RM != APPROVED).
- Reason: latest daily bar = 2026-05-29 (~92.7h stale); no 2026-06-01 close in feed. CLAUDE.md rule #5 → NO_TRADE.
- Book flat; no position opened. CB write skipped (pending_broker=7); FULL carried, throttle 1.0.

## 2026-06-02 — NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-02/2040_GLD.json` + `_gold_permanent_overlay_subsumed.json`
- Signal: dual_momentum_taa ENTRY (top-1, subsumes gold_permanent_overlay).
- Outcome: NO_TRADE. RM REJECTED (freshness hard-check #11), Compliance REJECTED (RM != APPROVED).
- Reason: latest daily bar = 2026-06-01 (~44.68h stale, ~2,680x over 60s cap); no 2026-06-02 close in daily feed at EOD (live IEX quote exists; daily-bar provider lags). CLAUDE.md rule #5 -> NO_TRADE.
- Book flat; no position opened. CB write skipped (pending_broker=7); FULL carried, throttle 1.0.

## 2026-06-03 — Pre-market RESEARCH-ONLY NO_TRADE (routine scope)

- Decision file: `decisions/2026-06-03/0642_GLD.json` (+ overlay subsumption stub `0642_GLD_gold_permanent_overlay_subsumed.json`)
- Signal basis: `data/market/2026-06-03/0630.json`, last bar 2026-06-02.
- Signal: dual_momentum_taa ENTRY (top-1 risk asset). 12m return +35.69% > SPY +30.35% > IEF +3.87% > cash +3.94%; above 210d MA. Gap vs SPY *widened* by +0.80pp on the fresh 06-02 close (now +5.34pp).
- Consolidation: subsumes gold_permanent_overlay overlay slot.
- Outcome: **NO_TRADE / REJECTED on routine scope** (pre_market is RESEARCH_ONLY in v1).
- Watch: persistent GLD lead can signal latent macro stress or be a head-fake; sharp SPY rally is the standard reversion path.

## 2026-06-04 — EOD NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-04/2040_GLD.json` (+ overlay subsumption stub `2040_GLD_gold_permanent_overlay_subsumed.json`)
- Signal: dual_momentum_taa ENTRY (top-1 risk asset). 12m +30.87% > SPY +28.71% > IEF +3.96% (below MA) > cash +3.92%; above 210d MA.
- Consolidation: subsumes gold_permanent_overlay overlay slot.
- Outcome: NO_TRADE. RM REJECTED (rule #5 stale-data), Compliance REJECTED.
- Reason: latest daily bar = 2026-06-03 (~44.7h stale, >60s cap); no 06-04 close at EOD. 4th consecutive stale EOD. CLAUDE.md rule #5 -> NO_TRADE.
- Book flat; no position opened. CB wrote this run: FULL, DD 0.00%, throttle 1.0, no transition.

## 2026-06-05 — EOD ENTRY submitted (PAPER_BUY, dual_momentum_taa; subsumes gold_permanent_overlay)

- Decision file: `decisions/2026-06-05/1642_GLD.json` (PAPER_BUY, final_status=PAPER_PROPOSED)
- Subsumed note: `decisions/2026-06-05/1642_GLD_gold_permanent_overlay_subsumed.json` (NO_TRADE, Strategy-C absorbed by Strategy-A line item)
- Routine: end_of_day_2026-06-05, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (no transition, DD 0.00%), throttle=1.0.
- Signal: dual_momentum_taa ENTRY — top-1 risk asset (12m +33.14% vs SPY +28.47% above MA, IEF +4.19% disqualified below MA, cash +3.91%); above 210d MA. Fresh 06-05 close (feed recovered, no stale->fresh distortion).
- Order: BUY 36 @ ref $411.27; stop $370.14 (-10%), TP $514.09 (+25%), R/R 2.5:1. ~14.72% of account; per-trade risk 1.472% < 1.5% cap.
- Submitted to Alpaca paper sandbox, status PENDING_BROKER (order_id 6ea08607…). Market closed at 16:46 ET -> queues for next-open fill. Not filled today; positions.json mirror-owned; reconcile alpaca-authoritative (no divergence, mirror in sync).
- Risk Manager: APPROVED. Compliance: APPROVED.

**Cumulative stats (updated 2026-06-05 EOD):**

- Open paper positions: 0 filled (1 BUY order PENDING_BROKER for next open)
- Closed paper trades (since 2026-05-18 re-entry): 1 (2026-05-29, +$215.21)
- Realized PnL (all-time post-reset): +$215.21
- Unrealized PnL: $0.00 (no filled position; order pending)
- Win rate: 100% (1/1 closed, post-reset)
- Active strategies: dual_momentum_taa (primary), gold_permanent_overlay (subsumed)

## 2026-06-08 — PAPER_CLOSE (dual_momentum_taa)

- Decision file: `decisions/2026-06-08/1635_GLD.json`
- Signal: EXIT — GLD below its 210d (10-month) MA; SPY now top-1 risk asset. 12m ret +27.45% (> cash) but MA filter failed.
- Closed: 36 shares (entry $397.87) at quote $397.04 — PENDING_BROKER (markets closed; fills at next open, alpaca-authoritative).
- Realized PnL at quote: -$29.88 (-0.21% on position); final realized PnL set on broker fill.
- Same-symbol CONFLICT this run: gold_permanent_overlay ENTRY vs dual_momentum_taa EXIT. v1 executes EXIT; overlay re-entry blocked as just-closed. See `logs/risk_events/2026-06-08_203250_signal_conflict.md` and `decisions/2026-06-08/1635_GLD_gold_permanent_overlay_subsumed.json`.
- Routine: end_of_day_2026-06-08, mode PAPER_TRADING, cb_state=FULL (EXITs never throttled).
- Risk Manager: APPROVED (position exists; close reduces risk). Compliance: APPROVED.

## 2026-06-10 — NO_TRADE (gold_permanent_overlay — conflict-blocked)

- Decision file: `decisions/2026-06-10/1638_GLD.json`
- Recurring same-symbol CONFLICT: gold_permanent_overlay ENTRY vs dual_momentum_taa EXIT. GLD remains below its 210d (10-month) MA → Strategy A disqualifies it (SPY is top-1 risk asset); Strategy C still wants it on policy.
- GLD is flat (closed 2026-06-08), so the A EXIT is a no-op and the C overlay ENTRY is blocked per v1 conflict rule. Overlay slot stays empty (Strategy C 0% vs 10% target).
- Risk event: `logs/risk_events/2026-06-10_203810_signal_conflict.md` (URGENT). Prior precedent: `logs/risk_events/2026-06-08_203250_signal_conflict.md`.
- Routine: end_of_day_2026-06-10, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (CB write skipped — 1 pending broker order; throttle 1.0 carried forward).
- Risk Manager: REJECTED (already-flat / conflict). Compliance: APPROVED.
- Invalidation / unblock: GLD reclaims its 210d MA, at which point A and C agree and the overlay re-entry is re-evaluated.

## 2026-07-02 — NO_TRADE (gold_permanent_overlay — conflict + data staleness)
- Decision file: `decisions/2026-07-02/2038_GLD.json`
- Recurring same-symbol CONFLICT: gold_permanent_overlay ENTRY vs dual_momentum_taa EXIT (GLD still below its 210d/10-month MA). GLD is FLAT, so A-EXIT is a no-op and C-overlay ENTRY is blocked under the v1 conflict rule. Signals additionally stale (2026-06-15 bars).
- Folded into today's data_staleness risk event rather than a fresh URGENT (both legs non-executable), consistent with 2026-06-30 handling.
- Routine: end_of_day_2026-07-02, PAPER_TRADING, cb_state=FULL (write skipped, 4 pending broker). RM REJECTED (already-flat/conflict) / Compliance APPROVED.
- Unblock: GLD reclaims its 210d MA on fresh data.

## 2026-07-03 — NO_TRADE (gold_permanent_overlay — conflict + market closed + data staleness)
- Decision file: `decisions/2026-07-03/2042_GLD.json`
- Routine: end_of_day_2026-07-03 (US market CLOSED — Independence Day observed; no trading session).
- Standing CONFLICT (since ~2026-06-11): gold_permanent_overlay ENTRY (permanent 10% policy) vs dual_momentum_taa EXIT (GLD below 210d MA; SPY top-1). GLD remains FLAT, so A-EXIT is a no-op and C-overlay ENTRY is blocked under v1 conflict rule.
- Outcome: **NO_TRADE** — standing signal conflict + stale bars (2026-06-16 = ~11 trading days stale) + no session to fill against. Per CLAUDE.md rule #5, no fresh ENTRY on stale data without live session. Conflict unblocks only when GLD reclaims 210d MA on fresh data. Re-evaluate on next trading day.
- Risk Manager: APPROVED (NO_TRADE reduces risk). Compliance: APPROVED.

## 2026-07-07 — NO_TRADE (gold_permanent_overlay — data staleness / insufficient indicators)
- Decision file: `decisions/2026-07-07/1649_GLD.json`
- Routine: end_of_day_2026-07-07, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (CB write skipped — Guard 1, 4 pending broker; throttle 1.0 carried).
- Signal: only `gold_permanent_overlay` ENTRY fired (permanent 10% policy). `dual_momentum_taa` produced NO signal this run — the deterministic regime engine returned `uncertain`/`low` with ALL indicators null because today's daily bars failed to load (yfinance TLS-blocked; Alpaca IEX daily bars stale). Consolidation `conflict=false`, `subsumed=[]` (no A-EXIT to conflict with today).
- Outcome: **NO_TRADE** — CLAUDE.md rule #5 (stale/insufficient data): quotes ~2784s stale (>60s cap); no momentum/MA confirmation computable. RM REJECTED (stale data) / Compliance APPROVED. GLD remains FLAT.
- Operational note: opening would submit a 5th real Alpaca order into an already-degraded mirror (4 stuck PENDING_BROKER rows since ~06-11; `confirm_broker_fills()` found unable to finalize them due to a status-string bug — see `logs/risk_events/2026-07-07_204950_pending_broker_mirror.md`).
- Unblock: fresh-bar session where indicators compute AND GLD reclaims its 210d MA (resolving the standing dual_momentum EXIT posture).
