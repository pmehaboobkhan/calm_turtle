# Current Market Regime — 2026-06-12

## Regime Classification (Deterministic Engine)
- **Regime:** bullish_trend
- **Confidence:** medium
- **Data as of:** 2026-06-12 pre-market signal run (from `data/market/2026-06-12/0630_signals.json`)

## Three Core Indicators

1. **SPY technical structure:**
   - Above 50-day MA (+2.31%, JSON `spy_pct_from_50dma: 0.023144470427523434`)
   - Above 200-day MA (binary: YES)
   - 12-month return: +23.73% vs cash +3.90% (carry beat by 1983 bps)
   - **DELTA vs 06-11:** +1.46pp increase from 50dMA distance (0.85% → 2.31%) — trend firming

2. **Volatility proxy:**
   - 20-day annualized realized vol: **15.22%** (up from 13.99% on 2026-06-11)
   - Three consecutive vol increases: 10.48% (2026-05-22) → 13.99% (06-11) → 15.22% (06-12)
   - VIX feed still unavailable; proxy backward-looking but rising
   - **RISING VOL PATTERN:** concern signal for tail-risk entry into FOMC June 16-17

3. **Macro trend filters (10-month / 210d SMA):**
   - SPY above 10m MA: YES (used by Strategy B trend filter) — unchanged
   - **GLD still BELOW 210d MA** — persistent; no recovery signal yet
   - IEF below 210d MA (unchanged)

## Momentum rank shifts vs 2026-06-11

| Rank | Symbol | 6m Ret | vs 06-11 | Status |
|---|---|---|---|---|
| 1 | CSCO | +54.88% | held rank 1 | ENTRY signal (Strategy B) |
| 2 | UNH | +26.30% | UP from rank 3 | ENTRY signal (Strategy B) — Healthcare surge |
| 3 | XOM | +25.65% | held rank 2 | ENTRY signal (Strategy B) — Energy sustained |
| 4 | JNJ | +20.51% | UP from rank 4 | ENTRY signal (Strategy B) — Healthcare leadership |
| 5 | GOOGL | +12.98% | held rank 5 | ENTRY signal (Strategy B) — Stable tech performer |
| 6 | NVDA | +10.89% | DOWN from rank 5 | NO_SIGNAL (hold zone buffer) — cooling but holding |
| 7 | COST | +10.13% | held rank 6 | NO_SIGNAL (hold zone) |

**Sector posture (new today):**
- **Healthcare explosive:** UNH +26.3%, JNJ +20.5% — top-5 duo now dominant; likely reflecting defensive rotation amid rising vol
- **Energy sustained:** XOM rank 3 — commodity momentum still attractive
- **Tech bifurcated:** CSCO (networking, +54.88% — monster performer) + GOOGL stable; but NVDA cooling (rank 5 → 6), MSFT collapsed (rank 21, -20.3% 6m), AAPL rank 8 (+6.85%)
- **Mega-cap weakness:** MSFT, AAPL, META off top-5; TSLA rank 18 (-10.3%); AMZN rank 10 (+6.0%)

## Critical shifts since 2026-06-11

1. **Proxy vol jump +122 bps:** three-session run (10.48% → 13.99% → 15.22%) narrows safety margin to high_vol threshold
   - Threshold: 20% triggers regime flip to high_vol
   - Current: 15.22% — 4.78pp cushion remaining

2. **Healthcare rotation:** UNH rank 3, JNJ rank 4 both ENTRY signals — suggests client shift toward defensive positioning ahead of FOMC
   - Consistent with rising vol unease

3. **GLD persistence below 210d MA:** prevents Strategy A re-entry and blocks Strategy C overlay. No sign of recovery yet.

4. **Strategy A posture:**
   - Still long SPY 20 (held since 06-08 per prior regime note)
   - Dual_momentum_taa 2026-06-12 signal: SPY ENTRY (redundant — already held), IEF EXIT, GLD EXIT, SHV EXIT
   - GLD-A leg remains FLAT; no momentum recovery signal

5. **Strategy B top-5 churn:**
   - New entries: CSCO, XOM, UNH, JNJ, GOOGL
   - Exited: AAPL, MSFT, AMZN, NVDA (hold), COST (hold), TLT, META, TSLA, JPM, BAC, V, MA, PFE, WMT, HD, ORCL
   - **Major rebalancing:** Healthcare + Energy + Cisco now dominant; Mag-7 largely exited except GOOGL

6. **Strategy C (gold permanent overlay):**
   - Signal: ENTRY (permanent allocation policy)
   - Status: still NO_TRADE due to recurring A-EXIT vs C-ENTRY conflict while GLD < 210d MA

## Counter-evidence / what would flip the regime

1. **Proxy-vol > 20%** → immediate hard flip to high_vol regime. Currently 4.78pp away.
2. **SPY closes below 10-month SMA** → breakage of uptrend. Triggers Strategy A→SHV cascade and Strategy B cash rotation.
3. **Three consecutive down days.** 06-10 was -1.6%. If 06-12 and 06-13 both down >0.5%, technical structure breaks. FOMC (06-16) could catalyze.
4. **GLD cascade through 200d MA** → signals macro hedge fully unwanted; early warning of equity stress or Fed policy shift.
5. **Earnings misses on top-5.** CSCO just reported beat; no earnings on CSCO/XOM/UNH/JNJ/GOOGL in next 5 days. Small window.

## Today's macro catalysts

- **PPI (May)** released 8:30 ET this morning (trigger for this pre-market scan). Prior +1.4% MoM.
- **Initial jobless claims** 8:30 ET. Prior 225k.
- **FOMC June 16-17** (4 sessions away). Likely inflation print influences Fed narrative.

## Recommended posture for downstream agents

- **Strategy A (dual_momentum_taa):** stay long SPY 20 (already held). GLD-A leg flat; no re-entry while GLD < 210d MA.
- **Strategy B (large_cap_momentum_top5):** Execute new ENTRY signals for CSCO, XOM, UNH, JNJ, GOOGL. Execute EXIT signals for AAPL, MSFT, AMZN, META, TSLA, JPM, BAC, V, MA, PFE, WMT, HD, ORCL, TLT. Hold NVDA + COST (no signal, within buffer).
- **Strategy C (gold_permanent_overlay):** GLD permanent overlay remains **NO_TRADE** — signal conflict blocking pending resolution of GLD trend recovery.
- **Risk Manager:** CB FULL (assumed from prior session; no new breach). Proxy-vol at 15.22% — monitor for third consecutive up vol session (would hit ~16.5%+, escalate yellow flag).

## Caution level

**MEDIUM-HIGH** (elevated from MEDIUM on 06-11):
- Proxy-vol three consecutive increases (10.48% → 13.99% → 15.22%) with 4.78pp cushion to high_vol flip.
- FOMC in 4 sessions; inflation data today may reset expectations.
- Healthcare rotation into top-5 (UNH, JNJ) suggests defensive unease, not confidence.
- GLD still below 210d MA (no recovery sign yet).
- Large sector rebalance today; execution risk in fills.

---

**Date:** 2026-06-12T10:31:00Z
**Called by:** pre_market routine (deterministic regime engine adoption + macro narrative overlay)
**Confidence:** medium (technical uptrend intact; but vol rising fast and healthcare rotation defensive)
**Next review:** 2026-06-12 EOD (or on circuit-breaker event, or if proxy-vol > 18%)
