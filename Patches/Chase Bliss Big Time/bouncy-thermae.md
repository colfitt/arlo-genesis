---
type: patch
title: Bouncy Thermae
device: Chase Bliss Big Time
date: 2026-06-14
description: Factory #4 — an upbeat echo sequencer reminiscent of CB Thermae; banjo-as-lead arpeggiated cascades where the repeats do the melodic work.
tags: [pitched, sequenced, melodic, banjo, thermae, factory, signature]
hidden:
  SCALE IGNORE: "optional ON (clean sine + scaled steps, less chaos)"
  STEP MODE: "variant — enable in Options → tap LEFT footswitch steps pitch through SCALE"
controls:
  - { name: "Slot/Bank", type: knob, value: "Internal slot 4 (factory) — recall PC 4" }
  - { name: "MODE", type: switch, value: "Short (or Mod)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed or Digital (keep pitch clean)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi or Focus", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Octave (or Oct+4+5 — maps to tap subdivisions)", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Square (Thermae pitch jumps)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~40%" }
  - { name: "TIME", type: knob, value: "mid (sets step speed/legato)" }
  - { name: "CLUSTER", type: knob, value: "low-mid" }
  - { name: "TILT EQ", type: knob, value: "noon" }
  - { name: "FEEDBACK", type: knob, value: "~50% (cascade length)" }
  - { name: "WET", type: knob, value: "~45%" }
  - { name: "RATE", type: knob, value: "moderate (alt under TIME)" }
  - { name: "DEPTH", type: knob, value: "moderate (alt under CLUSTER)" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
  - { name: "LEFT footswitch", type: button, value: "STEP variant — with STEP MODE on, tap to step pitch through SCALE" }
---

# Bouncy Thermae

## Concept
Factory preset #4 — Chase Bliss's official starter for "exploring sequencing," quoted verbatim as *"an upbeat echo sequencer reminiscent of an old friend"* (= the CB Thermae). Feed single banjo notes and the repeats arpeggiate into octave ladders, doing the melodic work. SCALE Octave plus MOTION Square gives the Thermae-style pitch jumps; the banjo's bright transients are ideal fuel.

## How to play it
1. Recall **PC 4**; faders fly to saved positions.
2. Feed single banjo/OP-1/synth notes; the repeats arpeggiate into octave ladders.
3. TIME sets step speed/legato; FEEDBACK sets cascade length.
4. Optional **SCALE IGNORE ON** in Options for a clean sine + scaled steps with less chaos.
5. STEP variant: enable **STEP MODE** in Options → tap the LEFT footswitch to step pitch through SCALE.

## Notes
- Oct+4+5 also maps to traditional tap subdivisions.
- The banjo's bright transients are the documented ideal source for Env/Square + SCALE stepping (DeepResearch §6).
- Numeric faders are a designed interpretation of factory intent; flying faders override on recall.

## Sources
- 🟢 factory intent (numerics interpreted) — `research/links/cb-big-time-factory-presets-recipes.md` (intent quoted); Thermae/SCALE/STEP behavior from `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` + `centerpiece-harp-lady-emily-hopkins-big-time-as-instrument.md` ("more mature Thermae").
- Transformed from Pedalxly Big-Time-Patches.md (factory)
