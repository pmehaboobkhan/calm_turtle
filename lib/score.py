"""Composite scorer for Hermes reflection cycles.

Reads closed trades from trades/paper/log.csv and scores them against
state/goal.yaml. Returns a float in [-1, +1]:
  +1.0  — all targets exceeded
   0.0  — exactly on-target
  -1.0  — all targets missed / breach failure_below floor
"""
from __future__ import annotations

import math
from datetime import UTC, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TRADES_LOG = REPO_ROOT / "trades" / "paper" / "log.csv"
GOAL_FILE = REPO_ROOT / "state" / "goal.yaml"


def _load_goal() -> dict:
    with GOAL_FILE.open() as f:
        return yaml.safe_load(f)


def _load_closed_trades(n: int | None = None) -> pd.DataFrame:
    df = pd.read_csv(TRADES_LOG, parse_dates=["timestamp"])
    closed = df[df["status"].str.upper() == "CLOSED"].copy()
    if n is not None:
        closed = closed.tail(n)
    return closed


def _realised_return_30d(closed: pd.DataFrame, starting_capital: float = 100_000.0) -> float:
    if closed.empty:
        return 0.0
    now = datetime.now(UTC)
    cutoff = now - timedelta(days=30)
    recent = closed[closed["timestamp"] >= cutoff]
    if recent.empty:
        return 0.0
    total_pnl = recent["realized_pnl"].sum()
    return total_pnl / starting_capital


def _max_drawdown(closed: pd.DataFrame, starting_capital: float = 100_000.0) -> float:
    if closed.empty:
        return 0.0
    cumulative = starting_capital + closed["realized_pnl"].cumsum()
    running_max = cumulative.cummax()
    drawdowns = (running_max - cumulative) / running_max
    return float(drawdowns.max())


def _sharpe(closed: pd.DataFrame, trading_days_per_year: int = 252) -> float:
    if len(closed) < 5:
        return 0.0
    returns = closed["realized_pnl"] / 100_000.0
    mean = returns.mean()
    std = returns.std(ddof=1)
    if std == 0 or math.isnan(std):
        return 0.0
    daily_sharpe = mean / std
    return float(daily_sharpe * math.sqrt(trading_days_per_year))


def _clip(value: float, lo: float = -1.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def score(n_trades: int | None = None) -> dict:
    """Score recent closed trades against goal.yaml.

    Args:
        n_trades: use only the last N closed trades (None = all within 30d).

    Returns dict with keys: score (float), components (dict), metadata (dict).
    """
    goal = _load_goal()
    closed = _load_closed_trades(n=n_trades)

    target_return = goal["target_return_30d"]
    max_dd_limit = goal["max_drawdown"]
    min_sharpe = goal["min_sharpe"]
    failure_below = goal.get("failure_below", -0.04)
    weights = goal.get(
        "score_weights",
        {"return_vs_target": 0.50, "drawdown_vs_max": 0.30, "sharpe_vs_min": 0.20},
    )

    realised_return = _realised_return_30d(closed)
    max_dd = _max_drawdown(closed)
    sharpe = _sharpe(closed)

    if target_return > 0:
        return_component = _clip((realised_return - target_return) / target_return)
    else:
        return_component = 0.0

    dd_component = _clip(1.0 - (max_dd / max_dd_limit)) if max_dd_limit > 0 else 0.0

    if min_sharpe > 0:
        sharpe_component = _clip((sharpe - min_sharpe) / min_sharpe)
    else:
        sharpe_component = 0.0

    composite = (
        weights["return_vs_target"] * return_component
        + weights["drawdown_vs_max"] * dd_component
        + weights["sharpe_vs_min"] * sharpe_component
    )

    if realised_return < failure_below:
        composite = min(composite, -0.9)

    return {
        "score": round(_clip(composite), 4),
        "components": {
            "realised_return_30d": round(realised_return, 6),
            "max_drawdown": round(max_dd, 6),
            "sharpe": round(sharpe, 4),
            "return_component": round(return_component, 4),
            "dd_component": round(dd_component, 4),
            "sharpe_component": round(sharpe_component, 4),
        },
        "metadata": {
            "n_closed_trades": len(closed),
            "target_return_30d": target_return,
            "max_drawdown_limit": max_dd_limit,
            "min_sharpe": min_sharpe,
            "scored_at": datetime.now(UTC).isoformat(),
        },
    }


if __name__ == "__main__":
    import json
    result = score()
    print(json.dumps(result, indent=2))
