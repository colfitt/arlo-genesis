---
type: patch
title: drone4 — moving sub-drone (echo motion)
device: TE OP-1 Field
date: 2026-06-14
description: The same Dr Wave sub-drone bed with delay movement inside the wall — drift under a static banjo lead.
tags: [drone, doom, sub-bass, delay, community, signature]
controls:
  - { name: "Engine", type: switch, value: "Dr Wave", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Octave", type: knob, value: "-2" }
  - { name: "FX", type: switch, value: "delay" }
  - { name: "LFO", type: switch, value: "value (on)", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Slot/Bank", type: knob, value: "Dr Wave slot [4]" }
---

# drone4 — moving sub-drone (echo motion)

## Concept

The drone1–3 formula with delay added for drift. Same Dr Wave sub-drone bed at −2, but the delay FX gives the wall internal motion so it never sits perfectly still. Good as a moving floor under a static banjo lead.

## How to play it

1. Load Dr Wave at Octave −2, FX delay, value LFO on.
2. Latch a low note via the **Hold** sequencer.
3. Let the delay smear the sub while you play a static lead on top.

## Notes

- Per-knob arrays not exposed by op1.fun — `op1-dump` the `.aif` for exact numbers.
- The −2 floor variant; pair with drone1–3 (no-FX) for a two-layer sub where one moves and one stays still.

## Sources

- Gear/TE OP-1 Field/research/links/op1fun-drone-ambient-patches-concrete.md (iFaber via pattisoni "drones" pack)
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
