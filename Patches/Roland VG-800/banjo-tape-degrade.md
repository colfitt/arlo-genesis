---
type: patch
title: Banjo Through a Falling Tape Machine
device: Roland VG-800
date: 2026-06-15
description: An audiochronicle reviewer's experimental favorite ("a banjo run through a tape machine falling down the stairs") mapped to this rig's tape stage — the hyper-real BANJO model run clean into Generation Loss → JHS 424 / PORTA424 for lo-fi, wobbly, characterful folk-tronica from the banjo source the whole board is built around.
tags: [banjo, lo-fi, tape, experimental, texture, tape-source, signature]
dips:
  OUTPUT SELECT: "LINE/PHONES, R/MONO into Board 1"
controls:
  - { name: "INST TYPE", type: switch, value: "ACOUSTIC", options: ["E.GUITAR", "ACOUSTIC", "SYNTH", "VIO"] }
  - { name: "ACOUSTIC MODEL", type: switch, value: "BANJO (recall the EBM5 BANJO GK profile first)" }
  - { name: "ONBOARD FX (REV/DLY/MOD)", type: switch, value: "OFF (the degrade lives downstream)" }
  - { name: "NORMAL MIX", type: knob, value: "keep clean; route to the rig's tape stage by ear (no published values)" }
  - { name: "Tape stage (downstream)", type: knob, value: "Generation Loss → JHS 424 / PORTA424 for wow/flutter, saturation & pitch wobble; short reverb to glue" }
---

# Banjo Through a Falling Tape Machine

## Concept

An audiochronicle reviewer's experimental favorite, mapped to this rig's tape stage: the hyper-real BANJO model run through tape-machine degradation — "a banjo run through a tape machine falling down the stairs" — lo-fi, wobbly, characterful folk-tronica from the banjo source the whole board is built around. The VG-800 stays clean and gives the tape pedals something to ruin.

## How to play it

1. Recall the EBM5 BANJO GK profile, set `INST = ACOUSTIC → BANJO model`.
2. Keep the VG-800 clean (onboard FX off) and route into `Generation Loss → JHS 424 / PORTA424` for the "falling down the stairs" wow & flutter and saturation.
3. Optionally automate a small pitch drift via an EXP pedal for extra instability.
4. Add a short reverb to glue it; use for off-kilter folk-tronica and texture beds, not straight bluegrass.

## Notes

- Direct from an audiochronicle hands-on review as a creative patch they enjoyed ("banjo run through a tape machine falling down the stairs"). Banjo is one of the VG-800's hyper-realistic stringed models.
- Maps cleanly onto the rig's existing tape stage (Generation Loss → JHS 424 / PORTA424) — the VG-800's clean model gives the tape pedals something to ruin. The on-VG-800 tape-degrade specifics are not published — the wobble is downstream gear; dial by ear.
- The banjo's fast decay is a feature here — the wobble masks the attack glitches. No published VG-800 values; this is a dialable recipe, not sourced knob settings.

## Sources

- https://www.audiochronicle.com/articles/boss-vg-800-review-a-virtual-guitar-rig-that-actually-feels-alive ("banjo through a tape machine falling down the stairs")
- `research/VG-800-DeepResearch.md` §-uses (alt-tuned/clean model → CB Generation Loss → JHS 424 / PORTA424 tape stage)
- `research/calibration-banjo-EBM5.md` (EBM5 BANJO GK profile; banjo fast-decay handling)
