---
type: patch
title: Dual Stereo Split (clean low / fuzz-ready high)
device: Roland VG-800
date: 2026-06-14
description: One-instrument-as-two layered/wide texture for the stereo split (CE-2W → Deco V2).
tags: [dual-guitar, string-split, stereo, fuzz, designed, signature]
controls:
  - { name: "INST TYPE", type: switch, value: "DUAL GUITAR" }
  - { name: "DIV MODE", type: switch, value: "DUAL", options: ["SINGLE", "DUAL"] }
  - { name: "Channel A", type: switch, value: "clean model on LOW strings (pan left)" }
  - { name: "Channel B", type: switch, value: "fuzz-ready model on HIGH strings (pan right)" }
  - { name: "AB BALANCE", type: knob, value: "50" }
  - { name: "ACOUSTIC RESONANCE", type: switch, value: "OFF (silently kills per-string/AB PAN)", options: ["ON", "OFF"] }
  - { name: "Slot/Bank", type: knob, value: "User Memory (guitar mode), e.g. U05-1" }
---

# Dual Stereo Split (clean low / fuzz-ready high)

## Concept

One-instrument-as-two layered/wide texture for the stereo split (CE-2W → Deco V2). `DIV MODE = DUAL` with a clean model on the low strings and a fuzz-ready model on the high strings (string/fret split), panned A-left / B-right for width.

## How to play it

1. Set `INST TYPE = DUAL GUITAR`, `DIV MODE = DUAL`.
2. Channel A = clean model on LOW strings; Channel B = fuzz-ready model on HIGH strings (string/fret split), or pan them.
3. `AB BALANCE = 50`. Pan A left / B right for width.
4. ⚠ Keep `ACOUSTIC RESONANCE` off — a stereo-collapsing block downstream silently kills the per-string/AB PAN.

## Notes

- Designed, but the DUAL / AB-balance / per-string-pan mechanics + the acoustic-resonance-collapses-stereo gotcha are community/demo-verified (Gear Sounds, main thread).

## Sources

- 🟣 designed from UsageGuide §8 + DeepResearch §9 + `research/transcripts/gear-sounds-full-tutorial.md`
- Transformed from Pedalxly VG-800-Patches.md (DOUG-designed)
