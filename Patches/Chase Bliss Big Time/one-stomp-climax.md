---
type: patch
title: One-Stomp Climax
device: Chase Bliss Big Time
date: 2026-06-14
description: The build/drop — hold the RIGHT footswitch and the OVERLOAD ramp detonates a part's climax into a wall (COLOR+FEEDBACK toward max), release to collapse.
tags: [performative, feedback, climax, overload, drone, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27" }
  - { name: "MODE", type: switch, value: "Long (OVERLOAD only works in Long)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Saturated", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Analog", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine slow", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~35% (headroom so the ramp has somewhere to go)" }
  - { name: "TIME", type: knob, value: "long" }
  - { name: "CLUSTER", type: knob, value: "~50%" }
  - { name: "TILT EQ", type: knob, value: "pushed DOWN (boost lows → longer/louder tails feeding the climb)" }
  - { name: "FEEDBACK", type: knob, value: "~55% (base) — the ramp takes it to max" }
  - { name: "WET", type: knob, value: "set conservatively (the ramp is scary loud)" }
  - { name: "DIFFUSE", type: knob, value: "high (alt under FEEDBACK)" }
  - { name: "TEXTURE", type: knob, value: "mid (alt under COLOR)" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
  - { name: "RIGHT footswitch (hold)", type: button, value: "OVERLOAD — ramps COLOR+FEEDBACK toward max into a wall; release to fall back" }
  - { name: "MODE button (hold)", type: button, value: "Panic reset to a clean simple delay (safety net)" }
---

# One-Stomp Climax

## Concept
The build/drop on one footswitch: hold the RIGHT footswitch in Long mode and the **OVERLOAD** ramp drives COLOR and FEEDBACK toward max, detonating a part's climax into a wall; release to collapse. COLOR and FEEDBACK sit with headroom so the ramp has somewhere to go, and TILT EQ is pushed down to boost lows that feed the climb.

## How to play it
1. Set the base state (MODE Long — OVERLOAD only works in Long).
2. At the climax, **hold the RIGHT footswitch** → OVERLOAD ramps COLOR+FEEDBACK toward max into a wall.
3. Release to fall back / collapse.
4. Safety: hold the **MODE button** to panic-reset to a clean simple delay if it gets out of hand.

## Notes
- The manual warns "beware volume levels" twice — set WET low before this.
- The hold-MODE clean reset is your safety net out of the chaos.

## Sources
- 🟣 designed from manual p.16/26 (OVERLOAD = hold RIGHT in Long, maxes COLOR+FEEDBACK) + `research/links/centerpiece-big-time-as-song-centerpiece-one-pedal.md` §2/§9 patch 4 ([V]) + `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (overload behavior + hold-MODE reset).
- Transformed from Pedalxly Big-Time-Patches.md (designed)
