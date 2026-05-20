# Risk Event — Daily-Loss Soft Limit Breached (Midday)

- **Timestamp:** 2026-05-20T16:12:36Z
- **Routine:** midday
- **Severity:** ELEVATED (soft limit breached; halt threshold not yet hit)
- **Mode:** PAPER_TRADING

## Trigger

Today's intraday PnL crossed the soft daily-loss limits in
`config/risk_limits.yaml`, but is well clear of the 2.0% drawdown halt
threshold. No forced full-portfolio close is mandated at this level.

| Metric              | Today          | Limit                | Breached |
|---------------------|----------------|----------------------|----------|
| Day PnL (USD)       | -$745.19       | $-500 (`max_daily_loss_usd`)        | YES |
| Day PnL (%)         | -0.728%        | -0.5% (`max_daily_loss_pct`)        | YES |
| Day drawdown halt   | -0.728%        | -2.0% (`daily_drawdown_halt_pct`)   | NO  |

- Opening equity (market_open routine, 2026-05-20T13:38:28Z): $102,306.89
  (source: `journals/daily/2026-05-20.md` > Market open section, cites
  `broker.account_snapshot`).
- Current equity (midday): $101,561.70 (source:
  `broker.account_snapshot()` run at 2026-05-20T16:10-16:11Z).
- Peak equity (CB): $104,090.72 unchanged. Drawdown from peak: 2.43%.

## Decision logic

- Midday routine **does not open positions** (spec).
- `risk_limits.yaml` configures `halt_after_daily_limit_breach: true` but
  the explicit numeric **halt** trigger is `daily_drawdown_halt_pct = 2.0%`,
  which is NOT breached.
- Portfolio Health (`portfolio_health.assess_positions`) reports 0
  invalidations across all 6 open positions; no stop/target hits; no
  individual position is in distress at the per-position stop_loss_pct
  (10%) or take_profit_pct (25%) level (largest single-name uPnL is
  GOOGL -2.47%).
- Therefore the conservative action is: **flag URGENT to operator, do
  NOT auto-close positions, and route any new-entry attempts to
  NO_TRADE**. Midday already proposes zero new entries by spec, so this
  is operationally consistent.

## Open positions snapshot (midday)

| Sym   | Qty | Entry    | Mark    | uPnL$    | uPnL%   |
|-------|-----|----------|---------|----------|---------|
| CSCO  | 130 | 117.6635 | 116.02  | -$213.66 | -1.40%  |
| GLD   | 36  | 412.0419 | 416.32  | +$154.01 | +1.04%  |
| GOOGL | 38  | 395.64   | 385.88  | -$370.88 | -2.47%  |
| UNH   | 39  | 391.9044 | 384.50  | -$288.77 | -1.89%  |
| WMT   | 116 | 132.5397 | 132.90  | +$41.79  | +0.27%  |
| XOM   | 97  | 160.4279 | 158.47  | -$189.92 | -1.22%  |

Quote source: `data/market/2026-05-20/midday_1610.json`
(`lib.data.get_latest_quote`, IEX feed, fetched 2026-05-20T16:10:25Z–16:10:33Z).

## What `pre_close` must do

1. Re-evaluate daily PnL at close; if it drifts toward -2.0%, the hard
   halt rule activates and the routine **must** propose a full close.
2. WMT earnings 2026-05-21 BMO — the pre-earnings exit decision was
   already flagged; with WMT currently +0.27% it remains cheap to exit
   in an orderly fashion.
3. GOOGL is the largest single-name uPnL drag (-2.47%); still well
   inside the 10% stop, but it is the most likely driver of further
   daily-loss accumulation.
4. Reconcile sim-vs-Alpaca cash divergence (still ~$67 gap noted at
   midday, was ~$1,827 at 2026-05-19 EOD — direction is improving but
   pre_close must verify).

## What this routine did NOT do

- Did NOT open any new positions (midday is monitoring-only by spec).
- Did NOT auto-close any position (no invalidation triggers; halt
  threshold not reached).
- Did NOT propose news-driven closes (no live news feed; per CLAUDE.md
  the absence of news is a risk factor, not a thesis confirmation).
