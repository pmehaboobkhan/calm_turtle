"""Tests for Alpaca-mirror state integrity fixes.

Two defects this covers (see prompts/proposed_updates/2026-05-26_alpaca_mirror_state_integrity.md):

1. Stop/target persistence — the Alpaca mirror reconcile rebuilds positions.json
   with stop_loss=null/take_profit=null, silently disabling the deterministic
   stop check. A `position_meta.json` side-file preserves them and:
     - paper_sim.open_position writes it; close_position removes the key;
     - sync_positions_from_broker() (called by reconcile in alpaca mode) merges
       the stops back into the mirrored positions.json;
     - portfolio_health.assess_positions falls back to it when the live
       positions.json value is null (defense-in-depth).
   The UNH regression: on 2026-05-26 UNH sat -8.23% and only +2.17% above its
   stop, but the stop check was inert because positions.json carried null.

2. pending_broker_count() — lets routines skip the circuit-breaker equity write
   while broker orders are in flight (cash debited, position not yet mirrored),
   which produced the spurious HALF state on 2026-05-19.

Run with: pytest tests/test_position_meta_and_pending.py -v
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from lib import paper_sim, portfolio_health  # noqa: E402

HEADER = ",".join(paper_sim.LOG_HEADER) + "\n"


# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------

@pytest.fixture
def isolated(monkeypatch, tmp_path):
    """Redirect all paper_sim file paths into a temp dir (sim mode)."""
    monkeypatch.delenv("BROKER_PAPER", raising=False)  # default = sim
    monkeypatch.setattr(paper_sim, "PAPER_DIR", tmp_path)
    monkeypatch.setattr(paper_sim, "LOG_PATH", tmp_path / "log.csv")
    monkeypatch.setattr(paper_sim, "POSITIONS_PATH", tmp_path / "positions.json")
    monkeypatch.setattr(paper_sim, "POSITION_META_PATH", tmp_path / "position_meta.json")
    return tmp_path


def _write_log(tmp_path: Path, rows: list[str]) -> None:
    (tmp_path / "log.csv").write_text(HEADER + "".join(r + "\n" for r in rows), encoding="utf-8")


def _write_positions(tmp_path: Path, content: dict) -> None:
    (tmp_path / "positions.json").write_text(json.dumps(content), encoding="utf-8")


# ===========================================================================
# Defect 1a — position_meta.json side-file lifecycle (paper_sim, sim mode)
# ===========================================================================

def test_open_position_writes_meta(isolated):
    paper_sim.open_position(
        symbol="AAPL", side="BUY", quantity=10, quote_price=180.0,
        rationale_link="decisions/2026-05-26/1600_AAPL.json",
        stop_loss=162.0, take_profit=225.0,
    )
    meta = json.loads((isolated / "position_meta.json").read_text())
    assert "AAPL" in meta
    assert meta["AAPL"]["stop_loss"] == 162.0
    assert meta["AAPL"]["take_profit"] == 225.0


def test_close_position_removes_meta(isolated):
    paper_sim.open_position(
        symbol="AAPL", side="BUY", quantity=10, quote_price=180.0,
        rationale_link="decisions/2026-05-26/1600_AAPL.json",
        stop_loss=162.0, take_profit=225.0,
    )
    paper_sim.close_position(
        "AAPL", quote_price=190.0,
        rationale_link="decisions/2026-05-26/1700_AAPL.json",
    )
    meta = json.loads((isolated / "position_meta.json").read_text())
    assert "AAPL" not in meta


# ===========================================================================
# Defect 1b — reconcile (alpaca) restores stops from meta
# ===========================================================================

def test_sync_from_broker_restores_stops_from_meta(isolated, monkeypatch):
    """The core fix: the Alpaca mirror has no stops, but the side-file does,
    so the rebuilt positions.json must carry the stop/target, not null."""
    # Side-file remembers UNH's stop/target from when it was opened.
    (isolated / "position_meta.json").write_text(json.dumps({
        "UNH": {"stop_loss": 352.017, "take_profit": 488.9125,
                "entry_basis": 391.9044, "opened_at": "2026-05-19T20:42:20Z",
                "rationale_link": "decisions/2026-05-19/2038_UNH.json"},
    }), encoding="utf-8")

    # Alpaca returns the position with NO stop metadata (the real behavior).
    from lib import broker
    monkeypatch.setattr(broker, "get_positions", lambda: [
        {"symbol": "UNH", "qty": "39", "avg_entry_price": "391.9044"},
    ])

    paper_sim.sync_positions_from_broker()

    pos = json.loads((isolated / "positions.json").read_text())
    assert pos["UNH"]["stop_loss"] == 352.017
    assert pos["UNH"]["take_profit"] == 488.9125


def test_sync_from_broker_leaves_null_when_no_meta(isolated, monkeypatch):
    """No side-file entry → behave as before (null stop). Backward compatible."""
    from lib import broker
    monkeypatch.setattr(broker, "get_positions", lambda: [
        {"symbol": "GLD", "qty": "36", "avg_entry_price": "412.0419"},
    ])
    paper_sim.sync_positions_from_broker()
    pos = json.loads((isolated / "positions.json").read_text())
    assert pos["GLD"]["stop_loss"] is None


# ===========================================================================
# Defect 1c — portfolio_health falls back to meta when positions.json is null
# ===========================================================================

def _positions_file(tmp_path: Path, positions: dict) -> Path:
    p = tmp_path / "positions.json"
    p.write_text(json.dumps(positions), encoding="utf-8")
    return p


def _meta_file(tmp_path: Path, meta: dict) -> Path:
    m = tmp_path / "position_meta.json"
    m.write_text(json.dumps(meta), encoding="utf-8")
    return m


def test_health_uses_meta_when_positions_stop_is_null(tmp_path):
    """The UNH regression: positions.json stop is null (mirror-wiped) but the
    side-file has the real -10% stop, so a breach must be detected."""
    pos_path = _positions_file(tmp_path, {
        "UNH": {"side": "BUY", "quantity": 39, "entry_price": 391.9044,
                "entry_ts": "2026-05-19T20:42:20Z",
                "stop_loss": None, "take_profit": None,
                "rationale_link": "alpaca-mirror"},
    })
    meta_path = _meta_file(tmp_path, {
        "UNH": {"stop_loss": 352.017, "take_profit": 488.9125},
    })
    # Quote breaks below the meta stop.
    [h] = portfolio_health.assess_positions(
        {"UNH": 351.0}, positions_path=pos_path, meta_path=meta_path,
    )
    assert h.stop_loss == 352.017
    assert h.stop_breached is True
    assert h.should_close() is True


def test_health_positions_stop_wins_over_meta(tmp_path):
    """If positions.json carries a live stop, it is authoritative; meta does
    not override it."""
    pos_path = _positions_file(tmp_path, {
        "AAPL": {"side": "BUY", "quantity": 10, "entry_price": 180.0,
                 "entry_ts": "2026-05-26T13:30:00Z",
                 "stop_loss": 170.0, "take_profit": 200.0,
                 "rationale_link": "x"},
    })
    meta_path = _meta_file(tmp_path, {"AAPL": {"stop_loss": 175.0, "take_profit": 200.0}})
    [h] = portfolio_health.assess_positions(
        {"AAPL": 172.0}, positions_path=pos_path, meta_path=meta_path,
    )
    # 172 > live stop 170 → not breached. If meta (175) wrongly won, it would breach.
    assert h.stop_loss == 170.0
    assert h.stop_breached is False


def test_health_null_stop_no_meta_is_backward_compatible(tmp_path):
    """No meta + null stop → no breach (preserves pre-fix behavior)."""
    pos_path = _positions_file(tmp_path, {
        "GLD": {"side": "BUY", "quantity": 10, "entry_price": 180.0,
                "entry_ts": "2026-05-26T13:30:00Z",
                "stop_loss": None, "take_profit": None, "rationale_link": "x"},
    })
    [h] = portfolio_health.assess_positions(
        {"GLD": 100.0}, positions_path=pos_path, meta_path=tmp_path / "missing.json",
    )
    assert h.stop_breached is False
    assert h.should_close() is False


# ===========================================================================
# Defect 2 — pending_broker_count()
# ===========================================================================

def test_pending_broker_count_zero_when_no_pending(isolated):
    _write_log(isolated, [
        "2026-05-15T00:31:53+00:00,_RESET_,RESET,0,0,scripts/sync_alpaca_state.py,,,RESET,0,fresh-start",
        "2026-05-18T20:00:00+00:00,GLD,BUY,36,412.0,d.json,375,521,OPEN,0,",
    ])
    _write_positions(isolated, {"GLD": {"side": "BUY", "quantity": 36, "entry_price": 412.0}})
    assert paper_sim.pending_broker_count() == 0


def test_pending_broker_count_counts_unmirrored_open(isolated):
    """A submitted BUY not yet mirrored into positions.json is in-flight."""
    _write_log(isolated, [
        "2026-05-15T00:31:53+00:00,_RESET_,RESET,0,0,scripts/sync_alpaca_state.py,,,RESET,0,fresh-start",
        "2026-05-18T20:45:00+00:00,GLD,BUY,36,0.0,d.json,375,521,PENDING_BROKER,0,broker_pending order_id=abc",
    ])
    _write_positions(isolated, {})  # not yet mirrored
    assert paper_sim.pending_broker_count() == 1


def test_pending_broker_count_excludes_mirrored_open(isolated):
    """Once the position is mirrored back, the in-flight skew is gone → 0."""
    _write_log(isolated, [
        "2026-05-15T00:31:53+00:00,_RESET_,RESET,0,0,scripts/sync_alpaca_state.py,,,RESET,0,fresh-start",
        "2026-05-18T20:45:00+00:00,GLD,BUY,36,0.0,d.json,375,521,PENDING_BROKER,0,broker_pending order_id=abc",
    ])
    _write_positions(isolated, {"GLD": {"side": "BUY", "quantity": 36, "entry_price": 412.0}})
    assert paper_sim.pending_broker_count() == 0


def test_pending_broker_count_counts_pending_close_still_open(isolated):
    """A submitted CLOSE whose position is still mirrored is in-flight."""
    _write_log(isolated, [
        "2026-05-15T00:31:53+00:00,_RESET_,RESET,0,0,scripts/sync_alpaca_state.py,,,RESET,0,fresh-start",
        "2026-05-26T19:46:30+00:00,NVDA,CLOSE,27,0.0,d.json,,,PENDING_BROKER,0,broker_close_pending order_id=xyz",
    ])
    _write_positions(isolated, {"NVDA": {"side": "BUY", "quantity": 27, "entry_price": 219.5}})
    assert paper_sim.pending_broker_count() == 1


def test_pending_broker_count_ignores_pre_reset(isolated):
    """A PENDING_BROKER row before the latest reset is stale, not in-flight."""
    _write_log(isolated, [
        "2026-05-12T20:45:00+00:00,GLD,BUY,34,0.0,old.json,387,538,PENDING_BROKER,0,broker_pending order_id=old",
        "2026-05-15T00:31:53+00:00,_RESET_,RESET,0,0,scripts/sync_alpaca_state.py,,,RESET,0,fresh-start",
    ])
    _write_positions(isolated, {})
    assert paper_sim.pending_broker_count() == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
