---
type: patch
title: Live Setup Config
device: Hologram Chroma Console
date: 2026-06-14
description: Make the pedal gig-ready given clunky preset switching and the mono→stereo dependency (community) — buffered bypass, audition off, MIDI Program Change for scene recall, calibrate per instrument.
tags: [live, setup, utility, midi, community]
hidden:
  Bypass mode (Global Settings): BUFFERED or BUFFERED + TRAILS (TRUE BYPASS defeats the mono→stereo re-expansion)
  Preset Browser Audition: OFF (current preset persists while scrolling)
  Dual Bypass: for in-song "adds"
  Scene recall: MIDI Program Change (no preset footswitches; preset switching has a load gap)
  Calibration: hold both footswitches → purple → play a note (re-calibrate when swapping banjo/baritone/VG-800)
  Power: ≥500 mA isolated (daisy-chaining caused a high-pitched whine)
controls:
  - { name: "Bypass mode", type: switch, value: "BUFFERED or BUFFERED + TRAILS", options: ["TRUE BYPASS", "BUFFERED", "BUFFERED + TRAILS"] }
  - { name: "Preset Audition", type: switch, value: "OFF", options: ["ON", "OFF"] }
---

# Live Setup Config

## Concept
A utility config to make the pedal gig-ready, given its clunky preset switching and the mono→stereo dependency. Buffered bypass keeps the re-expansion intact, audition-off keeps the current preset while scrolling, and MIDI Program Change handles scene recall since there are no preset footswitches.

## How to play it
1. **Global Settings:** Bypass = **BUFFERED** or **BUFFERED + TRAILS** (TRUE BYPASS defeats the mono→stereo re-expansion).
2. **Preset Browser Audition = OFF** (current preset persists while scrolling).
3. Use **Dual Bypass** for in-song "adds" + **MIDI Program Change** for scene recall (no preset footswitches; preset switching has a load gap).
4. **Calibrate per instrument:** hold both footswitches → purple → play a note (re-calibrate when swapping banjo/baritone/VG-800; SWELL/SWEETEN/SQUASH are level-triggered).
5. **Power:** ≥500 mA isolated (daisy-chaining caused a high-pitched whine).

## Notes
- Untagged on purpose (utility/live config, not on-aesthetic-tagged).

## Sources
- research/Chroma-Console-UsageGuide.md §5/§7; research/links/chroma-presets-how-banks-and-saving-work.md; research/links/wolfewithane-blog-chroma-console-usage-tips.md; research/transcripts/molten-modular-chroma-console-review.md; nervouscooks-deep-dive-tutorials-part2.md
- Transformed from Pedalxly Chroma-Console-Patches.md (community)
