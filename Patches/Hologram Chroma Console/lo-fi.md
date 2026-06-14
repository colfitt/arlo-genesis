---
type: patch
title: Lo-Fi
device: Hologram Chroma Console
date: 2026-06-14
description: Chewy lo-fi wobble that blends into the background (Sam Wittek "Lo-Fi") — PITCH-based irregular vibrato plus a FILTER high-roll-off for degraded/recorded-wrong glue.
tags: [lo-fi, wobble, glue, degraded, community, signature]
hidden:
  Texture FILTER style: LOW PASS (LPF zone, ~7–10 o'clock)
controls:
  - { name: "Movement effect", type: switch, value: "PITCH", options: ["PITCH", "VIBRATO", "PHASER", "TREMOLO", "DOUBLER"] }
  - { name: "Movement AMOUNT", type: knob, value: "to taste (chewy irregular wobble)" }
  - { name: "Texture effect", type: switch, value: "FILTER", options: ["FILTER", "CASSETTE", "SQUASH", "BROKEN", "INTERFERENCE"] }
  - { name: "Texture AMOUNT", type: knob, value: "LPF rolling off highs, ~7–10 o'clock" }
  - { name: "Slot/Bank", type: knob, value: "A3" }
---

# Lo-Fi

## Concept
A chewy lo-fi wobble that blends into the background. Wittek's "vibrato" here is actually the PITCH effect, which gives an irregular/intermittent waveform rather than a smooth sine — paired with a FILTER rolling off the highs ("like turning the tone knob down"), the result is degraded/recorded-wrong glue.

## How to play it
1. MOVEMENT — build on the **PITCH** effect (not VIBRATO) for an irregular/intermittent wobble.
2. TEXTURE **FILTER** in the LPF zone (~7–10 o'clock) rolling off the highs.
3. Result: "chewy vibrato that sounds really lo-fi … blends into the background."

## Notes
- Recipe/intent only — the Wittek PDF of knob positions is NOT on disk, so no clock-face numbers are available. The PITCH-vs-VIBRATO distinction is the load-bearing detail.

## Sources
- research/transcripts/sam-wittek-chroma-preset-showcase.md; research/links/sam-wittek-chroma-preset-pack-multitracks.md
- Ref: Sam Wittek — SW Chroma Console pack ("Lo-Fi")
- Transformed from Pedalxly Chroma-Console-Patches.md (community)
