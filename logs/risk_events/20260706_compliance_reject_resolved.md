# Compliance rejection — 2026-07-06 pre_market — RESOLVED / SUPERSEDED

Companion to: `logs/risk_events/20260706_compliance_reject.md`
Resolution timestamp: 2026-07-06 (post 10:53 UTC signals regeneration)
New verdict: APPROVED

## Root cause of the earlier rejection

The prior compliance verdict fired because, at the moment I read
`data/market/2026-07-06/0630_signals.json`, the file contained a
regime=`uncertain`/low, all-null indicators, and only one signal
(GLD permanent) — none of which matched the numbers cited in the
report/journal.

That JSON did NOT represent what the report author actually ran.
A lingering yfinance-path background job (the deterministic engine
with `BAR_SOURCE` defaulted to yfinance, which is TLS-blocked
through the proxy per 06-30 → 07-03 notes) had *overwritten* the
good Alpaca-sourced JSON after the report was drafted. The report's
citations were faithful to the engine output at draft time; the
on-disk artifact had been silently clobbered by a zombie job.

## Remediation

Operator re-ran signals with `BAR_SOURCE=alpaca` at ~10:53 UTC.
Fresh JSON at `data/market/2026-07-06/0630_signals.json` now shows:

- `regime.regime = bullish_trend`, `confidence = medium`
- `spy_pct_from_50dma = 0.017601979230494225` (matches "+1.76%")
- `proxy_vol_20d_annualized_pct = 16.283558583618685` (matches "16.28")
- CSCO `return_6m = 0.5004472843450478` (matches "+50.04%")
- XOM 0.1955 / GOOGL 0.1804 / UNH 0.1715 / NVDA 0.1624 — all matching
- Signal counts: 7 ENTRY, 17 EXIT, 2 NO_SIGNAL — matches
- `bar_source = "alpaca"`, all 25 symbols fetched clean (300 bars each)

## Verdict on this routine

Re-review of the report, journal, and JSON against CLAUDE.md and
`config/approved_modes.yaml` (mode `PAPER_TRADING`): all cited
numbers now trace exactly to the deterministic engine output.
No trade decisions were issued; no writes to `config/`, `.claude/agents/`,
`prompts/routines/`, or `trades/live/*`; no `trades/paper/log.csv` or
`decisions/2026-07-06/` writes; INTU not referenced as tradable;
`news_unavailable` handled as a risk factor per CLAUDE.md
"handling missing data."

This companion supersedes the fabrication concern in the prior log.
The 24-hour "second compliance rejection triggers HALT recommendation"
counter is NOT incremented — the original rejection is reclassified
as a stale-artifact false positive caused by a background-job race,
not a fabrication event.

## Operational follow-up (not blocking)

- Recommend the operator kill any lingering `signals.evaluate_all`
  background processes before drafting reports, or write to a
  timestamped filename (e.g. `0630_signals_alpaca.json`) so a
  zombie job cannot silently overwrite the trusted artifact.
- Consider adding `bar_source` to the report front-matter cross-check
  so a JSON with `bar_source != "alpaca"` under the current
  yfinance-blocked posture fails the pre_market routine loudly.
