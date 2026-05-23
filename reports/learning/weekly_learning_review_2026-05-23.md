# Weekly Learning Review — 2026-W21 (May 18–22, 2026)

> Generated: 2026-05-23 by weekly_review orchestrator (inline; no Agent/Task tool)
> Mode: PAPER_TRADING (not SAFE_MODE — learning writes permitted)
> Template: §21N
> max_self_learning_proposals_per_cycle: 0 — observation-to-memory only; no prompts/proposed_updates/ files written

---

## 1. Prediction Reconciliation (outcomes as of 2026-05-23)

### Predictions with closed outcomes this week

#### WMT PAPER_CLOSE (2026-05-20 pre_close)
- **Original prediction:** Pre-earnings exit avoids asymmetric catalyst risk; WMT Q1 FY27 BMO 2026-05-21.
- **Confidence at prediction:** 0.55 (procedural) / 0.78 (directional catalyst leg)
- **Outcome:** WMT Q1 FY27 print: EPS $0.66 (beat $0.65), revenue $177.75B (beat ~$174.65B), US comps +4.1%. Despite the beat, WMT fell ~8% on the print.
- **Resolution: CORRECT_POLICY + CORRECT_DOLLARS.** The pre-earnings exit at $131.23 (−$151.93 realized) avoided ~$1,215 of mark-to-market damage from the 8% gap-down. Validates `holding_earnings_caution_window_days=1` overlay as a robust risk-reduction mechanism.
- **Key lesson:** Earnings-window overlay correctly identified and neutralized asymmetric single-stock catalyst risk. The −$152 exit cost vs ~$1,215 avoided is a clean data point: the overlay has strong expected value even when directional uncertainty is high. Beat-and-fall (revenue beat, stock down 8%) is a common pattern in large-cap consumer staples at high valuations — our risk rules correctly treat all earnings prints as asymmetric risks, not directional bets.

#### WMT NO_TRADE post-print (2026-05-21 EOD)
- **Original prediction:** Declining re-entry on a stale pre-gap signal; re-evaluate on post-gap bar.
- **Confidence at prediction:** 0.75
- **Outcome:** WMT is in the hold-zone (rank 7, +20.40% 6m) on 2026-05-22 EOD — below the top-5 entry threshold. The NO_TRADE correctly avoided both the timing mismatch (stale pre-gap signal) and the continued weakness (WMT is no longer a top-5 momentum name on the post-print bar).
- **Resolution: CORRECT.** The post-gap bar correctly demoted WMT to the hold-zone. The judgment-driven NO_TRADE (RM REJECTED on stale price + defensive posture) produced the same outcome that a mechanical post-earnings guard would have produced.
- **Key lesson:** Confirms the proposal in §3 below: the engine fires ENTRY on a signal evaluated on the pre-event bar; a mechanical `stale_post_event` gate would make this deterministic rather than judgment-driven.

#### CB stays FULL (2026-05-19 HALF→FULL artifact)
- **Original prediction:** Transient artifact from in-flight fills; self-corrects at EOD.
- **Confidence at prediction:** 0.90
- **Outcome:** Correct. EOD reconcile + post-fill equity recompute confirmed DD was 0.00%, not 74%.
- **Resolution: CORRECT.** No capital was ever at risk from the spurious drawdown read.
- **Key lesson:** The root cause (CB equity = broker cash + sim MTM, evaluated before fills settled) is a structural defect. Confidence in the diagnosis was high; the fix requires a guard, not a conceptual change.

### Predictions still pending (momentum windows: 30–90 days)

| Prediction | Entry date | Status | Notes |
|-----------|-----------|--------|-------|
| CSCO HOLD (long momentum) | 2026-05-19 fill | Pending | +$380 uPnL week-end; above stop |
| GLD HOLD (Strategy A) | 2026-05-19 fill | Pending | +$67 uPnL; Strategy A rotation |
| GOOGL HOLD (momentum carry) | 2026-05-19 fill | Pending | −$488 uPnL; above stop $357.10 |
| XOM HOLD (energy momentum) | 2026-05-19 fill | Pending | −$520 uPnL; above stop $142.13 |
| UNH HOLD (boundary r5) | 2026-05-20 fill | Pending | +$146 uPnL; rank-5 boundary |
| NVDA PAPER_BUY (r5 promotion) | 2026-05-22 submitted | Pending | PENDING_BROKER; fills Tue 2026-05-26 |
| CSCO/GLD/GOOGL/UNH/XOM HOLD over long weekend | 2026-05-22 pre_close | Pending | Resolves Tue 2026-05-26 open |

---

## 2. Recurring Mistakes Identified This Week

### Mistake 1: CB equity write during broker fill settlement (HIGH SEVERITY)
- **Pattern:** Intraday routines write CB equity from `broker.account_snapshot()` while `PENDING_BROKER` rows exist in the sim ledger. Because the broker has debited cash for the pending orders but the positions haven't yet been mirrored back, the equity appears severely impaired (cash-only view).
- **Frequency:** First confirmed occurrence 2026-05-19; risk of recurrence on any day with PENDING_BROKER rows at an intraday routine time.
- **Impact:** Spurious HALF circuit-breaker state, 5 URGENT Telegram notifications for a non-event, false confidence that the system is in distress when it is not.
- **Resolution path:** Guard the CB equity write in intraday routines: if `paper_sim.pending_broker_count() > 0`, skip the write or use `paper_sim.portfolio_equity()` exclusively. Requires a human PR.

### Mistake 2: stop/target fields wiped by alpaca-mirror (HIGH SEVERITY)
- **Pattern:** When `paper_sim.reconcile()` runs in `alpaca-authoritative` mode, it rebuilds `positions.json` from the Alpaca mirror, which does not carry stop-loss and take-profit prices. Every position ends up with `stop_loss=null, take_profit=null`, disabling the deterministic `portfolio_health` stop check for the remainder of the session.
- **Frequency:** Every day this week (Mon–Fri). All stop monitoring was advisory-by-hand.
- **Impact:** Silent safety degradation. No automated stop was active on any of the 5 positions all week. If GOOGL or XOM had breached the −10% stop, the routine would not have caught it automatically.
- **Resolution path:** Maintain a side-file `trades/paper/position_meta.json` that stores the original entry stops/targets and is NOT overwritten by the reconciler. The `portfolio_health` check should merge this file with the live position data. Requires a human PR.

### Mistake 3: Post-earnings gap creates stale-signal ENTRY (MEDIUM SEVERITY)
- **Pattern:** The deterministic engine evaluates signals against the latest completed daily bar. If an earnings event occurred after the last bar date, the signal price is the pre-event close — which may be substantially different from the current tradeable price.
- **Frequency:** Two occurrences this week: WMT ENTRY on 2026-05-21 (−8% gap), NVDA correctly handled at EOD-2026-05-22 (2-day lag post-print gave time for the caution window to expire).
- **Impact on WMT:** The engine fired ENTRY on the 2026-05-20 pre-earnings bar. This required judgment-driven NO_TRADE rather than a mechanical gate. Risk: a future routine could act on the stale signal if the judgment layer fails.
- **Resolution path:** Add `signal_bar_date` tracking. If `signal_bar_date < event_date < today` for a known earnings/dividend event, flag the signal as `stale_post_event=true` and route to NO_TRADE mechanically. Requires a human PR to `lib/signals`.

---

## 3. Memory Updates (SAFE_MEMORY_UPDATE)

Applied to `memory/` this cycle. Mode is PAPER_TRADING (not SAFE_MODE); these writes are permitted.

### memory/strategy_lessons/2026-w21.md (NEW)
Key lessons this week documented for the strategy layer:
- WMT earnings-overlay validation: beat-and-fall is a real pattern; overlay correct even without directional certainty
- NVDA earnings-gate mechanics: 1-day caution window correctly prevented entry until 2 days post-print
- CB intraday guard defect (see §2 Mistake 1)
- Rank-5/6 boundary fragility (UNH/NVDA/AMZN jitter — 0.42pp gap at week-end)

### memory/agent_performance/2026-w22.md (NEW)
Raw prediction counts and calibration histogram for W21 trading period. PRELIMINARY; N too small for calibration curve.

### decisions/by_symbol/WMT.md (APPEND)
Outcome annotations appended for the 2026-05-20 pre-earnings close and the 2026-05-21 NO_TRADE post-print. Resolution: both CORRECT.

---

## 4. Proposed Memory Updates (observations only; no proposal files this cycle)

The following patterns are recorded as observations in `memory/strategy_lessons/2026-w21.md` for future self_learning review cycles. They are NOT promoted to `prompts/proposed_updates/` (max_self_learning_proposals_per_cycle=0).

| Observation | Priority | Suggested future proposal topic |
|------------|---------|--------------------------------|
| CB equity write guard against PENDING_BROKER rows | MUST-FIX | `cb_pending_broker_guard` |
| positions.json stop/target persistence under alpaca-mirror | MUST-FIX | `position_meta_sidecar` |
| Post-earnings stale signal → mechanical gate | HIGH | `post_earnings_gap_guard` |
| archive_routine_logs.py legacy filename tolerance | MEDIUM | `archive_filename_tolerance` |
| Sim-vs-Alpaca mark-gap investigation | MEDIUM | `sim_alpaca_mark_gap` |

When `max_self_learning_proposals_per_cycle` is raised from 0, these should be the first proposals drafted.

---

## 5. Strategy Review (observations; no proposal files this cycle)

### Strategy A (dual_momentum_taa — GLD)
- Week uPnL: +$67 (+0.16%). Modest positive contribution.
- GLD remains Strategy A top-1 by 12m return (+37.36% vs SPY +26.72% vs IEF +3.89%).
- IEF below 210d MA → cash-floor logic inactive (correct).
- No regime-driven rotation event this week.
- Observation: GLD's outsized YTD lead (+10.6pp over SPY) continues to suggest either inflation-hedge demand or macro-uncertainty accumulation. Both interpretations support holding the Strategy A + C combined GLD position.

### Strategy B (large_cap_momentum_top5)
- Week net: −$634 (4 held: CSCO +$380, GOOGL −$488, XOM −$520, UNH +$146; WMT realized −$152).
- Rank-5 boundary (UNH → NVDA transition) demonstrates the known fragility of the cut-off slot. UNH was rank 4 at week-end; NVDA entered at rank 5. The boundary jitter (UNH/NVDA/AMZN/COST trading in a ~2pp band) means the rank-5 slot will rotate frequently.
- CSCO remains the strongest 6m momentum name (+54.42%), but also the post-earnings-gap concern from prior weeks. The +$380 uPnL at week-end is positive resolution so far.
- GOOGL and XOM are the two underwater positions (-$488, -$520). Both carry the thinnest stop cushions going into the long weekend (7.2%, 9.1%). No catalyst identified; hold decisions are defensible.

### Strategy C (gold_permanent_overlay)
- Subsumed by Strategy A throughout the week. GLD 36-share position serves both the 60% A allocation (via the TAA strategy) and the 10% C allocation (overlay). No separate position required; no double-booking.

---

## 6. Calibration Drift Check (mandatory)

**No Risk Manager or Compliance calibration drift observed this week.**

- RM rejected WMT ENTRY (2026-05-21) correctly on "stale pre-earnings price + defensive posture."
- RM rejected WMT re-entry (2026-05-20 EOD) correctly on "earnings_window."
- All 5 PAPER_BUY decisions this week (GLD, CSCO, GOOGL, XOM, WMT on 05-18; UNH on 05-19; NVDA on 05-22) were APPROVED with correct theses.
- Compliance APPROVED all actionable decisions; no watchlist violations; INTU correctly blocked throughout.
- No HALT_AND_REVIEW recommendation warranted.

---

## 7. Halt-Trigger Check (monthly review cadence; included for completeness)

| Trigger | Status |
|---------|--------|
| Drawdown breach 12% (act before 15% hard cap) | No — 4.34% peak DD this week |
| 3-month rolling return negative | N/A (8 trading days of data) |
| Individual strategy drawdown ≥25% | No — Strategy B peak DD <5% this week |

**STAY_PAPER.** No halt or review triggers met.

---

*Generated: 2026-05-23T13:13:45Z. Mode: PAPER_TRADING. Subagent dispatches: 0 (inline). Schema validation: PASS.*
