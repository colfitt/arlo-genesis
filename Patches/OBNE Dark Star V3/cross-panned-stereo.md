---
type: patch
title: Cross-panned stereo (invert Spread vs downstream ping-pong)
device: OBNE Dark Star V3
date: 2026-06-14
description: Extra-wide, complex stereo bed — dry on one side while its wet plays on the other, Spread fully CCW to invert the wet image against a downstream ping-pong delay.
tags: [stereo, spread, width, routing, community, signature]
controls:
  - { name: "Spread", type: knob, value: "fully CCW (inverts WET image only, not dry); center = both reverbs summed to both outs; full CW = normal L/R" }
  - { name: "Multiply", type: knob, value: "interesting crosstalk with Spread inversion (OBNE official)" }
  - { name: "Routing", type: switch, value: "Stereo", options: ["Mono", "Mono-In-Stereo-Out", "Stereo"] }
---

# Cross-panned stereo (invert Spread vs downstream ping-pong)

## Concept
An extra-wide, complex stereo bed — dry on one side while its wet plays on the other. With Routing = Stereo and Spread fully CCW, a right-channel note's reverb lands on the LEFT out while its dry stays right (only the wet image inverts, not the dry). Run against a downstream ping-pong delay so every right ping yields reverb on the left and vice versa.

## How to play it
1. Set Routing = Stereo.
2. Turn Spread fully CCW to invert the wet image only.
3. Feed a downstream ping-pong delay so the inverted wet and the ping-pong interplay.
4. For comparison: Spread at center sums both reverbs to both outs; full CW = normal L/R.

## Notes
- UsageGuide §5 ties this to feeding Board 3's ping-pong delays before the tape stage.
- "Interesting crosstalk with Multiply" (OBNE official).
- A routing technique, not a slot recall — width before the print stage.

## Sources
- research/transcripts/mark-johnston-secret-weapons-dark-star-stereo.md + manual p.2
- Transformed from Pedalxly Dark-Star-V3-Patches.md (community)
