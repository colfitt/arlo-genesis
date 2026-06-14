---
type: patch
title: Polymetric Self-Mute Gate (square LFO)
device: Elektron Digitakt 2
date: 2026-06-14
description: A sustained banjo / fuzz / pad layer that gates itself in and out polymetrically without sequencing — a self-arranging wall via an off-grid SQUARE LFO.
tags: [generative, polymetric, gate, drone, community, signature]
controls:
  - { name: "LFO1 DEST", type: switch, value: "AMP volume (or FILTER freq)" }
  - { name: "LFO1 WAVE", type: switch, value: "SQUARE" }
  - { name: "LFO1 MULT", type: knob, value: "512 or 1k" }
  - { name: "LFO1 SPEED", type: knob, value: "a deliberately non-whole, off-grid number (NOT 8/16/32)" }
  - { name: "LFO1 MODE", type: switch, value: "HOLD", options: ["FREE","TRIG","HOLD","ONE","HALF"] }
  - { name: "LFO1 DEP", type: knob, value: "high" }
  - { name: "LFO2 (optional)", type: switch, value: "DEST = LFO1 SPEED (so the mute pattern itself drifts)" }
---

# Polymetric Self-Mute Gate (square LFO)

## Concept
The standout new generative move — a self-arranging wall. A SQUARE LFO with a deliberately off-grid speed gates the track's trigs on and off polymetrically, so a 4-bar loop mutes itself differently for many bars before repeating. An optional second LFO on the square LFO's speed makes the mute pattern itself drift.

## How to play it
1. LFO: `DEST = AMP volume` (or FILTER freq); `WAVE = SQUARE`; `MULT = 512` or `1k`; `SPEED =` a deliberately non-whole, off-grid number (NOT 8/16/32); `MODE = HOLD`; `DEP =` high.
2. The square gates trigs on/off polymetrically so a 4-bar loop mutes itself differently for many bars.
3. Optional: a 2nd LFO modulating the square LFO's `SPEED` so the mute pattern itself drifts.

## Notes
- Works on any sustained track.
- `MULT` integers (512/1k) are published; `DEP`/`SPD` are relative — dial by ear.

## Sources
- `research/links/elektronauts-underrated-lfo-settings-destinations.md` (t/241235 — mistcollector)
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
