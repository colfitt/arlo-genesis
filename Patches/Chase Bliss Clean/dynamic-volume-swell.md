---
type: patch
title: Dynamic Volume Swell
device: Chase Bliss Clean
date: 2026-06-14
description: Auto-swelling violined attacks with no volume pedal — playing crosses the Sensitivity threshold to swell in, then swells back out below it, feeding pre-swelled material to the granular/loop boards.
tags: [swell, volume-swell, pad, ambient, factory, signature]
dips:
  Dusty: off
  Swell Aux: "off (Dynamic Swell default) — ON only for the Manual Swell variant"
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: "off (momentary) — ON to make AUX a toggle"
  Spread: off
  MISO: off
hidden:
  Swell In time (Wet knob): "~noon (100 ms-4 s) — a nice swelling pad"
  Swell Out time (Dry knob): "~noon (100 ms-4 s) — a nice swelling pad"
controls:
  - { name: "AUX footswitch", type: button, value: "Swell (Dynamic Swell = default, momentary)" }
  - { name: "Sensitivity", type: knob, value: "sets the trigger point (signal swells in above it, swells out below it; green LED tracks it)" }
  - { name: "EQ", type: knob, value: "to taste underneath" }
  - { name: "Dynamics", type: knob, value: "to taste underneath" }
  - { name: "Wet", type: knob, value: "noon (main page) — repurposed as Swell In time on hidden page" }
  - { name: "Dry", type: knob, value: "noon (main page) — repurposed as Swell Out time on hidden page" }
---

# Dynamic Volume Swell

## Concept
Clean's Swell engine produces violined attacks with no volume pedal: when your playing crosses the Sensitivity threshold the signal swells in, and when you drop below it the signal swells back out (the green LED tracks it). The swell-in and swell-out times live in the Hidden Options (Wet = Swell In, Dry = Swell Out, ~100 ms–4 s each); ~noon on both makes a nice swelling pad. Use it on banjo lead lines, baritone drones, or VG-800 pads, and feed the granular/loop boards downstream pre-swelled material.

## How to play it
1. **Engage the AUX footswitch** — Dynamic Swell is the default (momentary). Flip the LATCH dip to make it a toggle instead.
2. Set Sensitivity to the trigger point — signal swells in when playing crosses it, swells out below it.
3. **Hidden Options** (hold both footswitches until LEDs go green): Wet = Swell In time (~noon), Dry = Swell Out time (~noon) for a nice swelling pad.
4. EQ/Dynamics to taste underneath.

## Notes
- **BLIPS variant:** set BOTH Swell In and Swell Out to their FASTEST and playing becomes short, muted, percussive blips.
- **Manual Swell variant:** flip the SWELL AUX dip → AUX triggers a single (tempo-synced) swell; hold mutes / release swells up, tap = instant swell (clock-sync UNCONFIRMED at the CC level).

## Sources
- Clean manual pp.30–31 Swell + Hidden Options pp.16–17 (Wet = Swell In, Dry = Swell Out) — `research/links/cb-manual-clean-compression-recipes.md`
- `research/transcripts/chase-bliss-clean-official-video-manual.md`
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (~noon both = swelling pad; presenter leaves LATCH on so AUX is a regular toggle)
- Transformed from Pedalxly Clean-Patches.md (factory)
