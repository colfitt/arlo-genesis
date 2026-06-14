---
type: patch
title: 8Bit Vinyl
device: Strymon TimeLine
date: 2026-06-14
description: 8-bit + low-sample crush with dVinyl static engaged (factory 17A) — the classic lo-fi crush floor as a degraded record-player repeat.
tags: [lo-fi, vinyl, bit-crush, degraded, recorded-wrong, texture, factory, signature]
controls:
  - { name: "TYPE", type: switch, value: "Lo-Fi", options: ["dTape","dBucket","Digital","Dual","Pattern","Reverse","Ice","Lo-Fi","Swell","Trem","Filter","Duck"] }
  - { name: "TIME", type: knob, value: "350 ms" }
  - { name: "SAMPLE", type: knob, value: "1.5 kHz" }
  - { name: "BITS", type: knob, value: "8-bit" }
  - { name: "MIX", type: knob, value: "mostly dry" }
  - { name: "VINYL", type: switch, value: "S (low-mid static)", options: ["Off","S","D"] }
  - { name: "FILTER", type: knob, value: "Off" }
  - { name: "Slot/Bank", type: knob, value: "17A" }
---

# 8Bit Vinyl

## Concept
The classic lo-fi crush floor: 8-bit depth plus a low 1.5 kHz sample rate, with dVinyl static engaged for a degraded record-player repeat. The vinyl crackle adds a constant lo-fi bed under the crushed echoes.

## How to play it
1. Load 17A.
2. Keep MIX mostly dry so the crush textures the part rather than burying it.
3. Use as a degraded record-player repeat under sustained material.

## Notes
- VINYL "S" = constant crackle; VINYL "D" = crackle only in the repeats.
- Both SAMPLE (1.5 kHz) and BITS (8-bit) are doing the damage here, unlike Decimated where sample rate alone destroys.

## Sources
- research/links/strymon-factory-presets-full-list.md (Strymon factory bank 17A)
- Transformed from Pedalxly TimeLine-Patches.md (factory)
