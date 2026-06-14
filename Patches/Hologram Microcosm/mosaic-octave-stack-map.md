---
type: patch
title: Mosaic Octave-Stack Map (A/B/C/D)
device: Hologram Microcosm
date: 2026-06-14
description: The foundation octave-bed engine — pick the octave color you need across Mosaic (Micro Loop) A/B/C/D, with Reverse and mute-source fade-out gestures.
tags: [octave-bed, micro-loop, mosaic, engine-map, factory, signature]
controls:
  - { name: "Engine", type: switch, value: "MOSAIC (Micro Loop)", options: ["A = normal + double speed (octave-UP harmonies)", "B = normal + half speed (octave-DOWN, rich)", "C = all double-speed (no normal)", "D = half/normal/double/quad (one octave below to two above)"] }
  - { name: "Activity", type: knob, value: "number of active loopers" }
  - { name: "Repeats", type: knob, value: "makes loops longer" }
  - { name: "Selector (press in)", type: button, value: "REVERSE the buffer" }
---

# Mosaic Octave-Stack Map (A/B/C/D)

## Concept
The foundation octave-bed engine — choose the octave color you need:
- **A** = normal + double speed (octave-UP harmonies)
- **B** = normal + half speed (octave-DOWN, "really rich, not artificial")
- **C** = all double-speed (no normal)
- **D** = half/normal/double/quad (one octave below to two above)

D is the Othling generative-bed mode; A is the looped-banjo mode.

## How to play it
1. Select engine MOSAIC (Micro Loop) and pick a variation A/B/C/D for the octave color.
2. Use Activity to set the number of active loopers; Repeats makes loops longer.
3. Press the selector in to REVERSE the buffer.
4. With Activity and Repeats high, mute the source for "wonderful fade-outs."

## Notes
- Documented canonical Mosaic map.
- "Mute source for fade-outs" is a usable performance gesture.

## Sources
- `research/transcripts/whirrings-microcosm-44-algorithms-walkthrough.md`
- `research/transcripts/starsky-carr-microcosm-demystified.md`
- `research/Microcosm-DeepResearch.md`
- Transformed from Pedalxly Microcosm-Patches.md (factory)
