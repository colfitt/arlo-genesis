---
type: patch
title: drone5 — metallic dissonant sub-drone
device: TE OP-1 Field
date: 2026-06-14
description: A harsher, post-punk / Swans-wall sub-drone — the Phase engine at −2 with grid FX gives a dissonant brittle floor.
tags: [drone, dissonant, metallic, post-punk, community, signature]
controls:
  - { name: "Engine", type: switch, value: "Phase", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Octave", type: knob, value: "-2" }
  - { name: "FX", type: switch, value: "grid" }
  - { name: "LFO", type: switch, value: "value (on)", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Slot/Bank", type: knob, value: "Phase slot [1]" }
---

# drone5 — metallic dissonant sub-drone

## Concept

A harsher, post-punk / Swans-wall sub-drone. The Phase engine (metallic / ring-mod-ish character) at −2 plus the grid FX produces a dissonant, brittle floor. Sits under the brittle-texture cluster (Swans / Big Black, No Reply / Joy Division aesthetics).

## How to play it

1. Load Phase at Octave −2, FX grid, value LFO on.
2. Latch a low dissonant interval (a tritone or minor 2nd works) with the **Hold** sequencer.
3. Layer over a cleaner sub-drone for a brittle/warm contrast.

## Notes

- Per-knob arrays not exposed by op1.fun — `op1-dump` the `.aif` for exact numbers.
- Phase is the metallic/ring-mod-flavored engine; grid FX adds the brittle texture.

## Sources

- Gear/TE OP-1 Field/research/links/op1fun-drone-ambient-patches-concrete.md (iFaber via pattisoni "drones" pack)
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
