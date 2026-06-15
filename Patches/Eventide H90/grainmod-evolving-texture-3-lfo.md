---
type: patch
title: "GrainMod — Evolving Grain Texture (3 LFOs)"
device: Eventide H90
date: 2026-06-15
description: "A granular texture machine whose three independent LFOs constantly reshape the grains so the sound evolves rather than repeats — an ever-shifting drone bed under a held note, ideal as the static-pad source feeding a reverb in the other slot. The 3-LFO targets and 'evolves rather than repeats' behavior are published (Production Expert + granular firmware notes); no parameter values are published, so this is a dialable recipe."
tags: [grainmod, granular, drone, ambient, texture, lfo, evolving, degraded]
dips:
  LFO RATES: "set the three LFOs to different, non-synced rates so cycles never line up"
  FILTER LFO: "modulate Filter slowly for a breathing tone"
controls:
  - { name: "Preset A Algorithm", type: switch, value: "GrainMod (granular)" }
  - { name: "LFO 1 Target", type: switch, value: "Trigger Rate (published target — no published value)" }
  - { name: "LFO 2 Target", type: switch, value: "Grain Duration (published target — no published value)" }
  - { name: "LFO 3 Target", type: switch, value: "Filter (published target — no published value)" }
  - { name: "LFO 1 Rate", type: knob, value: "non-synced, distinct from LFO 2/3 so cycles don't line up (recipe — no published value)" }
  - { name: "LFO 2 Rate", type: knob, value: "non-synced, distinct from LFO 1/3 (recipe — no published value)" }
  - { name: "LFO 3 Rate", type: knob, value: "slow, for a breathing filter tone (recipe — no published value)" }
  - { name: "Preset B Algorithm", type: switch, value: "long reverb for depth (recipe — no published value)" }
  - { name: "Firmware", type: switch, value: "post-v1.1.4 (granular algorithms postdate the bundled PDF — keep H90 Control updated)" }
---

# GrainMod — Evolving Grain Texture (3 LFOs)

## Concept
A granular texture machine whose three independent LFOs constantly reshape the grains so the sound evolves rather than repeats. LFO 1 targets Trigger Rate, LFO 2 targets Grain Duration, and LFO 3 targets Filter; with the three rates set differently the cycles never line up, producing an ever-shifting drone bed under a held note. It works best as the static-pad source feeding a reverb in the other slot — hold a chord and let the grains breathe and mutate underneath.

## How to play it
1. Update firmware via H90 Control; load **GrainMod** on Preset A.
2. Assign **LFO 1 -> Trigger Rate**, **LFO 2 -> Grain Duration**, **LFO 3 -> Filter**.
3. Set the three **LFO rates** to slightly different, non-synced values so the cycles don't line up.
4. Modulate **Filter** slowly with LFO 3 for a breathing tone.
5. Hold a chord or note and let the grains evolve underneath.
6. Add a long **reverb** on Preset B for depth.

## Notes
- No published exact knob values for this recipe — treat the control values above as a dialable starting point, not sourced settings. What IS sourced: the 3-LFO targets (Trigger Rate / Grain Duration / Filter) and the "evolves rather than repeats" behavior are published; dial the rest from the recipe or dissect a GrainMod community program.
- Granular algorithms postdate the bundled v1.1.4 PDF — keep firmware current via H90 Control.
- GrainMod offers fewer assignable performance controls than other granular algos, so most of the motion comes from the three LFOs rather than expression/footswitch mapping.

## Sources
- https://www.production-expert.com/production-expert-1/eventide-h90-multi-fx-pedal-new-granular-algorithms-explored (GrainMod: three LFOs target Trigger Rate, Grain Duration, Filter; evolving textures)
- research/links/eventide-h90-granular-firmware-update.md (GrainMod)
- research/links/patchstorage-ambient-drone-granular-programs.md (GrainMod — 3 LFOs)
- Provenance: Production Expert review + granular firmware notes — concept/LFO targets published, no values
