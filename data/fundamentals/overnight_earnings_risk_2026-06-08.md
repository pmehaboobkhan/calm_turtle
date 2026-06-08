# Overnight Earnings + Macro Risk Scan — 2026-06-08 Pre-Close

**Date:** 2026-06-08 (Monday) | **Routine:** `pre_close` (overnight-risk overlay)
**Caution window:** `holding_earnings_caution_window_days = 1` per `config/strategy_rules.yaml`
**Assessment scope:** Today (2026-06-08 AMC) + next trading day (2026-06-09 BMO/intraday)
**Open positions:** CSCO, GLD, NVDA, UNH, XOM (5)

---

## Summary Table — single-name earnings

| Symbol | Type | Last Earnings | Next Earnings | Within 1-day window? | Risk | Action |
|--------|------|---------------|---------------|----------------------|------|--------|
| CSCO | Cisco Systems (stock) | Q3 FY26: 2026-05-13 (beat) | ~2026-08-12 (Q4 FY26) | No | CLEAR | Hold |
| GLD | SPDR Gold Shares (commodity ETF) | N/A | N/A (no earnings) | N/A | CLEAR | Hold |
| NVDA | NVIDIA Corp (stock) | Q1 FY27: 2026-05-20 (beat) | 2026-08-26 AMC (confirmed) | No | CLEAR | Hold |
| UNH | UnitedHealth Group (stock) | Q1 2026: ~2026-04-21 (beat) | ~mid-Jul 2026 (Q2) | No | CLEAR | Hold |
| XOM | Exxon Mobil (stock) | Q1 2026: ~2026-04-28 | 2026-07-31 (announced) | No | CLEAR | Hold |

All five positions are individual stocks or a commodity ETF — no ETF top-holding
concentration relay applies (GLD holds physical bullion, no equity constituents
with earnings). Earnings-concentration check therefore N/A across the book.

**Single-name earnings verdict: ZERO held names report within the 2026-06-09
next-trading-day window.** Nearest print is CSCO ~2026-08-12 — over two months out.

---

## Macro overlay — scheduled events for the next session (2026-06-09)

Calendar-A list (the events that trigger a defensive overnight close): FOMC rate
decision, NFP, CPI, GDP, retail sales.

| Event | Scheduled | Distance from tonight | In next-session window? |
|-------|-----------|-----------------------|--------------------------|
| FOMC rate decision | 2026-06-16/17 (two-day) | ~8 trading days | No |
| CPI (May 2026) | **2026-06-10 (Wed)** | **2 trading days** | **No (watch tomorrow)** |
| PPI | 2026-06-11 (Thu) | 3 trading days | No |
| NFP (jobs report) | already past (early June) | — | No |
| GDP / retail sales | none this week | — | No |

**June 9 (tomorrow) itself carries only second-tier releases** — NFIB
small-business optimism, wholesale inventories, routine Treasury auctions —
**none on the calendar-A list.** No scheduled macro catalyst tomorrow rises to
the overnight-close threshold.

**CPI lands 2026-06-10 (Wednesday), two trading days out — OUTSIDE the
next-trading-day window.** It is a flag for *tomorrow's* pre_close run, not
tonight's. Holding through tonight's session does not expose the book to the CPI
binary.

---

## Consolidated overnight-risk verdict

| Criterion | Finding |
|-----------|---------|
| Single-name earnings AMC 2026-06-08? | None — all last prints >2 weeks past. |
| Single-name earnings BMO/intraday 2026-06-09? | None — nearest is CSCO ~2026-08-12. |
| ETF top-holding earnings (≥20% relay)? | N/A — only ETF held is GLD (physical gold, no constituents). |
| Calendar-A macro event 2026-06-09? | **None.** CPI is 06-10 (2 days out); FOMC is 06-16/17. |
| Whole-book overnight catalyst risk? | **NONE within the 1-day caution window.** |

**Overnight hold posture: NORMAL.** No position should be closed on overnight
earnings or scheduled-macro risk for tonight's session.

**Watch for tomorrow's (06-09) pre_close:** the May CPI print on 06-10 enters the
next-trading-day window then. The 06-09 pre_close run should re-evaluate whether
any held name (GLD especially, given its rate/USD sensitivity off record highs)
warrants a pre-CPI defensive trim or close.

---

## Metadata

**Scan completed:** 2026-06-08 pre_close routine.
**Data sources:**
- `config/strategy_rules.yaml` → `holding_earnings_caution_window_days: 1`
- `memory/symbol_profiles/` → CSCO.md, NVDA.md, UNH.md, XOM.md, GLD.md (next-earnings dates)
- `reports/pre_market/2026-06-08.md` → ORCL 06-10 AMC noted (not a holding); no held-name earnings flagged
- Web: NVDA next earnings 2026-08-26 AMC (zacks.com, nasdaq.com/market-activity/stocks/nvda/earnings)
- Web macro calendar: CPI 2026-06-10, PPI 2026-06-11, FOMC 2026-06-16/17 (bls.gov/schedule/news_release/cpi.htm; federalreserve.gov/monetarypolicy/fomccalendars.htm; tradingeconomics.com/united-states/calendar)
