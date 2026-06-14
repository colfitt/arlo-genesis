---
type: patch
title: Fuzz-Wall Chop-to-Drone Bed
device: Akai MPC Sample
date: 2026-06-14
description: Turning a sustained Board-1 fuzz/baritone wall off the Apollo bus into a tuned, loopable drone instrument with an infinite reverb tail.
tags: [drone, fuzz, chop, reverb, rig-integration, designed, signature]
controls:
  - { name: "Input Config Source", type: switch, value: "Rear (stereo)", options: ["Mic", "Rear", "USB", "Resample"] }
  - { name: "Chop Type", type: switch, value: "Threshold (or Regions 8)", options: ["By Transients", "Manual", "Threshold", "Regions"] }
  - { name: "Threshold (Shift+K3)", type: knob, value: "high ~70–90% (fewer, longer slices)" }
  - { name: "Loop + Loop Lock (Shift+B1)", type: button, value: "engage for sustained drone" }
  - { name: "Polyphony / Note On (Shift+Chop)", type: switch, value: "Note On (gate-while-held)", options: ["off", "Note On"] }
  - { name: "Tune Semi", type: knob, value: "to song key" }
  - { name: "Reverb Large K Time", type: knob, value: "+inf s (infinite wall)" }
  - { name: "Reverb Large K Mix", type: knob, value: "~40%" }
  - { name: "Reverb Large K Pre-Delay", type: knob, value: "~30 ms" }
  - { name: "Resample", type: button, value: "with LoFi/Color baked" }
  - { name: "Slot/Bank", type: knob, value: "Drone slice pad + Knob FX = Reverb Large" }
---

# Fuzz-Wall Chop-to-Drone Bed

## Concept
Turning a sustained Board-1 fuzz/baritone wall (off the Apollo bus) into a tuned, loopable drone instrument. Chop into a few rich long slices, sustain one with Loop Lock + Note On, tune it to key, and drown it in Reverb Large with the infinite tail. "Use sources nobody else has" (DJ Shadow) applied to the rig.

## How to play it
1. Sample a 10–20 s wall (Input Config Source = Rear, stereo).
2. Chop → Type = Threshold, `Shift+K3` Threshold high ~70–90% (fewer, longer slices) OR Regions 8.
3. Pick one rich slice → engage Loop + Loop Lock (`Shift+B1`), set Polyphony = Note On (`Shift+Chop` = NOTE ON gate-while-held) for a sustained drone.
4. Tune to song key (Semi).
5. Add Reverb Large Knob FX (Time = +inf s, Mix ~40%, Pre-Delay ~30 ms) for the infinite wall.
6. Resample with LoFi/Color baked.

## Notes
- Reverb Time → +inf s is the manual-confirmed infinite tail.
- "Use sources nobody else has" (DJ Shadow) applied to the rig.

## Sources
- 🟣 designed from `research/links/manual-fx-parameter-reference-knob-fx-color-vintage.md` (Chop Threshold, Loop Lock, Reverb +inf, Note On) + `research/MPC-Sample-DeepResearch.md` §6
- Transformed from Pedalxly MPC-Sample-Patches.md (designed)
