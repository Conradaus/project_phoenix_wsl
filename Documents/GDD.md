# Project Phoenix

# Game Design Document

*By Branching Path Games*

*Project Started: 01-10-2023*

**Authors:**

- Connor McDougall
- Jake Ellingham

---

## Table of Contents

1. [Design Principles](#1-design-principles)
2. [Game Overview](#2-game-overview)
3. [Character System](#3-character-system)
4. [Ability System](#4-ability-system)
5. [Character Loadouts](#5-character-loadouts)
6. [Equipment System](#6-equipment-system)
7. [Battle System](#7-battle-system)
8. [Game World & Progression](#8-game-world--progression)
9. [User Interface](#9-user-interface)
10. [Social Features](#10-social-features)
11. [Economy](#11-economy)
12. [Monetization Strategy](#12-monetization-strategy)
13. [Art and Audio](#13-art-and-audio)
14. [Appendices](#14-appendices)

---

# 1. Design Principles

Project Phoenix is built on four core design principles that guide all development decisions:

## 1.1 Intuitive, Concise and Consistent

- **UI Elements:** Clear descriptions and names that are intuitive to understand
- **Combat:** Straightforward mechanics with consistent application
- **Thematics:** Cohesive visual and gameplay elements
- **Learning Curve:** Easy to learn baseline mechanics

## 1.2 Design for Depth and Player Freedom

- **Opportunity Cost:** Meaningful choices with tradeoffs
- **Impactful Decisions:** Player choices significantly affect gameplay
- **No Unnecessary Limitations:** Avoid arbitrary restrictions
- **Freedom of Choice:** Multiple viable strategies and builds
- **Mastery Curve:** Difficult to master fully

## 1.3 Make Everything Overpowered

- **Thematics:** Powerful abilities that feel impactful
- **Unique Character Strengths:** Each character type has powerful, distinct advantages
- **Concentrated Coolness:** Focus on making each ability feel meaningful

## 1.4 Meaningful Progression and Integrity

- **Respect the Player's Time:** Significant rewards for time invested
- **No Purchasable Power:** Monetization focused on convenience, not power
- **Gameplay First:** Mechanics and balance take precedence over other considerations

---

# 2. Game Overview

## 2.1 Executive Summary

Project Phoenix is a competitive, turn-based tactical RPG with a focus on strategic PvP battles and character customization. The game combines the strategic depth of Trading Card Games with the character progression of RPGs, delivered as a web application accessible through browsers.

## 2.2 Core Gameplay Loop


| Phase                          | Activities                                                                                                |
| ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| **1. Character Building**      | • Allocate attribute points • Collect and select abilities • Equip and enhance gear                       |
| **2. Battle Preparation**      | • Select battle type (PvP or PvE) • Choose loadout • Enter matchmaking or select PvE encounter            |
| **3. Tactical Combat**         | • Initiative-based turn system • Strategic ability usage • Reaction mechanics for counterplay             |
| **4. Post-Battle Progression** | • Gain experience and resources • Collect new abilities and equipment • Refine build based on performance |
| **5. Return to Building**      | • Apply new resources to character • Adjust strategy based on battle results                              |


## 2.3 Game Structure

### 2.3.1 TCG-Inspired Structure

Project Phoenix adopts a structure similar to competitive card games:

- **Central Hub Interface:** Navigation center for all game features
- **Build Optimization:** Character building emphasizes synergies and counters
- **Collectible Abilities:** Abilities are collected like cards in a TCG
- **Match-Based Progression:** Rewards primarily from battle performance
- **Meta Evolution:** Balance adjustments and new content periodically shift the competitive environment

### 2.3.2 Player Progression Flow

1. **New Player:** Begin with basic character templates and limited ability options
2. **Early Game:** PvE scenarios teach mechanics and provide initial progression
3. **Mid Game:** Basic PvP becomes available after reaching milestone achievements
4. **Late Game:** Advanced abilities and equipment unlock through continued play
5. **Endgame:** Ranked competitive play becomes the primary activity

### 2.3.3 Game Mode Structure


| Mode                    | Description                                    |
| ----------------------- | ---------------------------------------------- |
| **Practice**            | AI opponents with customizable difficulty      |
| **Casual PvP**          | Unranked matches with minimal rewards          |
| **Ranked Play**         | Competitive matches with season-based rankings |
| **Limited-Time Events** | Special rule sets and exclusive rewards        |


---

# 3. Character System

## 3.1 Base Classes

Project Phoenix features three distinct base classes, each with unique playstyles and resource focuses:


| Class       | Resource Focus | Strengths                                     | Weaknesses                            |
| ----------- | -------------- | --------------------------------------------- | ------------------------------------- |
| **Warrior** | Stamina        | Consistent physical damage, Damage mitigation | Limited control options               |
| **Mage**    | Mana           | Burst magic damage, Control abilities         | Vulnerable to physical burst          |
| **Rogue**   | Stamina        | Burst physical damage, Bonus action synergy   | Vulnerable during defensive cooldowns |


### 3.1.1 Warrior

The warrior class focuses on stamina-based attack abilities. Their strengths lie in dealing consistent physical damage and providing reliable damage mitigation. This class favors raw offensive and defensive power at the cost of control or rapid action sequences.

### 3.1.2 Mage

The mage class utilizes mana-based abilities and offers tools for mana & HP sustain. They specialize in control abilities, using opponent manipulation as indirect defense. Mages typically deal burst magic damage with limited physical options, and their damage is often tied to cooldowns. They are vulnerable to burst damage, especially physical attacks.

### 3.1.3 Rogue

The rogue class focuses on stamina-based abilities that deal burst physical damage through rapid sequential actions. Their kit emphasizes heavy use of bonus actions and ways to obtain extra bonus actions, creating a "combo" playstyle. They also have control tools and powerful but short-duration defensive abilities. Rogues struggle against opponents who can deal consistent damage during their vulnerable windows.

### 3.1.4 Class Identity Through Ability Pools

Class strengths and weaknesses are enforced through **ability pool design**, not special-case engine rules. The engine treats all classes identically — differences emerge from which abilities each class has access to.


| Class       | Ability Pool Strengths                                            | Ability Pool Gaps                                |
| ----------- | ----------------------------------------------------------------- | ------------------------------------------------ |
| **Warrior** | Damage mitigation, consistent physical damage, Stamina efficiency | No mana recovery options, limited control        |
| **Mage**    | Mana recovery/sustain options, control abilities, magic burst     | Limited physical options, limited Stamina tools  |
| **Rogue**   | Bonus action generation, burst combos, short-duration defense     | No mana recovery options, weak sustained defense |


**Key example:** Mana has no natural regeneration for any class (see Section 3.5). Mages overcome this through class abilities that restore or sustain mana — this is a deliberate class advantage, not an engine mechanic. Warriors and Rogues lack mana recovery in their ability pools, making mana an attrition resource for them.

## 3.2 Subclasses (Masteries)

Each base class has four specialized subclasses (masteries) that focus on different attribute combinations and playstyles:

### 3.2.1 Warrior Masteries


| Mastery         | Attribute Focus         | Playstyle                                       |
| --------------- | ----------------------- | ----------------------------------------------- |
| **Berserker**   | Strength                | Consistent high physical damage                 |
| **Blademaster** | Strength & Dexterity    | High turn economy, burst damage, bleed synergy  |
| **Mercenary**   | Strength & Intelligence | Jack of all trades, multiple discipline synergy |
| **Paladin**     | Strength & Faith        | Tanky, reactionary, buff focus                  |


### 3.2.2 Mage Masteries


| Mastery        | Attribute Focus          | Playstyle                                  |
| -------------- | ------------------------ | ------------------------------------------ |
| **Battlemage** | Intelligence & Strength  | Attack & spell synergy, resource sustain   |
| **Occultist**  | Intelligence & Dexterity | Debuff synergy, control focus              |
| **Sorcerer**   | Intelligence             | Mana sustain & synergy, magic damage burst |
| **Pyromancer** | Intelligence & Faith     | Buff, burst & ignite synergy               |


### 3.2.3 Rogue Masteries


| Mastery      | Attribute Focus          | Playstyle                                  |
| ------------ | ------------------------ | ------------------------------------------ |
| **Outlaw**   | Dexterity & Strength     | Multiple hit & crit synergy, offhand focus |
| **Ranger**   | Dexterity                | Ranged attack focus                        |
| **Assassin** | Dexterity & Intelligence | Debuff & poison synergy, burst             |
| **Slayer**   | Dexterity & Faith        | Buff & stealth synergy, combo burst        |


## 3.3 Mastery System

The mastery system allows for character specialization and build customization:

- Players unlock mastery selection at **level 10**
- New masteries require unlocking with in-game resources or premium currency
- Each subclass has its own **mastery passive tree**
- Players earn **1 mastery point every 10 levels** (5 total at level 50)
- Each mastery tree has ~9 options, requiring choices with limited points
- Some passives have prerequisites while others are independent
- Mastery passives create significant build-enabling effects
  - Example: Blademaster's ability to equip an offhand while using a two-handed weapon

**Mastery Unlocking:** Players unlock the ability to choose a mastery upon reaching level 10 and earning their first mastery point. To select a mastery, the player must speak with a designated class trainer NPC in the main hub. At least one mastery option per base class will be available to choose from without any prior unlocking requirements beyond reaching level 10. Additional masteries for the full game *may* require discovery or specific achievements to become available for selection at their respective trainers.

## 3.4 Character Attributes & Stats

### 3.4.1 Primary Attributes

Players allocate points into four primary attributes that define their character's capabilities:


| Attribute        | Primary Effect | Secondary Effects                     |
| ---------------- | -------------- | ------------------------------------- |
| **Strength**     | Combat Power   | Health, Stamina Regeneration          |
| **Dexterity**    | Agility Power  | Accuracy, Dodge Chance, Speed         |
| **Intelligence** | Sorcery Power  | Debuff Chance, Mana Pool              |
| **Faith**        | Divine Power   | Debuff Resistance, Resolve Generation |


**Base vs Total Attributes:**

- **Base Attribute:** The value from level-up point allocation only. This is the permanent, deliberate investment.
- **Total Attribute:** Base + all modifiers (equipment bonuses, buffs, debuffs). This is the effective value used for scaling and derived stats.
- Equipment requirements check **Base Attributes only** (see Section 6.3.4). This prevents circular dependencies where equipping an attribute-boosting item could enable other equipment.

### 3.4.2 Derived Stats

These statistics are calculated from primary attributes and equipment:


| Category          | Stats                                                                         |
| ----------------- | ----------------------------------------------------------------------------- |
| **Combat Timing** | Speed, Initiative                                                             |
| **Resources**     | Health, Mana, Stamina, Resolve                                                |
| **Regeneration**  | Health Regen, Mana Regen, Stamina Regen                                       |
| **Defenses**      | Armor, Magic Resistance, Debuff Resistance, Dodge Chance, Max Dodge Chance    |
| **Offense**       | Critical Chance, Critical Damage, Accuracy, Debuff Chance, Resolve Generation |
| **Powers**        | Combat Power, Agility Power, Sorcery Power, Divine Power                      |


**Note:** Armor and Magic Resistance come from equipment and abilities only — they are not derived from attributes.

### 3.4.3 Attribute Scaling Rates

Target scaling rates for balancing (subject to tuning):


| Attribute        | Derived Stat         | Rate                          |
| ---------------- | -------------------- | ----------------------------- |
| **Strength**     | Combat Power         | 1:1 (1 STR = 1 Combat Power)  |
| **Strength**     | Health               | +1 HP per 2 STR               |
| **Strength**     | Stamina Regeneration | +1 per 10 STR                 |
| **Dexterity**    | Agility Power        | 1:1 (1 DEX = 1 Agility Power) |
| **Dexterity**    | Speed                | +1 Speed per 5 DEX            |
| **Dexterity**    | Accuracy             | +1% per 4 DEX                 |
| **Dexterity**    | Dodge Chance         | +1% per 4 DEX                 |
| **Intelligence** | Sorcery Power        | 1:1 (1 INT = 1 Sorcery Power) |
| **Intelligence** | Mana Pool            | +1 Mana per 2 INT             |
| **Intelligence** | Debuff Chance        | +1% per 3 INT                 |
| **Faith**        | Divine Power         | 1:1 (1 FTH = 1 Divine Power)  |
| **Faith**        | Debuff Resistance    | +1% per 3 FTH                 |
| **Faith**        | Resolve Generation   | +1% per 3 FTH                 |


### 3.4.4 Base Values

All characters start with these base values (before attribute allocation):


| Stat                 | Base Value             |
| -------------------- | ---------------------- |
| **Health**           | 50                     |
| **Mana**             | 50                     |
| **Stamina**          | 50                     |
| **Speed**            | 50                     |
| **Max Dodge Chance** | 65%                    |
| **Critical Chance**  | 0% (requires ability)  |
| **Critical Damage**  | 150% (1.5× multiplier) |


## 3.5 Character Resources

Project Phoenix utilizes several resource systems that create strategic depth:


| Resource          | Description               | Base Value | Turn Start Behavior                                    |
| ----------------- | ------------------------- | ---------- | ------------------------------------------------------ |
| **Health (HP)**   | Core survival resource    | 50         | No natural regeneration (restored by abilities only)   |
| **Stamina**       | Powers attack abilities   | 50         | Regenerates by Stamina Regen amount (not a full reset) |
| **Mana**          | Powers spells and utility | 50         | No natural regeneration (restored by abilities only)   |
| **Resolve**       | Powers ultimate abilities | 0          | Generated from combat (see below)                      |
| **Initiative**    | Determines turn order     | 0          | Accumulates based on Speed                             |
| **Bonus Actions** | Limits bonus action usage | 1          | Resets to maximum at turn start                        |


### 3.5.1 Resolve Generation

Resolve is generated during combat. Both the attacker and defender can gain Resolve from the same exchange:

**Defender gains Resolve from:**

| Source | Trigger | Rate |
| ------ | ------- | ---- |
| **HP Damage Received** | Defender takes HP damage from any source | 1 Resolve per 1 HP lost |

**Attacker gains Resolve from:**

| Source | Trigger | Rate |
| ------ | ------- | ---- |
| **Damage Mitigated** | Attacker's damage is reduced by the defender's Defenses (Armor, MR, Shield) | 1 Resolve per 1 damage mitigated |
| **Dodge** (counts as mitigation) | Defender dodges the attacker's ability entirely | Full ability damage counts as mitigated |

The raw Resolve gained is then multiplied by the recipient's **Resolve Generation** stat:


| Stat                   | Base Value | Scaling       | Example at 250 FTH |
| ---------------------- | ---------- | ------------- | ------------------ |
| **Resolve Generation** | 50%        | +1% per 3 FTH | 133% (50% + 83%)   |


**Resolve Cap:** 100 (maximum Resolve a character can hold)

**Ultimate Resolve Costs:** Each Ultimate ability defines its own Resolve cost. Costs typically range from 50 to 100, with more powerful Ultimates costing more. 100 Resolve represents the power ceiling, not the norm.

#### Design Intent

This system creates anti-tank counterplay:

- **Attacking a tank:** The tank's defenses mitigate heavily → the **attacker** gains lots of Resolve → their Ultimate charges faster
- **Being attacked as a squishy:** The squishy takes lots of HP damage → the **defender** gains Resolve (comeback mechanic)
- **High Faith tanks:** Compensate for lower HP damage intake via higher Resolve Generation multiplier
- **Dodging:** If the defender dodges, the **attacker** still gains Resolve for the full damage that was prevented (intentional compensation)

### 3.5.2 Shield Mechanics

Shield is NOT an inherent character stat — it is a **stacking buff** granted by abilities:

- Each Shield-granting ability creates a **separate buff** with its own duration
- Multiple Shield buffs can exist simultaneously, each tracking independently
- Shield **amounts** are combined and displayed on the HP UI bar
- When Shield takes damage, **FIFO order** applies (oldest Shield depletes first)
- Each buff icon shows its own remaining duration
- Shield absorbs damage AFTER Armor/MR mitigation
- When a Shield buff expires, its Shield amount is removed
- True damage bypasses Shield entirely

**Example:**

1. Ability A grants 50 Shield (2 turns) → Buff icon [A: 2t]
2. Ability B grants 30 Shield (3 turns) → Buff icon [B: 3t]
3. HP bar shows: 80 total Shield
4. Take 60 damage after mitigation → Shield A depleted (50), Shield B reduced to 20
5. After 3 turns: Buff B expires, Shield drops to 0

## 3.6 Leveling and Progression

Character progression follows these parameters:

- **Maximum level:** 50
- **Mastery Points:** 1 point is earned at levels 10, 20, 30, 40, and 50 (5 total)

### 3.6.1 Point Allocation


| Level                  | Attribute Points        | Skill Points           |
| ---------------------- | ----------------------- | ---------------------- |
| **Level 1 (Creation)** | 5                       | 1                      |
| **Levels 2-50**        | 5 per level (245 total) | 1 per level (49 total) |
| **Maximum Totals**     | 250                     | 50                     |


- **Point allocation is manual** — players must distribute points themselves
- **Points can remain unspent** — players may save points for later allocation
- Level 1 allocation happens during character creation, serving as a tutorial for understanding attributes

### 3.6.2 Experience Sources

- Primarily from battle victories
- Small amount from PvP losses

---

# 4. Ability System

## 4.1 Ability Classification

Abilities are classified by **Class**, **Ability Type**, **Action Type**, and **Tags**.

### 4.1.1 Class (Who Can Use It)


| Class   | Meaning                 |
| ------- | ----------------------- |
| WARRIOR | Only Warriors can equip |
| MAGE    | Only Mages can equip    |
| ROGUE   | Only Rogues can equip   |
| NEUTRAL | Any class can equip     |


### 4.1.2 Ability Type (What Kind)


| Type     | Slots | Source                          | Levelable |
| -------- | ----- | ------------------------------- | --------- |
| BASIC    | —     | Innate or from Active equipment | No        |
| CORE     | 10    | Collectible                     | Yes       |
| ULTIMATE | 2     | Collectible                     | No        |
| ITEM     | —     | From Trinket or Consumables     | No        |


**Notes:**

- BASIC abilities are granted by Active equipment (weapons, shields, focuses) or are innate (Punch, Jab, Rest). See Section 4.4.
- CORE abilities include both standard abilities and EMPOWER-tagged abilities that augment Basics. See Section 4.5.5.
- ULTIMATE abilities are **class-specific** (Warrior, Mage, Rogue) or Neutral. They are designed with specific masteries in mind but are not locked to a mastery — any character of that class can equip any of their class's Ultimates. Each Ultimate defines its own **Resolve cost** (typically 50-100).
- ITEM abilities are granted by Trinkets (activatable, reusable) and Consumables (single-use).
- CORE and ULTIMATE abilities are collectible items with **Rarity** (Common→Legendary) and **Rank** (★→★★★★★), following the same acquisition system as equipment. See Section 4.8.5 for Ability Rank and Section 11.2 for acquisition.

### 4.1.3 Action Type (How Used)


| Type     | Description                                    |
| -------- | ---------------------------------------------- |
| NORMAL   | Main action, triggers Reaction Phase           |
| REACTION | Response to turn character's Normal Action      |
| BONUS    | Immediate, no reaction, limited resource       |
| PASSIVE  | Grants a permanent Passive buff; always active |


### 4.1.4 Tags (What It Does)

Abilities can have multiple tags: ATTACK, SPELL, MELEE, RANGED, AOE, BUFF, DEBUFF, PHYSICAL, MAGIC, RECOVERY, CONSUMABLE, EMPOWER, TRIGGER, CONDITIONAL, BLESSING, CURSE.

**Notes:**

- MELEE and RANGED denote the range of attack abilities and empowers. Spells are not tagged RANGED even if they target at range.
- BUFF and DEBUFF are parent tags. Any ability that applies a positive effect uses BUFF; any ability that applies a negative effect uses DEBUFF. These are always present alongside their subcategory tags.
- BLESSING and CURSE are subcategory tags under BUFF and DEBUFF respectively (see Section 4.10). An ability tagged BLESSING must also be tagged BUFF. An ability tagged CURSE must also be tagged DEBUFF. An ability that grants a Passive (permanent buff) is tagged BUFF without BLESSING.
- EMPOWER identifies abilities that augment a Basic ability (see Section 4.5.5).
- TRIGGER identifies abilities containing effects that fire automatically when a condition is met (see Section 4.5.6).
- CONDITIONAL identifies abilities that require a game-state condition to be met before activation (see Section 4.5.7).

### 4.1.5 Examples


| Ability       | Class   | Type     | Action   | Tags                                    |
| ------------- | ------- | -------- | -------- | --------------------------------------- |
| Punch         | NEUTRAL | BASIC    | NORMAL   | ATTACK, MELEE, PHYSICAL                 |
| Slash         | NEUTRAL | BASIC    | NORMAL   | ATTACK, MELEE, PHYSICAL                 |
| Defend        | NEUTRAL | BASIC    | REACTION | BUFF, BLESSING                          |
| Fireball      | MAGE    | CORE     | NORMAL   | SPELL, MAGIC, DEBUFF                    |
| Double Strike | NEUTRAL | CORE     | NORMAL   | ATTACK, MELEE, PHYSICAL, EMPOWER        |
| Retaliation   | WARRIOR | CORE     | REACTION | BUFF, BLESSING, TRIGGER, EMPOWER, MELEE |
| Shadowstrike  | ROGUE   | CORE     | NORMAL   | ATTACK, MELEE, PHYSICAL, CONDITIONAL    |
| Meteor Storm  | MAGE    | ULTIMATE | NORMAL   | SPELL, AOE, MAGIC                       |
| Health Potion | NEUTRAL | ITEM     | BONUS    | RECOVERY, CONSUMABLE                    |


## 4.2 Disciplines and Powers

### 4.2.1 Disciplines

Disciplines are schools/categories that group abilities thematically:

- **COMBAT:** Physical combat abilities
- **AGILITY:** Speed and precision abilities
- **SORCERY:** Magical & debuff abilities
- **DIVINE:** Holy/faith-based & buff abilities

Abilities are tagged with one or more Disciplines. Some effects can target abilities by Discipline (e.g., "Disable all Combat abilities").

### 4.2.2 Powers

Powers are character stats used for scaling:


| Power             | Source       | Scaling |
| ----------------- | ------------ | ------- |
| **Combat Power**  | Strength     | 1:1     |
| **Agility Power** | Dexterity    | 1:1     |
| **Sorcery Power** | Intelligence | 1:1     |
| **Divine Power**  | Faith        | 1:1     |


Abilities define which Power(s) they scale with using **percentage scaling**. The bonus is calculated as `floor(Power × rate)`, where rate is a percentage expressed as a decimal.

**Example:** "20% Sorcery Power"

- At 50 Sorcery Power: `floor(50 × 0.20) = 10` → +10 damage
- At 75 Sorcery Power: `floor(75 × 0.20) = 15` → +15 damage
- At 100 Sorcery Power: `floor(100 × 0.20) = 20` → +20 damage

A higher percentage always means better scaling — intuitive at a glance. The `floor()` function ensures all final values are **whole numbers only**.

Items or buffs can grant Power directly without altering base attributes.

**Note:** An ability may have a Discipline tag but no scaling.

## 4.3 Damage Types


| Damage Type  | Mitigated By                                       |
| ------------ | -------------------------------------------------- |
| **PHYSICAL** | Armor, then Shield, then HP                        |
| **MAGIC**    | Magic Resistance, then Shield, then HP             |
| **TRUE**     | Nothing — direct HP damage (bypasses all Defenses) |


## 4.4 Basic Abilities

Every character has access to Basic abilities from two sources:

### Innate Basics

These abilities are not granted by equipment:


| Ability   | Action Type | Description                                                              |
| --------- | ----------- | ------------------------------------------------------------------------ |
| **Punch** | Normal      | Unarmed main hand attack. Available when no main hand weapon is equipped |
| **Jab**   | Normal      | Unarmed off hand attack. Available when no off hand item is equipped     |
| **Rest**  | Normal      | Restores stamina. Triggers the Reaction Phase. Always available          |


Punch and Jab serve as fallback Basic abilities for empty or disabled equipment slots. Rest is always available regardless of equipment.

### Equipment Basics

Active equipment grants Basic abilities based on the equipment Type (see Section 6.4 for full list):


| Source           | Examples                                        | Notes          |
| ---------------- | ----------------------------------------------- | -------------- |
| Main Hand Weapon | Slash (Sword), Cleave (Axe), Arcane Bolt (Wand) | Replaces Punch |
| Off Hand Weapon  | Varies by weapon type                           | Replaces Jab   |
| Shield           | Defend (Kite Shield), Block (Tower Shield)      | Replaces Jab   |
| Focus            | Hex (Grimoire), Mend (Tome)                     | Replaces Jab   |


- Equipping a weapon, shield, or focus in a slot **replaces** the innate Basic (Punch or Jab) for that slot.
- Swapping to an empty weapon set reverts to Punch and Jab (see Section 6.1.3).
- Rest is always available regardless of equipment.
- **Skip Reaction** is not an ability — it is a system action available during the Reaction Phase (see Section 7.3.1).

## 4.5 Action Type Details

### 4.5.1 Normal Actions

- One per turn, triggers Reaction Phase for all non-turn characters

### 4.5.2 Bonus Actions

- Each Bonus Action **resolves immediately** when activated — there is no batching or ordering
- A character may use as many Bonus Actions per turn as they have charges, resources, and cooldowns to support
- Must be used before committing to a Normal Action (which ends the Action Selection phase)
- Cannot be reacted to
- Limited by Bonus Action charges (default max: 1, resets at turn start; abilities or effects can grant additional charges)

### 4.5.3 Reactions

- Selected AFTER turn player commits to Normal Action
- Reactors know an action was selected, but not WHICH action
- Creates counterplay and mind games

### 4.5.4 Passives

- Always active or trigger automatically under specified conditions

### 4.5.5 Empowers

Empower abilities are Core abilities tagged with EMPOWER. Instead of being used independently, they augment a Basic ability to produce a combined effect.

#### How Empowers Work

1. The player selects an Empower ability (e.g., "Double Strike")
2. The Empower's targeting tag determines which Basic ability it combines with
3. The system automatically combines the Empower with the matching Basic — no two-step selection required
4. The combined ability resolves as a single action

#### Targeting

Each Empower defines which Basic abilities it can augment. Targeting can range from broad to narrow:


| Scope         | Example Targeting            | Applies To                         |
| ------------- | ---------------------------- | ---------------------------------- |
| Broad         | "any main-hand melee basic"  | Axe, Sword, Mace, Dagger, etc.     |
| Medium        | "any main-hand ranged basic" | Bow, Crossbow                      |
| Narrow        | "Arcane Bolt"                | Wand only                          |
| Type-specific | "any sword basic"            | Sword weapons only                 |
| Off-hand      | "any off-hand basic"         | Off-hand weapons, shields, focuses |


Targeting scope is determined by thematic fit and balance. An Empower is only usable when exactly one valid Basic ability matches its targeting. The character's current loadout and weapon set determine what matches.

#### Cost and Cooldown


| Rule                      | Behavior                                                                                  |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Combined Cost**         | Empower's resource cost is added to the Basic ability's cost                              |
| **Basic Must Be Ready**   | The targeted Basic ability must be off cooldown and have resources available              |
| **Both Go on Cooldown**   | Using the Empower puts both the Empower and the Basic ability (if it has one) on cooldown |
| **Independent Cooldowns** | The Empower and Basic ability track separate cooldown durations                           |


#### Damage Variants

Empowers modify the Basic ability's damage in one of several ways:


| Variant             | Description                                               | Example                                                                 |
| ------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Percentage**      | Multiplies the Basic ability's calculated damage          | Double Strike: 2 hits at 70% damage effectiveness                       |
| **Flat**            | Adds a fixed damage value on top of the Basic ability     | Throw Weapon: +6 Physical damage (scaling with Agility Power)           |
| **Type Conversion** | Changes the combined damage to a different damage type    | Holy Strike: 110% of Basic damage, converted to Magic damage            |
| **Effect Addition** | Adds a status effect on top of the Basic ability's damage | Radiant Flare: Empowers Radiance, adds Ignite chance to each target hit |


Variants can be combined (e.g., percentage + type conversion).

#### Empower Scaling and Variance Rules

Percentage and Flat Empowers follow different rules for Power scaling and damage variance. The core principle: Percentage Empowers are pure multipliers on the Basic ability's output (which already has its own scaling and variance), while Flat Empowers are independent damage sources (so they need their own).

| Property | Percentage Empower (e.g., Double Strike) | Flat Empower (e.g., Throw Weapon) |
| -------- | ---------------------------------------- | --------------------------------- |
| **Power Scaling** | No — would cause quadratic growth | Yes — independent scaling vector |
| **Level/Rank Scaling** | Yes — effectiveness % increases | Yes — flat amount increases |
| **Damage Variance** | No — inherits variance from the Basic ability | Yes — defines its own min-max range |

**Rationale:** A Percentage Empower already amplifies everything the Basic produces — its scaled damage, its variance, its Power bonus. Adding independent Power scaling or variance on top would either create quadratic growth or double-variance, making balance unpredictable. A Flat Empower adds a separate damage component that needs its own scaling and variance to remain relevant and interesting as Power grows. Flat Empowers can use a different Power type than the Basic (e.g., Agility Power on a Combat Basic), encouraging hybrid builds.

This is a balance guideline, not an engine restriction. Exceptions are valid design space but should be used sparingly and with awareness of the implications.

#### Inheritance

- Empowered abilities **inherit the Basic ability's crit chance**
- Crit multiplier applies to the **full combined damage**
- Downstream effects that reference total damage (Bleed, Ignite, etc.) use the full combined result

#### UI Display

Empower tooltips frontload combined calculations so players never need to do math:

```
Cost: 5 Stamina (15 total)
      ↑empower   ↑combined with Basic

Damage: 2× 14-18 Physical
        ↑calculated from current Basic

Currently empowering: Slash
```

The tooltip dynamically updates when the player changes weapons or weapon sets. If the Basic ability is on cooldown or requirements aren't met, the Empower is greyed out with a reason displayed.

**Note:** EMPOWER can also appear on trigger abilities that fire a Basic ability as a proxy (see Section 4.5.6). In this case, the Empower combination happens automatically when the trigger fires rather than through player selection, but all other Empower rules apply (scaling, cost stacking, crit inheritance).

### 4.5.6 Triggers

Trigger abilities contain effects that fire automatically when a game-state condition is met. The TRIGGER tag identifies this behavior. Triggers always live on a Blessing or Passive — the ability creates or is the buff, and the buff contains the trigger.

#### How Triggers Work

1. The ability creates a Blessing (temporary) or Passive (permanent) on the character
2. The Blessing/Passive defines a trigger condition and a response effect
3. When the condition is met during gameplay, the response fires automatically — no player input
4. The triggering Blessing/Passive must be active (not suppressed) for the trigger to fire

#### Trigger Response Types

A trigger's response is either a **self-contained effect** or an **ability proxy**.


| Response Type      | Description                                 | Cost                                  | Example                                                     |
| ------------------ | ------------------------------------------- | ------------------------------------- | ----------------------------------------------------------- |
| **Self-contained** | The trigger defines its own effect directly | Defined on the effect (default: zero) | Envenom: melee main-hand hits trigger Poison with X% chance |
| **Ability proxy**  | The trigger fires an existing ability       | Pays that ability's full cost         | Retaliation: fires melee main-hand Basic ability            |


**Ability proxy rules:** When a trigger fires an ability, it follows the same proxy rules as Empowers:

- The referenced ability must be **usable** (off cooldown, requirements met, resources available)
- Firing the ability **pays its cost** and **puts it on cooldown**
- If the ability is an Empower target (e.g., a Basic ability), the trigger can also be tagged EMPOWER to scale with the Basic ability's damage
- If the referenced ability is unavailable (cost, cooldown, requirements), the trigger **does not activate** — it is skipped entirely. No cost is paid, no cooldown or depletion occurs. The trigger remains listening for the next qualifying event

This creates design space for combo builds where triggers chain into abilities, with the trade-off of backloaded resource costs and usability requirements.

#### Trigger Patterns


| Source                            | Pattern                                                                                              | Example                                                                                                              |
| --------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Blessing + Trigger**            | Player uses ability → creates temporary Blessing → trigger fires if condition is met during duration | Retaliation: Reaction ability grants 1-turn Blessing. If user takes damage, fires melee main-hand Basic at X% damage |
| **Passive + Trigger**             | Permanent Passive listens for condition continuously                                                 | Envenom (Rogue): melee main-hand hits trigger Poison with X% chance                                                  |
| **Passive + Trigger + Cooldown**  | Passive fires when condition is met, then suppressed until cooldown expires                          | Reactive Shield: when hit by a critical, gain Shield. 3-turn cooldown                                                |
| **Passive + Trigger + Depletion** | Passive fires once, then suppressed for the remainder of the battle                                  | Undying Rage (Berserker mastery): when HP would reach 0, set to 1 HP instead. Once per battle                        |


#### Trigger Conditions

Triggers can respond to a range of game events:


| Category               | Example Conditions                                     |
| ---------------------- | ------------------------------------------------------ |
| **HP Threshold**       | When HP drops below X%, when HP would reach 0          |
| **Damage Received**    | When user takes damage, when hit by melee/ranged/spell |
| **Damage Dealt**       | When user deals damage, when user crits                |
| **Status Change**      | When a Curse is applied, when a Blessing expires       |
| **Resource Threshold** | When mana drops below X%, when resolve reaches 100     |


Turn-based triggers (start of turn, end of turn) are handled by the existing timing system (see Section 7.4) and do not require the TRIGGER tag.

#### Trigger Targeting

Player-activated abilities use direct selection or automatic self-targeting (see Section 4.7). Triggers fire automatically, so they must define their own targeting rule. Each trigger's ability description specifies which rule it uses.


| Targeting Rule   | Description                                                | Example                                                  |
| ---------------- | ---------------------------------------------------------- | -------------------------------------------------------- |
| **Source**       | Targets the character responsible for the triggering event | Retaliation: counter-attack against the source of damage |
| **Self**         | Targets the character who owns the trigger                 | Reactive Shield: gain Shield on self when critically hit |
| **Random Enemy** | Targets a random enemy                                     | Design space for chaos/chance effects                    |
| **All (AoE)**    | Affects all valid targets in a group                       | AoE retaliation effects, damage auras                    |


**Source** refers to the character that caused the event — the attacker for damage triggers, the debuff applier for status triggers, etc. If the source is no longer valid (e.g., defeated), the trigger does not activate.

Most triggers use **Source** (reactive responses to an attacker) or **Self** (self-applied buffs/shields). The trigger's description must always make the targeting rule clear.

#### Trigger Timing and Resolution

Triggers resolve **immediately** after their triggering event, before the next game action.

**Same character, multiple triggers from one event:**
Resolve in **buff application order** — the Blessing/Passive that was applied first resolves first. For Passives applied simultaneously (e.g., game-start passives), fallback to **ability slot order**.

**Multiple characters, same triggering event:**
Resolve in **initiative order** — higher initiative resolves first. This is consistent with the game's universal ordering principle.

**Chain triggers:**
A trigger's response can cause another trigger to fire (e.g., Retaliation deals damage → enemy's "on damage received" trigger fires). However, a single triggering event can only chain **once**:

```
Event → Trigger A fires → Trigger B fires from A's result → Stop
```

No further triggers fire from B's result during this chain. This prevents infinite loops.

#### Edge Cases


| Scenario                      | Resolution                                                                                                                                                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Trigger + Death**           | Character must survive the triggering event for the trigger to fire. Exception: "when HP would reach 0" triggers (e.g., Undying Rage) intercept death specifically                                            |
| **Trigger + Suppression**     | If a Passive is suppressed by the same event that would trigger it (e.g., Corrupted applied), suppression applies first — the trigger does not fire                                                           |
| **Ability proxy unavailable** | Referenced ability fails usability check (cost, cooldown, requirements). Trigger does not activate — skipped entirely. No cooldown or depletion occurs. Trigger continues listening for next qualifying event |


#### Suppression

All cases where a Passive becomes unavailable use the same mechanic: **suppression**. A suppressed Passive's effects and triggers are disabled, but the Passive is never removed — it reactivates when the suppression ends.


| Suppression Source | Duration            | Reactivation                                                                                         |
| ------------------ | ------------------- | ---------------------------------------------------------------------------------------------------- |
| **Cooldown**       | Fixed turn count    | Suppressed after trigger fires. Cooldown decrements at turn start. Reactivates when cooldown expires |
| **Corrupted**      | Curse duration      | Suppressed while Corrupted is active. Reactivates when Corrupted expires or is removed               |
| **Depletion**      | Remainder of battle | Suppressed after one-time trigger fires (e.g., "once per battle"). No natural reactivation           |


- Suppressed Passives show a visual overlay indicating the suppression source (cooldown timer, Corrupted icon, or depleted indicator)
- An "unsuppress" effect could theoretically reactivate any suppressed Passive, including depleted ones — this is intentional design space

### 4.5.7 Conditionals

The CONDITIONAL tag identifies abilities that have an additional game-state requirement beyond cost and cooldown. This requirement must be met before the ability can activate — whether that activation is player-initiated or trigger-initiated.

#### How Conditionals Work

1. The ability defines an activation condition (e.g., "requires Stealth Blessing")
2. When the condition is NOT met, the ability cannot activate (greyed out with reason displayed for player-activated abilities; silently skipped for triggers)
3. When the condition IS met, the ability becomes available for activation
4. For player-activated abilities: once the player commits during Action Selection, the ability **will execute** regardless of whether the condition changes before execution (e.g., Stealth broken by a reaction)

#### Condition Types


| Category                    | Example                           |
| --------------------------- | --------------------------------- |
| **Buff/Blessing active**    | "Requires Stealth" — Shadowstrike |
| **Target state**            | "Target below 25% HP" — Execute   |
| **Resource threshold**      | "Mana above 80%" — Overcharge     |
| **Curse/Ailment on target** | "Target is bleeding" — Bloodburst |


Multiple conditions can be combined (all must be met).

#### Interaction with Other Tags

CONDITIONAL combines naturally with other ability modifiers:


| Combination                 | Behavior                                                                                                                                                               |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONDITIONAL + TRIGGER       | Trigger only fires when both the trigger event occurs AND the condition is met. If condition is unmet, trigger is silently skipped (same as ability proxy unavailable) |
| CONDITIONAL + EMPOWER       | Empower is only usable when both the Empower targeting AND the condition are satisfied                                                                                 |
| CONDITIONAL + Cooldown      | Both must be satisfied — condition met AND off cooldown                                                                                                                |
| CONDITIONAL + Resource cost | All three must be satisfied — condition, cooldown, and resources                                                                                                       |


#### UI Display

Conditional abilities use a **glowing border** to indicate condition status, independent of ability readiness:


| Condition | Ability Ready  | Border  | Icon                  | Result                               |
| --------- | -------------- | ------- | --------------------- | ------------------------------------ |
| Met       | Yes            | Glowing | Normal                | Usable                               |
| Met       | No (cooldown)  | Glowing | Greyed + cooldown     | Condition there, ability not ready   |
| Met       | No (resources) | Glowing | Greyed + cost warning | Condition there, can't afford        |
| Not met   | Yes            | No glow | Greyed                | Ability ready, waiting for condition |
| Not met   | No             | No glow | Greyed + reason       | Neither satisfied                    |


Tooltip displays the condition with a status indicator:

```
Shadowstrike [Greyed Out]
Requires: Stealth active  ✗
```

When the condition is met:

```
Shadowstrike [Glowing Border]
Requires: Stealth active  ✓
```

## 4.6 Ability Damage Calculation

All abilities define their own damage values. Weapon equipment does not have a separate "base damage" property — damage is defined on the Basic ability the weapon grants.

### 4.6.1 Damage Ranges and Rolls

Every damaging ability defines a **min-max damage range** (e.g., 10-14). When the ability is used, the actual damage is determined by rolling a **uniform random integer** between the final min and max values (inclusive). Every value in the range has equal probability.

Level and Rank scaling apply to **both min and max** values:

```
Base Min/Max → + Level increments (both) → × Rank multiplier (both, floored) → Roll → + Power bonus → + resolution % (Section 4.6.5) → Pre-mitigation damage
```

**Example:** Slash (Base 10-14) at Level 5 (+11 from levels), Rank ★★★ (135%), 50 Combat Power (10% scaling):
1. Level: 21-25
2. Rank: floor(21 × 1.35)-floor(25 × 1.35) = 28-33
3. Roll: uniform random integer, e.g., 30
4. Power: floor(50 × 0.10) = +5
5. Pre-mitigation: 35 — damage % modifiers (Section 4.6.5) are not shown in this example (assumes none from gear/buffs)

#### Variance Tiers (Design Guideline)

When designing abilities, the following tiers guide how wide the damage range should be relative to the base (midpoint) value. These tiers are a design tool — the engine only sees the resulting min-max values.

| Tier | Spread | Base 12 Example | Base 25 Example | Typical Use |
| ---- | ------ | --------------- | --------------- | ----------- |
| **Consistent** | ±10% | 10-13 | 22-27 | Reliable abilities, predictable damage |
| **Standard** | ±20% | 10-14 | 20-30 | Majority of abilities |
| **Volatile** | ±35% | 8-16 | 16-33 | High-risk abilities, thematic flavor |

Most abilities use **Standard**. Volatile and Consistent are available for thematic or mechanical reasons on a per-ability basis — there are no hard rules tying variance to damage type or element.

### 4.6.2 Basic Ability Damage

Basic abilities granted by equipment have inherent base damage, cost, crit chance, and accuracy:

- **Base Damage:** Defined per ability as a min-max range (e.g., Slash: 10-14 Physical)
- **Rank Scaling:** Basic abilities inherit their equipment's Rank; the Rank multiplier (Section 6.6.2) applies to both min and max
- **Power Scaling:** Defined per ability as a percentage of Power (e.g., "10% Combat Power")

Innate Basic abilities (Punch, Jab) have no equipment and therefore no Rank — their base values are fixed, but they still scale with Power (Combat Power).

### 4.6.3 Spell Damage

Spells (Core or Ultimate abilities with the SPELL tag) have inherent base damage:

- **Base Damage:** Defined per spell as a min-max range (e.g., Fireball: 20-28 Magic)
- **Level Scaling:** Ability level increases both min and max with diminishing returns (see Section 4.8)
- **Power Scaling:** Defined per spell as a percentage of Power (e.g., "20% Sorcery Power")

### 4.6.4 Empowered Ability Damage

When a Basic ability is empowered, damage is calculated from both sources:

- **Percentage Empower:** Basic's final damage × Empower effectiveness. No own Power scaling or variance (see Section 4.5.5 Empower Scaling and Variance Rules)
- **Flat Empower:** Basic's final damage + flat bonus (own min-max range) + Empower's own Power scaling

Crit is inherited from the Basic ability and applies to the full combined result. See Section 4.5.5.

### 4.6.5 Outgoing Damage and Healing (Modifier Order)

Modifiers from gear, buffs, and similar sources are **rolled into the combatant’s state** (rebuilt when loadout or relevant buffs change) — they are not re-scanned from inventory during every damage roll. Two broad kinds matter for this section:

- **Aggregate modifiers** — feed always-on totals (max resources, crit chance, accuracy, debuff chance/resistance, etc.).
- **Resolution modifiers** — apply when a **specific instance** of damage or healing is calculated, and are matched using ability **tags** and channels (e.g. melee vs spell damage, recovery).

**Damage instances** — order **before** the mitigation pipeline (Section 7.7):

1. **Rolled damage** from the ability (after level/rank on the min–max range; Section 4.6.1) plus **ability flat bonuses** for that hit (e.g. Power scaling, Flat Empower components). **Empowered** abilities combine Basic and Empower damage per **Section 4.6.4** first. → one **subtotal**.
2. **Additive resolution %** — all applicable modifiers for that instance (e.g. +% Melee Damage when the ability is melee-tagged) **add together**, then apply **once**: `subtotal × (1 + sum of percentages)`.
3. If the attack **crits**, apply the **crit damage multiplier** (Section 4.9.3) to this amount.
4. The result is **pre-mitigation damage** and enters Section 7.7 (penetration → Armor/MR → Shield → HP).

**Healing instances** — same pattern: **sum flat heal** for the instance, then **additive % Recovery** (and similar resolution modifiers), then any healing-specific reduction rules. **Healing cannot crit** (Section 4.9.1).

Per-step **rounding** and exact data structures are specified in the Technical Design Document; combat values remain **whole numbers** where the ability system requires it.

## 4.7 Ability Targeting


| Target Type       | Description                    | Selection Method          |
| ----------------- | ------------------------------ | ------------------------- |
| **Single Target** | Affects one specific character | Direct selection          |
| **Area Effects**  | Affects all in specified group | Automatic group targeting |
| **Self**          | Affects only the user          | Automatic                 |


**Target Categories:**

- **Enemy:** Opponent characters only
- **Ally:** Friendly characters (includes self) only
- **Self:** User only
- **Any:** Allies or enemies

**AoE Resolution:** For area-of-effect abilities, damage, accuracy, and debuff chance are rolled **independently for each target**.

**Trigger Targeting:** Triggers fire automatically and cannot use direct selection. They define their own targeting rule (Source, Self, Random Enemy, or All). See Section 4.5.6 for details.

## 4.8 Ability Leveling

### 4.8.1 Core Ability Leveling

- Only Core abilities can be leveled
- Leveling happens in the **loadout**, not on the ability item itself
- Maximum level: 10
- Limited skill points (50 at max character level, 10 slots = strategic allocation required)

### 4.8.2 Scaling Per Level


| Effect            | Scaling                                        |
| ----------------- | ---------------------------------------------- |
| **Base Value**    | Increases with diminishing returns (see below) |
| **Resource Cost** | Increases linearly                             |


### 4.8.3 Diminishing Returns

Most abilities follow a tiered value increase pattern:


| Level Range | Value Increase | Example (Fireball)  |
| ----------- | -------------- | ------------------- |
| **1-4**     | Full value     | +4 damage per level |
| **5-7**     | Moderate value | +3 damage per level |
| **8-10**    | Small value    | +2 damage per level |


### 4.8.4 Investment Strategy

- **Efficient builds:** Keep abilities at level 4 for best point efficiency
- **Max output builds:** Level to 10 despite diminishing returns
- **Spread builds:** Many abilities at moderate levels

### 4.8.5 Ability Rank

All abilities have **Rank** (★ to ★★★★★). The Rank multiplier table (Section 6.6.2) applies universally — the only difference is where the Rank comes from:


| Ability Type | Rank Source                                               |
| ------------ | --------------------------------------------------------- |
| **Basic**    | Inherited from the equipment it is attached to            |
| **Core**     | Intrinsic — honed with duplicate copies at the Trainer |
| **Ultimate** | Intrinsic — honed with duplicate copies at the Trainer |


Innate Basic abilities (Punch, Jab) have no equipment and therefore no Rank — their base values are fixed.

Rank is separate from the loadout's Skill Point level:


| Property            | Ability Level (Skill Points)      | Ability Rank (★)                                                    |
| ------------------- | --------------------------------- | ------------------------------------------------------------------- |
| **What it is**      | Loadout investment                | Item quality                                                        |
| **How it improves** | Spend Skill Points in loadout     | Hone with duplicates (Core/Ultimate) or upgrade equipment (Basic) |
| **Applies to**      | Core abilities only               | All abilities (Basic inherits from equipment)                       |
| **Maximum**         | Level 10                          | ★★★★★                                                               |
| **Scales**          | Base values (diminishing returns) | Base values (diminishing returns, see Section 6.6.2)                |


Both systems scale base values independently. A Level 10, ★★★★★ ability is significantly stronger than a Level 1, ★ version of the same ability.

**Rarity determines starting Rank** for Core and Ultimate abilities, following the same pattern as equipment:


| Rarity    | Starting Rank | Character Level Req |
| --------- | ------------- | ------------------- |
| Common    | ★             | 1                   |
| Uncommon  | ★★            | 10                  |
| Rare      | ★★★           | 20                  |
| Epic      | ★★★★          | 30                  |
| Legendary | ★★★★★         | 40                  |


Each ability has a **fixed Rarity** — there is no Common version and Legendary version of the same ability. An ability's Rarity reflects its design complexity: Common abilities are straightforward, Legendary abilities are build-defining.

**Honing** (ranking up) abilities uses duplicate copies at the Class Trainer or Tutor. See Section 11.2 for the full crafting system.

**Display example:**

```
Fireball (Lv 7)
Rank: ★★★
Rarity: Rare
Requires: Level 20
```

## 4.9 Critical Hit System

### 4.9.1 Crit Requirements

- An ability must have a **base critical chance** to crit
- Basic abilities define their own crit chance per weapon type (e.g., Stab from Dagger = high crit, Heavy Slash from Greatsword = low crit)
- Spells can define their own crit chance
- Empowered abilities inherit the Basic ability's crit chance; crit applies to the full combined damage
- **DoTs cannot crit** (Bleed benefits indirectly if the source attack crits)
- **Healing cannot crit**

### 4.9.2 Crit Formula

```
Final Crit Chance = Ability Base Crit + Character Crit Chance
```

### 4.9.3 Crit Damage

- Base multiplier: 150% (1.5× normal damage)
- Can be increased by abilities, equipment, and stats

### 4.9.4 UI Display

Display crit chance with the character's bonus in parentheses:

```
Crit: 10% (25%)
     ↑base  ↑with your Crit Chance stat
```

## 4.10 Status Effects

All status effects from abilities fall into two families: **Buffs** (positive) and **Debuffs** (negative). Equipment bonuses are NOT status effects — they are direct stat modifications.

### 4.10.1 Buff Family (Positive Effects)


| Type         | Duration                 | Removal                                | Source               |
| ------------ | ------------------------ | -------------------------------------- | -------------------- |
| **Blessing** | Temporary (has duration) | Removed by "Remove a Blessing" effects | Abilities            |
| **Passive**  | Permanent (no duration)  | Cannot be removed, only **suppressed** | Abilities, Masteries |


- Blessings display as icons in the buff row with a countdown timer
- Passives display in a separate passive row with a glowing indicator and no timer
- Shield is a Blessing with unique stacking rules (see Section 3.5.2 for FIFO depletion)
- When a Passive is suppressed, its effects and triggers are disabled until the suppression ends. The Passive is never removed — it reactivates automatically.

### 4.10.2 Debuff Family (Negative Effects)


| Type        | Duration                 | Removal                                        | Source    |
| ----------- | ------------------------ | ---------------------------------------------- | --------- |
| **Curse**   | Temporary (has duration) | Removed by "Remove a Curse" effects, or Immune | Abilities |
| **Ailment** | Temporary (DoT damage)   | Specific cleanse effects, or Immune            | Abilities |


- Curses are non-damage debuffs (stat reductions, control effects, special restrictions)
- Ailments are damage-over-time effects with distinct calculation rules (see Section 7.6)

### 4.10.3 Status Effect List

**Blessings**


| Effect           | Description                                                        | Stacking                 |
| ---------------- | ------------------------------------------------------------------ | ------------------------ |
| **Stealth**      | Cannot be targeted directly (AoE still hits, any damage breaks it) | No                       |
| **Shield**       | Temporary HP, absorbs post-mitigation damage (FIFO depletion)      | Yes (separate instances) |
| **Invulnerable** | Cannot be damaged                                                  | No                       |
| **Immune**       | Prevents new Curses and Ailments from being applied                | No                       |


**Curses**


| Effect        | Description                                                           | Stacking |
| ------------- | --------------------------------------------------------------------- | -------- |
| **Slowed**    | Speed reduced by 50                                                   | TBD      |
| **Dazed**     | Reduced Dodge Chance                                                  | TBD      |
| **Corrupted** | Prevents new Blessings from being applied. Suppresses active Passives | No       |


**Ailments**


| Effect     | Description                                                                               | Stacking                               |
| ---------- | ----------------------------------------------------------------------------------------- | -------------------------------------- |
| **Ignite** | Magic DoT, 80% of pre-mitigation damage over 2 turns                                      | No (priority queue, see Section 7.6.3) |
| **Bleed**  | True DoT, 35% of actual HP lost per turn for 2 turns (70% total). No HP damage = no Bleed | Yes                                    |
| **Poison** | True DoT, % of target's max HP                                                            | Yes                                    |


### 4.10.4 Immune and Corrupted

Immune and Corrupted naturally counter each other through the taxonomy:

- **Immune** is a Blessing. It prevents Curses and Ailments.
- **Corrupted** is a Curse. It prevents Blessings and suppresses Passives.
- If Corrupted is active → Immune cannot be applied (Immune is a Blessing, Corrupted prevents Blessings)
- If Immune is active → Corrupted cannot be applied (Corrupted is a Curse, Immune prevents Curses)

Whichever is applied first prevents the other. No special-case rule needed — this is an emergent property of the system.

### 4.10.5 Effect Display

- **Stacking** means multiple instances can exist simultaneously
- Each instance appears as a **separate icon** with its own duration
- Instances are NOT combined into a single icon
- **UI Layout:**
  - Blessings displayed in the buff row (ordered by application time)
  - Passives displayed in a separate row with glowing indicators
  - Curses and Ailments displayed in the debuff row below
  - Located near the resource HUD bars

## 4.11 Ability Stat Block Reference

### 4.11.1 Stat Block Format

All ability stat blocks show **Level 1, Rank ★** base values. All abilities have a Rank — Basic abilities inherit theirs from equipment (see Section 4.8.5). See Section 4.8 for level scaling and Section 6.6.2 for rank scaling.

**Universal Headings** (every stat block):


| Heading    | Purpose                                                   |
| ---------- | --------------------------------------------------------- |
| Class      | Who can use it (WARRIOR / MAGE / ROGUE / NEUTRAL)         |
| Type       | BASIC / CORE / ULTIMATE / ITEM                            |
| Action     | NORMAL / REACTION / BONUS / PASSIVE                       |
| Tags       | Full tag list                                             |
| Discipline | Thematic school (COMBAT / AGILITY / SORCERY / DIVINE / —) |
| Target     | Who it affects                                            |
| Effect     | What the ability does and by what amount — always present |
| Cost       | Resource cost (or — if free)                              |
| Cooldown   | Turns (or — if none applies)                              |
| Scaling    | Power scaling percentage (or — if none)                   |


**Conditional Headings** (only when applicable):


| Heading     | Appears When                                        |
| ----------- | --------------------------------------------------- |
| Accuracy    | Ability makes a hit check (absent = always hits)    |
| Crit Chance | Ability can critically hit                          |
| Condition   | Tagged CONDITIONAL — defines activation requirement |
| Empower     | Tagged EMPOWER — defines which Basic it targets     |
| Debuff      | Applies a debuff with a chance roll                 |
| Note        | Important edge cases or clarifications              |


### 4.11.2 Universal Scaling Rules


| Property                                                                                          | Scales with Level/Rank          | Fixed |
| ------------------------------------------------------------------------------------------------- | ------------------------------- | ----- |
| **Effect values** (damage, shield, restore, effectiveness %)                                      | Yes                             | —     |
| **Cost**                                                                                          | Yes (increases with level only) | —     |
| All other properties (Accuracy, Crit, Cooldown, Duration, Debuff chance, Scaling rate, Hit count) | —                               | Yes   |


### 4.11.3 Example Stat Blocks

The following examples demonstrate the stat block format across different ability types and complexities. Values are illustrative and subject to tuning.

**Punch** — Innate fallback, simplest ability

```
Punch (Innate — Main Hand)                            [Level 1, Rank ★]
  Class:       NEUTRAL
  Type:        BASIC
  Action:      NORMAL
  Tags:        ATTACK, MELEE, PHYSICAL
  Discipline:  COMBAT
  Target:      Single Enemy
  Effect:      Deal 4-6 Physical damage
  Cost:        5 Stamina
  Accuracy:    90%
  Crit Chance: 0%
  Cooldown:    —
  Scaling:     10% Combat Power
```

**Slash** — Standard weapon Basic

```
Slash (Sword — Main Hand)                             [Level 1, Rank ★]
  Class:       NEUTRAL
  Type:        BASIC
  Action:      NORMAL
  Tags:        ATTACK, MELEE, PHYSICAL
  Discipline:  COMBAT
  Target:      Single Enemy
  Effect:      Deal 10-14 Physical damage
  Cost:        10 Stamina
  Accuracy:    95%
  Crit Chance: 5%
  Cooldown:    —
  Scaling:     10% Combat Power
```

**Arcane Bolt** — Mana-based magic Basic

```
Arcane Bolt (Wand — Main Hand)                        [Level 1, Rank ★]
  Class:       NEUTRAL
  Type:        BASIC
  Action:      NORMAL
  Tags:        SPELL, MAGIC
  Discipline:  SORCERY
  Target:      Single Enemy
  Effect:      Deal 12-16 Magic damage
  Cost:        8 Mana
  Accuracy:    100%
  Cooldown:    2
  Scaling:     15% Sorcery Power
```

**Defend** — Reaction, Shield-granting

```
Defend (Kite Shield — Off Hand)                       [Level 1, Rank ★]
  Class:       NEUTRAL
  Type:        BASIC
  Action:      REACTION
  Tags:        BUFF, BLESSING
  Discipline:  DIVINE
  Target:      Self
  Effect:      Grant 15 Shield (1 turn)
  Cost:        8 Stamina
  Cooldown:    1
  Scaling:     10% Divine Power
```

**Rest** — Recovery, no combat interaction

```
Rest (Innate)                                         [Level 1, Rank ★]
  Class:       NEUTRAL
  Type:        BASIC
  Action:      NORMAL
  Tags:        RECOVERY
  Discipline:  —
  Target:      Self
  Effect:      Restore 20 Stamina
  Cost:        —
  Cooldown:    —
  Scaling:     —
  Note:        Triggers the Reaction Phase (it is a Normal Action)
```

**Fireball** — Core spell with debuff

```
Fireball (Core Ability)                               [Level 1, Rank ★]
  Class:       MAGE
  Type:        CORE
  Action:      NORMAL
  Tags:        SPELL, MAGIC, DEBUFF
  Discipline:  SORCERY
  Target:      Single Enemy
  Effect:      Deal 20-28 Magic damage with a chance to Ignite
  Cost:        15 Mana
  Accuracy:    90%
  Cooldown:    2
  Scaling:     20% Sorcery Power
  Debuff:      Ignite — 50% base chance
```

**Double Strike** — Percentage Empower

```
Double Strike (Core Ability — Empower)                [Level 1, Rank ★]
  Class:       NEUTRAL
  Type:        CORE
  Action:      NORMAL
  Tags:        ATTACK, MELEE, PHYSICAL, EMPOWER
  Discipline:  COMBAT
  Target:      Single Enemy (via empowered Basic)
  Empower:     Any main-hand melee Basic
  Effect:      Hit twice at 70% effectiveness each
  Cost:        5 (15) Stamina — Empower cost (combined with Slash)
  Cooldown:    2
  Scaling:     —
  Note:        Combined damage example: Slash deals 12 → two hits of 8 each (70%)
               Inherits Basic's crit chance; crit applies to full combined damage
```

**Shadowstrike** — Conditional, burst from Stealth

```
Shadowstrike (Core Ability — Conditional)             [Level 1, Rank ★]
  Class:       ROGUE
  Type:        CORE
  Action:      NORMAL
  Tags:        ATTACK, MELEE, PHYSICAL, CONDITIONAL
  Discipline:  AGILITY
  Target:      Single Enemy
  Condition:   Requires Stealth active
  Effect:      Deal 25-35 Physical damage
  Cost:        15 Stamina
  Accuracy:    100%
  Crit Chance: 25%
  Cooldown:    3
  Scaling:     20% Agility Power
```

**Retaliation** — Reaction/Trigger/Empower (maximum complexity)

```
Retaliation (Core Ability)                            [Level 1, Rank ★]
  Class:       WARRIOR
  Type:        CORE
  Action:      REACTION
  Tags:        BUFF, BLESSING, TRIGGER, EMPOWER, MELEE
  Discipline:  COMBAT
  Target:      Self (Blessing); Source (Trigger response)
  Empower:     Main-hand melee Basic
  Effect:      Grant Blessing (1 turn). On damage received, fire empowered
               Basic at 80% damage effectiveness against the source.
  Cost:        5 Mana
  Cooldown:    3
  Scaling:     —
  Note:        Triggered Basic pays its own Stamina cost when it fires.
               If Basic is unavailable, trigger is skipped.
```

**Judgement** — Ultimate, execute, True damage, dual scaling

```
Judgement (Ultimate Ability)                           [Level 1, Rank ★]
  Class:       WARRIOR
  Type:        ULTIMATE
  Action:      NORMAL
  Tags:        ATTACK, MELEE, CONDITIONAL
  Discipline:  COMBAT, DIVINE
  Target:      Single Enemy
  Condition:   Target below 25% HP
  Effect:      Deal 40-50 True damage
  Cost:        75 Resolve
  Cooldown:    —
  Scaling:     20% Combat Power, 20% Divine Power
```

### 4.11.4 Full Progression Example

The following table shows **Slash** across all 10 levels at **Rank ★**, demonstrating proportional diminishing returns. Per-level increments are proportional to the ability's base values (see Section 4.8.3).

**Slash — Level Progression (Rank ★)**


| Level | Damage | Cost       | Per-Level Increase |
| ----- | ------ | ---------- | ------------------ |
| 1     | 10-14  | 10 Stamina | —                  |
| 2     | 13-17  | 11 Stamina | +3 (Full)          |
| 3     | 16-20  | 12 Stamina | +3 (Full)          |
| 4     | 19-23  | 13 Stamina | +3 (Full)          |
| 5     | 21-25  | 14 Stamina | +2 (Moderate)      |
| 6     | 23-27  | 15 Stamina | +2 (Moderate)      |
| 7     | 25-29  | 16 Stamina | +2 (Moderate)      |
| 8     | 26-30  | 17 Stamina | +1 (Small)         |
| 9     | 27-31  | 18 Stamina | +1 (Small)         |
| 10    | 28-32  | 19 Stamina | +1 (Small)         |


**Rank scaling** is applied as a multiplier *after* level scaling, using the values from Section 6.6.2:


| Rank  | Multiplier  | Slash Lv 5 Example |
| ----- | ----------- | ------------------ |
| ★     | 100% (base) | 21-25              |
| ★★    | 120%        | 25-30              |
| ★★★   | 135%        | 28-33              |
| ★★★★  | 145%        | 30-36              |
| ★★★★★ | 150%        | 31-37              |


*Rank example uses Lv 5 base values (21-25). Each value is multiplied then floored: e.g., `floor(25 × 1.35) = 33`.*

Power scaling is applied separately on top of both level and rank scaling. Cost scales with level only — rank does not affect cost.

---

# 5. Character Loadouts

## 5.1 Loadout Overview

A **Loadout** is a complete character build, similar to a deck in a TCG. Players can have multiple loadouts and select which one to use when entering battle.

### 5.1.1 Loadout Components


| Component                | Description                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| **Attribute Allocation** | How the 250 Attribute Points are distributed                     |
| **Equipment Set**        | All equipped gear, including two Weapon Sets (see Section 6.1.3) |
| **Core Ability Grid**    | 10 slots with selected abilities and level investments           |
| **Ultimate Slots**       | 2 slots with selected Ultimate abilities                         |


### 5.1.2 Loadout Switching

- Players can create and save multiple loadouts
- Select loadout when entering battle (like choosing a deck)
- Different loadouts allow for different strategies without respeccing

## 5.2 Ability Grid

### 5.2.1 Grid Structure

The ability grid is a **5 column × 2 row layout** (10 slots total) for Core abilities:

```
Tier 1   Tier 2   Tier 3   Tier 4   Tier 5
[Slot 1] [Slot 3] [Slot 5] [Slot 7] [Slot 9]
[Slot 2] [Slot 4] [Slot 6] [Slot 8] [Slot 10]
```

Plus **2 Ultimate slots** (separate from the grid).

**Tier System (WIP):** Each column represents a Tier. Abilities may be restricted to certain Tiers, creating smaller pools of competition per slot. This enables balance fine-tuning — if combinations are too strong, placing abilities in the same Tier forces harder choices. Needs testing.

### 5.2.2 How Abilities Are Equipped

1. **Collect** Core/Ultimate abilities from Oracle pulls, quest rewards, or Learning at Trainer
2. **Place** abilities into loadout slots
3. **Level** Core ability slots using Skill Points (1-10)
4. **Hone** abilities by feeding duplicate copies at the Class Trainer or Tutor (increases Rank)
5. Ultimate slots cannot be leveled but CAN be Honed (ranked up)

### 5.2.3 Skill Point Economy


| Factor                      | Value             |
| --------------------------- | ----------------- |
| **Total Skill Points**      | 50 (at max level) |
| **Core Ability Slots**      | 10                |
| **Max Level per Slot**      | 10                |
| **Points to Max All**       | 100               |
| **Actual Points Available** | 50                |


**Implication:** Players can only max 5 abilities, or spread points across all 10 at moderate levels. This forces strategic allocation.

### 5.2.4 Important: Leveling is Per-Slot

- The **ability item** itself has no level — the **loadout slot** has the level
- Placing an ability in a leveled slot grants it that level's power
- **Removing an ability resets the slot to Level 0** and refunds all invested Skill Points
- Loadout editing (equipping, removing, reallocating points) can only occur outside of combat

---

# 6. Equipment System

## 6.1 Equipment Slots

Characters have **10 equipment slots** divided into two categories:


| Category        | Slots                                                    | Function           |
| --------------- | -------------------------------------------------------- | ------------------ |
| **Active (5)**  | Main Hand, Off Hand, Trinket, Consumable 1, Consumable 2 | Grant abilities    |
| **Passive (5)** | Amulet, Ring, Helmet, Body, Boots                        | Provide stats only |


### 6.1.1 Active Slots

Active slots grant usable abilities in addition to stats:


| Slot             | Valid Equipment          | Notes                                         |
| ---------------- | ------------------------ | --------------------------------------------- |
| **Main Hand**    | 1H Weapon, 2H Weapon     | Part of Weapon Set (see 6.1.3)                |
| **Off Hand**     | 1H Weapon, Shield, Focus | Disabled when 2H equipped; Part of Weapon Set |
| **Trinket**      | Trinket                  | Grants an activatable ability (details TBD)   |
| **Consumable 1** | Consumable Item          | Single-use ability                            |
| **Consumable 2** | Consumable Item          | Single-use ability                            |


**Notes:**

- Focus abilities: Grimoire grants Hex (Curse), Tome grants Mend (Healing). See Section 6.4.2.
- Ranged weapons (Bow, Crossbow) are 2H weapons competing for Main Hand.

### 6.1.2 Passive Slots

Passive slots provide stats only — no granted abilities:

- Amulet
- Ring
- Helmet
- Body
- Boots

### 6.1.3 Weapon Swap System

Characters have **two weapon sets**. Each set is a **combined pair** of Main Hand + Off Hand equipment. Only the **active set** provides stats and abilities.

#### Weapon Set Structure


| Component | Description                   |
| --------- | ----------------------------- |
| **Set 1** | Main Hand + Off Hand (paired) |
| **Set 2** | Main Hand + Off Hand (paired) |


**Important:** Weapon sets are **atomic** — swapping changes both Main Hand and Off Hand together. You cannot swap individual slots independently.

#### Swap Rules


| Rule                 | Description                                                                       |
| -------------------- | --------------------------------------------------------------------------------- |
| **Swap Cost**        | 1 Bonus Action                                                                    |
| **Stamina Cost**     | 5 Stamina                                                                         |
| **Swap Cooldown**    | 2 turns (subject to tuning)                                                       |
| **Cooldown Ticking** | Cooldowns on BOTH sets tick down every turn, even when inactive                   |
| **Active Set Only**  | Only the active set grants stats (swap away from Shield = lose Armor immediately) |
| **Innate Ability**   | All characters can swap from the start (no unlock required)                       |
| **Empty Set**        | If a set is empty, swapping to it treats the character as Unarmed                 |


#### Mastery Interactions

Masteries can modify the swap system:


| Interaction Type         | Example                                     |
| ------------------------ | ------------------------------------------- |
| **Enhance**              | "Swap cooldown reduced by 1"                |
| **Restrict for benefit** | "Cannot swap, but Bow cooldown -1" (Ranger) |
| **Enable combos**        | "Can wield Crossbow one-handed" (Mercenary) |


## 6.2 Equipment Design Philosophy

### 6.2.1 Core Principle: Meaningful Opportunity Cost

Equipment design reinforces the balance philosophy that every build should have **clear strengths AND clear weaknesses**.


| Goal                       | Implementation                                         |
| -------------------------- | ------------------------------------------------------ |
| **Strengths & Weaknesses** | Each attribute investment has intentional gear gaps    |
| **Opportunity Cost**       | Desirable gear may require spreading attributes        |
| **Soft Push, Not Force**   | Pure builds are valid but accept limitations           |
| **Intentional Gaps**       | Not every combination needs a type — gaps are features |


### 6.2.2 Attribute Balance Through Equipment


| Attribute | Equipment Strengths                                   | Intentional Gaps             |
| --------- | ----------------------------------------------------- | ---------------------------- |
| **STR**   | High base ability damage, best armor, +HP boots       | Limited speed options        |
| **DEX**   | Speed boots, dodge body, crit damage helmets          | Low base ability damage      |
| **INT**   | High MR gear, mana helmets, debuff chance boots       | No armor access              |
| **FTH**   | Debuff resistance (body + boots), resolve gen helmets | No offensive equipment stats |


**Design intent:** A pure INT mage SHOULD struggle to get Armor. If they want defensive options, they spread into STR for armor equipment access — that's a meaningful choice.

### 6.2.3 Encouraging Attribute Spread

The system softly encourages hybrid builds:

- Desirable gear often requires secondary stat investment
- Pure single-stat gear exists but may have trade-offs
- Players naturally face the choice: "Stack more, or spread for this item?"

**Neither pure nor spread builds are "correct"** — both have trade-offs, and that's the goal.

### 6.2.4 Predefined Items

All equipment is **fully predefined** — no random affixes or rolls:

- Every item has fixed stats and effects determined at design time
- Players know exactly what an item does before acquiring it
- Enables precise balance tuning (similar to TCG card design)
- Supports strategic counterplay and build planning

### 6.2.5 Vanilla Items Have Very High Base Stats

Following TCG design principles (vanilla creatures tend to have better stats):


| Item Type      | Base Stats | Mods                 | Use Case                |
| -------------- | ---------- | -------------------- | ----------------------- |
| Vanilla        | Very High  | None                 | Raw power, no utility   |
| Effect Items   | Lower      | Yes                  | Utility, build-enabling |
| Downside Items | Very High  | Yes (with drawbacks) | Risk/reward, niche      |


This ensures vanilla items remain competitively viable rather than being immediately outclassed. Exceptions may exist for specific balance reasons.

## 6.3 Equipment Types

### 6.3.1 Type as Foundation

Every piece of equipment is built on a base **Type**. The Type defines:


| Defines              | Description                                         |
| -------------------- | --------------------------------------------------- |
| **Base Stats**       | The power numbers that scale with Rank              |
| **Fixed Properties** | Slot, tags, two-handed, etc.                        |
| **Requirements**     | Attribute requirements to equip                     |
| **Granted Ability**  | For Active equipment, the Basic ability it provides |


### 6.3.2 Rarity Branches from Type

All items of the same Type share the same foundation. Rarity determines the specific item and its Mods:

```
GREATSWORD (Type)
├── Base Stats: High damage
├── Fixed: High stamina, low crit, 2H
├── Requirements: Primarily STR
├── Granted Ability: Heavy Slash
│
├── Common: "Steel Greatsword" — vanilla, highest damage
├── Uncommon: "Serrated Greatsword" — +% chance to inflict bleed
└── Legendary: "Frostbane" — Build defining chance to inflict the slow debuff
```

**Item names always display Type:** "Frostbane (GREATSWORD)" — so players always know the foundation.

### 6.3.3 Type Defines Granted Ability (Active Equipment)

For equipment that grants abilities (weapons, shields, focuses, trinkets, consumables):

- **Same Type = Same Ability** regardless of rarity
- A Common GREATSWORD and Legendary GREATSWORD both grant "Heavy Slash"
- The ability comes from the TYPE, not the specific item
- Mods may enhance the ability, but the base ability is consistent

This creates clarity: players know exactly what ability they'll get from any GREATSWORD.

### 6.3.4 Flexible Requirements

Equipment attribute requirements are checked against **Base Attributes** only (level-up point allocation). Equipment bonuses, amulet bonuses, and temporary buffs do not count toward meeting requirements.

Requirements are NOT always 50/50 splits. Players can spread base attributes to access a wider range of equipment:


| Type        | Primary | Secondary | Example Req                 |
| ----------- | ------- | --------- | --------------------------- |
| Greatsword  | 80% STR | 20% DEX   | ~100 Base STR, ~25 Base DEX |
| Dagger      | 80% DEX | 20% STR   | ~100 Base DEX, ~25 Base STR |
| Sword       | 50% STR | 50% DEX   | ~60 Base each               |
| Kite Shield | 60% STR | 40% FTH   | ~75 Base STR, ~50 Base FTH  |


This allows nuance without rigid formulas.

**Design intent:** Base-only requirements prevent circular dependencies (e.g., equipping an amulet to meet a requirement, then swapping the amulet). Attribute allocation is the strategic commitment — equipment builds on top of it.

### 6.3.5 Equipment Classification Summary


| Property   | Description                                 | Examples                     |
| ---------- | ------------------------------------------- | ---------------------------- |
| **Type**   | Foundation defining all properties          | Greatsword, Dagger, Plate    |
| **Rarity** | Mod character + base rank                   | Common, Rare, Legendary      |
| **Slot**   | Valid equipment locations (can be multiple) | Main Hand, Off Hand, Body    |
| **Tags**   | Cross-type groupings for effect targeting   | Weapon, Armor, Melee, Ranged |


**Tags are minimal** — only used when effects need to target multiple Types at once (e.g., "+10% Melee damage" targets all melee weapons). Tags should NOT duplicate Type or Slot information.

## 6.4 Equipment Types

Equipment types are organized by slot category. Each type defines attribute requirements, granted abilities (for Active equipment), and stat profiles (for Passive equipment). Stat values are subject to tuning.

### 6.4.1 Weapon Types

12 weapon types organized by attribute combination. Each type defines a main hand Basic ability. Sword and Dagger can also be equipped in the off hand with a different ability.


| Type           | Req     | Hands | Main Hand Ability | Off-Hand Ability |
| -------------- | ------- | ----- | ----------------- | ---------------- |
| **Axe**        | STR     | 1H    | Cleave            | —                |
| **Battle Axe** | STR     | 2H    | Heavy Cleave      | —                |
| **Sword**      | STR/DEX | 1H    | Slash             | Thrust           |
| **Greatsword** | STR/DEX | 2H    | Heavy Slash       | —                |
| **Staff**      | STR/INT | 2H    | Force Strike      | —                |
| **Mace**       | STR/FTH | 1H    | Bash              | —                |
| **Warhammer**  | STR/FTH | 2H    | Heavy Bash        | —                |
| **Bow**        | DEX     | 2H    | Shoot Arrow       | —                |
| **Dagger**     | DEX/INT | 1H    | Stab              | Shank            |
| **Crossbow**   | DEX/FTH | 2H    | Shoot Bolt        | —                |
| **Wand**       | INT     | 1H    | Arcane Bolt       | —                |
| **Sceptre**    | INT/FTH | 1H    | Radiance          | —                |


**Design notes:**

- STR, STR/DEX, and STR/FTH have both 1H and 2H options — reflects STR's versatile combatant identity
- STR/INT has only a 2H option (Staff) — intentional gap
- DEX weapons have low base damage but high crit or speed — burst damage theme
- 2H weapons disable the off-hand slot
- "Heavy [X]" naming convention: 2H versions use the prefix "Heavy" (Slash → Heavy Slash, Cleave → Heavy Cleave, Bash → Heavy Bash)
- Wand's Arcane Bolt is mana-based single-target Magic damage, scaling with Sorcery Power
- Sceptre's Radiance is mana-based AoE Magic damage with a cooldown, scaling with Divine Power. The only AoE Basic ability in the game — balanced by cooldown and lower per-target damage

### 6.4.2 Off-Hand Equipment

Off-hand equipment falls into three categories based on attribute alignment. All off-hand items replace Jab when equipped.

**Shields (STR-based)**


| Type             | Req     | Ability | Notes                            |
| ---------------- | ------- | ------- | -------------------------------- |
| **Tower Shield** | STR     | Block   | Highest armor, passive reduction |
| **Kite Shield**  | STR/FTH | Defend  | Shield buff, Divine scaling      |


**Focuses (INT-based)**


| Type         | Req     | Ability | Notes                                                                                                  |
| ------------ | ------- | ------- | ------------------------------------------------------------------------------------------------------ |
| **Grimoire** | INT     | Hex     | 100% chance to apply Curse: target takes +X% increased damage from next hit. Scales with Sorcery Power |
| **Tome**     | INT/FTH | Mend    | Healing, mana-based, cooldown. Scales with Divine Power                                                |


**Dual-Wield Weapons**

Sword and Dagger (from Section 6.4.1) can be equipped in the off hand. When in the off hand, they grant a different Basic ability:


| Type       | Req     | Off-Hand Ability |
| ---------- | ------- | ---------------- |
| **Sword**  | STR/DEX | Thrust           |
| **Dagger** | DEX/INT | Shank            |


**Design notes:**

- Shields = STR combinations (tank fantasy)
- Focuses = INT combinations (caster fantasy)
- Dual-wield = DEX combinations (agile fighter fantasy)
- Any build can equip any off-hand if attribute requirements are met — requirements are soft-steers, not restrictions
- Off-hand slot is disabled when a 2H weapon is equipped in the main hand

### 6.4.3 Armor Types

Passive armor provides stats that scale with Equipment Rank. Each attribute defines one stat per slot. Hybrid armor combines both attributes' stats at reduced values (same principle as hybrid amulets). 10 types per slot: 4 pure + 6 hybrid.

**Stat Mapping:**


| Slot       | STR           | DEX          | INT              | FTH               |
| ---------- | ------------- | ------------ | ---------------- | ----------------- |
| **Body**   | Armor         | Dodge Chance | Magic Resistance | Debuff Resistance |
| **Helmet** | Stamina Regen | Crit Damage  | Mana             | Resolve Gen       |
| **Boots**  | +HP           | Speed        | Debuff Chance    | Debuff Resistance |


**Body Armor — Defensive**


| Type           | Req     | Stats                               |
| -------------- | ------- | ----------------------------------- |
| **Plate**      | STR     | Armor                               |
| **Leather**    | DEX     | Dodge Chance                        |
| **Robe**       | INT     | Magic Resistance                    |
| **Vestments**  | FTH     | Debuff Resistance                   |
| **Brigandine** | STR/DEX | Armor, Dodge Chance                 |
| **Chainmail**  | STR/INT | Armor, Magic Resistance             |
| **Cuirass**    | STR/FTH | Armor, Debuff Resistance            |
| **Cloak**      | DEX/INT | Dodge Chance, Magic Resistance      |
| **Surcoat**    | DEX/FTH | Dodge Chance, Debuff Resistance     |
| **Cassock**    | INT/FTH | Magic Resistance, Debuff Resistance |


**Helmet — Efficiency / Sustain**


| Type          | Req     | Stats                      |
| ------------- | ------- | -------------------------- |
| **Helm**      | STR     | Stamina Regen              |
| **Hood**      | DEX     | Crit Damage                |
| **Circlet**   | INT     | Mana                       |
| **Crown**     | FTH     | Resolve Gen                |
| **Sallet**    | STR/DEX | Stamina Regen, Crit Damage |
| **Coif**      | STR/INT | Stamina Regen, Mana        |
| **Greathelm** | STR/FTH | Stamina Regen, Resolve Gen |
| **Mask**      | DEX/INT | Crit Damage, Mana          |
| **Cowl**      | DEX/FTH | Crit Damage, Resolve Gen   |
| **Mitre**     | INT/FTH | Mana, Resolve Gen          |


**Boots — Utility / Survivability**


| Type         | Req     | Stats                            |
| ------------ | ------- | -------------------------------- |
| **Greaves**  | STR     | +HP                              |
| **Striders** | DEX     | Speed                            |
| **Slippers** | INT     | Debuff Chance                    |
| **Clogs**    | FTH     | Debuff Resistance                |
| **Boots**    | STR/DEX | +HP, Speed                       |
| **Treads**   | STR/INT | +HP, Debuff Chance               |
| **Sabatons** | STR/FTH | +HP, Debuff Resistance           |
| **Wraps**    | DEX/INT | Speed, Debuff Chance             |
| **Trackers** | DEX/FTH | Speed, Debuff Resistance         |
| **Sandals**  | INT/FTH | Debuff Chance, Debuff Resistance |


**Design notes:**

- 4 pure + 6 hybrid types per slot (10 total each)
- Every attribute combination has dedicated armor — no build is unsupported
- Each slot has a distinct stat theme: Body (defense), Helmet (efficiency/sustain), Boots (utility/survivability)
- Hybrid armor grants both stats at reduced values — pure armor gets more of one stat (same trade-off as amulets)
- FTH Debuff Resistance appears on both Body and Boots — intentional, FTH identity is resilience and doubling down is a valid build choice
- Cross-equipping is valid — a Mage who invests in STR can wear Plate

### 6.4.4 Jewelry Types

Jewelry has **no attribute requirements**, providing build-flexible options for any character.

**Ring — Percentage Modifiers (11 types)**

Rings are the exclusive source of percentage multipliers and flat percentage chance bonuses. No other equipment slot provides these modifiers.


| Type              | Stat                 |
| ----------------- | -------------------- |
| **Obsidian Ring** | +% Crit Chance       |
| **Topaz Ring**    | +% Accuracy          |
| **Venom Ring**    | +% Debuff Chance     |
| **Ward Ring**     | +% Debuff Resistance |
| **Iron Ring**     | +% Melee Damage      |
| **Jade Ring**     | +% Ranged Damage     |
| **Silver Ring**   | +% Spell Damage      |
| **Copper Ring**   | +% Ailment Damage    |
| **Gold Ring**     | +% Recovery Amount   |
| **Ruby Ring**     | +% HP                |
| **Pearl Ring**    | +% Mana              |


**Amulet — Attribute Investment (11 types)**

Opportunity cost: pure amulets give fewer total points but focused. Hybrid amulets give more total but split. Opal gives the most total but least per stat.


| Type                 | Stats            | Total |
| -------------------- | ---------------- | ----- |
| **Ruby Amulet**      | +20 STR          | 20    |
| **Emerald Amulet**   | +20 DEX          | 20    |
| **Sapphire Amulet**  | +20 INT          | 20    |
| **Diamond Amulet**   | +20 FTH          | 20    |
| **Citrine Amulet**   | +15 STR, +15 DEX | 30    |
| **Amethyst Amulet**  | +15 STR, +15 INT | 30    |
| **Garnet Amulet**    | +15 STR, +15 FTH | 30    |
| **Turquoise Amulet** | +15 DEX, +15 INT | 30    |
| **Amber Amulet**     | +15 DEX, +15 FTH | 30    |
| **Moonstone Amulet** | +15 INT, +15 FTH | 30    |
| **Opal Amulet**      | +10 All          | 40    |


**Design notes:**

- No attribute requirements — any build can equip any jewelry
- **Aggregate** ring stats (e.g. +% Crit Chance, +% Accuracy, debuff stats, +% HP/Mana affecting pools) feed **character totals**; the UI shows **final** values — a separate line for the ring’s contribution is optional
- **Resolution** ring stats (e.g. +% Melee/Ranged/Spell/Ailment damage, +% Recovery Amount) apply when damage or healing **resolves** — see **Section 4.6.5** (order: sum flats, then additive resolution %, then crit for damage only, then mitigation in Section 7.7)
- No gemstone or metal name is shared between rings and amulets — each piece is immediately identifiable by name
- Amulet values (20/15/10) are subject to tuning — the ratio between pure, hybrid, and spread is the design anchor

---

## 6.5 Equipment Properties

Equipment properties fall into three categories:

### 6.5.1 Fixed Properties (Never Scale)

Define the item's **identity** — constant regardless of Rank:


| Property               | Examples                                 |
| ---------------------- | ---------------------------------------- |
| Slot                   | Main Hand, Off Hand, Body, Ring, etc.    |
| Tags                   | Weapon, Armor, Melee, Ranged             |
| Two-Handed             | Yes/No (determines if off-hand disabled) |
| Attribute Requirements | Which attributes needed to equip         |


### 6.5.2 Base Stats (Scale with Rank)

The **power numbers** that increase when you temper:


| Category                                              | What Scales with Rank                                 |
| ----------------------------------------------------- | ----------------------------------------------------- |
| **Active Equipment** (Weapons, Shields, Focuses)      | Granted ability values (damage, cost, crit, etc.)     |
| **Passive Equipment** (Armor, Helmet, Boots, Jewelry) | Stat bonuses (Armor, MR, HP, Speed, attributes, etc.) |


Specific stat profiles per type are defined in Section 6.4.

### 6.5.3 Mods (Predefined, Never Scale)

Unique effects that differentiate items:

- Predefined per item — not random
- Never scaled by Rank — effects stay fixed
- Higher rarity = more powerful/interesting mods

**Examples:** +10% Crit Damage, 20% chance to Bleed, -15 Speed (downside), On hit: Restore 5 Stamina

## 6.6 Rarity and Rank System

### 6.6.1 Rarity Overview

Rarity determines drop frequency, mod character, and starting rank:


| Rarity    | Rank  | Level Req | Mods                   | Base Stats | Copies to Max | Color  |
| --------- | ----- | --------- | ---------------------- | ---------- | ------------- | ------ |
| Common    | ★     | 1         | None (vanilla)         | Highest    | 14            | Gray   |
| Uncommon  | ★★    | 10        | Minor utility          | Lower      | 12            | Green  |
| Rare      | ★★★   | 20        | Notable effects        | Lower      | 9             | Blue   |
| Epic      | ★★★★  | 30        | Powerful, may downside | Varies     | 5             | Purple |
| Legendary | ★★★★★ | 40        | Build-defining         | Varies     | Already max   | Orange |


### 6.6.2 Rank Scaling (Diminishing Returns)


| Rank  | Scaling | Cumulative |
| ----- | ------- | ---------- |
| ★     | Base    | 100%       |
| ★★    | +20%    | 120%       |
| ★★★   | +15%    | 135%       |
| ★★★★  | +10%    | 145%       |
| ★★★★★ | +5%     | 150%       |


### 6.6.3 Design Tradeoffs

- **Maximum raw stats:** Common → Temper to ★★★★★ (14 copies, cheap per copy but many needed)
- **Cool effects, no grinding:** Legendary (drops at ★★★★★, immediately usable)
- **Balance of both:** Rare/Epic items (fewer copies, moderate forge cost)
- Higher rarity items cost more total Materials to max via forging, but require fewer copies. This rarity premium is intentional — better items demand greater investment.

## 6.7 Blacksmith System

The Blacksmith NPC handles all equipment crafting using **Materials** (universal crafting currency):

### 6.7.1 Salvaging

Break down any equipment into Materials. Value scales with rarity:


| Rarity    | Salvage Value |
| --------- | ------------- |
| Common    | 1 Material    |
| Uncommon  | 3 Materials   |
| Rare      | 9 Materials   |
| Epic      | 27 Materials  |
| Legendary | 81 Materials  |


### 6.7.2 Forging

Spend Materials to create any specific equipment piece at its base Rank (player chooses exact type and rarity):


| Rarity            | Forge Cost    |
| ----------------- | ------------- |
| Common (★)        | 3 Materials   |
| Uncommon (★★)     | 9 Materials   |
| Rare (★★★)        | 27 Materials  |
| Epic (★★★★)       | 81 Materials  |
| Legendary (★★★★★) | 243 Materials |


Forge cost is always 3× the salvage value of that rarity (salvage 3 unwanted → forge 1 specific).

### 6.7.3 Tempering (Rank-Up)

Feed duplicate copies of the **same item** (any Rank) to increase its Rank:


| Upgrade      | Copies Required |
| ------------ | --------------- |
| ★ → ★★       | 2 copies        |
| ★★ → ★★★     | 3 copies        |
| ★★★ → ★★★★   | 4 copies        |
| ★★★★ → ★★★★★ | 5 copies        |


Copies are consumed at **any Rank** (additive, not multiplicative). Total copies to max from each starting Rank:


| Rarity    | Start | Copies to Max       |
| --------- | ----- | ------------------- |
| Common    | ★     | 2+3+4+5 = **14**    |
| Uncommon  | ★★    | 3+4+5 = **12**      |
| Rare      | ★★★   | 4+5 = **9**         |
| Epic      | ★★★★  | **5**               |
| Legendary | ★★★★★ | **0** (already max) |


Duplicate copies can be found through pulls, PvE drops, or Forged from Materials.

### 6.7.4 Crafting Loop

1. Get drops → Keep items you want, Salvage unwanted → Materials
2. Forge Materials into specific copies you need
3. Temper target items with copies to higher Ranks

### 6.7.5 Acquisition Methods


| Source      | Description                              |
| ----------- | ---------------------------------------- |
| Gambler     | Slot-targeted random pulls (gold sink)   |
| PvE Battles | Primary drop source, targeted encounters |
| PvP Battles | Rare random drops                        |
| Forging     | Created from Materials at Blacksmith     |


## 6.8 Prototype Scope

**Prototype:** Common equipment only, base stats framework.

**Full game adds:** Complete rarity/rank system, Salvage/Forge/Temper economy, full item variety.

---

# 7. Battle System

## 7.1 Initiative System

The initiative system uses a **Conditional Turn-Based (CTB)** model — a system where turn order is not fixed but determined dynamically by each character's Speed. All characters accumulate initiative simultaneously and the first to reach the threshold takes a turn.

### 7.1.1 Core Mechanics


| Rule                   | Description                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Accumulation**       | All characters gain initiative simultaneously, proportional to their Speed stat                                          |
| **Threshold**          | A character becomes eligible for a turn when their initiative reaches **≥100**                                           |
| **Turn Selection**     | If multiple characters reach ≥100 in the same tick, the character with the **highest initiative** takes their turn first |
| **Hard Reset**         | The selected character's initiative resets to **0** on turn start (excess is not carried over)                           |
| **Remaining Eligible** | After the turn resolves, if other characters are still ≥100, the next highest takes their turn                           |
| **Ties**               | If two or more characters have exactly equal initiative ≥100, random selection breaks the tie                            |


**Speed-to-turn ratio:** A character with twice the Speed takes approximately twice as many turns. To minimize overflow loss from the hard reset, the Speed value is divided down into small per-tick increments (e.g., Speed 100 might add 1.0 initiative per tick, requiring 100 ticks to reach the threshold). The finer the granularity, the less initiative is wasted on reset — preserving accurate Speed ratios.

**Example:** Character A (Speed 100) vs Character B (Speed 50)

- A reaches 100 initiative in half the time B does
- A takes roughly 2 turns for every 1 turn B takes
- After A takes a turn and resets to 0, B continues accumulating from where they were

### 7.1.2 Execution Order

During the Execution Phase (Phase 5), all submitted actions resolve in **current initiative order**, highest to lowest. The turn character **typically** resolves last because they were hard reset to 0:


| Character                       | Initiative at Execution | Resolution              |
| ------------------------------- | ----------------------- | ----------------------- |
| Reactor with highest initiative | e.g., 95                | Resolves first          |
| Reactor with lower initiative   | e.g., 70                | Resolves second         |
| Turn character                  | 0 (hard reset)          | Typically resolves last |


**Exception — Initiative gained during Action Selection:** Bonus actions execute before the Execution Phase. If a bonus action grants the turn character initiative (e.g., a buff that adds initiative), the turn character may have non-zero initiative during execution and could resolve **before** some or all reactors. This is intentional skill expression — the turn character spends resources to bypass the reaction threat, and the non-turn characters can see the initiative change and choose not to waste resources on a reaction.

### 7.1.3 Tie-Breaking Rules


| Situation                                                                | Rule                                                                                           |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| **Turn selection:** Multiple characters reach ≥100 with different values | Highest initiative goes first                                                                  |
| **Turn selection:** Multiple characters reach ≥100 with equal values     | Random selection; remaining eligible characters take their turns immediately after in sequence |
| **Execution phase:** Non-turn characters with equal initiative           | Random selection among tied non-turn characters                                                |
| **Execution phase:** Turn character tied with non-turn character(s)      | Non-turn characters have priority over the turn character                                      |


**Design intent for execution ties:** Beating non-turn characters in execution order must be **earned** (e.g., through bonus actions that grant initiative), not a happy coincidence of equal values. When initiative is tied during execution, the turn character always resolves last among the tied group.

### 7.1.4 Initiative Manipulation

- Speed modifications (buffs, debuffs, equipment) affect the accumulation rate
- Abilities can directly modify a character's current initiative value (e.g., "reduce target's initiative by 50")
- Faster characters may get consecutive turns if they reach 100 again before slower characters

## 7.2 Battle Format

### 7.2.1 Team Size


| Mode    | Team Size                  | Notes                                                                        |
| ------- | -------------------------- | ---------------------------------------------------------------------------- |
| **PvP** | 1v1 or 2v2                 | Maximum 2 characters per side                                                |
| **PvE** | 1-2 players vs 1-2 enemies | Enemy count may increase for full game, but architecture targets small teams |


2v2 is the maximum team size for PvP. The engine and state management should be designed around a maximum of **2 characters per side** as the baseline, with the understanding that PvE encounters could expand this modestly (e.g., 3-4 enemies) in the full game if the architecture permits without significant rework.

**Prototype:** 1v1 only for initial implementation. 2v2 support is a stretch goal within prototype scope.

### 7.2.2 Targeting in Team Battles

In 2v2 battles:

- Single-target abilities require the player to select which enemy (or ally) to target
- AoE abilities affect all valid targets in the specified group (all enemies, all allies, etc.)
- Self-targeting abilities always target the caster
- Each character on a team takes their own turn based on individual initiative

## 7.3 Turn Structure

Battles progress through six distinct phases. Each phase has a **design name** (documentation and UI) and a stable **identifier** for specifications and code (e.g. a `BattlePhase` enum or equivalent).


| # | Phase (design / UI)      | Identifier            | Description                                       | Actions                                                         |
| - | ------------------------ | --------------------- | ------------------------------------------------- | --------------------------------------------------------------- |
| 1 | **Initiative**           | `INITIATIVE`          | Accumulate initiative until character reaches 100 | Initiative gain based on speed                                  |
| 2 | **Start of Turn**        | `START_OF_TURN`       | Process start-of-turn effects                     | Regeneration, ailment damage, triggers                          |
| 3 | **Action Selection**     | `ACTION_SELECTION`    | Active character selects bonus and normal actions | Weapon Swap (bonus action), other bonus actions → Normal action |
| 4 | **Reaction Selection**   | `REACTION_SELECTION`  | Non-turn characters select reaction abilities     | Hidden selection; know action selected but not which            |
| 5 | **Execution**            | `EXECUTION`           | Actions resolve in initiative order               | Highest initiative first                                        |
| 6 | **End of Turn**          | `END_OF_TURN`         | Process end-of-turn effects                       | Cooldowns, durations, then return to Phase 1                    |


Identifiers are **canonical names** for implementation. Exact type names, source files, numeric enum values (if any), and wire formats are defined in the **Technical Design Document**. The **#** column is documentation order only.

### 7.3.1 Reaction Phase Details

**Reaction Selection** — Phase **4**, identifier `REACTION_SELECTION` (see Section 7.3). Also referred to as the **Reaction Phase** in prose.

- The Reaction Phase begins only AFTER the turn player selects a Normal Action
- Reactors know that an action was selected (the phase wouldn't start otherwise)
- Reactors do NOT know which specific action was selected
- Rest counts as a Normal Action and triggers the Reaction Phase
- UI may display: "The turn player has selected a normal action"

### 7.3.2 Battle Resolution

- Player character death (with no allies) = defeat
- All enemies defeated = victory
- Simultaneous death (rare, e.g., self-destruct abilities) = draw, treated as double loss

### 7.3.3 Death and Action Cancellation

If a character dies before their selected action executes (e.g., killed by a reaction), their action is **canceled** and does not resolve.

## 7.4 Effect Timing System

All timer effects process at **turn start**:

### 7.4.1 Start of Turn Processing (in order)

1. Resource regeneration (Stamina, limited HP/Mana regen)
2. Bonus Actions reset to maximum
3. Ailment damage (poison, bleed, ignite)
4. Cooldown decrements
5. Buff and debuff duration decrements
6. Start-of-turn triggers

### 7.4.2 End of Turn Processing

1. End-of-turn triggers

## 7.5 Cooldown System

### 7.5.1 Core Mechanics

- Cooldowns decrement at the **start** of the character's turn
- Only the turn character's cooldowns are reduced
- Reaction abilities follow standard cooldown rules

### 7.5.2 Cooldown Meanings


| Cooldown | Meaning          | Usable Pattern                                |
| -------- | ---------------- | --------------------------------------------- |
| **0**    | No cooldown      | Every turn, multiple times if resources allow |
| **1**    | Once per turn    | Every turn, but only once (prevents spam)     |
| **2**    | Every other turn | Turn 1, 3, 5, 7...                            |
| **3**    | Every third turn | Turn 1, 4, 7, 10...                           |


**Example:** A 1-turn cooldown on a Bonus Action prevents using it multiple times in one turn, but it's available every turn.

### 7.5.3 Weapon Swap Cooldown

The Weapon Swap has its own cooldown (see Section 6.1.3 for full swap rules). Ability cooldowns on weapon sets follow one exception to normal rules:


| Rule                 | Behavior                                                                                            |
| -------------------- | --------------------------------------------------------------------------------------------------- |
| **Swap Cooldown**    | 2 turns after swapping (subject to tuning)                                                          |
| **Both Sets Tick**   | Ability cooldowns on BOTH weapon sets (active and inactive) decrement at the character's turn start |
| **Why This Matters** | Swapping to Set 2 doesn't "freeze" Set 1's cooldowns — they keep ticking in the background          |


This enables tactical swap timing: use a high-cooldown ability on Set 1, swap to Set 2, and by the time you swap back, the cooldown may have expired.

## 7.6 Ailments

Ailments are damage-over-time effects with distinct strategic identities:

### 7.6.1 Ailment Overview


| Ailment    | Damage Type | Calculation                                | Duration               | Stacking            |
| ---------- | ----------- | ------------------------------------------ | ---------------------- | ------------------- |
| **Poison** | True        | % of target's Max HP                       | Varies                 | Yes                 |
| **Bleed**  | True        | 35% of actual HP lost per turn             | 2 turns (70% total)    | Yes                 |
| **Ignite** | Magic       | 80% of PRE-mitigation damage over duration | 2 turns (40% per tick) | No (priority queue) |


### 7.6.2 Ailment Strategic Identity

**Poison:**

- Deals True damage based on target's Max HP
- Ignores the damage of the ability that applied it
- Natural counter to HP-stacking tanks

**Bleed:**

- Deals True damage scaling from **actual HP lost** (after all mitigation including Armor/MR and Shield absorption)
- If the source hit dealt zero HP damage (fully absorbed by Shield), no Bleed is applied
- Partial Shield absorption: Bleed is based only on the HP portion (e.g., 50 post-armor damage → 30 absorbed by Shield → 20 HP lost → Bleed = 35% of 20 = 7 True damage per turn)
- Synergy: Strip or deplete Shield before applying Bleed; maximize the hit that causes it (damage buffs, armor penetration)

**Ignite:**

- Deals Magic damage, calculated from PRE-mitigation ability damage
- The DoT is then reduced by target's MR and absorbed by Shield
- Can apply while enemy has high defenses — base damage is locked in
- Synergy: Apply Ignite, THEN strip target's MR to amplify ticks
- Does not stack (see priority queue below)

### 7.6.3 Ignite Priority Queue

Because Ignite does not stack, multiple Ignites are handled specially:


| Rule                                    | Behavior                                           |
| --------------------------------------- | -------------------------------------------------- |
| All Ignites are tracked separately      | Each has own damage value and duration             |
| Only highest-damage Ignite deals damage | Per tick, the strongest active Ignite applies      |
| Durations are independent               | Each Ignite counts down on its own                 |
| UI shows longest remaining duration     | Player sees the maximum turns remaining            |
| When highest expires, next takes over   | Lower-damage Ignites activate when higher ones end |


### 7.6.4 Ailment Timing

- Ailment damage is applied at the **start** of the affected character's turn
- Ailment durations decrease at the **start** of the affected character's turn (after damage)

## 7.7 Damage and Mitigation

### 7.7.1 Defenses Definition

**Defenses** refers collectively to: **Armor**, **Magic Resistance**, and **Shield**.

### 7.7.2 Defense Formulas


| Defense              | Effect                                     |
| -------------------- | ------------------------------------------ |
| **Armor**            | 1 Armor = 1 Physical damage reduced (flat) |
| **Magic Resistance** | 1 MR = 1 Magic damage reduced (flat)       |
| **Shield**           | Absorbs post-mitigation damage (FIFO)      |


**Note:** Armor and MR can reduce damage to 0. This is intended for the tank power fantasy, with counterplay via True damage and Resolve generation.

### 7.7.3 Defense Penetration

When an ability "penetrates Defenses by X%":

- X% of the Defense value is ignored
- Example: 30% penetration vs 50 Armor → Only 35 Armor applies (70% of 50)

### 7.7.4 Damage Flow

**Pre-mitigation damage** is the amount produced by ability resolution — Sections 4.6.1–4.6.5 (roll, flats, additive resolution %, crit if applicable) — **before** penetration, Armor/MR, Shield, and HP loss.

For Physical and Magic damage:

```
Incoming Damage
    ↓
[1. Defense Penetration] — Reduce effective Armor/MR if applicable
    ↓
[2. Armor/MR Mitigation] — Flat reduction (1:1)
    ↓
[3. Shield Absorption] — Absorbs remaining damage (FIFO)
    ↓
[4. HP Loss] — Takes remaining damage
```

For True damage:

```
Incoming True Damage
    ↓
[Direct HP Loss] — Bypasses Armor, MR, AND Shield
```

## 7.8 Accuracy and Dodge System

### 7.8.1 Accuracy Rules

Each ability defines its own **Base Accuracy** as part of its stat block. If an ability does **not** define a Base Accuracy, no accuracy check is made — the ability always hits. This applies naturally to most buffs, recovery abilities, and self-targeting effects, which have no accuracy property and therefore never miss.

### 7.8.2 Hit Chance Formula

For abilities that define a Base Accuracy, hit chance is calculated as:

```
Final Hit Chance = Ability Base Accuracy + Attacker's Accuracy − Defender's Dodge Chance
```

The result is then clamped:

- **Minimum:** 100% − Defender's Max Dodge Chance (default 65%, so minimum hit = 35%)
- **Maximum:** 100%

### 7.8.3 Dodge as Mitigation

When an attack is dodged:

- The attacker gains Resolve for the **full damage amount** (as if it was mitigated)
- This is intentional compensation and can lead to strategic plays

### 7.8.4 Scaling


| Stat                 | Source                                      | Rate          |
| -------------------- | ------------------------------------------- | ------------- |
| **Accuracy**         | Dexterity + Equipment                       | +1% per 4 DEX |
| **Dodge Chance**     | Dexterity + Equipment                       | +1% per 4 DEX |
| **Max Dodge Chance** | Base 65%, modified by Equipment + Abilities | Varies        |


Because DEX provides BOTH Accuracy and Dodge equally, characters with equal DEX cancel each other out.

### 7.8.5 UI Display

Display ability accuracy with the character's bonus in parentheses:

```
Accuracy: 100% (150%)
         ↑base  ↑with your Accuracy stat
```

## 7.9 Debuff Application System

### 7.9.1 Debuff Chance Formula

```
Final Debuff Chance = Ability Base Chance + Attacker's Debuff Chance − Defender's Debuff Resistance
```

Clamped to 0%–100%.

### 7.9.2 Scaling


| Stat                  | Source                   | Rate          |
| --------------------- | ------------------------ | ------------- |
| **Debuff Chance**     | Intelligence + Equipment | +1% per 3 INT |
| **Debuff Resistance** | Faith + Equipment        | +1% per 3 FTH |


### 7.9.3 UI Display

Display debuff chance with the character's bonus in parentheses:

```
Ignite: 50% (133%)
       ↑base  ↑with your Debuff Chance stat
```

### 7.9.4 Design Intent

- **Intelligence builds** become control specialists with reliable debuff application
- **Faith builds** resist debuffs, valuable for slow/tanky characters
- High resistance can completely negate debuffs from low-investment attackers

## 7.10 Special Combat Mechanics

### 7.10.1 Stealth Mechanics


| Rule                    | Behavior                                             |
| ----------------------- | ---------------------------------------------------- |
| **What Stealth does**   | Prevents direct targeting of the stealthed character |
| **AoE/group abilities** | Can hit stealthed characters (intentional counter)   |
| **Breaking Stealth**    | Any damage, including DoT ticks and AoE              |


**Design Note:** Avoid creating abilities that apply Stealth via Reaction, to prevent timing edge cases.

## 7.11 Battle Environment Effects

- Environmental conditions affect all characters
- Examples: weather effects, terrain, magical auras
- Can modify resources, damage types, or ability effectiveness
- Special effects for boss encounters
- No positional mechanics required

---

# 8. Game World & Progression

## 8.1 Hub Structure

The game uses a hub-based structure rather than an open world:


| Location                | Function                         | Features                                                  |
| ----------------------- | -------------------------------- | --------------------------------------------------------- |
| **Town Hub**            | Central navigation               | Connect to all other locations                            |
| **Class Trainers** (×3) | Class ability crafting + mastery | Distill, Learn, Hone class abilities; mastery selection |
| **Tutor**               | Neutral ability crafting         | Distill, Learn, Hone neutral abilities                  |
| **Blacksmith**          | Equipment crafting               | Salvage, Forge, Temper using Materials                    |
| **Gambler**             | Random equipment acquisition     | Slot-targeted equipment pulls (gold sink)                 |
| **Oracle**              | Random ability acquisition       | Class-targeted ability pulls (gold sink)                  |
| **Guild Hall**          | Social features                  | Guild management (TBD)                                    |
| **Tavern**              | Social hub                       | Chat systems (TBD)                                        |
| **Battle Selection**    | Content access                   | PvE and PvP selection                                     |


Players navigate these areas through UI transitions without character movement.

**Crafting NPC summary:**

- **Blacksmith:** Equipment economy — Salvage/Forge/Temper using Materials
- **Class Trainers + Tutor:** Ability economy — Distill/Learn/Hone using Essence
- **Distilling** can be performed at any Trainer or Tutor regardless of the ability's class

## 8.2 Campaign Mode

The PvE campaign provides structured progression:

- **Map-based UI** showing available battles
- **Sequential difficulty** progression
- **Zone system** with increasing challenge
- **Boss encounters** at zone conclusions
- **Visual transitions** between zones
- **Special rewards** from boss encounters
- **Equipment exclusivity** for certain bosses

## 8.3 PvE Content

### 8.3.1 Campaign

- Sequential battle instances
- Increasing difficulty curve
- Boss encounters with special mechanics
- Zone-based progression

### 8.3.2 Quest System (TBD)

Quests are the primary source of ability acquisition (abilities do NOT drop from battles).

- **Quest structure:** Targeted NPC kills or specific encounter objectives
- **Tutorial quest chain:** Early progression chain that rewards class-appropriate abilities, designed to teach players different playstyles and ability interactions
- **Ability rewards:** Quests grant specific, predetermined abilities — not random
- **Progression gating:** Later quests may require higher character level or mastery selection
- **Repeatable quests (TBD):** May include repeatable quests that reward duplicate copies for Honing

### 8.3.3 Dungeons (TBD)

- Endurance-based PvE mode
- Continuous battles without resource reset
- Escalating difficulty and rewards
- Resource management challenge

## 8.4 PvP Content

### 8.4.1 Casual PvP

- Unranked matchmaking
- Level-range restrictions
- Minimal rewards
- Build testing environment

### 8.4.2 Ranked PvP

- Competitive matchmaking
- Available at max level (50)
- Season-based ranking
- MMR matching system
- Exclusive ranked rewards

### 8.4.3 Tournaments (Post-Launch)

- Scheduled competitive events
- Special rule sets
- Prestigious rewards
- Community spotlight

---

# 9. User Interface

## 9.1 Battle HUD

### 9.1.1 Character Information

- Character portraits
- Resource bars (Health, Mana, Stamina, Resolve)
- Shield amount displayed on HP bar (combined from all Shield Blessings)
- Blessing row, Passive row (glowing, no timer), and Curse/Ailment row with duration icons
- Active turn indicator

### 9.1.2 Initiative Bar

- Visual representation of all characters' initiative
- Color-coded player/enemy markers
- 100+ initiative indicator
- Initiative reset feedback

### 9.1.3 Ability Selection

- Grid layout of available abilities
- Cooldown and resource cost indicators
- Availability highlighting
- **Conditional border glow:** Abilities with the CONDITIONAL tag display a glowing border when their condition is met, independent of ability readiness (see Section 4.5.7)
- Hover tooltips with:
  - Accuracy display: "Accuracy: 100% (150%)"
  - Debuff chance display: "Ignite: 50% (133%)"
  - Crit chance display: "Crit: 10% (25%)"
  - Conditional status: condition met (✓) or unmet (✗) with reason

### 9.1.4 Battle Log

- Recent action text feed
- Damage, healing, status effect information
- Turn order changes

## 9.2 Character Management

### 9.2.1 Character Sheet

- Character model visualization
- Attribute displays using Base (Total) format (see Section 9.4.1)
- Derived stat displays with hover breakdowns
- Experience/level information
- Class/subclass details
- Unspent points indicator

### 9.2.2 Loadout Management

- Loadout selection/creation
- 2×5 Core ability grid with level display
- 2 Ultimate slots
- Skill point allocation interface
- Equipment preview

### 9.2.3 Equipment Management

Three-column layout: Active slots (left), Character model (center), Passive slots (right).

**Active Slots (Left Column — Orange Border)**


| Position      | Slot                    | Notes                                                |
| ------------- | ----------------------- | ---------------------------------------------------- |
| Top           | Weapon Set tabs (1 / 2) | Switches Main Hand + Off Hand between sets           |
| Below tabs    | Main Hand               | Changes with active set tab                          |
| Below MH      | Off Hand                | Changes with active set tab; disabled for 2H weapons |
| Separated     | Trinket                 | Independent of weapon sets                           |
| Below Trinket | Consumable 1            | Independent of weapon sets                           |
| Below C1      | Consumable 2            | Independent of weapon sets                           |


**Passive Slots (Right Column — Blue Border)**


| Position     | Slot   | Group   |
| ------------ | ------ | ------- |
| Top          | Amulet | Jewelry |
| Below Amulet | Ring   | Jewelry |
| Separated    | Helmet | Armor   |
| Below Helmet | Body   | Armor   |
| Below Body   | Boots  | Armor   |


**UI Behavior:**

- Active slots = orange border, Passive slots = blue border
- Weapon Set tabs only affect Main Hand and Off Hand — all other slots persist across sets
- Character model (center) updates to reflect the selected set's equipment
- Switching tabs previews the inactive set without swapping in battle
- Comparison tooltips show stat differences when hovering replacement items
- Drag-and-drop equipping supported

## 9.3 Hub Interface

### 9.3.1 Town Navigation

- Visual location representations
- One-click navigation
- Available activity indicators

### 9.3.2 NPC Interaction

- Dialog interfaces
- Service menus
- Quest information

### 9.3.3 Battle Selection

- Campaign map visualization
- PvP queue interface
- Match history display
- **Loadout selection** before entering battle

## 9.4 UI Conventions

### 9.4.1 Value Display Format

All modified values throughout the UI follow a consistent display pattern.

**At a Glance: Base (Total)**

```
STR: 80 (100)
     ↑base  ↑total with all modifiers

Damage: 14-18 (22-28)

Crit: 10% (25%)
```

- **Base** is the unmodified value (level-up points for attributes, ability base for damage/crit/accuracy)
- **Total** is the effective value after all modifiers (equipment, buffs, scaling)
- When Total equals Base, only the base value is shown (no parentheses)
- Total is color-coded: **green** when higher than base, **red** when lower (e.g., during a debuff)

**On Hover/Tap: Full Breakdown**

Hovering (or tapping on mobile) any modified value reveals the source breakdown:

```
STR: 80 (100)
  Base:            80
  Emerald Amulet: +15
  Warrior Buff:    +5
  Total:          100
```

**Universal Application:**

- Character sheet attributes (Base Attribute vs Total with equipment/buffs)
- Stat panel (HP, Speed, Mana, Power, etc.)
- Ability tooltips (damage, crit chance, accuracy, debuff chance)
- Equipment comparison tooltips
- Combat HUD (resource bars, buff/debuff effects on stats)

---

# 10. Social Features

## 10.1 Guild System (TBD)

### 10.1.1 Guild Creation and Management

- Name and insignia customization
- Member roles and permissions
- Guild treasury
- Progression system

### 10.1.2 Guild Benefits

- Shared member bonuses
- Guild-exclusive activities
- Future expansion potential

## 10.2 Tavern Chat System

The tavern serves as the game's social hub:

- Chat rooms with character visualization
- Automatic character placement in scene
- Channel system (General, Battle Requests)
- Direct messaging
- Emote system

## 10.3 Friends List

- Add/remove friend functionality
- Online status indicators
- Direct message access
- Recent players tracking
- PvP match invitations

---

# 11. Economy

## 11.1 Currency System

### 11.1.1 Gold

- Primary in-game currency
- Earned primarily from battle victories
- Small amount from PvP losses
- Used for pulls, crafting services, and other purchases
- Major sinks: Gambler (equipment pulls), Oracle (ability pulls), Blacksmith/Trainer services

### 11.1.2 Materials (Equipment Currency)

- **Universal** crafting currency for all equipment operations
- Obtained by **Salvaging** equipment at the Blacksmith
- Used for **Forging** specific equipment at the Blacksmith
- Salvage values scale with rarity: 1 / 3 / 9 / 27 / 81 (see Section 6.7.1)

### 11.1.3 Essence (Ability Currency)

- **Universal** crafting currency for all ability operations
- Obtained by **Distilling** abilities at any Class Trainer or Tutor
- Used for **Learning** specific abilities at the matching Class Trainer or Tutor
- Salvage values scale with rarity: 1 / 3 / 9 / 27 / 81 (same ratios as Materials)

**Learn costs** (create a specific ability at its base Rank):


| Rarity            | Learn Cost  |
| ----------------- | ----------- |
| Common (★)        | 3 Essence   |
| Uncommon (★★)     | 9 Essence   |
| Rare (★★★)        | 27 Essence  |
| Epic (★★★★)       | 81 Essence  |
| Legendary (★★★★★) | 243 Essence |


## 11.2 NPCs and Acquisition


| NPC                     | Random Pulls               | Crafting                                 | Other             |
| ----------------------- | -------------------------- | ---------------------------------------- | ----------------- |
| **Gambler**             | Equipment (slot-targeted)  | —                                        | Gold sink         |
| **Oracle**              | Abilities (class-targeted) | —                                        | Gold sink         |
| **Blacksmith**          | —                          | Salvage, Forge, Temper (Materials)       | —                 |
| **Class Trainers** (×3) | —                          | Distill, Learn, Hone (class abilities) | Mastery selection |
| **Tutor**               | —                          | Distill, Learn, Hone (neutral abilities) | —               |


### 11.2.1 Gambler — Equipment Pull System

The Gambler offers **slot-targeted random pulls** for equipment:

**How It Works:**

1. Player pays gold and selects an **equipment slot** (e.g., Main Hand, Body, Ring)
2. System rolls for **rarity** using the rates below
3. Player receives a **random equipment piece** of that rarity from the chosen slot

One-handed weapons may appear in both Main Hand and Off Hand pools — this is intentional, as they can equip to either slot.

**Rarity Drop Rates (shared across all pull systems):**


| Rarity    | Drop Rate | Avg Pulls |
| --------- | --------- | --------- |
| Common    | 55%       | ~2        |
| Uncommon  | 25%       | 4         |
| Rare      | 15%       | ~7        |
| Epic      | 4%        | 25        |
| Legendary | 1%        | 100       |


**Design Notes:**

- Common/Uncommon surplus feeds the Salvage → Materials economy
- Slot targeting prevents frustration from unwanted slot drops
- Gold cost scales with slot (weapons cost more than rings, etc.)

### 11.2.2 Oracle — Ability Pull System

The Oracle offers **class-targeted random pulls** for abilities:

**How It Works:**

1. Player pays gold and selects a **class source** (Warrior, Mage, Rogue, or Neutral)
2. System rolls for **rarity** using the same rates as the Gambler
3. Player receives a **random ability** of that rarity from the chosen class pool

Each ability has a **fixed rarity** — the rarity roll determines which rarity pool the ability is drawn from. If all abilities of the rolled rarity are already owned, the player receives a duplicate (useful for Honing).

**Pool Sizes:** Each class has ~20 Core + ~10 Ultimate abilities. Neutral has ~20 Core + ~10 Ultimate. Pool sizes per rarity within a class vary based on design (more Common abilities, fewer Legendary).

**Design Notes:**

- Class targeting ensures players can focus their pulls toward their build
- Smaller pools per rarity (compared to equipment) mean abilities are generally easier to complete
- Excess duplicates feed the Distill → Essence economy

### 11.2.3 Ability Crafting System (Class Trainers & Tutor)

Class Trainers handle their class's abilities; the Tutor handles neutral abilities. All share the same three services:

**Distill** — Break down an ability into Essence:


| Rarity    | Distill Value |
| --------- | ------------- |
| Common    | 1 Essence     |
| Uncommon  | 3 Essence     |
| Rare      | 9 Essence     |
| Epic      | 27 Essence    |
| Legendary | 81 Essence    |


Distilling can be performed at **any** Trainer or Tutor regardless of the ability's class.

**Learn** — Spend Essence to create a specific ability at its base Rank:

- Player chooses the exact ability they want
- Cost follows the Learn cost table (3 / 9 / 27 / 81 / 243 Essence)
- Class abilities can only be Learned at the matching Class Trainer
- Neutral abilities can only be Learned at the Tutor

**Hone** — Feed duplicate copies of the same ability to increase its Rank:


| Upgrade      | Copies Required |
| ------------ | --------------- |
| ★ → ★★       | 2 copies        |
| ★★ → ★★★     | 3 copies        |
| ★★★ → ★★★★   | 4 copies        |
| ★★★★ → ★★★★★ | 5 copies        |


Copies are consumed at any Rank (additive). This follows the same ladder as equipment Tempering. Duplicate copies can be found through Oracle pulls, quest rewards, or Learned from Essence.

### 11.2.4 Acquisition Methods Summary


| Source           | Equipment                         | Abilities                             |
| ---------------- | --------------------------------- | ------------------------------------- |
| **Random Pulls** | Gambler (slot-targeted)           | Oracle (class-targeted)               |
| **PvE Battles**  | Primary drop source               | —                                     |
| **PvP Battles**  | Rare random drops                 | —                                     |
| **Quests (TBD)** | —                                 | Targeted rewards (specific abilities) |
| **Crafting**     | Forge from Materials (Blacksmith) | Learn from Essence (Trainer/Tutor)    |


## 11.3 Economic Loops

### 11.3.1 Equipment Loop

1. Battle → earn gold and equipment drops
2. Salvage unwanted equipment → Materials
3. Forge specific equipment from Materials / Temper with copies → improve gear
4. Use improved equipment → tackle harder content
5. Spend gold at Gambler for slot-targeted pulls

### 11.3.2 Ability Loop

1. Earn gold from battles → spend at Oracle for class-targeted pulls
2. Complete quests → receive targeted ability rewards
3. Distill unwanted abilities → Essence
4. Learn specific abilities from Essence / Hone with copies → improve abilities
5. Use improved abilities → tackle harder content

### 11.3.3 Progression Loop

1. Battle → experience and levels
2. Allocate attribute and Skill Points
3. Collect new abilities and equipment
4. Unlock masteries at Class Trainers
5. Access more difficult content

### 11.3.4 Long-term Loop

1. Build specialized characters across multiple classes
2. Collect and max rare equipment and abilities
3. Perfect different builds and strategies
4. Compete in high-level PvP and endgame PvE

---

# 12. Monetization Strategy

## 12.1 Free-to-Play Model

Project Phoenix follows a free-to-play model focused on convenience:

- No paywalls for content
- No exclusive power through payment
- Focus on time-saving features
- Cosmetic options

## 12.2 Convenience Features


| Feature                  | Description                          | Benefit               |
| ------------------------ | ------------------------------------ | --------------------- |
| **Character Slots**      | Additional character slots           | More build variety    |
| **Loadout Slots**        | Extra saved loadouts                 | Quick build switching |
| **Respec Options**       | Reset attribute/skill/mastery points | Build flexibility     |
| **Progression Boosters** | Increased gold/XP gain               | Faster advancement    |


## 12.3 Cosmetic Options (TBD)

- Character appearances
- Equipment visuals
- Battle effects
- UI themes

## 12.4 Premium Currency

- Clear exchange rates
- No loot boxes or gambling
- Direct purchase of desired features
- Free currency through regular play

---

# 13. Art and Audio

## 13.1 Art Style Description (TBD)

## 13.2 Character Designs (TBD)

## 13.3 Equipment Visuals (TBD)

## 13.4 User Interface Design (TBD)

## 13.5 Sound Design (TBD)

## 13.6 Music Themes (TBD)

---

# 14. Appendices

## 14.1 Glossary of Terms


| Term              | Definition                                                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Ability Rank      | Star level (★ to ★★★★★) of an ability item; scales base values independently of Ability Level                               |
| Ability Type      | BASIC, CORE, ULTIMATE, or ITEM                                                                                              |
| Active Equipment  | Equipment that grants abilities (Weapons, Shields, Focuses, Trinkets, Consumables)                                          |
| Ailment           | Damage-over-time effect (Poison, Bleed, Ignite)                                                                             |
| Armor             | Flat reduction to physical damage; from equipment only                                                                      |
| Base Attribute    | Attribute value from level-up allocation only; used for equipment/ability requirements                                      |
| Base Stats        | Power numbers that scale with Rank (equipment and abilities)                                                                |
| Battle Phase      | One of six turn steps; identifiers: `INITIATIVE`, `START_OF_TURN`, `ACTION_SELECTION`, `REACTION_SELECTION`, `EXECUTION`, `END_OF_TURN` — see Section 7.3 |
| Basic Ability     | Ability granted by Active equipment or innate (Punch, Jab, Rest)                                                            |
| Blessing          | Temporary positive effect from an ability; removable                                                                        |
| Bonus Action      | Quick action, cannot be reacted to, resets at turn start                                                                    |
| Class Trainer     | NPC (one per class) for class-specific ability crafting (Distill, Learn, Hone) and mastery selection                      |
| Conditional       | Tag identifying an ability that requires a game-state condition to activate                                                 |
| Core Ability      | Main collectible ability; has Rarity and Rank; levelable via loadout Skill Points                                           |
| Curse             | Temporary negative non-damage effect from an ability; removable by Immune                                                   |
| Defenses          | Armor, Magic Resistance, and Shield collectively                                                                            |
| Discipline        | Thematic school grouping abilities (Combat, Agility, Sorcery, Divine); used for effect targeting                            |
| Distill           | Trainer/Tutor: break down an ability into Essence                                                                           |
| Empower           | Core ability tagged EMPOWER that augments a Basic ability                                                                   |
| Essence           | Universal ability crafting currency from Distilling; used for Learning abilities                                            |
| Fixed Properties  | Equipment properties that never scale (slot, tags, two-handed, requirements)                                                |
| Focus             | INT-based off-hand equipment (Grimoire, Tome); caster fantasy                                                               |
| Force (naming)    | Naming convention for Mage physical damage abilities (e.g., Force Strike)                                                   |
| Forge             | Blacksmith: spend Materials to create specific equipment                                                                    |
| Gambler           | NPC for random equipment pulls (slot-targeted, gold sink)                                                                   |
| Hard Reset        | Initiative resets to 0 on turn start (excess lost); ensures turn character always resolves last in execution                |
| Heavy (naming)    | Naming convention for 2H weapon abilities (e.g., Heavy Slash, Heavy Bash)                                                   |
| Initiative        | Resource accumulated proportional to Speed; at ≥100, character takes a turn (CTB model). Hard resets to 0 after turn        |
| Jab               | Innate Basic ability; unarmed off-hand attack                                                                               |
| Learn             | Trainer/Tutor: spend Essence to create a specific ability                                                                   |
| Loadout           | Complete character build (attributes, equipment, abilities)                                                                 |
| Hone              | Trainer/Tutor: feed duplicate ability copies to increase Rank                                                               |
| Materials         | Universal equipment crafting currency from Salvaging; used for Forging equipment                                            |
| Mods              | Predefined effects on equipment; never scale with Rank                                                                      |
| Normal Action     | Main turn action, triggers Reaction Phase                                                                                   |
| Oracle            | NPC for random ability pulls (class-targeted, gold sink)                                                                    |
| Passive (buff)    | Permanent positive effect from an ability; can be suppressed, never removed                                                 |
| Passive Equipment | Equipment that provides stats only (Body, Helmet, Boots, Ring, Amulet)                                                      |
| Power             | Scaling stat (Combat, Agility, Sorcery, Divine); 1:1 from attributes                                                        |
| Punch             | Innate Basic ability; unarmed main-hand attack                                                                              |
| Rank              | Star level (★ to ★★★★★); scales Base Stats for both equipment and abilities                                                 |
| Rarity            | Item tier (Common→Legendary); determines base Rank, mods, and level requirements                                            |
| Reaction          | Ability used by non-turn characters in response to the turn character's Normal Action                                       |
| Reactor           | Any non-turn character during the Reaction and Execution phases                                                             |
| Resolve           | Resource for Ultimates; generated from combat damage                                                                        |
| Rest              | Innate Basic ability; restores stamina, always available                                                                    |
| Salvage           | Blacksmith: break down equipment into Materials                                                                             |
| Shield            | Blessing providing temporary HP (FIFO depletion); displayed on HP bar                                                       |
| Skill Points      | Resource spent in loadout to level Core ability slots (1-10)                                                                |
| Suppression       | Temporarily disabling a Passive without removing it; sources include cooldown, Corrupted, and depletion (see Section 4.5.6) |
| Temper            | Blacksmith: feed duplicate equipment copies to increase Rank                                                                |
| Trigger           | Tag identifying an ability with effects that fire automatically when a condition is met                                     |
| Trinket           | Active equipment slot; grants a reusable activatable ability                                                                |
| True Damage       | Bypasses all Defenses                                                                                                       |
| Tutor             | NPC for neutral ability crafting (Distill, Learn, Hone)                                                                   |
| Type (Equipment)  | Foundation defining stats, properties, requirements, ability                                                                |
| Ultimate Ability  | Class-specific collectible; costs Resolve, cannot be leveled but can be Honed (ranked up)                                |
| Vanilla           | Equipment with no mods; highest base stats for type                                                                         |
| Weapon Set        | Paired Main Hand + Off Hand equipment; two sets per character                                                               |
| Weapon Swap       | Bonus action to switch active Weapon Set; 2-turn cooldown                                                                   |


## 14.2 Prototype Scope Notes

The following features are designated for the full game and NOT included in prototype:

- Focus equipment ability balancing (Hex, Mend values TBD)
- Guild System
- Dungeons mode
- Tournaments
- Cosmetic options
- Art and Audio systems
- Equipment rarity system (beyond Common)
- Rank/Tempering/Honing systems
- Salvage/Forge/Distill/Learn economy
- Gambler and Oracle pull systems
- Ability Rarity and Rank progression

The prototype focuses on:

- Core turn loop: Initiative → Action → Reaction → Execution → End
- 1v1 battles (2v2 is a stretch goal)
- Basic Common equipment with implicit modifiers only
- Abilities at fixed Rank ★ without Honing

