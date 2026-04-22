---
name: derive-spec
description: Turn a GDD section into a prototype-scoped spec with explicit cuts. Use for Phase 2 prototype scoping and any time new GDD territory enters the prototype.
---

# derive-spec

The GDD is deliberately over-designed for the prototype. This skill
produces the prototype-scoped spec by making the cuts **explicit** and
the rationale for each cut **reviewable**.

## What to do

1. Locate the GDD section(s) to be derived. Read them in full.
2. Produce a spec using the template at
   [`.cursor/templates/prototype-spec.md`](../../templates/prototype-spec.md).
3. For each GDD concept, attribute, mechanic, and system in the
   section, classify into one of:
   - **In scope at full fidelity** — implement as specified.
   - **In scope, simplified** — implement a named subset. Specify
     exactly what is kept and what is cut, and why.
   - **In scope, stubbed** — implement a placeholder interface so
     other systems can integrate, but no real logic.
   - **Out of scope** — not in the prototype at all.
4. For each cut, state the **re-expansion path**: what would need to
   change for the full GDD version to be restored later. This keeps
   the prototype from silently becoming the canonical design.
5. Extract any named concepts into a candidate addition to
   `.cursor/rules/30-domain-language.mdc`. (Propose the addition via
   `propose-adr` if the concept is new or redefined.)
6. Because specs live under `design/scope/`, writing them is
   Tier A and requires going through `propose-adr` for the scope
   change. Draft the spec, then wrap it in an ADR ("Scope change:
   derive <subsystem> from GDD §X") and run the full Tier A gate.

## Cut discipline

- **No implicit cuts.** If the GDD says something and the spec does
  not, that is a cut and it must be explicit.
- **No silent generalizations.** If the GDD specifies a number and
  the spec broadens it, that is a cut (fidelity down) and must be
  explicit.
- **No invented additions.** If the spec mentions something the GDD
  does not, that is either a derivation (note it) or an addition
  (requires a GDD edit via `propose-gdd-edit`, or an ADR that
  explicitly records the prototype-only addition).

## Hand-off

A derived spec becomes input to `draft-tech-design` for each
subsystem it describes.
