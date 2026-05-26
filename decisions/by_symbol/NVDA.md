# NVDA — Per-Symbol Decision Log

**Cumulative stats (created 2026-05-14 EOD):**

- Open paper positions: 0
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL: n/a (no position)
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5 (signal valid 2026-05-14, blocked by CB OUT + data staleness)

## 2026-05-14 — NO_TRADE (large_cap_momentum_top5, end_of_day)

- Decision file: `decisions/2026-05-14/2038_NVDA.json`
- Routine: end_of_day_2026-05-14, mode PAPER_TRADING, cb_state=OUT, throttle=0.0.
- Signal: ENTRY (rank 5/21 by 6m return +18.90%, SPY trend filter passed). NVDA promoted from rank 7 (hold-zone) on 2026-05-13 to rank 5 (ENTRY) today on a +3.46pp 6m return move — only *net-new* ENTRY in the slate today (AMZN slipped from rank 5 → 6 in the opposite direction).
- Decision: **NO_TRADE** with reason `circuit_breaker_OUT AND data_staleness_breach`.
  - CB state OUT mechanically blocks new opens (peak $119,140.25 inflated artifact persists into the 7th routine; DD 15.37%).
  - Daily-bar feed staleness is 6 calendar days (latest 2026-05-08 vs today 2026-05-14); `max_data_staleness_seconds = 60` exceeded.
- Intended sizing pre-throttle: ~25 shares (~$5,881 ≈ 5.88% of $100k, Strategy B target 6%). NVDA's watchlist cap is 10% (tightest in basket vs 15% standard) per watchlist note. Actual: 0 shares.
- Quote at close $235.25 (Alpaca IEX, 20:00:02Z). Stop $211.73, Target $294.06, nominal R/R 2.5:1.
- Risk Manager: APPROVED on NO_TRADE (reduces no risk). Compliance: APPROVED.
- Watch tomorrow: if either gate clears (CB peak fix lands via `prompts/proposed_updates/cb_equity_source.md` OR feed catches up), reconsider on the EOD-2026-05-15 signal.

## 2026-05-22 — PAPER_BUY (large_cap_momentum_top5, end_of_day)

**Cumulative stats (updated 2026-05-22 EOD):**

- Open paper positions: 1 (27 sh, opened 2026-05-22, PENDING_BROKER fill)
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL: n/a (order pending next-open fill; not yet a position)
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5 (ENTRY taken 2026-05-22 at rank 5)

- Decision file: `decisions/2026-05-22/1641_NVDA.json`
- Routine: end_of_day_2026-05-22, mode PAPER_TRADING, cb_state=FULL, throttle=1.0.
- Signal: ENTRY (rank 5/21 by 6m return +21.05%, SPY trend filter passed). NVDA promoted from rank 6 (NO_SIGNAL hold-zone, 2026-05-21) to rank 5 (ENTRY) today — the only net-new ENTRY in today's slate (AMZN holds rank 6, WMT rank 7, both hold-zone). The five held lines (CSCO, GLD, GOOGL, UNH, XOM) all re-confirmed ENTRY (maintain; no new decision files).
- Decision: **PAPER_BUY** — 27 shares at $219.51 (2026-05-21 close basis) = $5,926.77 = 5.84% of $101,510.01 equity. Stop $197.559 (-10%), target $274.3875 (+25%), R/R 2.5:1.
- CB FULL, throttle 1.0 → effective_qty = intended 27 (un-throttled). DD 2.48% (recovered from 4.34% on 2026-05-21), well below the 8% FULL→HALF trigger.
- Risk Manager: APPROVED (5.84% < 10% NVDA cap; per-trade risk 0.584% < 1.5%; post-open 6 positions ≤ 8; 1 trade today ≤ 5; second Tech line w/ CSCO noted, not a concentration breach). Compliance: APPROVED (in watchlist, not blocked, all theses present, no live path).
- Execution: order submitted to Alpaca paper sandbox (mirror mode), order_id 14d3ade1, OrderStatus.ACCEPTED, status PENDING_BROKER (queued for next-open fill). positions.json mirror-owned; reconcile alpaca-authoritative.
- Watch: rank-5 boundary name (lowest persistence); re-evaluate each EOD. EXIT if rank < 7 or SPY 10m-MA breaks or stop hit.

## 2026-05-26 — PAPER_CLOSE PROPOSED (midday daily-loss-limit breach)

- Decision file: `decisions/2026-05-26/1614_NVDA.json` (final_status `PAPER_PROPOSED` — NOT executed)
- Trigger: portfolio daily-loss limit breached -$569.77 / -0.563% (vs -$500 / -0.5% caps); `halt_after_daily_limit_breach=true`. Risk event: `logs/risk_events/20260526_161452_daily_loss.md`.
- Context: midday 212.75; day -$85.26; +16.43% above -10% rotation stop ($177.80). AI-chip competition narrative (mixed, not breaking).
- Gates: Risk Manager APPROVED + Compliance APPROVED (PAPER_CLOSE reduces exposure; permitted in PAPER_TRADING).
- Status: position remains OPEN; midday is monitoring-only (no fills). Close/hold escalated to human via URGENT notify; pre_close re-evaluates on close.
