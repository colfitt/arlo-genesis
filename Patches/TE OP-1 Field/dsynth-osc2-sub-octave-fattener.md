---
type: patch
title: "DSynth OSC2 — sub-octave fattener (tuning map)"
device: TE OP-1 Field
date: 2026-06-15
description: "Tune DSynth's second oscillator to specific community-MEASURED offsets that produce phaser-thickening and sub-octave reinforcement — turning a thin tone into a big clean bass or fat lead with no FX. One of the few OP-1 recipes with real reproducible per-value numbers (forum-measured, reproducible on the engine)."
tags: [bass, dsynth, sub, detune, tuning-map, field]
dips:
  OSC2_FREQUENCY: "reached by holding [Shift] while turning the OSC2 pitch encoder"
controls:
  - { name: "Engine", type: switch, value: "DSynth ([Shift]+[Synth] / T1)" }
  - { name: "OSC2 frequency offset", type: knob, value: "1 or 42 (fat phaser lead) / 18, 37, 55 (sub-octave) / 29 (1 oct down clean) / 50 (2 oct down + light sub)", options: ["0 = same octave clean","1 = bigger + phaser","18 = sub-oscillator","29 = one octave down clean + phaser","37 = sub-oscillator","42 = bigger + phaser","50 = two octaves down clean + light sub","55 = sub-oscillator"] }
  - { name: "Filter", type: knob, value: "~36 (neutral balance point)", options: ["0-36 = dark (cuts highs)","36 = neutral balance point","36-90 = bright (cuts lows)","past 90 = inaudible"] }
  - { name: "OSC1 / remaining params", type: knob, value: "to taste (DSynth has ~8 params across two oscillators)" }
---

# DSynth OSC2 — sub-octave fattener (tuning map)

## Concept

DSynth is the OP-1's deepest stock engine (~8 params across two oscillators). Tune its second oscillator to specific measured offsets and you get phaser-thickening and sub-octave reinforcement — a thin tone becomes a big clean bass or a fat lead with no effects at all. This is one of the few OP-1 recipes with real, reproducible per-value numbers: the OSC2 frequency map and the filter balance point below are community-MEASURED values (forum testing), not dialed-by-ear guesses.

## How to play it

1. Select DSynth ([Shift]+[Synth] / T1).
2. For a fat, phaser-thickened lead set OSC2 frequency to **1** or **42**.
3. For sub-octave weight under a bass set OSC2 to **18**, **37**, or **55**.
4. For clean octave-down doubling use **29** (one octave) or **50** (two octaves + light sub).
5. Keep the filter near **36** as a tonal balance point, then push up (brighter) or down (darker) to taste.

## Notes

- HONESTY FLAG: the OSC2 offset map and the filter-36 balance point are a published forum MEASUREMENT, not a TE spec — but they're reproducible on the engine, which makes this seed unusually concrete. OSC1 and the remaining DSynth params are a dialable recipe (set to taste); no published per-knob values exist for those.
- OSC2 frequency is reached by holding [Shift] while turning the OSC2 pitch encoder.
- DSynth is the OP-1's deepest stock engine (~8 params across two oscillators).

## Sources

- op-forums.com/t/op-1-master-the-dsynth-engine/23301 (user-measured OSC2 frequency map + filter range values)
- Community testing (forum-measured values, reproducible on the engine)
