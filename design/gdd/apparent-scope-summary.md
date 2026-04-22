# Apparent scope summary

A derived summary of what the GDD covers, produced during Phase 1
ingest. **This is a reading of the GDD, not a scope decision.** The
actual prototype scope is a Phase 2 Tier A decision.

Produced: Phase 1 ingest, derived from `design/gdd/GDD.md` — in
particular §14.2 (Prototype Scope Notes), §6.8 (Equipment Prototype
Scope), §7.2.1 (Battle Format prototype note), §2 (Game Overview),
and the subsystem-by-subsystem body of the GDD.

Source-of-truth for the scope decision itself is §14.2 of the GDD;
this summary organizes and cross-references it.

## What the GDD covers, by subsystem

### Core game loop (GDD §2.2)

Five-phase macro loop: Character Building → Battle Preparation →
Tactical Combat → Post-Battle Progression → Return to Building.
Supported by a TCG-inspired structure (§2.3.1): central hub,
collectible abilities, match-based progression, meta evolution.

### Character system (GDD §3)

- **Classes:** Warrior, Mage, Rogue, Neutral ability pool (§3.1).
Class identity enforced through ability pool design, not engine
rules (§3.1.4).
- **Masteries:** 12 total (4 per base class), unlocked at level 10,
with per-subclass passive trees and 5 mastery points earned at
levels 10/20/30/40/50 (§3.2, §3.3).
- **Primary attributes:** STR / DEX / INT / FTH (§3.4.1). Base vs
Total distinction: requirements check Base only.
- **Derived stats:** Combat/Agility/Sorcery/Divine Power; Speed;
HP/Mana/Stamina/Resolve; Armor / MR / Dodge / Accuracy / Crit /
Debuff Chance / Debuff Resistance / Resolve Generation (§3.4.2).
- **Resources:** HP, Mana, Stamina, Resolve, Initiative, Bonus
Actions (§3.5). Resolve generation is an anti-tank counterplay
system.
- **Shield:** Stacking buff with FIFO depletion, not an inherent
stat (§3.5.2).
- **Progression:** Max level 50; 5 AP and 1 SP per level (§3.6).

### Ability system (GDD §4)

- **Classification:** Class × Ability Type × Action Type × Tags
(§4.1).
- **Basics:** Innate (Punch, Jab, Rest) and equipment-granted
(§4.4).
- **Action types:** Normal / Reaction / Bonus / Passive (§4.5).
- **Empowers:** Percentage vs Flat; distinct scaling/variance rules
(§4.5.5).
- **Triggers:** Self-contained effects or ability proxies; chain
limit of one to prevent loops (§4.5.6).
- **Conditionals:** Ability activation gated by game state (§4.5.7).
- **Damage calculation:** Min-max range × Level × Rank × Power +
resolution % + crit (§4.6). Includes modifier order pipeline
(§4.6.5).
- **Targeting:** Single / AoE / Self; Enemy / Ally / Self / Any
(§4.7).
- **Leveling:** Core abilities only, via loadout slots (§4.8).
- **Rank:** ★ to ★★★★★ for all abilities (§4.8.5).
- **Crit:** Base crit on ability + character crit; 150% default
multiplier; DoTs and healing cannot crit (§4.9).
- **Status effects:** Blessing / Passive / Curse / Ailment families
(§4.10).
- **Stat blocks:** Universal format with conditional headings
(§4.11).

### Loadouts (GDD §5)

10-slot Core ability grid (5 Tiers × 2 rows) + 2 Ultimate slots +
attribute allocation + equipment set. Slot leveling is per-slot,
not per-item (§5.2.4). Tier system is marked "WIP" by the author.

### Equipment (GDD §6)

- 10 slots: 5 Active + 5 Passive (§6.1).
- **Active:** Main Hand, Off Hand, Trinket, Consumable ×2 — grant
abilities.
- **Passive:** Amulet, Ring, Helmet, Body, Boots — stats only.
- **Weapon Sets:** Two paired Main+Off sets, atomic swap on Bonus
Action, 2-turn cooldown (§6.1.3).
- **Type system:** Type is the foundation; Rarity provides Mods;
same Type = same ability (§6.3).
- **Weapon types:** 12 types organized by attribute combination
(§6.4.1).
- **Armor types:** 10 per slot (4 pure + 6 hybrid) × 3 slots
(§6.4.3).
- **Jewelry:** 11 rings (resolution modifiers) + 11 amulets
(attribute investment) (§6.4.4).
- **Rarity / Rank:** Common → Legendary; ★ → ★★★★★; diminishing
returns per rank (§6.6).
- **Blacksmith:** Salvage, Forge, Temper using Materials (§6.7).

### Battle system (GDD §7)

- **Initiative (CTB):** Speed-driven simultaneous accumulation to a
100 threshold; hard reset on turn (§7.1).
- **Team size:** 1v1 and 2v2 for PvP (§7.2.1).
- **Turn structure:** Six phases — `INITIATIVE`, `START_OF_TURN`,
`ACTION_SELECTION`, `REACTION_SELECTION`, `EXECUTION`,
`END_OF_TURN` (§7.3).
- **Reactions:** Hidden selection after turn player commits to a
Normal Action (§7.3.1).
- **Cooldowns:** Decrement at turn start; both weapon sets tick
always (§7.5).
- **Ailments:** Poison / Bleed / Ignite with distinct strategic
identities (§7.6). Ignite uses a priority queue (§7.6.3).
- **Mitigation:** Pre-mitigation → Penetration → Armor/MR → Shield
→ HP. True damage bypasses all Defenses (§7.7).
- **Accuracy/dodge:** Base + DEX bonuses; clamped to
[1 − Max Dodge, 100%] (§7.8).
- **Debuffs:** Base + INT − FTH; clamped [0%, 100%] (§7.9).
- **Stealth:** Prevents direct targeting; AoE and any damage breaks
it (§7.10.1).

### Game world and progression (GDD §8)

- Hub-based, not open-world (§8.1).
- Hub NPCs: Class Trainers ×3, Tutor, Blacksmith, Gambler, Oracle,
Guild Hall, Tavern, Battle Selection.
- PvE: Campaign, Quests (TBD), Dungeons (TBD) (§8.2, §8.3).
- PvP: Casual, Ranked, Tournaments (post-launch) (§8.4).

### User interface (GDD §9)

Battle HUD, character management (sheet / loadout / equipment),
hub navigation, Base (Total) value display convention (§9.4.1).

### Social (GDD §10)

Guild System (TBD), Tavern Chat, Friends List. Mostly TBD — light
spec.

### Economy (GDD §11)

- **Currencies:** Gold (primary), Materials (equipment crafting),
Essence (ability crafting) (§11.1).
- **Acquisition:** Gambler pulls (equipment), Oracle pulls
(abilities), PvE drops, PvP drops, quest rewards, crafting (§11.2).
- **Crafting at Blacksmith:** Salvage, Forge, Temper (§6.7).
- **Crafting at Trainer/Tutor:** Distill, Learn, Hone (§11.2.3).
- **Economic loops:** Equipment, ability, progression, long-term
(§11.3).

### Monetization, art, audio (GDD §§12, 13)

Free-to-play convenience model with TBD cosmetic options. Art and
audio mostly TBD.

## What the author has already flagged as prototype scope

From GDD §14.2 verbatim.

### Included in prototype

- Core turn loop: Initiative → Action → Reaction → Execution → End.
- 1v1 battles (2v2 is a stretch goal).
- Basic Common equipment with implicit modifiers only.
- Abilities at fixed Rank ★ without Honing.

### Explicitly deferred to full game

- Focus equipment ability balancing (Hex, Mend values TBD).
- Guild System.
- Dungeons mode.
- Tournaments.
- Cosmetic options.
- Art and Audio systems.
- Equipment rarity system (beyond Common).
- Rank / Tempering / Honing systems.
- Salvage / Forge / Distill / Learn economy.
- Gambler and Oracle pull systems.
- Ability Rarity and Rank progression.

### Additional scope questions that Phase 2 must resolve

The GDD does not explicitly state the prototype status of the
following. Phase 2's derive-spec + ADR process will need to answer
each one before domain docs are drafted.

- **Masteries and the mastery passive tree (GDD §3.2, §3.3).**
Unlock gated at level 10; prototype likely does not need character
progression up to level 10. Is mastery selection in-prototype,
deferred, or stubbed?
- **Trinkets and Consumables (GDD §6.1).** Status TBD per §6.1.1
note; the author has flagged the Hex/Mend balancing as deferred,
but the slots themselves are not explicitly cut.
- **Weapon Swap system (GDD §6.1.3).** Mentioned as part of the
loadout / equipment baseline, not as deferred; likely in-scope but
should be confirmed.
- **Ailments (GDD §7.6).** All three (Poison, Bleed, Ignite) are
part of core ability design. Presumably in-scope; confirm.
- **Status effects breadth (GDD §4.10.3).** Stealth, Invulnerable,
Immune, Slowed, Dazed, Corrupted — some may be deferred.
- **Hub NPCs beyond battle loop (GDD §8.1).** With the economy
deferred (Gambler, Oracle, Blacksmith, Trainer/Tutor crafting),
what remains of the hub in the prototype? Battle selection only?
- **PvE campaign (GDD §8.2, §8.3).** Explicit scope unclear. The
prototype's "Casual PvP" framing in §14.2 suggests PvP is the
primary playtest target; PvE may be minimal or absent.
- **Progression (GDD §3.6).** Leveling, AP/SP allocation, experience
— are these in the prototype or is the prototype a fixed-loadout
sandbox?
- **Loadout Tier system (GDD §5.2.1).** Author marked "WIP — needs
testing." Prototype-testable or deferred?
- **User interface breadth (GDD §9).** Full Battle HUD and Loadout
management needed for playtest; Character Sheet and Hub UI may be
minimal.
- **Social features (GDD §10).** Mostly TBD in the GDD; likely all
out of prototype scope but confirm.
- **Deployment target (not in GDD).** The workflow plan targets
"small-remote playtest" with trusted-circle testers; this is a
Phase 7 ADR, not a prototype-scope question, but it constrains
what the prototype must be built to support (authentication, match
hosting, state persistence).

## Hand-off to Phase 2

Phase 2 produces `design/scope/prototype-scope.md` via the
`derive-spec` skill, wrapped in an ADR since scope is a Tier A
decision. The questions in the previous section are the starting
agenda for that session. The `skeptic` subagent pressure-tests the
cuts; the human approves.

Until Phase 2 completes, no domain docs (§4), tech designs (§5,
§6), or implementation (§7+) can begin — each of those phases
consumes the approved scope as their governing input.