---
type: patch
title: VocalShift Mono-Drone-to-Chord (3-voice)
device: Eventide H90
date: 2026-06-14
description: Harmonize a mono banjo/baritone drone into a wide, scale-locked 3-voice stereo chord — a "singing wall."
tags: [pitch, harmonizer-plus, vocalshift, harmony, drone, sustained-wall, factory, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "30" }
  - { name: "Preset A Algorithm", type: switch, value: "VocalShift" }
  - { name: "Mix", type: knob, value: "to taste" }
  - { name: "Root / Scale", type: switch, value: "song key/scale" }
  - { name: "Shift A/B/C", type: knob, value: "interval per voice" }
  - { name: "Formant A/B/C", type: knob, value: "per voice" }
  - { name: "Formant Link", type: switch, value: "auto-stretches formants in proportion to shift" }
  - { name: "Per-voice Gain / Delay / Feedback / Pan A/B/C", type: knob, value: "Delay in ms or synced" }
  - { name: "Detune", type: knob, value: "equal up/down on Voices B & C to thicken" }
  - { name: "Tuning Speed", type: knob, value: "to taste" }
  - { name: "Quant", type: switch, value: "On/Off + Quant Error" }
  - { name: "Latency Mode", type: switch, value: "Low / High", options: ["Low", "High"] }
  - { name: "Glide A/B/C + Rise + Fall", type: knob, value: "to taste" }
  - { name: "Solo A/B/C", type: switch, value: "per voice" }
  - { name: "Performance", type: button, value: "Root learn, Glide, Glide (M), Hold (M), Hold" }
---

# VocalShift Mono-Drone-to-Chord (3-voice)

## Concept
Harmonize a mono banjo/baritone drone into a wide, scale-locked 3-voice stereo chord — a "singing wall." Shift A/B/C set the intervals; Detune on Voices B & C thickens; per-voice pan spreads it stereo. Stack into the wet-only super-algorithm for the full singing wall.

## How to play it
1. Engage VocalShift on Preset A.
2. Set Root / Scale to the song key, then dial Shift A/B/C intervals per voice.
3. Add equal up/down Detune on Voices B & C to thicken; pan the voices for stereo width.
4. Map Performance functions (Root learn, Glide, Hold) to footswitches as needed.

## Notes
- Official manual (v1.10). Control list verbatim.
- The mono-drone-to-stereo-chord use is the rig translation.
- Stack into the wet-only super-algorithm (see "Wet-Only Super-Algorithm Routing") for a singing wall.

## Sources
- research/links/eventide-h90-harmonizer-plus-vocal-algorithms.md (Eventide manual, harmonizer-plus)
- Transformed from Pedalxly H90-Patches.md (factory)
