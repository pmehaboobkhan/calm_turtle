# Current Market Regime — 2026-06-11

## Regime Classification (Deterministic Engine)
- **Regime:** bullish_trend
- **Confidence:** medium
- **Data as of:** 2026-06-11 pre-market signal run (from `data/market/2026-06-11/0630.json`)

## Three Core Indicators

1. **SPY technical structure:**
   - Above 50-day MA (+0.85%, JSON `spy_pct_from_50dma: 0.00849`)
   - Above 200-day MA (binary: YES)
   - 12-month return: +22.36% vs cash +3.89% (carry beat by 1847 bps)
   - **NEW:** 06-10 close at $725.43, down -1.6% from 737.05 on volume 59.8M

2. **Volatility proxy:**
   - 20-day annualized realized vol: **13.99%** (up from 10.48% on 2026-05-22)
   - VIX feed still unavailable; proxy backward-looking
   - Rising proxy-vol suggests unease entering session, post-06-10 selloff

3. **Macro trend filters (10-month / 210d SMA):**
   - SPY above 10m MA: YES (used by Strategy B trend filter)
   - **GLD now BELOW 210d MA** (was ABOVE on 05-22 — major shift)
   - IEF below 210d MA (unchanged)

## Critical shift since 2026-05-22: GLD rotation

GLD has broken below its 210-day MA and flipped from ENTRY to EXIT in dual_momentum_taa. SPY is now the sole top-1 winner.

- **Strategy A (dual_momentum_taa):** rotates fully to SPY (already long SPY 20 since 06-08). GLD-A leg is FLAT; the 06-08 close already removed the GLD-A position.
- **Strategy C (gold_permanent_overlay):** permanent 10% GLD overlay is the only remaining GLD ENTRY signal. There is an ongoing recorded signal_conflict (A EXIT vs C ENTRY) that has prevented overlay re-entry while GLD is below 210d MA.
- **Interpretation:** the gold-vs-equity rotation that was bullish in May (GLD outperforming by +10.6pp) has reversed. May reflect (a) inflation expectations stabilizing, (b) equity momentum unwinding hedges, or (c) early macro liquidity normalization.

## 6-month momentum leaders (Strategy B universe — from JSON)

| Rank | Symbol | 6m Ret | vs 05-22 |
|---|---|---|---|
| 1 | CSCO | +52.27% | held rank 1 |
| 2 | XOM | +31.62% | up from rank 3 |
| 3 | UNH | +26.89% | up from rank 4 |
| 4 | JNJ | +19.60% | **up from rank 9** |
| 5 | GOOGL | +13.75% | down from rank 2 |
| 6 | COST | +11.11% | hold buffer |
| 7 | NVDA | +8.15% | **down from rank 5** — closest to demotion |

**Sector posture:**
- **Tech:** bifurcated — CSCO (networking) + GOOGL in top-5; MSFT (rank 21), AAPL (rank 9), NVDA (rank 7) cooling.
- **Energy:** XOM rank 2, continued rotation into commodity.
- **Healthcare:** UNH (rank 3) + JNJ (rank 4) — sector leadership.
- **Financials/Payments:** all out of top-5 (ranks 12-18).
- **Consumer:** WMT, COST in hold zones (rank 6, 8). No discretionary momentum.

## Counter-evidence / what would flip the regime

1. **SPY below 10-month SMA** → hard floor. Closure below triggers Strategy A→SHV and Strategy B→cash.
2. **Three consecutive down days.** 06-10 was -1.6%. A repeat 06-11 and 06-12 (especially through PPI today) would break uptrend structure.
3. **GLD cascade through 200d MA** → signals macro hedge unwanted; early warning of equity stress.
4. **Earnings misses on top-5.** CSCO, XOM, UNH, JNJ, GOOGL have priced-in momentum. (CSCO already reported Q3 beat; no earnings imminent in next 5 sessions for the top-5.)
5. **VIX feed returning >18** on no catalyst → 13.99% proxy understating risk; complacency breaking.

## Today's macro catalysts (from news_sentiment)

- **PPI (May)** 8:30 ET. Prior +1.4% MoM. Hot reading → equities bearish, GLD/bonds further pressure.
- **Initial jobless claims** 8:30 ET. Prior 225k.
- **FOMC June 16-17** (5 sessions out) will price today's data.

## Recommended posture for downstream agents

- **Strategy A:** stay long SPY 20 (already held). GLD-A leg flat; no re-entry while GLD < 210d MA.
- **Strategy B:** maintain CSCO/XOM/UNH/GOOGL. **NEW signal:** JNJ now in top-5 (already held since 06-08 rotation). NVDA at rank 7 — boundary; demotion if it falls outside hold zone (top-7).
- **Strategy C:** GLD permanent overlay still **blocked** by the recurring A-EXIT vs C-ENTRY conflict. Stays NO_TRADE.
- **Risk Manager:** CB FULL, DD 1.08% (well below 8% half trigger). Proxy-vol rising. Watch for third consecutive down session.

## Caution level

**MEDIUM → MEDIUM-HIGH** (from MEDIUM on 06-10):
- Proxy-vol jumped 10.48% → 13.99% over three weeks.
- GLD broke 210d MA (major regime input).
- -1.6% on 06-10 was material; PPI today could extend the move.
- 1 pending broker order outstanding (CB write paused).

---

**Date:** 2026-06-11T10:33:00Z
**Called by:** pre_market routine (deterministic regime engine + macro narrative overlay)
**Confidence:** medium (technical structure intact; rising proxy-vol; no live VIX; GLD rotation introducing uncertainty)
**Next review:** 2026-06-11 EOD (or on circuit-breaker event)
