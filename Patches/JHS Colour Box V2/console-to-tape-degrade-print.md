---
type: patch
title: Console-to-Tape Degrade Print
device: JHS Colour Box V2
date: 2026-06-14
description: Deliberate degraded print of any source — push the Colour Box into console-crunch (just below full-fuzz), then let PORTA424 / JHS 424 tape-degrade the result → Apollo. The most literal "recorded-wrong" patch; completes the rig's console-to-tape arc.
tags: [console-to-tape, degrade, print, recorded-wrong, lo-fi, designed, signature]
controls:
  - { name: "HI/LO", type: switch, value: "HI", options: ["HI", "LO"] }
  - { name: "STEP", type: knob, value: "3–4 (+28/+33 dB)" }
  - { name: "PRE-VOL", type: knob, value: "1–2:00 (audible crunch, not full fuzz)" }
  - { name: "MASTER", type: knob, value: "trim to unity" }
  - { name: "TREBLE", type: knob, value: "slightly − (pre-tame what tape exaggerates)" }
  - { name: "TREBLE SHIFT", type: knob, value: "to taste" }
  - { name: "MIDDLE", type: knob, value: "+ at ≈1 kHz" }
  - { name: "MID SHIFT", type: knob, value: "~12:00 (≈1 kHz, classier low-mid thickness)" }
  - { name: "BASS", type: knob, value: "modest" }
  - { name: "BASS SHIFT", type: knob, value: "to taste" }
  - { name: "HI-PASS", type: knob, value: "~9–10:00 (≈140–180 Hz)" }
  - { name: "HI-PASS ON/OFF", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "INST/XLR", type: switch, value: "INST (1/4\" → tape) or XLR (→ interface, clean ref)", options: ["INST", "XLR"] }
  - { name: "20 dB PAD", type: switch, value: "off", options: ["on", "off"] }
---

# Console-to-Tape Degrade Print

## Concept
A deliberate degraded print of any source. The Colour Box IS the front of the console, the PORTA424 / JHS 424 ARE the tape at the back — push the Box into console-crunch (audible, but just below full fuzz), then let the 424 stage add the final breakup before the Apollo print. The most literal "recorded-wrong" patch in the rig.

## How to play it
1. INST input, **HI** mode. Gain-stage STEP 3–4 → PRE-VOL 1–2:00 (audible crunch, NOT full fuzz) → MASTER last (trim to unity).
2. Lift MIDDLE around ≈1 kHz (MID SHIFT ~12:00) for the "classier low-mid thickness" move.
3. Pull TREBLE slightly down to pre-tame what the tape will exaggerate; keep BASS modest.
4. Engage HI-PASS ~9–10:00 (≈140–180 Hz).
5. Output 1/4" → into PORTA424 / JHS 424 (tape) → Apollo x8; OR XLR → interface for a parallel clean-console reference track.

## Notes
- **DESIGNED** — the arc is documented; the exact crunch dials are inferred to sit just below full-fuzz so the tape stage adds the final breakup.
- The whole point is to leave headroom for the tape: too much crunch here and there's nothing for the 424 to degrade.

## Sources
- Designed from dossier §4 (tape arc)/§9 "Colour Box = the Neve front end → PORTA424/JHS 424 = the tape at the back → Apollo print; for a deliberate recorded-wrong print, push into console-crunch and let the 424/PORTA424 degrade the result" (`research/Colour-Box-V2-DeepResearch.md`, UsageGuide §4 `research/Colour-Box-V2-UsageGuide.md`); MID-SHIFT low-mid-thickness move from Produce Like A Pro (`research/transcripts/produce-like-a-pro-neve-in-a-pedal.md`).
- Transformed from Pedalxly Colour-Box-V2-Patches.md (designed).
