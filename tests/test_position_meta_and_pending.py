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


# ===========================================================================
# Defect 2b — confirm_broker_fills() finalizes PENDING_BROKER breadcrumbs
# ===========================================================================
#
# Without a finalizer, PENDING_BROKER rows accumulated 2026-05-18 → 2026-05-22
# while BROKER_PAPER=alpaca was active and never decayed — pending_broker_count()
# stayed at 7 for weeks, permanently blocking the Guard-1 CB equity write.
# confirm_broker_fills() is the symmetric companion to confirm_moc_fills():
# poll the broker for terminal status, write a terminal mirror-back row,
# update positions.json. See 2026-06-03_eod_stale_data_and_pending_broker_finalizer.md.

@pytest.fixture
def alpaca_mode(monkeypatch):
    monkeypatch.setenv("BROKER_PAPER", "alpaca")


def _read_log_rows(tmp_path: Path) -> list[dict]:
    import csv as _csv
    with (tmp_path / "log.csv").open("r", encoding="utf-8") as f:
        return list(_csv.DictReader(f))


def test_confirm_broker_fills_noop_in_sim_mode(isolated):
    """sim mode → returns empty summary, writes nothing, regardless of breadcrumbs."""
    _write_log(isolated, [
        "2026-05-18T20:45:00+00:00,GLD,BUY,36,0.0,d.json,375,521,PENDING_BROKER,0,broker_pending order_id=abc",
    ])
    _write_positions(isolated, {})
    before_rows = _read_log_rows(isolated)
    summary = paper_sim.confirm_broker_fills()
    assert summary == {"confirmed": [], "rejected": [], "still_pending": []}
    assert _read_log_rows(isolated) == before_rows  # no row written


def test_confirm_broker_fills_open_side_filled(isolated, alpaca_mode, monkeypatch):
    """A PENDING_BROKER BUY whose broker order reports 'filled' → OPEN row
    written, symbol inserted into positions.json, pending count drops to 0."""
    _write_log(isolated, [
        "2026-05-15T00:31:53+00:00,_RESET_,RESET,0,0,scripts/sync_alpaca_state.py,,,RESET,0,fresh-start",
        "2026-05-18T20:45:00+00:00,GLD,BUY,36,0.0,d.json,375,521,PENDING_BROKER,0,broker_pending order_id=abc",
    ])
    _write_positions(isolated, {})

    from lib import broker
    monkeypatch.setattr(broker, "get_order", lambda oid: {
        "id": oid, "status": "FILLED", "filled_avg_price": 412.0419, "filled_qty": 36,
    })

    summary = paper_sim.confirm_broker_fills()
    assert summary["confirmed"] == ["GLD"]
    assert summary["rejected"] == []
    assert summary["still_pending"] == []

    rows = _read_log_rows(isolated)
    open_rows = [r for r in rows if r["status"] == "OPEN" and r["symbol"] == "GLD"]
    assert len(open_rows) == 1
    assert "broker_confirmed" in open_rows[0]["notes"]
    assert "order_id=abc" in open_rows[0]["notes"]
    assert float(open_rows[0]["simulated_price"]) == 412.0419

    pos = json.loads((isolated / "positions.json").read_text())
    assert pos["GLD"]["entry_price"] == 412.0419
    assert pos["GLD"]["quantity"] == 36
    # Stops carried over from the PENDING_BROKER row.
    assert pos["GLD"]["stop_loss"] == 375
    assert pos["GLD"]["take_profit"] == 521

    # pending_broker_count drops because GLD is now mirrored.
    assert paper_sim.pending_broker_count() == 0


def test_confirm_broker_fills_open_side_canceled(isolated, alpaca_mode, monkeypatch):
    """A PENDING_BROKER BUY whose order was canceled → REJECTED row, no position."""
    _write_log(isolated, [
        "2026-05-15T00:31:53+00:00,_RESET_,RESET,0,0,scripts/sync_alpaca_state.py,,,RESET,0,fresh-start",
        "2026-05-18T20:45:00+00:00,XOM,BUY,97,0.0,d.json,142,197,PENDING_BROKER,0,broker_pending order_id=xx",
    ])
    _write_positions(isolated, {})

    from lib import broker
    monkeypatch.setattr(broker, "get_order", lambda oid: {
        "id": oid, "status": "CANCELED", "filled_avg_price": None, "filled_qty": 0,
    })

    summary = paper_sim.confirm_broker_fills()
    assert summary["rejected"] == ["XOM"]
    assert summary["confirmed"] == []

    rows = _read_log_rows(isolated)
    rejected_rows = [r for r in rows if r["status"] == "REJECTED" and r["symbol"] == "XOM"]
    assert len(rejected_rows) == 1
    assert "broker_rejected" in rejected_rows[0]["notes"]
    assert "status=canceled" in rejected_rows[0]["notes"]

    pos = json.loads((isolated / "positions.json").read_text())
    assert "XOM" not in pos
    assert paper_sim.pending_broker_count() == 0


def test_confirm_broker_fills_close_side_filled_with_position(isolated, alpaca_mode, monkeypatch):
    """A CLOSE PENDING_BROKER whose order fills while positions.json still
    has the symbol → CLOSED row with computed PnL, symbol dropped."""
    _write_log(isolated, [
        "2026-05-15T00:31:53+00:00,_RESET_,RESET,0,0,scripts/sync_alpaca_state.py,,,RESET,0,fresh-start",
        "2026-05-26T19:46:30+00:00,NVDA,CLOSE,27,0.0,d.json,,,PENDING_BROKER,0,broker_close_pending order_id=cl",
    ])
    _write_positions(isolated, {
        "NVDA": {"side": "BUY", "quantity": 27, "entry_price": 200.0,
                 "entry_ts": "x", "stop_loss": None, "take_profit": None,
                 "rationale_link": "decisions/.../NVDA.json"},
    })

    from lib import broker
    monkeypatch.setattr(broker, "get_order", lambda oid: {
        "id": oid, "status": "FILLED", "filled_avg_price": 210.0, "filled_qty": 27,
    })

    summary = paper_sim.confirm_broker_fills()
    assert summary["confirmed"] == ["NVDA"]

    rows = _read_log_rows(isolated)
    closed_rows = [r for r in rows if r["status"] == "CLOSED" and r["symbol"] == "NVDA"]
    assert len(closed_rows) == 1
    # PnL = (210 - 200) * 27 * (+1 for BUY closed) = 270
    assert float(closed_rows[0]["realized_pnl"]) == 270.0
    assert "broker_confirmed" in closed_rows[0]["notes"]

    pos = json.loads((isolated / "positions.json").read_text())
    assert "NVDA" not in pos


def test_confirm_broker_fills_close_side_filled_mirror_already_dropped(
    isolated, alpaca_mode, monkeypatch,
):
    """The case actually observed in production: by the time the finalizer
    runs, ``reconcile()`` / ``sync_positions_from_broker()`` has already
    rebuilt positions.json without the symbol. The CLOSED row still gets
    written (so pending count decays) but with realized_pnl=0 and an
    explicit 'already reconciled by mirror' note."""
    _write_log(isolated, [
        "2026-05-15T00:31:53+00:00,_RESET_,RESET,0,0,scripts/sync_alpaca_state.py,,,RESET,0,fresh-start",
        "2026-05-29T19:38:32+00:00,XOM,CLOSE,97,0.0,d.json,,,PENDING_BROKER,0,broker_close_pending order_id=zz",
    ])
    _write_positions(isolated, {})  # mirror dropped it already

    from lib import broker
    monkeypatch.setattr(broker, "get_order", lambda oid: {
        "id": oid, "status": "FILLED", "filled_avg_price": 145.0, "filled_qty": 97,
    })

    summary = paper_sim.confirm_broker_fills()
    assert summary["confirmed"] == ["XOM"]

    rows = _read_log_rows(isolated)
    closed_rows = [r for r in rows if r["status"] == "CLOSED" and r["symbol"] == "XOM"]
    assert len(closed_rows) == 1
    assert float(closed_rows[0]["realized_pnl"]) == 0.0
    assert "already reconciled by mirror" in closed_rows[0]["notes"]


def test_confirm_broker_fills_is_idempotent(isolated, alpaca_mode, monkeypatch):
    """Second call must be a no-op: the broker_confirmed/broker_rejected
    marker in the first run's appended row excludes the order from re-processing."""
    _write_log(isolated, [
        "2026-05-15T00:31:53+00:00,_RESET_,RESET,0,0,scripts/sync_alpaca_state.py,,,RESET,0,fresh-start",
        "2026-05-18T20:45:00+00:00,GLD,BUY,36,0.0,d.json,375,521,PENDING_BROKER,0,broker_pending order_id=abc",
    ])
    _write_positions(isolated, {})

    from lib import broker
    monkeypatch.setattr(broker, "get_order", lambda oid: {
        "id": oid, "status": "FILLED", "filled_avg_price": 412.0419, "filled_qty": 36,
    })

    first = paper_sim.confirm_broker_fills()
    assert first["confirmed"] == ["GLD"]
    rows_after_first = _read_log_rows(isolated)

    second = paper_sim.confirm_broker_fills()
    assert second == {"confirmed": [], "rejected": [], "still_pending": []}
    assert _read_log_rows(isolated) == rows_after_first  # no new row


def test_confirm_broker_fills_still_pending(isolated, alpaca_mode, monkeypatch):
    """A non-terminal status leaves the breadcrumb row alone and reports the symbol."""
    _write_log(isolated, [
        "2026-05-15T00:31:53+00:00,_RESET_,RESET,0,0,scripts/sync_alpaca_state.py,,,RESET,0,fresh-start",
        "2026-05-18T20:45:00+00:00,GLD,BUY,36,0.0,d.json,375,521,PENDING_BROKER,0,broker_pending order_id=qq",
    ])
    _write_positions(isolated, {})

    from lib import broker
    monkeypatch.setattr(broker, "get_order", lambda oid: {
        "id": oid, "status": "ACCEPTED", "filled_avg_price": None, "filled_qty": 0,
    })

    summary = paper_sim.confirm_broker_fills()
    assert summary["still_pending"] == ["GLD"]
    assert summary["confirmed"] == [] and summary["rejected"] == []
    assert paper_sim.pending_broker_count() == 1


def test_confirm_broker_fills_ignores_pre_reset_rows(isolated, alpaca_mode, monkeypatch):
    """A PENDING_BROKER row before the latest reset is stale — must not be
    re-queried at the broker (the order may be long gone)."""
    _write_log(isolated, [
        "2026-05-12T20:45:00+00:00,GLD,BUY,34,0.0,old.json,387,538,PENDING_BROKER,0,broker_pending order_id=old",
        "2026-05-15T00:31:53+00:00,_RESET_,RESET,0,0,scripts/sync_alpaca_state.py,,,RESET,0,fresh-start",
    ])
    _write_positions(isolated, {})

    from lib import broker
    calls = []

    def _spy(oid):  # would raise if called
        calls.append(oid)
        return {"id": oid, "status": "FILLED", "filled_avg_price": 0.0, "filled_qty": 0}
    monkeypatch.setattr(broker, "get_order", _spy)

    summary = paper_sim.confirm_broker_fills()
    assert summary == {"confirmed": [], "rejected": [], "still_pending": []}
    assert calls == []  # pre-reset row not queried


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
