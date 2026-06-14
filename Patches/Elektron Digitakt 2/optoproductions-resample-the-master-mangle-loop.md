---
type: patch
title: Optoproductions Resample-the-Master Mangle Loop
device: Elektron Digitakt 2
date: 2026-06-14
description: The on-box "recorded-wrong" engine — grow new degraded sounds by sampling the DT2's own master through Grid-slice → Comb → bit-crush, iteratively, per Optoproductions.
tags: [resample, mangle, degrade, recorded-wrong, factory, artist, signature]
controls:
  - { name: "Source AMP env", type: switch, value: "Attack/Hold/Decay; HOLD all the way to NOTE; note length 16; add overdrive; pull DECAY down" }
  - { name: "Resample INPUT", type: switch, value: "MAIN INPUT (scroll INPUT all the way left past L/R = the DT2's own master)" }
  - { name: "Master Overdrive", type: knob, value: "a touch (first pass); OFF on re-use pass (don't stack)" }
  - { name: "Master compression", type: switch, value: "push (first pass); OFF on re-use pass" }
  - { name: "Record", type: switch, value: "16–64 steps, arm, record-on-PLAY (FUNC+clear buffer to clear)" }
  - { name: "Re-use SRC (machine)", type: switch, value: "GRID, 16 slices", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "LOOP", type: switch, value: "ON (granular/glitch; move the loop point)", options: ["ON","OFF"] }
  - { name: "LFO → slice-select", type: switch, value: "WAVE = RANDOM, increase depth" }
  - { name: "FLTR (metallic)", type: switch, value: "Comb (high feedback); or HP filter + raised resonance + 2nd RANDOM LFO → filter freq" }
  - { name: "Per-channel degrade", type: switch, value: "overdrive / bit-crush, then resample again" }
---

# Optoproductions Resample-the-Master Mangle Loop

## Concept
The core "recorded-wrong without a computer" loop. Make a short source, resample the DT2's own master (scroll INPUT past L/R to MAIN INPUT) with master overdrive and compression, then on the next pass slice it in GRID, scan slices with a RANDOM LFO, add HP filter + resonance, push Comb for metallic, crush per-channel, and resample again — growing new degraded sounds iteratively.

## How to play it
1. Make a source: add a trig, AMP env = Attack/Hold/Decay, `HOLD` all the way to NOTE, note length 16, add overdrive, pull `DECAY` down.
2. Resample the master: `SAMPLE` page → `FUNC`+(clear buffer); scroll `INPUT` all the way left past L/R to MAIN INPUT (= the DT2's own master); push with a touch of Master Overdrive + master compression; record (16–64 steps), arm, record-on-PLAY.
3. Save (suffix `resample`), assign to a track (e.g. 9).
4. Re-use pass: new pattern, Save Kit → Load Kit, match BPM, turn OFF compressor + master overdrive (don't stack), AHD decay down, `LENGTH` + `LOOP ON` for granular/glitch, move the loop point; record the whole live performance (`INPUT = MAIN INPUT`, `LENGTH = Max`, arm, `PLAY`, twist live).
5. Slice & mangle: SRC = GRID, 16 slices, LFO → slice-select `WAVE = RANDOM` increase depth, play LFO speed/mult + grid `LENGTH` (4, 2); add HP filter raise resonance + 2nd RANDOM LFO → filter freq; try Comb high feedback for metallic; per-channel overdrive/bit-crush. Resample again.

## Notes
- The core "recorded-wrong without a computer" loop for fuzz-wall / banjo prints.
- Resample tracks 9–16; save each pass to the +Drive.

## Sources
- Ref: Optoproductions (Melvin) — "Digitakt 2 Creative Resampling" (yt `pvR1gMepME0`).
- `research/transcripts/optoproductions-dt2-creative-resampling.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (factory/artist)
