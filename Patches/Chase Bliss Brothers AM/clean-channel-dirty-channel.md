---
type: patch
title: "Clean Channel, Dirty Channel — two-amp-channel switcher"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: 'Manual "Finding Your Sound" recipe — a two-channel-amp template with a low-gain OVERDRIVE on Channel 1 and a mid-gain DISTORTION on Channel 2 sharing a common KOT character; tap both footswitches to SWAP, giving a rhythm-clean and a lead-dirty channel underfoot without stacking.'
tags: [overdrive, distortion, two-channel, rhythm-lead, factory, footswitch-push]
dips:
  MASTER: off
controls:
  - { name: "TREBLE BOOSTER", type: switch, value: "MIDDLE (off) to start", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
  - { name: "CHANNEL 1 MODE", type: switch, value: "OVERDRIVE — rhythm/clean channel (low gain)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "low — dial from recipe, no published clock" }
  - { name: "VOL 1", type: knob, value: "set so rhythm level matches the lead channel" }
  - { name: "PRESENCE 1", type: knob, value: "DOWN (default)" }
  - { name: "CHANNEL 2 MODE", type: switch, value: "DISTORTION — lead/dirty channel (mid gain)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 2", type: knob, value: "medium — dial from recipe, no published clock" }
  - { name: "VOL 2", type: knob, value: "set so lead level matches the rhythm channel" }
  - { name: "PRESENCE 2", type: knob, value: "DOWN (default)" }
  - { name: "Swap channels", type: button, value: "tap BOTH footswitches at once" }
---

# Clean Channel, Dirty Channel — two-amp-channel switcher

## Concept
The manual's two-channel template that mimics a classic two-channel amp: a low-gain OVERDRIVE on Channel 1 and a mid-gain DISTORTION on Channel 2 — two distinct stages sharing a common KOT character. Tap both footswitches at once to SWAP between them, so you have a rhythm-clean and a lead-dirty channel under your feet without stacking. This is the SWAP workflow (one channel at a time), not the series stack — distinct from the always-on + push "2-IN-1" factory preset.

## How to play it
1. Set Channel 1 to OVERDRIVE at low gain (rhythm channel) and Channel 2 to DISTORTION at mid gain (lead/dirty channel).
2. Use one channel at a time — tap BOTH footswitches at once to swap between them.
3. Because the two modes clip differently, set each channel's VOL so the rhythm and lead levels are balanced.
4. Leave the treble booster MIDDLE (off) unless the lead needs more cut, then flip it DOWN (Rangemaster).

## Notes
- Manual-named recipe ("Finding Your Sound"): modes are quoted; no exact knob numbers exist in any primary source — dial GAIN/VOL from the recipe.
- SWAP workflow (one channel at a time), NOT the series stack — distinct from the 2-IN-1 always-on + push factory preset.
- Watch the mode-to-mode level jump: distortion is more compressed than overdrive; balance with VOL.
- MASTER dip off — each channel's own VOL sets its level when used solo, since you're swapping rather than stacking.

## Sources
- research/links/factory-preset-settings.md (manual "Finding Your Sound" → Two-channel ideas: "CLEAN CHANNEL, DIRTY CHANNEL")
- research/transcripts/cb-technical-demo.md (tap both footswitches to swap; mode clipping/level differences)
- Ref: Brothers AM manual, "Finding Your Sound"
