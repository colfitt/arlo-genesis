---
type: patch
title: Gesture Tempo-Warp
device: Hologram Chroma Console
date: 2026-06-14
description: A mechanism recipe (not a single patch) — build evolving motion faster than you could turn a knob by hand using GESTURE, the manual's stated trick; clock-locked, plays back at any tempo.
tags: [technique, gesture, modulation, factory, signature]
hidden:
  GESTURE (C+D): move an encoder slowly (step lights red + timer), C+D to stop (loops, green); clock-locked
controls:
  - { name: "Gesture record (C+D)", type: button, value: "enter GESTURE; move an encoder slowly; C+D to stop (loops green)" }
  - { name: "Tempo", type: knob, value: "record slow at e.g. 120 BPM, re-tap/send faster MIDI tempo to play back faster than your hand" }
---

# Gesture Tempo-Warp

## Concept
A mechanism recipe you fold into other patches (not a standalone single patch). GESTURE lets you build evolving motion faster than you could turn a knob by hand — the manual's stated trick. Because gestures are clock-locked, you record a slow sweep and play it back at any tempo.

## How to play it
1. Enter **GESTURE (C+D)**, move an encoder slowly (the step lights red + a timer runs), then C+D to stop (it loops, turns green).
2. Gestures are **clock-locked**: record a slow sweep at e.g. 120 BPM, then re-tap or send a faster MIDI tempo to play it back faster than your hand could move (or record at 120, drop to 70 for a different feel).
3. Layer more knobs by repeating; delete one by nudging it a hair to white; hold C+D ~2s to wipe all.

## Notes
- This is a technique recipe applied across the bank, not a single dial-in patch.
- **Gestures SAVE with the preset** (but CAPTURE recordings do not).

## Sources
- research/transcripts/hologram-gesture-recording-howto.md (YouTube netMZsuuUA0); research/transcripts/nervouscooks-deep-dive-tutorials-part2.md
- Transformed from Pedalxly Chroma-Console-Patches.md (factory)
