# Weekly Learning Review — 2026-W28 (July 6–10, 2026)
# Review Date: 2026-07-11

> Prepared by: weekly_review orchestrator
> Mode: `PAPER_TRADING` (not SAFE_MODE — learning writes permitted)
> Template: §21N (consistent with W21–W23, W27 learning reviews)
> `max_self_learning_proposals_per_cycle = 0` (`config/risk_limits.yaml`, v1 observations-only) → No `prompts/proposed_updates/` files written this cycle.
> **Continuity note:** no gap this cycle — the last weekly_review (W27) covered through 2026-07-03; this review covers the immediately following week (W28, 2026-07-06 → 2026-07-10) with all 5 daily journals present.

---

## 1. Period Summary

**Trading days:** 5 full sessions (2026-07-06 Mon → 2026-07-10 Fri). 07-06 and 07-10 ran pre_market/market_open/midday/pre_close but produced **no EOD close section** (so no `memory/prediction_reviews/2026-07-06.md` or `2026-07-10.md`); 07-07, 07-08, 07-09 had complete EOD reviews.
**End-of-week state:** 4 open positions (SPY, GOOGL, JNJ, UNH), unchanged in composition all week; unrealized ≈ +$1,456 (indicative — JNJ/UNH marks carry wide-late-day-spread low confidence); broker equity $100,480.52 (07-10 pre_close, authoritative).
**Period return:** −0.020% (07-03 EOD $100,501.15 → 07-10 pre_close $100,480.52) — a pure mark-to-market drift week, no trading activity.
**Daily-loss events:** 0.
**Closed trades:** 0 this week (last closes remain the 3 from 2026-07-01); 4 all-time post-06-04-reset (unchanged from W27).
**Open predictions resolved this cycle:** ~15 (≈13–14 operational, 1 market-outcome, 1 falsified) — see §2.
**New predictions pending:** carried NVDA/CSCO/XOM reclaim-durability (now 2nd week deferred), plus routine within-week operational predictions rolling to 2026-07-13+.

**Dominant events:** (1) Zero trading activity — every session's health check returned no closes and the daily-bar feed staleness blocked every entry, extending the no-new-entry streak to its **5th+ consecutive reviewed week** (07-08 was in fact a *total* daily-bar load failure, not just staleness). (2) The circuit breaker received its **first fresh equity write since ~2026-06-11** via an authoritative-broker-equity bypass at 07-10 pre_close — a workaround, not a fix, since the 4-stuck-pending-broker-row root cause is unchanged. (3) A 07-07 midday `reconcile()` call briefly wiped `positions.json` to empty (broker mirror was transiently empty during the pending-broker window); caught and reverted with zero capital impact, but the step still lacks a guard. (4) A genuine Compliance/Safety **REJECTION** fired at 07-10 pre_market over an apparent phantom "TLT EXIT" signal; investigation determined the rejected version was the non-canonical artifact (an incomplete bars fetch had dropped a legitimate universe member, TLT), the canonical on-disk JSON was correct, and the routine was re-approved — harmless in outcome, but it surfaced a real process gap (a cited JSON snapshot was overwritten in place rather than written once).

---

## 2. Prediction Reconciliation (Full Detail)

### Predictions with a resolution window inside this week

| Prediction | Source | Confidence | Outcome | Notes |
|---|---|---|---|---|
| GOOGL holds above $331.68 stop through 07-06 | Carried from W27 (07-01/07-02 EOD) | 0.6 | **CORRECT** | Marks $354–368 all week, +6.8–10.9% above stop, never near breach; the only genuine market-outcome prediction this cycle |
| Fresh daily bars arrive by 07-06 | Carried from W27 (07-02 EOD) | uncertain (no numeric) | **FALSIFIED** | Feed stayed down all 5 sessions; 07-08 was a total load failure (`SSLError`), qualitatively worse than the prior "stale but present" pattern |
| GLD reclaims 210d MA / overlay unblocks | Carried from W27 (low confidence) | low | Overlay **stayed blocked** (observable base case held); MA reclaim itself **unverifiable** on stale data | 07-07 GLD NO_TRADE (`decisions/2026-07-07/1649_GLD.json`), all indicators null |
| Pending-broker count stays 4 | 07-07→08, 07-08→09, 07-09→10 (×3) | 0.9 | **6/6 CONFIRMED** (paired with CB-stays-FULL below) | High base-rate operational prediction |
| CB stays FULL | 07-07→08, 07-08→09, 07-09→10 (×3) | 0.9 | **CONFIRMED** each time | Same underlying cause |
| No destructive reconcile while broker view empty/flapping | 07-07→08 | 0.85 | **PARTIAL** — hazard dormant (broker view populated 07-08, reconcile clean 4/4); standing hazard re-affirmed, not resolved | The midday incident on 07-07 itself was the hazard materializing once; 08-onward it stayed dormant |
| Daily-bar feed still broken next session | 07-07→08, 07-08→09, 07-09→10 (×3) | 0.8 | **3/3 CONFIRMED** | |
| Post-close IEX basis-gap (~$1,295, 07-09) is a feed artifact, not real MTM | 07-09→10 | 0.75 | **CONFIRMED** | 07-10 reconcile clean, 0 discrepancies, account equity authoritative |
| 4 holds stay above stops | 07-07→08, 07-08→09, 07-09→10 | 0.6–0.65 | **CONFIRMED**, none breached | JNJ approached but did not reach its +25% take-profit |

### Predictions still open at end of W28 (resolve 2026-07-13+)

| # | Prediction | Confidence | Notes |
|---|-----------|-----------|-------|
| 1 | NVDA/CSCO/XOM 07-01 stop exits prove durable | n/a (deferred, 2nd consecutive week, no fresh close since the streak began) | Rolls to 07-13; `decisions/by_symbol/{CSCO,NVDA,XOM}.md` marked UNRESOLVED/DEFERRED again |
| 2 | Fresh daily bars arrive by 07-13 | uncertain (5th+ week of failure) | Highest-priority operational watch item, escalating |
| 3 | GLD reclaims its 210d MA and unblocks the overlay | low | No near-term catalyst identified |
| 4 | The 07-10 pre_close CB authoritative-equity bypass becomes a durable pattern (vs. a one-off) | n/a (observational) | Watch whether subsequent routines repeat it |
| 5 | JNJ reaches its +25% take-profit before its 07-15 earnings | n/a (price-path dependent) | Was ~+18–20% most of the week; earnings caution window opens 07-14 pre_close |

---

## 3. Recurring Mistakes

### Mistake #1 (MUST-FIX, recurring, 5th+ consecutive week): daily-bar feed staleness blocked all entries again

**Pattern:** Every W28 session evaluated signals on daily bars anchored to ~2026-06-23 or, on 07-08, failed to load at all (`SSLError`, yfinance TLS-blocked via the proxy; Alpaca free-IEX fallback lagging 11–16 trading days on the other 4 days). Rule #5 correctly refused every fresh ENTRY signal all week — the only decision file written, `decisions/2026-07-07/1649_GLD.json`, is a NO_TRADE on exactly this ground.

**Evidence:** `journals/daily/2026-07-06.md` through `2026-07-10.md`, each pre-market/EOD section; `journals/daily/2026-07-10.md` labels it the "7th consecutive session pattern."

**Root cause:** unchanged from W27 — infrastructure, not strategy or model behavior.

**Already-open candidate fix (do NOT duplicate):** `prompts/proposed_updates/2026-06-03_eod_stale_data_and_pending_broker_finalizer.md`. Still unresolved, 5th+ week running.

### Mistake #2 (MUST-FIX, recurring, with a new wrinkle this week): circuit-breaker persistence

**Pattern:** `trades/paper/circuit_breaker.json` stayed frozen at `updated_at: 2026-06-11` through 07-06 → 07-10 midday, suppressed every routine by Guard 1 (`pending_broker_count() == 4`). On 07-07 EOD, `confirm_broker_fills()` was run specifically to clear the backlog and could not — a **newly discovered root cause**: `broker.get_order()` returns the literal string `"OrderStatus.FILLED"`, and the finalizer's lowercased `== "filled"` comparison never matches, so every terminal order is permanently mis-classified `still_pending`. On 07-10 pre_close, the routine bypassed the guard using authoritative broker `account_snapshot` equity directly and wrote the **first fresh CB mark since ~06-11** (`circuit_breaker.json` `updated_at: 2026-07-10T19:35:44Z`) — but this does not clear the 4 stuck rows or un-freeze `peak_equity` ($100,792.58, unchanged).

**Evidence:** `journals/daily/2026-07-06.md` through `2026-07-10.md` (CB sections); `logs/risk_events/2026-07-07_204950_pending_broker_mirror.md`; `trades/paper/circuit_breaker.json`.

**Already-open candidate fixes (do NOT duplicate):** `prompts/proposed_updates/2026-06-03_eod_stale_data_and_pending_broker_finalizer.md` and `prompts/proposed_updates/2026-07-07_confirm_broker_fills_status_normalization_bug.md`. Both still unresolved.

### Mistake #3 (NEW this week, N=1, no capital impact): `reconcile()` wiped `positions.json` mid-session

**Pattern:** At 07-07 midday, `lib.paper_sim.reconcile()` (alpaca-authoritative) re-mirrored `positions.json` from the broker's filled-position view. Because the broker's mirror was transiently empty during the pending-broker window, this overwrote the local record of all 4 positions to `{}`. Not a trade, not a hand-edit — a side effect of the prescribed reconcile step firing during an already-known-hazardous window. Caught immediately (no `close_position()` call, no `log.csv` rows, no decision files), reverted via `git checkout`, verified intact.

**Evidence:** `journals/daily/2026-07-07.md` §Midday, "Reconcile — IMPORTANT INCIDENT."

**Assessment:** the CB-refresh step has an explicit Guard 1 for the pending-broker window; the reconcile step has no equivalent guard. This is the same underlying hazard as Mistake #2's root cause (the 4 stuck rows), manifesting through a different code path. A guard proposal is referenced in the day's journal against a 2026-05-26 draft (`prompts/proposed_updates/2026-05-26_alpaca_mirror_state_integrity.md`) — confirm next cycle whether this covers the exact reconcile-wipe scenario, or draft a new proposal once v2 proposal-writing is enabled.

### Mistake #4 (NEW this week, N=1, no downstream impact): cited JSON snapshot overwritten in place during a same-day re-run

**Pattern:** The 07-10 pre_market Compliance rejection (see §7) triggered a same-day re-run that regenerated `data/market/2026-07-10/0640_signals.json` — but overwrote the file in place (`Modify: 10:53:57Z`, after the 10:52:05Z rejection) rather than writing a new, distinctly-named snapshot. The subsequent independent verification (`logs/risk_events/2026-07-10_1100_signal_snapshot_verification.md`) could not diff the rejected version against the corrected version directly; it had to reconstruct the rejected version's shape from the numbers quoted in the rejection log itself. This time the correction was independently verifiable from source code (`lib/signals.py`), so no harm resulted — but the pattern (silently overwriting an already-cited artifact) is a real gap that would not always be recoverable this cleanly.

**Evidence:** `logs/risk_events/2026-07-10_105205_compliance_reject.md`, `2026-07-10_105205_compliance_reject_resolved.md`, `2026-07-10_1100_signal_snapshot_verification.md`.

**Recommended action (observation-only; not actioned this cycle — `max_self_learning_proposals_per_cycle=0`):** snapshot filenames should be write-once (e.g., a post-rejection re-run writes `<HHMM>_signals_v2.json`, and the report/regime file re-point to the new filename rather than the original being silently mutated). Not yet covered by any open `prompts/proposed_updates/` file — a genuinely new candidate for the next cycle in which proposal-writing is in scope.

### Mistake #5 (carried, N=1 this week): specialist agent fabrication caught by the no-fabrication rule

**Pattern:** on 07-10, the `macro_sector` specialist reused 07-09's momentum ranks and invented intraday P&L figures; this was caught and corrected before reaching `current_regime.md` or the committed report. Single incident — the guardrail worked as designed. Worth watching for recurrence as the feed outage persists (the longer specialists have no fresh data, the more tempting it may be for one to paper over the gap).

**Evidence:** `journals/daily/2026-07-10.md` §Pre-market, "What worked" / "What failed / friction."

---

## 4. Memory Updates Applied (SAFE_MEMORY_UPDATE)

| File | Content | Status |
|------|---------|--------|
| `memory/strategy_lessons/2026-w28.md` | 5 lessons: daily-bar staleness (MUST-FIX, 5th+ week), CB persistence with new bypass wrinkle (MUST-FIX), specialist-agent fabrication (NEW, N=1), held-book behaved / GOOGL prediction correct, sample-size reminder | Written this run |
| `memory/agent_performance/2026-w29.md` | W28 calibration snapshot: 0 closed trades, equity path, calibration buckets (~15 resolved predictions), all-time cumulative summary (unchanged at 4 trades / −$1,144.07) — filename follows the verified forward-pointing convention | Written this run |
| `decisions/by_symbol/GOOGL.md` | W27-carried prediction reconciliation appended (holds-above-stop RESOLVED CORRECT) | Written this run |
| `decisions/by_symbol/CSCO.md`, `NVDA.md`, `XOM.md` | W28 status appended — reclaim durability STILL DEFERRED, 2nd consecutive week | Written this run |
| `decisions/by_symbol/GLD.md` | W28 status appended — overlay stayed blocked; 210d-MA reclaim unverifiable on stale data | Written this run |
| `memory/symbol_profiles/GOOGL.md`, `JNJ.md`, `UNH.md` | W28 observation blocks appended (genuinely new information only) | Written this run |

No writes to:
- `memory/market_regimes/` (current_regime.md touched operationally during 07-10 pre_market remediation, not by this weekly cycle)
- `memory/prediction_reviews/` (individual session files are written at EOD; weekly does not duplicate them)
- `prompts/proposed_updates/` (`max_self_learning_proposals_per_cycle=0`; none written — every recurring issue is already covered by an open proposal per the check performed this cycle, and the two genuinely new findings, Mistakes #3/#4, are each N=1 and/or already-drafted-adjacent, so neither was force-fit into a new proposal this cycle)
- **`reports/weekly_digest/`** — intentionally out of scope this cycle. `prompts/proposed_updates/2026-05-15_weekly_digest_plain_english.md` (the "step 5b" plain-English digest) remains `Status: DRAFT — awaiting human PR review`; it was never merged into `prompts/routines/weekly_review.md` (the actual routine spec has no step 5b), and `CLAUDE.md`'s approved write paths do not currently include this directory. Flagging the inconsistency (old digest files exist in that directory from before this was noticed) for the operator to resolve via PR — merge or close the draft — rather than resolving it unilaterally.

---

## 5. Risk Themes for Next Week

### Theme 1: The daily-bar outage has gone from "stale" to "sometimes fails outright"

07-08's total load failure (`SSLError`, not just a lagging fallback) is a step worse than the pattern documented in prior weeks. If this recurs, it may indicate the yfinance block is becoming more aggressive, or that the proxy path itself is degrading — worth operator attention distinct from the "just wire a paid feed" recommendation already on file.

**Action:** 07-13 pre_market should note whether the failure mode is "stale" or "hard failure" and flag if the pattern shifts.

### Theme 2: The CB authoritative-equity bypass — durable fix or one-off?

The 07-10 pre_close bypass produced the first fresh CB mark in a month, but it did not touch the actual bug (the 4 stuck rows, `peak_equity` frozen). If future routines don't repeat the bypass, the CB reverts to being blind at every session; if they do repeat it inconsistently, the equity history itself becomes patchy and harder to reason about.

**Action:** 07-13 onward, confirm whether this bypass pattern becomes the routine's default behavior for CB refresh under Guard-1, or whether it was a one-off improvisation — and land the actual finalizer fix regardless.

### Theme 3: Regime margin compression

SPY's cushion above its 50-day moving average fell from +1.76% (07-06) to +0.052% (07-10) over the week — a razor-thin margin that a single ~1% down day could flip. This compounds the existing stale-bar risk: if the regime flips exactly when the bar feed is down, the system would be evaluating trend-following exits and entries on outdated information at the most consequential moment.

**Action:** 07-13 pre_market should prioritize a fresh-bar check specifically to re-verify the SPY trend margin before trusting any other read this cycle.

### Theme 4: JNJ approaching both its earnings window and its take-profit simultaneously

JNJ sat between +14.7% and +20.5% most of the week (below its +25% take-profit) with earnings landing 2026-07-15 — the caution window opens at the 07-14 pre_close. A take-profit hit and an earnings-caution de-risk could arrive in the same 1-2 session window.

**Action:** 07-14 pre_close should weigh both triggers explicitly rather than treating them as independent.

---

## 6. Strategy Attribution (W28)

| Strategy | W28 Realized | W28 Open (end of week, indicative) | All-time Realized (post-06-04-reset) |
|----------|-------------|-------------------|------------------|
| A — dual_momentum_taa | $0.00 | SPY 20sh, +$224 unrealized | −$29.88 (1 closed trade — GLD, 06-08) |
| B — large_cap_momentum_top5 | $0.00 | GOOGL/JNJ/UNH, net +$1,234 unrealized | −$1,114.19 (3 closed trades, all 07-01) |
| C — gold_permanent_overlay | $0.00 | subsumed (flat) | subsumed into A all-time |
| **Total** | **$0.00** | **≈ +$1,456 unrealized (indicative)** | **−$1,144.07 (4 closed trades)** |

Zero realized activity this cycle — every strategy simply held its book. Both strategy-level samples remain far below N=20 for any attribution conclusion.

---

## 7. Compliance Review (Step 7)

The compliance_safety agent review confirms:

- No writes to `config/` (risk_limits.yaml, strategy_rules.yaml, approved_modes.yaml, watchlist.yaml) ✓
- No writes to `.claude/agents/` ✓
- No writes to `prompts/routines/` ✓
- No `prompts/proposed_updates/` files written (cap=0) ✓
- No write to `reports/weekly_digest/` — confirmed intentionally out of scope this cycle (§4) ✓
- The 1 decision this week (`decisions/2026-07-07/1649_GLD.json`) is a data-staleness NO_TRADE: bull thesis, bear thesis, and invalidation condition fields present; RM/Compliance verdicts present ✓
- The 07-10 pre_market Compliance **REJECTION**: correctly fired on an apparent artifact mismatch, correctly gated the routine from committing until resolved, and the resolution was independently re-verified (a third, skeptical pass in `2026-07-10_1100_signal_snapshot_verification.md`) rather than taken on the first resolution's word alone. This is the compliance gate working exactly as designed — it is not a finding against the system, it is evidence the gate is load-bearing. The one real gap it surfaced (in-place snapshot overwrite) is flagged in §3 Mistake #4, observation-only ✓
- The `reconcile()` wipe incident (07-07 midday) involved zero trades and zero decision files; reverted before any commit; no gate was bypassed because no trade was ever at stake ✓
- No live execution; no `PROPOSE_LIVE_*` decisions; no `trades/live/*` writes ✓
- Mode `PAPER_TRADING` throughout; not HALTED; not SAFE_MODE ✓
- INTU absent from every trade artifact this cycle (blocklist-footer documentation references only) ✓
- No `risk_limits.yaml` parameters raised or modified ✓
- All MUST-FIX / NEW operational findings above correctly remain observation-only (human-PR / operator scope), not actioned as config edits ✓

**Compliance verdict: APPROVED**

---

## 8. Commit Reference

Commit SHA: to be filled by post-commit step.
Artifacts produced this run (for reference):
- `journals/weekly/2026-28.md`
- `reports/learning/weekly_learning_review_2026-07-11.md`
- `memory/strategy_lessons/2026-w28.md`
- `memory/agent_performance/2026-w29.md`
- `decisions/by_symbol/{GOOGL,CSCO,NVDA,XOM,GLD}.md` (prediction reconciliation / status appended)
- `memory/symbol_profiles/{GOOGL,JNJ,UNH}.md` (W28 observations appended)
- `logs/routine_runs/<ts>_weekly_review_2026-28_audit.md`

**Not produced this cycle (unapproved):** `reports/weekly_digest/2026-28.md` — see §4.

---
