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

## 2026-05-29 — EOD ENTRY re-fired, routed NO_TRADE (daily-loss halt active)
- Routine: end_of_day_2026-05-29, mode PAPER_TRADING, cb_state=FULL (CB write skipped, pending_broker=7), throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY re-confirmed — rank 4/21, 6m +21.64%, SPY trend up. News mixed (Berkshire exit vs Bernstein PT raise).
- Decision: **NO_TRADE / REJECTED** (`decisions/2026-05-29/2042_UNH.json`), reason `daily_loss_halt_active` — no re-entry the same session as the daily-loss halt. Re-entry resets next session (2026-06-01).

**Cumulative stats (updated 2026-05-29 EOD):**

- Open paper positions: 0 (closed at pre_close de-risk)
- Closed paper trades (since 2026-05-19 entry): 1 (2026-05-29)
- Realized PnL (2026-05-29 close): -$429.56 (vs entry $391.9044 basis)
- Active strategies: large_cap_momentum_top5 (signal ENTRY today, blocked by daily-loss halt)

## 2026-06-01 — NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-01/1639_UNH.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 4, +18.26% 6m).
- Outcome: NO_TRADE. RM REJECTED (freshness check #11), Compliance REJECTED (RM != APPROVED).
- Reason: latest daily bar = 2026-05-29 (~92.7h stale); no 2026-06-01 close in feed. CLAUDE.md rule #5 → NO_TRADE.
- Book flat; no position opened. CB write skipped (pending_broker=7); FULL carried, throttle 1.0.

## 2026-06-03 — Pre-market RESEARCH-ONLY NO_TRADE (routine scope), NEW top-5 entrant via boundary swap

- Decision file: `decisions/2026-06-03/0642_UNH.json`
- Signal basis: `data/market/2026-06-03/0630.json`, last bar 2026-06-02.
- Signal: large_cap_momentum_top5 ENTRY (rank 5/21, 6m +16.27%, SPY trend up). **UNH replaced GOOGL at rank 5 today** — the 06-02 prediction (`memory/prediction_reviews/2026-06-02.md` GOOGL conf 0.5 fragile) materialized on a single fresh bar.
- Outcome: **NO_TRADE / REJECTED on routine scope** (pre_market is RESEARCH_ONLY in v1).
- Background bear-factors carried from `memory/symbol_profiles/UNH.md`:
  - Berkshire Q1 13F fully exited UNH (smart-money sell signal; predates this entry).
  - DOJ Medicare-Advantage probe + Optum antitrust probe — ongoing background risk.
- Boundary fragility: a single bad UNH session or strong GOOGL session can swap the rank-5 slot back; EOD should re-confirm rank on the 06-03 close.
- Prior UNH paper hold (W21-W22) closed at small realized loss via daily-loss halt despite firming rank 5 -> rank 4 within the hold; the halt, not signal/stop, determined the exit.

## 2026-06-04 — EOD NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-04/2040_UNH.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 4/21, 6m +18.34%, SPY trend up). Boundary rank; GOOGL rank 6 (+14.16%), JNJ rank 7 (+9.92%) in hold-zone buffer.
- Outcome: NO_TRADE. RM REJECTED (rule #5 stale-data), Compliance REJECTED.
- Reason: latest daily bar = 2026-06-03 (~44.7h stale, >60s cap); no 06-04 close at EOD. Stale basis compounds rank-4/5/6 boundary fragility. 4th consecutive stale EOD. CLAUDE.md rule #5 -> NO_TRADE.
- Book flat; no position opened. CB wrote this run: FULL, DD 0.00%, throttle 1.0, no transition.

## 2026-06-05 — EOD ENTRY submitted (PAPER_BUY, large_cap_momentum_top5)

- Decision file: `decisions/2026-06-05/1642_UNH.json` (PAPER_BUY, final_status=PAPER_PROPOSED)
- Routine: end_of_day_2026-06-05, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (no transition, DD 0.00%), throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY — rank 3 by 126d return (+23.94%), SPY trend filter passed. Fresh 06-05 close.
- Order: BUY 15 @ ref $396.47; stop $356.82 (-10%), TP $495.59 (+25%), R/R 2.5:1. ~5.91% of account; per-trade risk 0.591% < 1.5% cap.
- Submitted to Alpaca paper sandbox, PENDING_BROKER (order_id f02529b8…). Market closed -> next-open fill. reconcile alpaca-authoritative, mirror in sync.
- Risk Manager: APPROVED. Compliance: APPROVED. Healthcare-policy headline risk noted (unhedgeable without news feed).

**Cumulative stats (updated 2026-06-05 EOD):**

- Open paper positions: 0 filled (1 BUY order PENDING_BROKER for next open)
- Active strategies: large_cap_momentum_top5

## 2026-07-15 — pre_close overnight-risk CLOSE (PAPER_CLOSE, large_cap_momentum_top5)

- Decision file: `decisions/2026-07-15/1936_UNH.json` (PAPER_CLOSE, final_status=PAPER_FILLED)
- Routine: pre_close_2026-07-15, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (refresh skipped, pending-broker Guard 1).
- Reason: overnight_risk — UNH Q2 2026 earnings **2026-07-16 BMO** (next trading day), within holding_earnings_caution_window_days=1. NOT a stop/target trigger (portfolio_health: no invalidation, pnl +5.0% on last IEX 418.42).
- Held from 2026-06-08 entry 398.674 (15sh, stop 356.82, tp 495.59). Closed ref 418.42 (wide ~5.4% IEX spread; bid 395.67/ask 418.42); est realized ~+$296 (+5.0%), actual set by Alpaca fill. Alpaca order a0519c5f status=FILLED.
- Gates: risk_manager APPROVED → compliance_safety APPROVED. reconcile discrepancies=[], open_count=2 (GOOGL, SPY remain). Mirrors the 2026-07-14 JNJ overnight-earnings precedent.

## 2026-07-15 — EOD reconcile of pre_close close + re-entry refusal (NO_TRADE)

- Routine: end_of_day_2026-07-15, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (refresh skipped, pending-broker Guard 1: 6 pending).
- Today's pre_close CLOSE now confirmed against Alpaca fill: SELL 15 @ **418.261333** (order a0519c5f, FILLED) vs 2026-06-08 basis 398.674 → **realized +$293.81 (+4.91%)**.
- EOD re-entry check: UNH signals large_cap_momentum_top5 ENTRY again (rank 2, 6m +28.11%) but is REFUSED — decision `decisions/2026-07-15/2044_UNH.json` (NO_TRADE). Two independent grounds: (1) daily bars STALE (rule #5); (2) UNH Q2 earnings 2026-07-16 BMO still inside the overnight caution window — re-buying now would re-add the exact binary the pre_close exit removed.
- Gates: risk_manager REJECTED (freshness + earnings caution), compliance_safety REJECTED (RM != APPROVED). No paper_sim.open_position called.

**Cumulative stats (updated 2026-07-15 EOD):**

- Open paper positions: 0 (flat — closed 2026-07-15 pre_close on 07-16 earnings risk)
- Closed paper trades: 2
  - 2026-05-20→2026-05-29: BUY 39 @ 391.9044 → SELL 39 @ 380.7038 = **−$436.82** (loss)
  - 2026-06-08→2026-07-15: BUY 15 @ 398.674 → SELL 15 @ 418.2613 = **+$293.81** (win)
- Realized PnL (lifetime): **−$143.01**
- Unrealized PnL: $0.00 (flat)
- Win rate: 50% (1W / 1L)
- Active strategies: large_cap_momentum_top5
