---
type: patch
title: Reference Cluster dump — fully numeric drone fuel
device: TE OP-1 Field
date: 2026-06-14
description: A literal numeric Cluster starting point (real extracted arrays) for building/importing via op1-dump / libop1 — generic format example, not a curated signature patch.
tags: [drone, cluster, reference, numeric, community]
controls:
  - { name: "Engine (type)", type: switch, value: "cluster", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "knobs[8]", type: knob, value: "[3072,0,512,3,0,0,0,0]" }
  - { name: "adsr[8]", type: knob, value: "[64,64,0,64,14336,64,4000,4000]" }
  - { name: "fx_type", type: switch, value: "nitro" }
  - { name: "fx_params[8]", type: knob, value: "[64,-14337,4515,7232,0,0,0,0]" }
  - { name: "lfo_type", type: switch, value: "value" }
  - { name: "Octave", type: knob, value: "0" }
  - { name: "synth_version", type: knob, value: "2" }
  - { name: "Slot/Bank", type: knob, value: "Cluster slot [3]" }
---

# Reference Cluster dump — fully numeric drone fuel

## Concept

A literal numeric starting point if you build or import via `op1-dump` / libop1. Cluster is supersaw drone fuel — these are REAL extracted arrays (3 independent community reverse-engineering implementations agree), but this is a GENERIC FORMAT EXAMPLE, not a curated signature patch. It's the only fully-numeric Cluster patch on disk.

## How to play it

1. Import the `.aif` (with this embedded JSON) via libop1 into the Cluster engine.
2. Tune by ear from there — the numbers are a starting point, not a destination.
3. 8192 ≈ center; range ≈ 0–32767 for the encoder values.

## Notes

- REAL extracted arrays, but a generic format example — not a signature patch. Treat as drone fuel / import template.
- Import via libop1, then dial to taste.

## Sources

- Gear/TE OP-1 Field/research/links/op1-patch-file-format.md (teoperator synth.go example) + UsageGuide §2
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
