# Proposed update — Weekly review: add Markov regime diagnostic block

**Date proposed:** 2026-05-21
**Proposer:** automated session (operator-approved)
**Target file (PR-only):** `prompts/routines/weekly_review.md`
**Type:** routine prompt addition (one new sub-step under §6)

---

## Why

Evaluated the `markov-hedge-fund-method` skill against the four ETFs that drive
Strategy A (60%) + Strategy C (10%) on 2026-05-21. Walk-forward Sharpe on SPY
was 0.245 (below the 0.8 portfolio target); IEF ~0, GLD negative; SHV
degenerate. The method is **NOT** suitable as a trade signal.

It IS useful as a **weekly diagnostic** because the transition matrix gives
information the existing 10-month SMA filter doesn't:

- Persistence numbers (e.g. SPY Bull→Bull ~89% historically) give a numeric
  threshold for "the regime is acting normally."
- Stationary Bear share is a calibration point for the regime-diversity gate
  (`config/risk_limits.yaml > gates.regime_diversity_gates`).
- A 3-state probabilistic view orthogonal to the binary trend filter.

Cost: one `lib.data.get_bars("SPY", limit=520)` call + ~5 ms of pure-Python
compute. No new dependencies.

## What to add

In `prompts/routines/weekly_review.md`, append one bullet to step 6 (the
journal-write step):

```diff
 6. Write `journals/weekly/<YYYY-WW>.md` and `reports/learning/weekly_learning_review_<date>.md` per the §21N template.
+   - Append the SPY Markov regime diagnostic block via:
+     `python3 scripts/weekly_regime_snapshot.py --symbol SPY >> journals/weekly/<YYYY-WW>.md`
+     This is a diagnostic, NOT a trading signal. Flag in the journal if SPY
+     Bull→Bull persistence drops below ~80% or stationary Bear share rises
+     above ~25% — corroborate against the 10-month SMA filter.
```

## Files already landed (this proposal only asks for the routine line)

- `lib/regime_markov.py` — pure-compute module (no I/O, no numpy)
- `scripts/weekly_regime_snapshot.py` — CLI that fetches SPY and prints markdown
- `tests/test_regime_markov.py` — unit tests for the pure-compute layer

## Reviewer checklist

- [ ] Confirm `scripts/weekly_regime_snapshot.py --symbol SPY` runs locally and
      emits the expected markdown block.
- [ ] Confirm `tests/test_regime_markov.py` passes.
- [ ] Confirm the diagnostic stays in the journal-write step, not the
      decision-making step. It must never feed `lib.signals` or position sizing
      without a separate PR that includes paper-only test results.
- [ ] Confirm the script uses `lib.data.get_bars` (existing yfinance/Alpaca
      routing) — no new external data dependency.

## Recurring-rejection silence

If this is rejected, do not re-propose for 30 days. Earliest re-propose date:
2026-06-20.
