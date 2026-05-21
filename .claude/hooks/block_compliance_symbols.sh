#!/usr/bin/env bash
# Refuse any Write/Edit that would land a compliance-blocked symbol in a
# trade artifact (decisions, paper log/positions, agent prompts, scripts).
# Documentation paths are deliberately whitelisted so the operator can
# journal *about* the block ("we cannot trade INTU because ...") without
# this hook objecting.
#
# Source of truth: config/watchlist.yaml > blocked_symbols[*].symbol
# The loader assertion in lib.config.watchlist() catches the inverse case
# (a blocked symbol re-added to symbols[]).
source "$(dirname "$0")/_lib.sh"
read_hook_input

file_path="$(hook_field tool_input.file_path)"
[ -z "$file_path" ] && allow

# Pull blocked symbols once. Empty list -> nothing to enforce, allow.
blocked="$(python3 - <<'PY'
import os, subprocess, sys, yaml
try:
    repo = subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"],
        stderr=subprocess.DEVNULL,
    ).decode().strip()
except Exception:
    repo = os.getcwd()
path = os.path.join(repo, "config", "watchlist.yaml")
if not os.path.exists(path):
    sys.exit(0)
with open(path, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f) or {}
syms = [str(e.get("symbol", "")).upper().strip()
        for e in (data.get("blocked_symbols") or []) if e.get("symbol")]
print(" ".join(syms))
PY
)"

# No blocklist configured -> nothing to enforce.
[ -z "$blocked" ] && allow

# Documentation whitelist: these paths may legitimately reference a blocked
# symbol (audit notes, learning reports, the operator manual itself).
case "$file_path" in
  *journals/*|*memory/*|*reports/learning/*|*reports/end_of_day/*|*reports/pre_market/*|\
  *docs/*|*prompts/proposed_updates/*|*CLAUDE.md|*README.md|\
  *config/watchlist.yaml)
    # Edits to config/watchlist.yaml itself are allowed here; the Python
    # loader assertion (validate_watchlist_invariants) catches any attempt
    # to add a blocked symbol to symbols[].
    allow
    ;;
esac

# Pull the proposed content (Write) or new_string (Edit/MultiEdit).
content="$(hook_field tool_input.content)"
[ -z "$content" ] && content="$(hook_field tool_input.new_string)"

for sym in $blocked; do
  # 1) Refuse if the file path itself names the blocked symbol (e.g.
  #    decisions/2026-05-21/0930_INTU.json or trades/INTU_log.csv).
  case "$file_path" in
    *[_/-]"$sym".json|*[_/-]"$sym"_*|*[_/-]"$sym".md|*[_/-]"$sym".csv|*/"$sym"/*)
      block "compliance blocklist refused write of $sym to $file_path. See config/watchlist.yaml:blocked_symbols."
      ;;
  esac

  # 2) Refuse if the proposed content references the blocked symbol as a
  #    word. Documentation paths were whitelisted above; remaining paths
  #    are trade artifacts (decisions/, trades/, lib/, scripts/, etc.).
  if [ -n "$content" ] && printf '%s' "$content" | grep -Eq "\\b${sym}\\b"; then
    block "compliance blocklist refused write of $sym to $file_path. See config/watchlist.yaml:blocked_symbols."
  fi
done

allow
