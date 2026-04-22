#!/usr/bin/env python3
"""subagentStop hook body for the verifier subagent.

If the verifier reports FAIL or MISSING citation, inject a followup_message
forcing the parent agent to resolve findings before proceeding.
"""
import json
import re
import sys


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        print(json.dumps({}))
        return

    output = (data.get("output") or "") + (data.get("final_message") or "")

    fail_in_overall = re.search(r"###\s*Overall[\s\S]*?FAIL", output)
    fail_colon = re.search(r"Overall:\s*FAIL", output)
    citation_missing = re.search(r"Cited artifact\(s\):\s*MISSING", output)

    if fail_in_overall or fail_colon or citation_missing:
        followup = (
            "The verifier subagent reported FAIL or MISSING citation on "
            "the change it just reviewed. Do NOT proceed with commit. "
            "Resolve every blocking issue listed in the VERIFIER REPORT "
            "before continuing; for any non-blocking follow-up, record it "
            "in the session summary. If the verifier flagged mis-tiering, "
            "re-run the change through the higher tier's gate."
        )
        print(json.dumps({"followup_message": followup}))
    else:
        print(json.dumps({}))


if __name__ == "__main__":
    main()
