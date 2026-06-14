---
type: patch
title: Pseudo-Sidechain Bus Limiter
device: Chase Bliss Clean
date: 2026-06-14
description: End-of-chain hard live limiter on a drum-machine / synth bus where a hot kick ducks the whole bus — dance-music pump without patching the sidechain jack. Ricky Tinez's main live preset.
tags: [limiting, sidechain, bus, electronic, pump, factory, artist]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: "off (pseudo version) — ON for the real-sidechain variant (kick into 1/8\" jack)"
  Latch: off
  Spread: off
  MISO: off
controls:
  - { name: "Dry", type: knob, value: "ALL THE WAY DOWN (limiter sound, no parallel)" }
  - { name: "Wet", type: knob, value: "output volume" }
  - { name: "Sensitivity", type: knob, value: "set so the left LED is clearly moving" }
  - { name: "Dynamics", type: knob, value: "into LIMITING (noon-3:00)" }
  - { name: "Attack", type: knob, value: "FAST (CCW) but to taste so kick transients pop through" }
  - { name: "EQ", type: knob, value: "cut some lows (CW) so hot bass doesn't over-trigger the ducking" }
  - { name: "Release", type: switch, value: "L (Fast)", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (or R for breakup texture)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
---

# Pseudo-Sidechain Bus Limiter

## Concept
End-of-chain on a drum-machine / synth bus (VG-800 modeled output, Digitakt/MPC): run Clean as a hard live limiter so that a hot kick pushes the whole bus down on every hit — a dance-music pump without patching the sidechain jack. Dry all the way down for the pure limiter sound, Dynamics into limiting, fast attack/release, and lows cut so the bass doesn't over-trigger the ducking. The closest thing Clean has to a "signature" use — documented step-by-step by a named electronic/house producer.

## How to play it
1. **Dry ALL THE WAY DOWN** (limiter sound, no parallel); Wet = output volume.
2. Set Sensitivity so the left LED is clearly moving.
3. Dynamics into LIMITING (noon–3:00).
4. Attack FAST (CCW) but to taste so kick transients pop through; Release toggle LEFT (Fast).
5. **EQ: cut some lows (CW)** so hot bass doesn't over-trigger the ducking.
6. Physics MID (or RIGHT for breakup texture).
7. **Trick:** let the kick run a bit too hot so it pushes the whole signal down on every hit.

## Notes
- Most relevant to the VG-800 source + Elektron/MPC boxes.
- **Requires redeploying Clean to a stereo end slot to pay off fully.**
- **REAL-sidechain variant:** flip the SIDECHAIN dip, feed the kick into the 1/8" jack to duck the bus (Bass Fox method) — Tinez prefers the pseudo version "so the sounds fight against one another."

## Sources
- `research/transcripts/ricky-tinez-clean-live-limiter-pseudo-sidechain.md` (Dry down, Sensitivity to LED, Dynamics into limiting, fast/fast, hot kick = pseudo-sidechain; cut lows because "the low end really overwhelms compressor circuits")
- Ref: Ricky Tinez (electronic/house) — his main live preset
- Transformed from Pedalxly Clean-Patches.md (factory/artist)
