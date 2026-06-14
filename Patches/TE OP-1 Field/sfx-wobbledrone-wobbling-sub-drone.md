---
type: patch
title: SFX-Wobbledrone — wobbling sub-drone
device: TE OP-1 Field
date: 2026-06-14
description: A wobbling sub-drone SFX one octave up from the doom floor — the −1 variant of the Dr Wave drone formula.
tags: [drone, sub-bass, sfx, delay, community, signature]
controls:
  - { name: "Engine", type: switch, value: "Dr Wave", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Octave", type: knob, value: "-1" }
  - { name: "FX", type: switch, value: "delay" }
  - { name: "LFO", type: switch, value: "value (on)", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Slot/Bank", type: knob, value: "Dr Wave slot [5]" }
---

# SFX-Wobbledrone — wobbling sub-drone

## Concept

A wobbling sub-drone SFX one octave up from the doom floor — the −1 variant of the Dr Wave drone formula. It sits between the −2 sub floor and the unison pads. A companion patch, "WAV-Droney," is the same thing with FX set to none.

## How to play it

1. Load Dr Wave at Octave −1, FX delay, value LFO on.
2. Latch a note with the **Hold** sequencer for a sustained wobble.
3. Use as a mid-register drone between drone1–3 (−2) and the unison Cluster pads.

## Notes

- Per-knob arrays not exposed by op1.fun — `op1-dump` the `.aif` for exact numbers.
- Companion "WAV-Droney" = identical recipe with FX none, if you want it static.

## Sources

- Gear/TE OP-1 Field/research/links/op1fun-drone-ambient-patches-concrete.md (Onemanbandthing via pattisoni "drones" pack)
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
