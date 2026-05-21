"""Compliance blocklist tests.

Covers the defense-in-depth INTU block introduced 2026-05-20 because the
operator is employed by Intuit. See:
  - config/watchlist.yaml > blocked_symbols
  - lib/config.py > blocked_symbols(), is_symbol_blocked(), validate_watchlist_invariants(), ComplianceError
  - lib/signals.py > universe filter
  - lib/paper_sim.py > open_position guard
  - lib/broker.py > submit_market_order guard
  - .claude/hooks/block_compliance_symbols.sh

Run with: pytest tests/test_compliance_blocklist.py -v
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from lib import broker, config, paper_sim, signals  # noqa: E402


# ---------------------------------------------------------------------------
# Layer 1+2 — config-level blocklist
# ---------------------------------------------------------------------------

def test_intu_is_blocked_by_default() -> None:
    """INTU must be in the blocklist out-of-the-box (employer restriction)."""
    assert config.is_symbol_blocked("INTU") is True
    assert config.is_symbol_blocked("intu") is True  # case-insensitive
    assert config.is_symbol_blocked("Intu") is True
    assert config.is_symbol_blocked("SPY") is False


def test_blocklist_contains_required_fields() -> None:
    """Each blocklist entry must carry an audit trail."""
    required = {"symbol", "reason", "scope", "added_on", "added_by"}
    entries = config.blocked_symbols()
    assert len(entries) >= 1, "blocklist must contain at least INTU"
    for entry in entries:
        missing = required - set(entry.keys())
        assert not missing, f"blocklist entry {entry.get('symbol')!r} missing {missing}"
        assert entry["scope"] == "all", "only scope=all is supported in v1"


def test_blocked_symbol_cannot_appear_in_symbols() -> None:
    """validate_watchlist_invariants() must reject a config where a blocked
    symbol also appears in the trading allowlist. Without this invariant,
    INTU could be silently re-approved by an accidental allowlist edit.
    """
    bad_watchlist = {
        "schema_version": 1,
        "universe": "test",
        "benchmarks": {"primary": "X"},
        "symbols": [
            {"symbol": "SPY", "company_name": "SPDR", "sector": "Equity",
             "approved_for_research": True, "approved_for_paper_trading": True,
             "approved_for_live_trading": False, "max_position_size_pct": 60},
            {"symbol": "INTU", "company_name": "Intuit Inc.", "sector": "Technology",
             "approved_for_research": True, "approved_for_paper_trading": True,
             "approved_for_live_trading": False, "max_position_size_pct": 15},
        ],
        "blocked_symbols": [
            {"symbol": "INTU", "company_name": "Intuit Inc.",
             "reason": "test", "scope": "all",
             "added_on": "2026-05-20", "added_by": "human"},
        ],
    }
    with pytest.raises(config.ConfigError, match=r"INTU"):
        config.validate_watchlist_invariants(bad_watchlist)


# ---------------------------------------------------------------------------
# Layer 3 — deterministic chokepoints
# ---------------------------------------------------------------------------

def _trend_bars(n: int, start: float = 100.0, daily_pct: float = 0.001) -> list[dict]:
    bars = []
    for i in range(n):
        close = start * (1 + daily_pct) ** i
        bars.append({
            "ts": f"2024-01-{(i % 28) + 1:02d}T00:00:00Z",
            "open": close * 0.999, "high": close * 1.001,
            "low": close * 0.998, "close": close, "volume": 1_000_000,
        })
    return bars


def test_large_cap_momentum_excludes_blocked_symbols() -> None:
    """Even if INTU is passed in watchlist_symbols with strong synthetic
    momentum, the strategy must never generate a signal for it.
    """
    bars = {
        "SPY": _trend_bars(280, start=400, daily_pct=0.0015),
        "IEF": _trend_bars(280, start=100, daily_pct=0.0005),
        "GLD": _trend_bars(280, start=180, daily_pct=0.0003),
        "SHV": _trend_bars(280, start=110, daily_pct=0.0002),
        "INTU": _trend_bars(280, start=100, daily_pct=0.0050),   # would be rank 1
        "STOCK_A": _trend_bars(280, start=100, daily_pct=0.0025),
        "STOCK_B": _trend_bars(280, start=100, daily_pct=0.0020),
    }
    sigs = signals.evaluate_large_cap_momentum_top5(
        bars,
        watchlist_symbols=list(bars.keys()),
        regime=signals.RegimeReading("bullish_trend", "medium", {}, []),
        strategy_rules={},
    )
    assert all(s.symbol != "INTU" for s in sigs), \
        "INTU must never appear in signal output, even with strongest momentum"


def test_paper_sim_open_position_refuses_blocked_symbol(monkeypatch, tmp_path) -> None:
    """The deterministic paper-sim must hard-fail on a blocked symbol."""
    monkeypatch.setattr(paper_sim, "PAPER_DIR", tmp_path)
    monkeypatch.setattr(paper_sim, "LOG_PATH", tmp_path / "log.csv")
    monkeypatch.setattr(paper_sim, "POSITIONS_PATH", tmp_path / "positions.json")
    monkeypatch.delenv("BROKER_PAPER", raising=False)
    with pytest.raises(config.ComplianceError, match=r"INTU"):
        paper_sim.open_position(
            symbol="INTU", side="BUY", quantity=1, quote_price=100.0,
            rationale_link="decisions/test/0001_INTU.json",
            stop_loss=90.0, take_profit=110.0,
        )


def test_broker_submit_refuses_blocked_symbol(monkeypatch) -> None:
    """The broker boundary must refuse a blocked symbol before any network call."""
    monkeypatch.setenv("ALPACA_PAPER_KEY_ID", "test_key")
    monkeypatch.setenv("ALPACA_PAPER_SECRET_KEY", "test_secret")
    with pytest.raises(config.ComplianceError, match=r"INTU"):
        broker.submit_market_order(symbol="INTU", qty=1, side="BUY")


# ---------------------------------------------------------------------------
# Layer 5 — PreToolUse hook
# ---------------------------------------------------------------------------

HOOK_PATH = REPO_ROOT / ".claude" / "hooks" / "block_compliance_symbols.sh"


def _invoke_hook(payload: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["bash", str(HOOK_PATH)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        check=False,
    )


def test_hook_refuses_intu_in_decision_path() -> None:
    """A Write targeting decisions/<date>/<HHMM>_INTU.json must be refused."""
    payload = {
        "tool_name": "Write",
        "tool_input": {
            "file_path": "decisions/2026-05-21/0930_INTU.json",
            "content": '{"symbol": "INTU", "decision": "PAPER_BUY"}',
        },
    }
    result = _invoke_hook(payload)
    assert result.returncode != 0, "hook must refuse INTU decision file"
    assert "INTU" in (result.stderr + result.stdout)


def test_hook_allows_intu_in_journal() -> None:
    """A learning note that references INTU is documentation, not a trade — allow."""
    payload = {
        "tool_name": "Write",
        "tool_input": {
            "file_path": "journals/daily/2026-05-21.md",
            "content": "Note: we cannot trade INTU due to employer restriction.",
        },
    }
    result = _invoke_hook(payload)
    assert result.returncode == 0, \
        f"hook must allow journal references to INTU, stderr={result.stderr}"
