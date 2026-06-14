---
type: patch
title: Freeze-Mode Drone with Feeding Reverb (wash-on-wash fix #1)
device: Strymon Big Sky
date: 2026-06-14
description: Hold a frozen chord while still getting ambience on the lead played over it — place a separate reverb/delay BEFORE the Big Sky so the dry lead picks up space upstream (Antoine Michaud, "Infinite vs Freeze").
tags: [drone, freeze, technique, placement, banjo-as-lead, community, signature]
hidden:
  HOLD: FREEZE
controls:
  - { name: "Machine", type: switch, value: "any (demoed on CLOUD)", options: ["Cloud","Shimmer","Bloom","Chorale","Swell","Magneto","Nonlinear","Reflections","Room","Hall","Plate","Spring"] }
  - { name: "VALUE", type: button, value: "click → scroll past Boost & Persist → Hold → FREEZE" }
  - { name: "Slot/Bank", type: knob, value: "any FREEZE preset (technique, no own slot)" }
---

# Freeze-Mode Drone with Feeding Reverb (wash-on-wash fix #1)

## Concept
A rig-critical placement recipe rather than a knob patch. FREEZE holds a chord while leaving notes played on top dry, so the held wall doesn't get chaotic the way INFINITE does (INFINITE adds every new note to the wash). To give the lead its own space, put a separate reverb/delay (e.g. the TimeLine) BEFORE the Big Sky — the upstream unit ambiences the lead before it reaches the frozen pedal.

## How to play it
1. Set HOLD = FREEZE via the VALUE knob: click VALUE → scroll past Boost & Persist → Hold → FREEZE.
2. Freeze a chord on the Big Sky (demoed on Cloud) to hold the wall.
3. Play the lead on top — it comes through dry from the Big Sky's perspective.
4. The reverb/delay placed *ahead* of the Big Sky gives that dry lead its ambience.

## Notes
- INFINITE vs FREEZE is the whole point: INFINITE = every new note feeds the wash (chaotic fast); FREEZE = your playing stays dry over the held wall.
- This is the banjo-as-lead-over-a-frozen-bed move — the lead's space comes from upstream, not the Big Sky.
- Behavior/placement recipe — no knob numbers given.

## Sources
- research/transcripts/antoine-michaud-bigsky-infinite-vs-freeze.md (youtube.com/watch?v=GYo2VkFiYYE) — Antoine Michaud, "Infinite vs Freeze"
- Transformed from Pedalxly Big-Sky-Patches.md (community)
