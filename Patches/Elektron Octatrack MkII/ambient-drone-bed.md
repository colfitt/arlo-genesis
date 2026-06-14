---
type: patch
title: Ambient Drone Bed (capture-and-sustain-the-wall-forever)
device: Elektron Octatrack MkII
date: 2026-06-14
description: A sustained, evolving drone bed under live guitar from a fuzz/baritone wall capture — the rig's core ambient/doom texture role.
tags: [drone, ambient, doom, generative, timestretch, lfo, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank B / Part 1 · Static or Flex drone track; CHAIN BEHAVIOUR silence-off" }
  - { name: "Track machine", type: switch, value: "Static (streamed, up to 2 GB) or Flex", options: ["Static", "Flex"] }
  - { name: "TSTR (timestretch)", type: switch, value: "ON to hold pitch at project BPM (or low RATE/TSTR OFF for tape-slow grind)", options: ["ON", "OFF", "AUTO"] }
  - { name: "LFO → FX1 filter cutoff", type: switch, value: "slow (drift)" }
  - { name: "LFO → PITCH", type: switch, value: "slow (drift)" }
  - { name: "LFO → STRT", type: switch, value: "slow/random (sample re-enters at different points each pass → never-repeating drone)" }
  - { name: "FX2", type: switch, value: "Dark Reverb" }
  - { name: "Pitch", type: knob, value: "DOWN ~2 octaves + heavy reverb = instant ambient wall (most-cited single move)" }
  - { name: "Direction", type: switch, value: "REVERSE the source for non-obvious texture", options: ["FWD", "REV", "PIPO"] }
  - { name: "CHAIN BEHAVIOUR", type: switch, value: "silence-off ([FUNC]+[BANK]) so drones sustain into the next pattern" }
  - { name: "BPM", type: knob, value: "30-60 BPM polymetric (different track length per track) + sparse trigs = generative drift" }
---

# Ambient Drone Bed (capture-and-sustain-the-wall-forever)

## Concept
A sustained, evolving drone bed under live guitar, built from a fuzz/baritone wall capture — the rig's core ambient/doom texture role. The STRT-LFO evolving engine, pitch-down-2-octaves, CHAIN-BEHAVIOUR-off sustain, and 30-60 BPM polymetric drift are the cited community techniques; the exact rig wiring is designed/inferred. The generative ambient patch on the OT.

## How to play it
1. Capture a sustained fuzz/baritone wall into a **Static** (streamed, up to 2 GB) or **Flex** machine.
2. Timestretch to hold indefinitely at project BPM (**TSTR ON** to hold pitch, or low RATE/TSTR OFF for tape-slow grind).
3. Put a **slow LFO on FX1 filter cutoff + a slow LFO on pitch** for drift. FX2 = **Dark Reverb**.
4. Run it as a continuous bed under the live guitar.
5. **Generative drift:** minimal trigs (1-2) + a slow/random **LFO on sample START (STRT)** so the sample re-enters at different points each pass → never-repeating drone.
6. **Instant wall:** pitch a sample DOWN ~2 octaves + heavy reverb (the most-cited single move). REVERSE the source for non-obvious texture.
7. **Hold across patterns:** **CHAIN BEHAVIOUR silence-off** ([FUNC]+[BANK]) so drones sustain into the next pattern; **polymetric** (different track length per track) + sparse trigs at **30-60 BPM** = generative drift.
8. **Reverb tails:** route long tails to EXTERNAL reverb (H90/Big Sky) via cue sends — per-track FX cut off on Part change.

## Notes
- Mixed provenance — the STRT-LFO evolving engine + pitch-down-2-oct + CHAIN-BEHAVIOUR-off + 30-60 BPM polymetric are **cited community techniques**; the exact rig wiring is designed/inferred.
- THE generative ambient patch on the OT.

## Sources
- links/elektronauts-drone-ambient-recipes.md + template-ambient-drone-looping-techniques.md + DeepResearch §13(d) (Elektronauts /29992 + /132931)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (DOUG-designed)
