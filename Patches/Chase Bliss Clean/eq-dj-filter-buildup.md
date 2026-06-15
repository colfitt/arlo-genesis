---
type: patch
title: "EQ DJ Filter — Build-Up / Drop Sweep"
device: Chase Bliss Clean
date: 2026-06-15
description: "Mode toggle MIDDLE (Manual, noon = flat) turns Clean's one-knob EQ into a live DJ-style filter — sweep it by hand on a drum/synth bus for high-shelf / low-pass moves during a build-up, then snap back to noon on the drop. A performance gesture, not a set tone: sweep up to open, down to close, for tension and release. Dialable recipe from Ricky Tinez's live demo; no published clock-face values (it's a hand sweep)."
tags: [eq, filter, performance, electronic, build-up, artist]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: off
  MISO: "off (optionally map EXP/CV to the EQ knob for foot control, CV 0-5 V only)"
controls:
  - { name: "Mode", type: switch, value: "Mid (Manual — fixed EQ, noon = flat; sweep the EQ knob by hand)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "EQ", type: knob, value: "the live filter — noon flat, CW removes lows (high-pass feel), CCW removes highs (low-pass feel); sweep in real time, snap to noon for the drop" }
  - { name: "Dry", type: knob, value: "blend up if you want the filter to feel parallel (EQ is wet-only)" }
  - { name: "Wet", type: knob, value: "output volume" }
  - { name: "Sensitivity", type: knob, value: "by left LED (set so comp tracks gently; the move here is the EQ sweep, not the comp)" }
  - { name: "Dynamics", type: knob, value: "to taste (light glue under the sweep)" }
  - { name: "Attack", type: knob, value: "to taste" }
  - { name: "Release", type: switch, value: "to taste", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
---

# EQ DJ Filter — Build-Up / Drop Sweep

## Concept
Ricky Tinez's live build-up tool: with the Mode toggle MIDDLE (Manual, noon = flat), the one-knob EQ becomes a hand-played DJ filter. Sweep the EQ knob in real time on a drum/synth bus for high-shelf / low-pass filter moves during a build-up or a drop — sweep up to open, down to close, for tension and release. This is a performance gesture, not a parked tone: the value is the motion, and you snap back to noon on the drop for instant full-range release. Distinct from the Shifty patch — here YOU move the filter, it doesn't follow an envelope.

## How to play it
1. **Set the Mode toggle MIDDLE (Manual)** and EQ to noon (flat).
2. During a build-up, sweep the EQ knob to remove lows (CW) or highs (CCW) for a DJ-filter rise.
3. Snap it back to noon on the drop for instant full-range release.
4. For hands-free moves, map the EQ knob to expression/CV (stay within CV 0-5 V).

## Notes
- **No published clock-face values** — this is a live hand sweep, so the controls above are a dialable recipe, not sourced exact settings. The "value" of the EQ knob is its motion; dial the rest by ear.
- Ricky Tinez wished it could fully mute/kill the signal — it filters, it doesn't kill, so it's a sweep, not a cut.
- EQ is wet-only; blend Dry up if you want the filter to feel more like a parallel sweep.
- Best on a drum/synth bus (the VG-800 / Elektron source), end-of-chain.

## Sources
- `research/transcripts/ricky-tinez-clean-live-limiter-pseudo-sidechain.md` (EQ noon = manual flat; sweep for DJ-style high-shelf / low-pass filter moves during a build-up/drop; wished for a full mute)
- Ref: Ricky Tinez (electronic/house) — live EQ filter sweep
- Transformed from Pedalxly Clean-Patches.md (artist)
