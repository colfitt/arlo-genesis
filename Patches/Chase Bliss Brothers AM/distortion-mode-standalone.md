---
type: patch
title: "Distortion Mode Standalone — hard-clip on one channel"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: 'Documented-behavior recipe for the AM''s DISTORTION mode run solo on a single channel: hard, aggressive clipping with more compression and saturation than overdrive while still retaining clarity. The mode character is quoted from CB''s technical demo and PG''s review; no exact knob numbers are published, so GAIN/VOL/TONE/PRESENCE are a dialable recipe.'
tags: [distortion, hard-clip, saturation, single-channel, factory, mid-present]
dips:
  HI GAIN: "optional — on for a hotter version (adds ~25% gain, LED turns red)"
  MASTER: "optional — on"
controls:
  - { name: "TREBLE BOOSTER", type: switch, value: "MIDDLE (off) to start, or to taste", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
  - { name: "CHANNEL MODE", type: switch, value: "DISTORTION — single channel on, run solo", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN", type: knob, value: "to taste — keep BELOW max for the cleanest version (max brings heavily-colored compression); no published clock" }
  - { name: "VOL", type: knob, value: "turned UP to compensate — distortion clips more and is naturally quieter than boost/OD; no published clock" }
  - { name: "TONE", type: knob, value: "to taste — no published clock" }
  - { name: "PRESENCE", type: knob, value: "DOWN to start, then to taste" }
---

# Distortion Mode Standalone — hard-clip on one channel

## Concept
The AM's DISTORTION mode on its own: harder, more aggressive clipping with more compression and saturation than overdrive, while still retaining clarity. Because it clips more, it is naturally quieter and more compressed than boost or overdrive — a clipping side effect you compensate for with VOL. A single-channel hard-clip voice for a thicker, more saturated drive that stays mid-present and is never scooped.

## How to play it
1. Set one channel to DISTORTION and run it solo (single channel on).
2. Dial GAIN to taste — keep it below max for the best behavior; the highest gain brings heavily-colored compression.
3. Turn VOL up to compensate: distortion clips more and is naturally quieter/more compressed than boost or overdrive.
4. Set TONE and PRESENCE to taste (PRESENCE DOWN to start); leave the treble booster MIDDLE (off) or set it to taste.
5. Engage HI GAIN (LED goes red, ~25% more gain) only if you want it hotter; MASTER dip optional.

## Notes
- Documented mode behavior: the hard-clipping character, the natural level drop, and the "retains clarity" note are quoted from primary sources; no exact knob numbers are published — dial GAIN/VOL/TONE/PRESENCE from the recipe.
- Always mid-present, never scoopy — it cuts even at high gain.
- PG flags heavily-colored compression at the highest gain levels; the sweet spot is below max ("you don't need maximum gain").

## Sources
- research/transcripts/cb-technical-demo.md (DISTORTION = "harder and more aggressive clipping," naturally quieter/compressed)
- research/links/premier-guitar-review-tips.md (high-gain colored compression; "you don't need maximum gain")
- research/transcripts/doug-hanson-demo.md ("Distortion is a hard-clipping distortion")
- Ref: Brothers AM manual, "Controls – Modes"
