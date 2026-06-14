---
type: patch
title: Crushed Analog
device: Chase Bliss Big Time
date: 2026-06-14
description: Factory #7 — a murky, modulated, saturated vintage echo; the End-Board bread-and-butter delay sitting right after Generation Loss. Start here.
tags: [lo-fi, saturated, tape-echo, vintage, factory, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Internal slot 7 (factory) — recall PC 7 or hold LEFT → scroll to slot 7" }
  - { name: "MODE", type: switch, value: "Short", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Saturated", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Warm", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine (subtle)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "0.5X", type: switch, value: "ON (12-bit crush)", options: ["off", "on"] }
  - { name: "COLOR", type: knob, value: "~45% (modest after Gen Loss)" }
  - { name: "TIME", type: knob, value: "to taste / tapped" }
  - { name: "CLUSTER", type: knob, value: "~25%" }
  - { name: "TILT EQ", type: knob, value: "slightly above noon (cut mud)" }
  - { name: "FEEDBACK", type: knob, value: "~45%" }
  - { name: "WET", type: knob, value: "~45%" }
  - { name: "TEXTURE", type: knob, value: "~40% (alt under COLOR — clipping symmetry → ragged)" }
  - { name: "DIFFUSE", type: knob, value: "low-mid (alt under FEEDBACK)" }
  - { name: "RATE", type: knob, value: "subtle (alt under TIME)" }
  - { name: "DEPTH", type: knob, value: "subtle (alt under CLUSTER)" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
---

# Crushed Analog

## Concept
Factory preset #7 — Chase Bliss's official starter for "making vintage echoes," quoted verbatim as *"a murky, modulated, and saturated delay."* This is THE starting point for the End-Board rig: it sits right after Generation Loss, running into MOOD MkII. Saturated STATE plus Warm/Analog voicing plus the 0.5X 12-bit crush give the bread-and-butter degraded echo for baritone JM, banjo, synth/VG-800, and fuzz walls.

## How to play it
- Recall **PC 7** (or hold LEFT → scroll to slot 7); the motorized faders fly to the real saved positions.
- Set TIME by tapping the LEFT footswitch to the song, or dial to taste.
- Keep COLOR modest (~45%) — the source is already degraded coming out of Generation Loss.
- SPREAD widen for stereo throw; TEXTURE around 40% takes the clipping symmetry ragged.

## Notes
- The numeric fader positions here are a **designed interpretation** of the factory intent — Chase Bliss publishes character, not numbers. On recall the real preset's flying faders override anything written here.
- Over-saturating a pre-degraded source "sounds awful" — that's why COLOR stays modest after Generation Loss.
- 0.5X ON is the built-in 12-bit crush.

## Sources
- 🟢 factory intent (numeric positions interpreted) — `research/links/cb-big-time-factory-presets-recipes.md` (manual Factory Presets pp.22–23, intent quoted verbatim); STATE×TEXTURE + 0.5X mechanics from `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` + `sonicstate-superbooth-john-snyder-eae-interview.md`.
- Transformed from Pedalxly Big-Time-Patches.md (factory)
