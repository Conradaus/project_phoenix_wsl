---
name: explain-like-im-not-a-coder
description: Produce a plain-English (plus optional mermaid) summary of a proposed or completed change, aimed at a game designer with no programming expertise. Required before every review gate the human touches.
---

# explain-like-im-not-a-coder

The human reviewing this project is a game designer, not a programmer.
Handing them a diff or a technical summary defeats the workflow's
review gates. This skill produces the artifact the human actually
reviews.

## What to do

1. Identify the change being explained: an ADR draft, a tech design
   draft, or a completed code diff.
2. Write a summary using the template at
   [`.cursor/templates/plain-english-summary.md`](../../templates/plain-english-summary.md).

## The summary must answer

1. **What does this change, in the game, from the player's or
   designer's point of view?** If the answer is "nothing visible,"
   state that and explain why the change still matters.
2. **Why are we doing it now?** Link it to a governing spec, ADR, or
   bug report.
3. **What trade-offs did we accept?** The plain-English version of
   the ADR's `Consequences` section.
4. **What changed in plain terms?** Avoid identifier-dumping. Name
   each concept in its domain term, not its code term, where possible.
5. **What could go wrong?** Failure modes the human should watch for
   during the next playtest, or limits that were accepted.
6. **Is anything deferred?** Explicit follow-ups the human should be
   aware of.
7. **A mermaid diagram, if it helps.** State changes, data flow, or
   a small before/after sketch. Diagrams often explain more cheaply
   than paragraphs for this audience.

## Voice rules

- **Use domain terms, not code terms.** "Ability", not
  `AbilityDefinition`. "Combat turn", not `TurnState`.
- **Describe behavior, not structure.** The human cares what the
  game does, not how the types are organized.
- **Avoid jargon.** If a concept is unavoidably technical, define it
  in one clause the first time it appears.
- **No "we refactored for maintainability."** Explain what
  maintainability means here, in this game, concretely.
- **Admit uncertainty.** If a trade-off is a real trade-off, say so.

## Length

- One screen, ideally. If the change is genuinely large, it was
  probably two changes; consider splitting.

## Output

- Produced as a chat message to the human, or saved alongside a
  committed artifact (e.g. as a section of an ADR) when durable.
- Always presented at the gate, never skipped. If you are about to
  hand the human a review without a plain-English summary, stop.
