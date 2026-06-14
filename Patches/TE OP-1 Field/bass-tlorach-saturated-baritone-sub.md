---
type: patch
title: Bass (tlorach) — saturated baritone sub
device: TE OP-1 Field
date: 2026-06-14
description: Thick saturated sub / baritone-weight bass — supersaw Cluster dropped two octaves + distortion; the closest single patch to "baritone weight + saturated drone."
tags: [bass, sub, baritone, doom, saturated, cluster, community, signature]
controls:
  - { name: "Engine", type: switch, value: "Cluster", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Octave", type: knob, value: "-2" }
  - { name: "FX", type: switch, value: "nitro (on)" }
  - { name: "LFO", type: switch, value: "none", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Slot/Bank", type: knob, value: "Cluster slot [7]" }
---

# Bass (tlorach) — saturated baritone sub

## Concept

Thick saturated sub / baritone-weight bass — the closest single patch to "baritone weight + saturated drone." A supersaw Cluster dropped two octaves with distortion (Nitro). Doubles as a doom bass or a saturated sub-drone.

## How to play it

1. Load Bass (Cluster, Octave −2, Nitro on, no LFO).
2. Play bass lines, or hold a note for a saturated sub-drone.
3. Pair with drone1–3 for a low-end wall.

## Notes

- Per-knob arrays not exposed by op1.fun — `op1-dump` the `.aif` for exact numbers.
- Cluster at −2 + Nitro = the baritone-weight saturated combo.

## Sources

- Gear/TE OP-1 Field/research/links/op1fun-bass-baritone-patches.md (tlorach "Bass" via DominusRegnavit "Bass Sounds" pack)
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
