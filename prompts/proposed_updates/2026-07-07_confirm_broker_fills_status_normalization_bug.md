# Proposed update — `confirm_broker_fills()` status-string normalization bug

**Author:** Claude (assistant), orchestrator during EOD 2026-07-07
**Date:** 2026-07-07
**Status:** DRAFT — awaiting human PR review. No protected/lib file edited; no trade placed.
**Scope:** `lib/paper_sim.py` (one function). PR-locked; this memo proposes, does not implement.

## Reason

The `PENDING_BROKER` finalizer proposed on 2026-06-03 (`confirm_broker_fills()`)
was implemented, but the first time it was actually run against real stale rows
(EOD 2026-07-07) it resolved **nothing**: `{"confirmed": [], "rejected": [],
"still_pending": [all 12 rows]}`, and `pending_broker_count()` stayed at 4.

### Root cause
`lib/broker.get_order()` returns `status = str(o.status)`, and alpaca-py's
`OrderStatus` enum stringifies as **`"OrderStatus.FILLED"`** (name form), not
its value `"filled"`. Inside `confirm_broker_fills()`:

```python
status = (o.get("status") or "").lower()      # -> "orderstatus.filled"
if status == "filled" and price is not None:  # FALSE
    ...
elif status in ("rejected","canceled","cancelled","expired"):  # FALSE
    ...
else:
    summary["still_pending"].append(symbol)   # <-- everything lands here
```

So every terminal order (verified: all 12 post-reset order_ids return
`OrderStatus.FILLED` with a valid `filled_avg_price`) is mis-classified as
`still_pending`. The finalizer can never decay `pending_broker_count()` against
this broker's status format. Consequence: CB equity writes and safe
`reconcile()` have been disabled by Guard-1 since ~2026-06-11 and this "cleanup"
cannot lift the suppression.

Note the same enum-name form already appears verbatim in historical log `notes`
(`status=OrderStatus.FILLED`), confirming `get_order()` has always returned the
name form — the finalizer's `== "filled"` check was never satisfiable here.

## Proposed fix (one line, `lib/paper_sim.py > confirm_broker_fills`)

Normalize the status to its bare token before comparison:

```python
raw = str(o.get("status") or "")
status = raw.lower().split(".")[-1]   # "OrderStatus.FILLED" -> "filled"
```

This makes both the `== "filled"` and the reject-set checks fire correctly while
remaining safe for a broker that already returns the value form (`"filled"`
`.split(".")[-1]` == `"filled"`). Consider applying the same normalization in
`confirm_moc_fills()` if it shares the comparison, and/or normalizing once inside
`lib/broker.get_order()` itself so downstream callers see a canonical status.

## Verification requested (pre-merge)

Because this fix will let `confirm_broker_fills()` finally mutate `positions.json`,
review the replay carefully. Traced by hand on the current post-reset log the
sequence is self-correcting (transient GLD/CSCO/XOM/NVDA BUY inserts are removed
by their matching CLOSE rows; the 4 real positions have no pending CLOSE rows and
are left untouched), so a corrected run should leave `positions.json` = {GOOGL,
JNJ, SPY, UNH} and drop `pending_broker_count()` to 0. **Still — run it once with
`positions.json` backed up**, and independently note that `reconcile()` must NOT
be run while `broker.get_positions()` is empty regardless of this fix (see
2026-05-26 `alpaca_mirror_state_integrity` draft for the reconcile-guard proposal;
both are needed).
