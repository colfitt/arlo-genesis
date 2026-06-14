---
type: patch
title: LoFi — Bitcrush + Decimate
device: Akai MPC Sample
date: 2026-06-14
description: Heavy 12-bit-and-below degrade on drums/loops — the recorded-wrong crunch, latched with Color the way DIBIA$E does it.
tags: [degrade, lofi, bitcrush, decimate, factory, artist, signature]
controls:
  - { name: "LoFi Bitcrush", type: knob, value: "24.00 → 2.00 (lower = crunchier)" }
  - { name: "LoFi Decimator", type: knob, value: "0–100%" }
  - { name: "Trigger", type: switch, value: "pad pressure (Pad FX); up to 4 Pad FX at once", options: ["pressure", "latch"] }
  - { name: "Latch", type: button, value: "hold pad + Latch to lock the FX on" }
  - { name: "Resample", type: button, value: "bake the degrade in" }
  - { name: "Slot/Bank", type: knob, value: "Pad FX (per-pad pressure)" }
---

# LoFi — Bitcrush + Decimate

## Concept
Heavy 12-bit-and-below degrade on drums/loops — the recorded-wrong crunch. It's a pressure-triggered Pad FX (up to 4 at once) that can be latched on. DIBIA$E latches LoFi + Color together for "real good dirty textures" — real artist use on this box. For double-degrade, sample the 12-bit Goldbaby SP1200/MPC60 WAVs, then add LoFi on top.

## How to play it
1. Pad FX → LoFi: Bitcrush 24.00 → 2.00 (lower = crunchier), Decimator 0–100%.
2. It's triggered by pad pressure; up to 4 Pad FX at once.
3. Hold pad + Latch to lock it on.
4. Bake via Resample.
5. DIBIA$E latches LoFi + Color together for "real good dirty textures."
6. Double-degrade: sample the 12-bit Goldbaby SP1200/MPC60 WAVs, then add LoFi on top.

## Notes
- Bitcrush/Decimate ranges AC50-confirmed (manual).
- DIBIA$E's LoFi+Color latch = REAL artist use on this box.

## Sources
- 🟢 manual ranges + `research/transcripts/akaipro-mpc-sample-using-effects.md`; latch from 🟢 artist `research/transcripts/youtube-dibiase-mpc-sample-demo.md`
- Ref: DIBIA$E
- Transformed from Pedalxly MPC-Sample-Patches.md (factory + artist)
