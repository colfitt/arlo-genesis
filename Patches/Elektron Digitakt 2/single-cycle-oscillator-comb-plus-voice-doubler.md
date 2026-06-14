---
type: patch
title: Single-Cycle Oscillator + Comb+ Voice-Doubler
device: Elektron Digitakt 2
date: 2026-06-14
description: A tuned, detunable drone oscillator that doubles or pairs with the banjo lead — single-cycle GRID waveforms with a Comb+ "fake 2nd oscillator".
tags: [drone, oscillator, single-cycle, comb, banjo, community, signature]
controls:
  - { name: "SRC (machine)", type: switch, value: "GRID", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "Source samples", type: switch, value: "AKWF (Adventure Kid Waveforms) or factory wavetables as a chain" }
  - { name: "LFO1 DEST", type: switch, value: "Grid SLOT (sweep waveforms)" }
  - { name: "Sample LENGTH (pseudo-PWM)", type: knob, value: "30 or 60 (very short)" }
  - { name: "LFO (PWM)", type: switch, value: "DEST = sample START (modulate it)" }
  - { name: "FLTR (fake 2nd osc)", type: switch, value: "Comb+", options: ["Lowpass 4","Lowpass 2","Highpass","Bandpass","Comb+","Comb-"] }
  - { name: "FEEDBACK", type: knob, value: "high (FDBK is ear-dialed)" }
  - { name: "Filter KEYTRACK", type: knob, value: "100 %" }
  - { name: "BR / Overdrive / SRR", type: switch, value: "PRE-FILTER (crush the raw cycle before the comb)" }
  - { name: "AMP DECAY", type: knob, value: "INF (hold as a bed)" }
---

# Single-Cycle Oscillator + Comb+ Voice-Doubler

## Concept
A tuned, detunable drone oscillator that doubles or pairs with the banjo lead. Load single-cycle waveforms (AKWF or factory wavetables) into GRID, sweep them with an LFO on grid SLOT, fake PWM by modulating sample START on a very short loop, and use a Comb+ filter with high feedback and 100% keytrack as a fake second oscillator. Crush before the comb and hold with INF decay for a bed.

## How to play it
1. SRC = GRID, load AKWF (Adventure Kid Waveforms, 2000+ free single-cycles) or factory wavetables as a chain.
2. LFO → grid SLOT to sweep waveforms.
3. Pseudo-PWM/wavetable: set sample `LENGTH = 30` or `60` (very short) and modulate sample `START` with an LFO.
4. Fake 2nd oscillator: `FLTR = Comb+`, `FEEDBACK` high, filter `KEYTRACK = 100 %`.
5. Put BR / Overdrive / SRR pre-filter — crush the raw cycle before the comb.
6. Set `AMP DECAY = INF` to hold as a bed.

## Notes
- Concrete: `LENGTH 30/60`, `KEYTRACK 100 %`, AKWF source. `FDBK` is ear-dialed.
- Save as preset "SC Drone Osc"; pair on a track next to patch 13.

## Sources
- `research/links/elektronauts-dt2-single-cycle-waves-oscillator.md` (t/214718 — Billy1992, Humanprogram)
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
