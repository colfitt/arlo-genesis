---
type: patch
title: LFO SPD/MULT Musical-Rate Table + 1:1 Resample Levels
device: Elektron Octatrack MkII
date: 2026-06-14
description: A calibration sheet — locking LFO-on-cutoff/STRT to the grid (slow breathing wall) and avoiding resample generation-loss with 1:1 record/CUE levels.
tags: [reference, calibration, lfo, resample, community]
controls:
  - { name: "Slot/Bank", type: knob, value: "Any track LFO; record/CUE levels are global" }
  - { name: "LFO rate 0.25 cyc/bar", type: knob, value: "SPD64 / MULT1× (@130 BPM)" }
  - { name: "LFO rate 0.5 cyc/bar", type: knob, value: "SPD32 / MULT1× (@130 BPM)" }
  - { name: "LFO rate 1.0 cyc/bar", type: knob, value: "SPD16 / MULT127 (@130 BPM — verify on-box)" }
  - { name: "LFO rate 4/3 cyc/bar", type: knob, value: "SPD12 / MULT2× (@130 BPM)" }
  - { name: "Slow drone breath", type: knob, value: "SPD ~32-64" }
  - { name: "Unity resample LEVEL", type: knob, value: "Flex record-track LEVEL = 127" }
  - { name: "Unity resample AMP VOL", type: knob, value: "0" }
  - { name: "Unity resample CUE VOL", type: knob, value: "127 (overdub); match CUE vol to track level for 1:1" }
  - { name: "Flat-LFO fine control", type: switch, value: "one LFO with a near-flat DESIGNER waveform (values 2-7) at DEPTH = 64, modulated by a 2nd LFO → imperceptible slow drift" }
---

# LFO SPD/MULT Musical-Rate Table + 1:1 Resample Levels

## Concept
A calibration sheet, not a sound: locking LFO-on-cutoff/STRT to the grid for a slow breathing wall, and avoiding resample generation-loss with 1:1 record/CUE levels. Pair with the Ambient Drone Bed / Scene-Locked LFO patches to lock the breath to tempo.

## How to play it
1. **LFO rate** (audio tracks, example @130 BPM): **0.25 cyc/bar = SPD64/MULT1×; 0.5 = SPD32/MULT1×; 1.0 = SPD16/MULT127; 4/3 = SPD12/MULT2×.** For a slow drone breath use **SPD ~32-64.**
2. **Unity resample:** Flex record-track **LEVEL = 127, AMP VOL = 0, CUE VOL = 127** (overdub); match CUE vol to track level for 1:1.
3. **Flat-LFO fine control:** one LFO with a near-flat DESIGNER waveform (values 2-7) at DEPTH = 64, modulated by a 2nd LFO → imperceptible slow drift.
4. Budget: RAM ~85.5 MB; a 4-bar/130 BPM clip ~7.4 s reserve per track.

## Notes
- Rates are **tempo-relative** (given @130 BPM); the MULT "127" notation for 1.0 cyc/bar **should be verified on-box.**
- A calibration sheet, not a sound — pair with the Ambient Drone Bed / Scene-Locked Random LFO patches to lock the breath to tempo.

## Sources
- Ref: Elektron Octatrack Master Reference (community Google Doc)
- research/links/lfo-musical-rate-table-master-reference.md
- Transformed from Pedalxly Octatrack-MkII-Patches.md (community)
