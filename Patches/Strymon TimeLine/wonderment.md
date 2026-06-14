---
type: patch
title: Wonderment — backwards-reverb tape wall
device: Strymon TimeLine
date: 2026-06-14
description: dTape + an external reverse-reverb in the rear feedback-loop insert + infinite-hold (Daniel Kastner) — a backwards-reverb tape wall; the named-artist instance of the feedback-loop-insert trick.
tags: [degraded, tape, reverse-reverb, feedback-loop, drone, wall, infinite-hold, artist, signature]
hidden:
  Rear switch: FEEDBACK LOOP (RIGHT IN/OUT become a send/return inside the feedback path)
controls:
  - { name: "TYPE", type: switch, value: "dTape", options: ["dTape","dBucket","Digital","Dual","Pattern","Reverse","Ice","Lo-Fi","Swell","Trem","Filter","Duck"] }
  - { name: "Rear routing switch", type: switch, value: "FEEDBACK LOOP", options: ["STEREO","FEEDBACK LOOP"] }
  - { name: "Footswitch HOLD", type: button, value: "HOLD the active footswitch to freeze the wall" }
  - { name: "dTape knob values", type: knob, value: "image/.syx-only (not captured)" }
  - { name: "Slot/Bank", type: knob, value: "user slot + routing" }
---

# Wonderment — backwards-reverb tape wall

## Concept
The named-artist instance of the rig's feedback-loop-insert trick. dTape, with the rear switch set to FEEDBACK LOOP so RIGHT IN/OUT become a send/return inside the feedback path; patch a reverse reverb into that loop (Kastner used an Alesis MIDIVERB II set to reverse reverb) so every repeat re-reverbs and grows backwards, then HOLD the active footswitch to freeze the wall.

## How to play it
1. Set dTape, then flip the rear routing switch to FEEDBACK LOOP.
2. Patch a reverse reverb into RIGHT IN/OUT (the feedback-path send/return).
3. Play sustained chords so each repeat re-reverbs and grows backwards.
4. HOLD the active footswitch to freeze the backwards-reverb wall.

## Notes
- Swap the MIDIVERB II for any rig reverb / Valhalla / a fuzz or filter into RIGHT IN/OUT.
- Costs stereo — the right channel becomes the send/return. Highest rig relevance of the feedback-loop finds.
- dTape knob numbers are image/.syx-only and not captured.

## Sources
- Strymon "This Week's Preset: Daniel Kastner's Wonderment"
- research/links/strymon-twp-kastner-wonderment-feedback-loop-reverb.md
- Transformed from Pedalxly TimeLine-Patches.md (factory)
