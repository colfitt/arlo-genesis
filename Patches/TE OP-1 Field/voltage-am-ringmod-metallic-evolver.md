---
type: patch
title: "Voltage — AM/ring-mod metallic evolver"
device: TE OP-1 Field
date: 2026-06-15
description: "The Voltage AM engine dialed for a biting, high-voltage-spark character with rich sidebands — surprisingly good for evolving textures. Sub-osc detune + ring-mod give a metallic, dissonant evolver; drop the sub for sub-octave doom; push AM + ground noise for a harsh electric lead. Encoder map from a named review (SINESQUARES), not TE docs — a dialable recipe, no published per-knob values."
tags: [lead, pad, evolving, metallic, voltage, am-synthesis, gritty]
dips:
  FX: "nitro (saturation) or punch (lo-fi grit)"
controls:
  - { name: "Engine", type: switch, value: "Voltage", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "OCHRE (sub-oscillator octave)", type: knob, value: "center = unison; dial down for sub weight (transposes sub +/-3 oct)" }
  - { name: "GREY (sub-osc detune + ring-mod amount)", type: knob, value: "raise for more metallic / dissonant ring-mod (dial to taste)" }
  - { name: "AM modulation amount", type: knob, value: "up for aggressive, biting sidebands (dial to taste)" }
  - { name: "Ground noise (built-in distortion/grit)", type: knob, value: "to taste — add gradually for electric grit" }
  - { name: "Low-pass filter", type: knob, value: "open for leads; close to darken (dial to taste)" }
  - { name: "OSC2 tune", type: knob, value: "to taste" }
  - { name: "LFO", type: switch, value: "value (assign slow → filter or AM for evolving movement)", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "FX", type: switch, value: "nitro (saturation) or punch (lo-fi grit)", options: ["nitro","punch","spring","delay","grid","cwo","phone","..."] }
---

# Voltage — AM/ring-mod metallic evolver

## Concept

The Voltage AM engine has a biting, "high-voltage spark" character with rich sidebands — and it's surprisingly good for evolving textures. Raise the sub-osc detune + ring-mod (GREY) for a metallic, dissonant evolver; drop the sub octave (OCHRE) for sub-octave doom; or push AM + ground noise for a harsh electric lead. This is the build path behind the existing celestial (Voltage +1 punch) and bass-face (Voltage -1 nitro value) patches — not a single downloaded patch, but the recipe they share.

## How to play it

1. Select the Voltage engine.
2. Set OCHRE (sub-osc octave) down for sub weight, or center/unison for a fuller tone.
3. Raise GREY for ring-mod / sub detune — more = more metallic / dissonant.
4. For an aggressive lead, raise AM and add Ground noise gradually for grit.
5. Assign a slow LFO (filter or AM) for an evolving sweep; add nitro or punch in the master FX slot.

## Notes

- HONESTY FLAG: the Voltage encoder map (OCHRE = sub-octave, GREY = detune + ring-mod) is from a named review (SINESQUARES), not TE docs — directionally reliable, but exact positions are to-taste. No published per-knob values exist; treat every control above as a dialable recipe.
- Ground noise is the engine's built-in distortion/character control.
- Backs the existing celestial (Voltage +1 punch) and bass-face (Voltage -1 nitro value) patches — this is the build path, not a single downloaded patch.

## Sources

- Gear/TE OP-1 Field/research/links/op1-cluster-engine-param-map-and-chorus-pad.md (§VOLTAGE — Ochre sub-octave, Grey detune+ring-mod)
- magazinmehatronika.com/en/op-1-field-review/ (Voltage = AM synthesis; AM amount, ground noise, LPF, OSC2 tune; "biting, aggressive", slow-LFO evolving)
