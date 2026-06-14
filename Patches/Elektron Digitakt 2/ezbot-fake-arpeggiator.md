---
type: patch
title: EZBOT Fake Arpeggiator (single-cycle sparkle)
device: Elektron Digitakt 2
date: 2026-06-14
description: Top-end sparkle layer over an ambient bed — a harmonically-rich plucked high voice using single-cycle GRID and an LFO "scan", per EZBOT.
tags: [ambient, sparkle, single-cycle, generative, factory, artist, signature]
controls:
  - { name: "Pattern length", type: knob, value: "8 steps (filled with notes)" }
  - { name: "Sample", type: switch, value: "Single-cycle waveform, FORWARD LOOPING" }
  - { name: "SRC (machine)", type: switch, value: "GRID", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "GRID resolution", type: knob, value: "64" }
  - { name: "LFO1 DEST", type: switch, value: "SLICE SELECT (as an LFO scan)" }
  - { name: "LFO1 WAVE", type: switch, value: "SINE or RANDOM (+ random SLEW)" }
  - { name: "Wavetable position", type: knob, value: "middle (LFO hovers around centre)" }
  - { name: "AMP DECAY", type: knob, value: "short (pluck)" }
  - { name: "FILTER DECAY", type: knob, value: "short (pluck)" }
  - { name: "LFO2 DEST", type: switch, value: "Filter cutoff (very slow)" }
  - { name: "Second copy speed", type: knob, value: "2× speed" }
  - { name: "Pan", type: knob, value: "each note hard-panned far L / far R" }
  - { name: "Reverb / Delay sends", type: knob, value: "heavy" }
---

# EZBOT Fake Arpeggiator (single-cycle sparkle)

## Concept
A top-end sparkle layer that sits as the shimmer over the wall. An 8-step note sequence plays a single-cycle waveform in GRID, while an LFO "scans" the slice/wavetable position to keep the timbre moving. Short pluck envelopes, a second very-slow LFO on the filter, a 2× copy and hard panning turn it into a faux-arpeggio shimmer over an ambient bed.

## How to play it
1. Fill an 8-step sequence with notes.
2. Sample = a single-cycle waveform set to FORWARD LOOPING; SRC = GRID, grid resolution `64`.
3. Route LFO → SLICE SELECT as an "LFO scan" (sine or RANDOM waveform + random `SLEW`); set wavetable position to the middle so the LFO hovers around centre.
4. Shape to a pluck: short `DECAY` on AMP and FILTER; remove the top end (it sits high); volume down.
5. Add a second LFO → filter cutoff, very slow.
6. Run one copy at 2× speed; hard-pan each note far L / far R.
7. Heavy reverb + delay.

## Notes
- EZBOT: "one of my favorite tricks." It sits as the shimmer over the wall (pairs over the bed of patch 1).
- Put it on a high track (e.g. 5–6) over the bed.

## Sources
- Ref: EZBOT — "Digitakt II Ambient Music Tutorial" (yt `4xBD3wQRR3I`).
- `research/transcripts/ezbot-dt2-ambient-music-tutorial.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (factory/artist)
