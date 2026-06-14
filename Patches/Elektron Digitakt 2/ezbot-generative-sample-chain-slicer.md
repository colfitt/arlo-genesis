---
type: patch
title: EZBOT Generative Sample-Chain Slicer
device: Elektron Digitakt 2
date: 2026-06-14
description: Turn a pile of one-shots (banjo / baritone / fuzz fragments) into a self-varying melodic/percussive generator — the canonical DT2 recipe for banjo-as-lead from real plucks, per EZBOT.
tags: [generative, sample-chain, slicer, banjo, factory, artist, signature]
controls:
  - { name: "Track + master length", type: knob, value: "64/64 (FUNC+YES per-track scaling)" }
  - { name: "PRESET POOL", type: switch, value: "Collect short dry sounds (browser → MANAGE → YES → Add to preset pool)" }
  - { name: "Play mode", type: switch, value: "PRESET KEYBOARD (FUNC+down → PRESET POOL)" }
  - { name: "Step-record", type: switch, value: "JUMP (RECORD, STOP, STOP — jumps by trig length)" }
  - { name: "SRC (machine, resampled chain)", type: switch, value: "GRID", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "GRID divisions", type: knob, value: "= number of samples (he uses 16)" }
  - { name: "AMP", type: knob, value: "trim to HOLD/sustain so it cuts clean" }
  - { name: "Overdrive", type: knob, value: "touch" }
  - { name: "LFO1 DEST", type: switch, value: "Slice-select (or p-lock slice per step)" }
  - { name: "Trig CONDITION", type: switch, value: "RANDOM (for generative slice)" }
  - { name: "Scale", type: switch, value: "DORIAN, root G minor (FUNC+keyboard)" }
  - { name: "FLTR (optional)", type: switch, value: "Comb (metallic character)" }
---

# EZBOT Generative Sample-Chain Slicer

## Concept
The workhorse for turning banjo/baritone plucks into evolving, never-identical lines. Build a sample chain of short dry one-shots, lay them with step-record jump, resample the result into one sample, and reload it into GRID. Then make it generative (LFO/p-lock slice with a RANDOM condition) and melodic (scale-constrain each slice). The "Slice" machine from the source video maps to GRID on current OS.

## How to play it
1. Build a sample chain (short dry samples evenly spaced, tails ending before the next slice). Set track + master length 64/64 (`FUNC`+`YES` per-track scaling).
2. Collect sounds into the PRESET POOL (preset browser → MANAGE → YES, check several short dry sounds, left-arrow → Add to preset pool); play via PRESET KEYBOARD mode (`FUNC`+down → PRESET POOL).
3. Lay the chain via STEP-RECORD JUMP (`RECORD`, `STOP`, `STOP`) — it jumps by trig length (1/4 → lands on 1, 5, 9, 13).
4. Resample the track into one sample, load into GRID, trim AMP to HOLD/sustain so it cuts clean, add a touch of OVERDRIVE, set grid divisions = number of samples (he uses 16).
5. Make it generative: LFO → slice-select, or p-lock slice per step with trig condition RANDOM.
6. Make it melodic: `FUNC`+keyboard → DORIAN, root G minor; push trig + push encoder to constrain to scale, assign each slice a random in-scale note.
7. Finish: optional Comb filter for metallic character; resample again.

## Notes
- The "Slice" machine in the video = GRID on current OS.
- Source one-shots live in the preset pool; resampled chain on track 1; mute the source track.

## Sources
- Ref: EZBOT — "A Guide To Generative Sample Chains On Digitakt 2" (yt `9bJpBYmoUMw`).
- `research/transcripts/youtube-ezbot-generative-sample-chains-dt2.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (factory/artist)
