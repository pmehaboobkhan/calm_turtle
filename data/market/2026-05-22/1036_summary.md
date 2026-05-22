# Market Data Summary — 2026-05-22 10:36 ET

**Data Source:** yfinance via `lib.data.get_bars()` | **Fetched:** 2026-05-22T10:41:06Z

## Freshness Verdict

✓ **All 25 watchlist symbols current through 2026-05-21** (last completed session).

- No stale or missing data detected.
- Max data staleness configured at 60 seconds; all bars within threshold.

---

## Open Positions (5 symbols, entered 2026-05-21)

| Symbol | Latest Close | 1d Move | Stop Loss | Distance to Stop | Cushion |
|--------|--------------|---------|-----------|------------------|---------|
| **CSCO** | 118.20 | +3.37% | 106.39 | +11.81 | 10.0% |
| **GLD** | 416.99 | -0.10% | 375.56 | +41.43 | 9.9% |
| **GOOGL** | 387.66 | -0.32% | 357.10 | +30.56 | 7.9% |
| **UNH** | 382.48 | -0.21% | 352.02 | +30.46 | 8.0% |
| **XOM** | 155.29 | -0.63% | 142.13 | +13.16 | 8.5% |

**Verdict:** All positions well above stop levels; tightest cushion is GOOGL at 7.9%. No stop violations.

---

## Entry-Signal Symbols: Structural Notes

**NVDA** (ENTRY signal via top-5 momentum):
- 1d: -1.77% | Volume: 202.6M (↑22.9% vs 20d avg) — elevated selling pressure despite entry signal.

**CSCO** (ENTRY signal, rank #1 momentum, 54.42% 6m return):
- 1d: +3.37% | Strong bounce; highest 6-month return in universe.

**GOOGL** (ENTRY, rank #2, 36.55% 6m), **UNH** (ENTRY, rank #4, 23.75% 6m), **XOM** (ENTRY, rank #3, 32.22% 6m):
- Minor declines (-0.32%, -0.21%, -0.63% respectively); all near entry prices; normal intraday range.

**GLD** (ENTRY via dual_momentum_taa + gold_permanent_overlay):
- -0.10% 1d | Minimal move; portfolio macro rotation into gold (top-ranked 12m momentum at +37.36%).

**WMT** (NO_SIGNAL, rank #7 out of top-5 buffer):
- -7.27% 1d | **Largest watchlist decline**. Volume: 52.9M (+186.6% vs 20d) — gap-down event; not an entry signal.

---

## Macro Regime

- **Regime:** Bullish trend (medium confidence)
- **SPY:** +0.20% 1d | Above both 50d MA and 200d MA
- **Trend filter:** Passed (SPY above 10-month MA) — dual_momentum + large_cap_momentum_top5 both active

All deterministic signals pre-computed and logged in `1036_signals.json`; no recomputation performed.

---

**File:** `/home/user/calm_turtle/data/market/2026-05-22/1036.json`
