---
type: patch
title: Detuned Synth-Pad Layer (Micropitch -> Synthonizer)
device: Eventide H90
date: 2026-06-14
description: A detuned saw synth-pad layer to sit under the baritone drone — Micropitch +/-9c into a saw Synthonizer, keeping the dry banjo on top.
tags: [pitch, synth-pad, detune, drone, baritone, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "26" }
  - { name: "Routing", type: switch, value: "Series", options: ["Series", "Parallel", "Insert"] }
  - { name: "Preset A Algorithm", type: switch, value: "Micropitch" }
  - { name: "Detune Left", type: knob, value: "-9 cents" }
  - { name: "Detune Right", type: knob, value: "+9 cents" }
  - { name: "Delay Spread", type: knob, value: "25 ms" }
  - { name: "Mix (A)", type: knob, value: "50%" }
  - { name: "Preset B Algorithm", type: switch, value: "Synthonizer" }
  - { name: "Voice 1 (B)", type: switch, value: "Saw" }
  - { name: "Glide (B)", type: switch, value: "Medium" }
  - { name: "Env Mod (B)", type: knob, value: "35%" }
  - { name: "Mix (B)", type: knob, value: "60%" }
---

# Detuned Synth-Pad Layer (Micropitch -> Synthonizer)

## Concept
A detuned saw synth-pad layer to sit under the baritone drone. Micropitch (+/-9 cents, 25 ms spread) widens and thickens, feeding a saw Synthonizer that turns the input into a synth bed. Keep the dry banjo on top.

## How to play it
1. Set Routing to Series.
2. Engage Micropitch on A (Detune Left -9c, Detune Right +9c, Delay Spread 25 ms, Mix 50%).
3. Engage Synthonizer on B (Voice 1 = Saw, Glide Medium, Env Mod 35%, Mix 60%).
4. Keep the dry banjo riding on top of the synth bed.

## Notes
- Community (Guitar Chalk H90 settings, recipe 4).
- Micropitch +/-9c into a saw Synthonizer = a synth bed.

## Sources
- research/links/guitarchalk-h90-dual-algorithm-recipes.md (guitarchalk.com/eventide-h90-settings/)
- Transformed from Pedalxly H90-Patches.md (community)
