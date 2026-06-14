---
type: patch
title: Banjo layer-builder
device: Chase Bliss Blooper
date: 2026-06-14
description: Turn one banjo phrase into a self-generating doom bed, then play fresh banjo lead live over it; designed for this rig.
tags: [drone, doom, layer-builder, octave-down, designed, signature]
controls:
  - { name: "Mode", type: switch, value: "NORM → ADD", options: ["NORM", "ADD", "SAMP"] }
  - { name: "VOLUME", type: knob, value: "12 o'clock" }
  - { name: "REPEATS", type: knob, value: "max" }
  - { name: "STABILITY", type: knob, value: "~10 o'clock" }
  - { name: "MOD B", type: knob, value: "octave-down / a fifth (sub-drone under the banjo)" }
  - { name: "MOD B slot", type: switch, value: "B4 Stepped Speed", options: ["B4", "B5", "B6"] }
  - { name: "MOD A", type: knob, value: "optional ALT-bank A3 Stutter for rhythmic chop" }
  - { name: "Slot/Bank", type: knob, value: "MOD B4 default + ALT A3 Stutter (BANK A dip) · MIDI PC 4" }
---

# Banjo layer-builder

## Concept

Turn one banjo phrase into a self-generating doom bed, then solo fresh banjo lead live over it. A Stepped-Speed octave-down layer adds sub-drone thickness beneath a captured banjo lead; optionally an ALT-bank Stutter brings rhythmic chop.

## How to play it

1. In NORM → ADD, capture a banjo lead phrase.
2. Set STABILITY ~10 o'clock, REPEATS max, VOLUME 12.
3. Overdub a Stepped-Speed (B4) layer set octave-down or a fifth for thickness.
4. Optionally bring in ALT-bank A3 Stutter (requires BANK A dip) for rhythmic chop.
5. Solo fresh banjo over the self-running bed.

## Notes

- Carry the finished wall over into SAMP (see Carryover) to trigger it alongside the Octatrack/OP-1.
- ALT bank requires the BANK dip (physical-only).

## Sources

- designed from `research/Blooper-DeepResearch.md` §13(d)
- Transformed from Pedalxly Blooper-Patches.md (designed)
