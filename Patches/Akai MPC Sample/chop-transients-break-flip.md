---
type: patch
title: Chop → Transients — Break-Flip
device: Akai MPC Sample
date: 2026-06-14
description: Flipping a drum break (or a fuzz-wall / banjo phrase) into a new re-sequenceable pattern using transient-detected slices.
tags: [sampling, chop, break-flip, factory, signature]
controls:
  - { name: "Chop mode", type: switch, value: "By Transients", options: ["By Transients", "Manual", "Regions"] }
  - { name: "Threshold (Shift+K3)", type: knob, value: "0–100% (higher = fewer slices)" }
  - { name: "Slice edit", type: knob, value: "enter slice → edit start/end with the knobs" }
  - { name: "Zoom (Shift + encoder)", type: button, value: "zooms straight to the transient" }
  - { name: "Chop toggle", type: switch, value: "off = original break; on = slices", options: ["off", "on"] }
  - { name: "Slot/Bank", type: knob, value: "16 pads (chop layout)" }
---

# Chop → Transients — Break-Flip

## Concept
Flipping a drum break — or a fuzz-wall / banjo phrase — into a new re-sequenceable pattern. Transient detection finds peaks and spreads slices across 16 pads, which you re-order over the loop. The Threshold control (`Shift+K3`) trades slice count for cleanliness.

## How to play it
1. Select sample → press Chop → mode = By Transients (detects peaks; `Shift+K3` = Threshold 0–100%, higher = fewer slices).
2. Slices spread across 16 pads. Re-sequence them in a new order over the loop.
3. Tighten each slice: enter the slice → edit start/end with the knobs; `Shift` + encoder zooms straight to the transient.
4. Chop off = original break; Chop on = slices.

## Notes
- Threshold detection is laggy/sample-dependent — fix split points by hand.
- LIMITATION: chopped slices share pitch/filter — use Extract (patch "Extract Slice to Own Pad") to edit one independently.

## Sources
- 🟢 `research/transcripts/akaipro-mpc-sample-chop-mode.md` + `research/transcripts/akaipro-mpc-sample-chopping-drum-breaks.md`
- Transformed from Pedalxly MPC-Sample-Patches.md (factory)
