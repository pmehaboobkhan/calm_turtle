# AMZN — Per-Symbol Decision Log

**Cumulative stats (updated 2026-05-13 EOD):**

- Open paper positions: 0
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL: n/a (no position)
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5 (signal valid, blocked today by CB OUT + data staleness)

## 2026-05-13 — NO_TRADE (large_cap_momentum_top5, end_of_day)

- Decision file: `decisions/2026-05-13/2050_AMZN.json`
- Routine: end_of_day_2026-05-13, mode PAPER_TRADING, cb_state=OUT, throttle=0.0.
- Signal: ENTRY (rank 5/21 by 6m return +21.11%, SPY trend filter passed). AMZN displaced JNJ in the top-5 vs yesterday's pre-market.
- Decision: **NO_TRADE** with reason `circuit_breaker_OUT AND data_staleness_breach`.
  - CB state OUT mechanically blocks new opens (peak $119,140.25 inflated artifact persists; DD 16.16%).
  - Daily-bar feed staleness is 19 calendar days (latest 2026-04-24 vs today 2026-05-13); `max_data_staleness_seconds = 60` is exceeded by orders of magnitude. Per `CLAUDE.md`: stale data = NO_TRADE for that symbol.
- Intended sizing pre-throttle: ~21 shares (~$5,948 ≈ 5.95% of $100k, Strategy B target 6%). Actual: 0 shares.
- Quote at close $283.24 (Alpaca IEX live, 20:00:00Z). Stop $254.92, Target $354.05, nominal R/R 2.5:1.
- Risk Manager: APPROVED on NO_TRADE (reduces no risk). Compliance: APPROVED.
- Watch tomorrow: if either gate clears (CB peak fix lands via `prompts/proposed_updates/cb_equity_source.md` OR feed catches up), reconsider on the EOD-2026-05-14 signal.

## 2026-05-14 — NO_SIGNAL (hold-zone), no decision written

- Routine: end_of_day_2026-05-14, mode PAPER_TRADING, cb_state=OUT, throttle=0.0.
- Signal: NO_SIGNAL — rank 6/21 (+18.07% 6m), inside top-5+2 hold-zone buffer. AMZN slipped one rank (5→6) vs 2026-05-13; NVDA was promoted from rank 7→5 in the opposite direction.
- Decision: continue watching; no decision file written (NO_SIGNAL has no asymmetric thesis to record).
- Status unchanged: 0 positions; signal valid but in hold-zone, not in ENTRY cohort. If AMZN re-enters top-5 on the next routine AND the CB + staleness gates have cleared, it becomes a fresh entry candidate.

## 2026-05-27 — REJECTED (large_cap_momentum_top5, end_of_day)

- Decision file: `decisions/2026-05-27/0224_AMZN.json`
- Routine: end_of_day_2026-05-27, mode PAPER_TRADING, cb_state=FULL (carried; CB write skipped — 2 stale pending broker rows), throttle=1.0.
- Signal: ENTRY (rank 5/21 by 126d return +22.17%, SPY 10mo-SMA trend filter passed). AMZN re-enters the top-5 as NVDA slips to rank 6 / NO_SIGNAL hold-zone — the inverse of the 2026-05-14 rotation.
- Decision: **REJECTED** with reason `daily_loss_limit_breach_cooloff_active + stale_entry_bars` (two independent hard checks).
  - RM check #9/#10: the 2026-05-26 close breached the daily-loss limit (-$614.25 / -0.607%); `halt_after_daily_limit_breach=true` + `cool_off_days_after_halt=1` keep today inside the de-risk cool-off. No exposure expansion.
  - RM check #11: daily bars driving the rank are stamped 2026-05-26 (~95,062 s / ~26 h stale vs the 60 s cap); live IEX quotes diverge >4% from those closes. Per CLAUDE.md rule #5, stale entry data forces NO_TRADE.
- Intended sizing pre-rejection: 22 shares (~$5,836 ≈ 5.81% of $100,512, Strategy B target 6%). Actual: 0 shares. Entry $265.29, stop $238.76, target $331.61, R/R 2.5:1.
- Risk Manager: REJECTED. Compliance: REJECTED (defers to RM).
- Watch tomorrow: re-confirm AMZN rank-5 on fresh 2026-05-28 daily bars AND verify the daily-loss-breach cool-off has elapsed before any entry. 2026-05-28 GDP 2nd release + PCE deflator is a non-benign macro window.

## 2026-05-28 — NO_TRADE (REJECTED — stale bars) (large_cap_momentum_top5)

- Routine: end_of_day_2026-05-28, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (carried; CB write skipped on pending_broker guard), throttle=1.0.
- ENTRY signal (top-5 candidate) — NOT opened. REJECTED on stale daily bars (~44.8h, dated 2026-05-27) for the 2nd consecutive session per CLAUDE.md rule #5 / RM check #11. paper_sim.open_position NOT called. Re-qualifies only on fresh bars + still-top-5 + SPY>210d SMA.
- Decision file: `decisions/2026-05-28/1630_AMZN.json`

## 2026-06-01 — NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-01/1639_AMZN.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 5, +17.84% 6m).
- Outcome: NO_TRADE. RM REJECTED (freshness check #11), Compliance REJECTED (RM != APPROVED).
- Reason: latest daily bar = 2026-05-29 (~92.7h stale); no 2026-06-01 close in feed. CLAUDE.md rule #5 → NO_TRADE.
- Book flat; no position opened. CB write skipped (pending_broker=7); FULL carried, throttle 1.0.
