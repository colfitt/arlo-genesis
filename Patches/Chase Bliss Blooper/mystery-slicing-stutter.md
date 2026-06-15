---
type: patch
title: "Mystery Slicing — ramped Stutter, new slice each time"
device: Chase Bliss Blooper
date: 2026-06-15
description: "Factory cheat-sheet recipe (Stutter card · 'Mystery Slicing') — pair Stutter with ramping so each time you turn it on the slices are a different size: a generative, ever-changing stutter that never repeats the same way twice."
tags: [stutter, ramp, glitch, beat-repeat, factory]
dips:
  BANK A: "ON — puts Stutter (A3, ALT bank) on the MOD A slot; alternatively load Stutter via BLIP"
  RAMP MOD A: "put the MOD A (Stutter) knob into ramping"
  RAMP BOUNCE: "continuous back-and-forth so the slice size keeps shifting"
  RAMP RANDOM: "alternative — varied, unpredictable slice sizes"
controls:
  - { name: "MOD A slot", type: switch, value: "A3 Stutter (ALT bank — requires BANK A dip, or load via BLIP)", options: ["A1", "A2", "A3"] }
  - { name: "MOD A engage", type: button, value: "re-engage to grab a fresh slice size (the ramp re-rolls per toggle)" }
  - { name: "RAMP knob (= VOLUME knob while ramping)", type: knob, value: "ramp speed — set to taste (no published value)" }
  - { name: "Mode", type: switch, value: "NORM or ADD", options: ["NORM", "ADD", "SAMP"] }
  - { name: "Slot/Bank", type: knob, value: "MOD A3 ALT bank (requires BANK A dip) + physical ramping dips (Bounce or Random)" }
---

# Mystery Slicing — ramped Stutter, new slice each time

## Concept

Stutter pairs nicely with ramping so that each time you turn it on the slices are a different size — a generative, ever-changing stutter that never repeats the same way twice. Because the ramp is moving the Stutter knob for you, the slice size lands somewhere new every time you re-engage, giving you an always-fresh beat-repeat / DJ-scratch rhythm.

## How to play it

1. Engage BANK A so Stutter sits on MOD A (A3), or load Stutter onto the slot via BLIP.
2. Set the ramping dips to automate MOD A — use BOUNCE for continuous back-and-forth, or RANDOM for the most varied slice sizes.
3. Set the RAMP knob (the VOLUME knob while ramping) for the ramp speed.
4. Each time you toggle Stutter on, the ramp lands the slice at a different size.
5. Toggle on/off through a passage for an always-changing stutter rhythm or a DJ/beat-repeat scratch effect.

## Notes

- Generative by design — the slice size re-rolls per engage thanks to the ramp position.
- Requires the BANK A dip and the ramp dips — both physical-only setups (the ramping dips are not MIDI-addressable; this is a fixed-setup decision, not a per-song recall).
- Combine with manic on/off toggling for a fake time-stretch (see Pseudo-Stretching).
- Random gives the widest spread of slice sizes; Bounce keeps the motion sweeping continuously.
- Honesty flag: ramp speed/flavor and the other knobs dial from this recipe — no published values.

## Sources

- `research/links/chasebliss-blooper-modifier-cheat-sheet.md` (STUTTER · MYSTERY SLICING, verbatim)
- Official CB modifier cheat-sheet PDF + Blooper manual (Ramping dips)
