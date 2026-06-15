---
type: patch
title: "Phaser — Script Phase 90 (single-knob swirl)"
device: Eventide H90
date: 2026-06-15
description: "Recreate the warm, single-knob MXR Script Phase 90 swirl using the H90 Phaser algorithm — that liquid, vocal-ish four-stage phase from countless '70s records. Concrete control recipe published by Eventide forum user 'brock', with a concrete Instant Phaser alt from forum user 'rograt'."
tags: [phaser, modulation, phase-90, mxr, vintage, community]
controls:
  - { name: "Preset A Algorithm", type: switch, value: "Phaser" }
  - { name: "Stages", type: switch, value: "4 (Phase 90); use 2 for a Phase 45", options: ["2", "4"] }
  - { name: "Type", type: switch, value: "Positive" }
  - { name: "Depth", type: knob, value: "50:50" }
  - { name: "Shape", type: switch, value: "Triangle" }
  - { name: "Speed", type: knob, value: "anywhere in 0.10-8.25 Hz, to taste" }
  - { name: "Intensity", type: knob, value: "backed off" }
  - { name: "Remaining params", type: knob, value: "zeroed" }
---

# Phaser — Script Phase 90 (single-knob swirl)

## Concept
Recreate the warm, single-knob MXR Script Phase 90 swirl using the H90 Phaser algorithm — that liquid, vocal-ish four-stage phase made famous on countless '70s records. The trick is to strip the Phaser down to one expressive control (Speed) and let the four stages do the work. Two stages instead of four gives you a Phase 45.

## How to play it
1. Load the Phaser algorithm on Preset A.
2. Set Stages 4, Type Positive, Depth 50:50, Shape Triangle.
3. Pick a Speed anywhere in the 0.10-8.25 Hz range, to taste.
4. Back off Intensity and zero the remaining params.
5. Optional: tie Speed to a HotKnob for live rate control. brock suggests pairing with a Flanger in series for more complexity.
6. Alt build (rograt): Instant Phaser algorithm in "Shallow" mode, Mix 95%, Output -3 dB.

## Notes
- Concrete control values published by forum user brock; the rograt Instant Phaser alt is also concrete (Instant Phaser, Shallow mode, Mix 95%, Output -3 dB).
- 2 Stages = Phase 45; 4 Stages = Phase 90.
- Speed is given as a usable range (0.10-8.25 Hz), not a single fixed value — dial it by ear.

## Sources
- research/links/eventide-forum-script-phase-90.md (Eventide forum, "Getting a Script Phase 90 preset from the H90"; brock: Phaser, 4 Stages, Positive, 50:50 Depth, Triangle, 0.10-8.25 Hz, back off Intensity; rograt: Instant Phaser Shallow, Mix 95%, Output -3 dB)
- https://www.eventideaudio.com/forums/topic/getting-a-script-phase-90-preset-from-the-h90/
- Transformed from community forum recipe (community)
