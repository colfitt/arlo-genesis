---
type: patch
title: Filter-House Crossfader Open/Close
device: Elektron Octatrack MkII
date: 2026-06-14
description: Daft Punk filter-house cutoff automation performed on the OT crossfader — the rig's most natural filter-house controller (taste-profile, designed-to-emulate).
tags: [filter-house, crossfader, scenes, taste-profile, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "OT-E1. Bank A / Part 1; Scene A = scene slot 1, Scene B = scene slot 2" }
  - { name: "Track machine", type: switch, value: "Flex, LOOP ON (disco/funk loop or resampled banjo/VG figure)", options: ["Flex", "Static"] }
  - { name: "FX1", type: switch, value: "multimode resonant filter" }
  - { name: "FX2", type: switch, value: "delay" }
  - { name: "Scene A (fader left)", type: button, value: "filter CLOSED (CUTOFF low, RESONANCE up)" }
  - { name: "Scene B (fader right)", type: button, value: "filter OPEN (CUTOFF high)" }
  - { name: "Slow LFO → FX1 cutoff", type: switch, value: "motion under it" }
  - { name: "Lo-Fi (bit reduction)", type: switch, value: "SP-1200 grit" }
---

# Filter-House Crossfader Open/Close

## Concept
Daft Punk filter-house cutoff automation performed on the OT crossfader — the rig's most natural filter-house controller. Throwing the crossfader A→B opens the filter, which IS the filter-house build. Designed-to-emulate the electronic-groove-first lineage, adapted to the OT's crossfader/scene engine and this rig's sources. A starting point, not played-and-verified.

## How to play it
1. Put a disco/funk loop (or resampled banjo/VG figure) on a Flex track, LOOP ON.
2. FX1 = multimode resonant filter, FX2 = delay.
3. Scene A (fader left) = filter CLOSED (CUTOFF low, RESONANCE up). Scene B (fader right) = filter OPEN (CUTOFF high).
4. Throwing the crossfader A→B IS the filter-house build.
5. Add a slow LFO → FX1 cutoff under it for motion; Lo-Fi (bit reduction) for SP-1200 grit.

## Notes
- OT-E1. Bank A / Part 1; Scene A = scene slot 1, Scene B = scene slot 2.
- Designed-to-emulate; starting point, dial to taste.

## Sources
- Ref: Daft Punk filter-house (cutoff sweep opens the loop over a build)
- Research/Taste-Profile/sources/splice-filter-house-techniques.md + daft-punk-homework-synths-reverbmachine.md
- Transformed from Pedalxly Octatrack-MkII-Patches.md (DOUG-designed)
