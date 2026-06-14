---
type: patch
title: wonky_bass — tilt-modulated sub bass
device: TE OP-1 Field
date: 2026-06-14
description: A modulated / tilt-controlled sub bass — the element LFO (accelerometer / G-sensor) wobbles the filter live as you tilt the unit.
tags: [bass, sub, modulated, g-sensor, iter, community, signature]
controls:
  - { name: "Engine", type: switch, value: "iter", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Octave", type: knob, value: "-2" }
  - { name: "FX", type: switch, value: "filter" }
  - { name: "LFO", type: switch, value: "element (G-sensor / tilt source)", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Slot/Bank", type: knob, value: "iter slot [1]" }
---

# wonky_bass — tilt-modulated sub bass

## Concept

A modulated / tilt-controlled sub bass with accelerometer wobble. The element LFO is the OP-1's accelerometer — tilt the unit and the filter wobbles live. iter engine at −2 with a filter FX, modulated by physical tilt.

## How to play it

1. Load wonky_bass (iter, Octave −2, filter FX, element LFO).
2. Play bass lines.
3. **Tilt the unit** to wobble the filter live — the element LFO is the G-sensor.

## Notes

- Element LFO = the accelerometer (see the G-sensor tip — FM radio / element-LFO use).
- Per-knob arrays not exposed by op1.fun — `op1-dump` the `.aif` for exact numbers.

## Sources

- Gear/TE OP-1 Field/research/links/op1fun-bass-baritone-patches.md (wavi "wonky_bass" via "Bass Sounds" pack)
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
