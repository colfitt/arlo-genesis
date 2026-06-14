---
type: patch
title: Gooey Modulation (warble-up delay)
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: A classic "warble up" modulated short delay — auto-ramp TIME from zero up to a short set time via the BOUNCE dip. (loopydemos.com / Silvio Schmidt)
tags: [delay, modulation, warble, community]
dips:
  TIME (BOUNCE): on (auto-ramps TIME from zero up to the set short time)
controls:
  - { name: "Wet MODE", type: switch, value: "Delay", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Wet TIME", type: knob, value: "very short" }
  - { name: "MIX", type: knob, value: "sets ramp rate" }
---

# Gooey Modulation (warble-up delay)

## Concept
A classic "warble up" modulated short delay. Set a **very short TIME**, then use the dips to auto-ramp TIME from zero up to that short set time (**BOUNCE on TIME**). MIX sets the ramp rate. The result is a gooey, warbling modulation rather than a discrete echo.

## How to play it
1. Set Wet MODE = **Delay** with a very short TIME.
2. Flick the BOUNCE dip on TIME so it auto-ramps from zero up to the set time.
3. Use **MIX** to set the ramp/warble rate.

## Notes
- More a modulation effect than a drone — included for completeness.
- Reference: loopydemos.com (Silvio Schmidt).

## Sources
- research/links/mood-mkii-recipe-sources-and-shared-settings.md; MOOD-MkII-UsageGuide.md §2
- Ref: loopydemos.com (Silvio Schmidt)
- Transformed from Pedalxly MOOD-MkII-Patches.md (community)
