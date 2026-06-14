---
type: patch
title: Beat-Repeat / Stutter Freeze (master Delay + DELAY CTRL)
device: Elektron Octatrack MkII
date: 2026-06-14
description: Glitch-collapse stutter over the fuzz wall or banjo loop, played live from the trig row with explicit master-delay values and the DELAY CTRL button-fu (Konstruct Noise).
tags: [stutter, beat-repeat, freeze, delay, performance, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank B / Part 2 · FX2 = Delay on Thru track (1) or master track 8" }
  - { name: "Delay SETUP SYNC", type: knob, value: "1" }
  - { name: "Delay SETUP LOCK", type: switch, value: "1", options: ["0", "1"] }
  - { name: "Delay SETUP PASS", type: switch, value: "0" }
  - { name: "Delay SETUP TAPE", type: switch, value: "1 (optional)", options: ["0", "1"] }
  - { name: "Delay MAIN TIME", type: knob, value: "32" }
  - { name: "Delay MAIN FB", type: knob, value: "127" }
  - { name: "Delay MAIN VOL", type: knob, value: "127" }
  - { name: "Delay MAIN BASE", type: knob, value: "0" }
  - { name: "Delay MAIN WDTH", type: knob, value: "127" }
  - { name: "Delay MAIN SEND", type: knob, value: "2" }
  - { name: "Play", type: button, value: "[FUNCTION]+[DOWN ARROW] until DELAY CTRL shows; hold [P/T8] to stutter; tap yellow trigs (leftward = faster); [P/T8]+left trig = freeze + set time" }
---

# Beat-Repeat / Stutter Freeze (master Delay + DELAY CTRL)

## Concept
Glitch-collapse stutter over the fuzz wall or banjo loop, played live from the trig row. The most "performable" of the freeze recipes — explicit numeric delay values plus live DELAY CTRL button-fu. LOCK = 1 + FB = 127 = a true frozen repeat, sustained-wall friendly. Sits over the Live-Mangle or Resample-the-Banjo patches.

## How to play it
1. **Delay SETUP:** SYNC = 1, **LOCK = 1**, PASS = 0 (optional **TAPE = 1**).
2. **Delay MAIN:** TIME = 32, **FB = 127**, VOL = 127, BASE = 0, WDTH = 127, SEND = 2.
3. **Play:** [FUNCTION]+[DOWN ARROW] until "DELAY CTRL" shows; hold rightmost trig **[P/T8] to stutter**; tap yellow trigs (leftward = shorter time = faster stutter); **[P/T8]+left trig = freeze + set time.**
4. LOCK = 1 + FB = 127 = true frozen repeat (sustained-wall friendly).

## Notes
- The most "performable" of the freeze recipes — explicit numeric delay values + the live DELAY CTRL button-fu.
- Sits over the Live-Mangle-the-Pedalboard or Resample-the-Banjo-Loop patches.

## Sources
- Ref: Konstruct Noise — "Octatrack Button-fu: Beat Repeat" (Aug 2015)
- research/links/beat-repeat-delay-control-konstructnoise.md
- Transformed from Pedalxly Octatrack-MkII-Patches.md (community)
