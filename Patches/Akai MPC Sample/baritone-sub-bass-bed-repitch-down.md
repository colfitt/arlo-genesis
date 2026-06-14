---
type: patch
title: Baritone Sub-Bass Bed — Repitch Down
device: Akai MPC Sample
date: 2026-06-14
description: A low, sustained baritone Jazzmaster / VG-800 drone repitched into a doom sub-bed, tuned to the kick's key and filtered sub-only.
tags: [drone, sub-bass, baritone, repitch, doom, rig-integration, designed, signature]
controls:
  - { name: "Warp", type: switch, value: "Pitch (repitch mode), value < 100% (e.g. 50% = down an octave + slower)", options: ["Off", "Pitch", "BPM"] }
  - { name: "Tune Semi (alt)", type: knob, value: "−12 with Warp = Off (octave-down, same length)" }
  - { name: "Tune root", type: knob, value: "MATCH the kick's key (reinforce)" }
  - { name: "Filter", type: switch, value: "LPF4", options: ["LPF2", "LPF4", "HPF2", "HPF4", "BPF"] }
  - { name: "Filter Cutoff", type: knob, value: "~60 (sub-only)" }
  - { name: "Loop + Loop Lock", type: button, value: "endless bed" }
  - { name: "Per-pad Volume", type: knob, value: "lowered — DO NOT Normalize sub-heavy hits (low-freq output clips)" }
  - { name: "Slot/Bank", type: knob, value: "Per-pad (Tune > Warp Pitch + Filter LPF4)" }
---

# Baritone Sub-Bass Bed — Repitch Down

## Concept
A low, sustained baritone Jazzmaster / VG-800 drone repitched into a doom sub-bed. Repitch-down (Warp = Pitch < 100%, or Semi −12) is the dossier's route to baritone sub-bass; tune the root to match the kick so they reinforce, then low-pass it sub-only and loop it endless. The sub-clip warning is rig-critical.

## How to play it
1. Sample a baritone drone off the Apollo bus.
2. Tune page: Warp = Pitch (repitch mode), value < 100% (e.g. 50% = down an octave + slower) OR Semi −12 with Warp = Off for octave-down, same length.
3. Tune the root to MATCH the kick's key so they reinforce.
4. Filter = LPF4, Cutoff ~60 to keep it sub-only.
5. Loop + Loop Lock for an endless bed.

## Notes
- ⚠️ CRITICAL: lower the pad Volume (don't Normalize sub-heavy hits) — low-freq output clips on the box; finalize lows in the Apollo.
- Repitch-down is the dossier's route to baritone sub-bass; the sub-clip warning is rig-critical.

## Sources
- 🟣 designed from `research/links/manual-fx-parameter-reference-knob-fx-color-vintage.md` (Warp Pitch, Filter) + `research/links/mpcforums-ac50-low-frequency-static-clipping.md`
- Transformed from Pedalxly MPC-Sample-Patches.md (designed)
