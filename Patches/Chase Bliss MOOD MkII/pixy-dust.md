---
type: patch
title: Pixy Dust
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: A rising "level-up / slot-machine" sparkle as the sample rate climbs — ramp CLOCK from zero to max and lean into the primitive-by-design reverb. (loopydemos.com / Silvio Schmidt)
tags: [reverb, sparkle, ramp, sfx, community]
dips:
  CLOCK (BOUNCE): off (flick on for continuous bounce instead of one-shot ramp)
controls:
  - { name: "Wet MODE", type: switch, value: "Reverb", options: ["Reverb", "Delay", "Slip"] }
  - { name: "CLOCK", type: knob, value: "ramp 0 → max (one-shot RAMP, or continuous BOUNCE via the CLOCK dip)" }
  - { name: "MIX", type: knob, value: "sets the ramp rate" }
hidden:
  RAMPING WAVEFORM (MIX): pairs naturally with this patch — choose shape
---

# Pixy Dust

## Concept
A rising "level-up / slot-machine" sparkle that climbs as the sample rate increases. **Ramp CLOCK from 0 to max** (a one-shot RAMP, or set it to continuously BOUNCE via the CLOCK dip; MIX sets the ramp rate). Lean into MOOD's primitive-by-design reverb for the arcade-sparkle character. An original-MOOD recipe that remains valid on the MkII.

## How to play it
1. Set Wet MODE = **Reverb**.
2. Set up the CLOCK ramp 0 → max — either a one-shot RAMP, or flick the CLOCK dip to BOUNCE for continuous rising sparkle.
3. Use **MIX** to set the ramp rate (how fast the sparkle climbs).
4. Play and let the rising sample rate do the "leveling-up" sparkle.

## Notes
- Pairs naturally with the **RAMPING WAVEFORM** hidden option (see ramping-waveform-select) — pick the LFO shape that drives the bounce.
- Reference: loopydemos.com (Silvio Schmidt).

## Sources
- research/links/mood-mkii-recipe-sources-and-shared-settings.md; MOOD-MkII-UsageGuide.md §2
- Ref: loopydemos.com (Silvio Schmidt)
- Transformed from Pedalxly MOOD-MkII-Patches.md (community)
