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
