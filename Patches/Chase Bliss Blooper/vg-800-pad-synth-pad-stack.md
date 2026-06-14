---
type: patch
title: VG-800 pad → synth-pad stack
device: Chase Bliss Blooper
date: 2026-06-14
description: Build a synth-pad stack from one held VG-800 pad note (clean-looping COSM/synth waveforms) via Pitcher ±octave shifts; designed for this rig.
tags: [pitch, harmony, pitcher, pad, designed, signature]
hidden:
  BANK A dip (ALT bank): on
controls:
  - { name: "Mode", type: switch, value: "ADD (so each shift prints)", options: ["NORM", "ADD", "SAMP"] }
  - { name: "MOD A", type: knob, value: "Pitcher — shift ±octaves to build a stack from one held note" }
  - { name: "MOD A slot", type: switch, value: "A2 Pitcher (ALT bank)", options: ["A1", "A2", "A3"] }
  - { name: "Slot/Bank", type: knob, value: "MOD A2 ALT bank (requires BANK A dip) · MIDI PC 14 (shares ALT-A harmony family)" }
---

# VG-800 pad → synth-pad stack

## Concept

Build a synth-pad stack from one held VG-800 pad note. A continuous COSM/synth waveform loops cleanly, so Pitcher can shift it ±octaves to build a layered stack from a single held note.

## How to play it

1. Loop a VG-800 pad (continuous waveform loops cleanly).
2. In ADD mode, set MOD A to Pitcher (ALT bank A2) — requires the BANK A dip.
3. Pitcher-shift the loop ±octaves to build a stack from one held note.
4. ADD mode means each shift prints into the wall.

## Notes

- Pitcher and Stretcher are DSP-heavy and mutually exclusive — plan one per loop.
- Pitcher behavior is cited; the VG-800 application is designed for this rig.

## Sources

- designed from `research/Blooper-DeepResearch.md` §6
- Transformed from Pedalxly Blooper-Patches.md (designed)
