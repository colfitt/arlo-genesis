---
type: patch
title: Bloom attack-then-bloom with fuzz
device: Strymon Big Sky
date: 2026-06-14
description: Epic ambient bloom that engulfs notes but stays uncluttered even with fuzz in front — you keep the attack, then it blooms (Rabea Massaad, official Strymon BigSky Pt.6 Bloom).
tags: [bloom, ambient, fuzz, saturated, epic, community, signature]
hidden:
  Feedback: lengthens/shortens the bloom
controls:
  - { name: "Machine", type: switch, value: "BLOOM", options: ["Cloud","Shimmer","Bloom","Chorale","Swell","Magneto","Nonlinear","Reflections","Room","Hall","Plate","Spring"] }
  - { name: "PARAM1", type: knob, value: "Low End" }
  - { name: "PARAM2", type: knob, value: "Length" }
  - { name: "DECAY", type: knob, value: "high (ambient/epic approach)" }
  - { name: "Slot/Bank", type: knob, value: "09C" }
---

# Bloom attack-then-bloom with fuzz

## Concept
An epic ambient bloom that engulfs notes but stays uncluttered even with a germanium fuzz in front — the attack reads first, then the reverb swells over everything. High Decay plus high Length gives the ambient/epic approach; the menu Feedback lengthens or shortens the bloom. On-aesthetic for the rig's saturated-strings-that-bloom lean.

## How to play it
1. Stack a germanium fuzz before the Big Sky.
2. Pick a note — the attack comes through first.
3. The bloom swells over the top, staying uncluttered.

## Notes
- PARAM1 = Low End, PARAM2 = Length; menu Feedback sets bloom length.
- Relative values (high Decay/Length), not numeric.

## Sources
- research/transcripts/rabea-massaad-bigsky-bloom-reverb.md (youtube.com/watch?v=U4fPrQWF35Y) — Rabea Massaad, official Strymon BigSky Pt.6 Bloom
- Transformed from Pedalxly Big-Sky-Patches.md (community)
