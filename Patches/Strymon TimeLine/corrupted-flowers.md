---
type: patch
title: Corrupted Flowers
device: Strymon TimeLine
date: 2026-06-14
description: Official Strymon free Lo-Fi preset (Ethan Tufts) — jagged broken-transmission texture with clean signal blended back under the corrupted repeats; dead-on the "recorded-wrong" goal.
tags: [lo-fi, broken-transmission, degraded, recorded-wrong, texture, factory, signature]
controls:
  - { name: "TYPE", type: switch, value: "Lo-Fi", options: ["dTape","dBucket","Digital","Dual","Pattern","Reverse","Ice","Lo-Fi","Swell","Trem","Filter","Duck"] }
  - { name: "SAMPLE", type: knob, value: "4 kHz (heavy aliasing)" }
  - { name: "BITS", type: knob, value: "10-bit" }
  - { name: "FILTER", type: knob, value: "8 (Apartment Intercom gadget)" }
  - { name: "GRIT", type: knob, value: "dialed in (Filter + Grit + slow modulation)" }
  - { name: "MIX", type: knob, value: "blends full-resolution clean signal back in" }
  - { name: "Slot/Bank", type: knob, value: "user slot (free .syx, import via Nixie 2)" }
---

# Corrupted Flowers

## Concept
Strymon's official free Lo-Fi preset: a jagged, broken-transmission texture where the clean signal is blended back in under the corrupted repeats, so it reads as textured rather than pure noise. Dead-on the "recorded-wrong" goal — Tufts: "set the sample rate way down to 4kHz … bit depth at 10-bits."

## How to play it
1. Import the free `.syx` via Nixie 2 (no `.syx` stored on disk; transcribed setting).
2. Run it late in the chain, after the synth/pad patches.
3. Bring MIX up if you want more obviously degraded repeats.

## Notes
- SAMPLE 4 kHz + BITS 10-bit + FILTER 8 (Apartment Intercom) is the copyable core; remaining bar-graphs are image/.syx-only.
- Pairs well after VG-800 pad patches.
- The cleaner factory cousin is "Intercom" (25B).

## Sources
- Strymon "This Week's Preset: Corrupted Flowers" (Ethan Tufts)
- research/links/strymon-twp-corrupted-flowers-lofi.md
- Transformed from Pedalxly TimeLine-Patches.md (factory)
