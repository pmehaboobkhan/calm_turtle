# Risk Event — Stale Data / Market Closed (market_open routine)

- **Timestamp (UTC):** 2026-05-25T13:37:49Z
- **Routine:** `market_open` (monitoring only)
- **Mode:** PAPER_TRADING (`BROKER_PAPER=alpaca`)
- **Severity:** Non-urgent (no transition, no loss, no live exposure). Logged because CLAUDE.md rule #5 requires a `logs/risk_events/` entry whenever data is stale.
- **Disposition:** NO ACTION. No closes, no circuit-breaker write, no notify. Routine recorded as no-op.

## What happened

`market_open` ran on **2026-05-25, which is US Memorial Day — equity markets are CLOSED.**
There is no market open today, therefore no real opening prints, no overnight-gap
detection possible, and no valid prices to evaluate stops/take-profits against.

Confirmation from two independent sources:

1. **Market status flag.** `data/market/2026-05-25/1042.json > market_status = "CLOSED_HOLIDAY_MemorialDay"`.
   The pre-market report (`reports/pre_market/2026-05-25.md`) and today's journal
   both state the next session is **Tuesday 2026-05-26**.

2. **Quote staleness.** `lib.data.get_latest_quote` for all 5 open positions returns
   `quote_ts = 2026-05-22T20:00 UTC` (the last completed session, Friday) while
   `fetched_ts ≈ 2026-05-25T13:37 UTC`.

   | Metric | Value |
   |---|---|
   | `max_data_staleness_seconds` (risk_limits) | 60 |
   | Observed quote age | 236,246 s (~2.73 days) |
   | Exceeds limit by | ~3,937× |

   The stale ticks are additionally **degenerate** — several are crossed/one-sided
   (e.g. GOOGL `last_price` 406.80 vs `bid` 367.84; XOM `last` 162.33 vs `bid` 146.35;
   CSCO/UNH `ask` 0.0). These are unreliable holiday quotes, not a real market open.

## Why no action was taken

Per CLAUDE.md:
- **Safety rule #5:** stale data beyond the staleness limit → produce `NO_TRADE`
  decisions and stamp the staleness. (Applied: zero closes proposed.)
- **Handling missing data:** any missing/stale input is a reason to be *more*
  conservative, never less.
- **Step 6 (circuit-breaker refresh) deliberately SKIPPED.** Marking portfolio
  equity to these stale, partially-crossed quotes would corrupt the circuit-breaker
  peak/drawdown record and could fabricate a false invalidation. The circuit-breaker
  state file was **left untouched** (last good = `FULL`, peak $104,090.72, last
  observed $101,510.01 as of 2026-05-22).
- **Step 7 (health-check / PAPER_CLOSE proposals) SKIPPED.** A close triggered off a
  stale/degenerate price is exactly the false-signal capital destruction these rules
  guard against. EXITs are never throttled — but there is no *real* invalidation to
  act on, only stale data. When uncertain, NO_TRADE.

## Open positions at time of event (reference only — values are STALE 05-22 closes)

CSCO, GLD, GOOGL, UNH, XOM (5 positions). All carried ENTRY signals on the
2026-05-22 evaluation → continue-to-hold; none near its strategy-default stop as of
that last good evaluation. No blocked symbols held (INTU not in book).

## Follow-up

- No follow-up required for the holiday itself. The next deterministic evaluation and
  any circuit-breaker refresh run at the **2026-05-26 (Tuesday)** session, where fresh
  bars must be re-pulled and freshness re-checked before any mark-to-market or close.
- If `market_open` is scheduled on future US market holidays, the routine should detect
  `market_status == CLOSED_*` and exit as a no-op before fetching quotes — consider a
  prompt/scheduler note (proposal only; not changed here).

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
