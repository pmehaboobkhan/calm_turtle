"""Hermes reflection cycle for Calm Turtle.

Two modes:
  --fallback   Deterministic rule-based reflection. Used before Hermes is
               installed. Reads score, applies one conservative parameter
               adjustment, writes proposal to prompts/proposed_updates/.

  --hermes     Production mode. Formats recent trades + current strategy as
               a prompt, calls hermes subprocess, parses the hypothesis,
               records it.

In both modes:
  - Exactly ONE variable is proposed per cycle (scientific-method guardrail).
  - Prior strategy snapshot is saved to state/history/.
  - Hypothesis is appended to state/hypotheses.jsonl.
  - The proposal goes to prompts/proposed_updates/ for human review.
  - config/strategy_rules.yaml is NEVER modified directly (PR-locked).
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
STRATEGY_FILE = REPO_ROOT / "config" / "strategy_rules.yaml"
GOAL_FILE = REPO_ROOT / "state" / "goal.yaml"
HYPOTHESES_FILE = REPO_ROOT / "state" / "hypotheses.jsonl"
HISTORY_DIR = REPO_ROOT / "state" / "history"
PROPOSALS_DIR = REPO_ROOT / "prompts" / "proposed_updates"
TRADES_LOG = REPO_ROOT / "trades" / "paper" / "log.csv"


def _load_yaml(path: Path) -> dict:
    with path.open() as f:
        return yaml.safe_load(f)


def _save_snapshot(strategy: dict, label: str) -> Path:
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    snap_path = HISTORY_DIR / f"strategy_snapshot_{ts}_{label}.yaml"
    with snap_path.open("w") as f:
        yaml.dump(strategy, f, default_flow_style=False, sort_keys=False)
    return snap_path


def _append_hypothesis(hypothesis: dict) -> None:
    HYPOTHESES_FILE.parent.mkdir(parents=True, exist_ok=True)
    with HYPOTHESES_FILE.open("a") as f:
        f.write(json.dumps(hypothesis) + "\n")


def _write_proposal(proposal_md: str) -> Path:
    PROPOSALS_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    proposal_path = PROPOSALS_DIR / f"strategy_proposal_{ts}.md"
    with proposal_path.open("w") as f:
        f.write(proposal_md)
    return proposal_path


def _load_recent_trades(n: int = 25) -> list[dict]:
    import csv  # noqa: PLC0415
    rows = []
    with TRADES_LOG.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("status", "").upper() == "CLOSED":
                rows.append(row)
    return rows[-n:]


def run_fallback() -> None:
    """Deterministic reflection: one rule, one variable changed."""
    from lib.score import score as compute_score  # noqa: PLC0415

    result = compute_score()
    strategy = _load_yaml(STRATEGY_FILE)
    goal = _load_yaml(GOAL_FILE)

    snap_path = _save_snapshot(strategy, "pre_fallback")
    print(f"  snapshot saved → {snap_path.name}")

    score_val = result["score"]
    components = result["components"]
    realised_return = components["realised_return_30d"]
    max_dd = components["max_drawdown"]

    target_return = goal["target_return_30d"]
    max_dd_limit = goal["max_drawdown"]

    variable_changed = None
    old_value = None
    new_value = None
    rationale = ""

    if max_dd > max_dd_limit:
        old_val = strategy.get("minimum_risk_reward_ratio", 1.5)
        new_val = round(old_val + 0.1, 2)
        variable_changed = "minimum_risk_reward_ratio"
        old_value = old_val
        new_value = new_val
        rationale = (
            f"Drawdown {max_dd:.2%} exceeds limit {max_dd_limit:.2%}. "
            f"Raising minimum R/R from {old_val} to {new_val} to reduce position frequency."
        )
    elif realised_return < target_return:
        old_val = strategy.get("abnormal_volatility_threshold_atr_multiplier", 2.5)
        new_val = round(old_val + 0.25, 2)
        variable_changed = "abnormal_volatility_threshold_atr_multiplier"
        old_value = old_val
        new_value = new_val
        rationale = (
            f"30d return {realised_return:.2%} below target {target_return:.2%}. "
            f"Loosening abnormal_volatility_threshold from {old_val} to {new_val} "
            "to allow entries in slightly elevated volatility."
        )
    else:
        print(f"  score={score_val:.4f} — on target. No change needed this cycle.")
        hypothesis = {
            "cycle_at": datetime.now(UTC).isoformat(),
            "mode": "fallback",
            "score": score_val,
            "variable_changed": None,
            "rationale": "On target — no change applied.",
            "proposal_path": None,
        }
        _append_hypothesis(hypothesis)
        return

    proposal_md = f"""# Strategy Proposal — Fallback Reflection
Generated: {datetime.now(UTC).isoformat()}
Mode: deterministic fallback
Score: {score_val:.4f}

## Hypothesis
Variable: `{variable_changed}`
Old value: `{old_value}`
Proposed value: `{new_value}`

## Rationale
{rationale}

## Components
- Realised 30d return: {realised_return:.4%}
- Max drawdown: {max_dd:.4%}
- Sharpe: {components['sharpe']:.4f}

## Action required
Review and apply by updating `config/strategy_rules.yaml` via a PR.
This file is PR-locked — do not edit directly.
"""

    proposal_path = _write_proposal(proposal_md)
    hypothesis = {
        "cycle_at": datetime.now(UTC).isoformat(),
        "mode": "fallback",
        "score": score_val,
        "variable_changed": variable_changed,
        "old_value": old_value,
        "proposed_value": new_value,
        "rationale": rationale,
        "proposal_path": str(proposal_path.relative_to(REPO_ROOT)),
    }
    _append_hypothesis(hypothesis)
    print(f"  variable: {variable_changed}  {old_value} → {new_value}")
    print(f"  proposal → {proposal_path.name}")
    print(f"  hypothesis appended to {HYPOTHESES_FILE.name}")


def run_hermes() -> None:
    """Call hermes subprocess with a formatted prompt."""
    from lib.score import score as compute_score  # noqa: PLC0415

    result = compute_score()
    strategy = _load_yaml(STRATEGY_FILE)
    goal = _load_yaml(GOAL_FILE)
    recent_trades = _load_recent_trades(25)

    snap_path = _save_snapshot(strategy, "pre_hermes")
    print(f"  snapshot saved → {snap_path.name}")

    prompt = f"""You are reflecting on the Calm Turtle trading system outcomes.

## Current score: {result['score']:.4f}
## Components
{json.dumps(result['components'], indent=2)}

## Goal
{json.dumps({'target_return_30d': goal['target_return_30d'], 'max_drawdown': goal['max_drawdown'], 'min_sharpe': goal['min_sharpe']}, indent=2)}

## Recent closed trades (last 25)
{json.dumps(recent_trades, indent=2)}

## Current strategy parameters (config/strategy_rules.yaml excerpt)
minimum_risk_reward_ratio: {strategy.get('minimum_risk_reward_ratio')}
abnormal_volatility_threshold_atr_multiplier: {strategy.get('abnormal_volatility_threshold_atr_multiplier')}
holding_earnings_caution_window_days: {strategy.get('holding_earnings_caution_window_days')}

## Your task
Propose exactly ONE variable change that is most likely to improve the score.
Format your response as JSON:
{{
  "variable": "<parameter name>",
  "old_value": <current value>,
  "proposed_value": <new value>,
  "rationale": "<one sentence why>",
  "confidence": <0.0-1.0>
}}
"""

    try:
        proc = subprocess.run(
            ["hermes", "--json"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=120,
        )
        output = proc.stdout.strip()
        start = output.find("{")
        end = output.rfind("}") + 1
        if start == -1 or end == 0:
            raise ValueError(f"No JSON in hermes output: {output[:200]}")
        parsed = json.loads(output[start:end])
    except (subprocess.TimeoutExpired, FileNotFoundError, ValueError) as e:
        print(f"  hermes call failed: {e}")
        print("  falling back to deterministic reflect")
        run_fallback()
        return

    variable_changed = parsed.get("variable")
    old_value = parsed.get("old_value")
    new_value = parsed.get("proposed_value")
    rationale = parsed.get("rationale", "")
    confidence = parsed.get("confidence", 0.0)

    proposal_md = f"""# Strategy Proposal — Hermes Reflection
Generated: {datetime.now(UTC).isoformat()}
Mode: hermes
Score: {result['score']:.4f}
Confidence: {confidence:.2f}

## Hypothesis
Variable: `{variable_changed}`
Old value: `{old_value}`
Proposed value: `{new_value}`

## Rationale
{rationale}

## Action required
Review and apply by updating `config/strategy_rules.yaml` via a PR.
This file is PR-locked — do not edit directly.
"""

    proposal_path = _write_proposal(proposal_md)
    hypothesis = {
        "cycle_at": datetime.now(UTC).isoformat(),
        "mode": "hermes",
        "score": result["score"],
        "variable_changed": variable_changed,
        "old_value": old_value,
        "proposed_value": new_value,
        "rationale": rationale,
        "confidence": confidence,
        "proposal_path": str(proposal_path.relative_to(REPO_ROOT)),
    }
    _append_hypothesis(hypothesis)
    print(f"  variable: {variable_changed}  {old_value} → {new_value}  (confidence={confidence:.2f})")
    print(f"  proposal → {proposal_path.name}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Hermes reflection cycle for Calm Turtle")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fallback", action="store_true", help="Deterministic rule-based reflection")
    group.add_argument("--hermes", action="store_true", help="Hermes-driven reflection")
    args = parser.parse_args()

    print(f"[reflect] {datetime.now(UTC).isoformat()}")
    if args.fallback:
        print("  mode: fallback (deterministic)")
        run_fallback()
    else:
        print("  mode: hermes")
        run_hermes()


if __name__ == "__main__":
    main()
