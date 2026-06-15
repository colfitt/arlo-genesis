---
type: patch
title: Shifty — Dynamic Envelope Filter / Auto-Wah
device: Chase Bliss Clean
date: 2026-06-15
description: Mode toggle LEFT (Shifty) turns Clean's one-knob EQ into a touch-responsive envelope filter — when your input crosses the Sensitivity threshold the EQ sweeps from the parked knob setting toward full frequency, then shifts back as the note decays, a vowel/wah-ish dynamic filter driven by your attack. Dialable recipe from BachelorMachines / Bass Fox / Gear Dead demos plus the official manual (Shifty EQ mode); no published clock-face values.
tags: [modulation, envelope-filter, auto-wah, dynamic-eq, shifty, community]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: "off / ON only if redeployed end-of-chain for smooth dynamic panning"
  MISO: off
controls:
  - { name: "Mode", type: switch, value: "L (Shifty — EQ sweeps from the parked point toward full frequency past threshold; sweep speed = Attack/Release)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "EQ", type: knob, value: "off-noon = the parked/resting filter point (CCW removes highs / darker rest, CW removes lows / thinner rest)" }
  - { name: "Attack", type: knob, value: "sets how fast the filter opens toward full frequency on the attack (dial from recipe)" }
  - { name: "Release", type: knob, value: "sets how fast the filter returns as the note decays (dial from recipe)" }
  - { name: "Sensitivity", type: knob, value: "by left LED = the trigger point the filter sweeps from (set so playing crosses it)" }
  - { name: "Dynamics", type: knob, value: "modest" }
  - { name: "Wet", type: knob, value: "up" }
  - { name: "Dry", type: knob, value: "to taste" }
---

# Shifty — Dynamic Envelope Filter / Auto-Wah

## Concept
With the Mode toggle LEFT (Shifty), Clean's one-knob EQ stops being a comp tone control and becomes an envelope filter: when your input crosses the Sensitivity threshold the EQ sweeps from its parked knob setting toward full frequency, then shifts back as you decay — a vowel/wah-ish dynamic filter driven by your attack, with sweep speed set by Attack and Release. It's a touch-responsive filter voice that's its own effect, not a compressor setting. This is distinct from the Modulated/Leslie patch: Shifty follows YOUR envelope, it isn't an LFO.

## How to play it
1. **Set the Mode toggle LEFT (Shifty).**
2. Set the EQ knob off-noon to choose the parked filter color (CCW = darker rest, CW = thinner rest).
3. Set Sensitivity by the left LED so playing crosses the threshold and triggers the sweep.
4. Use Attack/Release to set how fast the filter opens and returns.
5. Dig in: the EQ sweeps toward full frequency on the attack and returns as the note decays. Add SPREAD (end-of-chain only) for smooth dynamic panning.

## Notes
- **No published clock-face values** — controls above are a dialable recipe drawn from the demos and manual, not sourced exact settings. Set EQ / Attack / Release / Sensitivity by ear.
- BachelorMachines' favored use of Shifty is an "interactive harmonic swell"; Bass Fox used it as an "envelope EQ" on drums.
- Combined with heavy comp + a low-cut EQ rest point it can act almost like a gate (Gear Dead).
- SPREAD's "smooth dynamic panning" only applies if Clean is redeployed END-of-chain — keep it mono in the front slot.

## Sources
- `research/transcripts/chase-bliss-clean-official-video-manual.md` (Shifty L: EQ moves toward full frequency past threshold, sweep speed = Attack/Release)
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (Shifty = filter on an envelope follower governed by Attack/Release; best as interactive harmonic swell)
- `research/transcripts/geardead-fun-creative-compression-guitar.md` (EQ left + heavy comp acts almost like a gate)
- Chase Bliss Clean official manual (EQ pp.28–29 — Shifty mode; SPREAD = smooth dynamic panning)
- Transformed from Pedalxly Clean-Patches.md (community)
