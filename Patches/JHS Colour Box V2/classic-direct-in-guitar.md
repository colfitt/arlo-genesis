---
type: patch
title: Classic Direct-In Guitar (parallel DI + mic'd amp)
device: JHS Colour Box V2
date: 2026-06-14
description: Recreate documented direct-into-Neve guitar records — present "direct" character blended with a mic'd amp's weight via parallel outs. (Ref: Beatles "Revolution," Nirvana "Territorial Pissings," ZZ Top "Fool for Your Stockings," Pink Floyd "Another Brick Pt.2," Byrds "Mr. Tambourine Man" — documented direct-in TECHNIQUE, not verified pedal owners.)
tags: [guitar, direct-in, parallel-di, neve, technique, factory]
controls:
  - { name: "HI/LO", type: switch, value: "LO (verge of breakup) or HI (Revolution raunch)", options: ["HI", "LO"] }
  - { name: "STEP", type: knob, value: "2 (+23 dB)" }
  - { name: "PRE-VOL", type: knob, value: "11:00 (clean) to 1:00 (grit)" }
  - { name: "MASTER", type: knob, value: "to unity" }
  - { name: "TREBLE", type: knob, value: "flat baseline, touch high-mid to push forward" }
  - { name: "TREBLE SHIFT", type: knob, value: "to taste" }
  - { name: "MIDDLE", type: knob, value: "+2 (for a thin bridge pickup)" }
  - { name: "MID SHIFT", type: knob, value: "≈300 Hz (low-mids)" }
  - { name: "BASS", type: knob, value: "with a little BASS SHIFT" }
  - { name: "BASS SHIFT", type: knob, value: "to taste" }
  - { name: "HI-PASS", type: knob, value: "~9:00 for the grittier tone" }
  - { name: "HI-PASS ON/OFF", type: switch, value: "OFF (jangle) / ON (grittier)", options: ["ON", "OFF"] }
  - { name: "INST/XLR", type: switch, value: "INST (parallel: 1/4\" → amp + XLR → interface)", options: ["INST", "XLR"] }
  - { name: "20 dB PAD", type: switch, value: "off", options: ["on", "off"] }
---

# Classic Direct-In Guitar (parallel DI + mic'd amp)

## Concept
Recreate documented direct-into-Neve guitar records — a present "direct" character blended with a mic'd amp's weight. The actual deliverable is the parallel-out blend: the 1/4" out feeds an amp and the XLR feeds the interface simultaneously, and you mix the direct (present) track against the amp (round) track.

## How to play it
1. INST input. **LO** on the verge of breakup for jangle/clean, or **HI** for the grittier "Revolution" raunch.
2. STEP 2 → PRE-VOL 11:00 (clean) to 1:00 (grit) → MASTER to unity.
3. Start EQ flat; for a thin bridge pickup boost low-mids (MIDDLE +2, MID SHIFT ≈300 Hz) + a little BASS SHIFT + a touch of high-mid to "push the guitar forward."
4. HI-PASS off for jangle, on ~9:00 for the grittier tone.
5. Run **parallel outs**: 1/4" → amp and XLR → interface at the same time; blend the two tracks.

## Notes
- **ATTRIBUTION HONESTY** — those records are the documented direct-in **technique** the pedal emulates; cite as technique, NOT "these artists used this pedal."
- No demo gives numbered knob settings, so the clock values are a translation of the described "verge of breakup + sculpt to push forward" direction.

## Sources
- Reverb Tone Report "Classic Direct Guitar Tones" — parallel DI + mic'd-amp blend, parametric EQ to sculpt, HI/LO for headroom-vs-fuzz (`research/transcripts/reverb-classic-direct-guitar-tones.md`); Produce Like A Pro clean-funk + Telecaster-thickening (`research/transcripts/produce-like-a-pro-neve-in-a-pedal.md`); technique-vs-owner caveat per `research/links/neve-direct-in-recording-history.md`.
- Transformed from Pedalxly Colour-Box-V2-Patches.md (factory/technique).
