# JNJ — Per-Symbol Decision Log

**Cumulative stats (updated 2026-05-12 EOD):**

- Open paper positions: 0
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL: $0.00
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5 (signal valid, deferred today)

## 2026-05-12 — NO_TRADE (large_cap_momentum_top5)

- Decision file: `decisions/2026-05-12/2000_JNJ.json`
- Signal: ENTRY, rank 5/21 by 6m return (+20.17%); SPY trend filter passed.
- Outcome: NO_TRADE — deferred by max_trades_per_day=5 cap (first 5 opens consumed today's budget for GLD, GOOGL, XOM, CSCO, WMT). Will reconsider next routine if signal still confirms.
- Routine: end_of_day_2026-05-12, mode PAPER_TRADING, cb_state=FULL, throttle=1.0
- Risk Manager: REJECTED (limit binding). Compliance: APPROVED (NO_TRADE always permissible).

## 2026-05-12 — EOD re-run (20:40Z, deferred again)

- Routine: end_of_day_2026-05-12 (scheduled 16:30 ET re-run)
- Signal: ENTRY re-confirmed (rank 5/21, +20.17% 6m, SPY trend up).
- Outcome: still NO_TRADE — `max_trades_per_day=5` cap remains binding (5/5 used by morning opens). No new decision file written this re-run; the 20:00Z NO_TRADE record remains the authoritative entry. Re-evaluate at tomorrow's pre-market with a fresh daily-trade budget.

## 2026-05-13 — NO_SIGNAL (hold-zone), no decision written

- Routine: end_of_day_2026-05-13, mode PAPER_TRADING.
- Signal: NO_SIGNAL — rank 6/21 (+17.89% 6m), inside top-5 + 2 hold-zone buffer.
- Yesterday displaced by AMZN (rank 5). No re-entry candidate this routine.
- Outcome: continue tracking. If rank slips to ≥ 8, AMZN's signal would convert to a stronger candidate; if JNJ moves back to rank ≤ 5, the strategy would issue ENTRY again.


## 2026-05-18 — EOD signal ENTRY, routed NO_TRADE (max_trades_per_day cap)

- Decision file: `decisions/2026-05-18/2041_JNJ.json` (NO_TRADE, final_status=NO_TRADE)
- Routine: end_of_day_2026-05-18, mode PAPER_TRADING, cb_state=FULL, throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY valid — rank 5/21, 6m +17.99%, SPY trend up. Cut-off slot; only ~14 bps above rank-6 UNH (+17.85%) → highest rank-volatility / least durable of the 6 ENTRY candidates.
- Decision: **NO_TRADE**, reason `max_trades_per_day_cap_reached`. 6 ENTRY signals fired; risk_limits.max_trades_per_day=5. The five higher-conviction names (CSCO r1, GLD top-1 macro, GOOGL r2, XOM r3, WMT r4) consume the daily trade budget. Dropping the marginal sixth (JNJ) is the capital-preserving choice.
- Intended sizing pre-cap: ~67 shares (~15% of account). Actual: 0 shares.
- Risk Manager: APPROVED on NO_TRADE. Compliance: APPROVED.

**Cumulative stats (updated 2026-05-18 EOD):**

- Open paper positions: 0
- Closed paper trades: 0 (post-reset)
- Realized PnL: $0.00 (post-reset)
- Win rate: n/a (no closed trades post-reset)

## 2026-06-08 — PAPER_BUY (large_cap_momentum_top5)

- Decision file: `decisions/2026-06-08/1638_JNJ.json`
- Signal: ENTRY — rank 5 of 21 by 6m (126d) return +14.62% (top-5 boundary); SPY trend filter passed.
- Order: 26 shares @ quote $232.77 — PENDING_BROKER (fills at next open).
- Stop: $209.49, Target: $290.96, R/R: 2.5:1. Sized ~6% of account (Strategy B equal-weight top-5). Defensive Health_Care diversifier vs energy/tech tilt.
- Routine: end_of_day_2026-06-08, mode PAPER_TRADING, cb_state=FULL, throttle=1.0.
- Risk Manager: APPROVED. Compliance: APPROVED.

## 2026-07-14 — PAPER_CLOSE (large_cap_momentum_top5) — overnight_risk

- Decision file: `decisions/2026-07-14/1535_JNJ.json`
- Reason: **overnight_risk** — JNJ Q2 earnings **2026-07-15 (next trading day)**; BMO/AMC session unconfirmed → treated conservatively as next-trading-day exposure (`holding_earnings_caution_window_days=1`). NOT a stop/target trigger: `lib.portfolio_health` returned no invalidation (stop 209.49 / target 290.96 both far from price).
- Order: full **26-share close** via `lib.paper_sim.close_position`, conservative long-side bid ref **253.48** (JNJ spread had tightened to ~0.04% at execution vs ~2.26% at proposal time). Est. realized P/L ≈ **+$538 (+8.9%)** vs 232.75 entry; actual set by the Alpaca fill.
- Broker: `BROKER_PAPER=alpaca`, order `e01c2828-6815-4b22-8529-a5e1aad2f587` status=FILLED; local log row stamped PENDING_BROKER (append-only); `reconcile()` alpaca-authoritative, open_count=3, discrepancies=[]; JNJ removed from positions.json + position_meta.json.
- Routine: pre_close_2026-07-14, mode PAPER_TRADING, cb_state=FULL (refresh skipped — Guard 1, pending-broker). Gates: **Risk Manager APPROVED → Compliance APPROVED**. EXITs are never CB-throttled.

**Cumulative stats (updated 2026-07-14 EOD):**

- Open paper positions: 0 (JNJ closed 2026-07-14 pre_close for overnight earnings risk)
- Closed paper trades: 1 (post-reset)
- Realized PnL: +$538.98 (est. from close ref 253.48 vs 232.75 entry × 26 sh; actual set by the Alpaca paper fill)
- Win rate: 100% (1 of 1 closed trades profitable, post-reset)
- Active strategies: large_cap_momentum_top5 (JNJ remains a top-5 momentum name, rank 3 +23.59% 6m on 2026-07-14 stale bars; a fresh re-entry was refused NO_TRADE at EOD 2026-07-14 on data-staleness + imminent 07-15 earnings — see decisions/2026-07-14/1644_JNJ.json)
- Note: EOD 2026-07-14 executed no JNJ trade; the 07-14 realized close was a pre_close action. Header updated here by the EOD performance_review step.

## 2026-07-19 — weekly_review self_learning: reconciliation (W29)
- Reconciles the 2026-07-14 pre_close overnight-earnings CLOSE (`decisions/2026-07-14/1535_JNJ.json`): 26 sh @ $232.75 entry → exit ref ~$253.48, realized **+$538.98 est** (PENDING_BROKER; Alpaca e01c2828 FILLED). Not a stop/target trigger — earnings-caution overlay ahead of JNJ Q2 07-15 BMO.
- **Outcome (descriptive):** JNJ Q2 07-15 BMO **BEAT + raised** (sales $25.31B +6.6%, adj EPS $2.90, FY ~$101.1B; `journals/daily/2026-07-17.md` news overlay). Position was closed pre-emptively before the favorable print; post-close flat, so post-beat upside is not measurable from paper marks. Gates: RM APPROVED → Compliance APPROVED (no drift). Recorded, not assessed.
