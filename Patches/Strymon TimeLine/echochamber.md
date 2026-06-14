---
type: patch
title: EchoChamber
device: Strymon TimeLine
date: 2026-06-14
description: High-resonance up-ramp filter sweep placed pre-delay (factory 47A) — a resonant whoosh on the way into the repeats.
tags: [filter, resonance, sweep, whoosh, texture, community, signature]
controls:
  - { name: "TYPE", type: switch, value: "Filter", options: ["dTape","dBucket","Digital","Dual","Pattern","Reverse","Ice","Lo-Fi","Swell","Trem","Filter","Duck"] }
  - { name: "TIME", type: knob, value: "360 ms" }
  - { name: "LFO", type: switch, value: "Up", options: ["Up","Down","Tri","Sine","Square","Random"] }
  - { name: "SPEED", type: knob, value: "2/3" }
  - { name: "FILT-Q", type: knob, value: "7.0 (high resonance)" }
  - { name: "LOC", type: switch, value: "Pre", options: ["Pre","Post"] }
  - { name: "Slot/Bank", type: knob, value: "47A" }
---

# EchoChamber

## Concept
A high-resonance up-ramp filter sweep placed pre-delay — a resonant whoosh on the way into the repeats. The LFO ramps the cutoff up while LOC Pre filters the dry signal as it enters the delay.

## How to play it
1. Load 47A.
2. Play into it for a resonant whoosh feeding the repeats.
3. Switch LOC to Post if you want the sweep on the repeats themselves instead of the dry input.

## Notes
- FILT-Q 7 is aggressive — back it off if it self-resonates.
- LOC Pre filters the dry-into-delay; LOC Post sweeps the repeats themselves.

## Sources
- research/links/strymon-factory-presets-full-list.md (Strymon factory bank 47A)
- Transformed from Pedalxly TimeLine-Patches.md (community)
