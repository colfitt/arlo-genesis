---
type: patch
title: Drone-Bed Feeder
device: Longsword
date: 2026-06-14
description: A dense, stable, sustained drone source to feed the Microcosm / Dark Star / Generation Loss / Blooper / H90 so granular/tape/reverb processing reads as intentional, not choppy.
tags: [drone, bed, sustain, texture-feed, designed, signature]
controls:
  - { name: "Level", type: knob, value: "~1:00" }
  - { name: "Drive", type: knob, value: "~10:00 (backed off)" }
  - { name: "Low", type: knob, value: "~11:00 (slightly cut)" }
  - { name: "High", type: knob, value: "~11:00 (softened)" }
  - { name: "Mid", type: knob, value: "~1:00 (body)" }
  - { name: "Boost", type: knob, value: "set (footswitch OFF)" }
  - { name: "DIODE", type: switch, value: "center (no diodes)", options: ["up (MOSFET)", "center (no diodes)", "down (silicon)"] }
  - { name: "SHIFT", type: switch, value: "down (300 Hz)", options: ["up (1 kHz)", "down (300 Hz)"] }
  - { name: "Boost (footswitch)", type: button, value: "OFF (keep it a steady bed)" }
---

# Drone-Bed Feeder

## Concept
Swans/post-punk sustained crescendo + the rig's "dense source makes processing sound intentional" principle. DIODE center for max sustain/dynamics, Drive backed off to ~10:00 so the upstream fuzz and this combine into a smooth bloom rather than a fizz, Low/High slightly cut to keep the wall defined and the texture boards from getting harsh, Mid SHIFT-down (300 Hz) for body. Built for sustain and stability, not aggression.

## How to play it
1. DIODE center (no diodes, max sustain/dynamics), Drive ~10:00 (backed off).
2. Level ~1:00, Low ~11:00 (cut), High ~11:00 (softened), Mid SHIFT-down (300 Hz) ~1:00.
3. Boost footswitch OFF — keep it a steady bed.
4. Place after the Hizumitas + Brothers AM; into the Oxford only as a final shove.

## Notes
- A steady drone bed, not a riff voice.
- Softened highs keep the downstream reverbs/granular from getting brittle.
- Designed patch — knob positions are starting points, dial by ear.

## Sources
- designed from `Longsword-UsageGuide.md` §1 (Center = stacking mode) + the dossier's "stable hot wall is the ideal feed for the texture/time boards" + the taste-profile post-punk drone-wall cluster
- Transformed from Pedalxly Longsword-Patches.md (designed)
