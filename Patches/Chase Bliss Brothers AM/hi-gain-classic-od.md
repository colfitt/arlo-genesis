---
type: patch
title: "Hi-Gain Classic OD — +25% on the KOT voice"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: "AndyDemos' way to get more out of the classic overdrive: run OVERDRIVE on both sides with identical settings and flip the HI GAIN dip to add ~25% gain to all modes on that channel (the bypass LED turns red). \"A cool way of getting a little bit more out of a pretty classic-sounding overdrive pedal.\" A hotter take on the standard King of Tone voice without changing the knobs. Dialable recipe — the ~25% figure and the red-LED behavior are quoted, but no exact clock values are published."
tags: [overdrive, hi-gain, king-of-tone, factory, always-on]
dips:
  HI GAIN 1: "on (the channel you want hotter)"
  HI GAIN 2: "on (optional — flip both for both sides hotter)"
  MASTER: "on (optional)"
controls:
  - { name: "CHANNEL 1 MODE", type: switch, value: "OVERDRIVE (the classic KOT voice)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "dial from recipe — your normal OD setting (no published clock)" }
  - { name: "VOL 1", type: knob, value: "dial from recipe — rebalance after HI GAIN adds level" }
  - { name: "TONE 1", type: knob, value: "dial from recipe to taste" }
  - { name: "CHANNEL 2 MODE", type: switch, value: "OVERDRIVE (identical to Channel 1)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 2", type: knob, value: "dial from recipe — match Channel 1" }
  - { name: "VOL 2", type: knob, value: "dial from recipe — match Channel 1 / rebalance" }
  - { name: "TONE 2", type: knob, value: "dial from recipe — match Channel 1" }
  - { name: "PRESENCE", type: knob, value: "DOWN to start" }
  - { name: "TREBLE BOOSTER", type: switch, value: "MIDDLE (off)", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
---

# Hi-Gain Classic OD — +25% on the KOT voice

## Concept
AndyDemos' way to get more out of the classic overdrive: run OVERDRIVE on both sides with identical settings, then flip the HI GAIN dip to add roughly 25% gain to all modes on that channel — the bypass LED turns from green to red to confirm it's active. As Andy puts it, it's "a cool way of getting a little bit more out of a pretty classic-sounding overdrive pedal." It's a hotter take on the standard King of Tone voice without touching the knobs — the same OD character, just pushed harder. HI GAIN here is the documented King of Tone internal-mod option, brought out to a dip switch.

## How to play it
1. Set your channel(s) to OVERDRIVE with your normal settings (run both sides identical to A/B them cleanly).
2. Flip the HI GAIN dip ON for the channel you want hotter — it adds ~25% gain to all modes; the bypass LED turns from green to red.
3. Compare with HI GAIN off to hear the extra gain on the classic OD voice.
4. Rebalance VOL if the extra gain bumps the level.

## Notes
- AndyDemos + Doug Hanson + CB-quoted: the ~25% gain figure and the LED-turns-red behavior are quoted; no exact knob numbers — dial GAIN/VOL/TONE from recipe to taste.
- HI GAIN is per channel and saves with presets; it's documented as a King of Tone internal-mod option brought to the dip switch.
- Distinct from the BAD BROS preset (both HI GAIN dips cranked into a wall) and from the DISTORTION + HI GAIN metal use — this is HI GAIN on the clean classic OD voice.
- No published knob values — phrased as a dialable recipe by design.

## Sources
- research/transcripts/andy-brothers-am-demo.md ("OVERDRIVE on both sides… you'll hear what the HI GAIN dip switch adds… a little bit more out of a pretty classic-sounding overdrive")
- research/links/andy-demo-settings.md (HI GAIN dip)
- research/transcripts/doug-hanson-demo.md (HI GAIN adds ~25%, LED red)
- https://guitar.com/reviews/effects-pedal/the-big-review-chase-bliss-brothers-am/ (Hi-gain DIP adds ~25% gain to either channel)
- Ref: Brothers AM manual, "Customize" (HI GAIN)
