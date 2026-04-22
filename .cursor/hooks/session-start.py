#!/usr/bin/env python3
"""sessionStart hook body: inject pointer to AGENTS.md and canon index."""
import json

payload = {
    "additional_context": (
        "You are starting a new session in Project Phoenix. "
        "Before doing anything non-trivial, read AGENTS.md in full and "
        "consult design/index.md. Use the session-brief skill to produce "
        "the opening brief, then run the canon-guardian subagent against "
        "it. Every change is Tier A, B, or C; declare the tier before "
        "planning. Every non-Tier-C change must cite its governing "
        "canonical artifact."
    )
}
print(json.dumps(payload))
