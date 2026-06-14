---
type: patch
title: Master-Track Compressor — Glue / Bus
device: Elektron Octatrack MkII
date: 2026-06-14
description: Track-8 glue on the OT mix — techno/funk compressor starting points, softened toward parallel values for drone instead of pump.
tags: [reference, compressor, master, glue, community]
controls:
  - { name: "Slot/Bank", type: knob, value: "FX block on track 8 (master) or any track" }
  - { name: "GLUE (full mix / T8) ATT", type: knob, value: "24" }
  - { name: "GLUE REL", type: knob, value: "86" }
  - { name: "GLUE THR", type: knob, value: "50" }
  - { name: "GLUE RATIO", type: knob, value: "45" }
  - { name: "GLUE GAIN", type: knob, value: "8" }
  - { name: "GLUE MIX", type: knob, value: "112" }
  - { name: "SNARE/transient ATK", type: knob, value: "9" }
  - { name: "SNARE/transient REL", type: knob, value: "30" }
  - { name: "SNARE/transient THR", type: knob, value: "5" }
  - { name: "SNARE/transient RAT", type: knob, value: "73" }
  - { name: "SNARE/transient GAIN", type: knob, value: "59" }
  - { name: "SNARE/transient MIX", type: knob, value: "127" }
  - { name: "BASS punch (T5) ATK", type: knob, value: "27" }
  - { name: "BASS punch REL", type: knob, value: "96" }
  - { name: "BASS punch THR", type: knob, value: "43" }
  - { name: "BASS punch RATIO", type: knob, value: "34" }
  - { name: "BASS punch GAIN", type: knob, value: "6" }
  - { name: "BASS punch MIX", type: knob, value: "77" }
  - { name: "BASS punch RMS", type: knob, value: "76" }
  - { name: "For drone", type: knob, value: "raise THR, lower RATIO toward 34, MIX 77-112 (parallel)" }
  - { name: "RMS param", type: switch, value: "double-click FX1 switches Peak↔RMS", options: ["Peak", "RMS"] }
---

# Master-Track Compressor — Glue / Bus

## Concept
Track-8 glue on the OT mix. These are techno/funk starting points; soften toward the parallel values (higher THR, lower RATIO, MIX 77-112) for drone so the wall doesn't choke instead of pumping. Track VOLUME is PRE-FX, so it drives the comp.

## How to play it
1. **GLUE (full mix / T8):** ATT = 24, REL = 86, THR = 50, RATIO = 45, GAIN = 8, MIX = 112.
2. **SNARE/transient (single track):** ATK = 9, REL = 30, THR = 5, RAT = 73, GAIN = 59, MIX = 127.
3. **BASS punch (T5):** ATK = 27, REL = 96, THR = 43, RATIO = 34, GAIN = 6, MIX = 77, RMS = 76.
4. Note: track VOLUME is **PRE-FX** (drives the comp); the RMS param (double-click FX1) switches Peak↔RMS.
5. **For drone:** raise THR, lower RATIO toward 34, MIX 77-112 (parallel) so the wall doesn't choke; **scene-lock MIX = 0 when resampling through T8** (anti re-compression).

## Notes
- ⚠️ Values are **techno/funk-genre starting points** — soften for drone/doom as noted.
- signature_fit = no on the raw values; the "soften for drone" path is the rig-relevant read.

## Sources
- Ref: Elektronauts — "Glue Compressor settings" (previewlounge, konputa, Apr 2018)
- research/links/master-compressor-glue-settings.md
- Transformed from Pedalxly Octatrack-MkII-Patches.md (community)
