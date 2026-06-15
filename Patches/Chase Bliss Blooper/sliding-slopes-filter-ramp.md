---
type: patch
title: "Sliding Slopes — ramped Filter movement"
device: Chase Bliss Blooper
date: 2026-06-15
description: "Factory cheat-sheet recipe (Filter card · 'Sliding Slopes') — add movement to a static loop by ramping the Filter: Wiggle for subtle filter shifts or Random for glitchy 'computer thinking' sounds, automated motion that brings a loop to life without touching the knob."
tags: [filter, ramp, modulation, movement, factory]
dips:
  RAMP MOD B: "Filter (B6) — put the Filter knob into ramping"
  RAMP WIGGLE: "subtle filter shifts"
  RAMP RANDOM: "alternative — glitchy 'computer thinking' motion"
  RAMP SWEEP/POLARITY: "set the filter's travel range and direction"
  RAMP BOUNCE: "continuous back-and-forth (omit for ramp-and-hold)"
  RAMP SYNC: "optional"
controls:
  - { name: "MOD B slot", type: switch, value: "B6 Filter (default bank)", options: ["B4", "B5", "B6"] }
  - { name: "MOD B engage", type: button, value: "engaged" }
  - { name: "RAMP knob (= VOLUME knob while ramping)", type: knob, value: "movement speed — set to taste (no published value)" }
  - { name: "Mode", type: switch, value: "NORM or ADD", options: ["NORM", "ADD", "SAMP"] }
  - { name: "Slot/Bank", type: knob, value: "MOD B6 default bank + physical ramping dips (Wiggle or Random) · MIDI PC 10 (shares Filter family)" }
---

# Sliding Slopes — ramped Filter movement

## Concept

Add movement to a loop by ramping the Filter. Instead of a static filter setting, put the Filter knob into ramping so the pedal sweeps it for you: Wiggle gives subtle filter shifts, while Random gives glitchy "computer thinking" sounds. Automated filter motion that brings a static loop to life without ever touching the knob.

## How to play it

1. Set MOD B to Filter (B6) and engage it.
2. In the ramping dips, put the Filter knob into ramping with WIGGLE for subtle shifts (or RANDOM for glitchy computer-thinking motion).
3. Set the RAMP knob (the VOLUME knob while ramping) for the movement speed.
4. Use SWEEP/POLARITY to constrain the filter's travel range and direction; use BOUNCE for continuous back-and-forth; let the loop breathe under live playing.

## Notes

- Ramping dips are physical-only and NOT MIDI-addressable — a fixed-setup decision, not a per-song recall.
- Wiggle keeps the motion tight/subtle; Random gives wild, stepped, unpredictable sweeps; ramp-and-hold transitions to a point and stays, while Bounce moves continuously.
- Pair Filter with Stability to intensify the vintage character.
- Exact ramp speed/sweep values are not published — this is a dialable recipe, set by ear.

## Sources

- `research/links/chasebliss-blooper-modifier-cheat-sheet.md` (FILTER · SLIDING SLOPES, verbatim)
- `research/links/blooper-manual-named-patches-dip-recipes.md` (ramping dip reference)
- Official CB modifier cheat-sheet PDF + Blooper manual (Ramping / Wiggle / Random / Bounce / Sync dips)
- Transformed from Pedalxly Blooper-Patches.md (factory)
