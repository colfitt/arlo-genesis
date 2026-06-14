---
type: patch
title: Harmonic Tremolo / Stereo Leslie
device: Chase Bliss Clean
date: 2026-06-14
description: Turns a simple mono pad/drone into a fluttering harmonic-tremolo or distorted-Leslie/organ texture via the Modulated EQ mode; banjo arpeggios with movement before the texture board.
tags: [modulation, harmonic-tremolo, leslie, stereo, texture, community, signature]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: "off (front-of-board mono) / ON only if redeployed end-of-chain for the stereo Leslie"
  MISO: "off (front-of-board mono) / ON only if redeployed end-of-chain for the stereo Leslie"
controls:
  - { name: "Mode", type: switch, value: "R (Modulated — EQ auto-modulates as you play; rate = Attack)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "EQ", type: knob, value: "off-noon to pick the modulated center (CW reduces lows / CCW reduces highs)" }
  - { name: "Attack", type: knob, value: "set flutter rate (CCW faster, almost-FM)" }
  - { name: "Sensitivity", type: knob, value: "by LED (motion only happens while playing above threshold; fades when you stop)" }
  - { name: "Dynamics", type: knob, value: "modest" }
  - { name: "Wet", type: knob, value: "up" }
  - { name: "Dry", type: knob, value: "to taste" }
  - { name: "Release", type: switch, value: "to taste", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
---

# Harmonic Tremolo / Stereo Leslie

## Concept
In Modulated mode (Mode toggle RIGHT) Clean's EQ auto-modulates as you play, with the rate set by Attack — a harmonic tremolo. Redeployed in stereo (end-of-chain only), the modulated EQ becomes a "distorted Leslie/organ" auto-pan texture on a simple mono pad. Great for turning a VG-800 or baritone drone into fluttering movement, or banjo arpeggios with motion before the texture board.

## How to play it
1. **Mode toggle RIGHT (Modulated)** — EQ auto-modulates as you play; rate = Attack.
2. Set the EQ knob off-noon to pick the modulated center (CW reduces lows / CCW reduces highs).
3. Set Attack for the flutter rate (CCW faster, almost-FM).
4. Set Sensitivity by LED — motion only happens while playing above threshold and fades when you stop.
5. Dynamics modest; Wet up; Dry to taste.
6. **Stereo redeploy (end-of-chain only):** add SPREAD + MISO dips for an auto-pan "Leslie" — keep it mono in the front slot.

## Notes
- The stereo "Leslie" only pays off if Clean is **redeployed END-of-chain** — it runs mono at the front of Board 1.
- For a Shifty/envelope-filter variant: Mode toggle **LEFT** instead — the EQ sweeps open when you cross threshold, a vowel/wah-ish dynamic filter.

## Sources
- `research/transcripts/devin-belanger-clean-most-useful-pedal.md` (Modulated EQ in stereo = distorted Leslie on a mono pad)
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (Modulated R = harmonic tremolo, rate = Attack)
- `research/transcripts/geardead-fun-creative-compression-guitar.md` (EQ right = tremolo, Attack down = faster flutter)
- Transformed from Pedalxly Clean-Patches.md (community)
