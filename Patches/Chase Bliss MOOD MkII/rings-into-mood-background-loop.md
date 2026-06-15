---
type: patch
title: Rings into MOOD — background loop under reverb
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: "The Unperson's Mutable Rings → MOOD move — capture a loop, then use the hidden LEVEL BALANCE to drop the loop into the background while the live Rings runs through the Reverb for subtle ambience. Loop as quiet bed, live source up front. (The Unperson / Ali)"
tags: [artist, synth, looper, reverb, ambient, background-loop, technique]
hidden:
  LEVEL BALANCE (CLOCK): turn toward the wet/reverb side to drop the captured loop into the background — exact position by ear, no published value
controls:
  - { name: "Looper MODE", type: switch, value: "Tape or Stretch (capture a Rings phrase)", options: ["Env", "Tape", "Stretch"] }
  - { name: "Wet MODE", type: switch, value: "Reverb (on the live Rings input)", options: ["Reverb", "Delay", "Slip"] }
  - { name: "ROUTING", type: switch, value: "to taste (live input + loop)", options: ["IN", "IN+micro-loop", "micro-loop only"] }
  - { name: "CLOCK", type: knob, value: "hidden LEVEL BALANCE — drop the loop's volume (by ear)" }
---

# Rings into MOOD — background loop under reverb

## Concept
The Unperson's Mutable Rings → MOOD setup: run a loop on MOOD and use the **hidden LEVEL BALANCE** (hold both footswitches, turn **CLOCK**) to drop the captured loop's volume so it sits quietly in the background, while the live Rings runs through the **Reverb** for subtle, evolving ambience. A "loop as quiet bed, live source up front" synth-into-MOOD move. Works with any basic-waveform synth — bare sources show MOOD off best.

## How to play it
1. Patch Mutable Rings (or any synth) into MOOD.
2. Capture a Rings phrase into the Micro-Looper with Looper MODE = **Tape** or **Stretch**.
3. Use the **hidden LEVEL BALANCE** (hold both footswitches until LEDs go green, then turn **CLOCK** toward the wet side) to drop the captured loop down so it sits quietly in the background.
4. Set Wet MODE = **Reverb** and run the live Rings through it on top for subtle, evolving ambience over the quiet loop bed.

## Notes
- ⚠️ No published knob values — dial from this recipe. The Unperson describes using "a hidden function to decrease the loop's volume"; that's **LEVEL BALANCE (CLOCK in the hidden menu)**, and the exact position is set by ear.
- Works with any basic-waveform synth (Vong Replay, OP-1 clarinet preset) — bare sources show off MOOD best.
- Distinct from the dry-over-soaked-loop patch (the-unperson-dry-over-soaked-loop): here the **loop** is the quiet bed and the **live synth** is up front.

## Sources
- unperson-mood-mkii-reverb-delay-looper.md ("Mutable Rings → MOOD… runs a loop on MOOD; uses a hidden function to decrease the loop's volume so it sits in the background, with Rings running through the reverb for a subtle, beautiful ambience")
- MOOD-MkII-UsageGuide.md §6 (The Unperson — synth/Rings-into-MOOD routing)
- Ref: The Unperson (Ali) — yt RQcTZRnyauo — technique described, no published knob values
