---
name: propose-adr
description: Draft a new Architecture Decision Record from a kernel-of-truth statement. Use for every Tier A decision before any code is written. Also the sanctioned path for editing design/decisions/ and design/scope/.
---

# propose-adr

ADRs are the durable record of every Tier A decision. This skill is
both the drafter and the gatekeeper — the `preToolUse` hook only
permits writes under `design/decisions/**` and `design/scope/**` when
this skill has set `PHOENIX_CANONICAL_EDIT=1` on its shell invocation.

## What to do

1. Extract the **kernel of truth** from the user's request — the one
   sentence that captures the decision, e.g. "We will use an
   authoritative server with clients sending intents, not state."
2. Number the ADR. List existing ADRs in `design/decisions/` and use
   the next four-digit sequence (`0001`, `0002`, ...).
3. Draft the ADR using the template at
   [`.cursor/templates/adr.md`](../../templates/adr.md). All sections
   are required unless the template marks them optional.
4. Set the **Status** to `Proposed`.
5. **Run the role quartet** (`architect`, `engineer`, `game-designer`,
   `operator`) in parallel against the draft. See
   [`scripts/run-quartet.md`](scripts/run-quartet.md) for the
   invocation recipe.
6. Synthesize the four critiques into an `Addressed concerns` section
   on the ADR. Every critique must be either resolved in the decision,
   accepted as a known consequence, or explicitly deferred with a
   tracked follow-up.
7. **Run `skeptic`** as the final adversarial pass. Address its
   findings in the same `Addressed concerns` section.
8. **Run `explain-like-im-not-a-coder`** to produce a plain-English
   summary and add it as the ADR's first section (`Non-technical
   summary`).
9. Write the ADR to `design/decisions/NNNN-<slug>.md`. This write
   requires setting `PHOENIX_CANONICAL_EDIT=1` in the shell
   environment for the duration of the write; do so via the shell
   wrapper `scripts/write-adr.sh`.
10. Present the full synthesis to the human with the four raw
    critiques collapsed underneath and request explicit approval.
11. Upon approval, update the ADR's Status to `Accepted` and update
    `design/index.md` to reference it.

## The kernel-of-truth pattern

Do not ask the LLM to write an ADR from the user's full prose. Instead:

1. Restate the decision in one sentence and confirm it with the user
   if the framing is at all ambiguous.
2. Expand the one-sentence kernel into the full template.

This keeps the decision narrow and reviewable, and prevents the ADR
from quietly growing to cover decisions the human did not actually
make.

## Required sections (see template for full structure)

- **Non-technical summary** — what this means for the game, in plain
  English.
- **Context** — what problem, what constraints, what triggered this.
- **Decision** — the kernel sentence, expanded.
- **Alternatives** — at least two serious alternatives, with reasons
  each was rejected. No straw men.
- **Consequences** — what this commits us to, short and long term.
  Include negative consequences.
- **Addressed concerns** — synthesis of role-quartet and skeptic
  critiques.
- **Follow-ups** — anything deferred rather than resolved.

## Refusal conditions

Do not produce an ADR if:

- The "decision" is actually a choice between equivalent options with
  no real consequence — that is Tier B or C.
- The decision is not yet ripe — key context is missing. Ask the human.
- The ADR would duplicate an existing accepted ADR. Supersede instead.

## Superseding prior ADRs

To change a prior decision, draft a new ADR with Status `Proposed` and
a `Supersedes` field pointing at the prior ADR's filename. On
acceptance, update the prior ADR's Status to `Superseded` (this is
the only sanctioned edit to an accepted ADR; it still goes through
this skill).
