---
type: patch
title: Comb+ Banjo / Plucked-String Resonator
device: Elektron Digitakt 2
date: 2026-06-14
description: Turn a real banjo pluck (or noise burst) into a tuned metallic string / drone — banjo-as-lead through a Karplus-Strong-style Comb+ resonator.
tags: [banjo, comb, string, resonator, karplus-strong, factory, signature]
controls:
  - { name: "FLTR", type: switch, value: "Comb+ (positive feedback = string-like)", options: ["Lowpass 4","Lowpass 2","Highpass","Bandpass","Comb+","Comb-"] }
  - { name: "ATK/DEC/SUS/REL (filter env)", type: knob, value: "dial by ear (pluck = short ATK + medium DEC; bowed = long DEC/REL)" }
  - { name: "FREQ", type: knob, value: "resonant pitch (dial by ear; track via keytrack)" }
  - { name: "FDBK", type: knob, value: "mid = defined pluck; high = sustained 'string' (WARNING: high FDBK is very loud) — dial by ear" }
  - { name: "LPF (feedback low-pass)", type: knob, value: "open = zingy banjo, lower = mellow — dial by ear" }
  - { name: "ENV (bipolar env depth)", type: knob, value: "dial by ear" }
  - { name: "Keytrack (filter page 2)", type: switch, value: "ON, high depth (FREQ tracks the 12-tone scale)", options: ["ON","OFF"] }
  - { name: "Source", type: switch, value: "Short noise/click burst OR a real banjo pluck" }
  - { name: "BR / Overdrive / SRR", type: switch, value: "PRE-FILTER (crush the raw cycle before the comb)" }
---

# Comb+ Banjo / Plucked-String Resonator

## Concept
Turns a real banjo pluck (or a noise burst) into a tuned metallic string or drone using the DT2-only Comb+ filter as a Karplus-Strong-style resonator. Positive feedback gives a string-like ring (Comb− is hollow/tube). Keytrack on makes the resonant FREQ follow the 12-tone scale so you can play it. Crush before the comb for "recorded-wrong" texture.

## How to play it
1. Set `FLTR = Comb+` (positive feedback = string-like; Comb− = hollow/tube).
2. Dial the filter env `ATK/DEC/SUS/REL`, `FREQ` (resonant pitch), `FDBK` (feedback gain — mid = defined pluck, high = sustained "string"), `LPF` (feedback low-pass — open = zingy banjo, lower = mellow), `ENV` (bipolar env depth).
3. Turn Keytrack ON (filter page 2, high depth) so `FREQ` tracks the 12-tone scale.
4. Source = a short noise/click burst or a real banjo pluck.
5. For a pluck: short `ATK` + medium `DEC`. For a bowed drone: long `DEC/REL` or `AMP DECAY = INF` + a slow LFO → `FREQ`.
6. Put BR / Overdrive / SRR pre-filter — crush the raw cycle before the comb.

## Notes
- WARNING: high `FDBK` is very loud.
- Param names/ranges/behaviour are manual-authoritative; the ADSR / FDBK / FREQ integers are NOT published anywhere — dial by ear.
- Comb+ is DT2-only. Save as a preset ("Comb Banjo"); good as a kit's lead voice.

## Sources
- `research/links/dt2-manual-comb-filter-string-params.md` (Manual OS1.15A App A pp.105–108)
- `research/links/elektronauts-dt2-comb-filter-plucked-string-recipe.md` (t/222328)
- Transformed from Pedalxly Digitakt-2-Patches.md (factory)
