---
type: patch
title: Broken Console Preamp Fuzz
device: JHS Colour Box V2
date: 2026-06-14
description: "Pure \"recorded-wrong\" console-fuzz — splatty, gated, self-compressing solid-state-into-transformer ugliness, with the EQ flat so the preamp distortion is the whole sound. (Ref: Beatles \"Revolution\" / Nirvana \"Territorial Pissings\" direct-in.)"
tags: [fuzz, broken-console, doom, shoegaze, lo-fi, factory, artist, signature]
controls:
  - { name: "HI/LO", type: switch, value: "HI", options: ["HI", "LO"] }
  - { name: "STEP", type: knob, value: "5 (+39 dB, max)" }
  - { name: "PRE-VOL", type: knob, value: "5:00 (maxed)" }
  - { name: "MASTER", type: knob, value: "9–10:00 (pull WAY back)" }
  - { name: "TREBLE", type: knob, value: "noon/flat to start" }
  - { name: "TREBLE SHIFT", type: knob, value: "noon" }
  - { name: "MIDDLE", type: knob, value: "noon/flat to start" }
  - { name: "MID SHIFT", type: knob, value: "noon" }
  - { name: "BASS", type: knob, value: "noon/flat to start" }
  - { name: "BASS SHIFT", type: knob, value: "noon" }
  - { name: "HI-PASS", type: knob, value: "~11:00 (≈160 Hz, tighter overload)" }
  - { name: "HI-PASS ON/OFF", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "INST/XLR", type: switch, value: "INST", options: ["INST", "XLR"] }
  - { name: "20 dB PAD", type: switch, value: "off", options: ["on", "off"] }
---

# Broken Console Preamp Fuzz

## Concept
Genuine broken-console fuzz on guitar, baritone, or VG-800 — splatty, gated, self-compressing solid-state-into-transformer ugliness. This is the lo-fi/post-punk "recorded-wrong" aesthetic as a feature: STEP maxed, PRE-VOL maxed, EQ flat gives full-blown pure preamp distortion with no amp. Premier Guitar called it "blistering solid-state fuzz with anarchic pumping/gulping."

## How to play it
1. INST input, **HI** mode. Set **STEP 5** (max) and **PRE-VOL 5:00** (maxed).
2. **Set MASTER LAST** — pull it WAY back to 9–10:00. This is the biggest volume jump on the pedal.
3. Start with all EQ bands at noon/flat ("pure preamp distortion, no warmth until you EQ"), then dial BASS/MID to taste.
4. Engage the HI-PASS toggle, knob ~11:00 (≈160 Hz), for a tighter overload.
5. Run standalone (bypass the fuzzes) or stack into the 108 for a wall-of-wall, then into PORTA424 / JHS 424 → Apollo for the full console-to-tape degrade.

## Notes
- **WARNING:** biggest volume jump on the pedal — always set MASTER last.
- EQ flat = the rawest preamp clip; add BASS/MID only after the level is tamed.
- Source gives this verbatim, so the gain-staging values are exact, not translated.

## Sources
- Produce Like A Pro, verbatim: "STEP 5 max, PRE-VOL maxed, EQ flat → full-blown pure preamp distortion, no amp; flip HI + engage HIGH-PASS for a tighter overload" (`research/transcripts/produce-like-a-pro-neve-in-a-pedal.md`). Premier Guitar "blistering solid-state fuzz with anarchic pumping/gulping" (`research/links/neve-direct-in-recording-history.md`); WaveInformer "fuzz chaos — HI, STEP 5th, cranked PRE-VOL — blistering, gated, gnarly" (`research/links/waveinformer-v2-walkthrough.md`).
- Transformed from Pedalxly Colour-Box-V2-Patches.md (factory/artist).
