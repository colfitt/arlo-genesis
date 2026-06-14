---
type: patch
title: Expression heel/toe morph — octave-down → unity (Mark Johnston)
device: OBNE Dark Star V3
date: 2026-06-14
description: A musical expression sweep morphing a dark octave-down reverb up to a clean unity pad — far more musical than the footswitch jumps (Mark Johnston / Secret Weapons).
tags: [expression, pitch, morph, octave-down, community, signature, mark-johnston]
hidden:
  Expression target: Pitch + Filter (heel/toe morph)
  Aux mode: temporarily infinite Decay (to find unity pitch while setting)
controls:
  - { name: "Filter", type: knob, value: "HEEL = slight HPF; TOE = warmer/darker LPF" }
  - { name: "Pitch 1", type: knob, value: "HEEL = octave-down reverb; TOE = unity pitch" }
  - { name: "Expression", type: knob, value: "hold On/Off, move knobs heel→toe; untouched knobs unaffected; saved per preset" }
  - { name: "Routing", type: switch, value: "Stereo", options: ["Mono", "Mono-In-Stereo-Out", "Stereo"] }
---

# Expression heel/toe morph — octave-down → unity (Mark Johnston)

## Concept
A musical expression sweep that morphs a dark octave-down reverb up to a clean unity pad — far more musical than the footswitch jumps. HEEL = slight HPF Filter + octave-down reverb; TOE = reverb back at unity pitch + Filter at a warmer/darker LPF.

## How to play it
1. Temporarily assign Aux = infinite Decay to find unity pitch while setting it.
2. Hold On/Off and move the knobs heel→toe to define the morph endpoints.
3. HEEL: slight HPF + octave-down. TOE: unity pitch + warmer/darker LPF.
4. Untouched knobs are unaffected; the assignment saves per preset.

## Notes
- Demonstrated in an FX-loop (studio-post) position on a St. Vincent guitar.
- Directional morph — start/end states described, no clock numbers.

## Sources
- research/transcripts/mark-johnston-secret-weapons-dark-star-stereo.md
- Ref: Mark Johnston / Secret Weapons (demonstrator)
- Transformed from Pedalxly Dark-Star-V3-Patches.md (community)
