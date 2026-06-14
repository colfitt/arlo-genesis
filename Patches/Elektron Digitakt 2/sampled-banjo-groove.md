---
type: patch
title: Sampled-Banjo Groove (banjo-as-lead)
device: Elektron Digitakt 2
date: 2026-06-14
description: A playable chromatic banjo instrument sequenced as a groove — banjo-as-lead on the DT2, designed from verified DT2 capabilities.
tags: [banjo, groove, designed, signature]
controls:
  - { name: "Banjo source", type: switch, value: "A single plucked banjo note (EBM-5, stereo, post-VG-800) → Track 1" }
  - { name: "SRC (machine)", type: switch, value: "REPITCH", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "Play", type: switch, value: "Melodic line across the 16 trig keys; p-lock PITCH per step" }
  - { name: "Drums (tracks 2–4)", type: switch, value: "Sampled drum hits, ONESHOT" }
  - { name: "FLTR (banjo)", type: switch, value: "Lowpass 4 (tame the 2–4 kHz pierce)", options: ["Lowpass 4","Lowpass 2","Highpass","Bandpass","Comb+","Comb-"] }
  - { name: "Master Overdrive", type: knob, value: "light (glue)" }
  - { name: "Conditional", type: switch, value: "2:3 on a ghost note (never loops identically)" }
---

# Sampled-Banjo Groove (banjo-as-lead)

## Concept
A playable chromatic banjo instrument sequenced as a groove — banjo-as-lead on the DT2. Sample a single plucked banjo note into a Repitch track, play a melodic line across the 16 trig keys and p-lock the pitch per step, with sampled drums on tracks 2–4. A Lowpass 4 tames the pierce, light master overdrive glues it, and a 2:3 conditional on a ghost note keeps it from looping identically.

## How to play it
1. Sample a single plucked banjo note (EBM-5, stereo, post-VG-800) → Track 1, REPITCH machine.
2. Play a melodic line across the 16 trig keys; p-lock PITCH per step.
3. Tracks 2–4 = sampled drum hits (ONESHOT).
4. Add Lowpass 4 on the banjo to tame the 2–4 kHz pierce; light Master Overdrive for glue.
5. Add a `2:3` conditional on a ghost note so it never loops identically.

## Notes
- Designed/inferred — a reasoned rig starting point, NOT a found preset. Built from verified DT2 capabilities (Repitch, Lowpass 4, 2:3 conditional).
- Banjo on track 1; drums 2–4; save as a kit.

## Sources
- designed from `research/Digitakt-2-DeepResearch.md` §13a (Starting-Point Workflows)
- Transformed from Pedalxly Digitakt-2-Patches.md (designed)
