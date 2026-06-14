---
type: patch
title: EZBOT Steve-Reich Tape-Loop Phasing Pair
device: Elektron Digitakt 2
date: 2026-06-14
description: Self-phasing shimmer bed under a drone (classic Reich tape-loop motion) built from a resampled DT2 performance, per EZBOT.
tags: [ambient, generative, phasing, resample, drone, factory, artist, signature]
controls:
  - { name: "RECORDER source", type: switch, value: "MAIN OUTS" }
  - { name: "Record mode", type: switch, value: "PLAY-RECORD (quantized from bar 1)" }
  - { name: "Record length", type: knob, value: "4 bars" }
  - { name: "Copy A SRC (machine)", type: switch, value: "ONESHOT", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "Copy B SRC (machine)", type: switch, value: "ONESHOT", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "Trig LENGTH (both copies)", type: knob, value: "INFINITY (NOT 64 — so phase doesn't reset each pass)" }
  - { name: "Trig CONDITION (both copies)", type: switch, value: "1ST" }
  - { name: "LOOP", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "Pattern length", type: knob, value: "64 steps (4 bars)" }
  - { name: "Pan", type: knob, value: "one copy hard L, one copy hard R" }
---

# EZBOT Steve-Reich Tape-Loop Phasing Pair

## Concept
A self-phasing shimmer bed that recreates Steve Reich's tape-loop motion entirely on the box. Resample a 4-bar performance off the MAIN OUTS (capturing the delay/reverb/bit-reduction you dialed), then run two identical copies started together. Because the DT2 captures true stereo, slightly offsetting one copy and hard-panning them lets the two slowly phase against each other into an evolving wash.

## How to play it
1. Resample MAIN OUTS: `RECORDER` source = MAIN OUTS, use PLAY-RECORD (recording starts on `PLAY` = quantized from bar 1 — a threshold would clip the transient). Record 4 bars.
2. Save as `loop1`, place on a lower "resample track" (e.g. track 9); trig `LENGTH` = 4 bars = 64 steps.
3. Make two copies, both SRC = ONESHOT, both 64 steps, `LOOP ON`, started together.
4. Critical: set both trigs' condition = 1ST and trig `LENGTH = INFINITY` (not 64) so they don't reset the phase each pass.
5. Offset one copy slightly (start/end) and hard-pan one L, one R → the two slowly phase against each other.
6. Optionally repitch / reverse / drop an octave for a swelling bed.

## Notes
- The `1ST` + `LENGTH = INFINITY` fix is the load-bearing detail EZBOT found on-camera — without it the phases keep re-syncing.
- Resample-then-crush (SRR + BitRed = "jagged edges → more harmonics") is the on-aesthetic degrade move.
- Use resample tracks 9–10; save loops to the +Drive sample pool.

## Sources
- Ref: EZBOT — "Digitakt II Ambient Music Tutorial" (yt `4xBD3wQRR3I`).
- `research/transcripts/ezbot-dt2-ambient-music-tutorial.md`
- `research/links/ezbot-dt2-ambient-tutorial-recipe.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (factory/artist)
