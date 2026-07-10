# Independent verification — signal-snapshot drift, pre_market 2026-07-10

- **Supersedes/confirms:** `2026-07-10_105205_compliance_reject.md` (REJECTED) and
  `2026-07-10_105205_compliance_reject_resolved.md` (APPROVED, written by a prior
  process in this session before this verification).
- **Purpose:** re-derive the TLT/EXIT-count discrepancy from first principles
  (source code + documented agent invocation pattern) rather than trusting either
  prior verdict on its own word, per operator request.

## What was checked directly

1. **`lib/signals.py:280-359` (`evaluate_large_cap_momentum_top5`)**, read verbatim.
   Universe filter (line 292-295):
   `macro_etfs = set(TAA_RISK_ASSETS + [TAA_CASH_PROXY])` →
   `TAA_RISK_ASSETS=["SPY","IEF","GLD"]`, `TAA_CASH_PROXY="SHV"` →
   `macro_etfs = {SPY, IEF, GLD, SHV}`. Universe = watchlist symbols
   `not in macro_etfs and in bars_by_symbol and != SPY and not is_symbol_blocked`.
   **TLT is not in `macro_etfs` and is not blocked** (only INTU is blocked) →
   TLT is eligible for the momentum universe *whenever its bars are present*.
2. **`git log --oneline -- lib/signals.py`** → exactly one commit
   (`2f4ee9a`) in this file's history. No prior version ever added an
   `approved_for_paper_trading` filter that could have been removed — so a
   universe that excludes TLT was never "the old correct behavior."
3. **`.claude/agents/technical_analysis.md` canonical invocation pattern**
   (a config file this routine may read but not edit) fetches bars for
   `watchlist = [s["symbol"] for s in config.watchlist()["symbols"]]` —
   i.e. **every** watchlist symbol, with no `approved_for_paper_trading`
   pre-filter — then calls `signals.evaluate_all(bars, watchlist, ...)`.
   `prompts/routines/pre_market.md` step 5 uses the identical pattern.
   TLT (`approved_for_research: true`) is in `symbols[]`, so its bars are
   fetched and it lands in `bars_by_symbol`, and per (1) it is therefore a
   legitimate universe member.
4. **`config/strategy_rules.yaml`** has no explicit large-cap universe list —
   the universe is 100% code-derived per (1). No config artifact excludes TLT.
5. Current `data/market/2026-07-10/0640_signals.json` large_cap_momentum_top5
   ranks 1-21 are strictly monotonic in `return_6m` with no gaps/dupes
   (verified programmatically) — internally consistent with a genuine
   `evaluate_all` computation, not a hand-patched table.

## Conclusion

The **JSON version compliance first reviewed (EXIT 16 / 25 rows / 24 symbols /
universe_size 20, no TLT) was the non-canonical artifact** — it could only
have arisen from an incomplete bars fetch (TLT bars missing from
`bars_by_symbol`), which deviates from the documented canonical invocation
pattern in `technical_analysis.md` / `pre_market.md` step 5. The **current
on-disk JSON (EXIT 17 / 26 rows / 25 symbols / universe_size 21, TLT EXIT
rank 13) matches the canonical code path** and is adopted as the single
authoritative snapshot for this routine run. `reports/pre_market/2026-07-10.md`
and `memory/market_regimes/current_regime.md` already cite this version
exactly (verified line-by-line against the JSON: signal_counts, all 21
large-cap ranks/returns, TLT placement).

## Separate, unresolved process concern (do not let the correctness finding paper over this)

`data/market/2026-07-10/0640_signals.json` was **overwritten in place**
between the first compliance review (10:52:05Z) and now — `stat` shows
`Birth: 10:42:59Z`, `Modify: 10:53:57Z` (post-rejection), internal
`generated_at: 10:52:37Z`. The original (non-canonical) bytes were not
preserved under a distinct filename, so this verification could not diff
the two JSONs directly — only reconstruct the first version's shape from
the numbers quoted in the rejection log. `prompts/routines/pre_market.md`
step 5 says "Capture the output" (singular) and does not authorize
in-place mutation of an already-cited snapshot. **Recommendation (for
`self_learning` / `prompts/proposed_updates/`, not enacted here):**
snapshot filenames should be write-once; a re-run after a compliance
rejection should write `<HHMM>_signals_v2.json` (or similar) and the
report should be re-pointed to the new filename, never silently overwrite
the cited file. This time the substance of the correction was verifiable
from source code, but that will not always be true, and an in-place
overwrite of a cited artifact is a bad pattern regardless of whether this
particular instance turned out to be harmless.

## Verdict

Data-integrity concern **resolved on the merits** (TLT inclusion is
correct per current code + documented invocation pattern); artifact set
(report + regime memory + JSON) is internally consistent. Process gap
(in-place overwrite of a cited snapshot) is real and flagged above but
does not block this routine, since it did not corrupt the final numbers
this time. Proceeding to a fresh `compliance_safety` review of the
reconciled artifact set.
