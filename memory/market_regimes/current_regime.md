# Current Market Regime — 2026-07-10 (pre-market)

## Regime Classification (Deterministic Engine)
- **Regime:** bullish_trend
- **Confidence:** medium
- **Deterministic source:** `data/market/2026-07-10/0640_signals.json` (`lib.signals.detect_regime`, `bar_source: alpaca_iex_fallback`)
- **Called by:** `pre_market` routine (regime adoption + macro/sector narrative overlay)

> All numeric indicator values below are quoted verbatim from today's `0640_signals.json`.
> External/news claims cite their source inline. Intraday prices and live P&L are **not** stated —
> the daily-bar feed is stale (see below), so they cannot be computed authoritatively pre-market.

---

## CRITICAL CAVEAT: Data staleness + razor-thin margin

**Underlying daily bars end `2026-06-24T04:00:00Z` (2026-06-23 session close, SPY 733.32).** As of 07-10 pre-market that is **~16 calendar days / ~11–12 trading sessions stale**.

- `risk_limits.data.max_data_staleness_seconds = 60`; actual ≈ **1,406,691 s**. **VIOLATED** by ~5 orders of magnitude.
- Primary feed (yfinance) is TLS-reset through the agent proxy — the recurring "feed down" condition every session since ~06-25. Only the Alpaca IEX fallback returns data, and it lags 6–19 days.
- **Per CLAUDE.md rule #5:** any trade on stale data → `NO_TRADE`. If the feed is still stale at EOD, all new entries are forced to `HOLD-ALL` (as on 07-02/03/07/08/09).

**Implication:** the trend read is technically intact on the stale data but *operationally fragile*. Fetch FRESH bars first at EOD; treat overnight gap risk as high.

---

## Three core indicators (today's engine output)

### 1. SPY technical structure
- **Above 50-day MA:** YES, but by only **+0.052%** (`spy_pct_from_50dma: 0.0005226`) — **razor-thin.**
- **Above 200-day MA:** YES (structural support intact).
- **12-month total return:** **+22.20%** vs cash (SHV) **−0.05%** (Strategy-A `confidence_inputs`).
- A ~0.5% gap down would break the 50dma read.

### 2. Volatility proxy (no VIX feed)
- **20-day annualized realized vol:** **16.65%** (`proxy_vol_20d_annualized_pct`; `vix: null` → proxy used as `effective_vix_used`).
- Cushion to the 20% `high_vol` hard-flip: **~3.35pp**.
- External corroboration: VIX quoted **16.79** ([CNBC](https://www.cnbc.com/quotes/.VIX), 07-09) — consistent, no panic.

### 3. Macro trend filters (10-month / 210d SMA)
- **SPY above 10m MA:** YES (Strategy-B trend filter passes).
- **GLD below 210d MA:** yes → `dual_momentum_taa` EXIT for GLD (permanent overlay still holds the 10% sleeve).
- **IEF below 210d MA:** yes; 12m return −0.20% ≤ cash → EXIT.

---

## Momentum snapshot — today's engine (126-day / 6m return, rank)

| Rank | Symbol | 6m return | Signal | Note |
|---|---|---|---|---|
| 1 | CSCO | **+52.70%** | ENTRY (B) | AI-infrastructure / networking-refresh narrative |
| 2 | UNH | **+23.99%** | ENTRY (B) | Healthcare; earnings 07-16 |
| 3 | XOM | **+17.34%** | ENTRY (B) | Energy; US–Iran oil bid |
| 4 | JNJ | **+16.74%** | ENTRY (B) | Pharma; earnings 07-15 |
| 5 | GOOGL | **+12.39%** | ENTRY (B) | Cloud; thinnest margin (one slip → buffer) |
| 6–7 | NVDA, COST | (buffer) | NO_SIGNAL | rank 6–7 top-N+2 buffer — neither entry nor exit |

**Laggards (EXIT, not in top-5):** AAPL (8, +7.10%), JPM (9, +5.18%), BAC (10, +4.54%), WMT (11, +4.02%), AMZN (12, +3.02%), HD (14, −0.66%), PFE (15, −4.53%), V (16, −4.78%), MA (17, −13.57%), META (18, −15.33%), ORCL (19, −18.06%), TSLA (20, −21.97%), MSFT (21, −24.75%), plus TLT.

**Note vs prior file:** GOOGL re-entered the top-5 at rank 5 and NVDA fell to the rank-6 buffer — the reverse of the 07-09 snapshot. This is the authoritative ordering for 07-10.

---

## Sector posture

- **Healthcare leadership:** UNH (2) + JNJ (4) both top-5 — defensive names rising in momentum is a "risk-on without conviction" / late-cycle caution signal, not a regime flip.
- **Energy sustained:** XOM (3) on the commodity + US–Iran geopolitical bid.
- **AI/networking exceptional:** CSCO (1) at +52.70%.
- **Mega-cap growth weak:** MSFT/TSLA/ORCL/META all rank 18–21.

---

## Macro & geopolitical context (news_sentiment 2026-07-10, cited)

- **FOMC:** held 2026-06-17 at 3.5–3.75%, hawkish tilt; year-end 2026 dot ~3.8% (≥1 hike implied); PCE raised to 3.6% ([Federal Reserve](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm); [CNBC](https://www.cnbc.com/2026/06/17/fed-interest-rate-decision-june-2026.html)).
- **US–Iran conflict:** airstrike exchange; oil ~$80–82/bbl; Strait of Hormuz risk (~20% of global oil), partly offset by reported negotiation hopes ([Al Jazeera](https://www.aljazeera.com/); [EIA](https://www.eia.gov/outlooks/steo/)). Two-sided risk for XOM; possible vol catalyst.
- **VIX benign:** 16.79 ([CNBC](https://www.cnbc.com/quotes/.VIX)).

---

## Counter-evidence / what would flip the regime

1. **SPY closes below 50dma** (margin only +0.052%) → trend break to bearish/uncertain.
2. **Proxy-vol > 20%** → hard flip to high_vol (currently ~3.35pp away).
3. **Overnight macro shock** (Fed follow-through, Iran military escalation, credit stress) → same-day flip.
4. **Earnings miss on JNJ (07-15) / UNH (07-16)** → rotation stop-loss risk on held names.
5. **GLD cascade through 200dma** → early warning of hedging failure.

---

## Strategy posture (today's signals)

- **Strategy A (dual_momentum_taa, 60%):** SPY ENTRY; IEF/GLD/SHV EXIT. Full risk-on; no bond/gold diversifier seat via A.
- **Strategy B (large_cap_momentum_top5, 30%):** trend filter passing. Top-5 ENTRY = CSCO, UNH, XOM, JNJ, GOOGL. Held (GOOGL, JNJ, UNH) re-confirm; CSCO + XOM are the only *new* names. Broad EXITs on laggards.
- **Strategy C (gold_permanent_overlay, 10%):** ENTRY (permanent policy) — governs the 10% GLD sleeve despite the A-leg EXIT. Standing conflict, resolved by policy.

---

## Caution level: MEDIUM-HIGH

**Up:** margin above 50dma razor-thin (+0.052%); vol 16.65% (~3.35pp to high_vol); 11–12-day-stale data; defensive sector leadership; US–Iran oil risk; earnings cluster (JNJ 07-15, UNH 07-16, GOOGL 07-22).
**Not yet HIGH:** SPY above 200dma; Strategy-B trend filter passing; no circuit-breaker event (CB state FULL, DD ~0.25%); healthcare/energy constructive.
**Escalation → HIGH / flip:** SPY < 50dma; proxy-vol > 18%; overnight macro shock; first earnings miss on JNJ/UNH.

---

## Recommended posture for downstream agents

- **Risk Manager:** treat bullish_trend as valid *on the data*, subject to reversal risk; the dominant risk is data staleness — do not act on stale bars. If fresh data at EOD shows SPY < 50dma, rotate to SHV.
- **Strategies A/B/C:** no forcing entries onto stale data; entries are an EOD decision against a fresh close only. Consider de-risking JNJ (near take-profit, earnings 07-15) at EOD if data is fresh.
- **Compliance:** no blocked symbols in any signal; no margin/options/short/leverage. INTU neither researched nor signalled.

---

**Date:** 2026-07-10 (pre-market) · **Regime:** bullish_trend · **Confidence:** medium
**Deterministic source:** `data/market/2026-07-10/0640_signals.json`
**Data freshness:** STALE — bars end 2026-06-23 session (~11–12 trading days; violates 60s limit, CLAUDE.md rule #5)
**Next review:** 2026-07-10 EOD (fetch fresh bars first). Escalate if SPY < 50dma or proxy-vol > 18%.
