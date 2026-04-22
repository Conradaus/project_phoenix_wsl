# Prototype spec — Project Phoenix prototype scope

- **Governing GDD sections:** `design/gdd/GDD.md` — all sections, with
  §14.2 (Prototype Development Notes) as the author-authored seed this
  spec extends. Cited GDD sections are authoritative for their rules;
  this spec does not re-state them. Where this spec and the GDD
  disagree on a cited rule, this spec wins for the prototype.
- **Status:** Approved
- **Date:** 2026-04-22

## Non-technical summary

A networked 1v1 (2v2 stretch) turn-based PvP prototype for a
trusted-circle playtest. Full-fidelity combat loop; a representative
slice of characters, abilities, and equipment; no progression grind,
no economy, no hub scene, no social features. Max-level characters
allocated at creation. A rules-based Practice AI exists for solo
testing. Every cut has a re-expansion path so the prototype does not
calcify as canonical design.

## Success criteria

The playtest is designed to produce evidence on two primary questions.
Any other signal is secondary; blind spots are named in ADR 0001 so
test interpretation is honest.

- **Combat feel.** Does the turn loop + mitigation + Empower / Trigger
  / Conditional layer + Resolve / Ultimate arc produce strategic,
  readable, re-playable turns?
- **Build expression.** Do loadout, equipment, and mastery choices
  produce meaningfully different matches in the ways the GDD claims?

## Session + topology commitments

- **Topology:** networked PvP. Two humans on two machines,
  authoritative server mediates matches. No hotseat.
- **Authority model:** server-authoritative. The server owns turn
  state, hidden Reaction-Phase selection (§7.3.1), all RNG resolution
  (crits, dodges, Ignite queue ticks), and the legal-action
  enumerator. Clients send intents; the server resolves.
- **Anti-cheat posture:** the authority boundary exists to prevent
  obvious client-side cheating (forged RNG, peeking at hidden
  reactions, illegal actions). Production-grade anti-cheat is out of
  scope. Trusted-circle access is assumed for the first playtest.
- **Architecture is not pre-designed here.** Exact state-sync
  approach, message cadence, reconnect semantics, match-session
  lifecycle, and client-server contract are deferred to the Battle /
  network tech design, which is constrained to follow
  industry-standard server-authoritative patterns so the prototype's
  architecture is reusable in the full game.
- **Battle interface.** The Battle subsystem exposes a
  participant-agnostic interface: human clients, AI agents, and any
  future participant type are interchangeable consumers. Practice
  mode is the same Battle machine with an AI bound to one slot.

## Observability commitments

- **Combat event trace.** The server emits a structured per-match
  event log covering phase transitions, action selections (including
  hidden-until-resolution Reaction choices), resolution order, damage
  components, ailment applications, Ignite-queue state, trigger-chain
  activations and skips with skip reasons (proxy unavailable,
  conditional failure, suppression). Exportable per match. Dev and
  tester visible only, not player-facing.
- **Re-expansion:** replay capability is not committed;
  deterministic-seed inputs are not guaranteed. If playtests demand
  true replays, a follow-up ADR makes it explicit.

## In scope

### At full fidelity

These GDD sections apply **as written**, no modifications:

- **Character:** classes (§3.1), attributes and derived stats (§3.4),
  resources and Resolve (§3.5), Shield (§3.5.2).
- **Battle:** CTB initiative (§7.1), six-phase turn structure (§7.3),
  cooldowns (§7.5), mitigation pipeline (§7.7), accuracy / dodge
  (§7.8), debuff application (§7.9).
- **Abilities:** classification (§4.1), Basics (§4.4), Empowers
  (§4.5.5), Triggers (§4.5.6) — all four patterns (+Cooldown,
  +Depletion, +Blessing, Passive+Trigger) — Conditionals (§4.5.7),
  damage calculation and modifier order (§4.6), targeting (§4.7),
  crit (§4.9), status-effect taxonomy (§4.10), ailments (§7.6)
  including Ignite priority queue.
- **Equipment:** Weapon Swap (§6.1.3), Type / Rarity / Mod structure
  as it applies to Common-only items (§6.3, §6.5).
- **Loadout:** 5×2 Core grid + 2 Ultimate slots, per-slot Core
  leveling with Skill Points (§5.2.2, §5.2.3, §5.2.4, §4.8).
- **UI:** Base (Total) value display (§9.4.1), Battle HUD (§9.1)
  including §4.5.7 conditional border glow, Loadout and Equipment
  Management (§9.2.2, §9.2.3) with Weapon Set tabs, Character Sheet
  attributes and derived stats (§9.2.1) — character-model polish
  excluded.

Content-level statuses in scope: Stealth, Invulnerable, Slowed, Dazed
(§4.10.3), plus the structural Shield / Immune / Corrupted. The
Corrupted suppression edge case (§4.5.6) must be exercised by at
least one ability in the roster.

### Modifications to cited sections (not cuts)

These GDD rules are actively changed for the prototype, not merely
stripped:

- **§3.2 mastery unlock.** Masteries are selected at character
  creation, not unlocked at level 10 via the Class Trainer.
- **§3.6 progression cadence.** All 250 AP / 50 SP / 5 MP are
  allocated at character creation rather than earned across levels.
  The §3.6.1 level-up tutorial UX is not present.
- **§12.2 respec.** No respec flow. Delete-and-recreate is the only
  path.
- **§6.3.4 equipment attribute requirements.** Attribute-requirement
  gating is waived for the prototype. The Flexible Requirements
  *model* is preserved — equipment definitions may carry requirement
  values — but the enforcement check is disabled. This removes the
  gear-fit constraint for the shipped masteries against
  pure-attribute gear without adding hybrid content.

Downstream domain docs and tech designs cite both the GDD section
and this spec; this spec wins where they disagree for the prototype.

### Simplified

**Character progression.** (§3.6, §2.3.2)
- Kept: character creation allocates the full 250 AP / 50 SP / 5 MP.
- Cut: XP, leveling events, level-gated content.
- Re-expansion path: add XP, level-up event, level-based gating,
  respec.

**Masteries.** (§3.2, §3.3)
- Kept: one mastery per base class — Blademaster (Warrior),
  Pyromancer (Mage), Assassin (Rogue). Selected at creation. Each
  mastery ships with **at least 5 passive-tree nodes** (enough to
  spend 5 MP) and must include the mastery's GDD-named signature
  passive (e.g., Blademaster's 2H + offhand interaction per §3.3).
  Maximum depth is unconstrained; content pass decides.
- Structural note: the passive-tree data model is built at full
  fidelity (graph of nodes with effect bindings); node quantity is
  what varies. The build cost of the Mastery subsystem is not
  simplified, only its content volume.
- Cut: the other 9 masteries; level-10 gating (moot).
- Re-expansion path: add remaining masteries and expand trees.

**Loadout Tier restrictions.** (§5.2.1, marked WIP in the GDD)
- Kept: the 5-column visual grid. Loadout slots are modeled as
  `(column, row)` tuples from day one; `Tier` is a field on Core
  ability definitions, present but inert.
- Cut: the Tier-based eligibility rule on assignment.
- Re-expansion path: author Tier values on abilities; enable the
  check.

**Equipment type roster.** (§6.4)
- Kept: all 12 weapons; all 4 structural off-hands (Tower Shield,
  Kite Shield, Grimoire, Tome); dual-wield off-hand abilities
  (Thrust, Shank); all 11 rings; 4 pure-attribute armor per slot
  (12 total); 4 pure-attribute amulets.
- Cut: all 6 hybrid armor per slot (18 total); all 6 hybrid amulets
  + Opal (7 total). Mastery-to-gear fit is handled by waiving the
  attribute-requirement check (see Modifications), not by shipping
  matched hybrids.
- Re-expansion path: add hybrids as data; re-enable the requirement
  check when balancing demands it.

**Equipment rarity.** (§6.6, §14.2)
- Kept: all items ship at Common (★) with the Rank field *present
  and fixed*. Damage formulas (§4.6) continue to take Rank as an
  input; prototype data supplies the fixed value.
- Cut: rarity beyond Common, Rank progression (★★★+), Mods.
- Re-expansion path: populate higher rarities as data; the Mod
  system is a future tech design.

**Ability content volume.** (§11.2.2 targets ~20 Core + ~10 Ultimate
per class)
- Kept: ~10 Core + ~3 Ultimate per pool (Warrior, Mage, Rogue,
  Neutral) ≈ 52 abilities. Roster designed in a Phase-2.5 content
  pass under two coverage rubrics:
  - Taxonomic: every Action Type; every Empower / Trigger (all four
    Trigger patterns) / Conditional tag; one Basic per in-scope
    weapon type; ailment-applying abilities for Poison, Bleed,
    Ignite; at least one ability that applies Corrupted.
  - Interaction: at least one CONDITIONAL + EMPOWER + TRIGGER
    composite; at least one trigger-chain scenario that hits the
    stop-after-two rule (§4.5.6); at least one proxy-unavailable
    skip scenario; at least one multi-source Ignite scenario to
    exercise the priority queue.
- Cut: the remaining ~70 abilities.
- Re-expansion path: add abilities as data.

**Focus ability values.** (§4.4, Hex / Mend)
- Kept: Grimoire and Tome ship with placeholder Focus ability values
  (Hex, Mend) sufficient to make the ability legal in Battle; not
  tuned.
- Cut: balanced Focus tuning.
- Re-expansion path: tuning pass once Battle tech design lands.

**PvE.** (§2.3.3, §8.2, §8.3)
- Kept: Practice mode vs AI, fixed difficulty.
- Cut: Campaign, Quest system, Dungeons, customizable difficulty.
- Re-expansion path: Campaign and Quest are their own content
  systems.

**Practice mode AI.** (§2.3.3) — simplified, not stubbed
- Kept: Practice matches run through the normal Battle machine
  against an AI opponent. The AI is a "simple foe" rules-based
  agent; algorithm spec lives in the Practice-mode tech design.
- Capability floor: the AI must exercise the Reaction Phase, select
  Triggers, make Conditional-gated action choices, and apply
  ailments. Development-grade test scenarios rely on it; the ability
  roster's interaction-coverage rubric cannot be validated without
  it.
- Shared-logic constraint: the AI and the human client consume the
  **same legal-action enumerator** produced by the server. No
  duplicate "what can I press?" logic.
- Cut: the §2.3.3 difficulty tiers.
- Re-expansion path: add heuristics and difficulty tiers.

**Hub interface.** (§8.1, §9.3)
- Kept: a single navigation screen with cards for Battle Selection,
  Loadout, Character Sheet, Equipment.
- Cut: visual hub scene; all NPCs (economy cut with §14.2; the
  Class Trainer is obsoleted by mastery-at-creation).
- Re-expansion path: visual scene; restore NPCs alongside their
  systems.

### Stubbed

**Trinket and Consumable equipment slots.** (§6.1.1, §4.1.2 ITEM)
- Slot presence: the 5 Active slots appear in the equipment UI from
  day one. The loadout model reserves ITEM as a valid ability
  classification.
- Data shape: the ability-data schema for ITEM inhabitants (Trinket
  / Consumable mechanics) is *not* committed. Trinket activation is
  marked "details TBD" in GDD §6.1.1; the prototype does not invent
  a shape ahead of the GDD.
- Behavior: no ITEM abilities ship. Slots remain empty in any built
  loadout; the Consumable action path is not wired.
- Re-expansion path: propose a GDD edit specifying Trinket mechanics,
  author item data, enable the path.

## Out of scope

Inherited from GDD §14.2: Guild System, Dungeons, Tournaments,
Cosmetics, Art and Audio, equipment rarity beyond Common,
Rank / Temper / Hone progression, Salvage / Forge / Distill / Learn,
Gambler, Oracle, ability Rarity and Rank.

Added by this spec:

- **Character leveling and XP** (§3.6). Why out: the prototype tests
  combat feel and build expression at max level; the leveling loop
  is a separate signal.
- **Respec flow** (§12.2). Why out: delete-and-recreate covers the
  prototype's need; respec UX is a separate surface.
- **Masteries other than Blademaster, Pyromancer, Assassin** (§3.2).
  Why out: content-authoring cost; chosen trio stresses the
  highest-value mechanics (Weapon Swap, Ignite queue, Stealth).
- **Hybrid armor and amulets; Opal** (§6.4.3, §6.4.4). Why out: the
  waived requirement check (see Modifications) removes the need to
  ship matched hybrids.
- **Loadout Tier eligibility check** (§5.2.1). Why out: the GDD
  marks this WIP; the field is modeled but the check is not applied.
- **Campaign PvE** (§8.2) and **Quest system** (§8.3.2). Why out:
  PvP is the primary playtest vehicle.
- **Social features** — Guild Hall, Tavern, Friends List (§10).
  Why out: no playtest signal required; cut with the economy.
- **Battle environment effects** (§7.11). Why out: terrain /
  environment tempo is a separate balance signal.
- **Trinket and Consumable item rosters**. Why out: GDD §6.1.1
  marks Trinket mechanics "details TBD"; slots are stubbed above.
- **The ~70 abilities not drafted for the prototype's ~52**
  (§11.2.2). Why out: content volume.
- **Production-grade anti-cheat.** Why out: authority boundary alone
  is the cheat-prevention bar for the trusted-circle playtest.
- **Polish UI:** character model in Character Sheet (§9.2.1),
  battle-log animation (§9.1.4), equipment comparison tooltips
  (§9.2.3), initiative bar animations (§9.1.2). Why out: not needed
  for functional playtest signal.
- **Match replays, deterministic-seed input logs.** Why out: the
  combat event trace covers tester-bug triage; replays are
  re-expansion.
- **Deployment target.** Why out: Phase-7 ADR concern (where the
  server runs) not this spec.

## Named concepts introduced or redefined

This spec introduces no new named concepts. All terms derive from
the GDD glossary (§14.1) per `.cursor/rules/30-domain-language.mdc`.
The Modifications to cited sections block captures rules this spec
*changes* for the prototype, but uses no new vocabulary.

## Invariants this subsystem must preserve

Invariants are owned by the GDD; this spec cites the sections they
live in rather than re-stating them. Downstream docs cite the GDD
for the rule and this spec for any prototype-specific modification.

- **Combat state machine invariants.** GDD §7.3 (turn structure),
  §7.1 (initiative), §7.5 (cooldowns), §7.7 (mitigation).
- **Ability resolution invariants.** GDD §4.5.6 (Trigger chain
  stop-after-two, proxy unavailability, suppression), §4.5.7
  (Conditional commit-after-selection, trigger-path silent skip),
  §4.6 (modifier order, damage calculation).
- **Resource invariants.** GDD §3.5 (resources and Resolve), §3.5.2
  (Shield FIFO).
- **Ailment invariants.** GDD §7.6 including §7.6.3 Ignite priority
  queue.
- **Loadout invariants.** GDD §5.2.4 (per-slot leveling), §4.8
  (scaling per level).
- **Display invariants.** GDD §9.4.1 Base (Total) convention, §9.1
  Battle HUD structural elements.
- **Networked-session invariants** (prototype-specific): single
  legal-action enumerator authored by the server; clients send
  intents only; hidden Reaction-Phase selection never leaves the
  server until resolution.

## Cross-domain seams (named for downstream docs)

- **Equipment × Ability.** One Basic ability per in-scope weapon
  type (§4.4 / §6.4.1). Ability data cites its weapon-type binding.
- **Ability × Battle.** Ailment application is owned by Ability
  execution; the Ignite priority queue is owned by Battle state.
- **Loadout × Ability.** Per-slot Core leveling (§5.2.4). Level is
  stored on the loadout slot, not on the ability definition.
- **Battle × AI × Network.** The single legal-action enumerator
  lives on the server and is consumed identically by human clients
  and the Practice AI. No client-side re-derivation of legality.

## Dependencies on other subsystems

- **Depends on:** `design/gdd/GDD.md` (GDD §14.2 in particular) and
  the full GDD as canonical.
- **Depended on by:** all future domain docs, tech designs, ADRs,
  and implementation until superseded.

## Open questions

Deferred to later gates, not resolved here:

- Battle / network tech design — the exact state-sync approach,
  message cadence, reconnect and desync policy, match-session
  lifecycle, and client-server contract. Constrained by this spec
  to be server-authoritative and to follow industry-standard
  patterns suitable for extension to the full game.
- Match-replay / deterministic-input ADR — only if playtest demands
  it.
- Stack selection — Phase-3 ADR (anticipated ADR 0002).
- Mastery passive-tree node lists for the 3 included masteries —
  Phase-2.5 content pass.
- Ability roster — Phase-2.5 content pass, under the two coverage
  rubrics above.
- Practice AI algorithm — Practice-mode tech design, under the
  capability floor above.
- Focus ability values (Hex, Mend) balance tuning — after Battle
  tech design.
