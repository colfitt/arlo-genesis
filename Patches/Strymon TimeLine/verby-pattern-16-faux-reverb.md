---
type: patch
title: Verby — Pattern 16 faux reverb
device: Strymon TimeLine
date: 2026-06-14
description: The documented Pattern-16 reverb-fake (factory 12A) — an early-reflection wash with Smear maxed, a usable spring/room-ish reverb with no reverb engine needed.
tags: [pattern, faux-reverb, early-reflections, wash, failover, factory, signature]
controls:
  - { name: "TYPE", type: switch, value: "Pattern", options: ["dTape","dBucket","Digital","Dual","Pattern","Reverse","Ice","Lo-Fi","Swell","Trem","Filter","Duck"] }
  - { name: "TIME", type: knob, value: "220 ms" }
  - { name: "PATTERN", type: knob, value: "16 (early reflections)" }
  - { name: "SMEAR", type: knob, value: "high (bar-graph)" }
  - { name: "HIPASS", type: knob, value: "500 Hz" }
  - { name: "BOOST", type: knob, value: "−3.0 dB" }
  - { name: "Slot/Bank", type: knob, value: "12A" }
---

# Verby — Pattern 16 faux reverb

## Concept
The documented Pattern-16 reverb-fake: an early-reflection wash with Smear maxed, giving a usable spring/room-ish reverb with no reverb engine needed. Useful in the benched-failover case where the dedicated reverb is out.

## How to play it
1. Load 12A.
2. Play into it for a spring/room-ish wash without a second reverb pedal.
3. Use HIPASS 500 Hz to keep lows clear.

## Notes
- Pattern #16 (early reflections) + Smear maxed = the usable faux reverb.
- FauxSpring (48A, Pattern 15) is the shorter, springier variant.

## Sources
- research/links/strymon-factory-presets-full-list.md (Strymon factory bank 12A)
- Transformed from Pedalxly TimeLine-Patches.md (factory)
