# Risk Event — Pending-Broker Suppression NOT Cleared + Reconcile-Would-Wipe Hazard (EOD 2026-07-07)

- **Timestamp:** 2026-07-07T20:49:50Z (16:49 ET)
- **Routine:** end_of_day
- **Severity:** HIGH (state-integrity hazard; caught and avoided — NO capital impact, positions intact)
- **Mode:** PAPER_TRADING · BROKER_PAPER=alpaca

## Summary
Today's EOD was tasked with finally clearing the standing 4 stuck `PENDING_BROKER` log rows (since ~2026-06-11) by running `lib.paper_sim.confirm_broker_fills()` before the circuit-breaker refresh and `reconcile()`. **`confirm_broker_fills()` did NOT resolve the rows** — a status-string mismatch bug prevents it from recognizing filled orders. `pending_broker_count()` remains **4**. Combined with an intermittently-empty broker filled-position view, this means `reconcile()` (alpaca-authoritative) would have wiped `trades/paper/positions.json` to `{}` — the exact incident that hit at midday today. Destructive reconcile was therefore SKIPPED and positions were carried forward.

## Evidence

### 1. `confirm_broker_fills()` is a no-op due to a status-format bug (NEW finding)
- Ran `confirm_broker_fills()`; summary = `{"confirmed": [], "rejected": [], "still_pending": [GLD, CSCO, XOM, UNH, NVDA, GLD, SPY, GOOGL, JNJ, CSCO, NVDA, XOM]}`.
- `pending_broker_count()`: 4 before → **4 after** (no change). `positions.json` unchanged (the correct 4: GOOGL, JNJ, SPY, UNH) — non-destructive, but no progress.
- Root cause: `lib/broker.get_order()` returns `status = str(o.status)` = **`"OrderStatus.FILLED"`**. `confirm_broker_fills()` computes `status = o.get("status").lower()` = `"orderstatus.filled"` and tests `if status == "filled"` (and `in ("rejected","canceled","cancelled","expired")`). Neither matches, so every terminal order falls through to the `else` branch and is (mis)classified `still_pending`. Verified directly: `broker.get_order()` for all 12 post-reset pending order_ids returns `OrderStatus.FILLED` with valid `filled_avg_price`, yet none are recognized.
- Net effect: the finalizer built to decay `pending_broker_count()` toward 0 cannot fire against this broker's status format. The suppression that has disabled CB equity writes and safe reconcile since ~06-11 remains in place.
- **Proposed fix (human PR — NOT applied here; lib/ is not an orchestrator write path):** normalize the status in `confirm_broker_fills()` before comparison, e.g. `status = str(o.get("status") or "").lower().split(".")[-1]` (or map the alpaca enum), so `"OrderStatus.FILLED"` -> `"filled"`. A matching draft will be filed under `prompts/proposed_updates/`.

### 2. `reconcile()` would have wiped positions.json (hazard avoided)
- `broker.get_positions()` returned **`[]`** (empty) at EOD; `account_snapshot()` equity == cash == $66,627.55 (filled-position view empty — flapping: pre_close today it briefly showed 4). Local `positions.json` holds 4 real positions.
- In alpaca mode `reconcile()` calls `sync_positions_from_broker()`, which overwrites `positions.json` from `broker.get_positions()`. With the broker view empty, that overwrite is `{}` — a full wipe (identical to the midday 2026-07-07 incident).
- **Action:** `reconcile()` was NOT called. Verified via dry-check (`broker.get_positions()` empty vs 4 real local positions) exactly as the operator instruction prescribed. Positions carried forward unchanged.

### 3. Step 8a Alpaca-mirror reconciliation — DIVERGENCE (expected artifact)
- `only_local = [GOOGL, JNJ, SPY, UNH]`, `only_broker = []`, `qty_mismatch = []`.
- This is the KNOWN pending-broker-window artifact, not genuine ledger drift: `broker.get_order()` confirms all 4 BUY orders FILLED at the correct entry prices matching `positions.json`; only the aggregate `get_positions()` view is (intermittently) empty.
- **The operator remedy `scripts/sync_alpaca_state.py --reset-fresh-start` is NOT appropriate here** — it would set local state to the broker's transiently-empty view, i.e. wipe the 4 real positions. Deliberately not run.

## Disposition
- Positions.json intact and correct (GOOGL 16, JNJ 26, SPY 20, UNH 15) — verified before and after every step this run.
- Circuit-breaker refresh SKIPPED per Guard 1 (`pending_broker_count() = 4`); prior state FULL (peak $100,792.58) carried forward. No transition, no CB risk event.
- This is the "guard-fix" scenario (pending-broker artifact), NOT a genuine reconciliation failure of a corrupted ledger, so the routine finalizes journaling + audit + commit rather than hard-halting — the ledger is demonstrably intact.
- **Blocking dependency:** until `confirm_broker_fills()` is fixed (human PR) OR the operator manually finalizes the stale rows, CB equity writes and safe `reconcile()` remain disabled. This has now stood ~26 days. Escalated URGENT via Telegram.
