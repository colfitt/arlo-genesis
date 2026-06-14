---
type: patch
title: Banjo Lead Doubler
device: Strymon Deco V2
date: 2026-06-14
description: Softening the banjo's hard pluck attack into a swelling doubled lead voice inside a wall — banjo-as-lead, kept dark so it doesn't ice-pick.
tags: [banjo, lead, doubler, dark, designed, signature]
hidden:
  Low Trim: 11:00 (up; ~60-90 Hz cut to keep low-mids clean under the lead)
  Doubletracker Boost/Cut: 12:00
controls:
  - { name: "Tape Saturation", type: switch, value: "ON (light glue)", options: ["ON","OFF"] }
  - { name: "Doubletracker", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "Voice", type: switch, value: "classic (cassette if it needs more body)", options: ["classic","cassette"] }
  - { name: "Saturation", type: knob, value: "~10:00 (warming, not driving)" }
  - { name: "Tone", type: knob, value: "~10-11:00 (dark)" }
  - { name: "Type", type: switch, value: "sum (cleanest, no warble artifact on the melody)", options: ["sum","invert","bounce"] }
  - { name: "Lag Time", type: knob, value: "chorus ~12:00 (~20-30 ms doubling)" }
  - { name: "Blend", type: knob, value: "~10:00 (favor Reference — DOUBLE not effect)" }
  - { name: "Wobble", type: knob, value: "~9:00 (very low — softens attack without seasick pitch)" }
  - { name: "Slot/Bank", type: knob, value: "PC17" }
---

# Banjo Lead Doubler

## Concept
Purpose-built for the GK-5/EBM-5 banjo lead voice — the one source where the Deco's pluck-softening genuinely helps the melody read inside a drone. Light glue plus a clean sum double softens the banjo's hard pluck attack into a swelling doubled lead, kept dark so it doesn't ice-pick. Favor Reference and keep Wobble low so it doubles, not effects.

## How to play it
1. Engage Tape Saturation (light glue) and Doubletracker. Voice classic (cassette if it needs more body).
2. Saturation ~10:00 (warming, not driving), Tone ~10–11:00 (dark — banjo top-end is already tamed upstream).
3. Hold Tape Saturation ON, turn TONE to set Low Trim up ~11:00 (~60–90 Hz cut to keep low-mids clean under the lead).
4. Doubletracker: Type sum (cleanest, no warble artifact on the melody), Lag Time ~12:00 (~20–30 ms doubling), Blend ~10:00 (favor Reference = DOUBLE not effect), Wobble ~9:00 (very low).
5. Hold Tape Saturation ON, turn BLEND to set Doubletracker Boost/Cut to 12:00.

## Notes
- Keep Wobble low: past mid gets seasick on held lead notes.
- The one source where pluck-softening genuinely helps the melody read inside a drone.

## Sources
- Designed from UsageGuide §5 (banjo: Low Trim + dark Tone; "doubletracker's chorus/wobble softens the banjo's hard attack into something that swells")
- DeepResearch §6 + taste-profile banjo-as-lead lens
- Wobble-low/Blend-favor-Reference = Celi/Superdanger "doubling not warble"
- Transformed from Pedalxly Deco-V2-Patches.md (DOUG-designed)
