---
type: patch
title: Ramped Drone Swell
device: Chase Bliss Brothers AM
date: 2026-06-14
description: A drone-build tool — swell the saturation/intensity of the push into Channel 2 under a sustained banjo/baritone chord WITHOUT a level spike, before the Longsword and End Board chew on it; the signature sustained-wall builder driven by EXP/CV.
tags: [drone, swell, expression, cv, sustained-wall, designed, signature]
dips:
  MASTER: on
hidden:
  CONTROL dip bank (right side): assign EXP (or 0–5V CV) → GAIN 1 (or VOL 1); set polarity HEEL = no push / TOE = full push; SWEEP dip to taste
controls:
  - { name: "CHANNEL 2 MODE", type: switch, value: "OVERDRIVE (or DISTORTION) as the bed", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 2", type: knob, value: "11 o'clock" }
  - { name: "VOL 2", type: knob, value: "master" }
  - { name: "TONE 2", type: knob, value: "noon" }
  - { name: "CHANNEL 1 MODE", type: switch, value: "BOOST, on (the ramp target)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "starts low (swept up by EXP/CV)" }
  - { name: "TREBLE BOOSTER", type: switch, value: "MIDDLE or DOWN", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
  - { name: "PRESENCE", type: knob, value: "DOWN" }
  - { name: "EXP/CV", type: button, value: "sweep heel→toe into a held chord to bloom the drone (assigned to GAIN 1 / VOL 1 via CONTROL dips)" }
---

# Ramped Drone Swell

## Concept
A drone-build tool: swell the saturation/intensity of the push into Channel 2 under a sustained banjo/baritone chord, WITHOUT a level spike, before the Longsword and the End Board chew on it. The signature sustained-wall builder — Channel 2 (OVERDRIVE/DISTORTION) is the bed, Channel 1 (BOOST) is the ramp target, and an expression pedal or 0–5V CV sweeps the push.

## How to play it
1. Set Channel 2 (OVERDRIVE or DISTORTION) as the bed; Channel 1 (BOOST) on as the ramp target with GAIN 1 starting low.
2. Assign EXP (or 0–5V CV) → GAIN 1 (or VOL 1) via the CONTROL dip bank (right side); set polarity so HEEL = no push, TOE = full push; SWEEP dip to taste.
3. Keep the MASTER dip ON so the ramp adds saturation/intensity, not a level jump.
4. Sweep heel→toe into a held chord to bloom the drone.

## Notes
- Designed starting points, not found settings.
- CONTROLLER GOTCHA — on a Morningstar/MIDI controller, set the expression rule at the BANK level, not the preset level, and use a TRS-to-TRS cable with the omniport "Ring Active." If the swell isn't responding, that bank-vs-preset config is the first thing to check.
- Slot: intended as a MIDI preset (suggested).

## Sources
- designed from Brothers-AM-DeepResearch.md §9 (EXP/CV ramp, MASTER dip)
- research/links/cb-technical-demo-settings.md (expression over knobs)
- research/links/morningstar-expression-bank-level.md (bank-level rule + Ring-Active cabling)
- Transformed from Pedalxly Brothers-AM-Patches.md (designed)
