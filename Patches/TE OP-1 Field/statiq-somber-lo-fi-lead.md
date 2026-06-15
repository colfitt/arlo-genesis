---
type: patch
title: statiq — somber lo-fi lead / harmonic filler
device: TE OP-1 Field
date: 2026-06-14
description: "A distant, degraded lead — or harmonic-filler wall layer; a banjo-as-lead tone substitute when you want a synth carrying the line. Author: \"Somber, Distant, Lo-Fi.\""
tags: [lead, lo-fi, degraded, harmonic-filler, digital, community, signature]
controls:
  - { name: "Engine", type: switch, value: "Digital", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Octave", type: knob, value: "0" }
  - { name: "FX", type: switch, value: "nitro (on)" }
  - { name: "LFO", type: switch, value: "value (on)", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Slot/Bank", type: knob, value: "Digital slot [1]" }
---

# statiq — somber lo-fi lead / harmonic filler

## Concept

A distant, degraded lead — or a harmonic-filler wall layer. A banjo-as-lead tone substitute when you want a synth carrying the line. The author calls it "Somber, Distant, Lo-Fi. Great as a lead or as harmonic filler." 15.8k downloads — one of the highest-download synth patches. Near-spec for the brief: degraded/distant and dual-use as lead or filler.

## How to play it

1. Load statiq (Digital, Octave 0, Nitro on, value LFO on).
2. Play melodic lines for a distant lo-fi lead.
3. Or hold sustained notes as a degraded harmonic filler under a busier texture.

## Notes

- Per-knob arrays not exposed by op1.fun — `op1-dump` the `.aif` for exact numbers.
- Nitro provides the degraded grit; value LFO adds subtle movement.

## Sources

- Gear/TE OP-1 Field/research/links/op1fun-drone-ambient-patches-concrete.md (nate437 "statiq", op1.fun)
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
