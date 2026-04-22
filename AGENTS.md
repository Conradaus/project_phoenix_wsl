# Project Phoenix — Agent Handbook

> This file is the single entry point for every AI session in this repo.
> Read it in full at the start of every session. Cite it by name when you bootstrap.

Project Phoenix is a prototype of a complex, competitive, turn-based PvP RPG.
It is being built by a solo game designer (non-programmer) working primarily
through AI agents. The workflow in this file exists because the human cannot
reliably catch code-level mistakes — so review must happen at the document
layer, where the human is the expert.

If you are an agent, your job is not just to implement. Your job is to keep
the design canonical, make drift loud, and refuse to make silent decisions.

---

## 1. The hierarchy of truth

Every technical artifact in this repo is derived from the one above it.
AI drafts; human approves; the approved version becomes canonical and is
then referenced, not re-derived. If code disagrees with a doc, the doc
wins — or the doc is updated through a sanctioned skill and an ADR.

```
GDD                (design/gdd/)          human-owned, hook-protected
  -> Prototype Scope (design/scope/)      what of the GDD is in this prototype
    -> Domain Models (design/domain/)     entities, states, invariants
      -> Tech Designs (design/tech/)      how each subsystem is built
        -> ADRs       (design/decisions/) individual technical decisions
          -> Code                         derived; must cite its parent
```

The master cross-reference lives at [`design/index.md`](design/index.md).

## 2. Tiered review gates

Every proposed change must be classified into one of three tiers at the
start of planning. The `verifier` subagent double-checks the classification
after the change. Mis-classification is itself a drift event.

### Tier A — strict gate (markdown-first)

**Triggers:** introducing or changing a domain concept, a technical boundary
(new service, DB, protocol, major dependency), a module interface (shared
types, API contracts), or any rule / balance value derived from the GDD.

**Process:**
1. AI drafts an ADR (and a spec or tech-design update if needed).
2. The role quartet — `architect`, `engineer`, `game-designer`, `operator` —
   runs in parallel against the draft, each producing a structured critique.
3. AI synthesizes the four critiques into an `Addressed concerns` section
   on the revised ADR.
4. `skeptic` subagent does a final adversarial pass.
5. Human reviews the synthesis (raw critiques collapsed underneath) and
   explicitly approves before any code is written.
6. Implementation proceeds in Agent Mode, citing the approved ADR.
7. `verifier` subagent reviews the diff against the ADR.
8. `explain-like-im-not-a-coder` skill produces a plain-English change
   summary. Human approves the change. Commit cites the ADR.

### Tier B — light gate

**Triggers:** implementation within an already-approved spec; refactoring
that preserves interfaces; adding tests; fixing a bug without changing
specified behavior.

**Process:** plan-mode plan → implement → `verifier` → plain-English
summary → human approval → commit citing the parent spec.

### Tier C — auto

**Triggers:** formatting, comments, obvious typo fixes.

**Process:** happens inline; surfaced in the session summary; no gate.

**If a change does not clearly fit Tier B or Tier C, treat it as Tier A.**
When in doubt, tier up.

## 3. Session start procedure

Every session begins with the `session-brief` skill, which produces a
one-screen artifact answering:

1. What are we trying to accomplish this session?
2. Which canonical docs govern this work? (cite paths)
3. What subset of those docs is currently relevant? (cite sections)
4. What is the proposed tier for the planned change?
5. What is unknown or ambiguous? (ask the human before proceeding)

Then the `canon-guardian` subagent verifies the brief is accurate before
any further work begins.

## 4. Directory map

```
AGENTS.md                          <- you are here
README.md                          <- workspace overview for the human
.cursor/
  rules/                           <- always-applied / intelligent rules
  skills/                          <- progressive, invoked on demand
  agents/                          <- subagent definitions
  hooks/                           <- hook scripts (called by hooks.json)
  hooks.json                       <- hook registration
  templates/                       <- reusable starter content
design/
  index.md                         <- canonical cross-reference
  gdd/                             <- GDD (hook-protected)
  scope/                           <- prototype-scope.md (Phase 2)
  domain/                          <- one doc per domain concept (Phase 4+)
  tech/                            <- one tech design per subsystem (Phase 3+)
  decisions/                       <- numbered ADRs
    TEMPLATE.md
Documents/                         <- inbox for source material (GDD lives here pre-ingest)
```

## 5. Anti-patterns (reject these on sight)

- **Silent decisions.** If you are about to pick an option that has more than
  one reasonable answer, stop and produce an ADR, or ask the human.
- **Uncited changes.** Every non-Tier-C change must cite its parent spec
  or ADR in the commit message and in the change summary.
- **Drive-by edits.** Do not modify files outside the stated scope of the
  current change, even if you spot something you'd like to fix. Queue it
  as a follow-up instead.
- **Editing canonical design directly.** `design/gdd/**`, `design/scope/**`,
  and `design/decisions/**` are hook-protected. Modify them only through
  the `propose-gdd-edit` or `propose-adr` skills, which produce a
  reviewable diff for the human.
- **Guessing.** If a required fact is unknown, ask the human. Silence is
  the exact failure mode this workflow exists to prevent.
- **Refactoring without an ADR when the refactor crosses a module
  boundary.** If it is an interface change, it is Tier A.
- **Bypassing the role quartet on Tier A.** The four-voice review is the
  main drift defense; collapsing it into a single opinion defeats the
  purpose.

## 6. What "done" means for a change

A change is only complete when:

1. The tier was declared and honored.
2. All required reviews (quartet + skeptic for Tier A; verifier for Tier B)
   have run and their critiques are either addressed or explicitly deferred
   with a tracked follow-up.
3. A plain-English summary exists for the human.
4. The commit message cites the governing doc.
5. The human has approved.

## 7. Model selection

- Function subagents may use `fast` models to keep gate costs low.
- Role subagents that require depth (`architect`, `game-designer`, `skeptic`)
  should use `inherit`.
- The parent agent decides per-session which model is right; when in
  doubt on a Tier A deliberation, escalate.

## 8. Plain-English commitment

The human cannot reliably read code-level reasoning. Every gate the human
touches must have a plain-English artifact sitting in front of it. The
`explain-like-im-not-a-coder` skill exists to guarantee this. If you are
about to hand the human a diff without a plain-English summary, stop.
