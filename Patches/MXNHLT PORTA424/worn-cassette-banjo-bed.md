---
type: patch
title: Worn-Cassette Banjo Bed
device: MXNHLT PORTA424
date: 2026-06-14
description: Prints the GK-5 banjo (via VG-800) as a "banjo recorded to a worn cassette" lead voice — a bass shelf plus preamp compression rounds the bright percussive attack and thickens the body so the banjo sits as a lead inside a wall without ice-picking.
tags: [banjo-as-lead, eq-print, worn-cassette, lo-fi, designed, signature]
controls:
  - { name: "Input Trim", type: knob, value: "11 o'clock (warms, doesn't fuzz dense banjo)" }
  - { name: "Treble", type: knob, value: "9–10 o'clock (shelved DOWN, tame the top)" }
  - { name: "Bass", type: knob, value: "1–2 o'clock (shelved UP, thicken body)" }
  - { name: "Channel Fader", type: knob, value: "~75%" }
  - { name: "Master Volume", type: knob, value: "unity" }
  - { name: "Voltage", type: switch, value: "18V (keep transients firm)", options: ["9V", "18V"] }
  - { name: "Placement", type: switch, value: "end of chain", options: ["front of chain", "end of chain"] }
---

# Worn-Cassette Banjo Bed

## Concept
Prints the GK-5 banjo (via VG-800) as a "banjo recorded to a worn cassette" lead voice. The bass shelf plus preamp compression rounds the bright percussive attack and thickens the body so the banjo sits as a lead inside a wall without ice-picking. Banjo-as-lead is a top taste-weighting in this rig.

## How to play it
1. Set Input Trim to 11 o'clock — warms the dense banjo without fuzzing it.
2. Shelve Treble DOWN to 9–10 o'clock to tame the top; shelve Bass UP to 1–2 o'clock to thicken the body.
3. Channel Fader ~75%, Master at unity.
4. Run 18V to keep the percussive transients firm.
5. Mono-sum the bus; place at the end of chain.

## Notes
- The fixed ~100Hz / 10kHz Baxandall shelves are perfect for this whole-strip warm tilt — tilt, don't notch.
- All clock/fader/voltage values are designed-to-spec for the banjo-as-lead taste lens.

## Sources
- Designed for banjo-as-lead per the taste lens; built on the GK-5 banjo source notes (`PORTA424-DeepResearch.md` §6) + the EQ'd-lo-fi-print approach (`PORTA424-UsageGuide.md` §6). Dark-EQ target reinforced by `research/links/guitareffect-sound-like-mkgee-chain.md`.
- Transformed from Pedalxly PORTA424-Patches.md (DOUG-designed)
