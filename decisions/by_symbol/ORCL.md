# ORCL — decision history

## 2026-06-02 — NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-02/2040_ORCL.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 4, +21.82% 6m — new top-5 entrant).
- Outcome: NO_TRADE. RM REJECTED (freshness hard-check #11), Compliance REJECTED (RM != APPROVED).
- Reason: latest daily bar = 2026-06-01 (~44.68h stale, ~2,680x over 60s cap); no 2026-06-02 close in daily feed at EOD (live IEX quote exists; daily-bar provider lags). CLAUDE.md rule #5 -> NO_TRADE.
- Book flat; no position opened. CB write skipped (pending_broker=7); FULL carried, throttle 1.0.

## 2026-06-03 — Pre-market RESEARCH-ONLY NO_TRADE (routine scope)

- Decision file: `decisions/2026-06-03/0642_ORCL.json`
- Signal basis: `data/market/2026-06-03/0630.json`, last bar 2026-06-02.
- Signal: large_cap_momentum_top5 ENTRY (rank 4/21, 6m +21.85%, SPY trend up). 1-bar rank-4 persistence (06-01 -> 06-02) updates the prior 06-02 "freshest entrant most likely to slip" prior — ORCL HELD rank 4 on the fresh bar.
- Outcome: **NO_TRADE / REJECTED on routine scope** (pre_market is RESEARCH_ONLY in v1).
- Watch: ORCL fiscal Q4 earnings historically print mid-June; EOD must screen for `holding_earnings_caution_window_days=1` gate.
- Note: no symbol profile in `memory/symbol_profiles/` yet; ORCL has been a top-5 entrant for only two consecutive sessions.

## 2026-06-04 — EOD NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-04/2040_ORCL.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 5/21, 6m +15.33%, SPY trend up). Lowest top-5 slot.
- Outcome: NO_TRADE. RM REJECTED (rule #5 stale-data), Compliance REJECTED.
- Reason: latest daily bar = 2026-06-03 (~44.7h stale, >60s cap); no 06-04 close at EOD. 4th consecutive stale EOD. CLAUDE.md rule #5 -> NO_TRADE.
- Compound caution: mid-June earnings window flagged but NOT confirmable (no calendar feed; news_unavailable). Even on a fresh-data session, ORCL must be re-screened against a confirmed earnings calendar (holding_earnings_caution_window_days=1) before any open.
- Book flat; no position opened. CB wrote this run: FULL, DD 0.00%, throttle 1.0, no transition.

## 2026-06-05 — EOD NO_TRADE (valid ENTRY refused: trade-budget + imminent earnings)

- Decision file: `decisions/2026-06-05/1642_ORCL.json` (NO_TRADE)
- Routine: end_of_day_2026-06-05, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL, throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY — rank 5 by 126d return (+18.25%), SPY trend filter passed. Bona-fide rank-5.
- Outcome: NO_TRADE. Two reasons: (1) max_trades_per_day=5 fully consumed by GLD/CSCO/XOM/UNH/NVDA (all higher conviction; ORCL is the lowest-momentum ENTRY candidate). (2) ORCL reports Q4 FY2026 earnings 2026-06-10 AMC (confirmed: Oracle IR + StockTitan + MarketBeat) — 3 trading days out; a fresh entry today faces a binary catalyst after ~2 sessions.
- Re-evaluate after the 06-10 print (outside the earnings caution window) if ORCL stays top-5 and budget permits.
- Risk Manager: APPROVED (refuse). Compliance: APPROVED.

**Cumulative stats (updated 2026-06-05 EOD):**

- Open paper positions: 0
- Active strategies: large_cap_momentum_top5 (ENTRY signal fired; deliberately refused today)
