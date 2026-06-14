---
type: patch
title: Cassette Fatten
device: Strymon Deco V2
date: 2026-06-14
description: Fattening the low-output GK-5/EBM-5 banjo and baritone sources — cassette ALC adds roundness, grit and low end where single-coil/modeled pickups are thin (Superdanger Studios clean-boost recipe).
tags: [tape-warmth, cassette, fatten, boost, factory, signature]
controls:
  - { name: "Tape Saturation", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "Doubletracker", type: switch, value: "OFF", options: ["ON","OFF"] }
  - { name: "Voice", type: switch, value: "cassette", options: ["classic","cassette"] }
  - { name: "Saturation", type: knob, value: "~12:00 (knobs roughly at noon)" }
  - { name: "Tone", type: knob, value: "12:00 (roll dark for banjo)" }
  - { name: "Volume", type: knob, value: "unity-to-slightly-hot for a solo lift" }
  - { name: "Slot/Bank", type: knob, value: "PC11" }
---

# Cassette Fatten

## Concept
Cassette mode, knobs roughly at noon, used as a clean boost / fattening voice. The cassette ALC adds roundness, grit, low end and a touch of compression where low-output GK-5/EBM-5 banjo and baritone sources read thin. A subtle refinement, not night-and-day lo-fi — that lo-fi ruin is the End-Board's job.

## How to play it
1. Engage Tape Saturation only; Doubletracker off.
2. Set Voice to cassette, Saturation ~12:00, Tone ~12:00 (roll darker for banjo).
3. Push Volume unity-to-slightly-hot for a solo lift.
4. If cassette over-compresses against the dirt stack downstream, switch Voice to classic.

## Notes
- Two independent V2-confirmed sources prefer cassette as the fattening voice.
- Cassette compresses more than classic — back off if it squashes the source against the dirt stack.
- Gain device: level-match on engage.

## Sources
- transcripts/superdanger-one-pedal-endless-tone-deco-v2.md ("Cassette mode, knobs roughly at noon… clean boost"; "Cassette adds a lot more grit, low end, compresses a lot more")
- transcripts/kaleidoscope (cassette "fattens it up / more compressed"); UsageGuide §1
- Ref: Superdanger Studios "One Pedal, Endless Tone" (gxS7ueTq6_I)
- Transformed from Pedalxly Deco-V2-Patches.md (factory/artist)
