---
type: patch
title: Harmonic Tremolo
device: Hologram Chroma Console
date: 2026-06-14
description: A moving harmonic-tremolo / auto-filter without burning the Movement module (wolfewithane) — a tempo-synced FILTER gesture sweeping ~7→10 o'clock loops like DAW automation.
tags: [modulation, tremolo, filter, gesture, recorded-wrong, community, signature]
hidden:
  Texture FILTER style: LOW PASS (LPF zone)
  GESTURE (C+D): on FILTER AMOUNT, sweeping ~7 o'clock → 10 o'clock, tempo-synced (Tap Tempo / clock), then exit (loops)
controls:
  - { name: "Texture effect", type: switch, value: "FILTER", options: ["FILTER", "CASSETTE", "SQUASH", "BROKEN", "INTERFERENCE"] }
  - { name: "Texture AMOUNT", type: knob, value: "gestured ~7 o'clock → 10 o'clock, tempo-synced" }
  - { name: "Slot/Bank", type: knob, value: "D9" }
---

# Harmonic Tremolo

## Concept
A moving harmonic-tremolo / auto-filter that doesn't burn the Movement module — cheap and tempo-synced. TEXTURE FILTER (LPF zone) is driven by a recorded GESTURE on the FILTER AMOUNT knob sweeping ~7 o'clock → 10 o'clock, which loops like DAW automation for "a harmonic tremolo effect."

## How to play it
1. TEXTURE **FILTER** (LPF zone).
2. Record a **GESTURE (C+D)** on the FILTER AMOUNT knob sweeping **~7 o'clock → 10 o'clock**, tempo-synced (Tap Tempo / clock).
3. Exit — the gesture loops like DAW automation, producing a harmonic tremolo.

## Notes
- Tagged ⭐ — the gestured, recorded-wrong cousin of the plain trem.
- The 7a→10a sweep range is wolfewithane's concrete figure.

## Sources
- research/links/wolfewithane-blog-chroma-console-usage-tips.md; research/links/wolfewithane-why-buy-chroma-console-chain-recipes.md
- Ref: wolfewithane
- Transformed from Pedalxly Chroma-Console-Patches.md (community)
