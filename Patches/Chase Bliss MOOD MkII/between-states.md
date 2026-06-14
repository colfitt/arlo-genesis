---
type: patch
title: Between States (Delay ⇄ reverb morph)
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: Warp back and forth between multi-tap and reverb-like behavior by ramping or expression-sweeping MODIFY through its range.
tags: [delay, reverb, morph, ramp, expression, factory]
dips:
  MODIFY (BOUNCE): on (auto-ramps MODIFY back and forth)
controls:
  - { name: "Wet MODE", type: switch, value: "Delay (or Reverb)", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Wet MODIFY", type: knob, value: "sweep multi-tap ↔ reverb wash (via BOUNCE dip or expression pedal)" }
hidden:
  RAMPING WAVEFORM (MIX): triangle for smooth, random for generative drift
---

# Between States (Delay ⇄ reverb morph)

## Concept
Warping back and forth between multi-tap and reverb-like behavior. Use **Ramping (BOUNCE dip on MODIFY)** or an expression pedal assigned to MODIFY to sweep it continuously between distinct multi-tap echoes and a reverb wash. The sound morphs "between states" as MODIFY moves.

## How to play it
1. Set Wet MODE = **Delay** (or Reverb).
2. Either flick the BOUNCE dip on MODIFY for auto-ramping, or assign an expression pedal to MODIFY.
3. Let MODIFY sweep back and forth — the texture morphs multi-tap ↔ reverb wash.

## Notes
- Ties to the **RAMPING WAVEFORM** hidden option (ramping-waveform-select): pick triangle for a smooth morph, random for generative drift.

## Sources
- manual pp.24–25 "Between States"; research/links/mood-mkii-official-manual-try-this-recipes.md
- Transformed from Pedalxly MOOD-MkII-Patches.md (factory)
