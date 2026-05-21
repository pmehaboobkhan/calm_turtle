"""Unit tests for lib.regime_markov.

Pure-compute checks. No network, no Yahoo, no Alpaca.
"""
from __future__ import annotations

from lib import regime_markov


def test_label_regimes_classifies_bull_bear_sideways():
    closes = [100.0] * 20
    closes += [105.0]  # +5%   → Bull
    closes += [104.0]  # +4%   → Bull
    closes += [100.5]  # +0.5% → Sideways
    closes += [99.0]   # -1%   → Sideways
    closes += [95.0]   # -5%   → Bear
    labels = regime_markov.label_regimes(closes, window=20)
    assert labels == [2, 2, 1, 1, 0]


def test_transition_matrix_rows_sum_to_one():
    labels = [0, 1, 2, 1, 0, 2, 2, 1]
    matrix = regime_markov.build_transition_matrix(labels)
    for row in matrix:
        assert abs(sum(row) - 1.0) < 1e-9


def test_transition_matrix_unobserved_state_falls_back_uniform():
    labels = [1, 2, 1, 2, 1, 2]
    matrix = regime_markov.build_transition_matrix(labels)
    assert matrix[0] == [1 / 3, 1 / 3, 1 / 3]


def test_stationary_distribution_sums_to_one_and_is_fixed_point():
    matrix = [
        [0.8, 0.2, 0.0],
        [0.1, 0.7, 0.2],
        [0.0, 0.1, 0.9],
    ]
    pi = regime_markov.stationary_distribution(matrix)
    assert abs(sum(pi) - 1.0) < 1e-9
    new_pi = [sum(pi[i] * matrix[i][j] for i in range(3)) for j in range(3)]
    for a, b in zip(pi, new_pi):
        assert abs(a - b) < 1e-7


def test_regime_snapshot_handles_too_little_data():
    snap = regime_markov.regime_snapshot([100.0, 101.0, 102.0], window=20)
    assert snap["samples"] == 0
    assert snap["current_regime"] is None


def test_format_snapshot_markdown_includes_key_fields():
    closes = [100.0 + 0.1 * i for i in range(60)]
    snap = regime_markov.regime_snapshot(closes, window=20)
    md = regime_markov.format_snapshot_markdown(snap, symbol="TEST")
    assert "Markov regime diagnostic — TEST" in md
    assert "Transition matrix" in md
    assert "Stationary distribution" in md
    assert "NOT a trade signal" in md
