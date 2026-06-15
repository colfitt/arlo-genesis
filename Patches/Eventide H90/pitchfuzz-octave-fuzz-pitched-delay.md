---
type: patch
title: "PitchFuzz — Octave Fuzz + Pitched Delay"
device: Eventide H90
date: 2026-06-15
description: "Fuzz with up to three pitch-shifted voices and two delays in one algorithm — stack an octave (or 5th) on top of a thick fuzz with rhythmic pitched echoes for huge synth-like lead textures. On-aesthetic for the degraded lead role. The Fuzz 0-50/51-100 split, 0-3 pitch voices at +/-2 octaves, and Group/Arpeggiated delay routing are from the Eventide manual; the harmonics-plus-saturation pairing is recommended in an Eventide harmonics forum thread. Exact factory values aren't published — dial from the recipe."
tags: [pitchfuzz, distortion, fuzz, octave, pitch, delay, lead]
dips:
  ARPEGGIATED: "switch the two delays to Arpeggiated routing to turn the pitched voices into cascading patterns instead of a stacked pad"
  ENVELOPE: "envelope sensitivity can gate the pitched voices by pick attack — dig in to bring the harmonies up"
controls:
  - { name: "Preset Algorithm", type: switch, value: "PitchFuzz" }
  - { name: "Fuzz", type: knob, value: "~55-70 for fuzz character (range: 0-50 = distortion / 51-100 = full fuzz)" }
  - { name: "Pitch Amount", type: knob, value: "1-2 voices (range: 0-3 pitched voices)" }
  - { name: "Pitch A", type: knob, value: "+12 (octave) (range: +/-2 octaves)" }
  - { name: "Pitch B", type: knob, value: "+7 (5th) optional (range: +/-2 octaves)" }
  - { name: "Pitch C", type: knob, value: "off / third voice as desired (range: +/-2 octaves)" }
  - { name: "Delay Routing", type: switch, value: "Group (stacked pad) or Arpeggiated (cascades)", options: ["Group", "Arpeggiated"] }
  - { name: "Delay 1 / Delay 2", type: knob, value: "dial for rhythmic pitched echoes" }
---

# PitchFuzz — Octave Fuzz + Pitched Delay

## Concept
Fuzz with up to three pitch-shifted voices and two delays in a single algorithm. Stack an octave (and/or a 5th) on top of a thick fuzz, then send the pitched voices through the two delays for rhythmic pitched echoes — huge synth-like lead textures from one preset. On-aesthetic for the degraded lead role: bring the Fuzz into its upper half for full fuzz, add one or two pitch voices, and choose Group routing for a stacked pad or Arpeggiated routing for cascading patterns.

## How to play it
1. Load PitchFuzz; set Fuzz around 55-70 for fuzz character.
2. Set Pitch Amount to 1-2 voices; Pitch A +12 (octave), and/or Pitch B +7 (5th).
3. Choose Group routing for a stacked pad or Arpeggiated for cascades.
4. Dial the two delays for rhythmic pitched echoes.

## Notes
- No published exact knob values for this recipe — treat the control values above as a dialable starting point, not sourced settings. What IS sourced: the Fuzz 0-50 (distortion) / 51-100 (full fuzz) split, 0-3 pitch voices, the +/-2 octave per-voice range, and the Group/Arpeggiated delay routing are all from the Eventide manual.
- Recommended in the Eventide harmonics forum thread for blending added harmonics with saturation plus delay.
- Distinct from the existing shimmer-pad-wash-blackhole-pitchfuzz (that one is a reverb-wall pairing) — this is the standalone fuzz + pitch + delay lead.

## Sources
- https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/algorithms/distortion.html (PitchFuzz: Fuzz 0-50 dist / 51-100 fuzz, 0-3 pitch voices +/-2 oct, Group/Arpeggiated delays)
- https://www.eventideaudio.com/forums/topic/best-h90-harmonics-generating-algorithms-settings/ (PitchFuzz blends harmonics with saturation + delay) *(community)*
- provenance: manufacturer manual + Eventide harmonics forum — ranges published, factory values dialable
