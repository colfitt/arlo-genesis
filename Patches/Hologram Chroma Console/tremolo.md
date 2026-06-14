---
type: patch
title: Tremolo
device: Hologram Chroma Console
date: 2026-06-14
description: A back-pocket tremolo so no dedicated trem pedal is needed on the board (Sam Wittek "Tremolo") — TREMOLO from shimmer to square chop, RATE locks to tempo when MIDI-synced.
tags: [modulation, tremolo, utility, community]
hidden:
  MIDI sync: trem RATE locks to tempo when MIDI-synced
controls:
  - { name: "Movement effect", type: switch, value: "TREMOLO", options: ["TREMOLO", "VIBRATO", "PHASER", "PITCH", "DOUBLER"] }
  - { name: "Movement RATE", type: knob, value: "to taste (locks to tempo when MIDI-synced)" }
  - { name: "Movement AMOUNT", type: knob, value: "to taste (shimmer → square chop)" }
  - { name: "Slot/Bank", type: knob, value: "D8" }
---

# Tremolo

## Concept
A back-pocket tremolo so no dedicated trem pedal is needed on the board. MOVEMENT TREMOLO runs from a gentle shimmer to a square chop, and when MIDI-synced the trem RATE locks to tempo.

## How to play it
1. MOVEMENT **TREMOLO**.
2. Set RATE/AMOUNT to taste (shimmer → square chop).
3. When MIDI-synced, the trem RATE locks to tempo.

## Notes
- Untagged — a clean utility trem (left untagged on purpose).
- Wittek preset; recipe only.
- For a *harmonic* trem instead, see the Harmonic Tremolo patch.

## Sources
- research/transcripts/sam-wittek-chroma-preset-showcase.md; research/links/sam-wittek-chroma-preset-pack-multitracks.md
- Ref: Sam Wittek — SW Chroma Console pack ("Tremolo")
- Transformed from Pedalxly Chroma-Console-Patches.md (community)
