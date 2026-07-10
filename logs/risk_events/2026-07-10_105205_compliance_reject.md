# Compliance/Safety REJECTION — pre_market 2026-07-10

- **Gate:** Compliance & Safety (final gate, pre-commit)
- **Routine:** `pre_market` · **Trading date:** 2026-07-10 · **Mode:** `PAPER_TRADING`
- **Verdict:** REJECTED — routine must HALT (no commit) until artifacts are corrected.
- **Authoritative source:** `data/market/2026-07-10/0640_signals.json` (`lib.signals.evaluate_all`, `bar_source: alpaca_iex_fallback`).

## Reason: fabricated signal data cited to the deterministic engine (CLAUDE.md no-fabrication rule; check #3 traceability)

The pre-market report and the regime memory file state a **TLT `large_cap_momentum_top5` EXIT signal and an inflated EXIT count / rank set that do NOT exist in `0640_signals.json`.** Numbers are cited to the JSON but are not in it.

Authoritative JSON (verified):
- `signal_counts`: ENTRY 7, EXIT **16**, NO_SIGNAL 2, total **25**; array confirms 25 rows across **24 distinct symbols**.
- **TLT is not present in the signals array at all** (TLT is `approved_for_paper_trading: false` and outside the Strategy-B large-cap universe; `universe_size: 20`).
- JSON Strategy-B ranks: HD 13, PFE 14, V 15, MA 16, META 17, ORCL 18, TSLA 19, MSFT 20.

Artifact claims (do not trace to JSON):
- `reports/pre_market/2026-07-10.md:38` — "**7 ENTRY · 17 EXIT · 2 NO_SIGNAL** (26 signal rows across 25 symbols)". JSON = 16 EXIT / 25 rows / 24 symbols.
- `reports/pre_market/2026-07-10.md:57` — lists **"TLT"** as a Strategy-B EXIT and shifts 8 ranks +1: MSFT 21, META 18, TSLA 20, V 16, MA 17, PFE 15, HD 14, ORCL 19 (JSON: 20/17/19/15/16/14/13/18). Rank 21 exceeds `universe_size: 20`.
- `memory/market_regimes/current_regime.md:58` — same phantom "plus TLT" and the same 8 shifted ranks, written into the regime file this run (consumed by downstream agents).

This is fabricated engine output propagated into both the primary report and the operational regime memory. The journal's "What worked" claims the macro_sector agent's stale/fabricated numbers were caught and `current_regime.md` corrected; the correction was **incomplete** — the phantom TLT and +1 rank shift survived into the committed artifacts.

## Required remediation before re-submit
1. Correct report line 38 to **7 ENTRY / 16 EXIT / 2 NO_SIGNAL (25 rows / 24 symbols)**.
2. Remove the phantom **TLT** EXIT from report line 57 and regime line 58.
3. Restore Strategy-B ranks to the JSON values (HD 13, PFE 14, V 15, MA 16, META 17, ORCL 18, TSLA 19, MSFT 20).
4. Re-run the Compliance gate on the corrected artifacts.

## Checks that PASSED (for the record)
- No trade decisions produced: no `decisions/2026-07-10/` dir; no new rows in `trades/paper/log.csv` (last row 2026-07-01); no position content change. Research-only respected.
- No blocked symbol as a target: **INTU** appears only in blocklist-honoring footers (report:141, regime:111) — allowed documentation reference.
- Data staleness disclosed prominently (bars end 2026-06-23 session; ~1.4M s >> 60s limit); zero positions opened.
- No writes to forbidden paths (`config/`, `.claude/agents/`, `prompts/routines/`, `trades/live/`); no risk limit raised.
- Mode `PAPER_TRADING` (memory writes permitted).
- Verified-correct numerics: regime bullish_trend/medium; spy_pct_from_50dma +0.052%; proxy_vol 16.65%; top-5 CSCO/UNH/XOM/JNJ/GOOGL with returns +52.70/+23.99/+17.34/+16.74/+12.39%; SPY 12m +22.20%.

*Compliance/Safety always wins. Fabrication cited to the deterministic source is non-negotiable regardless of mode or trade impact.*
