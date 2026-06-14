---
type: patch
title: Comb-Filter Resampling Degradation Loop
device: Elektron Digitakt 2
date: 2026-06-14
description: Metallic/resonant iterative degradation — run loops / single shots through the Comb filter, resample, repeat. Banjo pluck → detuned metallic resonator.
tags: [resample, comb, degrade, metallic, banjo, community, signature]
controls:
  - { name: "FLTR", type: switch, value: "COMB (run loops / single shots through it)", options: ["Lowpass 4","Lowpass 2","Highpass","Bandpass","Comb+","Comb-"] }
  - { name: "Resample", type: switch, value: "Resample the comb-filtered output, then repeat (iterative)" }
---

# Comb-Filter Resampling Degradation Loop

## Concept
The simplest version of the resample-mangle loop, and great on a banjo pluck: run loops or single shots through the COMB filter, resample the result, then repeat — each pass adds more metallic/resonant degradation, turning a banjo pluck into a detuned metallic resonator.

## How to play it
1. Run loops / single shots through the COMB filter.
2. Resample.
3. Repeat — iterative metallic/resonant degradation each pass.

## Notes
- Technique-level (no numeric values).
- Use a resample track; save each generation.

## Sources
- `research/links/elektronauts-dt2-tips-tricks-thread.md` (t/212556 — Honeysmack, post #17)
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
