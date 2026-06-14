---
type: patch
title: Ambient Diffusion Bed
device: Hologram Chroma Console
date: 2026-06-14
description: The Chroma's single most important structural job (designed Starting Point d) — a wide, dark stereo wash that RE-EXPANDS the mono Blooper loop back to stereo before the H90.
tags: [ambient, bed, stereo, drone, re-expander, designed, signature]
hidden:
  DRIFT (Diffusion, on SPACE): 11
  Texture FILTER style: LOW PASS (LPF)
  Bypass mode: Buffered (not True Bypass) — required or the mono→stereo routing collapses
controls:
  - { name: "Diffusion effect", type: switch, value: "SPACE", options: ["SPACE", "REVERSE", "REELS", "CASCADE", "COLLAGE"] }
  - { name: "Diffusion TIME", type: knob, value: "2 o'clock (big)" }
  - { name: "Diffusion AMOUNT", type: knob, value: "1 o'clock" }
  - { name: "Movement effect", type: switch, value: "DOUBLER", options: ["DOUBLER", "VIBRATO", "PHASER", "PITCH", "TREMOLO"] }
  - { name: "Movement RATE", type: knob, value: "11" }
  - { name: "Movement AMOUNT", type: knob, value: "10 (stereo width)" }
  - { name: "Texture effect", type: switch, value: "FILTER (LPF)", options: ["FILTER", "CASSETTE", "SQUASH", "BROKEN", "INTERFERENCE"] }
  - { name: "Texture AMOUNT", type: knob, value: "1–2 o'clock (roll off highs)" }
  - { name: "MIX", type: knob, value: "~50%" }
  - { name: "Slot/Bank", type: knob, value: "C1" }
---

# Ambient Diffusion Bed

## Concept
The Chroma's single most important structural job in the rig — a wide, dark stereo wash that re-expands the mono Blooper loop back to stereo before the H90. DOUBLER + SPACE build the width, and an LPF darkens it into a bed; let the H90 reverb sit on top.

## How to play it
1. DIFFUSION **SPACE**, TIME **2 o'clock** (big), AMOUNT **1 o'clock**, secondary **DRIFT 11**.
2. MOVEMENT **DOUBLER**, RATE **11**, AMOUNT **10** (stereo width).
3. TEXTURE **FILTER (LPF)**, AMOUNT **1–2 o'clock** (roll off highs).
4. Set **MIX ~50%**. DOUBLER + SPACE build the width; LPF darkens into a bed; H90 reverb sits on top.

## Notes
- Inferred clock-face values (DOUG-designed) — not artist-attributed.
- Make sure both outputs are connected and bypass is **Buffered** (not True Bypass), or the mono→stereo routing collapses.

## Sources
- designed from DeepResearch §13(d)
- Transformed from Pedalxly Chroma-Console-Patches.md (designed)
