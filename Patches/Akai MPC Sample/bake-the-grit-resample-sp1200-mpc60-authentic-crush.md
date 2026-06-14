---
type: patch
title: Bake-the-Grit Resample — SP1200/MPC60 Authentic Crush
device: Akai MPC Sample
date: 2026-06-14
description: Authentic vintage-sampler grit on breaks/one-shots via the genuine pitch-up-then-resample SP1200 12-bit technique, with Vintage Emulator and LoFi baked in.
tags: [resample, degrade, vintage, sp1200, mpc60, lofi, community, signature]
controls:
  - { name: "Tune Semi (step 1)", type: knob, value: "+6 (pitch the source UP)" }
  - { name: "Vintage Emulator K1 Type", type: switch, value: "SP1200 / MPC60 / SP1200Ring", options: ["SP1200", "MPC60", "SP1200Ring", "MPC3000"] }
  - { name: "Resample (Pad 11)", type: button, value: "crush hits the pitched-up signal (recreates aliasing)" }
  - { name: "Tune Semi (step 4)", type: knob, value: "~−6 (tune the resample back DOWN)" }
  - { name: "LoFi Bitcrush (heavier)", type: knob, value: "~8 → 4" }
  - { name: "LoFi Decimator (heavier)", type: knob, value: "20–60%" }
  - { name: "Color (stack)", type: switch, value: "Cassette / Vinyl (for hiss)", options: ["Cassette", "Flutter", "Tube Amp", "Vinyl", "Saturation", "Radio"] }
  - { name: "Slot/Bank", type: knob, value: "Knob FX = Vintage Emulator / LoFi → resampled pad" }
---

# Bake-the-Grit Resample — SP1200/MPC60 Authentic Crush

## Concept
Authentic vintage-sampler grit on breaks/one-shots — the degraded "recorded-wrong" sound. Pitch the source up, crush it, resample, then pitch back down: this recreates the original memory-limit aliasing of a 12-bit/26 kHz SP1200. The emulations are flavor curves, not converter clones (matches the Sarah2ill A/B finding), but the pitch-up-then-resample is the genuine technique.

## How to play it
1. Tune the source UP +6 semitones (Tune Semi=+6).
2. Put Vintage Emulator Knob FX on the pad: K1 Type = SP1200 (grainy snare bite) / MPC60 (dark glue) / SP1200Ring (metallic edge).
3. Resample (Pad 11) so the crush hits the pitched-up signal (recreates the original memory-limit aliasing).
4. Tune the resample back DOWN ~−6 st.
5. Heavier: add LoFi (Bitcrush ~8→4, Decimator 20–60%) before resampling; stack Color = Cassette/Vinyl for hiss.

## Notes
- Honest: the emulations are flavor curves, not converter clones — subtle (matches the Sarah2ill A/B finding).
- The pitch-up-then-resample is the genuine SP1200 12-bit/26 kHz technique.

## Sources
- 🔵 `research/links/vintage-mode-sp1200-mpc60-resample-degrade-recipe.md` (maschinetutorials / illmuzik / djavemcree) + `research/links/manual-fx-parameter-reference-knob-fx-color-vintage.md`
- Transformed from Pedalxly MPC-Sample-Patches.md (community)
