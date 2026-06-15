---
type: patch
title: "Piera's Boost-Into-OD — more dirt, same volume"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: "Mike Piera's (Analog Man) alternate KOT stacking philosophy — run the BOOST into the OVERDRIVE rather than after it, so the boost slams the OD's input for more saturation without a big jump in overall volume. Artist-stated in a Guitar World interview; the deliberate counterpart to the boost-after-OD thickener."
tags: [overdrive, boost, stacked, saturation, king-of-tone, artist]
dips:
  MASTER: "off (optional on) — goal is more gain, not level; keep output put"
controls:
  - { name: "CHANNEL 1 MODE", type: switch, value: "BOOST (feeds the OD's input first via the AM's fixed series order)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "VOL 1", type: knob, value: "moderate — slam the OD's input, don't raise master (dial from recipe)" }
  - { name: "GAIN 1", type: knob, value: "to taste — how hard the boost hits the OD (dial from recipe)" }
  - { name: "TONE 1", type: knob, value: "to taste (dial from recipe)" }
  - { name: "CHANNEL 2 MODE", type: switch, value: "OVERDRIVE (receives the boosted signal)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 2", type: knob, value: "set for your OD voice (dial from recipe)" }
  - { name: "VOL 2", type: knob, value: "to taste — your OD/master level (dial from recipe)" }
  - { name: "TONE 2", type: knob, value: "to taste (dial from recipe)" }
  - { name: "PRESENCE", type: knob, value: "DOWN to start, bring UP if the saturated voice gets closed-in" }
---

# Piera's Boost-Into-OD — more dirt, same volume

## Concept
Mike Piera's (Analog Man) alternate King-of-Tone stacking philosophy: run the BOOST *into* the OVERDRIVE rather than after it, to push more distortion out of the OD channel WITHOUT a big jump in overall volume. This is the move for players who already have the level they need but want more saturation — the deliberate counterpart to the boost-after-OD thickener. In the AM's fixed series (Channel 1 → Channel 2), setting Channel 1 to BOOST and Channel 2 to OVERDRIVE makes the boost slam the OD's input for you.

## How to play it
1. Set Channel 1 to BOOST and Channel 2 to OVERDRIVE — the boost hits the OD's input first (the AM's series order does this for you).
2. Keep the boost's VOL moderate so it slams the OD rather than raising master volume.
3. Set GAIN 2 for your OD voice; the boosted input will push more saturation through it.
4. Result: more distortion/saturation from the OD with little additional volume.
5. Choose this vs boost-after-OD based on whether you want more GAIN (this) or more VOLUME (boost-after).

## Notes
- Artist-stated (Mike Piera, Guitar World): "others like to run the boost into the overdrive to add more distortion without too much additional volume" — no knob numbers are published, so all values here are a dialable recipe, not sourced settings.
- This is the gain-leaning counterpart to the boost-AFTER-OD approach (boost after the dirt = thicken + volume), covered by the existing Dan's Overdrive Boost patch. A separate DIST←OD pairing is the heavier "saturation stack" voice if you want more than the OD channel gives.
- The MASTER dip is optional: leave it off to keep this purely a gain change; turn it on only if you want VOL 2 to act as a global master and hold output put.
- Great for tightening into a higher-gain lead voice while staying at stage level.

## Sources
- https://www.guitarworld.com/gear/guitar-pedals/analogman-chase-bliss-brothers-am-interview (Piera: "most people, like me, like to run the boost after the overdrive… while others like to run the boost into the overdrive to add more distortion without too much additional volume")
- research/links/king-of-tone-lineage.md (KOT boost-into-dirt adds distortion vs boost-after-dirt adds volume)
- Ref: Guitar World — Analogman × Chase Bliss interview; Mike Piera (Analog Man)
