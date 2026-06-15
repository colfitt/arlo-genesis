---
type: patch
title: "Booster Trim Setup — tune the Rangemaster after a buffer"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: "A CB-blessed setup/utility patch using the three official internal treble-booster trims (impedance/output/bias). When buffers sit in front of the AM, back the Input-Impedance trim counter-clockwise so the booster \"behaves much better after a buffer,\" then use Output (CW hits the KOT harder, CCW for a unity feel) and Bias (headroom / Rangemaster break-up symmetry) to dial the booster's character. A blessed tweak, not a mod — no exact settings published beyond defaults/directions, so dial by ear."
tags: [treble-booster, rangemaster, internal-trims, setup, utility, designed]
hidden:
  Input-Impedance trim: "default fully CW; back CCW after a buffer (booster \"behaves much better after a buffer\")"
  Output trim: "default noon; CW = harder into the KOT, CCW = more unity feel"
  Bias trim: "default noon; adjust headroom / Rangemaster break-up symmetry"
controls:
  - { name: "TREBLE BOOSTER", type: switch, value: "DOWN (classic Rangemaster — while setting trims)", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
  - { name: "CHANNEL 1 MODE", type: switch, value: "BOOST or OVERDRIVE (so you can hear the booster)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "dial from recipe — no published clock values" }
  - { name: "VOL 1", type: knob, value: "dial from recipe — no published clock values" }
  - { name: "TONE 1", type: knob, value: "dial from recipe — no published clock values" }
---

# Booster Trim Setup — tune the Rangemaster after a buffer

## Concept
The Brothers AM's treble booster has three official internal trimmers that Chase Bliss documents and blesses: Input Impedance, Output, and Bias. These are not a mod — they are the intended way to fit the Rangemaster-style booster to your rig. The load-bearing one is Input Impedance: when buffered pedals sit upstream, backing it counter-clockwise from its default fully-CW makes the booster "behave much better after a buffer." Output sets how hard the booster drives the KOT-style front end (CW = harder, CCW = more unity), and Bias sets headroom and how symmetrical the Rangemaster break-up is. This is a setup/utility patch for dialing booster character, not a performance preset — and since no exact trim settings are published beyond the defaults and directions, you tune it by ear.

## How to play it
1. Pop the back cover. Set the TREBLE BOOSTER DOWN (classic Rangemaster) and run Channel 1 in BOOST or OVERDRIVE so you can hear the booster.
2. If buffers sit in front of the AM, back the Input-Impedance trim CCW from its default fully-CW so the booster behaves well after a buffer.
3. Use the Output trim to set drive into the KOT: CW hits it harder, CCW for a more unity feel.
4. Use the Bias trim for headroom / how symmetrical the Rangemaster break-up is. Make tiny movements with a small flathead — easy to damage.

## Notes
- CB-official + manual: the three trims, their defaults, and their directions are quoted; no exact settings are published beyond the defaults/directions — dial by ear. Front-panel knob clocks are NOT sourced, so treat GAIN/VOL/TONE 1 as a dialable recipe.
- The Input-Impedance-after-a-buffer adjustment is the load-bearing one when buffered pedals sit upstream (relevant in this rig — CB Clean + Colour Box buffer the front end).
- These mirror the real King of Tone / Prince of Tone internal trims — a blessed tweak, not a mod. Fragile: tiny moves only, small flathead, easy to damage.

## Sources
- research/links/treble-booster-internal-trims.md (CB official: 3 trims — impedance/output/bias; "behaves much better after a buffer")
- research/links/guitar-com-big-review-tips.md (internal trims: impedance/output/bias; treble/presence trim with top tone)
- Brothers-AM-DeepResearch.md §11 (Internal Trimmers)
- Ref: Brothers AM manual, "Internal Trimmers"; chasebliss.com Facebook post
