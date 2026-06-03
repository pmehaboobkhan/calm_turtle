# XOM — Per-Symbol Decision Log

**Cumulative stats (updated 2026-05-12 EOD):**

- Open paper positions: 1 (qty 40 @ $148.6497, opened 2026-05-12T20:02:25Z)
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL (latest mark): -$1.19 (close $148.62 vs entry $148.6497)
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5

## 2026-05-12 — PAPER_BUY (large_cap_momentum_top5)

- Decision file: `decisions/2026-05-12/2000_XOM.json`
- Signal: ENTRY, rank 2/21 by 6m return (+33.58%); SPY trend filter passed.
- Filled: 40 shares @ $148.6497
- Stop: $133.758, Target: $185.775, R/R: 2.5:1
- Sizing: 6% of $100k (Strategy B)
- Routine: end_of_day_2026-05-12, mode PAPER_TRADING, cb_state=FULL, throttle=1.0
- Risk Manager: APPROVED. Compliance: APPROVED.

## 2026-05-12 — EOD re-run (20:40Z, no trade)

- Routine: end_of_day_2026-05-12 (scheduled 16:30 ET re-run)
- Signal: ENTRY re-confirmed (rank 2/21, +33.58% 6m, SPY trend up).
- Position held; no fill, no close.
- Mark (2026-05-07 bar close): $146.51. Unrealized PnL: -$85.59 (-1.44%). **Lone unrealized loser today.**
- Stop ($133.758) is $12.75/share below mark; ample headroom. No exit triggered.
- cb_state=FULL, throttle=1.0.

## 2026-05-13 — EOD held (re-confirm ENTRY, no trade)

- Routine: end_of_day_2026-05-13, mode PAPER_TRADING, cb_state=OUT, throttle=0.0.
- Signal: ENTRY re-confirmed (rank 2/21 +29.76% 6m, SPY trend up).
- Quote at close $142.12 (Alpaca IEX live, 20:00:05Z; pre_close 19:36Z saw $151.33 — significant late-day reversal driven by oil-complex weakness).
- Mark vs entry $148.6497 → -$261.19 (-4.39%). Stop $133.758 (5.9% headroom).
- Decision: continue holding; no new decision file written.
- Watch: XOM gave back all of today's earlier gains in the final 25 minutes. Headroom to stop is now the tightest in the book.

## 2026-05-14 — EOD held (re-confirm ENTRY, no trade)

- Routine: end_of_day_2026-05-14, mode PAPER_TRADING, cb_state=OUT, throttle=0.0.
- Signal: ENTRY re-confirmed (rank 2/21 +27.73% 6m, SPY trend up).
- Quote at pre_close (19:41Z in-market): $152.55. Post-close IEX last $143.48 (degraded; bid $143.48 / ask $0.0 — discarded as a real mark).
- Mark vs entry $148.6497 → **+$156.01 (+2.62%)**. Stop $133.758 (12.3% headroom — recovered substantially vs yesterday's 5.9%).
- Decision: continue holding; no new decision file written.
- **Ex-dividend flag**: XOM goes ex-div 2026-05-15 ($1.03/share Q2 dividend declared 2026-05-02; record date 2026-05-15). Expect ~$1.03 (~0.68%) mechanical price drop at the open — NOT a thesis invalidation. Stop $133.758 sits ~$17.79 below the ex-div-adjusted mark; zero stop-risk impact.
- News tailwind this week: Iran/Strait of Hormuz oil-price spike; Q1 already beat ($85.14B rev, $1.16 EPS); Texas redomicile vote May 27 (governance, not thesis).

**Cumulative stats (updated 2026-05-14 EOD):**

- Open paper positions: 1 (qty 40 @ $148.6497)
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL (mark $152.55): +$156.01 (+2.62%)
- Win rate: n/a (no closed trades)
- Active strategies: large_cap_momentum_top5


## 2026-05-18 — EOD ENTRY submitted (PAPER_BUY, large_cap_momentum_top5 rank 3)

- Decision file: `decisions/2026-05-18/2041_XOM.json` (PAPER_BUY, final_status=PAPER_PROPOSED)
- Routine: end_of_day_2026-05-18, mode PAPER_TRADING, cb_state=FULL, throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY — rank 3/21, 6m +36.68%, SPY trend up. Energy = only commodity-sensitive sector in the basket (diversifier).
- Order: BUY 97 @ submitted quote $157.92; stop $142.128 (−10%), TP $197.40 (+25%), R/R 2.5:1. ~14.95% of account; per-trade risk 1.495% < 1.5% cap.
- BROKER_PAPER=alpaca: submitted to Alpaca paper sandbox, status PENDING_BROKER (order_id b65e42a2…). Queues for next-open fill. Not filled today.
- Prior pre-reset XOM position (qty 40 @ $148.6497) archived by the 2026-05-15 fresh-start reset; this is a fresh post-reset entry.
- Risk Manager: APPROVED. Compliance: APPROVED.

**Cumulative stats (updated 2026-05-18 EOD):**

- Open paper positions: 0 filled (1 BUY order PENDING_BROKER for next open)
- Closed paper trades: 0 (post-reset; pre-reset history immutable above)
- Realized PnL: $0.00 (post-reset)
- Unrealized PnL: $0.00 (no filled position)
- Win rate: n/a (no closed trades post-reset)

## 2026-05-19 — EOD fill confirmed + ENTRY maintain (NO_TRADE, large_cap_momentum_top5 rank 3)

- Decision file: `decisions/2026-05-19/2038_XOM.json` (NO_TRADE, reason=already_held_maintain)
- Routine: end_of_day_2026-05-19, mode PAPER_TRADING, cb_state=FULL (recovered HALF→FULL this run), throttle=1.0.
- Fill: 2026-05-18 PENDING_BROKER order filled at 2026-05-19 open via Alpaca mirror — **97 sh @ $160.4279** (reconcile alpaca-authoritative, mirror in sync).
- Signal: large_cap_momentum_top5 ENTRY re-confirmed — rank 3/21, 6m +38.13%, SPY trend up. ENTRY = maintain (already held); no new shares.
- Mark: quote $169.50 vs entry $160.4279 → uPnL **+$879.99 (+5.65%)** — best performer in the book.
- Risk Manager: APPROVED (maintain, no new risk). Compliance: APPROVED.

**Cumulative stats (updated 2026-05-19 EOD):**

- Open paper positions: 1 (qty 97 @ $160.4279, filled 2026-05-19 open)
- Closed paper trades: 0 (post 2026-05-15 reset)
- Realized PnL: $0.00 (post-reset)
- Unrealized PnL (mark $169.50): +$879.99 (+5.65%)
- Win rate: n/a (no closed trades post-reset)
- Active strategies: large_cap_momentum_top5

## 2026-05-20 — EOD maintain (NO_TRADE; large_cap_momentum_top5 rank 3)

- Routine: end_of_day_2026-05-20, mode PAPER_TRADING, cb_state=FULL (DD 2.62%), throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY re-confirmed — rank 3/21, 6m +38.10%, SPY trend up. ENTRY = maintain (already held); no new shares.
- Mark: EOD close $149.56 vs entry $160.4279 → uPnL **-$1,054.19 (-6.77%)**. Sharp late-day move (pre_close mark $158.23; closing print -$8.67 below). Still above per-strategy default stop_loss_pct=-10% ($144.39).
- Risk Manager: APPROVED (maintain — no stop breach, no invalidation; momentum thesis intact). Compliance: APPROVED.

**Cumulative stats (updated 2026-05-20 EOD):**

- Open paper positions: 1 (qty 97 @ $160.4279)
- Closed paper trades (all-time): 0 (post 2026-05-15 reset)
- Realized PnL (all-time): $0.00 (post-reset)
- Unrealized PnL (mark $149.56): -$1,054.19 (-6.77%)
- Win rate: n/a (no closed trades post-reset)
- Active strategies: large_cap_momentum_top5

## 2026-05-26 — PAPER_CLOSE PROPOSED (midday daily-loss-limit breach)

- Decision file: `decisions/2026-05-26/1614_XOM.json` (final_status `PAPER_PROPOSED` — NOT executed)
- Trigger: portfolio daily-loss limit breached -$569.77 / -0.563% (vs -$500 / -0.5% caps); `halt_after_daily_limit_breach=true`. Risk event: `logs/risk_events/20260526_161452_daily_loss.md`.
- Context: midday 151.59; day -$857.28 (dominant loss); +15.62% above -10% rotation stop ($127.92). Sector energy selloff on falling crude (US-Iran ceasefire / Strait reopening). Macro driver, not thesis break.
- Gates: Risk Manager APPROVED + Compliance APPROVED (PAPER_CLOSE reduces exposure; permitted in PAPER_TRADING).
- Status: position remains OPEN; midday is monitoring-only (no fills). Close/hold escalated to human via URGENT notify; pre_close re-evaluates on close.

## 2026-05-28 — NO_TRADE (maintain — stale bars + already-held) (large_cap_momentum_top5)

- Routine: end_of_day_2026-05-28, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (carried; CB write skipped on pending_broker guard), throttle=1.0.
- ENTRY re-fired (rank 3, 6m +28.03%); 97 sh held. Blocked by stale bars + already-held. Live mark $154.55, uPnL -$570.16 (+6.8% above stop).
- Decision file: `decisions/2026-05-28/1630_XOM.json`

## 2026-05-29 — PAPER_CLOSE (pre_close de-risk)
- Routine: pre_close_2026-05-29, mode PAPER_TRADING, BROKER_PAPER=alpaca, cb_state=FULL (DD 3.36%, no transition).
- CLOSE all positions per daily-loss-limit breach (logs/risk_events/20260529_160920_daily_loss.md; halt_after_daily_limit_breach=true). RM+Compliance APPROVED at midday (1609), executed at pre_close on late-day fill.
- Fill ~$145.37 vs entry $160.4279; realized ~$-1,460.62 (pre-fee, vs entry basis). Broker flat (0 open), reconcile clean.
- Decision file: decisions/2026-05-29/1609_XOM.json (final_status=PAPER_CLOSE).

## 2026-05-29 — EOD ENTRY re-fired, routed NO_TRADE (daily-loss halt active)
- Routine: end_of_day_2026-05-29, mode PAPER_TRADING, cb_state=FULL (CB write skipped, pending_broker=7), throttle=1.0.
- Signal: large_cap_momentum_top5 ENTRY re-confirmed — rank 2/21, 6m +28.43%, SPY trend up. XOM was the dominant driver of today's daily-loss breach.
- Decision: **NO_TRADE / REJECTED** (`decisions/2026-05-29/2042_XOM.json`), reason `daily_loss_halt_active` — re-buying the name that caused the breach on the same session is the revenge-trade mistake; refused. Re-entry resets next session (2026-06-01) and only if the energy selloff has not worsened.

**Cumulative stats (updated 2026-05-29 EOD):**

- Open paper positions: 0 (closed at pre_close de-risk)
- Closed paper trades (since 2026-05-18 re-entry): 1 (2026-05-29)
- Realized PnL (2026-05-29 close): -$1,460.62 (vs entry $160.4279 basis)
- Active strategies: large_cap_momentum_top5 (signal ENTRY today, blocked by daily-loss halt)

## 2026-06-01 — NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-01/1639_XOM.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 2, +28.57% 6m).
- Outcome: NO_TRADE. RM REJECTED (freshness check #11), Compliance REJECTED (RM != APPROVED).
- Reason: latest daily bar = 2026-05-29 (~92.7h stale); no 2026-06-01 close in feed. CLAUDE.md rule #5 → NO_TRADE.
- Book flat; no position opened. CB write skipped (pending_broker=7); FULL carried, throttle 1.0.

## 2026-06-02 — NO_TRADE (data_stale)

- Decision file: `decisions/2026-06-02/2040_XOM.json`
- Signal: large_cap_momentum_top5 ENTRY (rank 2, +31.91% 6m).
- Outcome: NO_TRADE. RM REJECTED (freshness hard-check #11), Compliance REJECTED (RM != APPROVED).
- Reason: latest daily bar = 2026-06-01 (~44.68h stale, ~2,680x over 60s cap); no 2026-06-02 close in daily feed at EOD (live IEX quote exists; daily-bar provider lags). CLAUDE.md rule #5 -> NO_TRADE.
- Book flat; no position opened. CB write skipped (pending_broker=7); FULL carried, throttle 1.0.

## 2026-06-03 — Pre-market RESEARCH-ONLY NO_TRADE (routine scope)

- Decision file: `decisions/2026-06-03/0642_XOM.json`
- Signal basis: `data/market/2026-06-03/0630.json`, last bar 2026-06-02.
- Signal: large_cap_momentum_top5 ENTRY (rank 2/21, 6m +30.76%, SPY trend up). Rank held vs the 06-01 basis (+31.91% -> +30.76%, no rank change).
- Outcome: **NO_TRADE / REJECTED on routine scope** (pre_market is RESEARCH_ONLY in v1).
- Operational guidance carried: **size small** — XOM drove BOTH daily-loss-halt breaches (05-26, 05-29). EOD must respect the $500 daily-loss budget.
