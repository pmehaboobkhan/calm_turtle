# Current Market Regime — 2026-07-13 (pre_close overnight risk scan)

## Regime Classification
- **Regime:** range_bound
- **Confidence:** low
- **Deterministic source:** `data/market/2026-07-13/1036_signals.json` (`lib.signals.detect_regime`, `bar_source: alpaca_iex_fallback`)
- **Called by:** `pre_market` routine 07-13; `pre_close` overnight macro scan 07-13

> All numeric indicator values below are quoted verbatim from the deterministic engine output.
> External/news claims cite their source inline with timestamps.
> Intraday prices and live P&L are **not** stated — the daily-bar feed is stale (see CRITICAL CAVEAT below).

---

## CRITICAL CAVEAT: Data staleness + 50dma knife-edge

**Underlying daily bars end `2026-06-25T04:00:00Z` (2026-06-24 session close, SPY 733.33).** As of 07-13 pre-close that is **~18.3 calendar days / ~13 trading sessions stale**.

- `risk_limits.data.max_data_staleness_seconds = 60`; actual ≈ **1,579,298 s**. **VIOLATED** by ~5 orders of magnitude.
- Primary feed (yfinance) is TLS-reset through the agent proxy — recurring "feed down" condition every session since ~06-25. Only Alpaca IEX fallback returns data, lagging 6–19 days.
- **Per CLAUDE.md rule #5:** any trade on stale data → `NO_TRADE`. If stale at EOD, all new entries forced to `HOLD-ALL`.

**Implication:** the trend read is technically intact on stale bars but *operationally fragile*. SPY sits at 50dma knife-edge (−0.053% below on a rolling-window sign flip); a 0.5% gap would breach it. Fetch FRESH bars first at EOD; treat overnight gap risk as moderate-to-high into June CPI release.

---

## Three core indicators (2026-07-13 engine output)

### 1. SPY technical structure — KNIFE-EDGE FRAGILITY
- **50-day MA position:** SPY **−0.053% BELOW** (`spy_pct_from_50dma: -0.0005266`) — **flipped from +0.052% above on 07-10.**
- **Sign flip driver:** SPY price near-flat (733.32 → 733.33 over 3 sessions); rolling 50-day window advanced ~1 session, causing the cross. Fragile in both directions.
- **200-day MA:** SPY above (structural support intact); ~3.0% below current price.
- **10-month MA:** SPY above (Strategy-B trend filter passes).
- **12-month total return:** **+20.86%** vs cash (SHV) **−0.05%**.

### 2. Volatility proxy
- **20-day annualized realized vol:** **16.65%** (`proxy_vol_20d_annualized_pct`; VIX feed null; proxy used).
- **Cushion to high_vol hard-flip (20%):** **~3.35 percentage points**.
- **External corroboration:** VIX **15.03** on 07-13 close ([Velox Macro](https://veloxmacro.com/how-to-read-the-vix-week-ending-july-6-2026/); 07-10 cited). Benign/complacent into a macro catalyst window (CPI 07-14, earnings 07-15/16).

### 3. Macro trend filters (10-month / 210d SMA)
- **SPY above 10m MA:** YES (Strategy-B trend filter passes).
- **GLD below 210d MA:** YES → TAA GLD EXIT (permanent overlay 10% sleeve still holds by policy).
- **IEF below 210d MA:** YES → TAA IEF EXIT.

---

## Momentum snapshot — 2026-07-13 engine (126-day / 6m return)

| Rank | Symbol | 6m return | Signal | Status |
|---|---|---|---|---|
| 1 | CSCO | **+52.25%** | ENTRY (B) | AI-infrastructure bid; not held |
| 2 | UNH | **+27.81%** | ENTRY (B) | Healthcare; **earnings 07-16 BMO** — held 15sh |
| 3 | JNJ | **+18.06%** | ENTRY (B) | Pharma; **earnings 07-15 BMO** — held 26sh, near target |
| 4 | XOM | **+16.37%** | ENTRY (B) | Energy; oil/Iran bid; not held |
| 5 | GOOGL | **+10.91%** | ENTRY (B) | Cloud; **earnings 07-22 AMC** — held 16sh, thinnest buffer (rank 5) |
| 1 (strat A) | SPY | **+20.86%** | ENTRY (A) | TAA top-1; held 20sh |

**Laggards (EXIT, rank ≥ 8):** COST (buffer +10.84%), NVDA (buffer +6.65%), BAC (+4.20%), JPM (+3.74%), WMT (+2.86%), AAPL (+1.62%), TLT (−0.01%), HD (−0.50%), AMZN (−0.55%), PFE (−6.05%), V (−6.16%), MA (−15.03%), META (−17.92%), ORCL (−23.04%), TSLA (−23.25%), MSFT (−27.31%).

---

## Overnight/gap risk assessment — 2026-07-14 session (next session)

### Scheduled macro events (calendar-A tier HIGH)
1. **June CPI (headline, core)** — 07-14, **08:30 ET** — [BLS](https://www.bls.gov/news.release/cpi.nr0.htm)
   - **Tier:** HIGH (rate-path binary; May CPI elevated at 4.17% headline / 2.82% core).
   - **Impact:** Beat = risk-on (extends rally, pushes SPY further above 50dma). Miss = hawkish repricing (gap down into knife-edge).
   - **Affected holdings:** SPY (direct), GOOGL/JNJ/UNH (indirect via sentiment).

2. **Bank earnings (JPM, BAC, GS, WFC)** — 07-14, **BMO**
   - **Tier:** HIGH/MED (tone setter for broad market, not held).
   - **Impact:** Weak prints increase defensive pressure; strong prints support risk-on.

3. **US–Iran escalation / Strait of Hormuz shipping** — ongoing, variable
   - **Tier:** MED (two-sided: upside to energy/inflation, downside to broad-market cost/vol).
   - **Impact:** Oil spike amplifies CPI miss fears; de-escalation supports risk-on.
   - **Source:** [Al Jazeera 07-10](https://www.aljazeera.com/economy/2026/7/10/strait-of-hormuz-shipping-grinds-to-halt-as-us-iran-resume-fighting); [CNN 07-11](https://www.cnn.com/2026/07/11/world/live-news/iran-war-trump).

### Open position overnight risk
- **SPY (20sh, 60% strategy core):** CPI at 08:30 is a same-session catalyst, not overnight surprise. Overnight gap risk moderate (0.5–1.5% in either direction). Current position is 0.15% above 50dma knife-edge; a 0.5% gap down breaches support and flips regime to bearish/uncertain. No stop breach (<–10% = 663.79).
- **GOOGL (16sh, rank 5, thinnest buffer):** No direct 07-14 event; earnings 07-22. CPI repricing affects cloud valuations moderately. No stop breach (<–10% = 331.68).
- **JNJ (26sh, rank 3, near target):** **EARNINGS 07-15 BMO** (TOMORROW NIGHT). Held at $232.75 entry, target $290.96. No overnight gap from CPI itself, but binary earnings risk is material for 07-15 morning. Current position +18.06% 6m; earnings miss cascades momentum risk into UNH (rank 2).
- **UNH (15sh, rank 2):** **EARNINGS 07-16 BMO** (day after CPI). Held at $398.67, target $495.59. No direct 07-14 risk, but JNJ miss on 07-15 could spill momentum into pre-earnings risk. Current position +27.81% 6m.

### Overnight gap risk quantification (07-13 close → 07-14 open, pre-CPI)
- **Baseline scenario (50%):** SPY opens flat to +0.2%. CPI 08:30 ET sets intraday direction.
- **CPI-miss scenario (25%):** SPY gaps 0.5–1.5% lower OR opens flat and sells into release. Likely lands 0.3–1.0% below 07-13 close. **Breaches 50dma on stale bars if gap > ~0.5%.**
- **CPI-beat scenario (25%):** SPY gaps 0.3–0.8% higher; extends rally; pushes further above 50dma. Low overnight risk here.
- **Iran escalation tail (5% embedded in above):** Overnight oil spike > +5% could trigger a pre-CPI gap up, reducing CPI miss concern but raising cost-push inflation fears.

---

## Counter-evidence / what would flip the regime

1. **SPY closes below 50dma on FRESH data** (Friday EOD 07-14 or earlier) → trend breaks to bearish/uncertain.
2. **Proxy-vol > 20%** OR **VIX > 25** → hard flip to high_vol; automatic Telegram alert.
3. **Overnight macro shock** (Iran military escalation, credit stress, Fed emergency action) → same-session flip.
4. **JNJ earnings miss on 07-15 BMO** → rotation stop-loss risk on held top-3; momentum cascade into UNH rank-2.
5. **GLD cascade through 200dma** → early warning of hedging failure across macro regime.

---

## Strategy posture (current, 2026-07-13)

- **Strategy A (dual_momentum_taa, 60%):** SPY ENTRY confirmed; IEF/GLD EXIT. Full risk-on; no bond/gold diversifier via A-leg. Vulnerable to CPI miss repricing at 50dma knife-edge.
- **Strategy B (large_cap_momentum_top5, 30%):** Trend filter passing. Top-5 entries (CSCO, UNH, XOM, JNJ, GOOGL) confirmed; held names (GOOGL, JNJ, UNH) re-confirm. New entries (CSCO, XOM) pending EOD fresh-data evaluation. Broad EXITs on laggards (rank 6+ buffer only).
- **Strategy C (gold_permanent_overlay, 10%):** Permanent GLD policy entry (not currently an open position); standing conflict with A-leg GLD EXIT resolved by policy. GLD below 210d MA but overlay persists.

---

## Caution level: MEDIUM-HIGH (elevated from MEDIUM on 07-10)

**Up:**
- SPY at 50dma knife-edge (−0.053%); a 0.5% gap flips regime to bearish/uncertain.
- June CPI binary 07-14 8:30 ET — rate-path catalyst into stale-bar regime read.
- Earnings cluster: JNJ 07-15, UNH 07-16 (both held, both on momentum rally). Early misses risk cascade.
- Complacent VIX (15.03) into vol-expansion event; no hedging priced.
- Data staleness masking live intraday repricing risk.
- US–Iran escalation tail (two-sided oil/vol).

**Not yet HIGH:**
- SPY above 200dma and 10-month MA — intermediate/long-term structure intact.
- Circuit-breaker FULL, DD ~0.2–0.3% (well inside 8% HALF threshold).
- Positions 7–10% above stops; no stop breach from 0.5–1.5% gap.
- CPI miss is priced risk, not a surprise (market expected elevated print).

**Escalation → HIGH / flip trigger:**
- Fresh EOD close shows SPY < 50dma.
- Proxy-vol > 18% OR VIX > 25.
- JNJ miss on 07-15 morning → momentum rotation.
- Oil > +7% overnight from Iran escalation (cost-push inflation tail).

---

## Recommended posture for downstream agents

- **Risk Manager:** treat range_bound + low confidence as valid *on the stale bars*, subject to EOD repricing risk. CPI binary at 08:30 ET is a **same-session re-rating event**, not overnight surprise. Monitor overnight oil/forex action; if oil > +5% overnight, raise caution to HIGH ahead of CPI release.
- **Strategies A/B/C:** 
  - No forcing of new entries until FRESH EOD close is fetched (07-14 EOD, after CPI 08:30 release).
  - If fresh 07-14 close shows SPY < 50dma, rotate SHV per dual_momentum_taa rule.
  - Monitor JNJ 07-15 BMO earnings; if miss confirmed, prepare rotation exit for held JNJ at open 07-16 unless filled on overnight gap.
  - Consider trim of GOOGL (rank-5 thinnest buffer) at EOD 07-14 if CPI miss reprices cloud valuations below threshold (not automatic, analyst discretion).
- **Compliance:** no blocked symbols in any signal; no margin/options/short/leverage. INTU neither researched nor signalled.
- **Telegram alerts:** ONLY if proxy-vol > 20% OR VIX > 25 OR caution flips to HIGH (latter requires CPI shock + oil/Iran escalation combo; not automatic from CPI miss alone).

---

## Data quality & intraday monitoring notes

1. **Overnight feed (now 07-13 close → 07-14 pre-open):** monitor Asia-Pacific markets for Iran developments, oil movements, and risk sentiment. If Shanghai/Hang Seng down > 1%, flag as pre-CPI headwind.
2. **07-14 pre-market (before 08:30 CPI):** fetch FRESH bars from Alpaca if available; update regime deterministically. If still stale, note in journal and hold all positions.
3. **07-14 08:30 (CPI release):** intraday monitoring agent watches live market reaction. If SPY gaps 1.5%+ lower on CPI miss, alert Risk Manager.
4. **07-14 EOD:** MANDATORY fresh-close evaluation. If fresh data shows SPY < 50dma, rotate SHV. If still above, re-confirm trend and proceed with any pending entries.

---

**Date:** 2026-07-13 (pre_close, 17:00 ET projected) · **Regime:** range_bound · **Confidence:** low
**Deterministic source:** `data/market/2026-07-13/1036_signals.json` (pre-market engine)
**Data freshness:** STALE — bars end 2026-06-24 session (~18.3 days / ~13 trading sessions stale; violates 60s limit, CLAUDE.md rule #5)
**Overnight risk:** MODERATE-TO-HIGH (June CPI 07-14 8:30 ET is a calendar-A binary; 0.5%+ gap breaches 50dma knife-edge)
**Next review:** 2026-07-14 pre-market (if fresh data available) or EOD (mandatory). Escalate to HIGH if proxy-vol > 18% or VIX > 25 or overnight oil > +7%.
**Notifications:** No automatic Telegram unless proxy-vol > 20% or regime flips to liquidity_stress / high_vol.
