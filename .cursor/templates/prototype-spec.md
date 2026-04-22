# Prototype spec — <subsystem or section>

- **Governing GDD sections:** <paths and headings>
- **Status:** Draft | Approved
- **Date:** YYYY-MM-DD

## Non-technical summary

<One short paragraph: what of the GDD this prototype will and will not
implement, in plain English.>

## In scope

### At full fidelity
- <concept / mechanic>: <GDD source>
- ...

### Simplified
- <concept / mechanic>: <GDD source>
  - Kept: <what is kept>
  - Cut: <what is cut>
  - Re-expansion path: <what restoring the full version would require>
- ...

### Stubbed
- <concept / mechanic>: <GDD source>
  - Interface kept so <other subsystems> can integrate.
  - Real logic deferred to: <post-prototype path>
- ...

## Out of scope

- <concept / mechanic>: <GDD source>
  - Why out: <reason>
- ...

## Named concepts introduced or redefined

Each must appear in `.cursor/rules/30-domain-language.mdc`. If a name
in this spec is new or redefines a GDD term, call it out here.

- <name>: <source, or "new for prototype">

## Invariants this subsystem must preserve

- <invariant> (GDD source: ...)
- ...

## Dependencies on other subsystems

- Depends on: <list>
- Depended on by: <list>

## Open questions

- <question>
- ...
