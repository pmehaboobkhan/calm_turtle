# Current Market Regime — 2026-07-09

## Regime Classification (Deterministic Engine)
- **Regime:** bullish_trend
- **Confidence:** medium
- **Data as of:** 2026-07-09 pre-market signal run (from `data/market/2026-07-09/0640_signals.json`)

## CRITICAL CAVEAT: Data Staleness & Margin Fragility

**Underlying daily bars end 2026-06-23 — data is 11 trading days stale.** The margin of safety has contracted sharply since 2026-06-12:

- **SPY distance from 50dma:** +0.22% (vs +2.31% on 06-12). **Margin eroded 209 basis points in 11 days.**
  - This is paper-thin. A single 1% gap down or early vol spike could break the trend before trade execution.
  - Gap risk at market open is HIGH.

- **Proxy volatility:** 16.87% annualized (vs 15.22% on 06-12). **Rise of +165 bps in 11 days.**
  - Cushion to high_vol regime flip (20% threshold) is now only **3.13pp**.
  - At the current acceleration rate, we could reach high_vol within 1-2 more trading sessions.

**Implication:** Trend is *technically* intact on the data but *operationally fragile* today. First confirmation comes at market open.

---

## Three Core Indicators

1. **SPY technical structure:**
   - Above 50-day MA (+0.22%, JSON `spy_pct_from_50dma: 0.002225984869204778`) — BARELY
   - Above 200-day MA (binary: YES) — longer-term support intact
   - 12-month return: +23.47% vs cash -0.05% (carry beat by 2352 bps)
   - **DELTA vs 06-12:** margin above 50dma compressed from +2.31% to +0.22% — trend firming on one metric (still above 200dma) but margin of safety crumbling

2. **Volatility proxy:**
   - 20-day annualized realized vol: **16.87%** (up from 15.22% on 2026-06-12)
   - **Rising vol pattern continues:** 15.22% (06-12) → 16.87% (06-23) — another +165 bps
   - VIX feed unavailable; proxy backward-looking
   - Only 3.13pp cushion to high_vol hard-flip at 20%

3. **Macro trend filters (10-month / 210d SMA):**
   - SPY above 10m MA: YES (used by Strategy B trend filter) — unchanged
   - **GLD still BELOW 210d MA** — persistent since 06-12; no recovery signal yet
   - IEF below 210d MA (unchanged)

---

## Momentum rank snapshot vs 2026-06-12

| Rank | Symbol | 6m Ret | Sector | Status |
|---|---|---|---|---|
| 1 | CSCO | +57.50% | Networking / Semiconductors | ENTRY signal (Strategy B) — AI infrastructure |
| 2 | UNH | +24.83% | Healthcare / Insurance | ENTRY signal (Strategy B) — Defensive rotation |
| 3 | XOM | +19.89% | Energy | ENTRY signal (Strategy B) — Commodity momentum |
| 4 | NVDA | +14.99% | Semiconductors | ENTRY signal (Strategy B) — Slightly cooling |
| 5 | JNJ | +14.83% | Pharma | ENTRY signal (Strategy B) — Defensive bid |

**Sector posture (persistent from 06-12):**
- **Healthcare explosive:** UNH (rank 2) + JNJ (rank 5) both top-5. Defensive rotation, not confidence.
- **Energy sustained:** XOM rank 3 — commodity momentum still attractive.
- **AI/networking exceptional:** CSCO +57.50% (rank 1) — infrastructure/AI-refresh narrative dominant.
- **Mega-cap growth under pressure:** MSFT rank 21 (-22.7% 6m), TSLA rank 20 (-21.1% 6m), META rank 19 (-15.3% 6m).

---

## Counter-evidence / what would flip the regime

1. **SPY closes below 50dma** (current margin only +0.22%) → immediate trend break. Cascades to bearish_trend or uncertain.
2. **Proxy-vol > 20%** → hard regime flip to high_vol. Currently 3.13pp away.
3. **Three consecutive down days** → technical structure breaks. FOMC (concluded 06-16/17; outcome unknown) could have catalyzed.
4. **GLD cascade through 200dma** → signals hedging fully rejected; early warning of equity stress.
5. **Earnings misses on top-5** (CSCO/UNH/XOM/NVDA/JNJ beat cycle breaks).
6. **Unexpected macro shock** (geopolitical, policy, or systemic) → same-day regime flip.

---

## Strategy posture (as of 2026-07-09 pre-market signals)

**Strategy A (dual_momentum_taa):**
- Signal: SPY ENTRY, IEF EXIT, GLD EXIT, SHV EXIT
- Interpretation: Full shift to SPY; risk assets leading on 12-month return.
- GLD-A leg: FLAT (blocked by GLD < 210dma exit signal).

**Strategy B (large_cap_momentum_top5):**
- SPY trend filter passing (above 10m MA).
- New entries: CSCO, UNH, XOM, NVDA, JNJ
- Broad exits from underperformers (MSFT, AAPL, META, TSLA, JPM, BAC, V, MA, PFE, WMT, HD, ORCL, TLT).

**Strategy C (gold_permanent_overlay):**
- Signal: ENTRY (permanent allocation policy)
- Status: GLD ENTRY active despite A-EXIT conflict (permanent policy overrides).

---

## Caution level

**MEDIUM-HIGH** (held from 2026-06-12 but fragility deepened):

- Margin above 50dma halved in 11 days (+2.31% → +0.22%). **ONE BAD OPEN BREAKS THE TREND.**
- Proxy-vol accelerating (+165 bps in 11 days); only 3.13pp to high_vol flip.
- Data stale 11 trading days; gap risk at open.
- Defensive sector leadership (UNH/JNJ) signals caution.
- GLD flat (no diversification recovery).
- FOMC outcome (06-16/17) unknown; no shock detected yet but rate decision could have shifted expectations.

**Factors not pushing to HIGH yet:**
- SPY above 200dma (longer-term support).
- Strategy B trend filter still passing.
- No circuit-breaker event triggered.
- Healthcare/energy not collapsing.

**ESCALATION TRIGGERS (→ HIGH or hard flip):**
- SPY opens > 1% below 50dma.
- Proxy-vol > 18% at open (yellow flag for 20% imminent).
- Any sudden macro shock disclosed at open.

---

## Recommended posture for downstream agents

- **Risk Manager:** Assume bullish_trend is valid on the data, **subject to immediate reversal risk at open**.
  - Proxy-vol at 16.87% — monitor for vol > 18% (escalate yellow) or > 20% (hard flip).
  - SPY margin 0.22% — watch for gap down or volatility at open; if SPY breaks 50dma, switch to SHV immediately.

- **Strategy A:** Execute SPY ENTRY (if not held), GLD EXIT, IEF EXIT, SHV EXIT per signal. **Caution on slippage if vol spiked overnight.**

- **Strategy B:** Execute top-5 ENTRY signals (CSCO/UNH/XOM/NVDA/JNJ) and broad EXITS **only after confirming SPY structure holds at open**. Fills may be wide if market gapped.

- **Compliance:** No blocked symbols triggered.

---

**Date:** 2026-07-09T10:40:46Z (pre-market)
**Called by:** pre_market routine (deterministic regime engine adoption + macro narrative overlay)
**Confidence:** medium (technical uptrend on paper; but data stale, margin paper-thin, vol accelerating)
**Next review:** 2026-07-09 market open (URGENT if gap or vol shock); 2026-07-09 EOD (routine); ESCALATE if proxy-vol > 18% or SPY < 50dma
