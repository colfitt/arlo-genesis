---
type: patch
title: CWO chorus (lush stereo, free the reverb slot)
device: TE OP-1 Field
date: 2026-06-14
description: Lush stereo chorus on high-sustain digital patches without a dedicated chorus slot — CWO with concrete community-verified values, value-LFO modulating the delay knob. Shoegaze-washed pads.
tags: [chorus, fx-recipe, shoegaze, width, community, signature]
controls:
  - { name: "FX", type: switch, value: "CWO" }
  - { name: "CWO freq", type: knob, value: "0" }
  - { name: "CWO delay", type: knob, value: "28" }
  - { name: "CWO feedback", type: knob, value: "15" }
  - { name: "LFO", type: switch, value: "value", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Value LFO speed", type: knob, value: "3 clicks right" }
  - { name: "Value LFO amount", type: knob, value: "5" }
  - { name: "Value LFO destination", type: switch, value: "green/delay knob" }
  - { name: "Slot/Bank", type: knob, value: "save into a pad patch's FX slot (e.g. windswept)" }
---

# CWO chorus (lush stereo, free the reverb slot)

## Concept

A lush stereo chorus for high-sustain digital patches that don't have a dedicated chorus slot — CWO is stereo per-instrument on the Field. Concrete, community-verified values (freq 0 / delay 28 / feedback 15) with a value LFO modulating the green/delay knob for movement. Shoegaze-washed pads.

## How to play it

1. Set the instrument's FX to **CWO**: freq **0**, delay **28**, feedback **15**.
2. Set the **value LFO**: speed 3 clicks right, amount 5, destination = green/delay knob.
3. Apply on any high-sustain digital patch for width.

## Notes

- CONCRETE community-verified values on disk; CWO is stereo per-instrument on the Field.
- Save into a pad patch's FX slot (e.g. windswept already ships with CWO loaded).

## Sources

- Gear/TE OP-1 Field/research/links/github-ratbag98-op1tips-distilled.md (op-forums t/1241) + UsageGuide §2
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
