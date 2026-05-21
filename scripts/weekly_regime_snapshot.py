"""Print a Markov regime diagnostic block for a symbol (default SPY).

Designed to be appended to the weekly journal as a sanity-check section. The
output is markdown — pipe it into the journal or read it stand-alone.

Usage:
    python3 scripts/weekly_regime_snapshot.py             # SPY, ~2y window
    python3 scripts/weekly_regime_snapshot.py --symbol GLD --limit 520

The walk-forward backtest of this method scored Sharpe ~0.24 on SPY — well
below the 0.8 portfolio target — so this script does NOT emit a trading
signal. It surfaces transition persistence + stationary mix so the human
reviewer can flag regime shifts the deterministic 10-month SMA might lag.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib import data, regime_markov  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--symbol", default="SPY")
    parser.add_argument(
        "--limit",
        type=int,
        default=520,
        help="Number of daily bars to pull (~2 years at 520). Default 520.",
    )
    parser.add_argument("--window", type=int, default=20)
    args = parser.parse_args()

    bars = data.get_bars(args.symbol, timeframe="1Day", limit=args.limit)
    if not bars:
        print(f"# Markov regime diagnostic — {args.symbol}\n\nNo bars returned.")
        return 1
    closes = [float(b["close"]) for b in bars]
    snapshot = regime_markov.regime_snapshot(closes, window=args.window)
    print(regime_markov.format_snapshot_markdown(snapshot, symbol=args.symbol))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
