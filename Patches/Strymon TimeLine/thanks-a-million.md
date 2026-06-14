---
type: patch
title: Thanks a Million
device: Strymon TimeLine
date: 2026-06-14
description: +1-octave smeared, tape-voiced Ice pad (Matt Piper, official Strymon preset) — the most directly copyable Ice voicing; drop the +OCT to root or a 5th for a smeared banjo-as-lead pad.
tags: [ice, shimmer, octave, pad, banjo-as-lead, ambient, factory, signature]
controls:
  - { name: "TYPE", type: switch, value: "Ice", options: ["dTape","dBucket","Digital","Dual","Pattern","Reverse","Ice","Lo-Fi","Swell","Trem","Filter","Duck"] }
  - { name: "INTRVL", type: switch, value: "+1 OCT", options: ["-OCT","-P5","+P5","+OCT","Oct+5th"] }
  - { name: "BLEND", type: knob, value: "~middle (~50/50 Ice ↔ dry)" }
  - { name: "SMEAR", type: knob, value: "maximum (softens repeat attack)" }
  - { name: "FILTER", type: knob, value: "cranked fully right (tape-delay EQ curve)" }
  - { name: "GRIT", type: knob, value: "dialed in some" }
  - { name: "SPEED (Mod Speed)", type: knob, value: "up (gooey/stereo)" }
  - { name: "DEPTH (Mod Depth)", type: knob, value: "up (gooey/stereo)" }
  - { name: "TIME", type: knob, value: "image/.syx-only (not captured)" }
  - { name: "Slot/Bank", type: knob, value: "user slot (free .syx, import via Nixie 2)" }
---

# Thanks a Million

## Concept
A +1-octave smeared, tape-voiced Ice pad — the most directly copyable Ice voicing of the lot, with every load-bearing parameter given in prose. The copyable core is Smear-max + Filter-full-right + Blend-mid. Drop the +OCT down to root or a fifth for a smeared banjo-as-lead pad.

## How to play it
1. Import the free `.syx` via Nixie 2 (no `.syx` on disk; transcribed setting).
2. Max SMEAR (softens the repeat attack), crank FILTER fully right (tape-delay EQ curve), set BLEND to ~middle.
3. Bring Mod Speed & Depth up for the gooey/stereo movement.
4. For banjo-as-lead, change INTRVL from +OCT to root or +5th.

## Notes
- TIME / MIX / REPEATS are image/.syx-only and not captured.
- FILTER full-right adds highs (the tape-delay EQ curve), per the front-panel constant.

## Sources
- Strymon "This Week's Preset: Thanks a Million" (Matt Piper)
- research/links/strymon-twp-ice-presets-solstice-thanks-a-million.md
- Transformed from Pedalxly TimeLine-Patches.md (factory)
