---
type: patch
title: Resample the pedalboard fuzz wall
device: TE OP-1 Field
date: 2026-06-15
description: The most rig-native trick — print a fuzz/texture wall from Board 1 to the Apollo, feed an output into the OP-1's 3.5mm line-in, and sample 20s into the Synth sampler so the fuzz wall becomes chromatic across the keys; drive with Tombola/Sketch and bounce to Disc tape for lo-fi (DeepResearch rig workflow + sonwu sampler menu — method-level, no published values).
tags: [sampler, wall, fuzz, shoegaze, texture, designed, signature]
dips:
  SAMPLE_CAP: "20s sampling cap on the Field"
controls:
  - { name: "Sample source (BLUE encoder)", type: switch, value: "LINE-IN (3.5mm; choose stereo)", options: ["mic", "line-in", "ear/tape", "radio"] }
  - { name: "Engine", type: switch, value: "Synth sampler (≤20s)", options: ["Synth Sampler", "Drum Sampler"] }
  - { name: "Recording gain", type: knob, value: "meter peaks high without clipping — dialable, no published value" }
  - { name: "Recording threshold", type: knob, value: "low, to auto-start on the transient — dialable, no published value" }
  - { name: "Drive source", type: switch, value: "Tombola or Sketch sequencer for moving, re-pitched texture" }
  - { name: "Bounce to Disc", type: switch, value: "print to a Disc tape for extra lo-fi, then USB back to Apollo/DAW" }
---

# Resample the pedalboard fuzz wall

## Concept

The most rig-native trick on the board: print a fuzz/texture wall from Board 1 to the Apollo, feed one of its outputs back into the OP-1's 3.5mm line-in, and sample ~20s into the Synth sampler. The fuzz wall is now chromatic across the keys — a playable instrument built from the printed pedalboard. Drive it with Tombola or Sketch for moving, stuttering re-pitched texture, then bounce to a Disc tape for extra lo-fi. Shoegaze / wall-of-texture territory.

## How to play it

1. Print the Board 1 wall to the Apollo; feed an Apollo output back to the OP-1 3.5mm line-in.
2. In the sampling menu, set the sample source to **LINE-IN** (BLUE encoder; choose stereo). Set **recording gain** so the meter peaks high without clipping, and a **low threshold** to auto-start on the transient.
3. Sample **~20s** into the **Synth sampler** — the wall is now chromatic across the keys.
4. Drive with **Tombola** or **Sketch** for moving, stuttering re-pitched texture.
5. Bounce to a **Disc tape** for extra lo-fi, then **USB** back to the Apollo/DAW.

## Notes

- Documented rig workflow (DeepResearch §5/§13d) + documented sampler menu (sonwu). Method-level — **no published knob values**; gain and threshold are a dialable recipe, set by ear/meter.
- Distinct from sampling the banjo — this captures the *printed pedalboard wall* as a playable instrument.
- 20s sampling cap on the Field. Samples are user-captured → tagged designed.

## Sources

- Gear/TE OP-1 Field/research/OP-1-Field-DeepResearch.md §5 (sampling the pedalboard wall), §13d
- Gear/TE OP-1 Field/research/transcripts/sonwu-op1-field-sampler-engine-tutorial.md (§Recording setup — line-in, gain, threshold)
