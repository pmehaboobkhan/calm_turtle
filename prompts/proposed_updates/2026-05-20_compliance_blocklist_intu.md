# Proposed updates: INTU compliance blocklist — agent prompts + settings.json

**Date:** 2026-05-20
**Reason:** Operator employed by Intuit. Employer insider-trading policy prohibits any position in INTU, anytime. Need a declarative compliance blocklist enforced at every layer.
**Scope:** Paranoid — block research, data fetches, signals, AND trades.

This draft pairs with the code-side changes already on branch `feature/intu-compliance-blocklist` (config schema, `lib/config.py`, `config/watchlist.yaml`, `lib/signals.py`, `lib/paper_sim.py`, `lib/broker.py`, `.claude/hooks/block_compliance_symbols.sh`, `CLAUDE.md`, `tests/test_compliance_blocklist.py`).

The seven changes below cannot be applied automatically — they touch files protected by `block_prompt_overwrites.sh` or the auto-mode self-modification classifier. The operator must apply them by hand at PR review time.

---

## 1. `.claude/settings.json` — register the new PreToolUse hook

**Where:** the `PreToolUse → matcher: "Edit|Write|MultiEdit" → hooks` array (lines 7-15).

**Change:** append one entry after `safe_mode_writes.sh`:

```diff
           { "type": "command", "command": ".claude/hooks/require_strategy_tests.sh" },
-          { "type": "command", "command": ".claude/hooks/safe_mode_writes.sh" }
+          { "type": "command", "command": ".claude/hooks/safe_mode_writes.sh" },
+          { "type": "command", "command": ".claude/hooks/block_compliance_symbols.sh" }
         ]
```

The hook script itself (`.claude/hooks/block_compliance_symbols.sh`) was already added on the feature branch and is executable.

---

## 2. `.claude/agents/risk_manager.md` — insert hard check #0

**Where:** insert a new bullet at line 21, before the existing "Symbol is in `watchlist.yaml`..." check.

**New bullet:**

```
0. **Compliance blocklist (overrides everything):** Symbol is NOT in `config/watchlist.yaml > blocked_symbols[]`. If it is, return `REJECTED` immediately with `reasoning` field set to `symbol_on_compliance_blocklist: <SYM> — see config/watchlist.yaml blocked_symbols`. This check overrides all other verdicts and cannot be downgraded to `NEEDS_HUMAN`. The operator is employed by the company in question; trading the symbol could violate their employer's insider-trading policy.
```

**Forbidden additions** (append to existing "Forbidden" list at line 35):

```
- Approving any trade for a symbol in `blocked_symbols[]`. There is no override path inside this agent.
```

---

## 3. `.claude/agents/compliance_safety.md` — insert hard check #0

**Where:** insert a new bullet at line 12, before "Mode compatibility".

**New bullet:**

```
0. **Compliance blocklist (overrides everything):** Symbol is NOT in `config/watchlist.yaml > blocked_symbols[]`. If it is, return `REJECTED` immediately and write `logs/risk_events/<ts>_compliance_blocklist_reject.md`. This check overrides mode, strategy, and Risk Manager verdict. Notify on every such rejection (not the second — every one).
```

**Forbidden additions** (append to existing "Forbidden" list at line 29):

```
- Approving a decision for a symbol in `blocked_symbols[]`, regardless of any other agent's verdict.
```

---

## 4. `.claude/agents/market_data.md` — refuse blocked symbols

**Where:** add to whichever section enumerates refusals. If none, add a "Refuse" section near the bottom.

**New bullet:**

```
- **Blocked symbols.** If the requested symbol appears in `config/watchlist.yaml > blocked_symbols[]`, refuse the fetch. Do not call any data API for it. Emit a `BLOCKED_SYMBOL` notice citing the blocklist entry (`symbol`, `reason`). Continue processing other symbols in the same routine.
```

---

## 5. `.claude/agents/news_sentiment.md` — refuse blocked symbols

**Where:** same as #4 above.

**New bullet:**

```
- **Blocked symbols.** Skip any symbol in `config/watchlist.yaml > blocked_symbols[]`. Do not query news APIs, do not summarize, do not score sentiment. Emit a `BLOCKED_SYMBOL` notice and move on.
```

---

## 6. `.claude/agents/fundamental_context.md` — refuse blocked symbols

**Where:** same as #4 above.

**New bullet:**

```
- **Blocked symbols.** Skip any symbol in `config/watchlist.yaml > blocked_symbols[]`. Do not pull SEC filings, fundamentals, or earnings calendars. Emit a `BLOCKED_SYMBOL` notice and move on.
```

---

## 7. `.claude/agents/trade_proposal.md` — pre-flight blocklist check

**Where:** at the top of the proposal-wrapping logic, before any signal is wrapped into a decision file.

**New bullet:**

```
- **Pre-flight blocklist check.** If `signal.symbol` is in `config/watchlist.yaml > blocked_symbols[]`, refuse to produce a `trade_decision.json` for it. Log the attempted symbol to `logs/risk_events/<ts>_compliance_blocklist_attempt.md` (this should never happen if upstream agents are functioning; the entry indicates a regression worth investigating). Return `NO_TRADE` with a `compliance_blocklist` rationale.
```

---

## Apply order at PR review

1. Land the feature branch as-is (all six code layers + tests + CLAUDE.md already present).
2. Apply the seven prompt/settings edits above by hand (or via a follow-up commit on the same branch).
3. Re-run `pytest tests/ -v` to confirm nothing regressed.
4. Smoke-test `/risk-check` and `/premarket-report` to confirm the agents read the blocklist on their next routine.

The deterministic Python layers will protect against accidental trades even before the agent prompts are updated — but the agent prompts are necessary for the LLM-driven research/news refusal path (paranoid scope).
