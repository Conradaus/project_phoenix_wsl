# Design index

Master cross-reference for Project Phoenix's canonical design chain.
Every entry below points at the canonical artifact and notes what
derives from it and what depends on it.

This file is updated by the `propose-adr`, `derive-spec`,
`draft-tech-design`, and `propose-gdd-edit` skills when they produce
or accept artifacts. Keep entries concise — this is an index, not a
re-explanation.

## Status: Phase 1 ingest complete

The GDD has been copied into [`design/gdd/GDD.md`](gdd/GDD.md).
Canonical vocabulary has been extracted from the GDD's own
Section 14.1 glossary into
[`.cursor/rules/30-domain-language.mdc`](../.cursor/rules/30-domain-language.mdc).
An apparent-scope summary derived from Section 14.2 of the GDD is in
[`design/gdd/apparent-scope-summary.md`](gdd/apparent-scope-summary.md).

No scope decision (Phase 2) has been made. No domain docs (Phase 4),
tech designs (Phase 3+), or ADRs exist yet.

## GDD — `design/gdd/`

[`design/gdd/GDD.md`](gdd/GDD.md) — full Game Design Document, 3080 lines.

### Section map

| # | Section | Anchor | Governs downstream |
|---|---------|--------|--------------------|
| 1 | Design Principles | [#1-design-principles](gdd/GDD.md#1-design-principles) | Cross-cutting design lens for all ADRs |
| 2 | Game Overview | [#2-game-overview](gdd/GDD.md#2-game-overview) | Prototype scope framing, game structure |
| 3 | Character System | [#3-character-system](gdd/GDD.md#3-character-system) | Character domain doc, attribute/resource/progression subsystems |
| 4 | Ability System | [#4-ability-system](gdd/GDD.md#4-ability-system) | Ability domain doc, classification, targeting, scaling, status effects |
| 5 | Character Loadouts | [#5-character-loadouts](gdd/GDD.md#5-character-loadouts) | Loadout domain doc, ability grid, skill points |
| 6 | Equipment System | [#6-equipment-system](gdd/GDD.md#6-equipment-system) | Equipment domain doc, types, rarity/rank, crafting |
| 7 | Battle System | [#7-battle-system](gdd/GDD.md#7-battle-system) | Battle/combat domain doc, turn structure, mitigation |
| 8 | Game World & Progression | [#8-game-world--progression](gdd/GDD.md#8-game-world--progression) | Hub, PvE/PvP, campaign, quest system |
| 9 | User Interface | [#9-user-interface](gdd/GDD.md#9-user-interface) | UI tech designs, battle HUD, character management |
| 10 | Social Features | [#10-social-features](gdd/GDD.md#10-social-features) | (Mostly out of prototype scope) |
| 11 | Economy | [#11-economy](gdd/GDD.md#11-economy) | Currency, NPCs, acquisition, crafting loops |
| 12 | Monetization Strategy | [#12-monetization-strategy](gdd/GDD.md#12-monetization-strategy) | (Out of prototype scope) |
| 13 | Art and Audio | [#13-art-and-audio](gdd/GDD.md#13-art-and-audio) | (Mostly TBD, out of prototype scope) |
| 14 | Appendices | [#14-appendices](gdd/GDD.md#14-appendices) | Glossary (§14.1) is canon for vocabulary; prototype scope notes (§14.2) seed Phase 2 |

## Prototype scope — `design/scope/`

_Empty. Produced in Phase 2 via `derive-spec` wrapped in an ADR._

The GDD's own Section 14.2 is the author-authored starting point for
the prototype-scope decision; see
[`design/gdd/apparent-scope-summary.md`](gdd/apparent-scope-summary.md)
for a derived summary that maps it to GDD sections.

- `design/scope/prototype-scope.md` — _(pending Phase 2)_

## Domain models — `design/domain/`

_Empty. Produced in Phase 4, one per in-scope subsystem._

Anticipated (not yet canonical; will be decided in Phase 2):

- Character (derives from GDD §3)
- Ability (derives from GDD §4)
- Loadout (derives from GDD §5)
- Equipment (derives from GDD §6)
- Battle (derives from GDD §7)

## Tech designs — `design/tech/`

_Empty. Produced in Phase 3 onward, one per subsystem. Each tech
design cites its governing domain doc and the ADRs that bear on it._

## ADRs — `design/decisions/`

_Empty. First ADR is expected to be `0001-stack-selection.md` in Phase 3._

### ADR log

| # | Title | Status | Date | Supersedes |
|---|-------|--------|------|------------|
|   |       |        |      |            |

## Cross-reference (populated as artifacts accrue)

### Subsystem → governing artifacts

| Subsystem | Domain doc | Tech design | Key ADRs |
|-----------|------------|-------------|----------|
|           |            |             |          |

### ADR → affected subsystems

| ADR | Subsystems affected |
|-----|---------------------|
|     |                     |

### Follow-ups ledger

Deferred concerns from accepted ADRs and tech designs that are
tracked outside the artifact itself.

| Origin | Description | Due | Status |
|--------|-------------|-----|--------|
|        |             |     |        |
