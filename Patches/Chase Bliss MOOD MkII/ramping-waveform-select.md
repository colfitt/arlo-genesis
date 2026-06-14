---
type: patch
title: RAMPING WAVEFORM select (auto-evolving drones)
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: Choose the LFO shape for internal ramping/bounce — a hidden option (hold both footswitches, turn MIX). Random / smooth-random on CLOCK = a self-evolving downsample drone.
tags: [hidden, ramp, lfo, generative, drone, factory, signature]
hidden:
  RAMPING WAVEFORM (MIX): fully CCW = triangle (default) → square → sine → random (stepped) → smooth-random (fully CW)
controls:
  - { name: "LEFT + RIGHT footswitches (hidden access)", type: button, value: "HOLD both (LEDs green), then turn MIX" }
  - { name: "MIX", type: knob, value: "after exiting hidden mode, MIX sets ramp speed when a BOUNCE/ramp dip is engaged" }
dips:
  BOUNCE/ramp (on the target knob): engage to run the ramp
---

# RAMPING WAVEFORM select (auto-evolving drones)

## Concept
Choosing the LFO shape for the internal ramping/bounce — generative degrade. A hidden option: hold **both footswitches** (LEDs green), then turn **MIX**. Fully CCW = triangle (default) → square → sine → random (stepped) → smooth-random (fully CW). Engage the ramp via the BOUNCE/ramp dip on the target knob; MIX then sets ramp speed.

## How to play it
1. **Hold both footswitches** until the LEDs go green (hidden-options mode).
2. Turn **MIX** to pick the waveform: triangle / square / sine / random / smooth-random.
3. Exit hidden mode; engage the BOUNCE/ramp dip on the knob you want to modulate.
4. Use **MIX** to set the ramp speed.

## Notes
- **Random / smooth-random on CLOCK = a self-evolving downsample drone** — set it and let it drift.

## Sources
- manual pp.16, 46–47; chasebliss-mood-mkii-video-manual-pt2.md; youtube-mood-mkii-hidden-options-dip-walkthrough.md
- Transformed from Pedalxly MOOD-MkII-Patches.md (factory)
