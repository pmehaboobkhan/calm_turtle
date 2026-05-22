# Current Market Regime — 2026-05-22

## Regime Classification (Deterministic Engine)
- **Regime:** bullish_trend
- **Confidence:** medium
- **Data as of:** 2026-05-22 pre-market signal run (10:36 UTC)

## Key Technical Indicators (3+ per requirement)

1. **SPY positioning:** 
   - Above 50-day MA by +6.89%
   - Above 200-day MA (binary: YES)
   - 12-month return: +26.72% vs cash +3.95% (outperforming carry by 2276 bps)

2. **Volatility / Risk Appetite:**
   - 20-day annualized realized volatility proxy: 10.48% (used as effective VIX substitute)
   - **Limitation flag:** VIX feed unavailable; this proxy is backward-looking and does NOT capture intraday pinning, vol-of-vol spike risk, or term-structure compression. Low proxy-vol may indicate complacency rather than genuine low risk.

3. **Macro Trend Filter (SPY 10-month SMA):**
   - SPY above 10-month simple moving average: YES (passed, used by Strategy B)
   - Gold (GLD) above 10-month SMA: YES (+37.36% YTD, far outperforming equities)
   - Bonds (IEF) below 10-month SMA: YES (only +3.89%, underwater vs cash)

## Macro Narrative

**Equity strength is being driven by broad momentum: small-cap cyclicals and energy are leading.** The 12-month SPY return of +26.72% reflects a sustained bull-run narrative since mid-2025, with no regime-breaking correction. Gold's +37.36% YTD lead suggests either inflation-hedge demand OR a hedge purchase ahead of macro uncertainty — the signal is ambiguous. Bonds (IEF 7–10y duration) have returned a paltry +3.89%, just barely matching the cash carry rate, indicating that curve normalization and carry trades are draining duration demand. This is a classic risk-on environment: equities dominating, commodities rallying, bonds lagging. **The sector signal from today's large-cap momentum scan is striking:** Cisco (CSCO +54.42% 6m, rank 1), Alphabet (GOOGL +36.55%, rank 2), Exxon (XOM +32.22%, rank 3), UnitedHealth (UNH +23.75%, rank 4), and NVIDIA (+21.05%, rank 5) are the momentum leaders. Technology and Energy are clearly outperforming, while mega-cap (MSFT rank 21, ORCL rank 20) and cyclical retail (HD -5.52%) are lagging. This suggests a sector rotation OUT of the Mag-7 mega-cap narrative INTO old-economy value (Energy) and mid-tier tech (CSCO, networking).

## Sector Posture Across Watchlist

- **Technology (AAPL, MSFT, GOOGL, NVDA, ORCL, CSCO):** Bifurcated. GOOGL and CSCO (rank 2, 1) are in the top-5 momentum, but AAPL (rank 10), MSFT (rank 21), ORCL (rank 20), NVDA (rank 5, borderline) are mostly out. The mega-cap concentration trade appears to be widening / deteriorating.
- **Communication Services (GOOGL, META):** GOOGL IN (rank 2); META OUT (rank 15, +1.79% 6m). GOOGL's search/AI narrative is outweighing META's relative weakness.
- **Financials (JPM, BAC, V, MA):** All OUT (ranks 14–18). Payments (V, MA) are also weak. Banks showing no momentum tailwind — possibly yield-curve headwind or rate-cut front-running.
- **Health Care (JNJ, UNH, PFE):** UNH IN (rank 4, +23.75%); JNJ OUT (rank 9), PFE OUT (rank 11). UNH's insurance + healthcare services play is outperforming pure pharma/healthcare.
- **Consumer Staples/Discretionary (WMT, COST, AMZN, TSLA, HD):** AMZN marginally in buffer (rank 6, +20.63%); WMT out post-earnings gap-down; COST OUT (rank 8); HD OUT (rank 19); TSLA OUT (rank 12). Consumer names showing broad weakness.
- **Energy (XOM):** XOM IN (rank 3, +32.22%). Strongest momentum outside of old-tier Tech and Healthcare.
- **Commodity/Gold (GLD):** IN via both dual_momentum_taa ENTRY and permanent_overlay (Strategy C 10% allocation). Gold is the *only* asset beating SPY's YTD return by a wide margin (+37.36% vs +26.72%), signaling either inflation fears or safe-haven accumulation.

## Counter-Evidence / What Would Flip the Regime

1. **SPY losing its 10-month MA:** A break below the 10-month SMA (not just the 50dma) would be the primary technical invalidation. This is the trend filter used by Strategy B and represents a regime flip from bullish_trend to either bearish_trend or range_bound. **Watch:** GOOGL ($357.10 stop) and XOM ($142.13 stop) are currently the thinnest cushions; a broad selloff could trigger these stops and cascade into a larger correction signal.

2. **Volatility spike on no fundamental catalyst:** The 10.48% proxy-vol is historically low. If the feed is restored and the true VIX prints >18–20, complacency is breaking. A vol spike on benign macro news would suggest hidden positioning or derivative unwinds — both regime-flip triggers toward high_vol or liquidity_stress.

3. **Gold reverting while equities hold:** If GLD's +37.36% lead begins to normalize back toward SPY (narrowing the +10.6pp spread), it may signal that the hedge is being unwound — a sign that macro uncertainty is subsiding. Alternatively, if GLD rallies further while equities fall, it would indicate explicit flight-to-safety, flipping to high_vol or macro_event_driven.

4. **Bonds unexpectedly rallying (IEF breaking above 10m MA):** Currently, IEF is a dead carry. A sharp rally in duration (perhaps on Fed-pivot news, recession fears, or geopolitical de-escalation) would suggest a regime shift toward risk-off or range_bound.

5. **Earnings disappointments on the 6-month momentum leaders:** CSCO, GOOGL, and XOM (the top 3 6-month momentum names) have built-in expectations. If any report and miss, it could trigger a mean-reversion that breaks the breadth of the bullish_trend (i.e., move from bullish to range_bound or uncertain).

6. **Two consecutive down sessions (already in progress):** The portfolio is down 1.25% (05-20) and 1.77% (05-21). The hard daily-loss circuit breaker is -2%; another 0.23pp down day would trigger FULL→HALF. While not a regime flip per se, a third consecutive down day would challenge the "bullish_trend" label and warrant a re-classification to uncertain or high_vol.

## Known Working Signals in This Regime
- **6-month absolute momentum (large_cap_momentum_top5):** CSCO, GOOGL, XOM, UNH, NVDA are the highest-conviction longs.
- **Broad-market 10-month trend filter:** SPY > 10m MA has been true for months and is filtering into both strategy A (TAA) and strategy B (large-cap momentum).
- **Sector rotation trades:** Old-economy (Energy, mid-tier Tech, Healthcare services) outperforming Mag-7 and financial sectors — momentum names are rotating out of mega-cap concentration.

## Known Failing Signals in This Regime
- **Pre-earnings carries on single names:** WMT on 2026-05-20 → -8% earnings gap despite beat. Pre-earnings caution window saved the position.
- **Mega-cap mega-cap reversal trades:** AAPL, MSFT rank outside top 5. Shorting the mega-cap decline is not a bullish_trend signal (Strategy B is long-only, not taking that bet).
- **Bonds as an outperformance hedge:** IEF is essentially cash, not providing diversification benefit in this rally.

## Caution Level
**MEDIUM → ELEVATED** (from yesterday's MEDIUM, due to 2-day drawdown sequence and thinnest stops on GOOGL, XOM):
- Portfolio DD is at 4.34% (half-way to the 8% FULL→HALF circuit-breaker transition).
- Two consecutive down sessions increase the risk of a third, which would trigger a circuit-breaker throttle.
- Volatility proxy is extremely low and likely understates true market risk given the lack of a live VIX feed.
- Gold's outsized outperformance (+37.36% vs +26.72% SPY) may signal underlying macro concerns (inflation, geopolitical, or central-bank stimulus unwinding).

## Recommended Posture for Downstream Agents
- **Strategy A (dual_momentum_taa):** GLD is the sole open position (ENTRY confirmed). Hold for momentum. SPY/IEF exits are correct (IEF below 10m MA; SPY outranked by GLD).
- **Strategy B (large_cap_momentum_top5):** Maintain CSCO, GOOGL, UNH, NVDA, XOM. Monitor GOOGL and XOM stops closely. Pre-earnings scans on 2026-05-22 should exclude any names within 5 trading days of prints.
- **Strategy C (gold_permanent_overlay):** 10% GLD allocation stands; it is the outperformer YTD.
- **Risk Manager:** Expect potential circuit-breaker transition if DD reaches 8% (currently 4.34%, so ~3.66pp headroom). If a third down day occurs, re-evaluate the regime classification and consider dropping caution to HIGH_VOL or UNCERTAIN.

---

**Date:** 2026-05-22T10:36:00Z  
**Called by:** pre_market routine (deterministic regime engine + macro narrative overlay)  
**Confidence:** medium (technical structure intact; volatility proxy limits certainty; no true VIX feed)  
**Next review:** 2026-05-22 EOD (or on circuit-breaker event)
