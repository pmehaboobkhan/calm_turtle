# Symbol Profile — GLD

> Descriptive observations only. No advice, no forward recommendations. Append-only per period.

## Week 2026-W20 observations
- Strategy: dual_momentum_taa (Strategy A), which subsumed gold_permanent_overlay (Strategy C) for the duration. Entry 2026-05-12 @ $430.7861 (34 sh). Held 2026-05-12 → 2026-05-15. Reset-terminated 2026-05-15T00:31:53Z (no signal invalidation).
- Strategy A top-1 risk asset by 12m return (≈ +38.5% at entry). Above the 210d MA at all points during the hold.
- 12m return faded ≈ −4pp per week over the window (≈ +42.56% → +38.50%) while SPY was closing the gap; GLD still comfortably ahead of SPY/IEF on the 12m-return rank at every observation.
- Permanent overlay (Strategy C) stayed subsumed by the Strategy A GLD line for the full window; no standalone overlay action was required while Strategy A held GLD. After the 2026-05-15 reset, the subsumption question became administratively moot.
- Most stable position intraday; mark stayed within ≈ −$94 to +$30 against the position over the window, well clear of the −10% stop ($387.63; 9.4%–10.0% headroom observed). Commodity-gold diversifier behavior consistent with the thesis.
- 2026-05-15 EOD: under the total data blackout, only the data-free gold_permanent_overlay ENTRY signal could fire (NO_TRADE on the data-staleness hard gate).

## Week 2026-W21 observations
- Strategy: dual_momentum_taa (Strategy A) top-1 risk asset, subsuming gold_permanent_overlay (Strategy C). PAPER_BUY submitted 2026-05-18 @ ref $417.29, filled 2026-05-19 open @ $412.0419 (−$5.25/sh favorable slip — the largest favorable slip of the cohort), 36 sh. Held all week; carried over the Memorial Day weekend into 2026-05-26 (still open).
- Maintained the 12m-return lead over both SPY and IEF at every observation (12m ~+42.34% at entry, fading toward ~the high-30s%/+26.72% SPY by 2026-05-22; GLD still comfortably top-1). The W20-observed ~−4pp/week 12m-return decay vs a rising SPY continued; GLD remained above its 210d/10m MA throughout. Descriptive — the rotation-vs-noise question is still open.
- IEF stayed below its 10m MA all week (only ~+3.89%, ~matching cash), so the dual-momentum cash floor was NOT active; GLD held the top risk-asset slot uncontested.
- Most stable line in the book again this week (commodity-gold diversifier behavior consistent with the thesis); did not approach the −10% stop ($375.561).
- Stop/target fields recorded as null on the position all week under the alpaca-mirror reconcile; descriptive standing observation.

## Week 2026-W22 observations
- Strategy: dual_momentum_taa (Strategy A, TAA top-1) subsuming gold_permanent_overlay (Strategy C). Carried 36 sh from the W21 entry @ $412.0419 into the W22 window (holiday Mon 2026-05-25).
- Closed 2026-05-29 pre_close @ $418.02. Realized PnL: +$215 (+1.45% vs entry). Closed by the all-positions daily-loss halt, NOT by a stop or rotation signal.
- TAA top-1 maintained all week (12m momentum still leading SPY and IEF; GLD above its 10mo MA throughout).
- The crisis-hedge thesis was intact at exit: gold moved inversely to equities during the energy-led selloff — GLD was modestly positive while XOM/GOOGL/UNH were negative on both loss days.
- 2026-05-29 specifically: midday mark $419.22 (+$258 unrealized, +1.74%) while the portfolio was in daily-loss-halt mode — the hedge was working as designed at the moment it was liquidated.
- Open policy question flagged this cycle (descriptive, no recommendation): GLD as the permanent overlay was the only genuinely defensive asset in the book during the macro shock, yet the all-positions daily-loss halt closed it alongside the loss names. Whether a permanent-overlay exemption from the halt is warranted is recorded here as an observation for future review; v1 makes no proposal.
