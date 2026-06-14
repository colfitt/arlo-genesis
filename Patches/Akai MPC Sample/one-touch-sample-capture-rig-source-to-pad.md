---
type: patch
title: One-Touch Sample Capture — Rig Source → Pad
device: Akai MPC Sample
date: 2026-06-14
description: Capturing the banjo / baritone / fuzz-wall off the Apollo bus or the built-in mic straight onto a pad.
tags: [sampling, capture, rig-integration, factory, signature]
controls:
  - { name: "Sample Record Source", type: switch, value: "Rear (for stereo rig bus)", options: ["Mic", "Rear (1/4\" TRS line)", "USB", "Resample"] }
  - { name: "REC GAIN", type: knob, value: "set at the source (Apollo/Babyface, not on the box)" }
  - { name: "Length", type: switch, value: "Free vs Sequence (Sequence = exactly one sequence length)", options: ["Free", "Sequence"] }
  - { name: "Record format", type: knob, value: "24-bit / 44.1; max 20 min" }
  - { name: "Slot/Bank", type: knob, value: "Selected pad" }
---

# One-Touch Sample Capture — Rig Source → Pad

## Concept
Capturing the banjo, baritone, or fuzz-wall off the Apollo bus or the built-in mic onto a pad. For the stereo rig bus, Source = Rear (the rear 1/4" TRS line inputs). The built-in condenser mic is a fast/dirty room capture option (it auto-mutes the speaker). Records 24-bit/44.1, up to 20 minutes.

## How to play it
1. Sample Record → pick Source (Mic / rear 1/4" TRS line inputs / USB / Resample).
2. Set REC GAIN at the source (Apollo/Babyface, not on the box).
3. Tap a pad → record.
4. Choose Length = Free vs Sequence (Sequence grabs exactly one sequence length — clean for loops).
5. For the stereo rig bus: Source = Rear.

## Notes
- Rig-specific source-naming (banjo/baritone/fuzz wall via Apollo TRS) is the mapping.
- ⚠️ No stereo→mono on the box; you can't resample L or R only.

## Sources
- 🟢 `research/transcripts/akaipro-mpc-sample-overview.md` + `research/MPC-Sample-DeepResearch.md` §5/§6
- Transformed from Pedalxly MPC-Sample-Patches.md (factory)
