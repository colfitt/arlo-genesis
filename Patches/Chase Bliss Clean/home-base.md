---
type: patch
title: Home Base (Safe Space)
device: Chase Bliss Clean
date: 2026-06-14
description: The maker's reset/return point — the default always-on, front-of-board transparent leveler feeding the JHS Colour Box.
tags: [compression, transparent, leveler, always-on, factory, signature]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: off
  MISO: off
controls:
  - { name: "Dynamics", type: knob, value: "10:00-11:00 (gentle comp, below noon)" }
  - { name: "Sensitivity", type: knob, value: "~11:00 start, then RE-SET by ear to the left red LED (do FIRST)" }
  - { name: "Wet", type: knob, value: "1:00 (unity-to-slight boost)" }
  - { name: "Dry", type: knob, value: "OFF (or ~9:00)" }
  - { name: "Attack", type: knob, value: "10:00-11:00" }
  - { name: "EQ", type: knob, value: "noon (off)" }
  - { name: "Release", type: switch, value: "Mid (User 650 ms)", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
  - { name: "Slot/Bank", type: knob, value: "Onboard LEFT preset slot" }
---

# Home Base (Safe Space)

## Concept
The maker's "if you get lost, return here" default — a transparent leveler that sits at the front of Board 1, after the Polytune 3 and feeding the JHS Colour Box V2. Gentle compression below noon, EQ off so the Colour Box does all the tone work; Clean just provides level and dynamics. Dead quiet even with Wet/Dry gained up, making it safe as a permanent front-end anchor.

## How to play it
1. **Set Sensitivity FIRST, by ear.** Start ~11:00, then re-dial against the LEFT red LED at real playing volume until it moves — and re-set it per instrument (the GK-5 banjo and passive baritone will never share a value).
2. Dynamics ~10–11:00 for gentle, transparent comp.
3. Wet ~1:00 for unity-to-slight boost into the Colour Box; Dry off.
4. Leave EQ at noon (off) and all toggles at Mid.

## Notes
- Save this to the onboard LEFT slot — "the transparent leveler" — and never lose your way back.
- Single-LED metering means there are no recallable detents; the Sensitivity value is by feel and per-instrument.
- All CUSTOMIZE dips OFF.

## Sources
- Clean manual pp.8–9 "Getting Started / safe space" (illustrated knob positions) — `research/links/cb-manual-clean-compression-recipes.md`
- `research/transcripts/chase-bliss-clean-official-video-manual.md` (Home Base + LED-first procedure)
- Transformed from Pedalxly Clean-Patches.md (factory)
