---
type: patch
title: Ambient Send-FX Patch (ping-pong delay + dark reverb)
device: Elektron Digitakt 2
date: 2026-06-14
description: A lush all-wet ambient bed — EZBOT's published send values mapped to the manual's exact knobs so it's enterable directly.
tags: [ambient, send-fx, delay, reverb, factory, artist, signature]
controls:
  - { name: "DELAY X (ping-pong)", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "DELAY WID", type: knob, value: "hard L/R" }
  - { name: "Delay Send (DEL)", type: knob, value: "≈ 88" }
  - { name: "DELAY LPF", type: knob, value: "lowered ('top filtered')" }
  - { name: "DELAY TIME", type: knob, value: "1.00–128.00 (≈32.00 = 1/8, ≈64.00 = 1/4)" }
  - { name: "DELAY FDBK", type: knob, value: "high = swelling" }
  - { name: "Reverb Send (REV)", type: knob, value: "≈ 90" }
  - { name: "REVERB DEC", type: knob, value: "long" }
  - { name: "REVERB GAIN", type: knob, value: "lower (darker tail)" }
  - { name: "REVERB HPF/LPF", type: knob, value: "carve mud" }
  - { name: "CHORUS routing", type: switch, value: "PARALLEL to reverb (chorus→reverb collapses to mono = flange-y)" }
  - { name: "Tempo (BPM)", type: knob, value: "≈ 80" }
---

# Ambient Send-FX Patch (ping-pong delay + dark reverb)

## Concept
A lush, all-wet ambient bed where EZBOT's published send values are mapped onto the manual's exact knob names so it's enterable directly. Ping-pong delay hard-panned with a high feedback swell and a lowered LPF, a long dark reverb carved with HPF/LPF, and chorus kept parallel (never serial) to avoid the mono collapse. Pairs with patch 1.

## How to play it
1. Edit via `FUNC`+`FX`.
2. DELAY: `X` (ping-pong) = ON, `WID` hard L/R, track `DEL` send ≈ 88, `LPF` lowered ("top filtered"), `TIME` 1.00–128.00 (≈32.00 = 1/8, ≈64.00 = 1/4), `FDBK` high = swelling.
3. REVERB: track `REV` send ≈ 90, `DEC` long, `GAIN` lower for a darker tail, `HPF/LPF` to carve mud.
4. CHORUS: keep PARALLEL to reverb (chorus→reverb collapses to mono = flange-y).
5. Tempo ≈ 80 BPM.
6. Tip: `FUNC` + press an encoder reads the exact numeric value.

## Notes
- Sends 88/90 + 80 BPM are EZBOT's; the value-add here is mapping them onto the authoritative manual knob names (`X/WID/FDBK/LPF/DEC/GAIN`).
- Global FX or per-pattern; pairs with patch 1.

## Sources
- Ref: EZBOT (yt `4xBD3wQRR3I`).
- `research/links/dt2-manual-send-fx-param-map.md`
- `research/links/ezbot-dt2-ambient-tutorial-recipe.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (factory/artist)
