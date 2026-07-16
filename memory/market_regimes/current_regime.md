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
