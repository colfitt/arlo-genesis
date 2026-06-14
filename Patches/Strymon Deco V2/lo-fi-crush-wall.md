---
type: patch
title: Lo-Fi Crush Wall
device: Strymon Deco V2
date: 2026-06-14
description: Maximum chord-density doom glue on the source — dark, compressed, warty; the closest factory-ish voice to the rig's degrade/doom lean before handing off to Generation Loss.
tags: [doom, lo-fi, drone, dark, glue, designed, signature]
hidden:
  Low Trim: 12-1:00 (up; cut to ~80-120 Hz so the baritone doesn't flab the wall)
  Doubletracker Boost/Cut: 12:00 (unity, so the double doesn't overpower)
controls:
  - { name: "Tape Saturation", type: switch, value: "ON (heavy)", options: ["ON","OFF"] }
  - { name: "Doubletracker", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "Voice", type: switch, value: "cassette", options: ["classic","cassette"] }
  - { name: "Saturation", type: knob, value: "~2:00 (heavy — past the deck-limit point, into extended-gain range)" }
  - { name: "Tone", type: knob, value: "~11:00 (dark)" }
  - { name: "Volume", type: knob, value: "to unity" }
  - { name: "Type", type: switch, value: "bounce", options: ["sum","invert","bounce"] }
  - { name: "Lag Time", type: knob, value: "~12-1:00 (slapback, ~50-100 ms)" }
  - { name: "Blend", type: knob, value: "~11:00 (favor Reference — density not echo)" }
  - { name: "Wobble", type: knob, value: "~12-1:00 (warped-tape movement)" }
  - { name: "Slot/Bank", type: knob, value: "PC12" }
---

# Lo-Fi Crush Wall

## Concept
Cassette + heavy saturation deliberately compressed and dark, with a warbly bounce double layered for density. Pushed to ~2:00 — past the "slamming the VU" point Celi calls the deck's real limit, into the extended-gain range. Built so that downstream Generation Loss / PORTA424 ruin reads as intentional. The Deco itself stays well-behaved (it won't self-oscillate); the actual destruction is the End-Board's job.

## How to play it
1. Engage Tape Saturation (heavy) and Doubletracker.
2. Voice cassette, Saturation ~2:00, Tone ~11:00 (dark), Volume to unity.
3. Hold Tape Saturation ON until LEDs flash, then turn TONE to set Low Trim up ~12–1:00 (cut to ~80–120 Hz so the baritone doesn't flab the wall).
4. Doubletracker: Type bounce (most warbly/lo-fi per Gueringer), Lag Time ~12–1:00, Blend ~11:00, Wobble ~12–1:00.
5. Hold Tape Saturation ON, turn BLEND to set Doubletracker Boost/Cut to 12:00 (unity) so the double doesn't overpower.

## Notes
- Cassette + heavy is intentionally compressed/dark — the warts are the point.
- The Deco won't self-oscillate; lean on the End-Board for the actual destruction.
- Guitar Chalk #5 "Crushed Lo-Fi" (Sat 9, Tone 2, Wobble 9) directionally agrees but is QC-flagged (SEO/AI source) — A/B by ear.

## Sources
- Designed from DeepResearch §13(d) "Saturated wall-thickener" + taste-profile lo-fi cluster + Gueringer Bounce=most-warble ranking + Celi "~2:00 = deck limit, extended beyond"
- Cross-checks Guitar Chalk #5 "Crushed Lo-Fi" (Sat 9, Tone 2, Wobble 9 — directionally agrees, QC-flagged)
- Transformed from Pedalxly Deco-V2-Patches.md (DOUG-designed)
