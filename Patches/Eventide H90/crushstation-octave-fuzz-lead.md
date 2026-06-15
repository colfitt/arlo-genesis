---
type: patch
title: "CrushStation — Octave Fuzz Lead (sag + crushed octave)"
device: Eventide H90
date: 2026-06-15
description: "Singing, saturated lead with an octave crushed into the dirt and tube-amp \"sag\" for a broken, dynamic feel — Eventide harmonizer tech baked into a distortion. A driven lead voice for the End board. Control set from the Eventide manual/product page; exact values not published — dial from recipe."
tags: [crushstation, distortion, fuzz, octave, lead, sag, drive]
dips:
  COMPRESSOR_SUSTAINER: "post-distortion for consistent lead sustain"
  GRIT_SUSTAIN: "raise both to cross into fuzz"
  SIBLING: "WeedWacker is the cleaner-drive sibling"
controls:
  - { name: "Preset A Algorithm", type: switch, value: "CrushStation (true stereo)" }
  - { name: "Drive", type: knob, value: "to taste — subtle boost -> full distortion" }
  - { name: "Octaves", type: knob, value: "mixes pitch-shifted octaves in BEFORE distortion" }
  - { name: "Sag", type: knob, value: "tube-amp sag — sputtery/crushed/broken character" }
  - { name: "Grit", type: knob, value: "push toward fuzz" }
  - { name: "Sustain", type: knob, value: "push toward fuzz / lead singing" }
  - { name: "Mix", type: knob, value: "clean (full left) -> dirty (full right)" }
  - { name: "Bass", type: knob, value: "EQ low shelf — dial to taste" }
  - { name: "Mids (tunable freq)", type: knob, value: "EQ mid band, tunable center frequency" }
  - { name: "Treble", type: knob, value: "EQ high shelf — dial to taste" }
  - { name: "Compressor / Sustainer", type: switch, value: "pre or post distortion (post for consistent lead sustain)", options: ["pre", "post"] }
---

# CrushStation — Octave Fuzz Lead (sag + crushed octave)

## Concept
A singing, saturated lead with an octave crushed into the dirt and tube-amp "sag" for a broken, dynamic feel — Eventide harmonizer tech baked into a distortion. Octaves are mixed in **before** the distortion so the pitch-shifted layer gets ground up with the rest of the signal; Sag gives the sputtery, crushed, broken response. CrushStation is true stereo. A driven lead voice for the End board.

## How to play it
1. Load CrushStation.
2. Set Drive to taste; add Octaves for the octave-up bite.
3. Dial Sag for the broken/sputtery character.
4. Shape with Bass / Mids / Treble and add Sustain for lead singing.
5. Blend Mix toward dirty but keep a touch of clean for clarity.

## Notes
- Octaves are mixed in BEFORE the distortion; CrushStation is true stereo.
- Place the Compressor / Sustainer post-distortion for consistent lead sustain; raise Grit + Sustain to cross into fuzz. WeedWacker is the cleaner-drive sibling.
- Control set published (manual / product page); exact values not published — dial from recipe.

## Sources
- https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/algorithms/distortion.html (CrushStation: Drive, Sag, Grit, Octaves before distortion, Compressor/Sustainer pre/post, Bass/Mids/Treble)
- https://store.eventideaudio.com/products/crushstation (Sag, Octaves, clean/dirty Mix)
- Transformed from Pedalxly H90-Patches.md (community)
