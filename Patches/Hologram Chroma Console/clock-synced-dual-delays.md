---
type: patch
title: Clock-Synced Dual Delays
device: Hologram Chroma Console
date: 2026-06-14
description: Two interlocking delay subdivisions locked to one clock (in-rig port of Wittek's "Analog") — REELS/CASCADE eighth-note off the Digitakt clock against a dotted-eighth on the downstream TimeLine; TIME-up extends echoes over a slow clock.
tags: [delay, rhythmic, ambient, midi-clock, community]
hidden:
  MIDI clock sync: EIGHTH-note off the Digitakt clock (slaved); DOTTED-EIGHTH on downstream TimeLine off the same clock
controls:
  - { name: "Diffusion effect", type: switch, value: "REELS or CASCADE", options: ["REELS", "CASCADE", "SPACE", "REVERSE", "COLLAGE"] }
  - { name: "Diffusion TIME", type: knob, value: "eighth-note synced; turn UP to multiply/extend beyond tapped tempo" }
  - { name: "Diffusion AMOUNT", type: knob, value: "to taste" }
  - { name: "Slot/Bank", type: knob, value: "D2" }
---

# Clock-Synced Dual Delays

## Concept
Two interlocking delay subdivisions locked to one clock — bouncy rhythmic/ambient delay across two pedals. The Chroma runs an eighth-note off the Digitakt's MIDI clock while the downstream TimeLine runs a dotted-eighth off the same clock. Turning TIME upward multiplies/extends the delay beyond the tapped tempo for long evolving echoes over a slow clock.

## How to play it
1. DIFFUSION **REELS** or **CASCADE**, clock-synced to an **EIGHTH-note** off the Digitakt's MIDI clock.
2. Run a **DOTTED-EIGHTH** on the downstream TimeLine off the same clock.
3. **Tap-tempo extension:** turn **TIME** upward to multiply/extend the delay beyond the tapped tempo for long evolving echoes over a slow clock.

## Notes
- In-rig port of Wittek's "Analog" method; method, not numerics.
- The TIME-extension trick is wolfewithane's.

## Sources
- research/Chroma-Console-UsageGuide.md §5; research/links/wolfewithane-blog-chroma-console-usage-tips.md
- Ref: Sam Wittek (method) / wolfewithane
- Transformed from Pedalxly Chroma-Console-Patches.md (community)
