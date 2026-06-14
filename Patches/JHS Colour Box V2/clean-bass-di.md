---
type: patch
title: Clean Bass DI (transparent color)
device: JHS Colour Box V2
date: 2026-06-14
description: Always-on warm-color DI for the Fender Pro Jazz bass straight to the Apollo x8 — no separate DI box; the point is saturation/warmth, not distortion. (Ref: Tape Op mid-'70s rock bass DI; Black Pumas Brendan Bond V2 bass board.)
tags: [bass, di, clean, warm-color, xlr-out, community, artist]
controls:
  - { name: "HI/LO", type: switch, value: "LO", options: ["HI", "LO"] }
  - { name: "STEP", type: knob, value: "2–3 clicks in from full-left (≈position 2–3)" }
  - { name: "PRE-VOL", type: knob, value: "9:00" }
  - { name: "MASTER", type: knob, value: "3:00" }
  - { name: "TREBLE", type: knob, value: "flat-ish (noon)" }
  - { name: "TREBLE SHIFT", type: knob, value: "noon" }
  - { name: "MIDDLE", type: knob, value: "flat-ish (noon)" }
  - { name: "MID SHIFT", type: knob, value: "noon" }
  - { name: "BASS", type: knob, value: "flat-ish (noon)" }
  - { name: "BASS SHIFT", type: knob, value: "noon" }
  - { name: "HI-PASS", type: knob, value: "~8–9:00 (≈160 Hz, clean sub)" }
  - { name: "HI-PASS ON/OFF", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "INST/XLR", type: switch, value: "XLR (out → interface)", options: ["INST", "XLR"] }
  - { name: "20 dB PAD", type: switch, value: "off (engage only for hot/line into XLR in)", options: ["on", "off"] }
---

# Clean Bass DI (transparent color)

## Concept
An always-on warm-color DI for the Fender Pro Jazz bass straight to the Apollo x8 — no separate DI box needed. The point is saturation and warmth, not distortion. At this low gain MASTER higher than PRE-VOL is fine; the "keep MASTER lower than PRE-VOL" hiss rule only matters at high gain.

## How to play it
1. Set input to **XLR** out → interface (the 1/4" out can simultaneously feed a pedalboard for parallel mono).
2. **LO** mode. Gain-stage: STEP 2–3 clicks in from full-left → PRE-VOL ~9:00 → MASTER ~3:00 ("pushed up into it a little just to have enough color").
3. Leave EQ flat-ish, or apply the clarity curve (see "Bass Clarity EQ Curve").
4. Engage the HI-PASS toggle, knob ~8–9:00 (≈160 Hz) — a sleeper feature to clean sub-frequencies.
5. PAD stays off on INST; engage it only if feeding a hot/line source into the XLR in.

## Notes
- Community-cited **exact** positions from the most detailed bass demo — these are not translated.
- The 1/4" out can feed a pedalboard while the XLR feeds the interface (parallel mono).

## Sources
- The Bass Negus, verbatim: "HI/LO = LO, STEP ~2–3 clicks in from full-left, PRE-VOL ~9 o'clock, MASTER ~3 o'clock — pushed up into it a little just to have enough color" (`research/transcripts/bass-negus-bass-tutorial.md`); Tape Op tracked-bass DI (`research/links/colour-box-tapeop-engineer-di.md`); artist per `research/links/colour-box-artist-vs-technique.md`.
- Transformed from Pedalxly Colour-Box-V2-Patches.md (community).
