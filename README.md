# Project Phoenix

A prototype of a complex, competitive, turn-based PvP RPG, built
primarily through AI agents by a solo game designer. This repository
is as much a **workflow** as it is a codebase — the way work is done
here is intentional and strict, because the human cannot reliably
catch code-level drift.

If you are a human returning to this project after time away, read
this file, then [`AGENTS.md`](AGENTS.md), then
[`design/index.md`](design/index.md), in that order.

If you are an AI agent starting a new session, read
[`AGENTS.md`](AGENTS.md) in full, produce a session brief via the
`session-brief` skill, and have the `canon-guardian` subagent verify
the brief before proceeding.

## Why this workflow exists

A solo non-programmer cannot reliably catch technical drift in code.
The workflow in this repo pushes every review gate **upstream to
design artifacts the human can judge**: specs, domain models, ADRs,
plain-English summaries. Code is derived mechanically from these
approved artifacts. When drift happens, it surfaces loudly — at a
hook, at a verifier pass, or in a plain-English summary — rather
than compounding silently.

The core rules are:

- There is a single canonical chain of truth:
  `GDD -> Scope -> Domain -> Tech -> ADRs -> Code`. Every technical
  artifact must trace to its parent.
- Every change is classified into a tier (A, B, or C) before work
  begins, and is gated by the tier's requirements. Tier A changes
  are reviewed by a role quartet (architect, engineer, game-designer,
  operator) plus a skeptic before any code is written.
- Canonical paths (`design/gdd/**`, `design/scope/**`,
  `design/decisions/**`) are hook-protected and can only be edited
  through sanctioned skills.
- Every human-facing gate includes a plain-English summary
  (`explain-like-im-not-a-coder`).

Full detail in [`AGENTS.md`](AGENTS.md).

## Repository map

```
AGENTS.md                    Agent handbook — read first.
README.md                    This file.
Documents/                   Inbox for source materials (GDD, references).
design/
  index.md                   Master cross-reference.
  gdd/                       Canonical Game Design Document (hook-protected).
  scope/                     Prototype scope (hook-protected).
  domain/                    Domain models, one per concept.
  tech/                      Tech designs, one per subsystem.
  decisions/                 ADRs, numbered. (hook-protected)
.cursor/
  rules/                     Always-applied / intelligent agent rules.
  skills/                    Progressive skills invoked on demand.
  agents/                    Subagent definitions (function, role, adversarial).
  hooks.json                 Hook registration.
  hooks/                     Hook scripts.
  templates/                 Reusable starter content for canonical docs.
```

## Phase roadmap

- **Phase 0 — workflow infrastructure.** Complete. All rules, skills,
  subagents, hooks, and templates are in place.
- **Phase 1 — GDD ingest.** Pending. Move the GDD from `Documents/`
  into `design/gdd/`, build `design/index.md` cross-references,
  populate `.cursor/rules/30-domain-language.mdc` with canonical
  vocabulary.
- **Phase 2 — prototype scope.** Tier A decision: which GDD
  subsystems make the prototype, at what fidelity.
- **Phase 3 — technical architecture.** Stack ADR and follow-on ADRs
  for deployment, persistence, client/server contract, state
  management.
- **Phase 4 — domain models.** One doc per in-scope subsystem with
  state diagrams and invariants.
- **Phase 5 — scaffolding.** First `hello-world` through the full
  gate workflow as a live drill.
- **Phase 6 — iterative features.** Feature loop: domain doc → tech
  design → ADRs → implementation → verifier → plain-English
  summary → commit.
- **Phase 7 — small-remote playtest deployment.** Deploy, iterate,
  establish a periodic drift-audit cadence.

## For future-you

If you come back to this after a long absence and cannot remember
how any of this works:

1. Read `AGENTS.md`. It is the handbook.
2. Run `ls design/decisions/` to see what has been decided.
3. Open `design/index.md` to see what is connected to what.
4. Tell the agent to "run the session-brief skill for <task>" and
   review the brief it produces. That is the canonical session
   start. Do not skip it.

## A note on pace

This workflow is deliberately slow on Tier A decisions. That is the
cost of drift resistance, and it is worth it on a project of this
length. If a decision feels too expensive to route through the full
Tier A gate, it is almost certainly Tier A and you need the gate
most.
