# Strategy Proposal — Fallback Reflection
Generated: 2026-05-23T18:47:34.483392+00:00
Mode: deterministic fallback
Score: 0.0126

## Hypothesis
Variable: `abnormal_volatility_threshold_atr_multiplier`
Old value: `2.5`
Proposed value: `2.75`

## Rationale
30d return 0.62% below target 0.75%. Loosening abnormal_volatility_threshold from 2.5 to 2.75 to allow entries in slightly elevated volatility.

## Components
- Realised 30d return: 0.6189%
- Max drawdown: 0.0000%
- Sharpe: 0.0000

## Action required
Review and apply by updating `config/strategy_rules.yaml` via a PR.
This file is PR-locked — do not edit directly.
