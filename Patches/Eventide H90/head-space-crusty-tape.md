---
type: patch
title: Head Space Crusty Tape (Boil/Break on footswitch)
device: Eventide H90
date: 2026-06-14
description: Degraded lo-fi multi-head tape repeats with tape-runaway pitch dives — 4 virtual heads, Boil and Break mapped to a footswitch. Leon Todd's "crusty tape" build.
tags: [delay, head-space, tape, lo-fi, degraded, recorded-wrong, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "32" }
  - { name: "Preset A Algorithm", type: switch, value: "Head Space (4 virtual playback heads)" }
  - { name: "Delay Time", type: knob, value: "tape length x Playback Speed (core time)" }
  - { name: "Per-head Level (x4)", type: knob, value: "set distinct per-head" }
  - { name: "Per-head Subdivision (x4)", type: knob, value: "distinct rhythmic positions vs core time" }
  - { name: "Per-head Pan (x4)", type: knob, value: "spread pans for a stereo smear" }
  - { name: "Boil (HotSwitch / Perform)", type: button, value: "tape speed-up runaway" }
  - { name: "Break (HotSwitch / Perform)", type: button, value: "power-down dive (Todd used it to end phrases)" }
---

# Head Space Crusty Tape (Boil/Break on footswitch)

## Concept
Degraded lo-fi multi-head tape repeats with tape-runaway pitch dives, sitting **before** the downstream PORTA424 / JHS 424 tape stage. Head Space drives 4 virtual playback heads; distinct per-head subdivisions and spread pans make a stereo smear. Boil (tape speed-up runaway) and Break (power-down dive) ride a footswitch.

## How to play it
1. Engage Head Space on Preset A; set Delay Time (tape length x Playback Speed) as the core time.
2. For each of the 4 heads, set distinct Level, Subdivision (rhythmic position vs core time), and spread Pan for a stereo smear.
3. Map Boil and Break to a HotSwitch / Perform footswitch.
4. Use Break (the power-down dive) to end phrases, as Todd did.

## Notes
- Leon Todd deep-dive (JZcYl40Leg0), his own "crusty tape" build. Squarely on-aesthetic (degraded/"recorded-wrong").
- No numeric per-head values transcribed — verbal description only.

## Sources
- research/transcripts/leon-todd-h90-headspace-deep-dive.md
- Transformed from Pedalxly H90-Patches.md (community)
