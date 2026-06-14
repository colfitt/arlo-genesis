---
type: patch
title: Tremolo Pad (Motion mode)
device: Chase Bliss Clean
date: 2026-06-14
description: A pseudo-tremolo that modulates the AMOUNT of compression (not EQ) for a dynamic pulsing pad — sustained drones with a breathing throb before the time/tape boards.
tags: [modulation, tremolo, motion, pad, drone, community, signature]
dips:
  Dusty: off
  Swell Aux: off
  Motion: on
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: off
  MISO: off
controls:
  - { name: "Dynamics", type: knob, value: "mod DEPTH (more CW = deeper throb)" }
  - { name: "Attack", type: knob, value: "mod RATE (CCW faster)" }
  - { name: "Sensitivity", type: knob, value: "by LED (motion only occurs while playing above threshold; fades below it)" }
  - { name: "Wet", type: knob, value: "up" }
  - { name: "Dry", type: knob, value: "to taste" }
  - { name: "EQ", type: knob, value: "noon (leave flat — Motion drives the comp LFO instead)" }
  - { name: "Release", type: switch, value: "to taste", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (or L for extra organic wobble — combine freely)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
  - { name: "Slot/Bank", type: knob, value: "MIDDLE 'live' slot is a good keeper for instant recall" }
---

# Tremolo Pad (Motion mode)

## Concept
With the MOTION dip on, Clean modulates the AMOUNT of compression (rather than the EQ) — a pseudo-tremolo that throbs the dynamics for a breathing, pulsing pad. Dynamics sets the modulation depth and Attack sets the rate. Built for sustained VG-800/baritone drones that want a breathing throb before the time/tape boards. A standalone tremolo voice that's also a comp.

## How to play it
1. **Engage the MOTION dip.**
2. Dynamics = mod DEPTH (more CW = deeper throb).
3. Attack = mod RATE (CCW faster).
4. Sensitivity by LED — motion only occurs while playing above threshold and fades below it.
5. Wet up; Dry to taste; EQ noon (leave flat — Motion drives the comp LFO instead).
6. Mode MID; Physics MID (or LEFT for extra organic wobble — combine freely).

## Notes
- Python (Elektronauts) pairs Physics LEFT for "more nuanced than the heavy-handed dropouts on GenLoss II/Lossy."
- Mix-and-match Motion freely with Physics, EQ modes, Sag, and Dusty.
- The MIDDLE "live" slot is a good keeper (Python keeps Motion on a preset for instant recall).

## Sources
- `research/links/elektronauts-clean-community-recipes.md` (Python: Motion pseudo-tremolo saved to second preset slot)
- `research/links/cb-manual-clean-compression-recipes.md` (MOTION: Dynamics = depth, Attack = rate, p.35)
- `research/transcripts/chase-bliss-clean-official-video-manual.md`
- Transformed from Pedalxly Clean-Patches.md (community)
