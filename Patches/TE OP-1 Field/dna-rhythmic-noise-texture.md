---
type: patch
title: "DNA — rhythmic noise texture engine"
device: TE OP-1 Field
date: 2026-06-15
description: "DNA is a rhythmic-noise synthesizer that generates a different beating pattern per voice, so chords produce complex evolving rhythms. Dial it as an evolving rhythmic bed or as raw material for percussion-type sounds. Engine behaviour described from a published OP-1 Field review (magazinmehatronika.com); no per-knob numeric values exist, so this is a dialable recipe."
tags: [texture, dna, rhythmic, noise, percussion, generative, field]
controls:
  - { name: "Engine", type: switch, value: "DNA" }
  - { name: "Low-pass filter", type: knob, value: "to taste (down = darker bed, up = busy wavetable-like texture)" }
  - { name: "Rhythmic-beating amount", type: knob, value: "raise for movement (recipe — no published value)" }
  - { name: "OSC2 detune", type: knob, value: "detune for instability (recipe — no published value)" }
  - { name: "Crunchy-noise control", type: knob, value: "add for grit (recipe — no published value)" }
---

# DNA — rhythmic noise texture engine

## Concept

DNA is a rhythmic-noise synthesizer that generates a different beating pattern per voice, so chords produce complex, evolving rhythms rather than a static tone. Use it as an evolving rhythmic bed under a pad, or as raw material for percussion-type sounds and wavetable-like noise. Raise the beating for movement, add crunchy noise for grit, detune OSC2 for instability, and filter to taste.

## How to play it

1. Select DNA.
2. Increase the rhythmic-beating parameter to generate moving patterns.
3. Add crunchy noise for grit and detune OSC2 for instability.
4. Filter down for a darker bed or up for a busy wavetable-like texture.
5. Layer under a pad or use as a percussion source; hold a chord for poly-rhythm complexity.

## Notes

- DNA generates a different pattern per voice — chords become evolving rhythms, not a single sustained tone.
- Good source for wavetable-like noise and percussion-type hits.
- HONESTY FLAG: dialable recipe, no published numeric values. The engine description (rhythmic-noise synth with LPF, rhythmic-beating, OSC2 detune, and crunchy-noise controls) comes from a published review, not a TE spec — set every knob by ear.

## Sources

- magazinmehatronika.com/en/op-1-field-review/ (DNA = rhythmic noise synth; LPF, rhythmic beating, OSC2 detune, crunchy noise)
