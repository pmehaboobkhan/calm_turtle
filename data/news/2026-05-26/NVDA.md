# News & Sentiment — NVDA (pending-order conflict symbol)

> Look-back: last 24h + most recent material event. Pre-market 2026-05-26 (live regular session; data-as-of 2026-05-22 close — 05-25 was Memorial Day).
> NVDA is NOT held. A `PENDING_BROKER` BUY order for 27 shares (order_id 14d3ade1…, submitted 2026-05-22 EOD) is queued to fill at the 05-26 open, but the deterministic engine has since flipped NVDA to EXIT. This file documents the news context behind that rank decay. Pre-market flags the conflict only; resolution is an EOD decision.

## NVDA — `mixed/soft`
- **Source:** CNBC NVDA Q1 FY27 earnings — https://www.cnbc.com/2026/05/20/nvidia-nvda-q1-fy27-earnings.html ; Reuters H200/China — https://www.reuters.com/technology/nvidia-h200-china-2026-05-15/ ; Google Finance NVDA — https://www.google.com/finance/quote/NVDA:NASDAQ
- **Timestamp:** Most recent material events 2026-05-20 (earnings) and 2026-05-15 (China headline); carried into the 05-26 open with no new weekend headline.
- **Summary:** NVDA reported Q1 FY27 on **2026-05-20**: headline **beat**, but the stock **fell (~2%)** on the print — the fourth straight beat-and-fade reaction, consistent with a high-expectations name where in-line guidance no longer satisfies. Separately, a **−4.6% selloff on 2026-05-15** tied to H200/China export-licensing uncertainty. Last close 2026-05-22 **$215.33 (−1.90%)**, intraday low $214.80 on heavy volume (~168M shares).
- **Tone:** `mixed/soft`. The price action confirms the deterministic signal: NVDA's 126d momentum has decayed to **+15.46%**, ranking it **9/21** — out of both the top-5 entry band and the top-7 hold-zone buffer → **EXIT**.

## Pending-order vs EXIT-signal conflict (flag only — no decision in pre-market)
- A live `PENDING_BROKER` BUY for **27 NVDA shares** was submitted at the **2026-05-22 EOD** (`decisions/2026-05-22/1641_NVDA.json`, order_id `14d3ade1-38db-4605-a93c-c88481ce5a53`, sim basis ~$219.51 = the 05-21 close used at submission). It is queued to fill at the **05-26 open**.
- Between submission and now, NVDA dropped rank 5 → 9 and the engine flipped it ENTRY → **EXIT** (`data/market/2026-05-26/1036_signals.json`). `positions.json` shows only 5 held names — **NVDA has not yet filled**.
- This is a genuine stale-order conflict the **EOD routine** must resolve: most likely **cancel the queued buy** (if still unfilled) or **close immediately** (if it filled at the open into an already-EXIT name). Pre-market makes **no decision** — capital preservation, when uncertain NO_TRADE.

## Connector status
News connector AVAILABLE this run (cited results carried from the prior-session search; no new weekend headlines). Coverage is headline-level (free web), not a paid newswire — treat as context, not precision. No `news_unavailable` flag for NVDA this run.
