---
type: patch
title: Filter-House Loop (open/close cutoff sweep)
device: Elektron Digitakt 2
date: 2026-06-14
description: Daft Punk filter-house — one looped figure whose timbre opens/closes over a build (vary the filter, not the notes). Designed-to-emulate.
tags: [filter-house, daft-punk, groove, filter, designed, signature]
controls:
  - { name: "Source", type: switch, value: "A 2-4-bar disco/funk loop (or resample a VG-800/banjo figure) on one track" }
  - { name: "SRC (machine)", type: switch, value: "ONESHOT", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "LOOP", type: switch, value: "ON (track length = loop length so it never changes)", options: ["ON","OFF"] }
  - { name: "FILTER (FX page)", type: switch, value: "multimode FILTER, FREQUENCY low + RESONANCE high-but-not-screaming" }
  - { name: "LFO → filter FREQUENCY", type: switch, value: "WAVE = TRIANGLE, MULT tempo-synced very slow (one cycle over many bars); or p-lock/hand-ride FREQUENCY" }
  - { name: "Bit Reduction", type: knob, value: "a touch (SP-1200 grit)" }
  - { name: "Delay send", type: knob, value: "tempo-synced" }
---

# Filter-House Loop (open/close cutoff sweep)

## Concept
The signature Daft Punk filter-house move on the DT2: one looped figure whose timbre opens and closes over a build by varying the filter, not the notes. A static 2–4-bar loop with the multimode filter low and resonant, swept open by a very-slow tempo-synced triangle LFO (or hand-ridden), with a touch of bit reduction for SP-1200 grit.

## How to play it
1. Load a 2-4-bar disco/funk loop (or resample a VG-800/banjo figure) on one track; SRC ONESHOT, LOOP ON, track length = loop length so it never changes.
2. FX page: multimode FILTER, FREQUENCY low + RESONANCE high-but-not-screaming.
3. LFO → filter FREQUENCY, WAVE = TRIANGLE, MULT tempo-synced very slow (one cycle over many bars) so cutoff opens across the build; or p-lock/hand-ride FREQUENCY for a manual sweep.
4. Add a touch of BIT REDUCTION for SP-1200 grit.
5. Tempo-synced DELAY send.

## Notes
- DT2-E1. All values dial-by-ear; LFO/filter param names manual-authoritative.
- Designed-to-emulate — not a found preset. One loop track; save as a preset.

## Sources
- Ref: Daft Punk 'Around the World'/'Da Funk' filter-house (timbre-variation over a static loop)
- `Research/Taste-Profile/sources/daft-punk-homework-synths-reverbmachine.md`
- `splice-filter-house-techniques.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (designed)
