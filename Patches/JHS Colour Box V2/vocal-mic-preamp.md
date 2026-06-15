---
type: patch
title: Vocal / Mic Preamp (Neve channel strip)
device: JHS Colour Box V2
date: 2026-06-14
description: "Track vocals / room mics / amp mics through the Colour Box as a Neve-flavored channel strip into the Apollo — PRE-VOL low for a clean breathy take, nudge HI for a degraded/lo-fi vocal. (Ref: Tape Op M160 ribbon vocal, Gene Clark \"No Other\" character.)"
tags: [vocal, mic-preamp, channel-strip, indie-folk, lo-fi, factory, artist]
controls:
  - { name: "HI/LO", type: switch, value: "LO (clean) or HI (overdriven vocal)", options: ["HI", "LO"] }
  - { name: "STEP", type: knob, value: "1–2 (+18/+23 dB)" }
  - { name: "PRE-VOL", type: knob, value: "9–10:00 (clean) up to 1:00+ (overdriven)" }
  - { name: "MASTER", type: knob, value: "set level" }
  - { name: "TREBLE", type: knob, value: "tame buzz to taste" }
  - { name: "TREBLE SHIFT", type: knob, value: "to taste" }
  - { name: "MIDDLE", type: knob, value: "cut some MID" }
  - { name: "MID SHIFT", type: knob, value: "to taste" }
  - { name: "BASS", type: knob, value: "+ for body" }
  - { name: "BASS SHIFT", type: knob, value: "to taste" }
  - { name: "HI-PASS", type: knob, value: "~9:00 (clean rumble)" }
  - { name: "HI-PASS ON/OFF", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "INST/XLR", type: switch, value: "XLR (out → interface)", options: ["INST", "XLR"] }
  - { name: "20 dB PAD", type: switch, value: "ON for a hot mic (SM7/condenser), off for quiet ribbons", options: ["on", "off"] }
---

# Vocal / Mic Preamp (Neve channel strip)

## Concept
Track vocals, room mics, or amp mics through the Colour Box as a Neve-flavored channel strip into the Apollo. Indie-folk cluster (intimate close-mic'd vocal): PRE-VOL low gives the clean breathy take; nudge HI for a degraded/lo-fi vocal that fits the recorded-wrong aesthetic.

## How to play it
1. Flip **INST/XLR to XLR**. Engage the **PAD ON** for a hot mic (SM7/condenser), off for quiet ribbons. Phantom passes through for condensers.
2. **LO** for clean, **HI** for an overdriven vocal. STEP 1–2.
3. PRE-VOL 9–10:00 for "clean as a whistle," up to 1:00+ for an overdriven vocal; set MASTER to level.
4. Engage HI-PASS ~9:00 to clean rumble; cut some MID, use TREBLE to tame buzz, lift BASS for body.
5. XLR out → interface (lower noise floor than 1/4").

## Notes
- The XLR out is **dead when the pedal is bypassed** (in INST mode), so confirm the pedal is engaged.
- Check the INST/XLR switch first — wrong input = total silence.

## Sources
- Produce Like A Pro "SM7 → XLR input — PRE-VOL up = overdriven vocal; PRE-VOL down = clean as a whistle with lots of low end" (`research/transcripts/produce-like-a-pro-neve-in-a-pedal.md`); Jorb ran a Wurlitzer via SM57 as a mic pre (`research/transcripts/jorb-multi-instrument.md`); Tape Op Beyerdynamic M160 ribbon vocal (`research/links/colour-box-tapeop-engineer-di.md`).
- Transformed from Pedalxly Colour-Box-V2-Patches.md (factory/artist).
