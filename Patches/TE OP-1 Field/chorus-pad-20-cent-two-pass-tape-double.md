---
type: patch
title: ±20-cent chorus pad (two-pass tape double)
device: TE OP-1 Field
date: 2026-06-14
description: A wide chorused stereo pad with no FX slot used — a hard-panned two-pass tape double detuned ±20 cents frees the single master FX slot for reverb. Shoegaze width.
tags: [pad, chorus, tape-trick, shoegaze, width, community, signature]
hidden:
  "[Shift]+Metronome → Cents": "+20 (sweet spot is 20 or -20)"
controls:
  - { name: "Source patch", type: switch, value: "Cluster pad, long Attack + long Release (T2)" }
  - { name: "Tape track 1 pan", type: knob, value: "hard RIGHT" }
  - { name: "Tape track 2 pan", type: knob, value: "hard LEFT (same start position)" }
  - { name: "Cents detune (track 2 pass)", type: knob, value: "+20" }
  - { name: "Slot/Bank", type: knob, value: "tape recipe (pairs with cluster_pad / planks)" }
---

# ±20-cent chorus pad (two-pass tape double)

## Concept

A wide chorused stereo pad that uses **no FX slot** — which frees the single master FX slot for reverb. You record the same pad to tape twice, hard-panned opposite, with one pass detuned +20 cents; on playback the two passes beat against each other for a wide chorus. "Sweet spot is 20 or −20" (Skywalkman). Rig-native — the pan-to-tape double turned into a tuned chorus. Shoegaze width.

## How to play it

1. Build a Cluster pad with long Attack + long Release (T2 envelope).
2. Record it to **tape track 1**, panned **hard RIGHT**.
3. `[Shift]+Metronome` → set **Cents = +20**.
4. Record the same pad to **tape track 2**, **hard LEFT**, same start position.
5. Playback = a wide chorus across the stereo field.

## Notes

- Fully-specified community recipe with the exact ±20-cent value on disk.
- Frees the master FX slot for reverb. Pairs with cluster_pad / planks.

## Sources

- Gear/TE OP-1 Field/research/links/op1-cluster-engine-param-map-and-chorus-pad.md (op-forums t/5764, Skywalkman)
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
