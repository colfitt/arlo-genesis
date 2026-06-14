---
type: patch
title: Gen Loss → Reverb → EQ (degraded-but-not-muddy ambient)
device: Chase Bliss Generation Loss
date: 2026-06-14
description: Keeping a degraded ambient wash from going muddy — put an EQ AFTER the reverb so it cleans the lows while keeping the reverbed high harmonics.
tags: [source-specific, chain-trick, ambient, placement, community, signature]
controls:
  - { name: "Signal order", type: switch, value: "Gen Loss → reverb (H90) → EQ", options: ["Gen Loss → reverb → EQ"] }
---

# Gen Loss → Reverb → EQ (degraded-but-not-muddy ambient)

## Concept
Keeping a degraded ambient wash from going muddy: put an EQ **after** the reverb so it cleans the lows while keeping the reverbed high harmonics. Relevant here because the H90 reverb is downstream. This is a placement recipe rather than a stored knob state.

## How to play it
1. Set the signal order: **Gen Loss → reverb (H90) → EQ.**
2. Pair it with any degrade patch above (e.g. "Dying Cassette" #3 or "Filtered Lo-Fi" #10).
3. Use the post-reverb EQ to clean the low-mids that would otherwise turn to sludge.

## Notes
- 🔵 community — Elektronauts tip; no specific Gen Loss knob values (it's a placement recipe).
- n/a for Slot/Bank — this is chain placement, not a stored knob state.

## Sources
- 🔵 `research/links/genloss-community-tips-pitfalls.md` + UsageGuide §3.
- Transformed from Pedalxly Generation-Loss-Patches.md (community).
