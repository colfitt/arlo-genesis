---
type: patch
title: "Endless — chromatic one-shot (one-note instrument)"
device: TE OP-1 Field
date: 2026-06-15
description: "Load a single note into the Endless sequencer and any one-shot becomes playable chromatically across the keys — the documented way to turn a banjo roll, cymbal scrape, or fuzz-wall hit into a melodic instrument. The mechanical backbone behind the Bon Iver 'cymbal that sings' move. Community/demo technique (ratbag98, digiphex) — method-level, no published values."
tags: [sampler, chromatic, endless, capture-and-mangle, designed, signature]
controls:
  - { name: "Engine", type: switch, value: "Sampler / Drum sampler (holding the one-shot)", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Sequencer", type: switch, value: "Endless ([Shift]+[Sequencer])" }
  - { name: "Note entry", type: button, value: "[Shift]+key — enter a SINGLE note; arrows for rests" }
  - { name: "Play", type: button, value: "play across the keys to re-pitch the one-shot chromatically" }
  - { name: "FX (to taste)", type: knob, value: "Porta / Vintage tape or Mother reverb — no published values" }
---

# Endless — chromatic one-shot (one-note instrument)

## Concept

Load a single note into the Endless sequencer and any one-shot becomes playable chromatically across the keys — the documented way to turn a banjo roll, cymbal scrape, or fuzz-wall hit into a melodic instrument. It's the mechanical backbone behind the Bon Iver "cymbal that sings" move: the artist concept is "sample a gesture and play it pitched," and Endless with a single entered note is the on-box mechanism that realizes it.

## How to play it

1. Sample a one-shot (banjo roll, cymbal scrape, fuzz-wall hit) into the **Sampler / Drum sampler**.
2. `[Shift]+[Sequencer]` → **Endless**.
3. Hold `[Shift]` and enter a **SINGLE** note into the sequence (use arrows for rests).
4. Play the keyboard — the one-shot fires chromatically at every pitch.
5. Add **Porta / Vintage tape** or **Mother reverb** to taste.

## Notes

- Documented technique (ratbag98; Endless capacity per loopop). Method-level — no knob values exist for this; treat the FX line as a dialable recipe.
- Engine behind Bon Iver's "sampled cymbal scrape played at different pitches."
- Distinct from the existing cymbal-scrape patch: that one is the artist concept; this is the on-box Endless mechanism that realizes it.

## Sources

- Gear/TE OP-1 Field/research/links/github-ratbag98-op1tips-distilled.md (§Chromatic drum hits via Endless)
- Gear/TE OP-1 Field/research/transcripts/digiphex-op1-field-sequencers-tutorial.md (§ENDLESS)
- Gear/TE OP-1 Field/research/OP-1-Field-UsageGuide.md §1 (Endless one-shot chromatic)
