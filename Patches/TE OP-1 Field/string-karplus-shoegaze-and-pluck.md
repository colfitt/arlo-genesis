---
type: patch
title: "String — Karplus pluck + shoegaze string-machine bed"
device: TE OP-1 Field
date: 2026-06-15
description: "The String engine is a Karplus-Strong waveguide model that runs from organic plucks and soft basses to a string-machine pad 'lovely for shoegaze bedding.' One engine, two homes: a singing dreamy pluck, or a lush sustained bed under banjo/baritone leads (and Cuckoo's secret acoustic-noise source). Dialable recipe — engine description from DeepResearch + review + Cuckoo; no published per-knob values."
tags: [pluck, pad, string, karplus-strong, shoegaze, bass, dreamy]
dips:
  BRAKE: "add the Brake tape effect to slow/reverse the loop for an ethereal reversed-string pass"
controls:
  - { name: "Engine", type: switch, value: "String (select via [Shift]+T1)", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Tension", type: knob, value: "moderate for a singing decay (pluck) / tighten for noise-source percussion (recipe — no published value)" }
  - { name: "Impulse", type: knob, value: "soft for a dreamy pluck (recipe — no published value)" }
  - { name: "Detune", type: knob, value: "slight, for inter-string shimmer (recipe — no published value)" }
  - { name: "Impulse type", type: switch, value: "excitation character — to taste (recipe — no published value)" }
  - { name: "T2 envelope", type: knob, value: "long Attack (Blue) + long Release (Orange) for the string-machine bed (recipe — no published value)" }
  - { name: "Unison", type: switch, value: "engage for a thick bed / Cuckoo's noise-source trick" }
  - { name: "FX", type: switch, value: "Mother reverb or CWO chorus", options: ["spring","delay","grid","punch","nitro","phone","CWO","Mother"] }
---

# String — Karplus pluck + shoegaze string-machine bed

## Concept

The String engine is a Karplus-Strong waveguide model — a noise burst fed into a delayed feedback loop with a closing low-pass — so its decay sounds physically natural. That one engine has two homes. Dial it dreamy and it sings: organic plucks, soft basses, a shimmering picked tone. Stretch its envelope and it becomes a string-machine pad "lovely for shoegaze bedding" — a lush sustained bed to sit under banjo or baritone leads. It is also Cuckoo's secret acoustic-noise source for synthesizing percussion. The terminology is physical (tension/impulse/detune) rather than ADSR, which is the tell that you're driving a model and not a subtractive synth.

## How to play it

1. Select String via [Shift]+T1.
2. Pluck mode: set moderate Tension for a singing decay, a soft Impulse, and a little Detune for shimmer.
3. Bed mode: open the T2 envelope to long Attack (Blue) + long Release (Orange), engage Unison, and hold sustained chords.
4. Add Mother reverb or CWO chorus; send to Board 1 (Microcosm / Dark Star) for smearing.
5. Percussion noise: put String in Unison, tighten the strings, and tune up (Cuckoo's trick) to synthesize shakers/snares before sampling.

## Notes

- HONESTY FLAG: this is a dialable recipe — no published per-knob values exist for the String engine. The control names (Tension, Impulse, Detune, Impulse type) come from a review/forum description of the engine, and the Blue/Orange + T1/T2 mappings are standard OP-1 conventions; treat the positions above as a starting recipe, not a TE spec.
- Karplus-Strong = noise burst into a delayed feedback loop with a closing low-pass — that's why the decay sounds natural; the terminology is physical (tension/impulse), not ADSR.
- Versatile by design: a pad bed, a dreamy pluck, a soft bass, or a noise source for shakers/snares all live in this one engine.
- Add the Brake tape effect to slow/reverse the loop for an ethereal reversed-string pass.

## Sources

- Gear/TE OP-1 Field/research/OP-1-Field-DeepResearch.md §3 (String — string-machine, shoegaze bedding)
- Gear/TE OP-1 Field/research/transcripts/cuckoo-op1-drumkit-build-and-sample-tutorial.md (§String engine noise source)
- magazinmehatronika.com/en/op-1-field-review/ (String = waveguide/Karplus; tension/impulse/detune/impulse-type)
- sinesquares.net/musicgear/teenage-engineering-op-1-field-hands-on-review (Brake to slow/reverse loop)
