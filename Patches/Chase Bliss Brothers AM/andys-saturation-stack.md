---
type: patch
title: "Andy's Saturation Stack — distortion fed by overdrive"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: AndyDemos' "saturation" approach for when you want more compression/saturation instead of more volume — DISTORTION on Channel 2 (left) with OVERDRIVE on Channel 1 (right) feeding all the extra gain into it; it doesn't add a volume boost, it adds gain and compression so everything sounds "meatier and bigger."
tags: [overdrive, distortion, stacked, saturation, two-channel, community]
dips:
  MASTER: "on (the goal is more gain/compression, NOT a volume boost — MASTER keeps level put)"
controls:
  - { name: "CHANNEL 1 MODE", type: switch, value: "OVERDRIVE, right channel — adds the extra gain feeding Channel 2", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "~halfway (Andy: 'about halfway on both' to stay detailed when stacked) — otherwise dial from recipe" }
  - { name: "VOL 1", type: knob, value: "push into Channel 2 — dial from recipe" }
  - { name: "TONE 1", type: knob, value: "to taste — dial from recipe" }
  - { name: "CHANNEL 2 MODE", type: switch, value: "DISTORTION, left channel — the saturated output", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 2", type: knob, value: "~halfway (Andy: 'about halfway on both' to stay detailed when stacked) — otherwise dial from recipe" }
  - { name: "VOL 2", type: knob, value: "master — dial from recipe" }
  - { name: "TONE 2", type: knob, value: "to taste — dial from recipe" }
  - { name: "PRESENCE", type: knob, value: "~25% down on a spanky guitar (hold footswitch + reduce presence), else DOWN" }
  - { name: "Both channels", type: switch, value: "ON — Channel 1 (OD) pushes Channel 2 (DIST)" }
---

# Andy's Saturation Stack — distortion fed by overdrive

## Concept
AndyDemos' "saturation" approach for when you want more compression and saturation instead of more volume: DISTORTION on the left channel (Channel 2) with OVERDRIVE on the right (Channel 1) feeding it all the extra gain. It doesn't add a volume boost — it adds gain and compression so everything sounds meatier and bigger. The counterpart to Andy's organic boost-at-end stack: this one chases saturation and compression, that one chases dynamic amp push.

## How to play it
1. Set Channel 2 (left) to DISTORTION and Channel 1 (right) to OVERDRIVE.
2. Stack both — the OVERDRIVE feeds extra gain into the DISTORTION.
3. Aim for more gain and compression, NOT more volume — Andy notes it makes everything "meatier and bigger" without a volume jump.
4. Run gain ~halfway on both to stay detailed; turn the MASTER dip on so the stack adds saturation, not level.

## Notes
- AndyDemos-quoted: the modes and the "more gain/compression not volume" intent are quoted; "about halfway on both" is the only knob hint Andy gives — otherwise dial from recipe. No published values; treat all clocks as a dialable recipe.
- The counterpart to Andy's organic boost-at-end stack: this one chases saturation/compression, that one chases dynamic amp push.
- More compression compounds on an already-squished source (e.g. after a Muff) — go easy if stacking downstream of a fuzz.
- Slot: intended as a MIDI preset (suggested).

## Sources
- research/transcripts/andy-brothers-am-demo.md ("DISTORTION mode on the left and OVERDRIVE on the right to add all that extra gain… not really adding extra volume… just more gain and compression… meatier and bigger")
- research/links/andy-demo-settings.md ("Saturation stack")
- Ref: AndyDemos — Chase Bliss Brothers AM (2025-04-15)
- Transformed from Pedalxly Brothers-AM-Patches.md (community)
