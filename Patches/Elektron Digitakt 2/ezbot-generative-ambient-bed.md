---
type: patch
title: EZBOT Generative Ambient Bed (wavetable drone)
device: Elektron Digitakt 2
date: 2026-06-14
description: Evolving, never-repeating ambient bed from DT2 factory wavetable sounds — the core generative-ambient template for the rig, per EZBOT (Matthew Piecora).
tags: [ambient, generative, drone, wavetable, factory, artist, signature]
controls:
  - { name: "Per-Track Scaling RESET (FUNC)", type: switch, value: "INFINITY (no auto-reset → polymetric)" }
  - { name: "Scale", type: switch, value: "HARMONIC MINOR" }
  - { name: "Keyboard FOLD", type: switch, value: "ON (2 octaves on trig keys)", options: ["ON","OFF"] }
  - { name: "SRC (machine)", type: switch, value: "GRID", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "GRID", type: knob, value: "64 (fine scan)" }
  - { name: "LOOP", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "AMP shape", type: knob, value: "pluck" }
  - { name: "Track PROBABILITY", type: knob, value: "≈ 20 %" }
  - { name: "LFO1 MULT", type: knob, value: "1 (not a tempo multiple → very slow)" }
  - { name: "LFO1 SPEED", type: knob, value: "16" }
  - { name: "LFO1 WAVE", type: switch, value: "TRIANGLE" }
  - { name: "LFO1 MODE", type: switch, value: "FREE", options: ["FREE","TRIG","HOLD","ONE","HALF"] }
  - { name: "LFO1 DEST", type: switch, value: "Multimode-filter FREQUENCY" }
  - { name: "Delay Send (DEL)", type: knob, value: "≈ 88" }
  - { name: "Reverb Send (REV)", type: knob, value: "≈ 90" }
  - { name: "Delay X (ping-pong)", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "Delay WID", type: knob, value: "hard L/R" }
  - { name: "Tempo (BPM)", type: knob, value: "≈ 80" }
---

# EZBOT Generative Ambient Bed (wavetable drone)

## Concept
The rig's default ambient canvas: an evolving, never-repeating bed built entirely from DT2 factory wavetable sounds. A 7-step sequence runs against infinite per-track scaling so the phase constantly drifts and the loop never lines up. Two slightly-offset, panned tracks with independently-drifting LFOs on the filter give a wide, living wall. Reverb (with INF/freeze) and ping-pong delay turn it into a wash.

## How to play it
1. Set per-track scaling `RESET = INFINITY` so there's no auto-reset (polymetric, never lines up).
2. Set Scale = HARMONIC MINOR and keyboard FOLD ON (2 octaves on the trig keys).
3. SRC = GRID on a factory wavetable sample, `GRID = 64`, `LOOP ON`; shape AMP to a pluck; scan by routing an LFO to sample `START` (the DT2 has no native "scan").
4. Lay ~7 trigs (7-step seq against infinite scaling = constant phase drift); set track PROBABILITY ≈ 20 %.
5. Duplicate the track (hold track → COPY, paste preset + sequence to track 2), offset track 2 by one step, push its notes up, pan track 1 slightly L / track 2 slightly R.
6. LFO (track 1): `MULT = 1`, `SPEED = 16`, TRIANGLE, mode FREE, `DEST` = multimode-filter FREQUENCY. Copy to track 2 (hold MOD → copy/paste) but change its `SPEED` so the two drift independently.
7. Add keytracking so higher notes open the filter; add a small LFO on BIT REDUCTION for moving grit.
8. Send FX: DELAY ping-pong (`X`) ON, `WID` hard L/R, `DEL` send ≈ 88, top LPF filtered; REVERB send ≈ 90 (reverb has INF/freeze). Tempo ≈ 80 BPM.

## Notes
- The default ambient canvas for the rig. Swap the factory wavetable for a sampled VG-800/baritone drone and it becomes a banjo-rig bed without changing the structure.
- Keep tracks 1–2 as the bed; leave lower tracks (9+) free for live resampling.
- EZBOT's sends (DEL ≈ 88 / REV ≈ 90) and 80 BPM are published/auto-transcribed-from-a-live-build values — "correct in spirit, fine-tune by ear" per his caveat.

## Sources
- Ref: EZBOT (Matthew Piecora) — "Digitakt II Ambient Music Tutorial" (yt `4xBD3wQRR3I`). "My favorite sampler of all time."
- `research/links/ezbot-dt2-ambient-tutorial-recipe.md`
- `research/transcripts/ezbot-dt2-ambient-music-tutorial.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (factory/artist)
