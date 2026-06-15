---
type: patch
title: "Pseudo-Stretching — Stutter fakes real-time stretch"
device: Chase Bliss Blooper
date: 2026-06-15
description: "Factory cheat-sheet recipe (Stutter card · 'Pseudo-Stretching') — mimic real-time stretching by tapping in a short tempo in Normal mode, turning on Stutter, and leaving Blooper recording: the loop-within-a-loop stutter held over time reads as a stretched, suspended texture."
tags: [stutter, stretch, performance, factory]
dips:
  BANK A: "ON = engages the alt bank so Stutter sits on MOD A slot A3 (or load Stutter via BLIP instead)"
controls:
  - { name: "Mode", type: switch, value: "NORM — tap a short tempo, then leave Blooper in the RECORDING state (do not advance to playback)", options: ["NORM", "ADD", "SAMP"] }
  - { name: "MOD A", type: knob, value: "stutter slice size (CCW = stutter what just happened / longest; CW = what's coming up / shortest)" }
  - { name: "MOD A slot", type: switch, value: "A3 Stutter (ALT bank — requires BANK A dip; or load via BLIP)", options: ["A1", "A2", "A3"] }
  - { name: "MOD A engage", type: button, value: "arcade button (engage to hold the stutter; toggle on/off for the manic fake-stretch)" }
  - { name: "Slot/Bank", type: knob, value: "MOD A3 alt bank (BANK A dip / BLIP) · dial other knobs from recipe (no published values)" }
---

# Pseudo-Stretching — Stutter fakes real-time stretch

## Concept

Mimic real-time stretching by tapping in a short tempo in Normal mode, turning on Stutter, and leaving Blooper recording. The loop-within-a-loop stutter held over time reads as a stretched, suspended texture — a fake time-stretch with no pitch artifacts, just a held, smeared slice that keeps re-triggering while the record head wanders.

## How to play it

1. Engage BANK A so Stutter is on MOD A (slot A3 in the alt bank), or load Stutter via BLIP.
2. In NORM, tap in a short tempo (this sets a short loop measure).
3. Turn on Stutter and leave Blooper in the recording state — do not advance to playback.
4. The held loop-within-a-loop reads as a real-time-stretch / suspended texture.
5. Alternatively, manically toggle Stutter on/off during playback for the same fake-stretch feel.

## Notes

- Stutter is time-based — it desyncs the record/play heads while engaged.
- Counter-clockwise stutters what just happened (longest slice); clockwise stutters what's coming up (shortest slice) — per the manual.
- Pairs nicely with ramping so each engage gives a different slice size (see Mystery Slicing).
- Requires the BANK A dip (or a BLIP load) to put Stutter on MOD A; the exact slice-knob position is not published — dial from recipe.

## Sources

- `research/links/chasebliss-blooper-modifier-cheat-sheet.md` (STUTTER · PSEUDO-STRETCHING + TIP, verbatim)
- `research/Blooper-DeepResearch.md` §3 (A3 Stutter alt bank)
- official CB modifier cheat-sheet PDF + Blooper manual (Stutter description — CCW = past / CW = upcoming)
