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

## 2026-05-26 — PAPER_CLOSE EXECUTED (pre_close)

- Decision file: `decisions/2026-05-26/1614_NVDA.json` (final_status now `PAPER_FILLED`).
- Executed by pre_close 2026-05-26 19:46:30Z at late-day quote 214.34, 27 shares. Reason: `daily_loss_limit_breach_midday`. `halt_after_daily_limit_breach=true` mandates de-risking; pre_close CAN execute approved closes (midday cannot).
- Broker: Alpaca paper sandbox order_id 40f0f701, OrderStatus.FILLED; log row appended to `trades/paper/log.csv`. Reconcile clean: 5 open positions, 0 discrepancies (alpaca-authoritative).
- Realized P&L: +$453.09 vs original 2026-05-22 entry basis ($197.559); -$42.33 vs alpaca-mirror reset basis ($215.9078).
- Overnight-risk check: NVDA Q1 FY27 already reported 2026-05-20 AMC (rev $81.6B +85% y/y, Q2 guide $91B) — NO earnings catalyst tomorrow. Close was driven solely by the daily-loss-limit de-risking mandate, not by an overnight event.

**Cumulative stats (updated 2026-05-29 EOD):**

- Open paper positions: 0
- Closed paper trades: 1 (2026-05-26 pre_close de-risk)
- Realized PnL (this trade): +$453.09
- All-time realized PnL: +$453.09
- Win rate: 100% (1/1)
- Active strategies: large_cap_momentum_top5 (trade closed per daily-loss halt)
- Last updated: 2026-05-29 EOD

## 2026-06-01 — NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-01/1639_NVDA.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 3, +18.75% 6m).
- Outcome: NO_TRADE. RM REJECTED (freshness check #11), Compliance REJECTED (RM != APPROVED).
- Reason: latest daily bar = 2026-05-29 (~92.7h stale); no 2026-06-01 close in feed. CLAUDE.md rule #5 → NO_TRADE.
- Book flat; no position opened. CB write skipped (pending_broker=7); FULL carried, throttle 1.0.

## 2026-06-02 — NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-02/2040_NVDA.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 3, +24.48% 6m).
- Outcome: NO_TRADE. RM REJECTED (freshness hard-check #11), Compliance REJECTED (RM != APPROVED).
- Reason: latest daily bar = 2026-06-01 (~44.68h stale, ~2,680x over 60s cap); no 2026-06-02 close in daily feed at EOD (live IEX quote exists; daily-bar provider lags). CLAUDE.md rule #5 -> NO_TRADE.
- Book flat; no position opened. CB write skipped (pending_broker=7); FULL carried, throttle 1.0.

## 2026-06-03 — Pre-market RESEARCH-ONLY NO_TRADE (routine scope)

- Decision file: `decisions/2026-06-03/0642_NVDA.json`
- Signal basis: `data/market/2026-06-03/0630.json`, last bar 2026-06-02.
- Signal: large_cap_momentum_top5 ENTRY (rank 3/21, 6m +25.90%, SPY trend up). 6m return improved modestly vs the 06-01 reading (+24.48% -> +25.90%); rank 3 cushion to rank 4 (ORCL +21.85%) is +4.05pp — durable.
- Outcome: **NO_TRADE / REJECTED on routine scope** (pre_market is RESEARCH_ONLY in v1).

## 2026-06-04 — EOD NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-04/2040_NVDA.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 3/21, 6m +19.37%, SPY trend up).
- Outcome: NO_TRADE. RM REJECTED (rule #5 stale-data), Compliance REJECTED.
- Reason: latest daily bar = 2026-06-03 (~44.7h stale, >60s cap); no 06-04 close at EOD. 4th consecutive stale EOD. CLAUDE.md rule #5 -> NO_TRADE.
- Book flat; no position opened. CB wrote this run: FULL, DD 0.00%, throttle 1.0, no transition.

## 2026-06-05 — EOD ENTRY submitted (PAPER_BUY, large_cap_momentum_top5)

- Decision file: `decisions/2026-06-05/1642_NVDA.json` (PAPER_BUY, final_status=PAPER_PROPOSED)
- Routine: end_of_day_2026-06-05, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (no transition, DD 0.00%), throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY — rank 4 by 126d return (+20.65%), SPY trend filter passed. Fresh 06-05 close.
- Order: BUY 27 @ ref $218.66; stop $196.79 (-10%), TP $273.33 (+25%), R/R 2.5:1. ~5.87% of account; per-trade risk 0.587% < 1.5% cap.
- Submitted to Alpaca paper sandbox, PENDING_BROKER (order_id d3e17805…). Market closed -> next-open fill. reconcile alpaca-authoritative, mirror in sync.
- Risk Manager: APPROVED. Compliance: APPROVED. Highest beta in basket; prior daily-loss-limit involvement (2026-05-26) noted in bear thesis.

**Cumulative stats (updated 2026-06-05 EOD):**

- Open paper positions: 0 filled (1 BUY order PENDING_BROKER for next open)
- Active strategies: large_cap_momentum_top5

## 2026-07-01 — market_open: PAPER_CLOSE (EXECUTED)

- Decision file: `decisions/2026-07-01/0939_NVDA.json`
- Routine: market_open_2026-07-01 (~09:39 ET, market OPEN), mode PAPER_TRADING, BROKER_PAPER=alpaca. CB refresh SKIPPED (Guard 1: pending broker order); FULL carried forward — EXITs are never CB-throttled.
- Trigger: `lib.portfolio_health` stop_loss breach — verbatim: "stop_loss breached: BUY entered at 208.9985, stop=196.7900, current=194.7400".
- Gate chain: trade_proposal → Risk Manager APPROVED → Compliance/Safety APPROVED.
- **PAPER_CLOSE executed:** full 27-share BUY position at ~$194.51 (Alpaca IEX last-trade). Entry $208.9985. Est. realized PnL **−$391 (−6.9%)**.
- **Clean, high-confidence exit:** breach durable across multiple fresh tight-spread (~0.02–0.4%) live prints, ~1.1% below the $196.79 stop — not an open-liquidity wick.
- Reconcile: `discrepancies: []`, alpaca-authoritative, local/Alpaca parity 5==5. NVDA removed from both books.

**Cumulative stats (updated 2026-07-01 market_open):**

- Open paper positions: 0 (closed 2026-07-01 on stop breach)
- Closed paper trades this line: 1 (est. realized −$391)
- Win rate: n/a (single mechanical stop-loss exit)
- Active strategies: none on NVDA post-close (re-entry allowed if NVDA re-enters top-5 momentum on a future EOD signal)
