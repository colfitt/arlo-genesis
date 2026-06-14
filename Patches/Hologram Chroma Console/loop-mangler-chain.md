---
type: patch
title: Loop-Mangler Chain
device: Hologram Chroma Console
date: 2026-06-14
description: Destroying a Blooper banjo/drum loop (AltWire) — build the weirdness gradually with REELS → Movement → Fuzz → Filter rather than all four at once.
tags: [glitch, chaos, loop, recorded-wrong, community, signature]
hidden:
  Module order: DIFFUSION REELS → MOVEMENT (vibrato/phaser/tremolo) → CHARACTER FUZZ → TEXTURE FILTER
controls:
  - { name: "Diffusion effect", type: switch, value: "REELS", options: ["REELS", "CASCADE", "SPACE", "REVERSE", "COLLAGE"] }
  - { name: "Movement effect", type: switch, value: "VIBRATO / PHASER / TREMOLO", options: ["VIBRATO", "PHASER", "TREMOLO", "PITCH", "DOUBLER"] }
  - { name: "Character effect", type: switch, value: "FUZZ", options: ["FUZZ", "SWEETEN", "SWELL", "HOWL"] }
  - { name: "Texture effect", type: switch, value: "FILTER", options: ["FILTER", "CASSETTE", "SQUASH", "BROKEN", "INTERFERENCE"] }
  - { name: "Slot/Bank", type: knob, value: "D5" }
---

# Loop-Mangler Chain

## Concept
A chain-order template for destroying a Blooper banjo/drum loop — build the weirdness gradually rather than slamming all four modules at once. "Feed a beat through Reels and Movement, then once you're comfortable with the weirdness, take it through Fuzz and Filter."

## How to play it
1. Set the module order on a beat/loop source: **DIFFUSION REELS → MOVEMENT (vibrato/phaser/tremolo) → CHARACTER FUZZ → TEXTURE FILTER.**
2. Start with REELS + MOVEMENT only.
3. Once comfortable with the weirdness, bring in FUZZ + FILTER.
4. Per-knob amounts to taste.

## Notes
- Chain-order template; no knob values published (author frames it as exploration).

## Sources
- research/links/altwire-chroma-console-review-chain-order-recipe.md (https://altwire.net/chroma-console-by-hologram-electronics-review/)
- Ref: AltWire (Derek Oswald) review
- Transformed from Pedalxly Chroma-Console-Patches.md (community)
