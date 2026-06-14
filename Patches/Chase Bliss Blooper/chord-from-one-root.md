---
type: patch
title: Chord-from-one-root
device: Chase Bliss Blooper
date: 2026-06-14
description: Build a strummed chord from a single banjo/baritone root note via Chromatic Speed punch-ins — no second instrument; the most rig-defining harmony move.
tags: [pitch, harmony, chromatic-speed, punch-in, factory, signature]
hidden:
  BANK A dip (ALT bank): on
controls:
  - { name: "Mode", type: switch, value: "ADD", options: ["NORM", "ADD", "SAMP"] }
  - { name: "MOD A", type: knob, value: "Chromatic Speed — quantized to the chromatic scale, always in key" }
  - { name: "MOD A slot", type: switch, value: "A1 Chromatic Speed (ALT bank)", options: ["A1", "A2", "A3"] }
  - { name: "MOD A engage", type: button, value: "punch in transposed intervals at different spots (one-shot/punch-in)" }
  - { name: "Slot/Bank", type: knob, value: "MOD A1 ALT bank (requires BANK A dip) · MIDI PC 14" }
---

# Chord-from-one-root

## Concept

Build a strummed chord from a single banjo or baritone root note — no second instrument. Chromatic Speed is quantized to the chromatic scale (always in key), so you can record a loop of root notes and punch in transposed intervals to turn one root into a chord. The single most rig-defining harmony move.

## How to play it

1. In ADD mode, set MOD A to Chromatic Speed (ALT bank A1) — requires the BANK A dip.
2. Record a loop of all root notes.
3. Punch in transposed intervals at different spots — a major 3rd, a 5th, an octave down, and backwards.
4. Use one-shot/punch-in for clean placement.
5. The single-root sequence transforms into strumming through a chord.

## Notes

- Requires firmware v3.0+ (current v3.2) for the ALT bank.
- BANK dip is physical-only, not MIDI-addressable.

## Sources

- `research/transcripts/chase-bliss-blooper-firmware-3-tutorial.md` (official Firmware 3.0 tutorial)
- Transformed from Pedalxly Blooper-Patches.md (factory/artist)
