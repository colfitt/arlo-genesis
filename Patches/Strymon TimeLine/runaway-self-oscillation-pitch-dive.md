---
type: patch
title: Runaway self-oscillation / pitch-dive
device: Strymon TimeLine
date: 2026-06-14
description: Chaotic, building, pitch-bending feedback used as its own instrument (Rhett Shull) — put the guitar down and play the pedal by sweeping TIME.
tags: [self-oscillation, pitch-dive, feedback, chaos, performance, artist, signature]
hidden:
  EXP → REPEATS: ride to swell into oscillation
controls:
  - { name: "TYPE", type: switch, value: "dTape (or dBucket/Digital)", options: ["dTape","dBucket","Digital","Dual","Pattern","Reverse","Ice","Lo-Fi","Swell","Trem","Filter","Duck"] }
  - { name: "TIME", type: knob, value: "any (then sweep for the pitch dive/rise)" }
  - { name: "MIX", type: knob, value: "up" }
  - { name: "REPEATS", type: knob, value: "past ~3:00 (feedback >100% → self-oscillation)" }
  - { name: "EXP", type: button, value: "ride → REPEATS to swell into it" }
  - { name: "Slot/Bank", type: knob, value: "any" }
---

# Runaway self-oscillation / pitch-dive

## Concept
Chaotic, building, pitch-bending feedback used as its own instrument: push REPEATS past ~3:00 so feedback regenerates above 100% and tips into self-oscillation, then sweep the TIME knob for the classic pitch dive/rise. Put the guitar down and play the pedal.

## How to play it
1. Set MIX up and push REPEATS past ~3:00 so it tips into self-oscillation.
2. Sweep the TIME knob for the pitch dive/rise.
3. Ride EXP → REPEATS to swell into and out of the oscillation.

## Notes
- Machine character: Digital cleanest/brightest, dBucket darker/warmer fuzz, dTape most pitch drift.
- Also see Matt Trojak's self-osc demo.

## Sources
- Rhett Shull — "5 Delay Tricks" (YouTube v8Kbmcvnmf0); also Matt Trojak self-osc demo
- research/transcripts/rhett-shull-timeline-5-delay-tricks.md + research/links/community-timeline-hidden-features-oscillation.md
- Transformed from Pedalxly TimeLine-Patches.md (community)
