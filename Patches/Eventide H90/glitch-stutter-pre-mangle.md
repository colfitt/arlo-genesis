---
type: patch
title: Glitch / Stutter Pre-Mangle
device: Eventide H90
date: 2026-06-14
description: Rhythmic "recorded-wrong" destruction of a sustained baritone drone before it hits the reverb — Glitch/Stutter (optionally GrainMod) into a reverb to catch the wreckage.
tags: [glitch, stutter, granular, degraded, recorded-wrong, drone, factory, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "19" }
  - { name: "Routing", type: switch, value: "Series (Glitch/Stutter -> reverb)", options: ["Series", "Parallel", "Insert"] }
  - { name: "Preset A Algorithm", type: switch, value: "Glitch (aliasing, bursts, pitch jumps — 3 glitch types, stackable) or Stutter (tight controlled burst patterns or loosely scattered, precise subdivision)" }
  - { name: "GrainMod (optional)", type: switch, value: "3 independent LFOs on Trigger Rate / Grain Duration / Filter" }
  - { name: "Preset B Algorithm", type: switch, value: "a reverb (catch the wreckage)" }
---

# Glitch / Stutter Pre-Mangle

## Concept
Rhythmic "recorded-wrong" destruction of a sustained baritone drone **before** it hits the reverb. Glitch (aliasing, bursts, pitch jumps — 3 stackable types) or Stutter (tight controlled burst patterns or loosely scattered, precise subdivision) shred the input; an optional GrainMod adds 3 independent LFOs on Trigger Rate / Grain Duration / Filter. A reverb on B catches the wreckage.

## How to play it
1. Set Routing to Series, Glitch/Stutter -> reverb.
2. Engage Glitch or Stutter on A; optionally add GrainMod's LFOs.
3. Feed a sustained baritone drone in; let it be shredded before the reverb catches the wreckage.

## Notes
- Character descriptions only (granular firmware). Factory algorithm.
- GrainMod LFO targets are from the patchstorage-ambient file.

## Sources
- research/links/eventide-h90-granular-firmware-update.md
- Transformed from Pedalxly H90-Patches.md (factory)
