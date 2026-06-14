---
type: patch
title: Banjo-Into-Fuzz Fixer
device: JHS Colour Box V2
date: 2026-06-14
description: Fakes body into an all-attack EBM-5 banjo (via GK-5 → VG-800) so it survives the fuzz wall as a LEAD voice — the only Board-1 unit that can high-pass AND parametrically fake body before the fuzz.
tags: [banjo, corrective-eq, pre-fuzz, lead, high-pass, designed, signature]
controls:
  - { name: "HI/LO", type: switch, value: "HI", options: ["HI", "LO"] }
  - { name: "STEP", type: knob, value: "2 (+23 dB)" }
  - { name: "PRE-VOL", type: knob, value: "12:00" }
  - { name: "MASTER", type: knob, value: "to taste" }
  - { name: "TREBLE", type: knob, value: "− (~10:00)" }
  - { name: "TREBLE SHIFT", type: knob, value: "~9–10:00 (≈6–10 kHz, hits harshest highs)" }
  - { name: "MIDDLE", type: knob, value: "+2 (~1:00)" }
  - { name: "MID SHIFT", type: knob, value: "~10:00 (≈300–500 Hz, fake low-mid body)" }
  - { name: "BASS", type: knob, value: "+3 (~1–2:00)" }
  - { name: "BASS SHIFT", type: knob, value: "~2:00 (≈300 Hz upper-bass)" }
  - { name: "HI-PASS", type: knob, value: "~8:00 (≈160 Hz, LIGHT)" }
  - { name: "HI-PASS ON/OFF", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "INST/XLR", type: switch, value: "INST", options: ["INST", "XLR"] }
  - { name: "20 dB PAD", type: switch, value: "off", options: ["on", "off"] }
---

# Banjo-Into-Fuzz Fixer

## Concept
The patch that makes the banjo-as-lead-into-fuzz idea actually work. An EBM-5 banjo via GK-5 → VG-800 is all 2–4 kHz attack with almost no body, so it ice-picks through the fuzz wall and disappears. This fakes low-mid body and high-passes the loose lows so the banjo survives the wall as a LEAD voice — the only Board-1 unit that can high-pass AND parametrically fake body before the fuzz.

## How to play it
1. INST input, **HI** mode. Gain-stage **STEP 2 → PRE-VOL noon → MASTER last** to taste.
2. Pull TREBLE down (~10:00) with TREBLE SHIFT swept to ~9–10:00 (≈6–10 kHz) so the cut hits the harshest highs and tames the 2–4 kHz pluck ice-pick.
3. Lift MIDDLE +2 with MID SHIFT ~10:00 (≈300–500 Hz) to fake low-mid body.
4. Add BASS +3 with BASS SHIFT ~2:00 (≈300 Hz upper-bass) for weight without sub-flub.
5. Engage HI-PASS **lightly** (~8:00 / ≈160 Hz) — the banjo has almost no real lows to lose.

## Notes
- **DESIGNED:** no numbered banjo recipe exists anywhere — clock values are synthesis from the documented direction.
- Directly serves the taste lens's "banjo-as-lead" tie-breaker.
- Keep the HI-PASS lighter than the baritone patch — the banjo's lows are mostly absent already.

## Sources
- Designed from dossier §6 "banjo is all 2–4 kHz attack, almost no body → pull TREBLE down (SHIFT toward ~6–10 kHz), boost BASS/low-MID to fake body, engage HI-PASS only lightly" (`research/Colour-Box-V2-DeepResearch.md`) + UsageGuide §6 banjo-into-fuzz fixer (`research/Colour-Box-V2-UsageGuide.md`).
- Transformed from Pedalxly Colour-Box-V2-Patches.md (designed).
