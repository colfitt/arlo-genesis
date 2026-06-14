---
type: patch
title: Tape Hopper (auto model-jumping)
device: Chase Bliss Generation Loss
date: 2026-06-14
description: The pedal autonomously jumping between tape machines — big EQ shifts as it crosses models, evolving texture with no external gear.
tags: [ramping, self-modulation, evolving, factory, signature]
dips:
  MODEL (ramp-target): on
  BOUNCE: on
  RANDOM: on
controls:
  - { name: "Volume", type: knob, value: "= ramp SPEED while ramping (hold left footswitch to set actual volume)" }
---

# Tape Hopper (auto model-jumping)

## Concept
The pedal autonomously jumping between tape machines — big EQ shifts as it crosses models, evolving texture with no external gear. Since there's NO MIDI clock on this pedal, the internal Bounce IS your evolving-motion engine.

## How to play it
1. Enable the **MODEL** ramp-target dip.
2. Enable the **BOUNCE** dip and the **RANDOM** dip.
3. The **Volume knob becomes ramp SPEED** while ramping — hold the left footswitch to set the actual volume.
4. **Save the whole ramp + dip setup to a preset** so the moving patch recalls intact.

## Notes
- Trick: Aux = **Filter** + tap aux *pauses* a Model ramp (Filter bypasses the model).
- The preset saves the *moving* patch, not a static state.

## Sources
- 🟢 `research/links/genloss-mkii-recipes-where-they-live.md` (manual pg.38–41) + `research/transcripts/nickrees-chasebliss-ramping-genloss-mood-reverse.md` + `research/transcripts/kevwyxin-read-the-manual-part2-advanced-dips-hidden.md`.
- Transformed from Pedalxly Generation-Loss-Patches.md (factory/artist provenance).
