---
type: patch
title: drone6 — lush moving Cluster drone
device: TE OP-1 Field
date: 2026-06-14
description: A wide, lush, moving drone at unison octave — Cluster supersaw + grid + tremolo make a breathing wall.
tags: [drone, pad, lush, cluster, community, signature]
controls:
  - { name: "Engine", type: switch, value: "Cluster", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Octave", type: knob, value: "0" }
  - { name: "FX", type: switch, value: "grid" }
  - { name: "LFO", type: switch, value: "tremolo (on)", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Slot/Bank", type: knob, value: "Cluster slot [1]" }
---

# drone6 — lush moving Cluster drone

## Concept

A wide, lush, moving drone at unison octave. Cluster (the JP-8000 supersaw engine) plus grid FX and a tremolo LFO equals a breathing wall — fuller and brighter than the Dr Wave sub-drones. Layer over drone1 for a two-tier drone (sub floor + lush mid wall).

## How to play it

1. Load Cluster at Octave 0, FX grid, tremolo LFO on.
2. Latch a chord or held note with the **Hold** sequencer.
3. Layer it over drone1–3 (Dr Wave −2) for a two-tier sub + wall.

## Notes

- Per-knob arrays not exposed by op1.fun — `op1-dump` the `.aif` for exact numbers.
- Tremolo LFO is what makes it "breathe"; grid FX adds texture/width.

## Sources

- Gear/TE OP-1 Field/research/links/op1fun-drone-ambient-patches-concrete.md (iFaber via pattisoni "drones" pack)
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
