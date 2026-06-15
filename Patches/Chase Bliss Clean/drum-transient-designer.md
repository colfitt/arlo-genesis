---
type: patch
title: Drum Transient Designer (Dry-Push Method)
device: Chase Bliss Clean
date: 2026-06-15
description: BachelorMachines' "right way" to beef drums — don't ask stage one to limit the transients (its attack isn't fast enough and you get a snap on every hit). Push the DRY signal to engage the always-on stage-two limiter for body, then use stage one purely as a transient designer, and blend Wet and Dry for the best of both. Dialable recipe, no published clock-face values.
tags: [compression, parallel, drums, transient-control, bus, community]
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
  - { name: "Dry", type: knob, value: "PUSH UP first to drive the always-on stage-2 limiter (body), then turn FULLY DOWN to design the transient, then blend back in" }
  - { name: "Wet", type: knob, value: "the shaped transient path — blend with Dry for body + snap" }
  - { name: "Sensitivity", type: knob, value: "by the left LED — sculpt how hard the wet path reacts" }
  - { name: "Dynamics", type: knob, value: "shape the snap (recipe, dial to taste)" }
  - { name: "Attack", type: knob, value: "shape the transient (recipe, dial to taste)" }
  - { name: "EQ", type: knob, value: "to taste" }
  - { name: "Release", type: switch, value: "shape the snap (recipe, dial to taste)", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
---

# Drum Transient Designer (Dry-Push Method)

## Concept
BachelorMachines' "right way" to beef drums: don't ask stage one to limit the transients — its attack isn't fast enough, so you get a snap on every hit. Instead push the DRY signal to engage the always-on stage-two limiter for body, then use stage one purely as a transient designer — Dry down, shape the transient with Sensitivity / Dynamics / Attack / Release, then blend Wet and Dry for the best of both. Driving the stage-2 limiter hard adds harmonics — that's the sound, and it's the basis of Dusty. A parallel-comp method, not a dip mode.

## How to play it
1. **Push DRY up first** to engage the always-on stage-two limiter — that's where the drum body/weight comes from.
2. To design the transient, turn **DRY fully DOWN** and listen to the wet path alone.
3. Sculpt the snap with **Sensitivity, Dynamics, Attack and Release** while watching the left LED.
4. **Blend WET and DRY** back together for the best of both — body from the limiter, snap from your shaped wet path.
5. Drive the stage-2 limiter harder for added harmonics/overdrive when you want it.

## Notes
- **No published clock-face values** — this is a demonstrated method, so the knobs above are a dialable recipe (sculpt by ear / the left LED), not sourced settings.
- Key insight: stage one is NOT a fast enough limiter for drums — use it as a designer, not a brickwall.
- The stage-2 limiter is a clipping circuit, so hard driving = harmonics; this is the basis of Dusty.
- Applies directly to the rig's MPC/Digitakt drum bus and the VG-800 percussive patches.
- Pays off best in a stereo end/bus slot if running a full drum bus.

## Sources
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (Drums "right way": engage stage-2 limiter by pushing DRY for body; use stage-1 as a transient designer with Dry down; mix Wet and Dry; stage-2 limiter is a clipping circuit)
- Ref: BachelorMachines (transient-designer drum method) — dialable recipe, no published values
- Transformed from Pedalxly Clean-Patches.md (community)
