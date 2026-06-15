---
type: patch
title: "Multi-Generational Resampling — re-capture the degraded loop"
device: Chase Bliss Blooper
date: 2026-06-15
description: "Andy Othling's degradation method on-pedal — build a loop with STABILITY engaged so it ages, switch to SAMP (Carryover) and trigger it, then re-record that already-aged output back into a fresh loop through more STABILITY. Stacking re-sampling generations so you're hearing the third or fourth pass of the sound — the 'recorded-wrong' aesthetic, native to Blooper (artist: Andy Othling / Lowercase Noises, Sound Methods interview; method mapped to Blooper, honesty-flagged)."
tags: [degrade, tape-aging, sampler, resample, artist, signature]
controls:
  - { name: "Mode", type: switch, value: "build in NORM/ADD (with STABILITY) → SAMP to trigger → back to NORM/ADD to re-record the next generation", options: ["NORM", "ADD", "SAMP"] }
  - { name: "STABILITY", type: knob, value: "engaged on the first loop; increase per generation so each re-capture ages further — set by ear, no published values" }
  - { name: "RIGHT footswitch", type: button, value: "in SAMP, triggers the carried-over loop so you can re-record its aged output" }
  - { name: "LEFT footswitch", type: button, value: "RECORD — re-record the triggered output into a fresh loop; in SAMP this wipes the loop, so re-capture deliberately" }
  - { name: "EXT RECORD", type: switch, value: "external footswitch into the EXT jack — hands-free re-capture between generations" }
  - { name: "Slot/Bank", type: knob, value: "mode toggle NORM/ADD ↔ SAMP plus STABILITY — dialable recipe, no published knob values" }
---

# Multi-Generational Resampling — re-capture the degraded loop

## Concept

Andy Othling's DAW resampling philosophy mapped onto the pedal: build a loop, switch to SAMP and trigger it, then re-record that triggered (already-aged) output back into a fresh loop through more STABILITY. Each pass is a new "generation," so by the third or fourth re-capture you're hearing a sampling of a sampling of a sampling — the original sound several degradations removed. STABILITY does the aging, SAMP/Carryover does the re-triggering, and the LEFT (RECORD) footswitch closes the loop on the next generation. The "recorded-wrong" aesthetic, native to Blooper.

## How to play it

1. Build a loop in NORM/ADD with STABILITY on so it ages.
2. Switch to SAMP (Carryover) and trigger the loop with the RIGHT footswitch to hear it back.
3. Re-record that triggered output into a fresh loop in NORM/ADD, adding more STABILITY this generation.
4. Repeat — each generation degrades further, so you end up hearing the third/fourth sampling of the original.
5. Let downstream pedals (Chroma / H90) re-stereo and reverb the final degraded wall.

## Notes

- Method maps Andy's DAW resampling idea ("you're hearing the fourth sampling of it") onto Blooper's ADD-Stability + SAMP-Carryover.
- Honesty flag: the original quote in the source is about Primal Tap / VSS-30, not Blooper-specific — the *method* transfers, the attribution does not. This is a designed mapping, not a sourced Blooper preset.
- Honesty flag: no published knob values — increase STABILITY per generation by ear; everything else dials from this recipe.
- Watch out: hitting RECORD (LEFT) in SAMP wipes the loop — re-record into a new pass deliberately rather than over the carried-over sample.

## Sources

- `research/links/andy-othling-sound-methods-ambient-technique.md` (multi-generational resampling philosophy; on-pedal mapping flagged)
- `research/transcripts/knobs-better-bloops-sampler-mode.md` (Carryover; SAMP record wipes loop)
- Ref: artist — Andy Othling (Lowercase Noises), Sound Methods interview (method mapped to Blooper, honesty-flagged)
