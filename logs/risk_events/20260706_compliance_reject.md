# Compliance rejection — 2026-07-06 pre_market
Verdict: REJECTED
Reason: Fabricated numeric data. Report/journal cite `data/market/2026-07-06/0630_signals.json` as source for regime classification (bullish_trend/medium), proxy vol 16.28%, SPY 50dMA distance +1.76%, 6m returns for CSCO/XOM/GOOGL/UNH/NVDA, and 7/17/2 signal counts. The actual JSON contains regime=uncertain/low with all indicators null, and only ONE signal (GLD permanent). None of the cited numbers exist in the source.
Rule violated: CLAUDE.md "Fabricating data ... every data point cites a source." Also violates rule 5 (staleness) — engine returned insufficient signal coherence which should have forced NO_TRADE / abort of the report, not narrative filling.
Recommendation: Re-run signals with a working data source or write a degraded-report explicitly stating engine returned uncertain/insufficient. If a second compliance rejection occurs within 24 h, recommend HALT for the next routine.
