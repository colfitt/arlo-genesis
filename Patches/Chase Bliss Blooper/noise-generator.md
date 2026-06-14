---
type: patch
title: Noise Generator
device: Chase Bliss Blooper
date: 2026-06-14
description: Turn Blooper into a no-input instrument — record its own Stability noise floor as raw drone material, then slow/filter/modify the captured noise.
tags: [degrade, noise, no-input, drone, factory, signature]
controls:
  - { name: "Mode", type: switch, value: "ADD", options: ["NORM", "ADD", "SAMP"] }
  - { name: "STABILITY", type: knob, value: "turned up (captures noise into the loop)" }
  - { name: "MOD B", type: knob, value: "optional Filter (B6) to shape the captured noise" }
  - { name: "MOD B slot", type: switch, value: "B6 Filter (optional)", options: ["B4", "B5", "B6"] }
  - { name: "Slot/Bank", type: knob, value: "STABILITY (+ optional Filter B6) · MIDI PC 8" }
---

# Noise Generator

## Concept

Turn Blooper into a no-input instrument — record its own noise floor as raw drone material, banjo not even plugged in. Stability injects noise that gets captured into the loop, giving you a white-noise soundtrack to then slow down, filter, and modify.

## How to play it

1. In ADD mode, record a layer of silence.
2. Turn STABILITY up.
3. Record an overdub — Blooper captures the noise from Stability into the loop.
4. Slow it down, filter it, or otherwise modify the captured noise.

## Notes

- A from-nothing drone underlay. Filter it dark downstream, or pitch it down with Pitcher for a sub-rumble bed.

## Sources

- `research/links/blooper-manual-named-patches-dip-recipes.md` (manual p.33)
- Transformed from Pedalxly Blooper-Patches.md (factory/artist)
