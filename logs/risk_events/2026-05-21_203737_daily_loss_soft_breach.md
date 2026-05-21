# Risk Event — Soft Daily-Loss Breach

- **Timestamp:** 2026-05-21T20:37:37+00:00
- **Routine:** end_of_day_2026-05-21
- **Mode:** PAPER_TRADING
- **Severity:** SOFT (advisory) — hard daily-loss halt NOT triggered
- **Circuit-breaker state:** FULL → FULL (no transition); portfolio DD 4.34% (peak $104,090.72)

## What breached

Today's mark-to-market PnL on the paper portfolio is **-$1,792 (-1.77%)** vs the
prior session close ($101,363.54), and **-$1,728 (-1.71%)** vs today's session open
($101,299.21).

| Limit (`risk_limits.yaml > limits`) | Threshold | Today | Breached? |
|---|---|---|---|
| `max_daily_loss_usd` | -$500 | -$1,792 | YES (soft) |
| `max_daily_loss_pct` | -0.5% | -1.77% | YES (soft) |
| `daily_drawdown_halt_pct` (hard) | -2.0% | -1.77% | NO |

## Driver

Unrealized mark-to-market loss on held positions, driven by late-day weakness:
CSCO (last $110.38, uPnL -$947), GOOGL (last $366.22, uPnL -$1,118), XOM (last
$147.08, uPnL -$1,295), partly offset by GLD (+$181) and UNH (+$395). No trades
were closed today — entirely unrealized. All five positions remain above their
-10% stops.

## Action taken

- **No hard halt.** The hard `daily_drawdown_halt_pct` (-2.0%) was not reached,
  so trading is not halted. Posture is defensive for the remainder of the session.
- **WMT re-entry declined** (`decisions/2026-05-21/1637_WMT.json`, NO_TRADE). The
  soft breach reinforced the decision not to add fresh risk on a stale pre-earnings
  signal contradicted by a same-day -8% earnings gap-down.
- **No EXIT signals** on held positions; trend-following design holds through
  intraday noise while stops remain intact.

## Follow-up

- Monitor proximity to the hard -2% halt on tomorrow's open.
- GOOGL ($357.10 stop) and XOM ($142.13 stop) carry the thinnest cushion after
  today's drop; pre_market 2026-05-22 should re-check stop proximity.
- This is the second soft daily-loss breach in two sessions (2026-05-20 was
  -1.25%). Two consecutive down sessions; not a halt trigger, but flagged for the
  weekly review's drawdown-trend assessment.
