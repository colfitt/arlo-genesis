---
type: patch
title: EXP Arc Sweep
device: Strymon Deco V2
date: 2026-06-14
description: Walking the whole tape arc — flange -> chorus -> slapback -> echo — under one foot during a sustained chord (the Hammock "perform the Deco" move, solo). Lag Time on expression.
tags: [expression, performance, flange, ambient, community, signature]
controls:
  - { name: "Tape Saturation", type: switch, value: "ON (light glue)", options: ["ON","OFF"] }
  - { name: "Doubletracker", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "EXP/MIDI jack", type: switch, value: "Expression mode (factory default)" }
  - { name: "EXP -> Lag Time", type: button, value: "heel = flange ~9:00 (short lag), toe = slapback/echo ~2-3:00 (MIDI alt CC#100 heel0/toe127; CC#18 = Lag Time direct)" }
  - { name: "Blend", type: knob, value: "12:00 (so the flange end reads strongest)" }
  - { name: "Wobble", type: knob, value: "~10:00" }
  - { name: "Type", type: switch, value: "sum (or invert for more dramatic through-zero at the heel)", options: ["sum","invert","bounce"] }
  - { name: "Voice", type: switch, value: "classic", options: ["classic","cassette"] }
  - { name: "Slot/Bank", type: knob, value: "PC18" }
---

# EXP Arc Sweep

## Concept
The single best live move on this pedal for sustained-wall playing: assign EXP to Lag Time and rock the foot to walk the whole tape arc — flange → chorus → slapback → echo — under one foot during a sustained chord. The Hammock "perform the Deco" move, solo, no second pair of hands.

## How to play it
1. Engage Tape Saturation (light glue) and Doubletracker; set the EXP/MIDI jack to Expression mode (factory default).
2. Assign EXP → Lag Time: unplug power, hold the Tape Saturation footswitch while powering up, then turn LAG TIME to the MAX position you want at the toe (the knob's start position = heel).
3. Set heel = flange (~9:00, short lag) and toe = slapback/echo (~2–3:00).
4. Blend 12:00 (so the flange end reads strongest), Wobble ~10:00, Type sum (or invert for a more dramatic through-zero at the heel), Voice classic.
5. Rock the foot to sweep the arc live. MIDI alt: CC#100 = EXP value (heel 0 / toe 127); CC#18 = Lag Time direct.

## Notes
- Community technique (TGP) + the verified Strymon EXP procedure.
- Hammock are the on-aesthetic reference but published NO knob numbers — values here complete the technique, not a Hammock setting.

## Sources
- links/thegearpage-deco-indispensable-settings.md ("assign EXP to Lag Time to sweep flange, chorus and delays in one continuous foot motion")
- links/strymon-deco-expression-assignment-procedure.md (exact heel/toe mechanic)
- links/hammock-deco-ambient-technique.md; manual Rev D CC#100/#18
- Ref: Hammock method ("perform the Deco") — strymon.net pedalboard feature
- Transformed from Pedalxly Deco-V2-Patches.md (community)
