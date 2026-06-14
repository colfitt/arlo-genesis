---
type: patch
title: Console Crunch Into The Fuzz Wall
device: JHS Colour Box V2
date: 2026-06-14
description: The single most-used always-on dirty setting in this rig — pre-shapes and tightens the MXR 108 + Hizumitas wall, acting as the fuzz tone-control (and high-pass) the fuzzes don't have.
tags: [always-on, crunch, pre-fuzz, mid-shaping, high-pass, community, signature]
controls:
  - { name: "HI/LO", type: switch, value: "HI", options: ["HI", "LO"] }
  - { name: "STEP", type: knob, value: "2–3 (+23/+28 dB)" }
  - { name: "PRE-VOL", type: knob, value: "12:00" }
  - { name: "MASTER", type: knob, value: "to taste (trim to unity)" }
  - { name: "TREBLE", type: knob, value: "− (~10:00)" }
  - { name: "TREBLE SHIFT", type: knob, value: "~12:00" }
  - { name: "MIDDLE", type: knob, value: "+3..+4 (~2:00)" }
  - { name: "MID SHIFT", type: knob, value: "~12:00 (≈1 kHz presence/cut)" }
  - { name: "BASS", type: knob, value: "modest (~12–1:00)" }
  - { name: "BASS SHIFT", type: knob, value: "noon" }
  - { name: "HI-PASS", type: knob, value: "~10–11:00 (≈120–200 Hz)" }
  - { name: "HI-PASS ON/OFF", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "INST/XLR", type: switch, value: "INST", options: ["INST", "XLR"] }
  - { name: "20 dB PAD", type: switch, value: "off", options: ["on", "off"] }
---

# Console Crunch Into The Fuzz Wall

## Concept
The key rig move. The Colour Box is the fuzz tone control the MXR 108 / EQD Hizumitas don't have — this patch pre-shapes and tightens the fuzz wall before it hits the fuzzes. Boost ~1 kHz for more aggressive, cutting fuzz; scoop it for darker "behind-the-wall" doom. The HI-PASS up to 120–200 Hz is the single best reason it lives before the fuzzes — the Hizumitas Tone can darken but can't high-pass.

## How to play it
1. INST input, **HI** mode. Gain-stage **STEP 2–3 → PRE-VOL noon → MASTER last** (trim to unity).
2. Push the MIDDLE up around 2:00 with MID SHIFT at noon (~1 kHz) for presence that cuts through the wall; pull TREBLE back to tame the ice-pick the 108 would otherwise exaggerate.
3. Engage the HI-PASS toggle and bring the knob up to ~10–11:00 (≈120–200 Hz) to keep the wall tight.
4. Run into the 108 + Hizumitas; trim MASTER to match unity against the clean voice.

## Notes
- Boost ~1 kHz = more aggressive/cutting fuzz; scoop it = darker doom.
- Community-described recipe — clock positions are translated from "console crunch = mid PRE-VOL with mild STEP gain" and "HPF ~100–160 Hz as a pre-fuzz tool."
- This is the rig's defining always-on dirty move.

## Sources
- Produce Like A Pro "crunch + a MID-SHIFT into the low mids → low-mid thickness, classier" (`research/transcripts/produce-like-a-pro-neve-in-a-pedal.md`); WaveInformer "console crunch = mid PRE-VOL with mild STEP gain" + HPF "~100–160 Hz as a pre-fuzz tool" (`research/links/waveinformer-v2-walkthrough.md`); dossier §5/§13(b) (`research/Colour-Box-V2-DeepResearch.md`).
- Transformed from Pedalxly Colour-Box-V2-Patches.md (community).
