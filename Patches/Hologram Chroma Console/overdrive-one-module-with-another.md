---
type: patch
title: Overdrive One Module With Another
device: Hologram Chroma Console
date: 2026-06-14
description: Deliberate soft-clip by pushing one module hot into the next (wolfewithane) — the Chroma is a 4-channel mixer; push EFFECT VOL near the headroom limit and hold unity with OUTPUT LEVEL.
tags: [drive, gain-staging, soft-clip, community, signature]
hidden:
  EFFECT VOL (Character) CC73: pushed hot into the next module
  EFFECT VOL (Movement) CC75: pushed hot into the next module
  EFFECT VOL (Diffusion) CC77: pushed hot into the next module
  EFFECT VOL (Texture) CC79: pushed hot into the next module
  OUTPUT LEVEL CC78: held to unity
  Calibration: re-calibrate to a hotter signal (e.g. Board-1 fuzz upstream)
controls:
  - { name: "Effect Vol (per module)", type: knob, value: "push hot into the next module for deliberate soft-clip near the headroom limit" }
  - { name: "Output Level", type: knob, value: "set to hold unity" }
  - { name: "Slot/Bank", type: knob, value: "A7" }
---

# Overdrive One Module With Another

## Concept
The Chroma is a 4-channel mixer, so you can push one module's EFFECT VOL hot into the next for a deliberate soft-clip near the headroom limit. Manage the gain stage with OUTPUT LEVEL and per-module EFFECT VOL to hold unity, and re-calibrate to a hotter signal when a fuzz feeds it.

## How to play it
1. Push a module's **EFFECT VOL** (secondary layer, A+B) hot into the next module for deliberate soft-clip near the headroom limit.
2. Manage with **OUTPUT LEVEL** + per-module EFFECT VOL to hold unity.
3. Re-calibrate to a hotter signal (e.g. Board-1 fuzz upstream).

## Notes
- Use the soft-clip deliberately for grit, or back off to stay clean.
- **CCs:** EFFECT VOL Character **73** / Movement **75** / Diffusion **77** / Texture **79**; OUTPUT LEVEL **78** (confirmed against the MIDI map).

## Sources
- research/links/wolfewithane-blog-chroma-console-usage-tips.md; research/links/chroma-console-midi-cc-implementation-manual.md
- Ref: wolfewithane
- Transformed from Pedalxly Chroma-Console-Patches.md (community)
