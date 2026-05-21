"""3-state (Bull/Bear/Sideways) Markov regime diagnostic.

Diagnostic only — NOT a trading signal. The walk-forward backtest of this method
on SPY produced Sharpe ~0.24, well below the portfolio target of 0.8. Use this
module to surface regime-change information in the weekly review (transition
persistence, stationary mix) so the human reviewer has a second view on whether
the current regime resembles history.

Threshold and window match the markov-hedge-fund-method skill defaults:
  Bull     : 20-day rolling return >  +2%
  Bear     : 20-day rolling return <  -2%
  Sideways : otherwise

Pure-Python by design — no numpy/pandas dependency. Keeps the module load fast
and unit-testable in isolation, matching lib.indicators.
"""
from __future__ import annotations

from collections.abc import Sequence

STATES: tuple[str, str, str] = ("Bear", "Sideways", "Bull")  # indices 0, 1, 2


def label_regimes(
    closes: Sequence[float],
    *,
    window: int = 20,
    threshold: float = 0.02,
) -> list[int]:
    """Label each day as Bear (0) / Sideways (1) / Bull (2) from rolling return.

    Returns a list of length `len(closes) - window` (the first `window` days
    have no rolling return defined and are dropped).
    """
    if len(closes) <= window:
        return []
    labels: list[int] = []
    for i in range(window, len(closes)):
        ret = closes[i] / closes[i - window] - 1.0
        if ret > threshold:
            labels.append(2)
        elif ret < -threshold:
            labels.append(0)
        else:
            labels.append(1)
    return labels


def build_transition_matrix(labels: Sequence[int]) -> list[list[float]]:
    """MLE 3x3 transition matrix from a sequence of regime labels.

    P[i][j] = empirical probability of moving from state i to state j on the
    next day. Rows where state i was never observed get a uniform 1/3 row so
    downstream code (stationary, P(Bull next), etc.) never sees NaN.
    """
    counts = [[0, 0, 0] for _ in range(3)]
    for a, b in zip(labels, labels[1:]):
        counts[a][b] += 1
    matrix: list[list[float]] = []
    for row in counts:
        total = sum(row)
        if total == 0:
            matrix.append([1 / 3, 1 / 3, 1 / 3])
        else:
            matrix.append([c / total for c in row])
    return matrix


def stationary_distribution(
    matrix: Sequence[Sequence[float]],
    *,
    max_iter: int = 1000,
    tol: float = 1e-10,
) -> list[float]:
    """Long-run regime mix: solve πP = π by power iteration on the matrix.

    Returns [P(Bear), P(Sideways), P(Bull)]. Avoids a numpy linalg dependency.
    """
    pi = [1 / 3, 1 / 3, 1 / 3]
    for _ in range(max_iter):
        new_pi = [
            sum(pi[i] * matrix[i][j] for i in range(3))
            for j in range(3)
        ]
        delta = max(abs(new_pi[j] - pi[j]) for j in range(3))
        pi = new_pi
        if delta < tol:
            break
    total = sum(pi)
    return [p / total for p in pi]


def regime_snapshot(closes: Sequence[float], *, window: int = 20) -> dict:
    """One-call summary: labels, transition matrix, stationary, current regime.

    Returns a dict suitable for direct JSON serialization or for rendering
    into a markdown block via `format_snapshot_markdown`.
    """
    labels = label_regimes(closes, window=window)
    if not labels:
        return {
            "window": window,
            "samples": 0,
            "current_regime": None,
            "transition_matrix": None,
            "stationary": None,
            "diagonal": None,
        }
    matrix = build_transition_matrix(labels)
    pi = stationary_distribution(matrix)
    return {
        "window": window,
        "samples": len(labels),
        "current_regime": STATES[labels[-1]],
        "transition_matrix": matrix,
        "stationary": {STATES[i]: pi[i] for i in range(3)},
        "diagonal": {STATES[i]: matrix[i][i] for i in range(3)},
    }


def format_snapshot_markdown(snapshot: dict, *, symbol: str) -> str:
    """Render a snapshot dict as a markdown block for the weekly journal."""
    if snapshot["samples"] == 0:
        return (
            f"### Markov regime diagnostic — {symbol}\n\n"
            f"Insufficient data (need > {snapshot['window']} bars).\n"
        )
    m = snapshot["transition_matrix"]
    pi = snapshot["stationary"]
    diag = snapshot["diagonal"]
    lines = [
        f"### Markov regime diagnostic — {symbol}",
        "",
        f"> Diagnostic only — NOT a trade signal. Samples: {snapshot['samples']} | "
        f"current regime: **{snapshot['current_regime']}**",
        "",
        "**Transition matrix (rows = from, cols = to):**",
        "",
        "| from \\ to | Bear | Sideways | Bull |",
        "|-----------|------|----------|------|",
    ]
    for i, name in enumerate(STATES):
        lines.append(
            f"| {name} | {m[i][0]*100:.1f}% | {m[i][1]*100:.1f}% | {m[i][2]*100:.1f}% |"
        )
    lines += [
        "",
        "**Persistence (diagonal):** "
        f"Bear→Bear {diag['Bear']*100:.1f}% · "
        f"Sideways→Sideways {diag['Sideways']*100:.1f}% · "
        f"Bull→Bull {diag['Bull']*100:.1f}%",
        "",
        "**Stationary distribution (long-run mix):** "
        f"Bear {pi['Bear']*100:.1f}% · "
        f"Sideways {pi['Sideways']*100:.1f}% · "
        f"Bull {pi['Bull']*100:.1f}%",
        "",
        "_Reviewer cue: if current persistence drops materially below the "
        "SPY historical Bull→Bull ~89% or stationary Bear share spikes above "
        "~25%, treat as a regime-change flag and corroborate against the "
        "10-month SMA filter before next week's TAA rebalance._",
        "",
    ]
    return "\n".join(lines)
