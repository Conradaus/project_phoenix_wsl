---
name: drift-audit
description: Compare current code and doc state to the canonical chain. Surface deltas, uncited changes, undocumented concepts, and dead docs. Run on demand or periodically.
---

# drift-audit

This skill is the slow-creep catcher. Even with the review gates in
place, small drifts accumulate — a term renamed without updating the
glossary, a behavior tweaked without updating the spec, an ADR quietly
contradicted by a later change. This skill runs the whole graph and
reports it.

## What to do

1. Enumerate all canonical docs: GDD, scope, domain, tech, decisions.
2. Enumerate all code (once the project has code).
3. For each layer, compare against the layer above:
   - **Scope vs GDD:** does every in-scope subsystem still trace to a
     GDD section? Has any GDD section changed in a way the scope
     should have acknowledged?
   - **Domain vs scope:** does every domain doc correspond to a
     subsystem listed in scope? Any scope items lacking a domain doc?
   - **Tech vs domain:** every subsystem has a tech design? Every
     tech design still implements its domain doc accurately?
   - **ADRs vs tech/domain:** are there decisions visible in the
     tech designs or code that should have had an ADR but do not?
   - **Code vs tech:** are modules, types, and flows still matching
     their tech designs? Any modules without a tech-design parent?
4. Produce a report in the format of
   [`.cursor/templates/drift-audit-report.md`](../../templates/drift-audit-report.md).
5. Classify each finding:
   - **Drift (red)** — live contradiction; must be fixed or ADR'd.
   - **Stale (yellow)** — docs lagging code; update required but no
     contradiction yet.
   - **Orphan (yellow)** — docs or code without a traceable parent.
   - **Missing (yellow)** — expected artifact doesn't exist.
6. For each red finding, produce a proposed remediation: either a
   code fix or an ADR draft (the latter via `propose-adr`).

## Invocation

- **On demand:** "Run a drift audit on the Combat subsystem" or
  "Run a full drift audit."
- **Scheduled:** Later (Phase 7+), consider wiring this to a Cursor
  Automation with a cron trigger, posting the report to a predictable
  location.

## Output discipline

- The audit is a **report**, not an action. It must not make changes
  on its own. Remediations go through their normal gates.
- The report is concise. Each finding is one bullet with a
  path citation. Details only when the human asks.
