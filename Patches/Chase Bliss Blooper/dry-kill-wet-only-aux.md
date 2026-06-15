---
type: patch
title: "Dry Kill — wet-only loop in a parallel/aux path"
device: Chase Bliss Blooper
date: 2026-06-15
description: "Engage the DRY KILL dip so Blooper outputs only the wet loop, letting it live in a parallel/aux path while the rig's dry chain stays untouched — the documented mitigation for Blooper's mono collapse (factory manual dip recipe + DeepResearch routing analysis)."
tags: [routing, looper, setup, stereo, factory]
dips:
  DRY KILL: "ON = removes the clean signal from Blooper's output, leaving only the loop"
controls:
  - { name: "DRY KILL dip", type: switch, value: "ON (wet/loop only at output)", options: ["ON", "OFF"] }
  - { name: "MODE", type: switch, value: "any (this is a routing setup, not a sound recipe)" }
  - { name: "Routing", type: switch, value: "place Blooper in a parallel/aux send (stereo mixer or H90 routing) rather than the main series chain to keep the dry path stereo" }
  - { name: "Other knobs", type: knob, value: "dial from recipe — no published values" }
---

# Dry Kill — wet-only loop in a parallel/aux path

## Concept

Engage the DRY KILL dip to remove the clean signal from Blooper's output, leaving only the wet loop. This lets Blooper live in a parallel/aux path (or keep the rig's dry chain stereo) so the looped wall is mono/wet while the dry signal stays untouched elsewhere — the documented mitigation for Blooper's mono collapse.

## How to play it

1. Engage the DRY KILL dip so only the loop comes out of Blooper.
2. Route Blooper as a parallel/aux device (via a mixer or the H90's routing) so its mono wet loop sits alongside an untouched stereo dry path.
3. Capture and play loops as a wet-only layer that doesn't fold the whole rig to mono.
4. If left in the main series chain instead, accept that the rig is mono from Blooper onward whenever powered.

## Notes

- DeepResearch §5: as wired in series, the rig is mono from Blooper's input onward; DRY KILL + a parallel path is the way to keep the dry chain stereo.
- The dip is physical-only, not MIDI-addressable.
- This is a setup/routing patch, not a sound recipe — no knob values are published, so all other controls are a dialable recipe rather than sourced settings.

## Sources

- `research/links/blooper-manual-named-patches-dip-recipes.md` (DRY KILL dip, manual pp.40-42)
- `research/Blooper-DeepResearch.md` §5 (DRY KILL + parallel/aux path to preserve stereo dry chain)
