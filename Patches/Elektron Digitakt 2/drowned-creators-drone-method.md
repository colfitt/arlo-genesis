---
type: patch
title: DROWNED! Creator's Drone Method (slow + random-slew LFOs)
device: Elektron Digitakt 2
date: 2026-06-14
description: Long-evolving drone presets via slow filter/pitch LFOs and random LFOs with slow slews — the gold-standard quoted DT2 drone-modulation primitive, per boorch (DROWNED! pack).
tags: [drone, doom, lfo, degrade, factory, artist, signature]
controls:
  - { name: "LFO usage", type: switch, value: "All 3 LFOs per track" }
  - { name: "Slow LFOs", type: switch, value: "DEST = FILTER (and sometimes PITCH), slow → evolve over long periods" }
  - { name: "Random LFOs", type: switch, value: "WAVE = RANDOM with slow SLEWS → unpredictability" }
  - { name: "Source samples", type: switch, value: "Seamless loops with slowly-evolving character baked in (stereo)" }
  - { name: "FLTR (some presets)", type: switch, value: "COMB (metallic/resonant motion)" }
  - { name: "Degrade move", type: switch, value: "Reprocess sources outside the box (through the pedalboard) then resample back in" }
---

# DROWNED! Creator's Drone Method (slow + random-slew LFOs)

## Concept
The most concrete drone *guidance* found for the DT2 — technique, not numbers. Verbatim creator method: "all LFO work on DTII is either slow LFOs modulating FILTER and sometimes PITCH to make them evolve for even longer periods, or RANDOM LFOs with slow SLEWS to add unpredictability." Start from source samples that already evolve, use all three LFOs, lean on the Comb filter for metallic motion, and degrade outside the box (through the rig's texture boards) before resampling back in.

## How to play it
1. Use all 3 LFOs per track.
2. Set slow LFOs modulating FILTER (and sometimes PITCH) so they evolve for even longer periods.
3. Use RANDOM LFOs with slow SLEWS to add unpredictability.
4. Start from source samples that are seamless loops with slowly-evolving character baked in (don't rely on the engine for all motion).
5. Use the COMB filter on some presets for metallic/resonant motion.
6. Use stereo source samples (real stereo material into the stereo engine).
7. For "headcrusher" variants, reprocess sources outside the box (run prints through the pedalboard), then resample back in.

## Notes
- The degrade-outside-then-resample move maps directly onto running prints through the rig's texture boards.
- Save each drone as a preset; build a "drone" kit.

## Sources
- Ref: boorch (Bruce Menace) — DROWNED! thread (elektronauts t/220614).
- `research/links/elektronauts-drowned-dt2-drone-preset-pack.md`
- `research/links/elektronauts-dt2-generative-and-drone.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (factory/artist)
