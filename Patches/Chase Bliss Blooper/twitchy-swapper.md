---
type: patch
title: Twitchy Swapper — envelope-triggered interruptions
device: Chase Bliss Blooper
date: 2026-06-15
description: Push Swapper to max sensitivity so even light string touches trigger it, then record in Additive — dynamics-driven swaps interrupt and replace parts of the loop as you play; factory cheat-sheet recipe (Swapper card tip).
tags: [swapper, envelope, glitch, dynamics, factory]
dips:
  BANK B: "ON = engages the alt-bank Swapper in the MOD B slot (alternatively load Swapper via BLIP)"
controls:
  - { name: "Mode", type: switch, value: "ADD", options: ["NORM", "ADD", "SAMP"] }
  - { name: "MOD B", type: knob, value: "MAX (most sensitive — SENS; documented tip)" }
  - { name: "MOD B slot", type: switch, value: "B6 Swapper (ALT bank)", options: ["B4", "B5", "B6"] }
  - { name: "MOD B engage", type: button, value: "engaged (arcade button)" }
  - { name: "Slot/Bank", type: knob, value: "MOD B6 Swapper · requires BANK B dip (or BLIP load) — physical-only setup; surrounding knobs dial from recipe (no published values)" }
---

# Twitchy Swapper — envelope-triggered interruptions

## Concept

Swapper is very sensitive at maximum — just touching the guitar strings triggers it. Take advantage of that to create twitchy, dynamics-triggered interruptions that replace parts of the loop based on how hard you play. Recording in ADD bakes the envelope-driven swaps right into the loop.

## How to play it

1. Engage BANK B and set MOD B to Swapper (or load Swapper via BLIP).
2. Turn the Swapper knob (MOD B) to max — the highest sensitivity (SENS).
3. Play — even light string touches trigger the swap, interrupting and replacing parts of the loop.
4. Record in ADD to bake the twitchy, dynamics-driven interruptions into the loop.

## Notes

- Envelope-controlled: the swaps respond to your picking dynamics — great for replacing parts of a loop interactively in ADD.
- Requires the BANK B dip (or a BLIP load) to reach the alt-bank Swapper — physical-only setup, no MIDI PC for the alt slot here.
- The "max sensitivity" position is the documented tip; the surrounding knob values dial from recipe — no published values.

## Sources

- `research/links/chasebliss-blooper-modifier-cheat-sheet.md` (SWAPPER · TIP: sensitive at max, twitchy interruptions, verbatim)
- `research/Blooper-DeepResearch.md` §3 (B6 Swapper, envelope-controlled swaps)
- Transformed from Pedalxly Blooper-Patches.md (factory)
