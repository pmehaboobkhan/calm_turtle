# Risk Event — Corrupt daily bar (2026-06-09) detected at pre-market

- **Timestamp (UTC):** 2026-06-10T10:35:00Z
- **Routine:** `pre_market`
- **Severity:** WARN
- **Category:** data_quality
- **Trigger:** `lib.data.get_bars()` returned a 2026-06-09 daily bar with `open/high/low/close = NaN` (volume populated) across **all 25 watchlist symbols**.

## What was observed
- All 25 symbols in `config/watchlist.yaml` returned a final bar timestamped `2026-06-09T00:00:00+00:00` with `close=nan`.
- Identical pattern across SPY, GLD, IEF, SHV plus 21 large-caps suggests a provider-side outage rather than per-symbol corruption.
- Without truncation, this contaminates downstream momentum / 50d MA / 210d MA calculations and would mis-classify the regime as `bearish_trend` purely due to `NaN > MA` comparisons returning False.

## Mitigation applied this run
- Trailing-NaN bars truncated symbol-by-symbol before passing to `signals.detect_regime` and `signals.evaluate_all`. Last clean bar = `2026-06-08T00:00:00+00:00`.
- Truncation recorded in `data/market/2026-06-10/<HHMM>.json > data_quality`.
- Regime + signals computed against the 06-08 close (this is research-only; pre-market does not open trades).
- The 2026-06-09 bar's contaminated state is also visible in yesterday's EOD report context — the operator should investigate why the close was published with NaN OHLC.

## Downstream impact on this routine
- **No paper trades.** Pre-market is research-only.
- The pre-market report uses the 06-08 close as the most recent reliable mark and flags the staleness explicitly to downstream EOD.
- If the corruption persists into today's EOD (16:30 ET), `end_of_day` MUST refuse all ENTRY signals under CLAUDE.md rule #5 (`risk_limits.data.max_data_staleness_seconds`) and produce `NO_TRADE` decisions with the staleness logged.

## Recommended follow-up (no auto-action)
- Verify the data-vendor connector wrote the 06-09 bar from a partial / cancelled session.
- Inspect `lib.data.get_bars()` to consider raising a structured error (or marking the bar `quarantined`) rather than returning NaN OHLC silently.
- If today's 06-10 daily bar also lands as NaN at EOD, this becomes a 2-day systemic outage and `pre_close` / `end_of_day` should write a HIGH-severity risk event and consider escalating per the precedent in the 2026-06-03 / 06-04 snapshots.

## Files
- Sanitized signals: `data/market/2026-06-10/1035.json` (this run)
- Raw bars source: `lib.data.get_bars()` (provider feed)
