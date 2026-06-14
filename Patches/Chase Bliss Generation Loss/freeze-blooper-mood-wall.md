---
type: patch
title: Freeze → Blooper/MOOD Wall
device: Chase Bliss Generation Loss
date: 2026-06-14
description: Building a layered drone wall — freeze a degraded Gen Loss tone, capture it into Blooper / micro-loop it in MOOD, then play more on top. The "engaged for a moment, captured forever" texture move.
tags: [freeze, drone, wall, rig-integration, designed, signature]
dips:
  CLASSIC: on
  DROP BYP: on
  SNAG BYP: on
hidden:
  Aux Onset (Wow knob): sets how fast it grabs
controls:
  - { name: "Aux", type: switch, value: "Fail (left footswitch fires Freeze)", options: ["Stop", "Filter", "Fail"] }
  - { name: "Failure", type: knob, value: "modest (so the captured loop isn't pure chaos)" }
  - { name: "Model", type: knob, value: "heavy base first (e.g. #3 Dying Cassette or #5 Baritone Drone)" }
---

# Freeze → Blooper/MOOD Wall

## Concept
Build a layered drone wall: freeze a degraded Gen Loss tone, capture it into Blooper / micro-loop it in MOOD, then play more on top. The "engaged for a moment, captured forever" texture move. This is the rig version of how Stringer/Othling deploy it — a degraded texture feeding loop/granular.

## How to play it
1. Set up the **Hidden FREEZE** patch (#15): Aux=Fail, CLASSIC + DROP BYP + SNAG BYP dips on.
2. Choose a heavy base first — e.g. "Dying Cassette" (#3) or "Baritone Drone" (#5).
3. Keep **Failure modest** so the captured loop isn't pure chaos.
4. Freeze it → the downstream Blooper records the held tape voice as a loop layer; MOOD micro-loops it. Play more on top.

## Notes
- 🟣 designed — combines the verified Freeze recipe with the dossier's stated Blooper/MOOD pairing (Gen Loss = the ideal *source* for those loops).
- Pair with a Blooper/MOOD scene via the cb-stack PC recall.

## Sources
- 🟣 designed from `research/links/genloss-aux-freeze-classic-trick.md` + DeepResearch §9 (Blooper/MOOD pairings) + `research/links/spiritbox-mike-stringer-rig-rundown.md`.
- Transformed from Pedalxly Generation-Loss-Patches.md (designed).
