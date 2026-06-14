---
type: patch
title: Quest Hook
device: Longsword
date: 2026-06-14
description: The everything-at-noon factory baseline — neutral day-one distortion to calibrate the pedal before dialing any other recipe.
tags: [calibration, neutral, distortion, factory]
controls:
  - { name: "Level", type: knob, value: "noon" }
  - { name: "Drive", type: knob, value: "noon" }
  - { name: "Low", type: knob, value: "noon" }
  - { name: "High", type: knob, value: "noon" }
  - { name: "Mid", type: knob, value: "noon" }
  - { name: "Boost", type: knob, value: "noon" }
  - { name: "DIODE", type: switch, value: "up (MOSFET)", options: ["up (MOSFET)", "center (no diodes)", "down (silicon)"] }
  - { name: "SHIFT", type: switch, value: "up (1 kHz)", options: ["up (1 kHz)", "down (300 Hz)"] }
  - { name: "Boost (footswitch)", type: button, value: "OFF (kick it to take the tone over the top)" }
---

# Quest Hook

## Concept
The manual's everything-at-noon baseline — neutral, day-one distortion for any source. EAE's "great starting point for a wide variety of instrument and amp combinations." Use it to calibrate the pedal before dialing anything else.

## How to play it
1. Set every knob to noon, DIODE up (MOSFET), SHIFT up (1 kHz), Boost footswitch OFF.
2. Play your source and listen to the reference voice.
3. Kick the **Boost footswitch** to "take it over the top" for a hotter version.
4. Return here whenever you reset the pedal so every other recipe has a known reference point.

## Notes
- EAE's literal first-time procedure.
- Numeric knob positions are read off the manual's printed line diagrams and are approximate — treat as starting points and dial by ear.
- Remember the EQ is a studio Baxandall/active-mid console, not a RAT Filter: small moves are drastic and the bands barely interact, so adjust gradually.
- 9 V ONLY — the V4.5 protection shuts the pedal down above 9 V.

## Sources
- EAE Longsword V4.5 Technical Manual (Rev A, Jun 17 2025), factory preset (a) — `Gear/Longsword/research/links/eae-manual-presets.md`
- Transformed from Pedalxly Longsword-Patches.md (factory)
