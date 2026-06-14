---
type: patch
title: Hidden Noise-Floor Tames (Hiss + Mechanical Noise)
device: Chase Bliss Generation Loss
date: 2026-06-14
description: The real fix for the universally-flagged "hiss is too aggressive" complaint — and keeping a clean noise floor before the downstream cassette print.
tags: [utility, noise, hiss, hidden, factory, signature]
dips:
  HUM BYP: on
hidden:
  Hiss Level (Flutter knob): turn down to kill hiss
  Mechanical-Noise Level (Saturate knob): noon=0, CW=hum, CCW=VCR noise
  Crinkle/Pop (Failure knob): to taste
  Aux Onset (Wow knob): to taste
  Input Gain (Dry toggle): Line (for the VG-800's near-line output)
  Bypass Type (Model knob): CW=clickless DSP / CCW=true bypass
controls:
  - { name: "Noise", type: switch, value: "off (leave off by default)", options: ["off", "on"] }
---

# Hidden Noise-Floor Tames (Hiss + Mechanical Noise)

## Concept
The real fix for the universally-flagged "hiss is too aggressive" complaint, and the way to keep a clean noise floor before the downstream cassette print. These are global hidden settings that persist across presets.

## How to play it
1. Hold both footswitches until the LEDs go green to enter the hidden menu.
2. **Hiss Level = Flutter knob** — turn down to kill hiss.
3. **Mechanical-Noise Level = Saturate knob** — noon=0, CW=hum, CCW=VCR noise.
4. **Crinkle/Pop = Failure**, **Aux Onset = Wow** — set to taste.
5. **Input Gain = Dry toggle** — set **Line** for the VG-800's near-line output.
6. **Bypass Type = Model** — CW=clickless DSP / CCW=true bypass.

## Notes
- For this rig: keep hidden **Hiss low + HUM BYP** so you don't stack two noise floors into the PORTA424 tape stage.
- Leave the Noise toggle **off** by default.
- Hidden settings persist across presets (global).

## Sources
- 🟢 `research/transcripts/kevwyxin-read-the-manual-part2-advanced-dips-hidden.md` + DeepResearch §2 + UsageGuide §1 + `research/transcripts/chasebliss-official-video-manual.md`.
- Transformed from Pedalxly Generation-Loss-Patches.md (factory/artist provenance).
