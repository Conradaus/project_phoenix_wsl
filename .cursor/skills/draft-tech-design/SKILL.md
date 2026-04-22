---
name: draft-tech-design
description: Turn an approved spec or domain doc into a subsystem tech design with module boundaries, data flow, and interfaces. Use after scope is approved and before implementation of a new subsystem.
---

# draft-tech-design

Tech designs live under `design/tech/` and are the bridge between
domain docs and code. A tech design must be approved (Tier A) before
implementation of the subsystem begins.

## What to do

1. Identify the input canon: the spec section(s) in
   `design/scope/prototype-scope.md` and the domain docs in
   `design/domain/` that this subsystem implements.
2. Read all input canon in full. Do not rely on recollection.
3. Read the currently-accepted ADRs that bear on this subsystem
   (stack, persistence, contract format, etc.).
4. Produce the tech design using the template at
   [`.cursor/templates/tech-design.md`](../../templates/tech-design.md).
5. Include **at least one mermaid diagram** — module diagram, state
   diagram, sequence diagram, or data-flow — whichever best conveys
   the subsystem's shape. Prefer more than one where they add clarity.
6. List every interface this subsystem exposes, with exact type
   signatures (in the project's chosen language; pseudocode only if
   no stack is chosen yet).
7. List every dependency this subsystem takes on other subsystems.
   Arrows point one way; if you cannot draw the dependency graph
   without a cycle, stop — the design is wrong.
8. Enumerate the invariants this subsystem must preserve, cross-
   referencing the invariants from its governing domain doc(s).
9. **Run the role quartet** as in `propose-adr` — tech designs are
   Tier A.
10. Synthesize critiques. Run `skeptic`. Produce the plain-English
    summary via `explain-like-im-not-a-coder`.
11. Get explicit human approval. Then the tech design may be written
    to `design/tech/<subsystem>.md` (this is not hook-protected, but
    changes to an approved tech design should themselves be Tier A).

## Discipline

- **Every named concept must exist in `30-domain-language.mdc`.** If
  it does not, stop and propose its addition.
- **Every decision made during the tech design that is not already
  covered by an accepted ADR must produce a new ADR.** Do not bury
  technical decisions inside a tech design; they belong in ADRs.
- **Prefer citing existing abstractions over inventing new ones.**
  Inventiveness during tech design is drift.

## Hand-off

An approved tech design is the governing spec for Tier B
implementation work. Tier B changes cite the tech design in commits
and change summaries.
