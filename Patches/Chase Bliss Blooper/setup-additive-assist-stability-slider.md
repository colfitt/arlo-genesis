---
type: patch
title: Setup — Additive Assist + Stability slider (BLIP)
device: Chase Bliss Blooper
date: 2026-06-14
description: Choosing predictable prints vs happy-accident walls, and keeping walls aged-not-hissy — global BLIP firmware settings for Additive Assist and the Stability slider.
tags: [setup, firmware, blip, stability, factory, signature]
hidden:
  Additive Assist (BLIP): "OFF (Free Recording, default) = play/record heads drift for accident walls; ON = resets play head each loop to preview exactly what a one-shot commits"
  Stability slider (BLIP): "bias toward pure wow/flutter, dialing out white noise as the Stability knob sweeps CW"
controls:
  - { name: "Slot/Bank", type: knob, value: "firmware settings (BLIP) · global, applies to every loop slot" }
---

# Setup — Additive Assist + Stability slider (BLIP)

## Concept

Two global BLIP firmware settings that decide the character of every loop: Additive Assist chooses between predictable prints and happy-accident walls, and the Stability slider keeps walls aged-not-hissy.

## How to play it

1. In the BLIP USB interface, set Additive Assist:
   - OFF (Free Recording, default) = play/record heads drift for accident walls.
   - ON = resets the play head each loop so the loop previews exactly what a one-shot commits.
2. Set the Stability slider to dial out white noise as the Stability knob sweeps CW — bias toward pure wow/flutter (Andy's gripe: he wants warble, not hiss).

## Notes

- For this rig: leave Additive Assist OFF for accident walls, flip ON to dial in a specific result before printing; bias the Stability slider to flutter-not-noise.
- Global — applies to every loop slot.

## Sources

- `research/links/chasebliss-blooper-recording-with-modifiers-guide.md`
- `research/transcripts/chase-bliss-blooper-firmware-3-tutorial.md`
- `research/transcripts/andy-othling-office-hours-blooper.md` (Andy community note)
- Transformed from Pedalxly Blooper-Patches.md (factory/artist)
