---
type: patch
title: Color FX — Cassette / Vinyl / Tube / Saturation / Radio
device: Akai MPC Sample
date: 2026-06-14
description: Tape/vinyl/radio degradation on drums and drone slices via the Color FX, as a per-pad Knob FX or pressure-latched Pad FX.
tags: [degrade, color, tape, vinyl, factory, signature]
controls:
  - { name: "Color mode", type: switch, value: "Cassette / Flutter / Tube Amp / Vinyl / Saturation / Radio", options: ["Cassette", "Flutter", "Tube Amp", "Vinyl", "Saturation", "Radio"] }
  - { name: "Vinyl (Knob FX)", type: knob, value: "tone / crackle / pitch" }
  - { name: "Tape Emulator (Knob FX)", type: knob, value: "noise / tape drift" }
  - { name: "Pad FX route", type: switch, value: "pressure-triggered, latch-able, up to 4 at once", options: ["pressure", "latch"] }
  - { name: "Resample", type: button, value: "bake the degrade in" }
  - { name: "Slot/Bank", type: knob, value: "Pad FX or Knob FX (per-pad)" }
---

# Color FX — Cassette / Vinyl / Tube / Saturation / Radio

## Concept
Tape/vinyl/radio degradation on drums and drone slices. Color emulates Cassette, Flutter, Tube Amp, Vinyl, Saturation, and Radio. Cassette and Vinyl are on-aesthetic for the recorded-wrong rig. DIBIA$E latches Color + LoFi together for dirty textures.

## How to play it
1. Color emulates Cassette, Flutter, Tube Amp, Vinyl, Saturation, Radio.
2. As a Knob FX (per-pad): e.g. Vinyl = tone/crackle/pitch; Tape Emulator = noise/tape drift.
3. As a Pad FX: pressure-triggered, latch-able, up to 4 at once.
4. Bake via Resample.
5. DIBIA$E latches Color + LoFi for dirty textures.

## Notes
- Cassette/Vinyl = on-aesthetic for the recorded-wrong rig.

## Sources
- 🟢 `research/MPC-Sample-DeepResearch.md` §3 (manual Color list) + `research/transcripts/akaipro-mpc-sample-using-effects.md`
- Transformed from Pedalxly MPC-Sample-Patches.md (factory)
