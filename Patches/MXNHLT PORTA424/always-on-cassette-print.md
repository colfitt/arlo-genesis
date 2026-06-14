---
type: patch
title: Always-On Cassette Print
device: MXNHLT PORTA424
date: 2026-06-14
description: End-of-chain bus print that stamps subtle cassette warmth and light compression over the whole mono-summed H90 bus with no obvious grit — the rig's effectively-always-on default glue.
tags: [console-warmth, glue, always-on, clean, factory, signature]
controls:
  - { name: "Input Trim", type: knob, value: "9 o'clock" }
  - { name: "Treble", type: knob, value: "12 o'clock" }
  - { name: "Bass", type: knob, value: "12–1 o'clock" }
  - { name: "Channel Fader", type: knob, value: "~70% of travel (upper third)" }
  - { name: "Master Volume", type: knob, value: "to unity (into JHS 424)" }
  - { name: "Voltage", type: switch, value: "18V", options: ["9V", "18V"] }
  - { name: "Placement", type: switch, value: "end of chain (after H90, before JHS 424)", options: ["front of chain", "end of chain"] }
  - { name: "Footswitch", type: button, value: "engaged (always-on, true-bypass latching)" }
---

# Always-On Cassette Print

## Concept
End-of-chain bus print that stamps subtle cassette warmth plus light compression over the whole mono-summed H90 bus, with no obvious grit. This is the rig's effectively-always-on default glue — coloration not destruction. Low Trim at the end of the chain gives the clean DI / console-warmth voicing.

## How to play it
1. Mono-sum the H90 stereo bus to mono into the PORTA424 input (the load-bearing setup decision).
2. Set Input Trim to 9 o'clock — the clean DI zone, below the breakup gate.
3. Treble at noon, Bass at 12–1 o'clock for a flat-to-slightly-warm tilt.
4. Run the Channel Fader up into its upper third (~70%) and bring Master Volume to unity into the JHS 424.
5. Leave the footswitch engaged — this is the always-on print.

## Notes
- MONO-SUM the H90 stereo to mono into the input — the load-bearing setup decision for this rig.
- 18V keeps the low end firm under reverb-heavy H90 tails.
- Fader sits upper-third per the builder's B10k-taper "finer control at the top" note.
- All clock/fader/voltage values are designed-to-spec — no factory numbers exist for this box.

## Sources
- Builder directional voicing — low Trim at END of chain = clean DI / console-warmth print (`research/links/mxnhlt-product-page.md`, `research/links/staging-mono-print-tips.md`); numeric clock/fader/voltage values are designed-to-spec (no factory numbers exist). Mirrors DeepResearch §13(a).
- Transformed from Pedalxly PORTA424-Patches.md (factory/artist directional voicing; numeric fill designed)
