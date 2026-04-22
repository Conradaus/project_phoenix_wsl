# ADR 0001 — Prototype scope

- **Status:** Accepted
- **Date:** 2026-04-22
- **Related:** `design/scope/prototype-scope.md`, `design/gdd/GDD.md`
  §14.2

## Non-technical summary

This decision says what our prototype is, and equally importantly,
what it is for. It is a small, playable slice of the game designed
for a trusted circle of testers to play networked 1v1 PvP matches on
their own machines. Its job is to produce evidence on two questions:
does combat feel good, and does choosing a character, loadout, and
gear actually change how matches play? To produce that evidence
honestly, the combat engine is built at full fidelity, with three of
the twelve masteries and roughly fifty abilities. We run the
networking server-authoritatively from day one — that way the
architecture does not get rebuilt when the prototype becomes the
full game, and obvious cheating is prevented by construction rather
than by policy. We deliberately leave out leveling, loot, crafting,
hub scenes, social features, and campaign. Every cut is named, and
each names the test data it does not produce, so we do not mistake
the prototype's playtest for evidence it was not built to give.

## Context

- `AGENTS.md` and `.cursor/rules/10-tiered-gates.mdc` classify scope
  decisions as Tier A. `design/scope/**` and `design/decisions/**`
  are hook-protected.
- GDD §14.2 (Prototype Development Notes) is the author-authored
  seed but intentionally does not resolve every open scope question.
  The Phase-1 summary at `design/gdd/apparent-scope-summary.md`
  enumerated the open questions; this ADR and its governed spec
  resolve them.
- Prototype purpose: trusted-circle networked 1v1 (stretch 2v2) PvP
  playtest.
- The 12 open scope questions were walked conversationally with the
  human. The resulting draft was then reviewed by the full Tier A
  role quartet (architect, engineer, game-designer, operator) plus
  skeptic. Critiques are consolidated in Addressed concerns below.

## Decision

Accept `design/scope/prototype-scope.md` as the governing
prototype-scope artifact. Its Simplified, Stubbed, and Out-of-scope
classifications are binding for all downstream domain docs, tech
designs, ADRs, and implementation until superseded.

Commitments in the spec that carry material architectural or scope
weight:

- **Networked, server-authoritative PvP from day one.** No hotseat.
  The server owns turn state, hidden Reaction-Phase selection, RNG
  resolution, and the legal-action enumerator. Exact network
  architecture (sync approach, message cadence, reconnect semantics)
  is deferred to the Battle / network tech design, which must follow
  industry-standard patterns suitable for extension to the full game.
- **Basic cheat-prevention via the authority boundary.** The
  authority split exists to prevent obvious client-side cheating;
  production-grade anti-cheat is out of scope for the trusted-circle
  playtest.
- **Full-fidelity combat state machine** — six-phase turn loop, CTB
  initiative, hidden Reaction-Phase selection, mitigation pipeline,
  ability classification and all four Trigger patterns, Conditional
  and Empower layers, ailments including the Ignite priority queue,
  four content statuses plus the structural three, Weapon Swap,
  Base / Total UI convention.
- **Acknowledged modifications to cited GDD rules.** Mastery
  selection moved to character creation; full AP / SP / MP
  allocation at creation; respec cut; equipment
  attribute-requirement gating waived.
- **Three masteries.** Blademaster, Pyromancer, Assassin — chosen
  to stress Weapon Swap, Ignite queue, and Stealth respectively.
  Each ships with a passive-tree node floor of 5 and its GDD-named
  signature passive. The Mastery Passive Tree subsystem is built
  at full fidelity; only content volume is cut.
- **Equipment:** all 12 weapons, 4 off-hands + dual-wield abilities,
  11 rings, pure-attribute armor and amulets only. Attribute
  requirements waived so any mastery can wear any gear. Common (★)
  rarity with Rank field modeled and fixed.
- **Ability roster** ≈ 52 (~10 Core + ~3 Ultimate per pool),
  designed under both taxonomic and interaction coverage rubrics.
- **Grimoire / Tome Focus abilities** ship with engineer-placeholder
  values for Hex and Mend; tuning deferred.
- **Practice mode** vs a simplified AI agent (not a stub) with a
  named capability floor — must exercise Reactions, Triggers,
  Conditionals, and ailment application — consuming the same
  legal-action enumerator as human clients.
- **Hub** is a single navigation screen, no scene, no NPCs.
- **Trinket and Consumable slots** present in the equipment UI as a
  sentinel scaffold. ITEM ability classification reserved in the
  loadout model. No ITEM inhabitant schema committed; no items ship.
- **Dev-only combat event trace** emitted by the server as an
  observability floor for tester-bug triage.

## Alternatives considered

### Alternative 1 — Minimum-viable PvP

- Summary: cut further — no masteries, minimal status breadth,
  ~20 abilities, no Practice AI.
- Why rejected: removes too much of the design's identity to produce
  useful signal on either success criterion. The combat-feel signal
  depends on Empower / Trigger / Conditional breadth; the
  build-expression signal depends on mastery identity.

### Alternative 2 — Faithful GDD subset

- Summary: keep all 12 masteries, the full ~120-ability roster,
  Campaign mode, full hybrid equipment.
- Why rejected: content-authoring and balance workload exceed the
  trusted-circle playtest window. Signal collected against a
  partially tuned superset is lower-quality than signal collected
  against a tightly scoped subset.

### Alternative 3 — Single-class vertical slice

- Summary: ship Warrior only — one base class, one mastery,
  mirror-match PvP.
- Why rejected: strips class-asymmetry, which is load-bearing for
  the build-expression success criterion. Mirror-match PvP does not
  answer "do loadout / equipment / mastery choices differentiate
  matches?"

### Alternative 4 — Pure (non-hybrid) mastery trio

- Summary: ship Berserker (STR), Sorcerer (INT), Ranger (DEX)
  instead of the hybrid trio. All three use single-attribute focus,
  so pure-attribute gear fits without modification.
- Why rejected: pure masteries stress fewer combat mechanics — no
  Weapon Swap primary, no Ignite primary, no Stealth primary — which
  is worse for the combat-feel success criterion. The hybrid-gear
  concern that motivated this alternative is resolved more cheaply
  by waiving the equipment attribute-requirement check for the
  prototype.

### Alternative 5 — Hotseat first, networked later

- Summary: two humans on one shared machine for the first playtest;
  add networking in a second playtest phase.
- Why rejected: introduces hotseat-specific rules into the Battle
  subsystem's interfaces (who owns input when, how hidden reactions
  are rendered) that would be refactored out on the transition to
  networked play. Building server-authoritative from day one avoids
  that architectural drift and lets the prototype serve as a
  best-practice reference for the full game's networking.

## Consequences

### Positive

- Playable networked PvP playtest achievable in a bounded window.
- Combat engine built at full fidelity; tech designs will not need
  rework when deferred systems are added.
- Networking architecture built once, reusable for the full game.
- Every cut has a re-expansion path.
- Observability floor named, so tester reports are actionable.

### Negative (accepted)

On combat feel (primary success criterion):
- Environment effects (§7.11) are cut; tempo and terrain
  interactions are not diagnostic.
- Common-only rarity with no Mods skews TTK and utility-item feel
  toward the raw-stat end of the GDD's intended mix.
- Ultimate roster at ~3 per pool is below the §11.2.2 ~10 target;
  Ultimate variety and Resolve-tempo feel are only partially
  diagnostic.

On build expression (primary success criterion):
- Only 3 of 12 masteries ship; cross-mastery comparison within a
  class is not diagnostic (no Blademaster vs. Berserker matchup).
- Playtest cannot distinguish base-class identity from mastery
  identity (every Warrior is a Blademaster, etc.).
- Loadout Tier restrictions (§5.2.1) are cut; balance complaints
  need filtering for "combo reachable under Tier rules."
- Equipment attribute-requirement gating is waived; the Flexible
  Requirements UX and mastery-via-gear-pressure design lever are
  not diagnostic.
- Delete-and-recreate instead of respec biases testers toward
  single-build commitment.
- Focus tuning uses placeholder values; Grimoire / Tome build
  strength is not diagnostic.

On other outcomes:
- No economy signal — acquisition UX, drop-rate tuning, and Mod
  utility are all untested.
- Practice AI is rules-based and simple; its algorithm is itself a
  design surface with its own tech design.
- Networked PvP introduces first-class integration risks
  (disconnect, desync, reconnect, mid-turn failures); the Battle
  tech design must address these explicitly.
- Cheat-prevention is authority-boundary only; no client-tampering
  defense, no rate limiting, no telemetry-based detection. Must be
  revisited before any non-trusted-circle access.
- The dev event trace is not a replay; reproducing disputed
  interactions relies on log reconstruction, not re-execution.

### Future decisions made harder

- The Battle / network tech design must define authority split,
  state-sync approach, and disconnect / reconnect / desync policy
  following industry-standard patterns.
- The Practice-mode tech design is itself an AI-design surface and
  must be reviewed by game-designer before engineer implementation.
- Stack-selection ADR must support every in-scope mechanic *plus*
  networked PvP from day one.
- Future scope expansions each require their own ADR citing this
  one.
- A Trinket GDD edit is required before Trinket / Consumable items
  can ship.
- A production-grade anti-cheat posture must be decided before the
  prototype serves non-trusted-circle players.

## Addressed concerns

Synthesis of the role-quartet and skeptic critiques. Raw critiques
were collected during drafting and are summarized per-role below.
Each concern is either resolved in the Decision, accepted as a
Consequence, or explicitly deferred with a tracked follow-up.

### architect

- Concern: **Networking / authority seam is unnamed.** Deferring
  "deployment target" to Phase 7 conflated where the server runs
  with what networking means for Battle's interfaces.
  Resolution: Resolved in Decision — networked server-authoritative
  PvP committed; exact architecture deferred under named constraints
  to the Battle / network tech design.
- Concern: **"ITEM ability type remains a valid classification"
  under-specified the shape commitment.** Sentinel vs data-shape
  stub was ambiguous.
  Resolution: Resolved in Decision — slot presence modeled; ITEM
  inhabitant schema not committed until the Trinket GDD edit lands.
- Concern: **Rank / Tier field shape for cut systems unspecified.**
  Domain docs would otherwise invent a shape from silence.
  Resolution: Resolved in Decision — Rank field modeled and fixed;
  Tier field modeled and inert.
- Concern: **"Apply as written" sections had unacknowledged rule
  changes** (mastery-at-creation, full-allocation-at-creation,
  Character Sheet citation conflict).
  Resolution: Resolved in Decision — new "Modifications to cited
  sections" block in the spec, and a citation-precedence rule
  (this spec wins over the GDD for the prototype where they
  disagree).
- Concern: **"Simplified masteries" hides a full-fidelity Mastery
  subsystem build cost.** Quantity cut ≠ structural cut.
  Resolution: Accepted as consequence — spec names this structurally;
  ADR Consequences list content-authoring regression cost as a
  negative.
- Concern: **Joint invariants across subsystems not named.**
  Equipment×Ability, Ability×Battle, Loadout×Ability seams were
  silent.
  Resolution: Resolved in Decision — new "Cross-domain seams"
  section in the spec names the four load-bearing edges.
- Concern: **Practice Mode's "normal battle UI" clause is a
  boundary commitment, not an AI-spec footnote.**
  Resolution: Resolved in Decision — spec elevates the
  participant-agnostic Battle interface and the shared legal-action
  enumerator to explicit commitments.

### engineer

- Concern: **"Full fidelity" stack height vs first-pass quality.**
  The combined state machine has N² interaction paths; a first pass
  is likely to ship with correctness bugs in edges unless a
  systematic test harness is budgeted.
  Resolution: Accepted as consequence — ADR scopes "no rework" to
  combat-design rules, not implementation. Scenario test harness
  tracked as follow-up for the Battle tech design.
- Concern: **~52-ability mandatory tag coverage is a hidden
  multiplier.** Content + QA cost, not engine cost.
  Resolution: Deferred — Phase-2.5 content pass carries the cost
  under both taxonomic and interaction rubrics.
- Concern: **Practice AI and Focus (Hex / Mend) left open while
  both are in the battle path.**
  Resolution: Partial resolution — Practice AI reclassified as
  simplified with named capability floor; Focus abilities ship with
  placeholder values sufficient to make them legal. Tuning is a
  follow-up.
- Concern: **ITEM slot stub with no items risks unexercised code
  paths.**
  Resolution: Deferred — slot scaffold kept (architectural tradeoff
  for cheap re-expansion); the Battle tech design's scenario test
  harness must exercise the latent ITEM path.
- Concern: **Practice AI interface coupling could drift from the
  human path.**
  Resolution: Resolved in Decision — single legal-action enumerator
  on the server, consumed identically by human clients and AI.
- Concern: **Rank / Rarity / Mods cut must remain representable in
  formulas.**
  Resolution: Resolved in Decision — Rank field modeled and fixed;
  formulas unchanged from §4.6 / §4.8.
- Concern: **Hybrid equipment "add as data" depends on schema
  generality.**
  Resolution: Deferred — Equipment domain doc / tech design must
  confirm the Type schema supports multi-stat / multi-requirement
  extensions.
- Concern: **Mastery tree "1–9 nodes" risks hard-coded branching.**
  Resolution: Deferred — Mastery tech design models the passive
  tree as a general graph of nodes + edges; no engine-side
  hard-coding of node count.
- Concern: **Tier grid eligibility cut while UI shows 5 columns
  risks save-format migration.**
  Resolution: Resolved in Decision — loadout slots keyed by
  (column, row) from day one; Tier field modeled but inert.

### game-designer

- Concern: **Hybrid-mastery gear mismatch.** All three shipped
  masteries are hybrid-attribute, and the original draft cut
  exactly the hybrid gear they were designed around.
  Resolution: Resolved in Decision — equipment attribute-requirement
  gating waived (§6.3.4), so any mastery can wear any gear without
  needing matched hybrid content. Mastery-via-gear-pressure is
  explicitly named as not-diagnostic in Consequences.
- Concern: **Passive tree depth is the mastery.** Without a floor,
  a 1–3 node tree would deliver no mastery identity.
  Resolution: Resolved in Decision — minimum 5 nodes per shipped
  mastery; GDD-named signature passive required.
- Concern: **Ultimate roster disproportionately cut** (~2 per pool
  was 20% of target while Core was 50%).
  Resolution: Partial resolution — bumped to ~3 per pool (~12
  total) so each mastery has 2 class Ultimates. Remaining shortfall
  named in Consequences as a diagnostic limit on Resolve / Ultimate
  tempo feel.
- Concern: **Common-only rarity distorts combat feel** (no Mods,
  raw-stat vs vanilla-vs-modded mix).
  Resolution: Accepted as consequence — named in the combat-feel
  Negative Consequences block.
- Concern: **Class vs mastery identity collapsed.** Every Warrior
  is a Blademaster; playtest cannot tell the two apart.
  Resolution: Accepted as consequence — named in the
  build-expression Negative Consequences block.
- Concern: **Trigger pattern coverage depends on unwritten content
  pass** (Depletion pattern's canonical example sits on a cut
  mastery).
  Resolution: Deferred — roster coverage rubric extended to all
  four Trigger patterns; tracked in follow-ups.
- Concern: **Cutting Tier restrictions shifts what playtest can flag
  as broken.**
  Resolution: Accepted as consequence — balance complaints need
  filtering for "combo reachable under Tier rules."
- Concern: **Practice AI is design work, not just tech work.**
  Resolution: Deferred — follow-up requires game-designer review of
  the Practice-mode tech design before engineer implementation.

### operator

- Concern: **"Playtest" without a named session shape** (topology
  and trust model).
  Resolution: Resolved in Decision — networked, server-authoritative
  committed. Trust model named (trusted-circle, authority-boundary
  cheat-prevention).
- Concern: **"Deployment target deferred" conflates hosting with
  session-delivery decisions.**
  Resolution: Resolved in Decision — session delivery (networked
  PvP, server-authoritative) decided here; hosting deferred to
  Phase-7 ADR.
- Concern: **Observability and debuggability gap** for a combat
  spec with hidden state + priority queues + trigger chains.
  Resolution: Resolved in Decision — dev-only combat event trace
  in scope with enumerated fields covering phase transitions,
  resolution order, ailment applications, Ignite-queue state, and
  trigger skip reasons.
- Concern: **Multiplayer failure modes unspecified** (disconnects,
  desyncs, ties, AFK, mid-Reaction close).
  Resolution: Deferred — the Battle / network tech design must name
  prototype-grade policies.
- Concern: **Cheat / trust boundaries not explicitly scoped.**
  Resolution: Accepted as consequence — server-authority is the
  prototype's cheat-prevention bar; production-grade anti-cheat out
  of scope with a follow-up before non-trusted-circle access.
- Concern: **Playtest operations** — build distribution, bug
  reporting, host responsibilities — are the prototype's only
  output signal and are not scoped.
  Resolution: Partial resolution — event trace commits the
  technical substrate; playtest runbook (build labeling, log paths,
  bug template) is a follow-up as the first playtest approaches.

### skeptic

- Steel-manned argument: **The reduced Tier A was not sanctioned by
  `.cursor/rules/20-negative-constraints.mdc`.** The original plan
  to skip architect, engineer, and operator was a drift event.
  Response: acknowledged. The missing three critics were run before
  this ADR was accepted; their outputs are synthesized above.
- Untested assumption: **No stated success criteria.** Every cut
  was defended against a vacuum.
  Response: Resolved in Decision — two-criterion Success criteria
  section added to the spec; Negative Consequences organized
  against each criterion so blind spots are auditable.
- Untested assumption: **"Full-fidelity combat" contradicted by
  several cuts** (Tier restrictions, Environment effects, Focus
  TBD, uncertain Corrupted application).
  Response: Resolved in Decision — kernel phrasing narrowed to
  "full-fidelity combat state machine"; each cracked seam named
  explicitly; roster coverage mandates Corrupted application.
- Untested assumption: **Practice AI is load-bearing, not a stub.**
  Without it the Reaction layer cannot be exercised.
  Response: Resolved in Decision — reclassified as simplified with
  named capability floor.
- Untested assumption: **Multiplayer topology silently deferred.**
  Hidden Reaction-Phase selection in PvP implies server authority
  by construction.
  Response: Resolved in Decision — networked server-authoritative
  committed.
- Untested assumption: **"Cuts are reversible" is architecturally
  true but epistemically false for playtest signal.** Data gathered
  under the cut version cannot be re-collected.
  Response: Accepted as consequence — the Negative Consequences
  block now explicitly names what each cut makes
  epistemically-not-diagnostic.
- Untested assumption: **Several "cuts" are silent forward
  commitments, not data additions** (max-level-at-creation UX,
  mastery-at-creation, passive-tree shape).
  Response: Resolved in Decision — "Modifications to cited
  sections" block in the spec makes each an explicit
  rule-change rather than a cut.
- Untested assumption: **~52 roster defended by taxonomy, not
  interaction coverage.**
  Response: Resolved in Decision — two-rubric coverage requirement
  (taxonomic + interaction) with specific scenarios named.
- Untested assumption: **Trinket / Consumable stub is a GDD gap
  disguised as a prototype cut.**
  Response: Resolved in Decision — spec states plainly that no
  ITEM inhabitant schema is committed until the Trinket GDD edit
  lands; a follow-up tracks that edit.
- Untested assumption: **Neutral pool sizing unmotivated.**
  Response: Deferred — content pass can revise the Neutral pool
  count against a separate rubric.

## Follow-ups

- #1: Archive or delete `design/gdd/apparent-scope-summary.md` on
  acceptance. (Performed as part of accepting this ADR.)
- #2: Phase-2.5 content pass — mastery passive-tree nodes for the 3
  shipped masteries, including GDD-named signature passives.
- #3: Phase-2.5 content pass — the ~52 specific abilities under
  both the taxonomic and interaction coverage rubrics.
- #4: Practice-mode AI specification in Phase 3+, reviewed by
  game-designer before engineer implementation.
- #5: Resolve Focus ability values (Hex, Mend) — currently
  engineer-placeholder in the prototype, TBD in the GDD.
- #6: Possible GDD edit for Trinket mechanics if / when items are
  added to the Trinket / Consumable slots.
- #7: Small `derive-spec` skill edit: codify "cite, don't restate"
  as cut discipline (Tier C change).
- #8: Update `design/index.md` on acceptance; reconcile the prior
  "first ADR expected to be `0001-stack-selection.md`" note.
  (Performed as part of accepting this ADR; stack-selection is now
  anticipated as ADR 0002.)
- #9: Battle / network tech design: define authority split,
  state-sync approach, disconnect / reconnect / desync policy, and
  match-session lifecycle following industry-standard
  server-authoritative patterns.
- #10: Battle tech-design follow-up: define a scenario test harness
  that exercises both the interaction-coverage rubric and the
  latent ITEM code path.
- #11: Anti-cheat posture decision before any non-trusted-circle
  playtest access.
- #12: Playtest runbook (build labeling, log paths, bug-report
  template) before the first playtest session.

## Links

- Governing artifact: `design/scope/prototype-scope.md`
- Parent canon: `design/gdd/GDD.md`, §14.2 in particular.
- Superseded prior ADRs: none (this is ADR 0001).
