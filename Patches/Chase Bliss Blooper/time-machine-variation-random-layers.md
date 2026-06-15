---
type: patch
title: "Time Machine — Variation (random layer shuffle)"
device: Chase Bliss Blooper
date: 2026-06-15
description: "Factory manual named patch (Time Machine — Idea 1 'Variation', manual p.44) — randomize how many layers play so your loop changes and shifts constantly on its own: a generative arrangement built from ramped LAYERS, no modifiers required. Companion to the existing Time Machine — Sequencing patch (SYNC), where this uses RANDOM."
tags: [layers, ramp, generative, factory]
dips:
  RAMP LAYERS: "on — the layer count is what ramps"
  RAMP BOUNCE: "on — keep the variation moving continuously"
  RAMP RANDOM: "on — randomizes how many layers play (chaotic, not patterned)"
controls:
  - { name: "RAMP knob (= VOLUME knob while ramping)", type: knob, value: "shuffle speed to taste — quicker = unique glitches, slower = remixes (no published value)" }
  - { name: "Mode", type: switch, value: "any", options: ["NORM", "ADD", "SAMP"] }
  - { name: "Slot/Bank", type: knob, value: "physical ramping dips on LAYERS + BOUNCE + RANDOM · ramp dips are not MIDI-addressable" }
---

# Time Machine — Variation (random layer shuffle)

## Concept

The manual's Time Machine "Variation" ramping patch: randomize how many layers are playing so your loops change and shift constantly, all on their own. Put LAYERS into ramping with RANDOM and Blooper keeps reshuffling the arrangement for you — a generative remix with no modifiers, just ramped layers. Where the companion Sequencing patch uses SYNC for a steady, patterned roll, Variation uses RANDOM for chaotic, free-running change.

## How to play it

1. Build a multi-layer loop with several distinct layers.
2. Set the ramping dips to LAYERS + BOUNCE + RANDOM.
3. Set the RAMP knob (the VOLUME knob while ramping) for the shuffle speed.
4. Blooper now randomly varies how many layers play, constantly reshuffling the arrangement on its own.

## Notes

- The "Variation" idea (manual p.44) is distinct from the existing "Sequencing" patch (LAYERS + BOUNCE + SYNC): Variation is RANDOM (chaotic, free-running), Sequencing is SYNC (steady, patterned).
- Works with no modifiers — pure generative arrangement.
- Ramping dips are physical-only and NOT MIDI-addressable; the shuffle speed dials from recipe.
- Quicker ramp = unique glitches; slower ramp = remixes of your loop (manual).
- Exact RAMP-knob value is not published — this is a dialable recipe, set by ear.

## Sources

- `research/links/blooper-manual-named-patches-dip-recipes.md` (TIME MACHINE — Idea 1 Variation, manual p.44, verbatim)
- `research/transcripts/knobs-better-bloops-layers.md` (random ramp LAYERS auto-shuffle)
