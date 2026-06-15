---
type: patch
title: "Sweep — auto-sweeping synth/filter texture"
device: Roland VG-800
date: 2026-06-15
description: "The factory \"Sweep\" preset Juca Nery tours, built on the synth engine's SWEEP function (SWEEP RISE / SWEEP FALL glide on a pitch/filter change). A swelling, gliding synth texture that morphs as it sounds — drone/pad food that moves on its own."
tags: [synth, sweep, drone, factory, ambient, textural]
dips:
  COMP SW: "ON to extend decay if feeding a sustained texture"
  OUTPUT SELECT: "LINE/PHONES"
controls:
  - { name: "INST TYPE", type: switch, value: "SYNTH" }
  - { name: "SYNTH TYPE", type: switch, value: "GR-300 / SOLO", options: ["GR-300", "SOLO"] }
  - { name: "MODE", type: switch, value: "V+D (or VCO)", options: ["V", "D", "V+D", "VCO"] }
  - { name: "SWEEP SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "SWEEP RISE", type: knob, value: "dial from recipe — 0 = instant; raise for a slow rise (0–100; no published value)" }
  - { name: "SWEEP FALL", type: knob, value: "dial from recipe — 0 = instant; raise for a slow fall (0–100; no published value)" }
  - { name: "COMP SW", type: switch, value: "ON (extends decay so the sweep has time to develop)", options: ["ON", "OFF"] }
  - { name: "Slot/Bank", type: knob, value: "Factory bank (\"Sweep\")" }
---

# Sweep — auto-sweeping synth/filter texture

## Concept

The factory "Sweep" preset Juca Nery tours, built on the synth engine's `SWEEP` function — a `SWEEP RISE` / `SWEEP FALL` glide applied to a pitch/filter change so each note morphs as it sounds. `INST = SYNTH` (GR-300 or SOLO) with `SWEEP SW = ON`: a swelling, gliding synth texture that moves on its own. With longer rise/fall times it becomes drone/pad food that evolves under a single held note — ideal source material for a granular stage.

## How to play it

1. Recall the factory "Sweep" memory, or build: `INST TYPE = SYNTH`, `SWEEP SW = ON`.
2. Set `SWEEP RISE` / `SWEEP FALL` longer for a slow, audible glide on each note (0 = instant).
3. `COMP SW = ON` to extend sustain so the sweep has time to develop.
4. Into Microcosm / Blooper the moving texture becomes self-evolving granular food.

## Notes

- Named factory preset (Juca Nery tour: "Sweep"). `SWEEP SW` / `SWEEP RISE` / `SWEEP FALL` are manual-verified GR-300 synth params (glide time on a PITCH change).
- Exact factory RISE/FALL values are not published — dial from the recipe.
- ⚠ Recipe, not capture: the `SWEEP RISE` / `SWEEP FALL` settings above are dialable starting points, not sourced values. Recall the factory "Sweep" memory and tweak to taste.

## Sources

- 🟢 `research/transcripts/juca-nery-creative-tool-patch-tour.md` (factory-patch tour: "Sweep")
- 🟢 `research/links/parameter-guide-synth-engine-values.md` (SWEEP SW / SWEEP RISE 0–100 / SWEEP FALL 0–100)
- 🟢 `research/transcripts/gear-sounds-full-tutorial.md` (SWEEP switch + SWEEP FALL/RISE on synth)
- Transformed from Pedalxly VG-800-Patches.md (factory)
