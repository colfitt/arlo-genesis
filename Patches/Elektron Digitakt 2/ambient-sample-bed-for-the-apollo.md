---
type: patch
title: Ambient Sample Bed for the Apollo
device: Elektron Digitakt 2
date: 2026-06-14
description: An evolving stereo pad bed from a sustained baritone/fuzz drone — to print to the Apollo or feed back into the texture boards. Designed from verified DT2 features.
tags: [ambient, pad, drone, designed, signature]
controls:
  - { name: "Source", type: switch, value: "A long sustained baritone/fuzz drone (stereo, post-board)" }
  - { name: "SRC (machine)", type: switch, value: "STRETCH or GRID", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "Pattern", type: switch, value: "Hold a single trig over a 128-step pattern" }
  - { name: "LFO1", type: switch, value: "slow TRIANGLE → FILTER cutoff" }
  - { name: "LFO2", type: switch, value: "slow → PITCH (tiny depth) for drift" }
  - { name: "LFO3", type: switch, value: "RANDOM + slow SLEW → filter or sample-start" }
  - { name: "FLTR", type: switch, value: "Comb+ (key-tracked) for shimmer/metallic motion", options: ["Lowpass 4","Lowpass 2","Highpass","Bandpass","Comb+","Comb-"] }
  - { name: "Reverb send", type: knob, value: "heavy (Supervoid reverb)" }
  - { name: "Chorus + Reverb", type: switch, value: "PARALLEL (not chorus→reverb, avoids mono-collapse)" }
  - { name: "Output", type: switch, value: "Print to Apollo, or route the single track over USB/Main back into Microcosm/H90/Chroma" }
---

# Ambient Sample Bed for the Apollo

## Concept
An evolving stereo pad bed from a sustained baritone/fuzz drone — to print to the Apollo or feed back into the texture boards. One held sample over a 128-step pattern with a three-LFO split (filter / pitch-drift / random-slew), a key-tracked Comb+ for shimmer, heavy reverb, and chorus + reverb kept parallel to avoid the mono collapse.

## How to play it
1. Sample a long sustained baritone/fuzz drone (stereo, post-board) → STRETCH or GRID, hold a single trig over a 128-step pattern.
2. LFO1: slow TRIANGLE → FILTER cutoff.
3. LFO2: slow → PITCH (tiny depth) for drift.
4. LFO3: RANDOM + slow `SLEW` → filter or sample-start.
5. Comb+ (key-tracked) for shimmer/metallic motion.
6. Heavy Supervoid reverb send; chorus + reverb in PARALLEL (not chorus→reverb, avoids mono-collapse).
7. One 128-step pattern, slowly p-locked. Print to Apollo or route the single track over USB/Main back into Microcosm/H90/Chroma.

## Notes
- Designed/inferred. The 3-LFO split (filter/pitch/random-slew) follows boorch's real quoted technique (patch 9); the rest is reasoned from verified DT2 features.
- One held-sample track; one 128-step pattern.

## Sources
- designed from `research/Digitakt-2-DeepResearch.md` §13d
- `research/links/elektronauts-dt2-generative-and-drone.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (designed)
