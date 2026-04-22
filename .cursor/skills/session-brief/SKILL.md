---
name: session-brief
description: Produce the one-screen session-opening brief that cites governing canon and declares the tier. Use at the start of every non-trivial session, or any time context has drifted.
---

# session-brief

The session brief is the first artifact of every session. It keeps
work anchored to canon despite fresh memory. Invoke this skill
before any planning or implementation on a non-trivial change.

## What to do

1. Read [`AGENTS.md`](../../../AGENTS.md) in full.
2. Read [`design/index.md`](../../../design/index.md) to locate the
   canonical docs relevant to this session.
3. Skim the specific governing docs (GDD sections, prototype scope,
   domain docs, tech designs, ADRs) that bear on the user's request.
4. Write the brief into chat using the template in
   [`.cursor/templates/session-brief.md`](../../templates/session-brief.md).
5. Ask the human any questions flagged in the "Unknown / ambiguous"
   section before proceeding.
6. Launch the `canon-guardian` subagent (readonly) against the brief
   to verify it correctly identifies the governing canon.

## The brief must answer

1. **Objective.** What are we trying to accomplish this session? One
   or two sentences, the human's words where possible.
2. **Governing canon.** Specific paths and section headings. If the
   governing artifact does not exist yet, name the artifact that
   needs to be created first.
3. **Relevant subsystems.** Which domain concepts, tech designs, or
   ADRs are in play?
4. **Proposed tier.** A, B, or C — with a one-sentence reason.
5. **Change scope envelope.** Which files and directories are likely
   to be touched? Any scope exclusions? (This helps catch drive-by
   refactors later.)
6. **Unknown / ambiguous.** Specific questions for the human. If this
   section is non-empty, pause here and ask before proceeding.

## Output contract

- Produced as a chat message to the human, not a committed file.
  (Session briefs are ephemeral; the commit trail plus ADRs is the
  durable record.)
- Must use the template structure verbatim — the `canon-guardian`
  subagent checks for structural adherence.
- Must fit on one screen. If it exceeds one screen, compress.

## When not to produce a brief

Only for a Tier C change explicitly and narrowly scoped by the human
in the same message (e.g. "fix the typo on line 42 of README"). Even
then, confirm the Tier C classification explicitly before proceeding.
