#!/usr/bin/env python3
"""beforeSubmitPrompt hook body: per-turn drift reminder."""
import json

payload = {
    "additional_context": (
        "Reminder: declare the change's tier (A/B/C) before planning; "
        "cite governing canon on every non-Tier-C change; tier-up when in doubt."
    )
}
print(json.dumps(payload))
