---
type: patch
title: Hold-Sampler Frozen Drone
device: Hologram Microcosm
date: 2026-06-14
description: Freeze a fuzz/baritone/VG-800 wall into a sustaining drone, then scroll A/B/C/D sub-modes over the held bed and play a dry banjo lead on top (Andy Othling technique).
tags: [drone, frozen, hold-sampler, ambient, sustained-wall, factory, artist, signature]
hidden:
  Hold mode (Repeats knob, 2nd bar in Global Config): Toggle (default; settable to Momentary)
  Remote freeze: CC 48
controls:
  - { name: "Engine", type: switch, value: "Any granular/loop engine (Mosaic = looped cluster, Blocks = pad/drone, Tunnel B = single-sample drone)" }
  - { name: "Activity", type: knob, value: "twist live over the freeze" }
  - { name: "Filter", type: knob, value: "roll back (CCW) for less top end" }
  - { name: "Time", type: knob, value: "twist live (fast Time = choppy)" }
  - { name: "Mix", type: knob, value: "pull back so dry passes unaffected over the drone" }
  - { name: "Hold", type: button, value: "right footswitch — freezes the most recent wet segment (held buffer keeps feeding the FX)" }
  - { name: "Slot/Bank", type: knob, value: "RED #45 (PC 45) — frozen-drone beds, Hold-ready" }
---

# Hold-Sampler Frozen Drone

## Concept
Freeze a sustained source (fuzz wall, baritone Jazzmaster, VG-800 pad) into a continuous drone, then play a dry lead over it. Play a phrase, press HOLD to freeze the most recent wet segment, and the held buffer keeps feeding the engine. The headline rig family for banjo-as-lead over sustained walls. The buffer holds more than you hear — switching engines reveals it.

## How to play it
1. Pick any granular/loop engine (Mosaic = looped cluster, Blocks = pad/drone, Tunnel B = single-sample drone).
2. Play a phrase, then press HOLD (right footswitch) to freeze the most recent wet segment.
3. While frozen, scroll the A/B/C/D sub-modes over the held bed to restack octave ranges (each mode-step adds an octave).
4. Roll Filter back (CCW) for less top end without changing modes.
5. Keep twisting Activity and Time live over the freeze (fast Time = choppy).
6. Pull Mix back so your dry signal passes unaffected, then play a fresh lead over the drone.

## Notes
- Hold = Toggle by default; settable to Momentary in Global Config via the Repeats knob (2nd bar). Remote freeze over MIDI = CC 48.
- Looper activation CLEARS the Hold buffer — they are mutually exclusive.
- No numeric knob chart exists in any source; this is a gesture recipe. See the Frozen Drone Bed starting point for a clock-face calibration.
- REAL technique demoed by Othling and Hologram's own video.

## Sources
- `research/transcripts/andy-othling-microcosm-hold-drone-technique.md`
- `research/transcripts/hologram-official-hold-sampler-overview.md`
- `research/links/deliciousaudio-microcosm-hold-sampler-arp-granules.md`
- Ref: Andy Othling (Lowercase Noises)
- Transformed from Pedalxly Microcosm-Patches.md (factory/artist)
