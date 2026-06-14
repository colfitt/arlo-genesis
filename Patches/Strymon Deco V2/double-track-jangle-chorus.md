---
type: patch
title: Double-Track Jangle Chorus (Brock thick clean)
device: Strymon Deco V2
date: 2026-06-14
description: Modest Mouse double-tracked thick-chorus jangle + stereo-tremolo movement (approximated) — Deco wobble + Wide-Stereo doubler stands in for Brock's stereo tremolo, NOT the real chop.
tags: [jangle, chorus, indie, stereo, designed, artist-modest-mouse, signature]
hidden:
  Wide Stereo Mode: on (Live-Edit, hold Tape Saturation ON, turn WOBBLE right of 12:00; needs stereo out)
controls:
  - { name: "Tape Saturation", type: switch, value: "ON (light glue)", options: ["ON","OFF"] }
  - { name: "Doubletracker", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "Voice", type: switch, value: "classic", options: ["classic","cassette"] }
  - { name: "Saturation", type: knob, value: "~10:00 (warming, not driving)" }
  - { name: "Tone", type: knob, value: "~12:00 (keep the brittle top)" }
  - { name: "Type", type: switch, value: "sum (cleanest double, no warble on the melody)", options: ["sum","invert","bounce"] }
  - { name: "Lag Time", type: knob, value: "~12:00 (~20-30 ms doubling -> natural thick chorus)" }
  - { name: "Blend", type: knob, value: "~11:00 (favor Reference = DOUBLE not warble)" }
  - { name: "Wobble", type: knob, value: "~9-10:00 (low — tape movement standing in for stereo tremolo)" }
  - { name: "Slot/Bank", type: knob, value: "PC21" }
---

# Double-Track Jangle Chorus (Brock thick clean)

## Concept
A designed-to-emulate build for Modest Mouse's double-tracked thick-chorus jangle plus stereo-tremolo movement. A clean sum double at ~20–30 ms gives the natural thick chorus; Wide Stereo Mode supplies the L/R width of a double-tracked pair. EXPLICIT APPROXIMATION: Brock's signature movement is a stereo TREMOLO (Seymour Duncan Shape Shifter) — no tremolo box in the target list, so the Deco wobble + Wide-Stereo doubler is the nearest approximation, NOT the real amplitude chop. Use the rig's actual tremolo (BF-3) for the true effect.

## How to play it
1. Engage Tape Saturation (light glue) and Doubletracker. Voice classic.
2. Saturation ~10:00 (warming, not driving), Tone ~12:00 (keep the brittle top).
3. Doubletracker: Type sum (cleanest double, no warble on the melody), Lag Time ~12:00 (~20–30 ms doubling), Blend ~11:00 (favor Reference = DOUBLE not warble), Wobble ~9–10:00 (low — a touch of tape movement standing in for the stereo tremolo).
4. Enable Wide Stereo Mode: hold Tape Saturation ON, turn WOBBLE right of 12:00 for the L/R width of a double-tracked pair (needs stereo out).

## Notes
- Designed-to-emulate + EXPLICIT APPROXIMATION flag: this approximates the thickness/movement, not the amplitude chop. Use BF-3 for the real tremolo.
- Needs stereo out for the Wide Stereo width.

## Sources
- Designed from Deco doubletracker (Blend-favor-Reference = double not warble, Celi/Superdanger) + Wide Stereo Mode
- Research/Taste-Profile/sources/modest-mouse-brock-jangly-clean-tone-gear.md, brock-anti-precious-stereo-tremolo-amp-settings.md
- Ref: DEC-LF1 — Modest Mouse, double-tracked lead → "natural thick chorus" + stereo tremolo (approximation)
- Transformed from Pedalxly Deco-V2-Patches.md (DOUG-designed)
