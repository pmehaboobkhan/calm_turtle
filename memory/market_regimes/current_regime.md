# Current Market Regime — 2026-07-14

## Regime Classification (Deterministic Engine)
- **Regime:** range_bound
- **Confidence:** LOW
- **Data as of:** 2026-06-26 (bardata end; 12 trading days stale vs today 2026-07-14)
- **Detected by:** `lib.signals.detect_regime` (SPY structure + volatility proxy)

---

## REGIME FLIP SUMMARY

**Prior regime (2026-07-09):** bullish_trend/medium  
**Current regime (2026-07-14):** range_bound/low

**What broke the trend:** SPY dropped 0.68% BELOW its 50-day MA, exactly as the prior regime warned ("paper-thin margin — one bad open breaks the trend"). The 200-day MA and 10-month MA still hold above, but the 50dma exit is the technical trigger for range-bound classification.

**Proxy volatility:** Declined slightly to 16.53% annualized (from 16.87% on 07-09), reducing but **NOT eliminating** the 3.47pp cushion to high_vol hard-flip at 20%.

---

## Three Core Indicators (Current State)

1. **SPY technical structure:**
   - **Below 50-day MA:** -0.68% (versus +0.22% on 07-09) — TREND BROKEN
   - **Above 200-day MA:** YES (longer-term support still intact)
   - **Above 10-month / 210-day MA:** YES (Strategy B trend filter still passes)
   - **12-month return:** +20.12% vs cash -0.03% (carry beat 2015 bps, but short-term structure weakened)
   - **Interpretation:** Intermediate term flipped; long-term still positive. Market in consolidation / rebalancing, not decisive downtrend.

2. **Volatility proxy:**
   - **20-day annualized realized vol:** 16.53% (down 34 bps from 16.87% on 06-23)
   - **Trajectory:** Vol peaked at 16.87%, now slightly receding — suggests consolidation (not escalation)
   - **VIX feed:** UNAVAILABLE (null in data)
   - **Cushion to high_vol flip:** 3.47pp (at 20% threshold)

3. **Sector & momentum structure:**
   - **Defensive + Energy leadership:** UNH (+31.63%), JNJ (+23.59%), CSCO (+45.47% AI/networking), XOM (+14.25%), COST (+11.19%)
   - **Mega-cap growth collapse:** MSFT -23.6%, TSLA -22.0%, META -17.3% (all fully exited from Strategy B rank)
   - **Interpretation:** Sector rotation from growth → defensive/staples/energy. Consistent with **earnings season uncertainty** and risk-off positioning, not macro expansion.

---

## Counter-evidence / what would refute range_bound classification

1. **SPY closes decisively ABOVE 50dma** (needs +0.68%+ rebound) on multiple consecutive days → signals trend repair, flip back to bullish_trend.
2. **Proxy-vol > 20%** → hard regime flip to high_vol (current margin 3.47pp; could occur if market sees unexpected shock).
3. **Healthcare earnings beats** (UNH 07-16, JNJ 07-15) on strong guidance → re-ignites defensive+growth rebalance, could push toward neutral/uncertain rather than bearish.
4. **Healthcare earnings misses** (UNH 07-16, JNJ 07-15) on weak guidance → cascade into bearish_trend or liquidity_stress (Rank 2 + Rank 3 momentum stocks breaking).
5. **Unexpected macro shock or policy announcement** at any time → same-day regime flip to high_vol or macro_event_driven.
6. **GLD breaks above 210-day MA** → diversification narrative reignites; suggests equity hedging appetite returning.

---

## Macro / Sector Narrative (Deterministic + External Context)

**Narrative:** The range-bound/low regime with broken 50dma reflects a market in transition—growth leadership (mega-cap tech) has collapsed (-17% to -24% over 6 months), while defensive and energy sectors have dominated momentum screens. This sector rotation is *not* a classic bear signal but rather an **earnings-season valuation reset**: as inflation moderates and rate-cut expectations shift, the market is repricing growth relative to dividend-paying and commodity-linked assets. The collapse of short-term trend (50dma break) while longer-dated MAs (200d, 10-month) remain above suggests **consolidation within a still-positive longer-term framework**, not a decisive trend reversal.

**Event risk—critical:** Healthcare earnings land on 07-15–07-16 for UNH (Rank 2 at +31.63% 6m) and JNJ (Rank 3 at +23.59% 6m), the two momentum leaders driving the defensive sector narrative. A miss on either would break both the top-5 momentum signals *and* validate the growth-to-defensive rotation as a flight-to-safety, potentially triggering a cascade into bearish_trend or uncertain. Conversely, beats on strong forward guidance could re-stabilize the consolidation. **This is the near-term inflection point for regime confirmation or reversal.**

**Data staleness & macro blindness:** Full-history bars end 2026-06-26; macro sources (FRED, CNBC, economic calendar) are proxy-blocked and unavailable. This 12-day data lag is significant in an earnings-heavy window. Fed policy, jobless claims, inflation prints, or geopolitical shocks between 06-26 and today (07-14) are invisible to the model. Per risk protocols, this absence of macro visibility is treated as a **caution escalator**—confidence in range_bound classification is already LOW, and lack of fresh macro input justifies staying conservative on position sizing and stop discipline.

---

## Strategy posture (implied from regime; no decisions made)

**Strategy A (dual_momentum_taa):**
- Trend filter: SPY BELOW 50dma (failed) → would normally trigger EXIT / SHV allocation
- Longer MA filter: SPY ABOVE 200d + 10m MA (pass) → partial conflict
- **Regime implication:** A-strategy should consider stepping down to SHV or neutral pending regime confirmation. Prior signal (SPY ENTRY) is now technically invalidated.

**Strategy B (large_cap_momentum_top5):**
- Trend filter: SPY ABOVE 10m MA (pass) → still active
- Top-5 list: CSCO, UNH, XOM, JNJ, COST (defensive+energy)
- **Regime implication:** Entries execute on trend filter; but **stop-watch earnings for UNH/JNJ on 07-15/16**. If either misses, momentum signal breaks and rank turnover likely.

**Strategy C (gold_permanent_overlay):**
- Signal: ENTRY (permanent allocation)
- Status: GLD still BELOW 210d MA → no recovery signal yet

---

## Caution level

**MEDIUM** (elevated from prior MEDIUM-HIGH due to vol stabilizing, but sustained by earnings event risk + data staleness):

- **Trend break confirmed:** SPY < 50dma as warned on 07-09. Intermediate direction now uncertain.
- **Event risk imminent:** UNH 07-16, JNJ 07-15 earnings (Rank 2 + 3 momentum stocks). Miss = cascade.
- **Data lag:** 12 trading days behind; macro sources offline. Flying partly blind.
- **Sector rotation incomplete:** Defensive leadership could persist OR reverse on earnings beats. No clear conviction.
- **Vol still elevated:** 16.53% annualized; 3.47pp to high_vol flip. If surprise macro shock or earnings shock → vol could spike fast.

**Factors *not* pushing to HIGH:**
- 200d MA + 10m MA still support longer-term trend.
- Proxy vol declining, not escalating.
- No circuit-breaker event triggered.
- Range-bound is *not* bearish; it's consolidation.

---

## Recommended posture for downstream agents

- **Risk Manager:**
  - Assume **range_bound is operational** on stale data.
  - **Prepare for earnings shock:** UNH/JNJ earnings 07-15–07-16 may trigger vol spike or rank turnover. Have SHV escalation ready.
  - If proxy-vol > 18% (yellow flag) or SPY rallies back above 50dma, **re-run regime detection** before extending positions.
  - Data lag + macro blindness → bias toward HALF position sizing or neutral on new entries until data refreshes post-earnings.

- **Strategy A:**
  - Prior ENTRY signal (bullish_trend) is **technically invalidated** by 50dma break.
  - **Pending regime confirmation** on fresh data post-earnings (after 07-16).
  - Consider stepping to SHV or neutral if not already hedged.

- **Strategy B:**
  - Trend filter (10m MA) still passes → signal integrity held on longer timeframe.
  - **Monitor UNH / JNJ earnings on 07-15–07-16.** On miss → stop positions and reverse rank list.
  - On beat + strong guidance → consolidation narrative holds; range_bound may persist or flip neutral.

- **Compliance:** No blocked symbols triggered. INTU remains blocked.

---

## Next review points

1. **IMMEDIATE (2026-07-15 pre-market):** Scan for UNH earnings results (expected after hours 07-15 or pre-market 07-16).
2. **IMMEDIATE (2026-07-16 pre-market):** Scan for JNJ earnings results (expected post-market 07-15 or pre-market 07-16).
3. **EOD 2026-07-16:** If either missed, escalate to bearish_trend investigation or uncertain pending fresh macro data.
4. **Routine (2026-07-16 EOD):** Refresh SPY bars on latest close; re-run regime detection if vol > 18% or SPY > 50dma.

---

**Date:** 2026-07-14T10:15:00Z (pre-market research context, no live data)  
**Called by:** Macro / Sector Context Agent (deterministic regime adoption + narrative overlay)  
**Confidence:** LOW (stale data, macro sources offline, earnings event risk, sector inflection uncertain)  
**Macro data freshness:** 2026-06-26 (bars); FRED / CNBC / economic calendar BLOCKED by proxy — treat as caution escalator  
**Next regime review:** 2026-07-16 post-UNH/JNJ earnings; or immediately if vol/tech data updates show > 18% proxy vol or SPY > 50dma

---

## Signals known to work in range_bound regimes
- Oversold bounces off support MAs (200d acts as floor)
- Earnings-driven reversals (UNH/JNJ earnings 07-15–07-16 as test case)
- Sector-rotation trades (defensive already led; energy sustained; watch for reversal)
- VIX mean-reversion if spike occurs
- Tighter stop discipline (ranges whipsaw tight stops)

## Signals known to fail in range_bound regimes
- Trend-following momentum (SPY < 50dma break already triggered exit)
- Gap-up continuation plays (consolidation chops them)
- Macro-driven directional bets (macro data offline; regime neutral to earnings)
- Long-term MA breakouts (200d/10m MA already captured; new breakout unlikely without fresh catalyst)
