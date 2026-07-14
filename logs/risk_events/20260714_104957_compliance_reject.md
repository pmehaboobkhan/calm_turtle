# Compliance/Safety Verdict — REJECTED

- **Routine:** pre_market (research-only)
- **Trading date:** 2026-07-14
- **Mode:** PAPER_TRADING
- **Gate:** Final Compliance/Safety (last gate)
- **Verdict:** REJECTED
- **Rejection count within trailing 24h:** 1 (prior compliance_reject was 2026-07-06, outside window — no second-rejection notification / HALT recommendation triggered)

## Scope of what PASSED (safety-critical)
- Mode compatibility: PAPER_TRADING; routine is research-only. NO trade decisions produced — no `decisions/2026-07-14/` directory, no `trades/paper/log.csv` write, no `trades/` git changes. PASS.
- Blocklist: INTU appears only as documentation ("remains blocked / did not appear in any signal"). Not traded, not researched, not proposed as a candidate. PASS.
- Forbidden paths: no writes to `config/*`, `.claude/agents/*.md`, `prompts/routines/*.md`, `trades/live/*`. Only approved write paths touched. PASS.
- Staleness + NO_TRADE posture: 12-trading-day bar staleness (bars through 2026-06-26, >> 60s cap) is prominently disclosed; report and journal both mandate NO_TRADE per CLAUDE.md rule #5 and recommend no action on stale bars. PASS.
- Candidate labeling: all 5 top candidates carry bull thesis, bear thesis, and invalidation, explicitly labeled "candidates only — NO trade decisions today." PASS.

## Reason for REJECTION — Check #4 (numeric provenance / no fabricated numbers presented as deterministic)
The report presents numbers as deterministic engine output that are NOT contained in the committed source-of-truth snapshot `data/market/2026-07-14/0640_signals.json`:

1. **EXIT detail table** ("Today's deterministic signals → EXIT (17)"): per-symbol ranks 8–21 and 6-month returns for 14 symbols (AAPL +3.34% rank 8 ... ORCL -23.92% rank 21) are cited to `signals[]`. The source JSON's `exit_signals` array collapses ALL 17 exits into a single placeholder `{"symbol":"OTHER_SYMBOLS", "note":"17 symbols generated EXIT signals (full list omitted for brevity in this snapshot)"}`. None of these ranks/returns exist in the source of truth. Confirmed: `grep` for AAPL/NVDA/MSFT/ORCL and the specific figures returns NOT FOUND in the JSON; it is the only market-data file for today.
2. **"Notable rotation" narrative:** "NVDA ... rank 10, +1.46%" presented as deterministic — not in the JSON.
3. **Regime memory** (`memory/market_regimes/current_regime.md`) repeats the same untraceable figures (MSFT -23.6%, TSLA -22.0%, META -17.3% as deterministic 6-month returns).
4. **ENTRY "confirmations_passed (verbatim)"** column quotes engine strings ("SPY above 210d MA", "SPY trend filter passed (above 10m MA)", etc.). The JSON `entry_signals` contain only `confidence_inputs` booleans/returns — zero confirmation strings (`grep` count = 0). Labeling these as "verbatim" engine output overstates provenance.

All ENTRY/candidate numbers and all regime numbers DO trace cleanly to the JSON; the defect is confined to EXIT-detail figures, the NVDA rotation stat, and the "verbatim" confirmation strings. Because these are presented in sections explicitly headed "deterministic" and cited to `signals[]`, they violate check #4 ("no fabricated numbers presented as deterministic") and CLAUDE.md ("every data point cites a source"). As the compliance gate, numbers claimed as deterministic that cannot be verified against the deterministic artifact cannot be approved as deterministic.

## Required remedy (documentation-only; no safety-posture change)
Either:
- (a) Regenerate `0640_signals.json` so `exit_signals` contains the full per-symbol list (rank + 126d/6m return) and add the entry `confirmations_passed` strings, so the report traces 1:1; OR
- (b) Relabel the EXIT-detail table, the NVDA rotation stat, and the "verbatim" confirmation strings in the report and in `current_regime.md` as NOT persisted in the snapshot / context-only, removing the "deterministic / signals[]" attribution.

No trade was produced and the NO_TRADE posture is correct, so this is a provenance/traceability defect only — but it must be corrected before commit under "Compliance/Safety always wins."
