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
