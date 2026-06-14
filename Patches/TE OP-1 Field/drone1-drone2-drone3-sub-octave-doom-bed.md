---
type: patch
title: drone1 / drone2 / drone3 — sub-octave doom bed
device: TE OP-1 Field
date: 2026-06-14
description: The core OP-1 sub-drone — a banjo/baritone drone underlay for doom/drone walls, three near-identical Dr Wave sub-drones forming the spine of iFaber's "drones" pack.
tags: [drone, doom, sub-bass, bed, community, signature]
controls:
  - { name: "Engine", type: switch, value: "Dr Wave", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Octave", type: knob, value: "-2" }
  - { name: "FX", type: switch, value: "none" }
  - { name: "LFO", type: switch, value: "value (on)", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Slot/Bank", type: knob, value: "Dr Wave slots [1]/[2]/[3]" }
---

# drone1 / drone2 / drone3 — sub-octave doom bed

## Concept

The core OP-1 Field sub-drone — a baritone/banjo drone underlay built for doom and drone walls. Three near-identical Dr Wave sub-drones dropped two octaves with the value-LFO on form the spine of iFaber's "drones" pack. Dr Wave at −2 + value LFO is the documented house recipe for an OP-1 sub-drone.

## How to play it

1. Load the Dr Wave engine, drop Octave to −2, FX none, value LFO on.
2. Latch a low note with the **Hold** sequencer.
3. Play the banjo (or a synth lead) as a melodic lead over the held drone.
4. Print to **Porta** tape for wobble/degrade.

## Notes

- Per-knob arrays are not exposed by op1.fun — `op1-dump` the `.aif` for exact numbers. Engine/octave/FX/LFO granularity is honest here.
- Three slots ([1]/[2]/[3]) hold the same recipe with micro-variations; stack two for a thicker floor.
- Pairs with the saturated Cluster sub bass (Bass / tlorach) for a low-end wall.

## Sources

- Gear/TE OP-1 Field/research/links/op1fun-drone-ambient-patches-concrete.md (https://op1.fun/users/pattisoni/packs/drones-2166)
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
