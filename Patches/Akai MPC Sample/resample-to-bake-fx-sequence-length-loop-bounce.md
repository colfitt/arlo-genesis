---
type: patch
title: Resample to Bake FX — Sequence-Length Loop Bounce
device: Akai MPC Sample
date: 2026-06-14
description: Printing Knob FX / Color / LoFi into a clean loop, then chop and rebuild — the generative loop and the workaround for every "FX is global" limit.
tags: [resample, bake-fx, loop, workflow, factory, signature]
controls:
  - { name: "Sample Record Source", type: switch, value: "Resample", options: ["Mic", "Rear", "USB", "Resample"] }
  - { name: "Length (K2)", type: switch, value: "Sequence (one loop, recommended) vs Free", options: ["Sequence", "Free"] }
  - { name: "Shortcut", type: button, value: "Sample + Pad 11 = auto-resample current source with FX printed" }
  - { name: "Post-bake", type: knob, value: "turn off live FX; chop/retune the resample" }
  - { name: "Slot/Bank", type: knob, value: "Empty pad (Pad 11 for the shortcut)" }
---

# Resample to Bake FX — Sequence-Length Loop Bounce

## Concept
Printing Knob FX / Color / LoFi into a clean loop, then chopping and rebuilding — the core "resample bed → re-mangle" move for the recorded-wrong aesthetic, and the workaround for every "FX/character is global" limit on the box.

## How to play it
1. With a loop playing plus a Knob FX on it (e.g. Tape Emulator): Sample → empty pad → Sample Record → Source = Resample.
2. Set length with K2 = Sequence (exactly one sequence loop, recommended) vs Free.
3. Strike the pad → Play → it auto-stops at sequence end → Stop.
4. Now you have a loop with FX baked in; turn off the live FX; chop/retune the resample.
5. Shortcut: Sample + Pad 11 auto-resamples the current source with FX printed.

## Notes
- ⚠️ Resample is SILENT on the first try — do it twice.
- The workaround for every "FX/character is global" limit.

## Sources
- 🟢 `research/transcripts/akaipro-mpc-sample-resampling.md` + `research/transcripts/akaipro-mpc-sample-using-effects.md`; bug from `research/links/mpcforums-ac50-bugs-and-fixes-thread.md` (t/220432)
- Transformed from Pedalxly MPC-Sample-Patches.md (factory)
