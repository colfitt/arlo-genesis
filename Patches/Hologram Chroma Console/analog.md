---
type: patch
title: Analog
device: Hologram Chroma Console
date: 2026-06-14
description: Warm, bouncy rhythmic/ambient delay with modulation blooming on later repeats (Sam Wittek "Analog") — CASCADE BBD delay synced to an eighth-note, stacked against a dotted-eighth on a downstream TimeLine off one MIDI clock.
tags: [delay, analog, rhythmic, ambient, midi-clock, community]
hidden:
  MIDI clock sync: EIGHTH-note subdivision (slaved); stacked vs DOTTED-EIGHTH on downstream Strymon TimeLine off the same clock
controls:
  - { name: "Diffusion effect", type: switch, value: "CASCADE", options: ["CASCADE", "REELS", "SPACE", "REVERSE", "COLLAGE"] }
  - { name: "Diffusion TIME", type: knob, value: "to taste (eighth-note when clock-synced)" }
  - { name: "Diffusion AMOUNT", type: knob, value: "to taste (more repeats = more modulation)" }
  - { name: "Slot/Bank", type: knob, value: "D1" }
---

# Analog

## Concept
A warm, bouncy rhythmic/ambient delay where modulation blooms on the later repeats — the dual-delay-against-another-pedal trick. DIFFUSION CASCADE is a warm BBD/analog delay ("the more repeats, the more modulation"), MIDI-clock-synced to an eighth-note and stacked against a dotted-eighth on a downstream Strymon TimeLine, both off one MIDI clock.

## How to play it
1. DIFFUSION **CASCADE** (warm BBD/analog delay).
2. MIDI-clock-sync the Chroma to an **EIGHTH-note** subdivision.
3. Run a **DOTTED-EIGHTH** on the downstream Strymon TimeLine off the same clock.

## Notes
- Wittek's personal favorite of the set. PDF knob positions NOT on disk; recipe only.
- In-rig port = Chroma + TimeLine off the Digitakt's clock.

## Sources
- research/transcripts/sam-wittek-chroma-preset-showcase.md; research/links/sam-wittek-chroma-preset-pack-multitracks.md
- Ref: Sam Wittek — SW Chroma Console pack ("Analog")
- Transformed from Pedalxly Chroma-Console-Patches.md (community)
