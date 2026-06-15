---
type: patch
title: "Banjo roll — drum-sampler 16-slice carve"
device: TE OP-1 Field
date: 2026-06-15
description: Drop a single in-time banjo roll loop into the Drum Sampler and let the auto-16-slice (lower keys) + 8-slice (upper) carve it into a playable, choppable kit — per-slice pitch, choke groups, reverse, and attack turn one banjo phrase into a chromatic/percussive instrument entirely on-box. Method-level from documented Drum-sampler behavior (sonwu, ADG, Cuckoo) — no published knob values.
tags: [drum-kit, sampler, banjo, capture-and-mangle, designed, signature]
dips:
  CAP: "20 s record limit on the Field"
  WATCH: "double-compression on sample-in"
controls:
  - { name: "Engine", type: switch, value: "Drum sampler (record ≤20 s; auto-slices into 16 lower keys + 8 upper)" }
  - { name: "BLUE", type: knob, value: "per-slice PITCH; press BLUE to ZOOM the waveform; [Shift]+BLUE = reverse" }
  - { name: "OCHRE", type: knob, value: "slice START point (trim to zero crossing)" }
  - { name: "GRAY", type: knob, value: "slice END point (trim to zero crossing)" }
  - { name: "RED", type: knob, value: "play mode", options: ["held", "play-to-end (arrow+line)", "choke group (arrow+G)", "loop"] }
  - { name: "ATTACK", type: knob, value: "start-slope de-click (0 = full volume immediately)" }
  - { name: "Last (brown) knob", type: knob, value: "L/R = slice pan; [Shift]-press = A/B stack-morph" }
---

# Banjo roll — drum-sampler 16-slice carve

## Concept

Drop a single in-time banjo roll loop into the Drum Sampler and let the auto-16-slice (lower keys) + 8-slice (upper) carve it into a playable, choppable kit. Per-slice pitch, choke groups, reverse, and attack turn one banjo phrase into a chromatic/percussive instrument entirely on-box. Distinct from the existing "cuckoo on-box kit" (synthesize-then-sample) and "stereo stacked drums" patches: this is the auto-slice carve of a real banjo capture.

## How to play it

1. Record an in-time 4-bar banjo roll loop (≤20 s) so the auto-slices land on the grid.
2. Go to `[Drum]`; the loop is auto-sliced into **16 lower keys + 8 upper keys** (all referencing the same underlying sample, one start/end per slice).
3. Per slice: set pitch (**BLUE**), trim start/end to zero crossings (**OCHRE** / **GRAY**), choose play mode (**RED**), and raise **ATTACK** to de-click badly-cut slices.
4. Set two hat-like slices to a choke group (**RED** → `arrow+G`) so they cut each other off.
5. Copy a slice (hold key + `[Lift]`) to another key and reverse it (hold key + `[Drop]`); `[Shift]+BLUE` also flips playback direction.

## Notes

- Method-level — **no published knob values**. The Drum-sampler *behavior* (16+8 auto-slice, per-slice BLUE/OCHRE/GRAY/RED, ATTACK, brown-knob pan / A/B morph, reverse) is documented; the exact dial positions for a given banjo loop are yours to set by ear. Treat the controls above as a dialable recipe, not sourced settings.
- Documented Drum-sampler behavior per sonwu, ADG, Cuckoo.
- Field-specific: 20 s record cap; watch for double-compression on sample-in.
- Tagged `designed` = build-method, not a downloadable patch. Save to the `drum/` folder.

## Sources

- Gear/TE OP-1 Field/research/transcripts/sonwu-op1-field-sampler-engine-tutorial.md (§DRUM SAMPLER)
- Gear/TE OP-1 Field/research/transcripts/adg-op1-field-full-walkthrough-for-owners.md (§Drum sampler)
- Gear/TE OP-1 Field/research/OP-1-Field-DeepResearch.md §6 (banjo as drum sampler), §13a
- Transformed from Pedalxly OP-1-Field-Patches.md (DOUG-designed) — method-level, no published values
