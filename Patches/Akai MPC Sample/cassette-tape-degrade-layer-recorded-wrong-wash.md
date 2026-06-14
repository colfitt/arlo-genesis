---
type: patch
title: Cassette/Tape Degrade Layer — Recorded-Wrong Wash
device: Akai MPC Sample
date: 2026-06-14
description: Wow/flutter/hiss on any sample or the whole beat for the degraded shoegaze/lo-fi finish, via the Tape or Vinyl Emulator Knob FX.
tags: [degrade, tape, vinyl, wow-flutter, factory, signature]
controls:
  - { name: "Tape Emulator K1 Wow", type: knob, value: "30–60% (range 10–100)" }
  - { name: "Tape Emulator K2 Noise", type: knob, value: "20–40%" }
  - { name: "Tape Emulator K3 Pitch instability", type: knob, value: "30–50% (range 20–100)" }
  - { name: "Color (alt)", type: switch, value: "K1 Mode = Cassette / Flutter", options: ["Cassette", "Flutter"] }
  - { name: "Vinyl Emulator K1 Tone", type: knob, value: "~40" }
  - { name: "Vinyl Emulator K2 Crackle", type: knob, value: "20–50%" }
  - { name: "Vinyl Emulator K3 Pitch", type: knob, value: "30–60%" }
  - { name: "Scope", type: switch, value: "per-pad or All Pads (B2)", options: ["per-pad", "All Pads (B2)"] }
  - { name: "Resample", type: button, value: "bake (Pad FX can't be sequenced)" }
  - { name: "Slot/Bank", type: knob, value: "Knob FX = Tape Emulator / Vinyl Emulator" }
---

# Cassette/Tape Degrade Layer — Recorded-Wrong Wash

## Concept
Wow/flutter/hiss on any sample or the whole beat for the degraded shoegaze/lo-fi finish. Use the Tape Emulator for cassette-style wow/noise/pitch-instability, or the Vinyl Emulator for crackle/tone/pitch. All ranges are manual-confirmed (UG v1.3).

## How to play it
1. Tape Emulator Knob FX: K1 Wow 30–60% (range 10–100), K2 Noise 20–40%, K3 Pitch instability 30–50% (20–100).
2. OR Color Knob FX K1 Mode = Cassette / Flutter.
3. For vinyl instead: Vinyl Emulator K1 Tone ~40, K2 Crackle 20–50%, K3 Pitch 30–60%.
4. Apply per-pad or All Pads (B2).
5. Bake via Resample (Pad FX can't be sequenced).

## Notes
- All ranges manual-confirmed (UG v1.3).

## Sources
- 🟢 `research/links/manual-fx-parameter-reference-knob-fx-color-vintage.md` (Tape/Vinyl Emulator + Color ranges)
- Transformed from Pedalxly MPC-Sample-Patches.md (factory)
