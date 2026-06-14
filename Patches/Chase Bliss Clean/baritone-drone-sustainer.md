---
type: patch
title: Baritone Drone Sustainer
device: Chase Bliss Clean
date: 2026-06-14
description: Tames the boomy low strings of the passive baritone Jazzmaster and extends held drones/chords into a sustained bed for the doom/drone wall before the Colour Box adds girth.
tags: [compression, baritone, drone, doom, sustain, designed, signature]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: off
  MISO: off
hidden:
  Envelope Balance (EQ knob): "LEFT/full (track lows — keep the control signal full-range so it tames the boom)"
controls:
  - { name: "Sensitivity", type: knob, value: "by LED (full-range envelope — do NOT high-pass the control here; you WANT it to catch the lows)" }
  - { name: "Dynamics", type: knob, value: "noon (limiting for a sustained ceiling)" }
  - { name: "Attack", type: knob, value: "10:00 (slightly faster, to catch heavier/slower baritone transients)" }
  - { name: "Wet", type: knob, value: "1:00" }
  - { name: "Dry", type: knob, value: "10:00 (keep some body)" }
  - { name: "EQ", type: knob, value: "1:00 (slight CW to shave boom if it overwhelms — optional)" }
  - { name: "Release", type: switch, value: "R (Slow 1.5s)", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
  - { name: "Slot/Bank", type: knob, value: "Candidate onboard preset (baritone-drone set), MIDI-recallable with a doom scene" }
---

# Baritone Drone Sustainer

## Concept
The mirror of the banjo patch, designed for the passive baritone Jazzmaster's held drones/chords feeding the doom/drone wall. Where the banjo patch high-passes the control signal, here you keep the envelope full-range so the compressor catches the lows and tames the boom, while limiting + a slow release extend the held notes into a sustained bed before the Colour Box adds girth.

## How to play it
1. **Set Sensitivity by ear to the left LED first** — full-range envelope; do NOT high-pass the control here, you WANT it to catch the lows.
2. Dynamics ~noon (limiting for a sustained ceiling).
3. Attack ~10:00 (slightly faster, to catch heavier/slower baritone transients).
4. Release toggle RIGHT (Slow 1.5 s); Wet ~1:00; Dry ~10:00 (keep some body).
5. **Hidden option:** Envelope Balance LEFT/full (track lows).
6. Optional: EQ ~1:00 (slight CW) to shave boom if it overwhelms.

## Notes
- If the low strings over-trigger, EITHER cut lows on the EQ knob (CW) OR back Envelope Balance the other way — test by ear/LED.
- Approximate/designed values — dial by feel against the LED. All dips OFF.

## Sources
- Designed from manual limiting zone + `research/links/daily-clean-dialing-in-everyday-compression.md`
- `research/Clean-DeepResearch.md` §6 (baritone: full-range Envelope Balance, faster attack for heavier transients, slow release + limiting for a wall)
- `research/transcripts/ricky-tinez-clean-live-limiter-pseudo-sidechain.md` ("the low end really overwhelms compressor circuits" — cut lows if it over-ducks)
- Transformed from Pedalxly Clean-Patches.md (designed)
