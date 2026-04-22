#!/usr/bin/env python3
"""preToolUse hook body: gate writes/edits/deletes to canonical design paths.

Any Write/StrReplace/Delete targeting design/gdd/**, design/scope/**, or
design/decisions/** returns permission: ask so the human explicitly
approves every canonical edit. Other paths pass through.
"""
import json
import os
import sys


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        print(json.dumps({"permission": "allow"}))
        return

    tool_input = data.get("tool_input") or data.get("input") or {}
    target = (
        tool_input.get("path")
        or tool_input.get("file_path")
        or tool_input.get("target_notebook")
        or ""
    )

    cwd = os.getcwd()
    if target.startswith(cwd + "/"):
        target = target[len(cwd) + 1:]

    protected_prefixes = (
        "design/gdd/",
        "design/scope/",
        "design/decisions/",
    )

    is_protected = any(target.startswith(p) for p in protected_prefixes)

    if is_protected:
        reason = (
            f"Canonical design path touched: {target}. "
            "Canonical artifacts (GDD, scope, ADRs) require explicit "
            "human approval on every edit. If this edit was produced via "
            "the propose-adr or propose-gdd-edit skill, confirm to proceed. "
            "Otherwise, reject and route the change through the sanctioned "
            "skill first."
        )
        print(json.dumps({"permission": "ask", "reason": reason}))
    else:
        print(json.dumps({"permission": "allow"}))


if __name__ == "__main__":
    main()
