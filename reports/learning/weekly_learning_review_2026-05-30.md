# Weekly Learning Review — 2026-W22 (May 26–29, 2026)
# Review Date: 2026-05-30

> Prepared by: weekly_review orchestrator  
> Mode: `PAPER_TRADING` (not SAFE_MODE — learning writes permitted)  
> Template: §21N (matches weekly_learning_review format from W21)  
> `max_self_learning_proposals_per_cycle = 0` → No `prompts/proposed_updates/` files written.

---

## 1. Period Summary

**Trading days:** 4 (2026-05-26 Mon, 05-27 Tue, 05-28 Wed, 05-29 Thu; 05-25 holiday)  
**End-of-week state:** 100% cash ($100,578.03)  
**Period return:** −0.565% (broker-authoritative)  
**Daily-loss events:** 2 (05-26: −0.607%; 05-29: −1.473%) — same macro driver both times  
**Closed trades:** 6 (3 wins, 3 losses; all by daily-loss halt mandate)  
**Open predictions resolved:** 8 (including all W21 carry-overs)  
**New predictions pending:** 1 (AMZN rank-5 re-entry re-evaluation at 06-01)  

---

## 2. Prediction Reconciliation (Full Detail)

### W21 carry-over predictions — now resolved

| Symbol | Entry | Close | Outcome | Verdict | Accuracy | Notes |
|--------|-------|-------|---------|---------|----------|-------|
| CSCO | $117.66 (05-19) | $121.17 (05-29) | +$456 / +2.98% | WIN | Correct: rank-1 persistence held; thesis intact until halt mandate | Closed by halt, not stop or rotation signal |
| GLD | $412.04 (05-19) | $418.02 (05-29) | +$215 / +1.45% | WIN | Correct: TAA top-1; macro hedge; gold/crude inverse in energy selloff | Debate: should crisis hedge be exempt from halt? |
| GOOGL | $395.64 (05-19) | $382.62 (05-29) | −$495 / −3.29% | LOSS | Partial: DOJ risk priced; energy correlation and general beta drag | Above stop throughout; thesis not invalidated by close |
| XOM | $160.43 (05-19) | $145.37 (05-29) | −$1,461 / −9.35% | LOSS | Below prediction: hold thesis assumed crude would stabilize | US-Iran de-escalation extended crude sell; same macro twice |
| UNH | $391.90 (05-20) | $380.89 (05-29) | −$430 / −2.81% | LOSS | Below prediction: Berkshire exit was smart-money signal | Above stop throughout; defensive healthcare underperformed |
| NVDA | $197.559 original entry → $215.91 alpaca-mirror fill (05-26) | $214.34 (05-26 pre_close) | +$453 vs original / −$1.57 vs mirror basis | WIN (original basis) | Correct on promotion basis; closed same day as fill | De-risked as rank-9 weakest-thesis name; correct de-risk priority |
| WMT entry rejected (05-26 EOD) | n/a (rejected) | n/a | Deferral neutral | CORRECT_POLICY | Rank-5 entry on breach day + stale bars — correct refusal | Outcome: WMT stable; deferral benign |
| 05-29 no re-entry after halt | n/a (refused) | n/a | +$0 (flat-on-day) | CORRECT_POLICY | Halt mandate served its purpose; flat close vindicated refusal | Revenge-trade risk avoided |

### Overall prediction accuracy this cycle

| Category | Count | Correct | Notes |
|----------|-------|---------|-------|
| ENTRY signal quality | 5 (CSCO, GLD, GOOGL, XOM, UNH held from W21) | 2/5 wins | 2 wins $671; 3 losses $2,386. Profit factor 0.28 on this cohort. |
| Policy decisions (NO_TRADE / REJECTED) | 3 | 3/3 correct | Daily-loss halt refusals; WMT entry deferral — all validated |
| De-risk priority (NVDA chosen over CSCO/GLD) | 1 | 1/1 correct | NVDA was rank-9 at de-risk time; CSCO/GLD outperformed vs entry |

**Running calibration:** 11 resolved predictions all-time (post-reset). Policy decisions: 100% correct (5/5). Entry/hold outcomes: 5W / 6L cumulative.

---

## 3. Recurring Mistakes

### Mistake #1 (repeated from W21, severity escalated): PENDING_BROKER log artifact blocking CB writes

**Pattern:** Completed round-trips (BUY submitted → FILLED → CLOSE submitted → FILLED) leave the BUY row as `PENDING_BROKER` permanently in the append-only `log.csv`. The `pending_broker_count()` function counts any `status=PENDING_BROKER` row, so it returns non-zero after the first round-trip. The CB equity write is gated behind `pending_broker_count() == 0`, so it never runs again after the first round-trip.

**Evidence this week:** CB write skipped on every routine (05-26 through 05-29, 7+ consecutive skips). By EOD 05-29, `pending_broker_count = 7`.

**Impact:** CB peak-tracking carried manually (correct but fragile). If a genuine CB transition occurred, the state file would lag and downstream logic might read stale state.

**Root cause:** The `PENDING_BROKER` status was designed as an in-flight indicator. After the broker confirms fills, the local log should be updated to `OPEN` (for buys) or `CLOSED` (for sell-closes). But the log is append-only, so status updates require a separate finalize step.

**Proposed resolution (not executable here — requires human PR):** Add an EOD finalize sweep that queries broker order status for all `PENDING_BROKER` rows and writes a new row with the correct final status. OR: modify `pending_broker_count()` to exclude rows where the broker position for that symbol is flat.

**Frequency:** Every session for 2 weeks. Severity: HIGH (CB tracking degraded; no false transition yet, but growing risk).

---

### Mistake #2 (new W22): Same macro driver triggered two daily-loss events in 4 sessions

**Pattern:** XOM (single large-cap name, ~15% of equity) was the primary driver of both the 05-26 (−0.607%) and 05-29 (−1.473%) daily-loss breaches. The macro driver was identical: US-Iran diplomatic de-escalation / Strait of Hormuz reopening prospects → crude oil -10%+ on the week → XOM -9.35%.

**Evidence:** 05-26 midday: XOM −5.5% intraday (WTI ~$92, Iran ceasefire reports). 05-29 midday: XOM −9.06% (continued crude de-escalation narrative). Both days: XOM was the single largest negative contributor.

**Impact:** The first breach (05-26) was partially recoverable — only NVDA was de-risked. The second breach (05-29) was not — all 5 positions were closed. The concentrated energy-sector exposure turned a manageable macro theme into a repeated hard-event trigger.

**Root cause analysis:**
- The -10% rotation stop is the formal risk limit; XOM never breached it (05-29 low was $145.37 vs $142.13 stop = +2.25% cushion at close). The *daily-loss limit* (-$500 / -0.5%), not the stop, was the breach.
- The daily-loss limit is portfolio-level; a single name at ~15% of equity that moves -5% intraday will consume ~$750 of the $500 daily-loss budget in isolation.
- The current 6 equal-weight positions at ~6-15% each means any one name moving >3.3% intraday can breach the $500/0.5% limit.

**Implication for next entry cycle:**
1. XOM sizing on re-entry: consider halving the normal allocation (~7.5% instead of ~15%) given two consecutive energy-led breaches.
2. For any sector that has already caused a daily-loss breach this week, the pre_close overnight-risk overlay should flag a reduced re-entry size.
3. This is a policy question (sizing override per recent-loss event) requiring human review — not a config change the agent can make.

---

### Mistake #3 (carried from W21, unresolved): `positions.json` stop/target wiped by alpaca-mirror reconcile

**Pattern:** When `BROKER_PAPER=alpaca` and the broker-authoritative reconcile fires, `positions.json` is rebuilt from broker state. Broker state does not include `stop_loss` or `take_profit` fields, so they are written as `null`. The `portfolio_health.assess_positions()` function then has no armed stops and returns an empty `to_close` list regardless of price action.

**Evidence:** All week (and W21), every routine's health check note: "stop/target = null under alpaca-mirror; stops were validated manually against the table above."

**Impact:** Silent safety degradation. If XOM had breached its $142.13 stop on 05-29 midday (it didn't — low was ~$145), the automated stop check would not have caught it. The operator's manual cross-check would have, but the automation layer is inert.

**Proposed resolution:** Create/maintain `trades/paper/position_meta.json` with `{symbol: {stop_loss, take_profit, entry_date, strategy, entry_price}}`. The reconciler reads this file on reconcile and re-populates `positions.json` stop/target from it, rather than wiping them. Requires human PR.

**Frequency:** Every session for 3 weeks. Severity: HIGH (safety gap growing; near-miss on XOM 05-29).

---

### Mistake #4 (new W22): Data pipeline staleness blocked entries for 2 consecutive sessions

**Pattern:** Daily bars failed to refresh for sessions 05-27 EOD (bars stamped 05-26, ~26h stale) and 05-28 EOD (bars stamped 05-27, ~44.8h stale). The `max_data_staleness_seconds = 60` cap is in `risk_limits.yaml`, so all entry signals were correctly forced to NO_TRADE — but the operator had no early warning.

**Evidence:** 05-27 EOD decision notes: "bars ~26h stale vs 60s cap." 05-28 EOD: "~44.8h old." Both sessions: AMZN entry rejected on stale data (would have been the only new-exposure candidate).

**Impact:** Missed two entry opportunities on what may have been a valid AMZN rank-4/5 signal (AMZN still in top-5 at 05-29 EOD; would likely have been ~flat through the week before the 05-29 de-risk). Two sessions effectively monitoring-only on the deterministic engine. The stale-data gate prevented bad fills but also good fills.

**Root cause:** The bar-fetch pipeline (`lib.data.get_bars`) apparently cached or failed to fetch fresh bars for consecutive sessions. Not investigated at EOD runtime (no tool to diagnose).

**Proposed resolution:** A pre_market freshness alarm: if the latest cached bar is >4h past the prior session's expected close (4:00 PM ET), write a `logs/risk_events/<ts>_stale_bar_feed.md` and alert operator before EOD runs on stale data. This converts a reactive (EOD discovers staleness, blocks all entries) to a proactive (pre_market surfaces staleness, operator can refresh) pattern.

**Frequency:** 2 consecutive sessions in W22. Severity: MEDIUM (correct outcome enforced by the gate; but blind spots possible if guard logic had a bug).

---

## 4. Memory Updates Applied

The following memory writes were performed this cycle (SAFE_MEMORY_UPDATE):

| File | Content |
|------|---------|
| `memory/strategy_lessons/2026-w22.md` | 5 strategy execution lessons (energy concentration, GLD carve-out, stale bars, pending_broker, same-day-fill/close) |
| `memory/agent_performance/2026-w23.md` | W22 trading-period calibration snapshot: 6 closed trades, 50% win rate, profit factor 0.47, all PRELIMINARY |
| `decisions/by_symbol/NVDA.md` | Cumulative stats + 05-26 close outcome row appended (this run) |
| `decisions/by_symbol/CSCO.md` | Already current — 05-29 close written at 2026-05-29 EOD commit `78439c6` |
| `decisions/by_symbol/GLD.md` | Already current — 05-29 close written at 2026-05-29 EOD commit `78439c6` |
| `decisions/by_symbol/GOOGL.md` | Already current — 05-29 close written at 2026-05-29 EOD commit `78439c6` |
| `decisions/by_symbol/UNH.md` | Already current — 05-29 close written at 2026-05-29 EOD commit `78439c6` |
| `decisions/by_symbol/XOM.md` | Already current — 05-29 close written at 2026-05-29 EOD commit `78439c6` |

No `prompts/proposed_updates/` writes (max_self_learning_proposals_per_cycle = 0 enforced).

---

## 5. Proposed Policy Questions (Not Executable Here — Flag for Human Review)

Since `max_self_learning_proposals_per_cycle = 0`, these are not drafted into `prompts/proposed_updates/`. They are documented here as human-review flags only.

1. **GLD permanent overlay exemption from daily-loss de-risk:** Should `halt_after_daily_limit_breach=true` have a carve-out for the `gold_permanent_overlay` strategy position? Evidence: GLD was closed at +$215 (genuine win) during a macro stress event it was designed to hedge. Closing the hedge in a crisis is arguably counterproductive to the portfolio design. This requires modifying `config/strategy_rules.yaml` or `config/risk_limits.yaml` — human PR required.

2. **XOM (energy sector) size-down on re-entry after consecutive breaches:** Should the system automatically halve position sizing on any symbol that contributed to two consecutive daily-loss events within N days? The current `max_position_size_pct: 15.0` and equal-sizing (6 names) allows ~15% individual concentration. Evidence: XOM at ~15% of equity caused two breach days. This is a calibration question requiring `config/risk_limits.yaml` change — human PR required.

3. **`pending_broker_count()` fix:** Should `pending_broker_count()` cross-check broker order status to exclude already-confirmed fills? This is a code change to `lib/` — human PR required.

4. **Pre-market data-freshness alarm:** Should `pre_market` write a `logs/risk_events/<ts>_stale_bar_feed.md` if the latest daily-bar file is >4h past expected prior-session close? This is a routine-logic change — human PR required.

---

## 6. Forward Learning Priorities

For W23 (week of June 1, 2026):

1. **Monitor whether PENDING_BROKER rows resolve at the 06-01 open**. If `pending_broker_count` normalizes to 2 (or 0), the CB equity write can resume. If it stays at 7+, the defect is worsening.

2. **Watch XOM re-entry sizing** — given two consecutive energy-beta daily-loss events, size down if re-entering. Document whether the reduced sizing decision is operator-driven or system-driven.

3. **Watch AMZN entry qualification** — AMZN was the deferred rank-4/5 candidate for 3 sessions; if it re-qualifies on fresh bars 06-01 with a clean session, the entry outcome is a learning data point (was the deferral cost-effective or did it avoid a loss?).

4. **Track crude oil / US-Iran diplomatic status** — the macro driver of both weekly loss events. If the situation resolves (deal signed, Hormuz formally reopened), the XOM thesis may weaken structurally, not just cyclically.

---

*Generated: 2026-05-30T09:00:00Z. Routine: weekly_review. Mode: PAPER_TRADING. Review period: 2026-W22 (May 26–29).*
