---
type: patch
title: Board-2 terminus global config (routing / trails)
device: OBNE Dark Star V3
date: 2026-06-14
description: The correct global setup for Dark Star as the last stereo device on Board 2 before the handoff to Board 3 — Stereo routing, trails on, normal Spread (DOUG-designed).
tags: [routing, trails, global, setup, designed, signature]
controls:
  - { name: "Routing", type: switch, value: "Stereo (hold On/Off + tap Preset until bottom LED blinks)", options: ["Mono", "Mono-In-Stereo-Out", "Stereo"] }
  - { name: "Trails", type: switch, value: "ON (hold Preset 5s while assigning routing; faster blink = trails on)", options: ["off", "on"] }
  - { name: "Spread", type: knob, value: "full CW / normal (unless you want reversed-image disorientation)" }
---

# Board-2 terminus global config (routing / trails)

## Concept
The correct global setup for Dark Star as the last stereo device on Board 2 before the handoff to Board 3 (Generation Loss → Big Time → MOOD → Blooper → H90 + Chroma). Stereo routing, trails on so Board 3 keeps chewing the tail when bypassed, normal Spread unless you want the reversed-image disorientation. Firmware target V3.0R.

## How to play it
1. Set Routing = Stereo — hold On/Off + tap Preset until the bottom LED blinks.
2. Set Trails = ON — hold Preset for 5 s while assigning routing; a faster blink = trails on.
3. Keep Spread full CW / normal unless you want the reversed-image disorientation.
4. Chain: OBNE Parting → CB Lost & Found → Hologram Microcosm → Walrus QI Etherealizer → Dark Star → (stereo to Board 3).

## Notes
- Routing + trails save GLOBALLY, not per-preset.
- The routing/trails mechanics are manual-confirmed; the rig-specific choices are designed.
- Bass sub-pad variant: Mix well below unity, Filter LPF, Pitch octave-down (the analog dry-through keeps low-end punch).
- VG-800 synth/pad patches = the most seamless walls (sustain into sustain; poly patches artifact under heavy Pitch/Crush, which is on-aesthetic).
- Firmware target V3.0R.

## Sources
- designed from DeepResearch §5-6 + UsageGuide §5 + manual p.3
- Transformed from Pedalxly Dark-Star-V3-Patches.md (designed)
