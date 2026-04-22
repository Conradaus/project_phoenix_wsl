---
name: propose-gdd-edit
description: The only sanctioned path for modifying design/gdd/**. Produces a reviewable diff with rationale for human approval. Use whenever an apparent GDD issue surfaces during downstream work.
---

# propose-gdd-edit

The GDD is canonical. It is hook-protected and cannot be edited by
the agent directly. When downstream work (spec, tech design, ADR,
implementation) surfaces an apparent GDD issue — ambiguity,
contradiction, or a passage that needs refinement to be implementable
— the fix must come through this skill.

## What to do

1. Identify the exact passage(s) in question. Cite path and line
   range. If the issue spans multiple passages, list them all.
2. Classify the issue:
   - **Ambiguity** — passage admits multiple reasonable interpretations.
   - **Contradiction** — passage contradicts another passage or an
     earlier, accepted interpretation.
   - **Under-specification** — passage lacks detail needed to
     implement; the implementation choice is substantive.
   - **Drift symptom** — the implementation diverged from the GDD
     and it is unclear whether the GDD or the implementation should
     change.
3. Draft the proposed edit using the template at
   [`.cursor/templates/gdd-edit.md`](../../templates/gdd-edit.md).
   Include:
   - **Current passage** verbatim.
   - **Proposed passage** verbatim.
   - **Rationale** — why this edit is required, in plain English.
   - **Downstream impact** — specs, domain docs, tech designs, ADRs
     that would need updates if this edit is accepted.
   - **Alternatives** — at least one alternative phrasing considered
     and rejected.
4. Present the proposal as a chat message to the human. **Do not
   write to `design/gdd/**` yet.**
5. On human approval, perform the write using the `write-adr.sh`
   wrapper (same mechanism as ADRs — it sets `PHOENIX_CANONICAL_EDIT=1`
   which permits the write through the hook). GDD edits live under
   `design/gdd/**` which is also hook-protected via the same
   `PHOENIX_CANONICAL_EDIT` flag.
6. Log the edit as an appendix entry in `design/decisions/` (a small
   "GDD-edit log" ADR or entry in an existing running log) so the
   trail of canonical-design changes is durable.
7. Queue the downstream-impact items listed in step 3 as follow-ups.

## Discipline

- **Never edit the GDD to make implementation easier without
  recording why.** The rationale must stand on design grounds, not
  implementation convenience.
- **Never quietly "harmonize" the GDD with the code.** If code and
  GDD disagree, the disagreement is a finding to surface, not a
  license to retrofit.
- **The human is the author.** This skill proposes; the human
  disposes. Default posture: assume the human's GDD wording is
  correct and the downstream interpretation is the one that needs
  adjusting, not the GDD.
