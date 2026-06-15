---
type: patch
title: "Reverse Octave Cascade — every repeat reversed and an octave down"
device: Chase Bliss Blooper
date: 2026-06-15
description: "Andy Othling's recipe — in ADD with the quantized pitch modifier (Stepped Speed) set to 'reverse octave down,' every repeat plays reversed and an octave below the one before it, cascading into a descending, backward sub-drone. It lands on fifths too. From Andy Othling's (Lowercase Noises) Office Hours stream."
tags: [stepped-speed, reverse, pitch, drone, artist]
controls:
  - { name: "Mode", type: switch, value: "ADD (the pitch/reverse step bakes into each repeat)", options: ["NORM", "ADD", "SAMP"] }
  - { name: "MOD B", type: knob, value: "reverse + octave-down — CCW past noon into reverse, stepped to the octave-down interval (set by ear; no published clock position)" }
  - { name: "MOD B slot", type: switch, value: "B4 Stepped Speed (default bank — quantized pitch)", options: ["B4", "B5", "B6"] }
  - { name: "MOD B engage", type: button, value: "arcade button — engage Stepped Speed move" }
  - { name: "REPEATS", type: knob, value: "up (so the cascading repeats accumulate) — dialable, no published clock position" }
  - { name: "STABILITY", type: knob, value: "optional — add for a chorus-y degrade (dialable to taste)" }
  - { name: "Slot/Bank", type: knob, value: "MOD B4 default bank (quantized) · MIDI PC 3 (Stepped-Speed family)" }
---

# Reverse Octave Cascade — every repeat reversed and an octave down

## Concept

Andy Othling's cascade: in ADD with the quantized pitch modifier (Stepped Speed) set to "reverse octave down," every repeat plays reversed and an octave below the one before it. Stacked up, the repeats tumble into a descending, backward sub-drone — and because the step is quantized it lands on fifths as well as octaves, so it stays musical. Andy is careful to distinguish the two pitch modifiers: "modifier one is unquantized octave, four is quantized pitch" — this cascade wants the quantized one (Stepped Speed, B4).

## How to play it

1. Build a loop and set MOD B to Stepped Speed (B4) — the quantized pitch modifier.
2. In ADD mode, set the knob to reverse + octave-down (CCW past noon into reverse, stepped to the octave-down interval).
3. Turn REPEATS up so the cascading repeats accumulate.
4. Each repeat now plays reversed and an octave (or a fifth) below the previous one — a descending, backward sub-drone.
5. Optionally add STABILITY for a chorus-y degrade as the cascade builds.

## Notes

- Use the quantized pitch modifier (Stepped Speed, B4), not the unquantized octave one — Andy: "modifier one is unquantized octave, four is quantized pitch." The cascade comes from the quantized stepping.
- The cascade needs ADD — the pitch/reverse step has to bake into each repeat. In NORM the shift is fixed (one octave, no cascade).
- Honesty flag: exact knob position is not published — set "reverse octave down" by ear (CCW past noon into reverse, then to the octave-down step). It lands on fifths too. REPEATS and STABILITY are dialed from this recipe, not from published values.

## Sources

- 🟣 artist:Andy Othling (Lowercase Noises) — Office Hours stream (id `2oUlQwi4JRo`), via `research/transcripts/andy-othling-office-hours-blooper.md` (reverse fifths/octaves; MOD 4 quantized reverse octave down, verbatim quotes).
