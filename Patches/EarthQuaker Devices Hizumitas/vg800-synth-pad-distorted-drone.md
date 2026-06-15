---
type: patch
title: "VG-800 Synth-Pad Distorted Drone — fuzz a synth model"
device: EarthQuaker Devices Hizumitas
date: 2026-06-15
description: "Feeding the VG-800's synth/pad/COSM output into the Hizumitas: continuous-waveform synth patches (pad, organ, GR-style synth) turn into massive distorted drones, good for the rig's drone aesthetic. The Hizumitas tracks the synth as long as it stays a continuous waveform — a patch for unholy textures by fuzzing an already-synthesized signal (inference from circuit behavior, no published Hizumitas+VG-800 docs — dialable recipe)."
tags: [drone, ambient, texture, synth, designed]
controls:
  - { name: "Volume", type: knob, value: "near unity (set by ear, recipe — no published value)" }
  - { name: "Sustain", type: knob, value: "up (sustaining drone bloom — recipe, no published value)" }
  - { name: "Tone", type: knob, value: "to taste (recipe — no published value)" }
---

# VG-800 Synth-Pad Distorted Drone — fuzz a synth model

## Concept
Feeding the VG-800's synth/pad/COSM output into the Hizumitas: continuous-waveform synth patches (pad, organ, GR-style synth) turn into massive distorted drones — good for the rig's drone aesthetic. The Hizumitas tracks the synth as long as it's a continuous waveform. A patch for unholy textures by fuzzing an already-synthesized signal. Dial the Hizumitas as a sustaining drone voice (Sustain up, Tone to taste) and choose a VG-800 synth/pad/organ COSM patch.

## How to play it
1. Set the VG-800 to a synth/pad/organ patch (continuous waveform tracks best).
2. Feed it into the Hizumitas set for a sustaining drone (Sustain up, Tone to taste).
3. Hold notes/chords — the synth becomes a massive distorted drone.
4. Feed long reverb/granular after for the full ambient-drone texture.

## Notes
- **Honesty flag:** there is NO published documentation of the Hizumitas with the VG-800 — this is inference from circuit behavior. All Hizumitas positions are a dialable recipe, not sourced settings.
- Pad/organ/continuous-waveform synth patches track well and turn into massive distorted drones (good); poly guitar-synth patches artifact heavily (see the existing `max-chaos-runaway.md` patch).
- On-aesthetic for the user's drone preference; kept as the stronger of the two VG-800 inference seeds (dropped the modeled-amp variant for the cap).

## Sources
- gear/.../research/Hizumitas-DeepResearch.md §7 — "When the VG-800 outputs synth-modeled signal (pad, organ, GR-style synth) the Hizumitas will track it as long as the synth output is a continuous waveform... pad patches turn into massive distorted drones (good for the user's drone aesthetic)"
- research/Hizumitas-UsageGuide.md §6 — "VG-800 synth/pad patches turn into massive distorted drones (good)"
- Provenance: inference:DeepResearch §7 (no published Hizumitas+VG-800 docs — dialable recipe)
