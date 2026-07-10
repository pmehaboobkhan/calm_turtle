# RESOLVED — supersedes 2026-07-10_105205_compliance_reject.md

- **Original verdict:** REJECTED (pre_market 2026-07-10) on apparent fabrication: report/regime claimed 17 EXIT / 26 rows / TLT EXIT / MSFT rank 21, while `0640_signals.json` showed 16 EXIT / 25 rows / no TLT / universe_size 20.
- **New verdict:** APPROVED. Root cause was inverted.

## What actually happened
The JSON I first reviewed was a **non-canonical** artifact: the market_data specialist pre-filtered the momentum universe by `approved_for_paper_trading`, dropping TLT (giving universe_size 20). The **report and regime file were already canonical.**

Ground truth (verified directly in source, not on peer assertion):
- `lib/signals.py:292` — `macro_etfs = set(TAA_RISK_ASSETS + [TAA_CASH_PROXY])`. Confirmed constants: `TAA_RISK_ASSETS=['SPY','IEF','GLD']`, `TAA_CASH_PROXY='SHV'` → `{SPY,IEF,GLD,SHV}`. **TLT is NOT a macro ETF here.**
- `lib/signals.py:293-295` — momentum universe = watchlist symbols `not in macro_etfs`, has bars, `!= SPY`, `not is_symbol_blocked`. TLT satisfies all → **TLT is a legitimate momentum-universe member (size 21)** and emits an EXIT at its return rank.
- `is_symbol_blocked('TLT') == False` (only INTU blocked).
- TLT 126d return -0.09% sits between AMZN (+3.02%, r12) and HD (-0.66%, r14) → **rank 13**, shifting HD..MSFT to 14..21. Internally consistent; all other symbols' returns unchanged.

## Regenerated canonical JSON (data/market/2026-07-10/0640_signals.json, an allowed write path)
`signal_counts {ENTRY:7, EXIT:17, NO_SIGNAL:2, rows:26, distinct:25}`, `large_cap_universe_size:21`, TLT EXIT rank 13. Report line 38/57 and regime line 58 now match exactly.

## Harm assessment
TLT EXIT is harmless: TLT is `approved_for_paper_trading:false` (never openable), it is an EXIT not an ENTRY, no TLT position is held, and this routine is research-only with zero positions opened.

## All other PASS checks re-confirmed post-remediation
No `decisions/2026-07-10/`; no 2026-07-10 rows in `trades/paper/log.csv` (last row 2026-07-01); no position content change; INTU only in blocklist-honoring footers; staleness disclosed; no writes to `config/`/`.claude/agents/`/`prompts/routines/`/`trades/live/`; no risk limit raised; mode PAPER_TRADING.

**Lesson for the routine:** specialists must emit the CANONICAL engine universe (do not pre-filter by tradability before ranking) — pre-filtering changed ranks and counts and produced a false fabrication signature.
