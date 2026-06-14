---
type: patch
title: Living Reverb (drifting reverb HPF)
device: Elektron Digitakt 2
date: 2026-06-14
description: Keep an ambient wash from sitting static — an LFO continuously drifts the reverb tail's high-pass filter.
tags: [ambient, reverb, lfo, drone, community]
controls:
  - { name: "LFO1 DEST", type: switch, value: "Reverb HPF" }
  - { name: "LFO1 SPD", type: knob, value: "very low" }
  - { name: "LFO1 DEP", type: knob, value: "mid-range" }
  - { name: "LFO1 WAVE", type: switch, value: "Sine / Triangle" }
  - { name: "LFO1 MODE", type: switch, value: "FREE", options: ["FREE","TRIG","HOLD","ONE","HALF"] }
---

# Living Reverb (drifting reverb HPF)

## Concept
A simple move to keep an ambient wash alive: route a slow LFO to the Reverb HPF so the high-pass of the reverb tail drifts continuously, never settling into a static wash. Pairs naturally on top of the EZBOT bed (patch 1).

## How to play it
1. LFO: `DEST = Reverb HPF`; `SPD =` very low; `DEP =` mid-range; `WAVE = Sine/Triangle`; `MODE = FREE`.
2. The reverb tail's high-pass drifts continuously.

## Notes
- Relative values (author's); OG-era but transfers.
- Set on a send-bus track, or as global FX.

## Sources
- `research/links/59perlen-lfo-sound-design-digitakt.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
