---
type: patch
title: Joel's Rangemaster Boost
device: Chase Bliss Brothers AM
date: 2026-06-14
description: Joel Korte's stated personal favorite — the classic Rangemaster treble booster ON going into BOOST mode for an open, headroomy single-channel voice with "a little bit of hair"; the natural banjo-cut-recovery base.
tags: [boost, treble-booster, rangemaster, bright, always-on, artist, signature]
hidden:
  Input-Impedance trim: back CCW (buffers upstream — booster "behaves better after a buffer")
controls:
  - { name: "TREBLE BOOSTER", type: switch, value: "DOWN (classic Rangemaster)", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
  - { name: "CHANNEL 1 MODE", type: switch, value: "BOOST (no diodes / most headroom / open)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "10–11 o'clock" }
  - { name: "VOL 1", type: knob, value: "noon" }
  - { name: "TONE 1", type: knob, value: "noon" }
  - { name: "CHANNEL 2 MODE", type: switch, value: "off (single-channel)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "PRESENCE", type: knob, value: "DOWN" }
---

# Joel's Rangemaster Boost

## Concept
Joel Korte's stated personal favorite space ("I live in it a lot"): the classic Rangemaster treble booster ON going into BOOST mode — open, headroomy, with "a little bit of hair." A bright, cutting always-on, and the cleanest, brightest way to get the banjo to read again after the Muff.

## How to play it
1. Set the TREBLE BOOSTER DOWN (classic Rangemaster) into Channel 1 in BOOST mode (no diodes = most headroom, open).
2. Run single-channel — Channel 2 off.
3. RIG TRIM: because CB Clean + Colour Box buffer the front end, back the internal Input-Impedance trim CCW so the Rangemaster "behaves better after a buffer."

## Notes
- Modes/booster are quoted; knob clocks are inferred starting points.
- Expect a slightly higher noise floor — Joel notes that's normal when emphasizing upper-mids+treble, and the AM's filtering keeps it quiet.
- Slot: intended as a MIDI preset (suggested).

## Sources
- research/transcripts/cb-technical-demo.md
- research/links/cb-technical-demo-settings.md (Joel Korte: "Rangemaster on and going into the boost")
- research/links/treble-booster-internal-trims.md
- Ref: Joel Korte (Chase Bliss founder) — personal go-to (official Technical Demo)
- Transformed from Pedalxly Brothers-AM-Patches.md (factory/artist)
