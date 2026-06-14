---
type: patch
title: Always-On Huge Fuzz Feeder
device: Chase Bliss Clean
date: 2026-06-14
description: Slams the MXR 108 / Hizumitas / Longsword evenly so even quiet picking triggers full downstream saturation — the "always massive" doom feeder.
tags: [compression, limiting, fuzz-feeder, doom, designed, signature]
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
  - { name: "Sensitivity", type: knob, value: "HIGH (by LED, hot enough that quiet notes still move it)" }
  - { name: "Dynamics", type: knob, value: "noon-1:00 (hard limiting)" }
  - { name: "Wet", type: knob, value: "1:00-2:00 (hot, to slam the next pedal)" }
  - { name: "Dry", type: knob, value: "OFF" }
  - { name: "Attack", type: knob, value: "9:00 (fast)" }
  - { name: "EQ", type: knob, value: "noon (off)" }
  - { name: "Release", type: switch, value: "Mid (User 650ms)", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
  - { name: "Slot/Bank", type: knob, value: "MIDI-recallable doom-feeder preset alongside the fuzz-board scene" }
---

# Always-On Huge Fuzz Feeder

## Concept
A hard-limiting feeder designed to slam the MXR 108 / Hizumitas / Longsword evenly so that even quiet picking triggers full downstream saturation — the "always massive" doom voice. High Sensitivity plus limiting flattens dynamics into a hot, consistent drive level.

## How to play it
1. **Set Sensitivity by ear to the left LED first** — run it HIGH, hot enough that quiet notes still move it.
2. Dynamics ~noon–1:00 (hard limiting).
3. Wet ~1–2:00 (hot, to slam the next pedal); Dry off.
4. Attack ~9:00 (fast); EQ noon; toggles at Mid.

## Notes
- **HONEST:** Wet here is comp make-up gain, not a pristine clean boost — plenty hot to slam the fuzz but not transparent.
- To let the fuzz BREATHE with your attack instead, back Dynamics DOWN out of limiting (toward 10:00 comp). Don't over-compress into the Hizumitas (Big-Muff style) if you want the dynamic bloom.
- All dips OFF.

## Sources
- Designed from manual limiting zone + `research/links/daily-clean-dialing-in-everyday-compression.md` (push Sensitivity up so even quiet picking triggers full saturation)
- `research/Clean-DeepResearch.md` §9 + §13(c) (light comp before fuzz = consistent drive; high Sensitivity = "always-on huge")
- Transformed from Pedalxly Clean-Patches.md (designed)
