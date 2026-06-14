---
type: patch
title: Baritone sub-drone doom
device: Chase Bliss Blooper
date: 2026-06-14
description: Instant doom thickness on a sustained baritone chord — sub-drones tuned to fifths/octaves via Stepped Speed octave-down, no second instrument; designed for this rig from cited Stepped Speed behavior.
tags: [drone, doom, sub-drone, octave-down, designed, signature]
controls:
  - { name: "Mode", type: switch, value: "NORM (capture) → ADD (overdub)", options: ["NORM", "ADD", "SAMP"] }
  - { name: "STABILITY", type: knob, value: "~10 o'clock" }
  - { name: "REPEATS", type: knob, value: "max" }
  - { name: "MOD B", type: knob, value: "octave-down (quantizes to octaves/fifths; CCW = reverse, CW = forward)" }
  - { name: "MOD B slot", type: switch, value: "B4 Stepped Speed", options: ["B4", "B5", "B6"] }
  - { name: "Slot/Bank", type: knob, value: "MOD B4 default bank + STABILITY · MIDI PC 3" }
---

# Baritone sub-drone doom

## Concept

Instant doom thickness on a sustained baritone chord. Stepped Speed quantizes to octaves and fifths, so an octave-down setting drops sub-drones tuned beneath the chord — no second instrument needed. Combine with the Accumulator approach (mild modifier left running, STABILITY climbing) for the literal sound of a drone collapsing over minutes.

## How to play it

1. Capture a sustained baritone chord (post-Hizumitas/Longsword wall) in NORM.
2. Drop to playback, then overdub in ADD with MOD B set to Stepped Speed (B4).
3. Set Stepped Speed octave-down — CCW for reverse, CW for forward.
4. Set STABILITY ~10 o'clock and REPEATS max.
5. Let the mild modifier run with STABILITY climbing for a slow collapse.

## Notes

- Stepped Speed's octave/fifth quantizing behavior is cited (KNOBs); the baritone-doom application is designed for this rig.

## Sources

- designed from `research/Blooper-DeepResearch.md` §6 + `research/transcripts/knobs-better-bloops-modifiers.md`
- Transformed from Pedalxly Blooper-Patches.md (designed)
