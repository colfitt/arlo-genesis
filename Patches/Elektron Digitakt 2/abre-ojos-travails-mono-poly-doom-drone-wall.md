---
type: patch
title: Abre Ojos "Travails" Mono→Poly Doom-Drone Wall
device: Elektron Digitakt 2
date: 2026-06-14
description: Industrial doom-drone wall — sample a mono source into the DT2 and Euclidean-layer it into a "poly" drone (maps to baritone / banjo-through-pedals), per Abre Ojos's "Travails" live AV set.
tags: [doom, drone, industrial, euclidean, factory, artist, signature]
controls:
  - { name: "Tempo (BPM)", type: knob, value: "46" }
  - { name: "Source sample", type: switch, value: "Mono source sampled directly into the DT2 (rig: baritone / banjo through Board 1)" }
  - { name: "SRC (machine)", type: switch, value: "GRID", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "Sequencing", type: switch, value: "EUCLIDEAN (FUNC+AMP: two pulse generators + rotation, combine OR/XOR/AND/SUB)" }
---

# Abre Ojos "Travails" Mono→Poly Doom-Drone Wall

## Concept
The rare directly-on-aesthetic, verified DT2 doom-drone artist recipe. Sample a single mono source into the DT2, then use the GRID machine plus EUCLIDEAN sequencing — two pulse generators and rotation, combined with OR/XOR/AND/SUB — to layer that captured material into stacked drone layers while you play the live source on top. Maps cleanly to baritone / banjo through the pedalboard.

## How to play it
1. Set tempo = 46 BPM.
2. Sample the source (for the rig: baritone / banjo through Board 1) directly into the DT2.
3. Use the GRID machine + EUCLIDEAN sequencing (`FUNC`+`AMP`: two pulse generators + rotation, combine with OR/XOR/AND/SUB) to layer the sampled material into stacked drone layers.
4. Play the live source on top.
5. Reference (source patch, Evolver side): oscillators with wave-sequencing, filter mod via mod-wheel, tuned feedback, distortion.

## Notes
- 46 BPM is the one exact number; the Grid+Euclidean layering is the documented method (no per-param values posted).
- Use several Grid tracks fed from one captured drone sample; one kit.
- Euclidean params are NRPN-only on the DT2 (Euclidean Mode On/Off NRPN 3.14, Pulses Gen1 3.8, Pulses Gen2 3.9 — no CC).

## Sources
- Ref: Abre Ojos — "Travails" live AV set (matrixsynth.com, abreojos.net).
- `research/links/matrixsynth-travails-abreojos-dt2-doom-drone.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (factory/artist)
