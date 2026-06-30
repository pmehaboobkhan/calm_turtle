# Risk Event — Stop-Breach Observation (XOM)

- **Timestamp (UTC):** 2026-06-30T19:37:35Z
- **Routine:** pre_close (monitoring; does NOT open/close positions)
- **Mode:** PAPER_TRADING
- **Severity:** ELEVATED (observation only — no auto-action in v1)

## What happened

The deterministic health check (`lib.portfolio_health.assess_positions`) flagged **XOM** with `stop_breached: True` at the 15:37 ET pre-close mark:

- XOM: last **136.61** vs per-position stop **136.84** — **BELOW stop** (−10.13% vs entry 152.0058; MtM −$400.29 on 26 shares).
- Invalidation trigger: `stop_loss breached: BUY entered at 152.0058, stop=136.8400, current=136.6100`.

`lib.portfolio_health.positions_to_close(quotes)` → **[XOM]** (the only `should_close()` flag).

## Why no forced close was taken

Consistent with the documented v1 design (see `journals/daily/2026-06-11.md` and
`logs/risk_events/2026-06-11_203801_stop_breach_observation.md`):

- **v1 has no forced-close-on-stop path.** The deterministic momentum engine holds
  positions through per-position stop breaches; the **portfolio circuit-breaker
  (8% HALF / 12% OUT) is the true loss-limit.**
- pre_close is a **monitoring routine** — it never opens positions and only
  closes on confirmed material overnight risk routed through the gates. A
  mechanical stop breach is recorded here as an observation; the **end_of_day
  routine** is the only routine that decides close/re-rank actions against
  closing prices.
- XOM momentum thesis (Strategy B, energy momentum) was rank 2–3 at last
  deterministic regime call; next earnings confirmed **2026-07-31** (outside any
  overnight window). The EOD routine will re-evaluate XOM against the close and
  the re-ranked Strategy-B basket.

## Watch / carry-forward

- **XOM** below its per-position stop at pre-close — EOD must decide whether to
  re-rank/exit on close prices.
- **CSCO** last 117.58 vs stop 117.00 — **0.50% above stop, NOT breached** but
  the closest of the book; monitor for a close-price breach at EOD.
- Portfolio CB remains FULL, DD ~0.49% off peak $100,792.58 — far from the 8%
  HALF trigger; the loss-limit is not engaged.

No URGENT alert (portfolio CB did not transition). Flagged ELEVATED for EOD attention.
