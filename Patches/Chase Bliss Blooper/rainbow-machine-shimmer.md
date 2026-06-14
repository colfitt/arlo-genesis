---
type: patch
title: Rainbow Machine shimmer
device: Chase Bliss Blooper
date: 2026-06-14
description: Shimmer that cascades up octave by octave each repeat (or down for a sub-drone) via Stepped Speed in ADD on a delay base; Andy Othling's livestream move.
tags: [pitch, shimmer, octave, delay, ambient, artist, signature]
controls:
  - { name: "Mode", type: switch, value: "ADD", options: ["NORM", "ADD", "SAMP"] }
  - { name: "REPEATS", type: knob, value: "up (delay base); raise for more cascade" }
  - { name: "MOD B", type: knob, value: "octave-up = cascade up (shimmer); octave-down = cascade into sub-drone" }
  - { name: "MOD B slot", type: switch, value: "B4 Stepped Speed (quantized octave)", options: ["B4", "B5", "B6"] }
  - { name: "STABILITY", type: knob, value: "added for a chorus-y quality" }
  - { name: "MOD B (Filter)", type: knob, value: "optional Filter (B6) to darken each pass" }
  - { name: "Slot/Bank", type: knob, value: "MOD B4 default + STABILITY + optional Filter B6 · MIDI PC 3 (shares Stepped-Speed family)" }
---

# Rainbow Machine shimmer

## Concept

Shimmer that cascades up octave by octave each repeat — or down for a sub-drone. Set Blooper as a delay and use Stepped Speed (the quantized octave, which Andy distinguishes from A1's unquantized octave) in ADD so the shift cascades. In NORM the shift is fixed with no cascade; ADD makes it cascade.

## How to play it

1. In ADD mode, set Blooper as a delay (REPEATS up).
2. Set MOD B to Stepped Speed (B4): octave-up so each repeat cascades up (shimmer), or octave-down to cascade into a sub-drone.
3. Add STABILITY for a chorus-y quality.
4. Raise REPEATS for more of the cascade.
5. Optionally stack Filter (B6) to darken each pass.

## Notes

- Knob positions are relative (from Andy's livestream).
- The reverse-fifths/octaves variant gives a descending reversed drone.

## Sources

- `research/transcripts/andy-othling-office-hours-blooper.md`
- Ref: Andy Othling (Lowercase Noises)
- Transformed from Pedalxly Blooper-Patches.md (factory/artist)
