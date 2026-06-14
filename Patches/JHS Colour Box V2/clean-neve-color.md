---
type: patch
title: Clean Neve Color
device: JHS Colour Box V2
date: 2026-06-14
description: The always-on home-base voice the whole fuzz wall is built through — Neve direct-in console color that makes a DI'd source sound recorded, not plugged-in. (Ref: Neve 1073 direct-in; Mac DeMarco V1 / Black Pumas Eric Burton V2 verified users.)
tags: [always-on, clean, console-color, neve, baseline, factory, artist]
controls:
  - { name: "HI/LO", type: switch, value: "LO", options: ["HI", "LO"] }
  - { name: "STEP", type: knob, value: "1 (+18 dB)" }
  - { name: "PRE-VOL", type: knob, value: "9:00" }
  - { name: "MASTER", type: knob, value: "1–2:00 (set to unity)" }
  - { name: "TREBLE", type: knob, value: "+slight (~1:00)" }
  - { name: "TREBLE SHIFT", type: knob, value: "~2:00 (≈8 kHz air)" }
  - { name: "MIDDLE", type: knob, value: "flat (noon)" }
  - { name: "MID SHIFT", type: knob, value: "noon" }
  - { name: "BASS", type: knob, value: "+slight (~1:00)" }
  - { name: "BASS SHIFT", type: knob, value: "~10:00 (≈120 Hz weight)" }
  - { name: "HI-PASS", type: knob, value: "~7–8:00 (≈60–80 Hz) if engaged" }
  - { name: "HI-PASS ON/OFF", type: switch, value: "OFF", options: ["ON", "OFF"] }
  - { name: "INST/XLR", type: switch, value: "INST", options: ["INST", "XLR"] }
  - { name: "20 dB PAD", type: switch, value: "off (N/A on INST)", options: ["on", "off"] }
---

# Clean Neve Color

## Concept
The "home base" always-on voice the entire rig is voiced through — guitar, banjo, or baritone via VG-800. Even "clean" isn't sterile: transformer weight plus a forward mid makes a DI'd source sound *recorded*, not plugged-in. Bypassing it makes the front end brighter, looser, and less mid-forward, so this engaged tone is the reference everything downstream is judged against.

## How to play it
1. Set the input to **INST** and confirm signal (wrong input = total silence).
2. Gain-stage in order: **STEP 1** (coarse) → **PRE-VOL 9:00** (drive) → **MASTER 1–2:00** last (trim back to unity, leaving room to claw back).
3. Dial the subtle EQ: a touch of TREBLE with SHIFT up near 8 kHz for air; MIDDLE flat at noon; a touch of BASS with SHIFT down near 120 Hz for weight.
4. Leave HI-PASS toggled OFF for the full body; flip it on (~7–8:00) only if you need to clean rumble.

## Notes
- Every EQ band is flat/bypassed at its noon detent, so the noon MIDDLE is effectively out of circuit.
- Clock values are a **translation** of WaveInformer's described "LO + subtle EQ" recipe — the source describes, it does not number.
- Sits 4th on Board 1, before the MXR 108 + EQD Hizumitas fuzz wall — "always-on when able."

## Sources
- WaveInformer "Clean Neve preamp — hi-fi and pristine with subtle analog coloration" (`research/links/waveinformer-v2-walkthrough.md`) + dossier §13(a) (`research/Colour-Box-V2-DeepResearch.md`); artists per `research/links/colour-box-artist-vs-technique.md`.
- Transformed from Pedalxly Colour-Box-V2-Patches.md (factory/artist).
