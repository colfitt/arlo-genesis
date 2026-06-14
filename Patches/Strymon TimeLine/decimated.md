---
type: patch
title: Decimated
device: Strymon TimeLine
date: 2026-06-14
description: Maximum sample-rate destruction (factory 42B) at 750 Hz with light vinyl crackle — heavy aliasing for the harshest broken-transmission tone.
tags: [lo-fi, bit-crush, aliasing, degraded, recorded-wrong, harsh, factory, signature]
controls:
  - { name: "TYPE", type: switch, value: "Lo-Fi", options: ["dTape","dBucket","Digital","Dual","Pattern","Reverse","Ice","Lo-Fi","Swell","Trem","Filter","Duck"] }
  - { name: "TIME", type: knob, value: "400 ms" }
  - { name: "SAMPLE", type: knob, value: "750 Hz" }
  - { name: "BITS", type: knob, value: "32-bit" }
  - { name: "MIX", type: knob, value: "mostly dry" }
  - { name: "VINYL", type: switch, value: "S (low)", options: ["Off","S","D"] }
  - { name: "FILTER", type: knob, value: "Off" }
  - { name: "Slot/Bank", type: knob, value: "42B" }
---

# Decimated

## Concept
Maximum sample-rate destruction: SAMPLE down to 750 Hz produces heavy aliasing for the harshest broken-transmission tone, with light vinyl crackle on top. It's brutal — best as a single destroyed accent rather than a constant bed.

## How to play it
1. Load 42B.
2. Use it on a single destroyed accent/hit rather than a sustained wash.
3. Keep MIX mostly dry so the aliasing reads as a wrong-sounding echo.

## Notes
- Sample rate, not bit depth, is doing the damage here (BITS is left at 32-bit).
- VINYL "S" set low for a touch of crackle.

## Sources
- research/links/strymon-factory-presets-full-list.md (Strymon factory bank 42B)
- Transformed from Pedalxly TimeLine-Patches.md (factory)
