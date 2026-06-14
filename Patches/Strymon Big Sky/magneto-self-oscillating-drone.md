---
type: patch
title: Magneto self-oscillating drone / broken tape verb
device: Strymon Big Sky
date: 2026-06-14
description: Sustained tape-regeneration drone source feeding the print chain (PORTA424/JHS 424) for compounding wear — crank Feedback for the closest the Big Sky gets to self-oscillating runaway (community + DOUG-designed).
tags: [magneto, tape, drone, broken-tape, degraded, community, designed, signature]
hidden:
  Heads: 6
  Spacing: Uneven
  Low End: 10:00
  Diffusion: high (smears the multi-head echo into reverb)
controls:
  - { name: "Machine", type: switch, value: "MAGNETO", options: ["Cloud","Shimmer","Bloom","Chorale","Swell","Magneto","Nonlinear","Reflections","Room","Hall","Plate","Spring"] }
  - { name: "DECAY", type: knob, value: "~300 mS (= delay time)" }
  - { name: "PRE-DELAY", type: knob, value: "1:00 (= Feedback; crank toward max for a sustained DRONE)" }
  - { name: "MOD", type: knob, value: "1:00 (= wow & flutter / tape pitch instability)" }
  - { name: "MIX", type: knob, value: "11:00" }
  - { name: "Slot/Bank", type: knob, value: "03A" }
---

# Magneto self-oscillating drone / broken tape verb

## Concept
A sustained tape-regeneration drone source that feeds the print chain (PORTA424 / JHS 424) for compounding wear. Six heads with Uneven spacing, ~300 mS delay time, and Feedback cranked toward max gives the closest the Big Sky gets to self-oscillating runaway. High Diffusion smears the multi-head echo into reverb; MOD adds wow & flutter / tape pitch instability.

## How to play it
1. Set Heads = 6, Spacing = Uneven; Even spacing + stereo gives a big ping-pong field instead.
2. Crank Feedback (Pre-Delay) toward max for a sustained drone.
3. Feed the output into the PORTA424/JHS 424 print chain for compounding tape wear.

## Notes
- On Magneto the front knobs remap: PRE-DELAY → Feedback, DECAY → delay time.
- Mixed provenance: the crank-feedback-for-drone behavior is community-cited (🔵); the numeric clock values are DOUG-inferred (🟣) starting points, not found settings.
- "Tape Age/Crinkle" granular controls are Magneto STANDALONE/MX features, NOT on the original Big Sky.

## Sources
- research/links/community-magneto-cloud-drone-techniques.md
- designed from research/Big-Sky-DeepResearch.md §13(d)
- Transformed from Pedalxly Big-Sky-Patches.md (community + designed)
