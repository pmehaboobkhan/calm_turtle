# SPY — Per-Symbol Decision Log

**Cumulative stats (updated 2026-06-08 EOD):**

- Open paper positions: 1 PENDING_BROKER (qty 20 @ quote $737.55, ordered 2026-06-08; fills next open)
- Closed paper trades: 0
- Realized PnL: $0.00
- Unrealized PnL: n/a (order pending fill)
- Win rate: n/a (no closed trades)
- Active strategies: dual_momentum_taa (primary, top-1 risk asset); also SPY trend filter for large_cap_momentum_top5

## 2026-06-08 — PAPER_BUY (dual_momentum_taa)

- Decision file: `decisions/2026-06-08/1636_SPY.json`
- Signal: ENTRY — top-1 risk asset. 12m total return +25.18% (> cash SHV +3.93%) AND above its 210d (10-month) MA. Leadership rotated from GLD (now below its 210d MA) to SPY.
- Order: 20 shares @ quote $737.55 — PENDING_BROKER (markets closed; fills at next open, alpaca-authoritative).
- Stop: $663.79 (-10%), Target: $921.94 (+25%), R/R: 2.5:1.
- Sizing rationale: Strategy A intent 60%; per-trade risk cap (1.5% / 10% stop) reduces position to ~15% of account (14.65%), well below the 60% macro-ETF cap.
- Routine: end_of_day_2026-06-08, mode PAPER_TRADING, cb_state=FULL, throttle=1.0.
- Risk Manager: APPROVED. Compliance: APPROVED.

## 2026-07-20 midday — HOLD (NO_TRADE)

- Live IEX 746.11 vs entry 743.78 (+0.32%); no stop/target breach, no trend-filter flip. Material-adverse macro/geopolitical news flagged as risk factor but not thesis-invalidating; not corroborated by fresh quote. CB=FULL, DD 0.82%. No gates invoked (no trade proposed).
