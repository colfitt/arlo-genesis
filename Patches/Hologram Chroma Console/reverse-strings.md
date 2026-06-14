---
type: patch
title: Reverse Strings
device: Hologram Chroma Console
date: 2026-06-14
description: A bowed/backwards string-like lead (wolfewithane) — the turnkey banjo-as-lead "recorded-wrong" voice; SWELL into pitch-wobble into reverse delay, tamed with an LPF.
tags: [reverse, lead, banjo, recorded-wrong, ambient, community, signature]
hidden:
  Module order: CHARACTER SWELL → MOVEMENT VIBRATO → DIFFUSION REVERSE
  Texture FILTER style: LOW PASS (LPF, ~7–10 o'clock) on the banjo's top
controls:
  - { name: "Character effect", type: switch, value: "SWELL", options: ["SWELL", "SWEETEN", "HOWL", "FUZZ"] }
  - { name: "Character AMOUNT", type: knob, value: "to taste" }
  - { name: "Movement effect", type: switch, value: "VIBRATO", options: ["VIBRATO", "PHASER", "PITCH", "TREMOLO", "DOUBLER"] }
  - { name: "Movement AMOUNT", type: knob, value: "to taste" }
  - { name: "Diffusion effect", type: switch, value: "REVERSE", options: ["REVERSE", "SPACE", "REELS", "CASCADE", "COLLAGE"] }
  - { name: "Diffusion AMOUNT", type: knob, value: "to taste" }
  - { name: "Texture effect", type: switch, value: "FILTER", options: ["FILTER", "CASSETTE", "SQUASH", "BROKEN", "INTERFERENCE"] }
  - { name: "Slot/Bank", type: knob, value: "B1" }
---

# Reverse Strings

## Concept
A bowed/backwards string-like lead — the turnkey banjo-as-lead "recorded-wrong" voice. An envelope SWELL feeds a pitch-wobble (VIBRATO) which feeds a REVERSE delay, while an LPF on TEXTURE tames the banjo's ice-pick top.

## How to play it
1. Set the chain (module order): **CHARACTER SWELL → MOVEMENT VIBRATO → DIFFUSION REVERSE.**
2. Pair the **FILTER LPF range (~7–10 o'clock)** on TEXTURE to tame the banjo's bright top.
3. Dial per-knob AMOUNTs to taste — the author frames this as a starter chain.

## Notes
- Concrete module/effect assignments + order are published; knob values are left to taste by the author.
- Calibrate at MEDIUM/HIGH headroom — the signal here is already processed and hot.

## Sources
- research/links/wolfewithane-why-buy-chroma-console-chain-recipes.md (https://wolfewithane.com/why-hologram-chroma-console)
- Ref: wolfewithane — "Why would I buy this pedal?"
- Transformed from Pedalxly Chroma-Console-Patches.md (community)
