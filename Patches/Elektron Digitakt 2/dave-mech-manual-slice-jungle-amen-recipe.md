---
type: patch
title: Dave Mech Manual-Slice Jungle / Amen Recipe
device: Elektron Digitakt 2
date: 2026-06-14
description: Chop a break into a playable, rearrangeable slice instrument — then mangle it onto the aesthetic with down-octave, bit crush, LFO→filter, reverse-loop and Comb, per Dave Mech.
tags: [slice, jungle, amen, break, mangle, factory, artist, signature]
controls:
  - { name: "OS", type: switch, value: "1.15+" }
  - { name: "SRC (machine)", type: switch, value: "SLICE", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "Create Slice Grid", type: switch, value: "YES → 32 slices" }
  - { name: "DIRT", type: switch, value: "transient/zero-cross detection ON (kills clicks)", options: ["ON","OFF"] }
  - { name: "Trig mode", type: switch, value: "SLICE (16 trig keys = slices)" }
  - { name: "Locks", type: switch, value: "LINEAR LOCKS (slices 1,2,3,4…) or RANDOM LOCKS (instant rearrangements)" }
  - { name: "Note LENGTH", type: knob, value: ">1 step plays multiple consecutive slices (1 = choppy, 2 = longer phrases)" }
  - { name: "LFO → slice-select", type: switch, value: "SAMPLE-AND-HOLD (a little slew)" }
  - { name: "Tune slices", type: knob, value: "down an octave (weight)" }
  - { name: "LFO2 DEST", type: switch, value: "Low-pass freq (copy LFO1 → LFO2)" }
  - { name: "FLTR", type: switch, value: "COMB (metallic) or Lowpass 4", options: ["Lowpass 4","Lowpass 2","Highpass","Bandpass","Comb+","Comb-"] }
  - { name: "Per-slice", type: switch, value: "reverse + loop; retrig on slices; add delay + bit crush" }
---

# Dave Mech Manual-Slice Jungle / Amen Recipe

## Concept
Chops a break into a playable, rearrangeable slice instrument with the SLICE machine, then mangles it onto the doom/drone aesthetic. Create a 32-slice grid with DIRT on (transient/zero-cross detection kills clicks), trigger slices from the 16 keys, and use linear or random locks for instant rearrangements. The degrade half — down-octave, bit crush, LFO→filter, reverse-loop, Comb — is the on-aesthetic part.

## How to play it
1. OS 1.15+. `SRC` → machine = SLICE; load break; `YES` → Create Slice Grid, choose 32 slices, `DIRT` = transient/zero-cross detection ON (kills clicks).
2. Trig mode = SLICE (16 trig keys = slices).
3. Create LINEAR LOCKS (slices 1,2,3,4…) or RANDOM LOCKS for instant rearrangements (copy a good page, paste back after randomizing the next).
4. Note `LENGTH > 1` step plays multiple consecutive slices (1 = choppy, 2 = longer phrases).
5. Mangle: LFO → slice-select with SAMPLE-AND-HOLD (a little slew); tune slices down an octave for weight; add delay; add bit crush; copy LFO1→LFO2, route LFO2 → low-pass freq; reverse + loop per slice; switch filter to COMB (metallic) or Lowpass 4. Retrig on slices.

## Notes
- The degrade/mangle half (down-octave + bit crush + LFO→filter + reverse-loop + Comb) is the on-aesthetic part.
- One break per track; save as a kit.

## Sources
- Ref: Dave Mech — "MANUAL SLICES for Digitakt II // OS 1.15" (yt `sSEMZsMSjd4`).
- `research/transcripts/davemech-dt2-slice-machine-os115.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (factory/artist)
