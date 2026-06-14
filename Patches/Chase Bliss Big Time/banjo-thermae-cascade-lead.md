---
type: patch
title: Banjo Thermae Cascade Lead
device: Chase Bliss Big Time
date: 2026-06-14
description: Banjo (GK-5 → VG-800) as lead — feed single plucks and the repeats arpeggiate into clean octave ladders; SCALE IGNORE keeps the pitch ramps musical.
tags: [pitched, sequenced, melodic, banjo, thermae, designed, signature]
hidden:
  SCALE IGNORE: "ON (smooth sine modulation + scaled transposition, none of the chaos)"
  STEP MODE: "variant — Options → STEP MODE ON → tap LEFT footswitch to step pitch through the scale"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27 (or refine Factory #4 in place)" }
  - { name: "MODE", type: switch, value: "Short (or Mod for tighter)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Digital or Compressed (keep pitch artifacts low)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi or Focus", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Octave (clean octave jumps) OR Oct+4+5", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Square (Thermae pitch jumps)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~40%" }
  - { name: "TIME", type: knob, value: "mid (lower = snappier steps, higher = legato)" }
  - { name: "CLUSTER", type: knob, value: "low-mid (let the core cascade read clearly)" }
  - { name: "TILT EQ", type: knob, value: "noon → up (keep bright banjo transients defined)" }
  - { name: "FEEDBACK", type: knob, value: "~45–55% (cascade length)" }
  - { name: "WET", type: knob, value: "~45%" }
  - { name: "RATE", type: knob, value: "moderate (alt under TIME)" }
  - { name: "DEPTH", type: knob, value: "moderate (alt under CLUSTER)" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
  - { name: "LEFT footswitch", type: button, value: "STEP variant — with STEP MODE on, tap to step pitch through the scale manually" }
---

# Banjo Thermae Cascade Lead

## Concept
Banjo (GK-5 → VG-800) as lead: feed single plucks and the repeats arpeggiate into clean octave ladders — the melodic hook. The key trick is **SCALE IGNORE ON**, which gives smooth sine modulation plus scaled transposition without the pedal going feral. The banjo's fast bright transients are the documented ideal source for Env/Square + SCALE stepping.

## How to play it
1. Feed single banjo plucks; the repeats arpeggiate into octave ladders.
2. Turn **SCALE IGNORE ON** in Options for musical pitch ramps without chaos.
3. Lower TIME for snappier steps, raise it for legato.
4. Keep CLUSTER low-mid so the core cascade reads clearly.
5. STEP variant: Options → **STEP MODE ON** → tap the LEFT footswitch to step pitch through the scale manually.

## Notes
- SCALE IGNORE is the key to MUSICAL pitch ramps without the pedal going feral.
- TILT EQ noon → up keeps the bright banjo transients defined.
- Numeric faders are designed starting points; on recall flying faders override them.

## Sources
- 🟣 designed from `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (SCALE/MOTION/STEP/SCALE IGNORE) + harp-lady transcript ("more mature Thermae") + DeepResearch §6 (banjo transients = MOTION/SCALE fuel) + centerpiece §4 (pitch-dive part, [V behavior]/[R knobs]).
- Transformed from Pedalxly Big-Time-Patches.md (designed)
