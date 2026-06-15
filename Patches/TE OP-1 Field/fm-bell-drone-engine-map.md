---
type: patch
title: "FM — bell/drone (engine-map build)"
device: TE OP-1 Field
date: 2026-06-15
description: "A dialable recipe (no published values) for building an FM bell/drone voice from the documented FM encoder map — raise operator level for harmonics, hunt the ratio set for harmonic-vs-discordant character, pick an algorithm, add detune for inharmonic movement. The dial-it-yourself build path behind Andreas Roman's 'Tombola on FM bells.' FM encoder map from Attack Magazine's FM deep-dive."
tags: [bells, fm, drone, shimmer, ambient, designed]
controls:
  - { name: "Engine", type: switch, value: "FM", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","DSynth","DBox","Synth Sampler","Sampler"] }
  - { name: "Blue (level of all non-Base operators)", type: knob, value: "CCW = pure sine; raise to bring in FM harmonics (bell brightness)" }
  - { name: "Beige/Ochre (frequency / ratio set)", type: knob, value: "sweep harmonic → discordant for bell color (ratio steps vary wildly)" }
  - { name: "Grey (algorithm select)", type: knob, value: "pick 1 of 9 operator-routing algorithms" }
  - { name: "Orange (detune)", type: knob, value: "add for inharmonic movement / drift" }
---

# FM — bell/drone (engine-map build)

## Concept

Build an FM bell/drone voice from the ground up using the documented FM encoder map rather than a preset. Raise the non-Base operator level (Blue) to push past a pure sine into FM harmonics — that's the bell brightness. Sweep the frequency/ratio set (Beige/Ochre) to find a ratio that lands anywhere on the harmonic-to-discordant continuum, which is what sets the bell's color. Choose one of nine algorithms (Grey) to change how the operators route into each other, and add detune (Orange) for inharmonic movement. This is the engine recipe that feeds the existing "Andreas Roman — Tombola on FM bells" performance patch: drive this voice with the Tombola for raindrop shimmer, or hold a low note for an FM drone.

## How to play it

1. Select the **FM** engine.
2. Raise **Blue** to bring in FM harmonics (bell brightness) — full CCW is a pure sine.
3. Sweep **Beige/Ochre** to find a ratio set with the desired harmonic-vs-discordant bell color.
4. Pick a **Grey** algorithm; add **Orange** detune for inharmonic movement.
5. Drive with the Tombola for raindrop shimmer, or hold a low note for an FM drone.

## Notes

- **No published numeric values** — this is a dialable recipe, not sourced knob positions. The FM encoder *map* (what each color-coded encoder does) is from a named source (Attack Magazine's FM deep-dive); the exact positions are to-taste.
- Distinct from the "Andreas Roman — Tombola on FM bells" patch: that one is the sequencer/performance move, this is the underlying engine build recipe.
- The ratio set (Beige/Ochre) does not step in even musical intervals — it ranges widely from harmonic to discordant, so audition by ear.
- Engine list shown is the OP-1 Field set (DSynth/DBox are Field-only additions over the original OP-1).

## Sources

- Gear/TE OP-1 Field/research/links/op1-cluster-engine-param-map-and-chorus-pad.md (§FM encoder map — Attack Magazine)
- Gear/TE OP-1 Field/research/links/cdm-op1-field-album-workflow.md (Andreas Roman — FM bells)
- dialable recipe (no published values) — FM encoder map from Attack Magazine
