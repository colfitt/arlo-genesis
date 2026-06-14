---
type: patch
title: Baritone Drone Wall Shaper
device: JHS Colour Box V2
date: 2026-06-14
description: Keeps the low B/E of a baritone (Jazzmaster or VG-800 baritone model) from flubbing the fuzz while building a sustained doom wall — STEP 3 slams the 108 for denser sustain, the HPF stops sub-mush from collapsing the wall. (Post-punk / Swans drone-wall translation.)
tags: [baritone, drone, doom, post-punk, pre-fuzz, high-pass, designed, signature]
controls:
  - { name: "HI/LO", type: switch, value: "HI", options: ["HI", "LO"] }
  - { name: "STEP", type: knob, value: "3 (+28 dB, more sustain into the 108)" }
  - { name: "PRE-VOL", type: knob, value: "1:00" }
  - { name: "MASTER", type: knob, value: "trim to unity" }
  - { name: "TREBLE", type: knob, value: "flat-to-slightly-cut" }
  - { name: "TREBLE SHIFT", type: knob, value: "noon" }
  - { name: "MIDDLE", type: knob, value: "+2 (~1:00)" }
  - { name: "MID SHIFT", type: knob, value: "~12:00 (≈1 kHz, cut inside the wall)" }
  - { name: "BASS", type: knob, value: "+slight (~12–1:00)" }
  - { name: "BASS SHIFT", type: knob, value: "~2:00 (≈300 Hz upper-bass body)" }
  - { name: "HI-PASS", type: knob, value: "~10–11:00 (≈140–200 Hz, tighter than banjo)" }
  - { name: "HI-PASS ON/OFF", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "INST/XLR", type: switch, value: "INST", options: ["INST", "XLR"] }
  - { name: "20 dB PAD", type: switch, value: "off", options: ["on", "off"] }
---

# Baritone Drone Wall Shaper

## Concept
A post-punk / Swans drone-wall translation for baritone (Jazzmaster or VG-800 baritone model). STEP 3 adds clean-ish gain that slams the 108 for denser sustain, while the HPF stops the sub-mush from collapsing the wall. Keeps the low B/E from flubbing the fuzz while building a sustained doom wall. Dynamics here are for the BUILD, not for tightness.

## How to play it
1. INST input, **HI** mode. Gain-stage **STEP 3 → PRE-VOL 1:00 → MASTER last** (trim to unity).
2. Lift BASS slightly with BASS SHIFT ~2:00 (≈300 Hz upper-bass body) — leave the sub for the HPF.
3. Lift MIDDLE +2 with MID SHIFT ~12:00 (≈1 kHz) for cut inside the wall.
4. Leave TREBLE flat-to-slightly-cut.
5. Engage HI-PASS at ~10–11:00 (≈140–200 Hz) — tighter than the banjo, the low B needs the most cleanup.

## Notes
- **DESIGNED:** no numbered baritone recipe exists — clock values are synthesis from the documented direction.
- Less corrective EQ than the banjo (baritone is "home territory"); the work is mostly the high-pass plus a mid lift for cut.

## Sources
- Designed from dossier §6 "Baritone: home territory — HI-PASS to keep the low B from flubbing the fuzz, modest mid lift for cut; less corrective EQ than the banjo" (`research/Colour-Box-V2-DeepResearch.md`) + UsageGuide §6 baritone note (`research/Colour-Box-V2-UsageGuide.md`) + taste lens "baritone weight / drone-doom" (`Research/Taste-Profile/taste-profile.md`).
- Transformed from Pedalxly Colour-Box-V2-Patches.md (designed).
