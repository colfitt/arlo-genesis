---
type: patch
title: Wet Slapback Cassette
device: Strymon Deco V2
date: 2026-06-14
description: Clean-ish wet cassette slapback behind a banjo lead — body and depth without the wobble seasickness. Strymon factory preset (PC1).
tags: [slapback, cassette, lead, wet, factory]
hidden:
  Doubletracker Boost/Cut: nudge up if the slap needs oomph
controls:
  - { name: "Tape Saturation", type: switch, value: "optional", options: ["ON","OFF"] }
  - { name: "Doubletracker", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "Voice", type: switch, value: "cassette", options: ["classic","cassette"] }
  - { name: "Type", type: switch, value: "sum (cleanest)", options: ["sum","invert","bounce"] }
  - { name: "Lag Time", type: knob, value: "~1:00 (slapback, 50-150 ms)" }
  - { name: "Blend", type: knob, value: "~12:00" }
  - { name: "Wobble", type: knob, value: "low ~7-8:00 (turned way down)" }
  - { name: "Volume", type: knob, value: "down low (slapback-level trick)" }
  - { name: "Saturation", type: knob, value: "up slightly (so the slap doesn't sound weak)" }
  - { name: "Slot/Bank", type: knob, value: "PC1 (factory WET SLAPBACK CASSETTE)" }
---

# Wet Slapback Cassette

## Concept
A clean-ish wet cassette slapback that sits behind a banjo lead, adding body and depth without the wobble seasickness. Sum type keeps it the cleanest. A factory-named preset (PC1); the clock-faces come from the Kaleidoscope walkthrough.

## How to play it
1. Engage Doubletracker (Tape Saturation optional).
2. Voice cassette, Type sum, Lag Time ~1:00 (slapback), Blend ~12:00, Wobble low (~7–8:00).
3. Slapback-level trick: bring Volume down low and Saturation up slightly so the slap doesn't sound weak (this counters the gain jump).
4. Hold Tape Saturation ON, turn BLEND to nudge Doubletracker Boost/Cut up if the slap needs oomph.

## Notes
- For a "real room" slap, switch Type to invert (models wall-reflection phase inversion per Celi/manual).
- Factory preset occupies fixed PC1 — renumber elsewhere only if you want it on a free slot.

## Sources
- links/strymon-deco-v2-manual-revd-secondary-midi.md (factory PC1)
- transcripts/kaleidoscope (cassette/sum/Lag ~1:00/Blend 12/Wobble ~7–8:00)
- links/thegearpage-deco-indispensable-settings.md (Volume low + Saturation up slightly so slap isn't weak)
- Ref: Strymon factory preset "Wet Slapback Cassette"
- Transformed from Pedalxly Deco-V2-Patches.md (factory/artist)
