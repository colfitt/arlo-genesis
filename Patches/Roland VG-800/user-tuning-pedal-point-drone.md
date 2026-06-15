---
type: patch
title: "USER Tuning Pedal-Point Drone — per-string custom tuning"
device: Roland VG-800
date: 2026-06-15
description: "A custom drone built from the ALT TUNE USER mode — set each string's PITCH (±24 semitones) independently so the low strings become a unison/fifth pedal-point and the high strings carry the melody, all without retuning the instrument. The bespoke doom/drone enabler the baritone calibration file describes (\"low strings to a unison/fifth pedal, high strings to the melody\"); per-string values are designer's choice, the mechanism is manual-verified."
tags: [alt-tuning, drone, doom, designed, baritone, banjo]
dips:
  GUITAR TO MIDI: "CONTROL ASSIGN → GUITAR TO MIDI → ALT TUNE = ON (so the retuned pitches transmit, not the physical notes)"
  OUTPUT SELECT: "LINE/PHONES"
controls:
  - { name: "ALT TUNE SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "ALT TUNE MODE", type: switch, value: "ALT TUNE", options: ["ALT TUNE", "HARMONY"] }
  - { name: "ALT TUNE TYPE", type: switch, value: "USER (per-string custom tuning)", options: ["OPEN D/E/G/A", "DROP D-A", "D-MODAL", "NASHVL", "4TH", "-12 to +12 STEP", "USER"] }
  - { name: "PITCH 1-7 (HiC-LowB)", type: knob, value: "-24 to +24 semitones per string — e.g. drop the low strings to a unison/fifth pedal-point, leave/raise the high strings for melody (per-string values are designer's choice)" }
  - { name: "FINE 1-7 (HiC-LowB)", type: knob, value: "-50 to +50 — small detune per string to thicken/drift the drone" }
  - { name: "NORMAL MIX", type: knob, value: "~30% (keep real attack under the retuned model; dial by ear — no published value)" }
  - { name: "Slot/Bank", type: knob, value: "User Memory (guitar mode)" }
---

# USER Tuning Pedal-Point Drone — per-string custom tuning

## Concept

A custom drone built from the `ALT TUNE` `USER` mode — set each string's `PITCH` (−24 to +24 semitones) independently so the low strings become a unison/fifth pedal-point and the high strings carry the melody, all without physically retuning the instrument. The bespoke doom/drone enabler the baritone calibration file calls out by name: "low strings to a unison/fifth pedal, high strings to the melody." `FINE` (±50 per string) adds slight detune drift to thicken the drone. Unlike a global transposer, this is per-string custom voicing — the doom/banjo player's bespoke tuning, dialed in software.

## How to play it

1. Set `ALT TUNE SW = ON`, `ALT TUNE MODE = ALT TUNE`, `ALT TUNE TYPE = USER`.
2. Set `PITCH` per string: e.g. drop the low strings to a unison or fifth pedal-point, leave or raise the high strings for the melody.
3. Use `FINE` (±50) for a slight detune drift to thicken the drone.
4. `NORMAL MIX ~30%` to keep real attack under the retuned model (dial by ear).
5. Hold the low pedal strings; play melody on top. Into the fuzz wall the extreme shifts artifact — a feature.
6. To drive a sampler/synth with the *retuned* pitches: `CONTROL ASSIGN → GUITAR TO MIDI → ALT TUNE = ON` (otherwise MIDI spells the physical notes).

## Notes

- Manual-verified mechanism: `ALT TUNE` `USER` exposes `PITCH 1–7` (HiC–LowB, −24 to +24 semitones) and `FINE 1–7` (−50 to +50) per string. The baritone calibration file explicitly calls out USER tuning for "low strings to a unison/fifth pedal, high strings to the melody."
- The per-string `PITCH`/`FINE` values are the **designer's choice — not a published preset.** Treat the example voicing above as a dialable recipe, not a sourced setting. The parameter names and ranges are sourced; the specific numbers are yours to design.
- Honesty: extreme per-string `PITCH` shifts stack the pitch-shifter and artifact more the lower you go — calibrate at the tuning you actually play. The `NORMAL MIX` value is dialed by ear; no published value.
- Distinct from `E V Drop C` and the −7 STEP doom wall (those are global all-string transposers via `±STEP`); this is per-string custom voicing via `USER`.

## Sources

- 🟢 `research/links/parameter-guide-alt-tuning-values.md` (USER: PITCH 1–7 −24 to +24 semitones, FINE 1–7 −50 to +50 per string — manual-verified, Parameter Guide eng02 pp.4–5)
- 🟣 `research/calibration-baritone-JM.md` (USER tuning: "low strings to a unison/fifth pedal, high strings to the melody")
- 🟢 `research/links/vguitarforums-guitar-to-midi.md` (CONTROL ASSIGN → GUITAR TO MIDI → ALT TUNE = ON to transmit retuned pitches)
- 🟣 designed — per-string values are designer-set; mechanism + rig calibration note are sourced
