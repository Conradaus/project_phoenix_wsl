#!/usr/bin/env bash
# Write an ADR (or scope doc) through the canonical-edit gate.
# Usage: write-adr.sh <path-under-design/decisions-or-scope> <<<"$content"
# The PHOENIX_CANONICAL_EDIT=1 env var is what lets the preToolUse hook
# permit the write. This wrapper is the sanctioned path.

set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "usage: $0 <target-path>" >&2
  exit 64
fi

target="$1"

case "$target" in
  design/decisions/*|design/scope/*|design/gdd/*)
    ;;
  *)
    echo "error: write-adr.sh only permits writes under design/decisions, design/scope, or design/gdd" >&2
    exit 65
    ;;
esac

export PHOENIX_CANONICAL_EDIT=1
# The agent's Write tool (invoked downstream) will see this env var
# and the preToolUse hook will permit the write.
# This script is a documentation of the protocol, not the actual
# writer: the agent performs the write inside the environment this
# export provides.
echo "PHOENIX_CANONICAL_EDIT set for target: $target"
