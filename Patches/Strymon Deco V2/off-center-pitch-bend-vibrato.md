---
type: patch
title: Off-Center Pitch-Bend Vibrato
device: Strymon Deco V2
date: 2026-06-14
description: Pitch-bent warped-tape vibrato on a sustained note — the "recorded-wrong" wow/flutter character right on the source. Strymon's own named recipe "Off-Center".
tags: [vibrato, pitch-bend, warped-tape, degrade, factory, signature]
controls:
  - { name: "Tape Saturation", type: switch, value: "optional", options: ["ON","OFF"] }
  - { name: "Doubletracker", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "Type", type: switch, value: "sum (or invert for a hollower tonality)", options: ["sum","invert","bounce"] }
  - { name: "Lag Time", type: knob, value: "minimum (lag deck wobbling around zero)" }
  - { name: "Blend", type: knob, value: "FULL CW (lag deck only — random detune is the whole signal)" }
  - { name: "Wobble", type: knob, value: "heavy ~2-3:00 (up toward maximum = random vibrato/pitch)" }
  - { name: "Slot/Bank", type: knob, value: "PC15" }
---

# Off-Center Pitch-Bend Vibrato

## Concept
Strymon's own named "Off-Center" recipe: blend down to just the lag deck wobbling around zero, push Wobble heavy, and the random detune becomes pitch-bent warped-tape vibrato — the "recorded-wrong" wow/flutter character right on the source. A strong degrade-aesthetic fit on the banjo/baritone.

## How to play it
1. Engage Doubletracker (Tape Saturation optional).
2. Type sum (or invert for a hollower tonality).
3. Lag Time to minimum (lag deck wobbling around zero).
4. Blend FULL CW (lag deck only — no Reference, so the random detune is the whole signal).
5. Wobble heavy (~2–3:00, up toward maximum = random vibrato/pitch).
6. Variations: blend Reference back (Blend toward 50/50) for a wild tape flange instead; or Type bounce at min Lag + min Wobble for auto-panning stereo movement.

## Notes
- Strymon's own named recipe (direction verbatim); the "heavy Wobble" = ~2–3:00 clock-face is a completion, flagged designed/approximate.
- Blending Reference back transforms the effect into a flange — keep Blend full CW for the pure vibrato.

## Sources
- transcripts/strymon-tape-flanging-chorus-examples.md (Strymon "Off-Center": Blend to just the lag deck + heavy Wobble = pitch-bent; blend Reference back = wild flange)
- transcripts/strymon-pete-celi-in-depth-demo.md (Blend full CW = lag deck only; add Wobble for vibrato)
- Ref: Strymon named recipe "Off-Center" (PUNklBG8gAc)
- Transformed from Pedalxly Deco-V2-Patches.md (factory/artist)
