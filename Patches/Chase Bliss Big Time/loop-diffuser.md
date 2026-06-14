---
type: patch
title: Loop Diffuser
device: Chase Bliss Big Time
date: 2026-06-14
description: Factory #9 — a slowly dissolving delay with infinite feedback; play a few notes, sit back, and let an oceanic single-chord-forever doom bed climb.
tags: [drone, self-oscillating, ambient, doom, factory, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Internal slot 9 (factory) — recall PC 9" }
  - { name: "MODE", type: switch, value: "Long", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Saturated (or #!&%)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Analog", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine (slow)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~30% (LOW so echoes climb)" }
  - { name: "FEEDBACK", type: knob, value: "~80% (ABOVE color → climbing wall)" }
  - { name: "CLUSTER", type: knob, value: "high ~70%" }
  - { name: "TILT EQ", type: knob, value: "noon → slightly down (lows feed the loop = longer tails)" }
  - { name: "WET", type: knob, value: "conservative (these get loud)" }
  - { name: "DIFFUSE", type: knob, value: "high ~75% (alt under FEEDBACK)" }
  - { name: "DIFFUSE TYPE", type: switch, value: "on (ethereal)", options: ["off", "on"] }
  - { name: "DEPTH", type: knob, value: "moderate (alt under CLUSTER)" }
  - { name: "RATE", type: knob, value: "slow (alt under TIME)" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
  - { name: "RIGHT footswitch (hold)", type: button, value: "FREEZE the bed and solo over it" }
---

# Loop Diffuser

## Concept
Factory preset #9 — Chase Bliss's official starter for "musical drones and slow-building atmosphere," quoted verbatim as *"a slowly dissolving delay with infinite feedback – play a few notes, sit back, and see what happens."* An oceanic single-chord-forever doom bed: low COLOR plus high FEEDBACK is the manual's documented "most change over time" gain structure, so the echoes climb into a wall. Feed the wet into an H90 hall downstream.

## How to play it
1. Recall **PC 9**; the motorized faders fly to the saved positions.
2. Play a few notes and sit back — the infinite-feedback loop slowly dissolves and rebuilds.
3. Hold the **RIGHT footswitch to FREEZE** the bed, then solo over the held pad.

## Notes
- Low COLOR + high FEEDBACK (FEEDBACK above COLOR) is the documented "most change over time" gain structure.
- Keep WET low — the manual warns twice about runaway volume.
- Numeric faders are a designed interpretation of the factory intent; on recall the real preset's flying faders override these.

## Sources
- 🟢 factory intent (numerics interpreted) — `research/links/cb-big-time-factory-presets-recipes.md` (intent quoted); low-COLOR/high-FEEDBACK climb rule from manual pp.24–25 + `research/transcripts/sonicstate-superbooth-john-snyder-eae-interview.md` (#!&% sag-and-return).
- Transformed from Pedalxly Big-Time-Patches.md (factory)
