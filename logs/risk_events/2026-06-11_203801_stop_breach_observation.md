# Stop-Loss Breach Observation — CSCO, NVDA — 2026-06-11

**Type:** Mark-to-market below per-position stop_loss (observation; v1 EOD does NOT auto-close on stops)
**Detected by:** EOD orchestrator (Step 9 PnL cross-check vs position_meta stops)
**Timestamp:** 2026-06-11T20:38:01Z
**Routine:** end_of_day
**Severity:** ELEVATED (risk flag for operator; not an auto-action in v1)

## Observation

Two open positions closed below their recorded per-position stop_loss on the 2026-06-11 bar, yet the deterministic momentum engine did NOT emit an EXIT signal for either (the large_cap_momentum_top5 strategy ranks/holds on 6-month return; it does not consume per-position stops):

| Symbol | Last | Stop | % vs entry | Signal action | Rank |
|---|---|---|---|---|---|
| CSCO | 115.94 | 117.00 | -10.83% | ENTRY (held) | rank 1 (6m +52.27%) |
| NVDA | 191.33 | 196.79 | -12.52% | NO_SIGNAL (hold zone) | rank 7 (6m +8.15%) |

## Why no auto-close in v1

Per `prompts/routines/end_of_day.md` steps 6–7, the v1 EOD routine opens/closes paper positions **purely on deterministic signal actions** (ENTRY / EXIT). Per-position `stop_loss` / `take_profit` are recorded as position metadata for traceability and for a future stops-overlay, but there is no forced-close-on-stop code path in the v1 EOD flow. The momentum engine continues to hold CSCO (rank 1) and NVDA (rank 7, within the top-7 buffer hold-zone).

This is a known design tension: a pure trend/momentum holder tolerates drawdown that a per-position stop would cut. The asymmetric drawdown protection in v1 is the **portfolio-level circuit-breaker** (Path Z), not per-name stops.

## Action / disposition

- **No trade executed this run** (deterministic engine produced 0 EXITs on open positions).
- Flag carried to journal "what failed" section and to tomorrow's pre_market watch list.
- CSCO is the marginal name: rank-1 by 6m return but worst MtM drawdown (-10.83%). If CSCO momentum rank deteriorates and it exits the top-7 buffer, the engine will EXIT it on a future bar.
- NVDA at rank 7 sits at the edge of the demotion buffer; a further slip to rank ≥ 8 flips it from NO_SIGNAL (hold) to EXIT.
- **Recommend** Self-Learning Agent (weekly) evaluate whether a per-position hard-stop overlay should be proposed for `large_cap_momentum_top5` — propose only via `prompts/proposed_updates/`, never a direct config change.

## Context

- Portfolio equity $100,227.16 (+0.23% vs $100k start); day PnL -$102.71 (-0.10%).
- CB FULL, throttle 1.0 (write skipped — 1 pending broker order; FULL carried forward).
- Total unrealized vs entry across book: -$887.63, concentrated in CSCO (-$648) and NVDA (-$739), partially offset by UNH (+$494).
