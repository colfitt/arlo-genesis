---
type: patch
title: Oceanic Drone Bed
device: Chase Bliss Big Time
date: 2026-06-14
description: Freeze-and-solo ambient bed on one pedal — build a wall, FREEZE it into a non-degrading infinite pad, and play melody over the held pad.
tags: [drone, self-oscillating, ambient, doom, freeze, designed, signature]
hidden:
  Expression assign: "optional — map COLOR or FEEDBACK to expression for a hand-ridden swell/recede"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot (e.g. 1) via CC27, or use PC0 LIVE while dialing" }
  - { name: "MODE", type: switch, value: "Long", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "#!&% (misbias) or Saturated", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Analog", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine (slow)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~25–30% (LOW so echoes climb into the limiter)" }
  - { name: "TIME", type: knob, value: "long (8–12 s)" }
  - { name: "CLUSTER", type: knob, value: "high ~70%" }
  - { name: "TILT EQ", type: knob, value: "slightly below noon (boost lows → longer/louder tails)" }
  - { name: "FEEDBACK", type: knob, value: "~80% (well above COLOR)" }
  - { name: "WET", type: knob, value: "set carefully — LOUD" }
  - { name: "DIFFUSE", type: knob, value: "high ~80% (alt under FEEDBACK)" }
  - { name: "DIFFUSE TYPE", type: switch, value: "on (ghostly)", options: ["off", "on"] }
  - { name: "DEPTH", type: knob, value: "moderate (alt under CLUSTER)" }
  - { name: "RATE", type: knob, value: "very slow (alt under TIME)" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
  - { name: "RIGHT footswitch (hold)", type: button, value: "FREEZE (non-degrading infinite pad), then solo over it" }
---

# Oceanic Drone Bed

## Concept
Carry an ambient intro/outro on one pedal: build a wall with low COLOR / high FEEDBACK so the echoes climb into the limiter, then FREEZE it into a non-degrading infinite pad and play melody over the held bed. Builds on Factory #9 (Loop Diffuser) but adds the explicit FREEZE-then-solo performance move and an expression ride.

## How to play it
1. Play one chord and let the wall build.
2. Hold the **RIGHT footswitch to FREEZE** — the pad becomes a non-degrading infinite bed.
3. Solo over the frozen pad.
4. Feed the wet into an H90 hall downstream for the full doom wall.
5. Optional: map COLOR or FEEDBACK to expression for a hand-ridden swell/recede.

## Notes
- First-principles from verified control behavior — not artist-attributed.
- Numeric faders are designed starting points; on recall flying faders override them.
- WET is LOUD here — set carefully before performing.

## Sources
- 🟣 designed from manual pp.24–25 (low-COLOR/high-FEEDBACK climb) + FREEZE behavior (manual p.16) + `research/links/centerpiece-big-time-as-song-centerpiece-one-pedal.md` §2–3 (oceanic drone bed patch, [R]) + Snyder misbias sag-return (`sonicstate-superbooth-john-snyder-eae-interview.md`).
- Transformed from Pedalxly Big-Time-Patches.md (designed)
