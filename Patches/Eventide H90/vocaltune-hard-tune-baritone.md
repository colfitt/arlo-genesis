---
type: patch
title: VocalTune Hard-Tune Baritone (vocoder-like)
device: Eventide H90
date: 2026-06-14
description: Robotic auto-tune / "vocoder-like" effect on a sustained baritone or sampled vocal — Tuning Speed cranked, Formant +/-600c reshaping timbre. Feed it the strings.
tags: [pitch, harmonizer-plus, vocaltune, auto-tune, vocoder, factory, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "29" }
  - { name: "Preset A Algorithm", type: switch, value: "VocalTune" }
  - { name: "Root / Scale", type: switch, value: "the key the input is quantized to" }
  - { name: "Tuning Speed", type: knob, value: "cranked to robotic/hard-tune end (back off for subtle correction)" }
  - { name: "Formant", type: knob, value: "-600 to +600 c (reshapes timbre WITHOUT repitching)" }
  - { name: "Quant Error", type: knob, value: "lets small variations through (more natural)" }
  - { name: "EQ (Bass/Treble shelving)", type: knob, value: "-18..+12 dB" }
  - { name: "Compressor", type: knob, value: "Threshold / Ratio 1:1-20:1 / Attack 0.1-100 ms / Release 1-1000 ms / Gain -16..+12 dB" }
  - { name: "Gate", type: switch, value: "built-in" }
---

# VocalTune Hard-Tune Baritone (vocoder-like)

## Concept
A robotic auto-tune / "vocoder-like" effect on a sustained baritone or sampled vocal — also a gentle pitch-lock for the banjo lead. Tuning Speed cranked gives the hard-tune robot; Formant +/-600c reshapes the timbre without repitching; built-in EQ, compressor, and gate clean it up. Feed it the string source, not just vocals.

## How to play it
1. Engage VocalTune on Preset A.
2. Set Root / Scale to the key the input should quantize to.
3. Crank Tuning Speed to the robotic/hard-tune end (back off for subtle correction).
4. Use Formant (-600 to +600 c) to reshape the timbre; let Quant Error through for a more natural feel.
5. Dial the built-in EQ / compressor / gate as needed.

## Notes
- Official manual (firmware v1.10, ported from the H9000). Control ranges are from the manual.
- The "crank Tuning Speed / formant +/-600c on banjo-baritone" application is the rig translation.

## Sources
- research/links/eventide-h90-harmonizer-plus-vocal-algorithms.md (Eventide manual, harmonizer-plus)
- Transformed from Pedalxly H90-Patches.md (factory)
