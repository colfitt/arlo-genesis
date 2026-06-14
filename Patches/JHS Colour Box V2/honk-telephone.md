---
type: patch
title: Honk / Telephone (mid-stacked radio voice)
device: JHS Colour Box V2
date: 2026-06-14
description: Deliberate "recorded-wrong" telephone/radio voice — set all three EQ SHIFTs to a midrange frequency and boost all three bands as far as possible for a snarly, honking, almost comical mid-forward tone. (Ref: Modest Mouse brittle-jangle / Car Seat Headrest demo-crunch territory.)
tags: [honk, telephone, mid-stack, lo-fi, art-rock, community, signature]
controls:
  - { name: "HI/LO", type: switch, value: "LO (clean honk) or HI (screaming honk into fuzz)", options: ["HI", "LO"] }
  - { name: "STEP", type: knob, value: "2 (+23 dB)" }
  - { name: "PRE-VOL", type: knob, value: "11:00" }
  - { name: "MASTER", type: knob, value: "to taste" }
  - { name: "TREBLE", type: knob, value: "~4–5:00 (max boost)" }
  - { name: "TREBLE SHIFT", type: knob, value: "~7:00 (≈2 kHz, lowest)" }
  - { name: "MIDDLE", type: knob, value: "5:00 (max +10)" }
  - { name: "MID SHIFT", type: knob, value: "~12–1:00 (≈1–1.5 kHz)" }
  - { name: "BASS", type: knob, value: "~4:00" }
  - { name: "BASS SHIFT", type: knob, value: "~5:00 (≈440 Hz, into low-mids)" }
  - { name: "HI-PASS", type: knob, value: "~11:00 (keep it nasal)" }
  - { name: "HI-PASS ON/OFF", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "INST/XLR", type: switch, value: "INST", options: ["INST", "XLR"] }
  - { name: "20 dB PAD", type: switch, value: "off", options: ["on", "off"] }
---

# Honk / Telephone (mid-stacked radio voice)

## Concept
A deliberate "recorded-wrong" telephone/radio voice on banjo, guitar, or synth — or a brutal mid-stack to make the fuzz scream. Maps to the lo-fi cluster's degraded-preamp aesthetic and the art-rock "broken part is the hook" move. Into the 108, the stacked mids make the fuzz cut hard and present.

## How to play it
1. INST input. Pick **LO** for a clean honk or **HI** for a screaming honk into the fuzz.
2. Gain-stage **STEP 2 → PRE-VOL 11:00 → MASTER last** to taste.
3. The trick: set ALL THREE SHIFTs to a midrange frequency and BOOST all three bands as far as possible —
   - TREBLE SHIFT ~7:00 (≈2 kHz, its lowest) + TREBLE ~4–5:00
   - MID SHIFT ~12–1:00 (≈1–1.5 kHz) + MIDDLE 5:00 (max +10)
   - BASS SHIFT ~5:00 (≈440 Hz, into the low-mids) + BASS ~4:00
4. Engage the HI-PASS toggle ~11:00 to keep it nasal.

## Notes
- Community-cited verbatim trick — the EXACT clock translation is mine, since the source gives "midrange + max boost" qualitatively.
- Into the 108 this lands in Modest Mouse brittle-jangle / Car Seat Headrest demo-crunch territory.

## Sources
- WaveInformer signature trick, verbatim: "Set all 3 bands of EQ to a midrange frequency, and boost each of them as much as possible. The resulting sound is a snarly, honking, almost comical mid-forward tone" (`research/links/colour-box-gain-staging-di-technique.md` + `research/links/waveinformer-v2-walkthrough.md`).
- Transformed from Pedalxly Colour-Box-V2-Patches.md (community).
