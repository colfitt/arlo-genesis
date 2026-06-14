---
type: patch
title: DUAL Fake Chorus (no modulation pedal)
device: Roland VG-800
date: 2026-06-14
description: Wide doubled clean for the stereo split — chorus without a chorus block.
tags: [dual-guitar, chorus, width, community]
controls:
  - { name: "INST TYPE", type: switch, value: "DUAL GUITAR" }
  - { name: "Guitar A / B model", type: switch, value: "same model, slightly different tuning" }
  - { name: "A: FINE (all strings)", type: knob, value: "+5 (via ALT TUNE USER)" }
  - { name: "B: FINE (all strings)", type: knob, value: "-5 (via ALT TUNE USER)" }
  - { name: "A:/B: STR DELAY", type: knob, value: "5–20 ms apart per string (0–100 ms range)" }
  - { name: "ALT TUNE SW", type: switch, value: "ON (required for STR DELAY to apply)", options: ["ON", "OFF"] }
  - { name: "Per-string LEVEL", type: knob, value: "balanced" }
  - { name: "Pan", type: knob, value: "A left / B right" }
  - { name: "Slot/Bank", type: knob, value: "User Memory (guitar mode), e.g. U05-2" }
---

# DUAL Fake Chorus (no modulation pedal)

## Concept

A wide doubled clean for the stereo split — chorus without a chorus block. Two copies of the same model, one tuned slightly sharp and one slightly flat (and/or with the per-string sound delayed), panned hard, fake a chorus the same way a 12-string is faked: "delay the string sound of one to simulate a 12-string" (manual).

## How to play it

1. Set `INST TYPE = DUAL GUITAR`. Use the same model for A and B.
2. Detune them: A `FINE` all +5, B `FINE` all -5 (via `ALT TUNE USER`), and/or set `A:/B: STR DELAY` 5–20 ms apart per string.
3. `ALT TUNE SW` must be ON for STR DELAY to apply.
4. Balance the per-string `LEVEL`.
5. Pan A left / B right.

## Notes

- Method is video-sourced (Gear Sounds: "the most useful function of the pedal — the alternate tunings"); the `A:/B: STR DELAY 0–100 ms` mechanism is manual-sourced. Numbers are designed starting points.

## Sources

- 🔵 `research/transcripts/gear-sounds-how-to-create-patch.md` (https://www.youtube.com/watch?v=7JWBcjFbTg8); STR DELAY from parameter-guide-alt-tuning-values.md
- Transformed from Pedalxly VG-800-Patches.md (community)
