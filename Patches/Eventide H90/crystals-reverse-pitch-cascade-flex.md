---
type: patch
title: "Crystals — Reverse Pitch Cascade (FLEX lift)"
device: Eventide H90
date: 2026-06-15
description: "Twin REVERSE pitch shifters + delay + feedback + reverb that bloom into climbing, cascading granular swells — the signature backwards, glassy Eventide texture for ambient intros/outros, and a great wet-only super-algorithm A slot (Crystals 100% into a distortion algorithm). Composition (twin reverse shifters + delays + feedback + reverb) and FLEX are from the manual + Algorithm Guide; Leon Todd contributes the Crystals -> distortion wet-only combo. Exact factory values not published — dial from the recipe."
tags: [crystals, pitch, reverse, granular, ambient, cascade, shimmer]
controls:
  - { name: "Preset A Algorithm", type: switch, value: "Crystals (twin reverse pitch shifters + delays + feedback + reverb)" }
  - { name: "Pitch Shift A", type: knob, value: "+12 (octave up) — dial to song", options: ["cents, e.g. +1200 (octave), +700 (5th)"] }
  - { name: "Pitch Shift B", type: knob, value: "+7 (5th) or +12 (octave) for a climbing stack — dial to song", options: ["cents, e.g. +1200 (octave), +700 (5th)"] }
  - { name: "Pitch A Mix", type: knob, value: "balance voice A (dial to song)" }
  - { name: "Pitch B Mix", type: knob, value: "balance voice B (dial to song)" }
  - { name: "Reverse Delay Buffer A", type: knob, value: "tempo-synced (e.g. 1/4 or 1/2)", options: ["tempo-syncable note divisions or ms"] }
  - { name: "Reverse Delay Buffer B", type: knob, value: "tempo-synced (e.g. 1/4 or 1/2)", options: ["tempo-syncable note divisions or ms"] }
  - { name: "Feedback A", type: knob, value: "moderate — raise for a climbing cascade (dial to song)" }
  - { name: "Feedback B", type: knob, value: "moderate — raise for a climbing cascade (dial to song)" }
  - { name: "Reverb Mix", type: knob, value: "up for a bigger cloud (dial to song)" }
  - { name: "Reverb Decay", type: knob, value: "long for sustained swells (dial to song)" }
  - { name: "Program Mix", type: knob, value: "blend the wet cloud under dry (use for the wet-only -> distortion trick)" }
  - { name: "FLEX", type: button, value: "press-and-hold to lift both voices up one octave for a build" }
---

# Crystals — Reverse Pitch Cascade (FLEX lift)

## Concept
Twin REVERSE pitch shifters running into delay, feedback and reverb that bloom into climbing, cascading granular swells — the signature backwards, glassy Eventide texture. Great for ambient intros and outros, and a strong wet-only super-algorithm in the A slot: run Crystals 100% wet into a distortion algorithm so the backwards cloud gets crushed and re-voiced. Pitch A at the octave and Pitch B a 5th (or another octave) stacks a climbing harmony; FLEX lifts the whole cloud an octave on demand for a build.

## How to play it
1. Load **Crystals** on Preset A.
2. Set the **Reverse Delay Buffer A/B** tempo-synced (e.g. 1/4 or 1/2).
3. Dial **Pitch A +12** (octave) and **Pitch B +7** (5th) or **+12** for a climbing stack.
4. Add **Feedback A/B** for cascading repeats and raise **Reverb Mix / Decay** to grow the cloud.
5. Hit **FLEX** to lift everything an octave for a build — or run Crystals 100% wet into a distortion algorithm and blend under dry with **Program Mix** (the wet-only super-algorithm trick).

## Notes
- The composition (twin reverse pitch shifters + delays + feedback + reverb) and the FLEX octave-lift are from the manufacturer manual + Algorithm Guide; **exact factory values are not published — treat the control values here as a dialable recipe, not sourced settings.**
- Leon Todd explicitly suggests **Crystals -> distortion** as a wet-only super-algorithm pair: put Crystals 100% wet in front of a distortion algorithm and blend it under the dry with Program Mix.
- No named factory presets for this in the manual — build from the recipe.
- For the End board, this lives well as a wet-only A slot feeding the distortion combo above.

## Sources
- https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/algorithms/pitch.html (Crystals: twin reverse pitch shifters + delays + feedback + reverb; FLEX shifts both voices up an octave)
- research/H90-DeepResearch.md §3 (Crystals — Algorithm Guide §10, manuals/EventideH90.pdf)
- research/transcripts/leon-todd-h90-routing-trick-wet-only-superalgorithm.md (Crystals -> distortion combo)
- Provenance: manufacturer manual + Algorithm Guide + Leon Todd combo — composition/FLEX published, no values
