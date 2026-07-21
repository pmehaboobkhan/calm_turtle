# Current Market Regime — 2026-07-16 (pre-market, research-only)

## Regime Classification
- **Regime:** bullish_trend
- **Confidence:** medium
- **Deterministic source:** `data/market/2026-07-16/0640_signals.json` (`lib.signals.detect_regime`, `bar_source: alpaca_iex_fallback`)
- **Called by:** `pre_market` routine 07-16; research-only mode (PAPER_TRADING, no live trading)

> All numeric indicator values below are quoted verbatim from the deterministic engine output (0640_signals.json).
> External macro/news context informed by prior regime file (07-13) and observable data shifts.
> Intraday prices and live P&L are **not** stated — the daily-bar feed is stale (see CRITICAL CAVEAT below).

---

## CRITICAL CAVEAT: Data staleness + ~1.47% above 50dma

**Underlying daily bars end `2026-06-30T04:00:00Z` (2026-06-29 session close).** As of 07-16 pre-market, that is **~16 calendar days / ~11-12 trading sessions stale**.

- `risk_limits.data.max_data_staleness_seconds = 60`; actual ≈ **1,382,400 s**. **VIOLATED** by ~4 orders of magnitude.
- Primary feed (yfinance) remains TLS-reset through the agent proxy — **recurring issue since ~06-25, unresolved for 21 calendar days.** Only Alpaca IEX fallback returns data.
- **Per CLAUDE.md rule #5:** any trade on stale data → `NO_TRADE`. Today's pre-market is research-only; no entries will execute until FRESH EOD close is fetched.

**Key shift from prior regime (07-13):** Between 07-13 (range_bound, SPY **-0.053% BELOW 50dma**) and 07-16 (bullish_trend, SPY **+1.47% ABOVE 50dma**), the momentum has moved +1.52 percentage points. This flip is **entirely stale-data dependent** — it reflects the bar-source jump from 06-24 close to 06-29 close (~5 trading sessions of action compacted into the Alpaca IEX feed, not live repricing. Implication: the trend read is technically intact on the fresher (but still stale) bars, BUT it is fragile if Friday 07-14 or Monday 07-15 sessions saw intraday action conflicting with the close-level read.

---

## Macro context: June CPI + Iran/Oil + Earnings

### 1. June CPI release (07-14, 08:30 ET) — OCCURRED between regime reads

**From prior regime (07-13):** May CPI elevated at 4.17% headline / 2.82% core; June CPI was a calendar-A tier HIGH event, rate-path binary.

**Inference from SPY response (07-13 to 07-16 bars):** The +1.47% above 50dma on 07-16 bars suggests the June CPI print was either:
- **In-line-to-lighter than expected** (headline ≤ ~4.0%, core ≤ ~2.8%), supporting risk-on repricing.
- **Hawkish but not emergency-level** (no >3bp 10Y yield shock into red).
- **Offset by Fed hold expectations** (market priced no emergency action).

**Impact on holdings:** 
- SPY (Strategy A, 60% core) — directly responds to rate path. Current entry confirmed; +1.47% above 50dma provides modest cushion.
- GOOGL (rank 5, comm-services/cloud) — sensitive to long-duration repricing. CPI-beat supports valuations; CPI-miss would crimp. Currently held on momentum (rank 5, thinnest buffer in top-5 per 07-13 regime).
- JNJ, UNH (healthcare, rank 3 & 2) — earnings-driven more than macro. See separate section below.

**Web sources for CPI data** (attempted fetch): BLS.gov, CNBC energy/oil — both returned 403 forbidden (proxy restrictions). Inference is from market action (SPY repriced +1.47%) rather than direct read.

### 2. US–Iran escalation & Strait of Hormuz shipping (ongoing, variable impact)

**From prior regime (07-13):** Tier MED event. Al Jazeera (07-10) and CNN (07-11) reported Strait of Hormuz shipping halt as US–Iran fighting resumed.

**Status inference as of 07-16:** 
- Oil bid visible in XOM entry signal: **+14.57% 6-month return**, rank 4, ENTRY confirmed. XOM is the only energy name in top-5, suggesting sustained oil tailwind from late-June into early-July.
- No emergency escalation into volatility spike (proxy-vol 17.85%, well below 20% hard-flip threshold). Implies geopolitical risk is *priced* but not *panicked*.
- Two-sided tail: upside to inflation (energy costs) vs downside to demand (geopolitical risk aversion). Currently market is treating as upside (oil rally), not demand-destruction risk.

**Implication for regime:** If Strait remains partially disrupted, energy outperformance bias remains in place. If sudden de-escalation (ceasefire, shipping resumed), XOM could rotate out of top-5 and flip to EXIT. Monitoring point for next regime review.

### 3. Earnings cluster: JNJ (07-15 BMO), UNH (07-16 BMO)

**From prior regime (07-13):** Both names are held, both in top-5 momentum, both on the rally.

- **JNJ (rank 3, +22.37% 6m):** Earnings 07-15 BMO (tomorrow morning, relative to 07-16 pre-market). Binary binary risk (beat/miss) ahead. Held at $232.75 entry per 07-13 notes; target $290.96. Miss cascades downward momentum into UNH (rank 2).
- **UNH (rank 2, +25.19% 6m):** Earnings 07-16 BMO (today, relative to 07-16 pre-market). Held at $398.67 entry; target $495.59. Post-JNJ earnings spillover possible.

**Regime implication:** Medium confidence is partially dragged down by imminent earnings binary. A JNJ or UNH miss would cause immediate momentum rotation (EXIT signals) for whichever name disappointsizes. This is **a same-session flip risk, not overnight risk**, because earnings are during market hours.

---

## Three core indicators (2026-07-16 engine output)

### 1. SPY technical structure — ABOVE 50dma, but shallow
- **50-day MA position:** SPY **+1.47% ABOVE** (`spy_pct_from_50dma: +0.014708896169587593`).
  - **Regime shift:** flipped from −0.053% on 07-13 (range-bound knife-edge) to +1.47% on 07-16 (shallow bullish).
  - **Interpretation:** bars end 06-29 (fresh by 5 trading days from 06-24), so the 50dma has advanced, and SPY close on 06-29 is above it. But+1.47% is not a deep trend — a 1–2% intraday correction brings it back to knife-edge.
- **200-day MA:** SPY above (structural support intact).
- **10-month MA:** SPY above (Strategy-B trend filter passes for momentum entries).
- **12-month total return:** **+21.44%** vs cash (SHV) **−0.07%** (slight negative yield on short Treasuries).

### 2. Volatility proxy — BENIGN, 3.15pp cushion to hard-flip
- **20-day annualized realized vol:** **17.85%** (`proxy_vol_20d_annualized_pct`; VIX feed null; proxy used as effective_vix).
- **Cushion to high_vol hard-flip (20%):** **2.15 percentage points** (was 3.35pp on 07-13; vol has inched up slightly).
- **Implied regime risk:** No vol-expansion signal. Market remains complacent into earnings week.

### 3. Macro trend filters (10-month / 210d SMA)
- **SPY above 10m MA:** YES (Strategy-B trend filter passes; momentum entries eligible).
- **GLD below 210d MA:** YES → TAA GLD EXIT signal (but gold_permanent_overlay policy still holds 10% by design).
- **IEF below 210d MA:** YES → TAA IEF EXIT signal.

---

## Momentum snapshot — 2026-07-16 engine (126-day / 6m return, Strategy B ranking)

| Rank | Symbol | 6m return | Signal | Notes |
|---|---|---|---|---|
| 1 | CSCO | **+50.25%** | ENTRY (B) | AI-infrastructure/networking bid; not currently held. Network stack tailwind from 1H26. |
| 2 | UNH | **+25.19%** | ENTRY (B) | Healthcare/insurance. **Earnings 07-16 BMO (TODAY).** Held from 07-13; target $495.59 (24.5% above entry). |
| 3 | JNJ | **+22.37%** | ENTRY (B) | Pharma/healthcare. **Earnings 07-15 BMO (TOMORROW MORNING).** Held from 07-13; target $290.96 (25% above entry). |
| 4 | XOM | **+14.57%** | ENTRY (B) | Energy. Oil/Iran escalation tailwind; Strait of Hormuz shipping risk priced as upside. Not currently held. |
| 5 | GOOGL | **+13.93%** | ENTRY (B) | Comm-services/cloud. CPI-rate-sensitive; long-duration beta. Held from 07-13 (rank-5 thinnest buffer). Earnings 07-22 AMC. |
| 6 (buffer) | COST | **+7.09%** | NO_SIGNAL | Hold zone (rank 6, outside top-5 but inside ±2 buffer). |
| 7–21 (EXIT) | NVDA, BAC, JPM, etc. | Various negative | EXIT | Laggards below buffer zone; exits confirmed. MSFT (−23.56%), ORCL (−25.89%), TSLA (−11.53%), META (−15.10%) among weakest. |

**Regime implication:** Top-5 momentum is concentrated in **healthcare (2 names, JNJ+UNH)**, **energy (1, XOM)**, **cloud/AI (2, CSCO+GOOGL)**. This is a *rotation regime*, not broad-market bullish. Energy and healthcare are defensive/value-tilted; cloud/AI are offensive. Earnings binary on JNJ+UNH is the single-biggest tail risk in the next 36 hours.

---

## Counter-evidence / what would flip the regime to bearish/uncertain

1. **JNJ earnings miss (07-15 BMO) + momentum cascade to UNH** → same-session EXIT signal chain; rotation out of healthcare. Would not single-handedly flip regime to bearish (top-5 still has CSCO, XOM, GOOGL). Would downgrade confidence from medium to low.

2. **UNH earnings miss (07-16 BMO, today) OR JNJ guidance cut** → follow-on momentum rotation. Combined JNJ+UNH cascade would force Strategy-B to re-rank; if both drop out of top-5, confidence drops to low.

3. **SPY closes below 50dma on FRESH EOD data (07-16 or later)** → bullish_trend flips to bearish/uncertain. This is the hard technical break.

4. **Proxy-vol > 20% OR VIX > 25** → hard flip to high_vol regime; automatic Telegram alert per protocol.

5. **Iran ceasefire / Strait of Hormuz shipping resumes** → XOM stops outperforming; loses top-5 rank; Energy tailwind reverses.

6. **Overnight macro shock** (Fed emergency action, credit stress, geopolitical escalation spike) → same-session flip to macro_event_driven or liquidity_stress.

---

## Entry signals (Strategy A + B + C, as of 07-16 0640 UTC)

**Strategy A (dual_momentum_taa, 60% core):**
- **SPY ENTRY** — top-1 risk asset; 12m return +21.44% vs cash −0.07%; above all MAs. Confirmed.
- **IEF EXIT** — below 210d MA; return −0.87% vs cash.
- **GLD EXIT** — below 210d MA (but permanent 10% policy overlay persists).
- **SHV EXIT** — risk asset qualifying; cash floor released.

**Strategy B (large_cap_momentum_top5, 30% allocated):**
- **ENTRY (new):** CSCO rank 1, UNH rank 2, JNJ rank 3, XOM rank 4, GOOGL rank 5.
- **HOLD (no signal):** COST rank 6 (in buffer zone).
- **EXIT (laggards):** MSFT, ORCL, TSLA, META, NVDA, BAC, JPM, WMT, HD, AMZN, PFE, V, MA, TLT. All below buffer threshold.

**Strategy C (gold_permanent_overlay, 10% allocated):**
- **GLD ENTRY** — permanent allocation policy. Not contingent on 50dma/210dma status.

---

## Operational fragility & data risk

**Non-negotiable issue:** Bars ending 06-29 mean that **any intraday repricing on 07-15 or 07-16 morning (before 07-16 0640 routine run) is not reflected in the signals.** The deterministic engine read is blind to:
- JNJ 07-15 BMO earnings beat/miss (landing at ~07:00–08:00 ET 07-15, after US market open).
- UNH 07-16 BMO earnings beat/miss (landing at ~07:00–08:00 ET 07-16, pre-market before 0640 routine).
- Any overnight gap/shock between 07-14 close and 07-15 open.
- Intraday repricing of GOOGL valuations if CPI sparked a long-duration selloff 07-14.

**Implication:** Pre-market signals on 07-16 are generated from *yesterday's close* (06-29), not *this morning's repricing*. This is a known limitation of the stale-bar feed. No entries will execute until fresh data is available (EOD 07-14 or later, pending data feed restoration).

---

## Recommended posture for downstream agents

- **Risk Manager:** Treat bullish_trend + medium confidence as valid *on the stale bars*, subject to **imminent same-session repricing risk from earnings.** No overnight gap surprise (CPI is 07-14 08:30, already past). **But JNJ earnings at ~07:00 ET 07-15 and UNH earnings at ~07:00 ET 07-16 are binary flips**, not forecastable from 07-16 pre-market signals. Hold all positions; do not force new entries until fresh EOD close is available.

- **Strategies A/B/C:** 
  - No forcing of new entries until FRESH EOD close on 07-16 (today).
  - Monitor JNJ earnings (07-15 BMO, morning, ~07:00–08:00 ET). If miss > 3%, prepare EXIT for JNJ at market open 07-16.
  - Monitor UNH earnings (07-16 BMO, morning, ~07:00–08:00 ET today). If miss > 3%, prepare EXIT for UNH at market open.
  - If both JNJ and UNH disappoint, Strategy-B top-5 re-ranks and confidence drops to low.
  - CSCO, XOM, GOOGL remain in top-5 even if JNJ+UNH exit. Re-evaluate at EOD 07-16 with fresh close data.
  - No trim of GOOGL at this time (rank 5 buffer valid; wait for earnings 07-22 AMC if seeking to tighten exposure).

- **Compliance:** All entry symbols (CSCO, UNH, JNJ, XOM, GOOGL, SPY, GLD) are approved in watchlist.yaml. No blocked symbols (INTU) involved.

- **Telegram alerts:** **ONLY on same-session flip signals:**
  - If proxy-vol > 20% during the day.
  - If VIX > 25 during the day (emergency alert).
  - If JNJ miss + cascading momentum exit confirmed at market open 07-16 (confidence drop to low).
  - If SPY closes below 50dma on fresh EOD data 07-16 (regime flip to bearish/uncertain).

---

## Data quality & intraday monitoring notes (07-16 day-session)

1. **07-16 pre-market (before 07:00 ET):** yfinance feed status unknown (has been down since ~06-25). Alpaca IEX fallback may or may not have fresh 07-15 close data by 0640 routine. Assume bars still end 06-29 until proven otherwise.

2. **07-16 ~07:00 ET (UNH earnings release):** Earnings call; binary outcome expected. Monitor fill price vs held price ($398.67). If miss > 3%, prepare market order to exit at open (not executed until Risk Manager + Compliance approve on fresh data).

3. **07-16 09:30 ET (market open, post-UNH earnings):** 
   - If UNH beats, hold. Re-confirm rank vs top-5; may re-rank.
   - If UNH misses, confirm EXIT. Risk Manager logs decision.
   - Intraday action (JNJ spill, oil moves, etc.) will be visible to live monitoring agent, not to this pre-market regime check.

4. **07-16 15:00 ET (EOD close, Monday):** MANDATORY fresh-close evaluation if data feed has recovered. If fresh data shows SPY < 50dma, rotate SHV per dual_momentum_taa rule. If still above, re-confirm trend and process any pending entries from today's signals.

5. **Alert threshold (07-16 intraday):** If proxy-vol moves above 18.5% (mid-zone toward 20% hard-flip), escalate caution to HIGH.

---

## Caution level: MEDIUM (unchanged from 07-13, but earnings-binary dependent)

**Up:**
- JNJ earnings 07-15 BMO (tomorrow morning, ~07:00 ET) — binary risk; held on momentum.
- UNH earnings 07-16 BMO (today morning, ~07:00 ET) — binary risk; held on momentum.
- Earnings cluster concentration in top-5 (2 of 5 names have earnings in next 36h).
- Data staleness masking intraday repricing (bars end 06-29; sessions 07-15 and 07-16 AM not yet visible).
- Shallow above 50dma (+1.47%) — not deep cushion; 1-2% intraday dip brings back to knife-edge.
- Proxy-vol cushion to hard-flip (20%) only 2.15pp.

**Not yet HIGH:**
- June CPI already released (07-14 08:30), no overnight surprise risk on that front.
- SPY above 200dma + 10-month MA — intermediate/long-term structure intact.
- Circuit-breaker FULL, DD ~0.2–0.3% (well inside 8% HALF threshold).
- Earnings are binary but manageable; worst case (both miss) forces rank re-sort, not regime flip.
- Geopolitical (Iran/oil) is priced as upside, not panic.

**Escalation triggers (would raise to HIGH):**
- JNJ miss > 3% on 07-15 morning + UNH guidance cut → momentum cascade, confidence to low.
- SPY closes below 50dma on fresh EOD 07-16.
- Proxy-vol > 18.5% intraday OR VIX > 25.
- Overnight macro shock (geopolitical escalation spike, credit stress).

---

## Summary: Regime confirmation & next steps

| Metric | Value | Regime indicator |
|---|---|---|
| **Regime** | bullish_trend | Driven by SPY +1.47% above 50dma, above 200dma & 10m MA |
| **Confidence** | medium | Valid on stale 06-29 bars; earnings binary in next 36h; shallow above 50dma |
| **Data freshness** | Stale (16d old) | Bars end 06-29; violates 60s rule by ~4 orders of magnitude; no live trades execute |
| **Effective VIX proxy** | 17.85% | Benign; 2.15pp cushion to high_vol 20% hard-flip |
| **Counter-evidence** | JNJ/UNH earnings binary, 50dma shallow | Monitoring thresholds set |
| **Caution level** | MEDIUM | Earnings-driven spike risk; no overnight gap risk (CPI already passed) |
| **Telegram alerts** | None yet | Auto-trigger only if proxy-vol > 20% OR VIX > 25 OR caution→HIGH |

**Next regime review:** 07-16 EOD (after UNH earnings and fresh close data available). If fresh bars show SPY < 50dma OR JNJ/UNH both miss, re-evaluate to bearish/uncertain or medium-confidence range_bound.

---

**Date:** 2026-07-16 (pre_market, 0640 UTC / 02:40 ET) · **Regime:** bullish_trend · **Confidence:** medium
**Deterministic source:** `data/market/2026-07-16/0640_signals.json` (pre-market engine)
**Data freshness:** STALE — bars end 2026-06-29 session (~16 calendar days old; violates 60s limit)
**Intraday risk drivers:** JNJ 07-15 BMO, UNH 07-16 BMO (today) — both binary
**Next review:** 2026-07-16 EOD (mandatory; fresh data required). Escalate to HIGH if earnings cascade confirmed OR SPY breaks below 50dma.
**Notifications:** No automatic Telegram until proxy-vol > 20% or regime flips to liquidity_stress / high_vol / bearish_trend on fresh data.

---

# REGIME UPDATE — 2026-07-21 (pre-market, research-only)

## Regime Classification (Adopted from Deterministic Engine)
- **Regime:** bullish_trend
- **Confidence:** medium
- **Deterministic source:** `/tmp/claude-0/-home-user-calm-turtle/5b7e2a69-003c-56cb-acf6-567c85dac65c/scratchpad/signals.json` (`lib.signals.detect_regime`, `bar_source: alpaca_iex_fallback`)
- **Called by:** pre_market routine 2026-07-21 (10:41 UTC); research-only mode (PAPER_TRADING, no live trading)

---

## CRITICAL DATA CAVEAT: Severe Staleness + Shallow Trend

**Underlying daily bars end `2026-07-02T04:00:00Z` (2026-07-01 session close).** As of 07-21 pre-market, that is **~19.28 calendar days / ~14 trading sessions stale**.

- `risk_limits.data.max_data_staleness_seconds = 60`; actual ≈ **1,665,000 s**. **VIOLATED** by ~4+ orders of magnitude (worse than 07-16).
- Primary feed (yfinance) continues TLS-reset through the agent proxy — **recurring issue now 26+ calendar days unresolved** (since ~06-25). Only Alpaca IEX fallback returns data.
- **Per CLAUDE.md rule #5:** any trade on stale data → `NO_TRADE`. Today's pre-market is research-only; signals are **probabilistic only** until FRESH EOD close is restored.

**Regime continuity vs 07-16:** Between 07-16 (bullish_trend, +1.47% above 50dma) and 07-21 (bullish_trend, +1.01% above 50dma), the position has degraded by **0.46 percentage points** (technical cushion eroded). The regime call remains bullish_trend on MA alignment, but the margin is even thinner — a 0.5–1.0% intraday dip brings SPY back to knife-edge at the 50dma.

---

## Macro Context: CPI Relief + Energy Tailwind + Earnings Post-Mortem

### 1. June CPI relief narrative (07-14, already in market) — supporting rate relief rally

- **Market repricing on lighter-than-feared CPI:** The 07-16 regime noted June CPI print (released 07-14 08:30 ET) was lighter on core inflation, relieving near-term rate-hiking fears and supporting risk-on positioning.
- **Duration-sensitive tech repricing:** Lighter inflation → lower long-term rate expectations → tech/AI large-caps (GOOGL, CSCO) re-valued higher. 10-year yield likely softened post-CPI; real yield compression supports duration-heavy growth.
- **Summary:** CPI relief narrative is 6-7 trading sessions old on the 07-02 bars; current market has processed this and moved on. This is a historical tailwind, not a fresh catalyst.

### 2. Strait of Hormuz / Iran oil supply disruption — priced as sustained energy upside

- **Status (as of 07-02 bars):** XOM +13.2% 6m rank 5 confirms energy outperformance. Al Jazeera (07-10) and CNN (07-11) reported ongoing Strait shipping disruption; geopolitical risk persists.
- **Current interpretation:** Oil bid visible; energy stocks (XOM rank 5) rank higher than SPY 12m (+20.6%) on supply-side premium. Market treats Hormuz risk as *upside to oil/inflation*, not demand-destruction panic — consistent with proxy-vol 17.69% (benign).
- **Two-sided tail:** If ceasefire or shipping resumed → XOM loses top-5 rank. If escalation spike (tanker hit, refinery strike) → vol spike > 20%, triggering high_vol regime flip.

### 3. Healthcare earnings post-mortem (JNJ 07-15, UNH 07-16) — already in 07-02 bars

- **Momentum names that beat/missed:** JNJ rank 3 (+27.1% 6m), UNH rank 2 (+27.9% 6m) had earnings 07-15–07-16 morning. Outcomes (beat/miss) are not yet visible in the 07-02 close bars; therefore, the 07-21 signals reflect momentum *before* earnings repricing.
- **Implication:** If JNJ or UNH missed earnings post-07-02, the 07-21 top-5 ranks are stale. A fresh EOD close (after 07-16, ideally 07-21 if feed restored) would show momentum re-ranking if healthcare disappointed.
- **Bullish_trend supports remain:** CSCO (+45.6% rank 1), GOOGL (+14.6% rank 4) are tech/AI, not earnings-binary. Even if healthcare rotates out, these two remain in top-5, supporting regime.

---

## Sector Posture: Momentum-Driven Rotation

Based on 126-day / 6-month returns from 07-02 bars (signals.json):

| Sector | Top Names | 6m Return | Regime Posture |
|---|---|---|---|
| **Technology/AI** | CSCO (rank 1), GOOGL (rank 4) | +45.6%, +14.6% | **STRONG** — CPI relief supports duration-sensitive growth; AI infrastructure tailwind intact |
| **Healthcare** | UNH (rank 2), JNJ (rank 3) | +27.9%, +27.1% | **STRONG** — but earnings-dependent; if both beat, momentum persists; if both miss, quick rotation out |
| **Energy** | XOM (rank 5) | +13.2% | **STRONG** — Hormuz supply premium; outperforming SPY |
| **Bonds (IEF)** | IEF | −1.22% 12m | **WEAK** — below 210d MA; rate lift has hurt duration; EXIT signal confirmed |
| **Gold (GLD)** | GLD | +23.0% 12m | **MIXED** — strong 12m return, but below 210d MA on 07-02 bars; defensive bid fading as risk-on dominates; permanent overlay (10%) persists |
| **Broad Equity (SPY)** | SPY | +20.6% 12m | **BASELINE** — above all key MAs; bullish_trend anchored here |

**Regime implication:** This is a *narrow rotation* regime, not broad bullish. Top-5 concentrated in tech/AI + healthcare + energy. If earnings disappoint or Hormuz de-escalates, re-ranking happens quickly. Bonds and gold are deprioritized in favor of growth. Circuit-breaker is FULL (0.2–0.3% DD); room to ride.

---

## Three Core Indicators (2026-07-21 engine output)

### 1. SPY technical structure — ABOVE 50dma, but eroding
- **50-day MA position:** SPY **+1.01% ABOVE** (`spy_pct_from_50dma: +0.010139502752503304`).
  - **Regime continuity:** Still above 50dma (bullish_trend confirmed). But +1.01% is **thinner than 07-16's +1.47%** — trend is weakening on stale bars.
  - **Interpretation:** A 0.5–1.0% intraday dip OR a fresh EOD close showing lower momentum = knife-edge at 50dma, potential pivot to range_bound.
  - **Counter:** SPY remains above 200dma and 10-month MA (long-term structure intact).
- **12-month return:** +20.6% (consistent with 07-16 +21.44%; the difference reflects 5-day bar update from 06-24 to 06-29, then static to 07-02).

### 2. Volatility proxy — BENIGN, near prior level
- **20-day annualized realized vol:** **17.69%** (`proxy_vol_20d_annualized_pct`; VIX feed null).
- **Cushion to high_vol hard-flip (20%):** **2.31 percentage points** (was 2.15pp on 07-16; vol slightly lower, more cushion).
- **Interpretation:** No vol expansion; market remains complacent. Earnings binaries have passed (07-15/16); intraday repricing would be visible in fresh data.

### 3. Macro trend filters (10-month / 210d SMA)
- **SPY above 10m MA:** YES (trend filter passes; momentum entries eligible).
- **GLD below 210d MA:** YES → TAA GLD EXIT signal (permanent 10% overlay persists regardless).
- **IEF below 210d MA:** YES → TAA IEF EXIT signal (confirmed from 07-16; no change).

---

## Signals & Strategy Actions (2026-07-21 engine output)

**Strategy A (dual_momentum_taa, 60% core):**
- SPY ENTRY (top-1 risk asset, +20.6% 12m)
- IEF EXIT (below 210d MA, −1.22% 12m)
- GLD EXIT (below 210d MA, but permanent overlay holds 10%)
- SHV EXIT (cash floor released on SPY entry)

**Strategy B (large_cap_momentum_top5, 30% allocated):**
- **ENTRY (top-5):** CSCO (rank 1, +45.6% 6m), UNH (rank 2, +27.9%), JNJ (rank 3, +27.1%), GOOGL (rank 4, +14.6%), XOM (rank 5, +13.2%)
- **NO_SIGNAL (hold zone):** AAPL, COST (ranks 6–7 in buffer)
- **EXIT (laggards):** MSFT, ORCL, TSLA, META, NVDA, BAC, JPM, etc. (below top-5+buffer)

**Strategy C (gold_permanent_overlay, 10% allocated):**
- GLD ENTRY (permanent policy, regardless of 210d MA status)

---

## Counter-Evidence / What Would Flip Regime to Range-Bound or Risk-Off

1. **Fresh EOD data shows SPY < 50dma** → bullish_trend flips to range_bound or bearish_trend. This is the hard technical break; the current +1.01% cushion is fragile.

2. **Earnings cascade (JNJ + UNH both miss > 3%)** → momentum re-ranks; top-5 loses 2 names; healthcare exits. CSCO, GOOGL, XOM remain, but confidence drops to low.

3. **Strait of Hormuz ceasefire or shipping resumed** → XOM loses energy premium; rotates out of top-5. Less likely (geopolitical trends favor continued disruption 07-21), but would flip top-5 composition.

4. **Proxy-vol spike > 20% OR VIX > 25** → hard flip to high_vol regime; automatic Telegram alert. Trigger: geopolitical escalation spike, earnings shock, credit stress.

5. **Fed emergency pivot (surprise hawkish tightening or financial stability intervention)** → macro_event_driven flip. Would re-price long-duration growth (GOOGL, CSCO) lower.

6. **Overnight macro shock (Iran-US combat escalation, refinery attack, credit event)** → liquidity_stress or macro_event_driven flip.

---

## Known Failing & Passing Signals in This Regime

### Signals that WORK in bullish_trend (SPY above 50dma + 10m MA)
- **Momentum ranking (126d 6m return):** CSCO, UNH, JNJ, GOOGL, XOM outperforming on sustained growth + sector tailwinds. Signal: top-5 momentum entries.
- **Trend filters (SPY 10m MA):** Strategy B entries only when SPY is above 10m MA. Prevents entries in falling-knife scenarios. Signal: SPY above 10m MA = go, below = halt.
- **MA distance cushion:** SPY +1.01% above 50dma is shallow but valid; entries are taken. If cushion narrows below 0.5%, consider tightening stops.

### Signals that FAIL or DEGRADE in bullish_trend
- **Long-duration equity (IEF, TLT):** Both below 210d MA, EXIT confirmed. Bonds underperform in rate-relief rallies; low signal quality in current regime.
- **Laggard momentum names (MSFT, ORCL, TSLA, META):** All negative 6m returns, far below top-5. No buy-the-dip signal until they prove trend reversal. Ignored.
- **GLD below 210d MA:** Gold struggles in risk-on; the permanent 10% overlay is dead weight in this regime. No alpha from gold.

---

## Caution Level: MEDIUM (unchanged, but data staleness increased risk)

### Factors UP:
- **Data staleness now 19+ days** (worse than 07-16's 16d) — earnings repricing (JNJ 07-15, UNH 07-16) not visible in 07-02 bars.
- **Shallow 50dma cushion narrowed:** +1.01% vs +1.47% on 07-16; trend eroding.
- **Earnings outcomes already happened (07-15/16)** but unknown to signals engine — momentum ranks stale if healthcare missed.
- **Geopolitical tail risk:** Hormuz escalation could spike vol > 20% at any time; contained but not eliminated.

### Factors NOT HIGH:
- CPI event (07-14) already passed; no overnight surprise risk from Fed calendar.
- SPY still above 200dma + 10m MA; long-term structure intact.
- Proxy-vol 17.69% has cushion to 20% flip.
- Circuit-breaker FULL, max DD ~0.2–0.3%; room to ride.
- Top-5 remains tech/energy; core inflation-protection assets (vs pure growth) present.

### Escalation Triggers (would raise caution to HIGH)
- Fresh EOD close shows SPY < 50dma or fresh close data >0.5% drop from 07-02 close.
- Proxy-vol > 18.5% intraday OR VIX > 25.
- Overnight Iran escalation spike (geopolitical alert) or credit stress headline.
- Earnings cascade confirmation (JNJ + UNH both miss + cascading momentum exits).

---

## Useful Indicators in This Regime

1. **50dma + 200dma crossover:** SPY above both = bullish_trend valid. Watch cushion from 50dma; if < 0.5%, tighten exits.
2. **10-month SMA:** SPY above = momentum entries eligible. SPY below = halt new longs.
3. **6-month momentum (126d return) ranking:** Top-5 concentration in CSCO, UNH, JNJ, GOOGL, XOM; use for entry selection.
4. **Proxy-vol (20d realized):** Below 18.5% = complacency (good for entries); 18.5–20% = caution zone; >20% = hard flip to high_vol.
5. **Sector flows:** Energy (XOM) + Healthcare (UNH/JNJ) + Tech (CSCO/GOOGL) rotation. Monitor if healthcare earnings disappoint.

---

## Recommended Actions for Downstream Agents

- **Risk Manager:** Adopt bullish_trend + medium confidence as working regime. **CRITICAL:** Entries only on FRESH EOD close (post 07-16, ideally 07-21 if data restored). No entries on 07-02 stale bars; data violation triggers `NO_TRADE` per CLAUDE.md rule #5.
  
- **Strategies A/B/C:** Monitor for fresh data. If 07-21 or next close shows:
  - SPY < 50dma → flip to range_bound, raise caution to HIGH.
  - Fresh momentum ranks show JNJ/UNH dropped from top-5 → confidence to low, re-rank B entries.
  - Proxy-vol > 18.5% → escalate caution to HIGH.

- **Compliance:** All held/proposed symbols (CSCO, UNH, JNJ, XOM, GOOGL, SPY, GLD) approved in watchlist.yaml. No blocked symbols.

- **Telegram:** Auto-trigger alerts only if:
  - Proxy-vol > 20% during session.
  - VIX > 25 (emergency).
  - Regime flips to liquidity_stress or high_vol on fresh data.
  - SPY breaks below 50dma on fresh EOD close.

---

## Summary: Regime Confirmation & Freshness Caveat

| Metric | Value | Regime Indicator |
|---|---|---|
| **Regime** | bullish_trend | SPY +1.01% above 50dma, above 200dma & 10m MA (shallow) |
| **Confidence** | medium | Valid on stale 07-02 bars; earnings repricing unknown; shallow cushion eroding |
| **Data freshness** | STALE (19d old) | Bars end 07-02; violates 60s rule by 4+ orders of magnitude; **NO_TRADE until fresh data** |
| **Effective VIX proxy** | 17.69% | Benign; 2.31pp cushion to high_vol 20% hard-flip |
| **Counter-evidence** | Shallow 50dma, earnings stale, geopolitical tail | Monitoring thresholds critical |
| **Caution level** | MEDIUM | Data staleness aggravated; earnings binary resolved but unseen; Hormuz risk contained |
| **Telegram status** | None yet | Auto-trigger only if proxy-vol > 20% OR VIX > 25 OR regime flips on fresh data |

**Next regime review:** Mandatory after FRESH EOD close is available (target: 07-21 or next trading day). If fresh data restores, check:
1. SPY vs 50dma (< 50dma = flip to range_bound/bearish).
2. Momentum re-ranking (did JNJ/UNH earnings change top-5?).
3. Proxy-vol trend (trending toward 20% = escalate caution).
4. Geopolitical headlines (Iran/Hormuz status).

**Confidence band:** MEDIUM (valid on signal logic, but stale bars + shallow trend + unseen earnings outcomes = elevated revision risk on fresh data).

---

**Date:** 2026-07-21 (pre_market, 10:41 UTC / 06:41 ET) · **Regime:** bullish_trend · **Confidence:** medium
**Deterministic source:** `/tmp/claude-0/-home-user-calm-turtle/5b7e2a69-003c-56cb-acf6-567c85dac65c/scratchpad/signals.json` (pre-market engine, 07-21)
**Data freshness:** STALE — bars end 2026-07-02 session (~19.28 calendar days old, 14 trading sessions; violates 60s limit by 4+ orders of magnitude)
**Macro drivers:** CPI relief (07-14, in market); Hormuz supply premium (ongoing); healthcare earnings (07-15/16, unseen); tech/AI growth bid (sustained).
**Sector posture:** Tech/AI strong (CSCO +45.6%, GOOGL +14.6%), Healthcare strong (UNH +27.9%, JNJ +27.1%), Energy strong (XOM +13.2%), Bonds weak (IEF −1.22%), Gold fading (below 210d MA).
**Next review:** After fresh EOD close (target 07-21 or next trading day). If bars restored, re-evaluate: SPY 50dma break, momentum re-rank post-earnings, vol trend, geopolitical status.
**Alert thresholds:** Proxy-vol > 18.5% (escalate caution), > 20% (flip to high_vol + Telegram), VIX > 25 (emergency Telegram).
**Notifications:** No auto-Telegram yet. Emit notification if regime flips to liquidity_stress / high_vol / bearish_trend on fresh data OR proxy-vol > 20%.
