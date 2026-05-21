"""Read repo configs. Single source of truth for which file maps to which dict."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = REPO_ROOT / "config"


class ConfigError(RuntimeError):
    """Raised when a config file violates a runtime invariant (e.g. a blocked
    symbol also present in the trading allowlist)."""


class ComplianceError(RuntimeError):
    """Raised when code attempts to act on a symbol that compliance forbids.

    Used by deterministic chokepoints (signal generation, paper-sim, broker)
    so a blocked symbol can never reach a position-state change, regardless
    of which mode the bot is in.
    """


def _load_yaml(name: str) -> dict[str, Any]:
    path = CONFIG_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"missing config: {path}")
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def watchlist() -> dict[str, Any]:
    wl = _load_yaml("watchlist.yaml")
    validate_watchlist_invariants(wl)
    return wl


def blocked_symbols() -> list[dict[str, Any]]:
    """Return the compliance blocklist (employer/regulatory restrictions).

    Empty list when the optional `blocked_symbols` key is absent. Reading
    from this function (rather than from `watchlist()["blocked_symbols"]`
    directly) is the supported API.
    """
    return list(_load_yaml("watchlist.yaml").get("blocked_symbols") or [])


def is_symbol_blocked(symbol: str) -> bool:
    """True if `symbol` is on the compliance blocklist (case-insensitive)."""
    if not symbol:
        return False
    target = symbol.upper()
    return any(entry.get("symbol", "").upper() == target for entry in blocked_symbols())


def validate_watchlist_invariants(wl: dict[str, Any]) -> None:
    """Raise ConfigError if the watchlist violates a cross-section invariant.

    Currently enforces: a symbol on `blocked_symbols[]` must not also appear
    in `symbols[]` (the trading allowlist). Without this check, a compliance-
    blocked symbol could be silently re-approved by an accidental allowlist edit.
    """
    blocked = {entry.get("symbol", "").upper()
               for entry in (wl.get("blocked_symbols") or [])}
    if not blocked:
        return
    allowlisted = {s.get("symbol", "").upper() for s in (wl.get("symbols") or [])}
    overlap = sorted(blocked & allowlisted)
    if overlap:
        raise ConfigError(
            f"compliance violation: symbols on blocked_symbols[] cannot appear "
            f"in symbols[]: {overlap}. Remove from symbols[] or remove from "
            f"blocked_symbols[] via human-reviewed PR."
        )


def risk_limits() -> dict[str, Any]:
    return _load_yaml("risk_limits.yaml")


def strategy_rules() -> dict[str, Any]:
    return _load_yaml("strategy_rules.yaml")


def routine_schedule() -> dict[str, Any]:
    return _load_yaml("routine_schedule.yaml")


def approved_modes() -> dict[str, Any]:
    return _load_yaml("approved_modes.yaml")


def current_mode() -> str:
    return approved_modes()["mode"]


def is_symbol_approved(symbol: str, action: str = "paper_trading") -> bool:
    """Return True if symbol is in watchlist with the requested approved_for_<action> flag."""
    flag = f"approved_for_{action}"
    for s in watchlist().get("symbols", []):
        if s["symbol"].upper() == symbol.upper():
            return bool(s.get(flag, False))
    return False
