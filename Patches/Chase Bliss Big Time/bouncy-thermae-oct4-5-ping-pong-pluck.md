---
type: patch
title: Bouncy Thermae Oct+4+5 Ping-Pong Pluck
device: Chase Bliss Big Time
date: 2026-06-15
description: "Centerpiece pitch-stepper — the factory-#4 'Bouncy Thermae' cascade tuned for a bare synth pluck and pushed wider: SCALE Oct+4+5 steps each repeat octave/+5th/+4th into a chordal ladder, MOTION Square fires the Thermae pitch-jumps, STEP MODE lets the LEFT footswitch walk pitch by hand, and SPREAD ping-pong throws the climbing repeats hard L↔R. Feed one mono pluck and the repeats self-play a melodic sequence. DOUG-designed from factory-#4 intent + documented SCALE/MOTION/STEP behavior (no published per-knob values — dialable recipe)."
tags: [pitched, sequenced, melodic, thermae, synth, oct4-5, ping-pong, step, designed, signature]
hidden:
  STEP MODE: "ON (Options page → tap LEFT footswitch to walk pitch up through the SCALE by hand — the composed-run performance move)"
  MISO: "auto-engages off IN-L (mono-in / stereo-out) so SPREAD ping-pong has a real stereo field to throw repeats across"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot (flying faders fly to it on recall)" }
  - { name: "MODE", type: switch, value: "Short", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed (holds stepped repeats together, keeps pitch clean, no runaway — NOT Saturated/misbias)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi or Focus", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Oct+4+5 (octave + 5th + 4th cascade — the wide flavor; also maps to tap subdivisions if you want it clock-locked)", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Square (Thermae pitch-jumps)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~40%" }
  - { name: "TIME", type: knob, value: "mid (sets step speed)" }
  - { name: "CLUSTER", type: knob, value: "low-mid (let the core ladder read)" }
  - { name: "TILT EQ", type: knob, value: "noon → up (keep pluck transients defined so the SCALE engine fires cleanly)" }
  - { name: "FEEDBACK", type: knob, value: "~50–60% (how long the ladder builds)" }
  - { name: "WET", type: knob, value: "~45% (set BELOW the dry pluck at first — stacked 5ths/octaves pile energy fast)" }
  - { name: "RATE", type: knob, value: "moderate (alt under TIME)" }
  - { name: "DEPTH", type: knob, value: "moderate (alt under CLUSTER)" }
  - { name: "SPREAD", type: switch, value: "ping-pong (climbing repeats alternate hard L↔R across the stereo field)", options: ["off", "widen", "ping-pong"] }
  - { name: "LEFT footswitch", type: button, value: "With STEP MODE on, tap to walk pitch up through the SCALE by hand — composed runs; leave it for hands-free self-stepping off Square MOTION" }
  - { name: "MODE (press-and-hold)", type: button, value: "Panic-reset back to a plain delay if a cascade runs away" }
---

# Bouncy Thermae Oct+4+5 Ping-Pong Pluck

## Concept
The factory-#4 'Bouncy Thermae' cascade tuned for a synth pluck source and pushed wider: **SCALE on Oct+4+5** so each repeat steps octave/+5th/+4th into a richer chordal ladder, **MOTION Square** for the Thermae pitch-jumps, **STEP MODE on** so the LEFT footswitch can walk pitch through the scale by hand, and **SPREAD ping-pong** so the climbing repeats alternate hard L↔R across the stereo field. Feed one bare mono pluck and the repeats become a self-playing melodic sequence. The whole point is the cascade arranges the note — the instrument plays almost nothing. Distinct from 'Bouncy Thermae' (Factory #4, SCALE Octave, STEP as a variant) by the wider Oct+4+5 ladder, the ping-pong field, and a synth-pluck source instead of banjo.

## How to play it
1. Recall the patch (faders fly to saved positions); confirm **SCALE = Oct+4+5**, **MOTION = Square**, **SPREAD = ping-pong**.
2. Enable **STEP MODE** in Options if you want hand-stepped runs from the LEFT footswitch.
3. Feed a single bare mono synth pluck into **IN-L** (MISO auto-engages for stereo-out).
4. Let the repeats arpeggiate up the octave/5th/4th ladder, ping-ponging L↔R; **TIME** sets step speed, **FEEDBACK** sets how long the ladder builds.
5. For a composed run, tap **LEFT** to walk pitch through the scale by hand; for hands-free, leave it self-stepping off the Square MOTION.
6. Press-and-hold **MODE** to panic-reset back to a plain delay if a cascade runs away.

## Notes
- **STATE must stay Compressed** (not Saturated/misbias) — drive smears the Oct+4+5 transposition into noise and defeats the musical-ladder goal.
- Oct+4+5 also maps to traditional tap subdivisions if you want the cascade clock-locked / rhythmic.
- **SPREAD ping-pong needs MISO** (IN-L only) to have a stereo field to throw repeats across — feed the right input and the bounce collapses.
- **Honesty flag:** the numeric faders are a DIALABLE RECIPE — a designed interpretation of factory-#4 'Bouncy Thermae' intent, NOT published TE/CB per-knob values. The Big Time's motorized flying faders override them on recall. Switch positions and Options-page items (STEP MODE / MISO) are verified against the existing Big Time patch sheets + GearProfile; the specific values are designed starting points.

## Sources
- 🟣 designed from factory-#4 'Bouncy Thermae' intent (`Patches/Chase Bliss Big Time/bouncy-thermae.md`) + `Patches/Chase Bliss Big Time/banjo-thermae-cascade-lead.md` (SCALE / MOTION / STEP / MISO method).
- `gear/Chase Bliss Big Time/research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (MOTION / SCALE / STEP / SCALE IGNORE behavior).
- `gear/Chase Bliss Big Time/research/transcripts/centerpiece-harp-lady-emily-hopkins-big-time-as-instrument.md` ("more mature Thermae" framing).
