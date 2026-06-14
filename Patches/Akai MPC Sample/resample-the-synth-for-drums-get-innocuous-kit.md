---
type: patch
title: Resample-the-Synth-for-Drums (Get Innocuous kit)
device: Akai MPC Sample
date: 2026-06-14
description: The signature DFA method — synthesize the whole kit from one polysynth's voices and resample them into the sampler, the "Get Innocuous!" move AC50-mapped.
tags: [taste-profile, resample, synth-drums, dfa, designed, signature]
controls:
  - { name: "Source synth", type: switch, value: "VG-800 SYNTH or OP-1 (one polysynth's voices)", options: ["VG-800", "OP-1"] }
  - { name: "Resample (Pad 11)", type: button, value: "resample each voice in (silent first try, do it twice)" }
  - { name: "Tune", type: knob, value: "to key" }
  - { name: "Amp Env Attack", type: knob, value: "0" }
  - { name: "Amp Env Decay", type: knob, value: "short, Decay-From = Start" }
  - { name: "Transient FX", type: knob, value: "shape the punch" }
  - { name: "Loop + layer", type: knob, value: "additively like 'All My Friends'" }
  - { name: "Slot/Bank", type: knob, value: "Empty pads (Pad 11 = Resample shortcut); kit kept in one Project" }
---

# Resample-the-Synth-for-Drums (Get Innocuous kit)

## Concept
The signature DFA method — synthesize the kit from one polysynth's voices and resample them in (the "Get Innocuous!" CS-60 move), AC50-mapped. One synth becomes the whole kit. Designed (MPC-E2) — the DFA method, not LCD's actual CS-60.

## How to play it
1. Synthesize a kick/snare/cowbell from the VG-800 SYNTH (or OP-1) — one polysynth's voices.
2. Resample (Pad 11) each into the sampler (resample is silent the first try, do it twice).
3. Tune to key, shape with Amp Env (Attack 0, short Decay with Decay-From=Start) + Transient FX.
4. Then loop and layer additively like "All My Friends". One synth → the whole kit.

## Notes
- MPC-E2.
- Known bug: Resample silent first try → do it twice.
- The DFA method, not LCD's actual CS-60.

## Sources
- 🟣 designed from `Research/Taste-Profile/sources/lcd-murphy-resample-synth-drums-analog-imperfection.md`
- Ref: LCD Soundsystem "Get Innocuous!" (kit built from a Yamaha CS-60 and resampled)
- Transformed from Pedalxly MPC-Sample-Patches.md (designed)
