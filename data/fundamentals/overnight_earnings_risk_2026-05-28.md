# Overnight Earnings Risk Scan — 2026-05-28 Pre-Close

**Date:** 2026-05-28 (Thursday) | **Routine:** `pre_close` (overnight risk overlay)  
**Caution window:** `holding_earnings_caution_window_days = 1` per `config/strategy_rules.yaml`  
**Assessment scope:** Today (2026-05-28 AMC) + Tomorrow (2026-05-29 BMO)

---

## Summary Table

| Symbol | Company / Type | Last Earnings | Next Announced | Within 1-day window? | Risk Level | Action |
|--------|---|---|---|---|---|---|
| CSCO | Cisco Systems | Q3 FY26: 2026-05-13 (reported) | Q4 FY26: TBD (not yet announced) | No | CLEAR | Hold |
| GOOGL | Alphabet Inc. Class A | Q1 2026: ~Apr 2026 (past) | Q2 2026: TBD (not yet announced) | No | CLEAR | Hold |
| UNH | UnitedHealth Group | Q1 2026: ~2026-04-21 (reported) | Q2 2026: TBD (not yet announced) | No | CLEAR | Hold |
| XOM | Exxon Mobil Corp | Q1 2026: ~2026-04-28 (reported) | Q2 2026: 2026-07-31 (announced) | No | CLEAR | Hold |
| GLD | SPDR Gold Shares ETF | N/A (commodity ETF) | N/A (no earnings) | N/A | CLEAR | Hold |

---

## Per-Symbol Detail

### CSCO — Cisco Systems (Technology sector)

**Last earnings reported:** Q3 FY26 on 2026-05-13 (beat: $15.8B revenue, YoY +12%; raised FY26 guidance)  
**Next earnings announced:** Q4 FY26 date **not yet publicly announced**  
**Within 1-day window (2026-05-28/05-29)?** **No**

**Verdict:** **CLEAR**  
- Q3 earnings (May 13) already in the rear-view and reflected in the position (+58.55% momentum, rank 1).
- The 2026-05-27 pre_close journal confirmed "no print in the 1-day window" and the 2026-05-28 midday news scan found no material update.
- No announced Q4 FY26 date available to trigger caution.
- **Action:** No overnight-risk close warranted. Continue to hold.

**Source:** SEC EDGAR filings (08-K filed 2026-05-13), Cisco Investor Relations, CNBC.

---

### GOOGL — Alphabet Inc. Class A (Communication Services sector)

**Last earnings reported:** Q1 2026, reported approx. April 2026  
**Q1 results cited:** Revenue $109.9B (beat $107.2B est.); Cloud +63% YoY  
**Next earnings announced:** Q2 2026 date **not yet publicly announced**  
**Within 1-day window (2026-05-28/05-29)?** **No**

**Verdict:** **CLEAR**  
- Q1 2026 earnings are well in the past (April); the stock has already moved on those results (+34.53% momentum, rank 2).
- The 2026-05-27 pre_close confirmed "Q1 past. No print in window."
- 2026-05-28 midday scan found no breaking news; DOJ search-antitrust remedy (April 8 Choice Screen ruling) is pre-existing, already priced.
- No Q2 2026 date announced yet.
- **Action:** No overnight-risk close warranted. Continue to hold.

**Source:** Google Investor Relations, SEC filings, Yahoo Finance.

---

### UNH — UnitedHealth Group (Health Care sector)

**Last earnings reported:** Q1 2026, reported approx. 2026-04-21; beat: adjusted EPS $7.23 vs $6.57 consensus  
**Guidance raised:** FY26 guidance raised to >$18.25 (from prior)  
**Next earnings announced:** Q2 2026 date **not yet publicly announced**  
**Within 1-day window (2026-05-28/05-29)?** **No**

**Verdict:** **CLEAR**  
- Q1 earnings (April 21) are well past; results were strong (beat, guidance raise) and have been reflected in the position (+22.73% momentum, rank 4).
- 2026-05-27 pre_close confirmed "no imminent print. No print in window."
- 2026-05-28 midday scan noted no fresh catalyst; DOJ Medicare-Advantage probe is pre-existing background (under investigation since July 2025), no new development.
- Berkshire's UNH exit (noted in memory) is a known bear-case factor, already part of the thesis tension.
- **Action:** No overnight-risk close warranted. Continue to hold.

**Source:** UnitedHealth Investor Relations, SEC 8-K, Healthcare Finance News, Yahoo Finance.

---

### XOM — Exxon Mobil Corporation (Energy sector)

**Last earnings reported:** Q1 2026, reported approx. 2026-04-28  
**Next earnings announced:** Q2 2026 / 2Q26 earnings scheduled **2026-07-31** (well outside the 1-day window)  
**Within 1-day window (2026-05-28/05-29)?** **No**

**Verdict:** **CLEAR**  
- Q1 2026 earnings are past; the stock has moved well beyond those results (+29.75% momentum, rank 3).
- 2026-07-31 is 64 calendar days away, 44+ trading days forward — no near-term earnings risk.
- 2026-05-27 pre_close confirmed "next earnings 2026-07-31. No print in window."
- 2026-05-28 midday scan shows constructive analyst update (Mizuho PT $159→$175, Barclays PT $163→$182 on higher 2026/27 oil outlook tied to Iran crisis duration).
- Current weakness (-7.81% vs entry, driven by crude softening on US-Iran de-escalation) is commodity/price-action, not earnings risk.
- **Action:** No overnight-risk close warranted. Continue to hold (monitor XOM's thinnest stop cushion +2.2pp into 05-29 macro data, but earnings risk = None).

**Source:** Exxon Investor Relations, SEC filings, Yahoo Finance energy sector, CNBC.

---

### GLD — SPDR Gold Shares ETF (Commodity ETF)

**Earnings:** N/A (commodity ETF, no earnings)  
**Top holdings (major gold ETF):** holds physical gold bullion, not equity positions with earnings events  
**Overnight risk from top-5 holdings?** See below.

**Verdict:** **CLEAR**  
- GLD is a commodity ETF (10% permanent overlay strategy + TAA top-1). It has no earnings event itself.
- GLD's only relevant risk is changes to spot gold price or macro/rate environment.
- The 2026-05-28 GDP-2 and PCE data (printed 08:30 ET this morning) already affected gold: Core PCE +0.2% m/m (in-line), Q1 GDP +1.6% (weaker than 2.0% expected). Gold drifted lower on the weaker growth + in-line inflation print, now trading spot ~$4,404.
- No ETF-top-holdings earnings within the 1-day window; GLD does not track individual stocks with earnings dates.
- **Action:** No earnings-driven close warranted. Continue to hold (macro hedge through the 05-29 session; GLD expected to track rate expectations and macro data, not earnings).

**Source:** GLD Fund fact sheet (commodity-based), SPDR ETF documentation, Kitco spot gold, BEA macro data.

---

## Consolidated Overnight Risk Verdict

**Positions held:** CSCO, GOOGL, UNH, XOM, GLD (5 total)

| Criteria | Finding |
|---|---|
| **Single-name earnings AMC 2026-05-28?** | None. All last earnings are >1 week past. |
| **Single-name earnings BMO 2026-05-29?** | None. No announced Q2 2026 earnings for any of the 5. |
| **Concentration risk (≥20% per symbol)?** | Not assessed in this sector-aggregate scan (individual stock holdings irrelevant to ETF concentration). GLD concentration check: dual 10% permanent + ~4% TAA = ~14% effective gold weight. Inside policy cap. |
| **Macro overnight event (2026-05-28 session)?** | GDP-2 + PCE deflator + Durable Goods printed 08:30 ET this morning. Already reflected in 2026-05-28 close marks. Non-event for 05-29 (no new macro calendar items scheduled pre-open 05-29). |
| **Whole-book overnight risk from earnings catalysts?** | **NONE.** Zero earnings events for any held name within the 1-day caution window. |

---

## Pre-Close Recommendation

**No positions should be closed on overnight earnings risk.** All five holdings (CSCO, GOOGL, UNH, XOM, GLD) have clear, non-imminent next earnings dates (all >1 month away or N/A for ETF) and no AMC/BMO earnings risk for 2026-05-28/05-29.

**Overnight hold posture:** **NORMAL** (trend-following momentum book; all signals re-confirmed hold; no earnings catalyst to trigger defensive close).

---

## Metadata

**Scan completed:** 2026-05-28 pre_close routine (pre-submission to overnight-risk decision gate)  
**Data sources:**
- `config/strategy_rules.yaml` → `holding_earnings_caution_window_days: 1`
- `journals/daily/2026-05-27.md` → pre_close overnight-risk overlay (2026-05-27T19:35:00Z)
- `journals/daily/2026-05-28.md` → midday news scan + health check
- `memory/symbol_profiles/` → CSCO.md, GOOGL.md, UNH.md, XOM.md, GLD.md (historical earnings dates)
- SEC EDGAR filings & investor relations (Cisco 05-13 8-K, Alphabet, UnitedHealth, Exxon)
- Market data: `data/market/2026-05-28/0630.json` (pre-market bars), live quotes (market_open/midday/pre_close)

**Revision/update frequency:** Ad-hoc on earnings announcements; next routine overnight scan at 2026-05-29 pre_close.
