---
type: patch
title: De-Perfect the Digital (VG-800 / synth bonus LFO)
device: Chase Bliss Generation Loss
date: 2026-06-14
description: A bonus LFO/wobble for already-wonky digital sources — Gen Loss EQ-colors and degrades AFTER the VG-800's modeled amp/cab, fuzzing the IR's sterility into a worn cassette of an amp.
tags: [source-specific, vg-800, synth, lfo, community, signature]
hidden:
  Input Gain (Dry toggle): Line (for the VG-800's near-line output)
controls:
  - { name: "Wow", type: knob, value: "Light" }
  - { name: "Flutter", type: knob, value: "Light" }
  - { name: "Model", type: knob, value: "to taste" }
---

# De-Perfect the Digital (VG-800 / synth bonus LFO)

## Concept
A bonus LFO/wobble for already-wonky digital sources. Gen Loss EQ-colors and degrades AFTER the VG-800's modeled amp/cab, fuzzing the IR's sterility into a worn cassette of an amp; pad/synth COSM patches become "found-tape" drones. Especially good on VG-800 string/baritone pads → drone beds.

## How to play it
1. Dial in **light Wow/Flutter** as a de-perfecting wobble.
2. Pick a Model to taste.
3. Set hidden **Input Gain (Dry toggle) = Line** for the VG-800's near-line output — loud signals add digital aliasing if mis-set.

## Notes
- 🔵 community — Elektronauts tip ("a nice additional LFO for Digitone sounds that are already a bit wonky").
- Place Gen Loss *after* the VG-800's amp/cab modeling so it degrades the IR's sterility.

## Sources
- 🔵 `research/links/genloss-community-tips-pitfalls.md` + DeepResearch §6 + UsageGuide §3.
- Transformed from Pedalxly Generation-Loss-Patches.md (community).
