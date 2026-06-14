---
type: patch
title: Cohesive Tuned Kit — Whole-Kit Build
device: Akai MPC Sample
date: 2026-06-14
description: A whole-kit build recipe — tune, level, mute-group, velocity-shape, filter-as-EQ, and pan — so the kit sounds finished instead of amateur.
tags: [drum-craft, kit, mixing, tuning, designed]
controls:
  - { name: "Tune (all drums)", type: knob, value: "one song key (Semi −24…+24 / Fine ±90 ¢)" }
  - { name: "Per-pad Volume", type: knob, value: "−INF…+6 dB (level the kit)" }
  - { name: "Normalize (Shift in Trim/Mix/Amp)", type: button, value: "each one-shot to 0 dB" }
  - { name: "Kit Volume (Shift+K2)", type: knob, value: "leave headroom, don't slam to +6" }
  - { name: "Mute Group (Play page)", type: knob, value: "closed + open hat = same group (closed chokes open)" }
  - { name: "Vel Sens (per-pad)", type: knob, value: "0–127 (127 = most dynamic; 0 = always-full)" }
  - { name: "Filter (per-pad = EQ)", type: switch, value: "HPF hats/perc; LPF busy melodic bed", options: ["LPF2", "LPF4", "HPF2", "HPF4", "BPF"] }
  - { name: "Pan (per-pad)", type: knob, value: "50L–C–50R (kick/snare/sub center; hats/perc/FX out)" }
  - { name: "Slot/Bank", type: knob, value: "Kit / all 16 pads of one bank" }
---

# Cohesive Tuned Kit — Whole-Kit Build

## Concept
A whole-kit build recipe so a kit sounds finished instead of amateur. The AC50 has no parametric EQ, so the per-pad Filter is your EQ. The six-step routine (tune, level/normalize, mute-group, velocity, filter, pan) is designed craft layered onto AC50-confirmed controls.

## How to play it
1. Tune all drums to one song key.
2. Level with per-pad Volume (−INF…+6) plus Normalize each one-shot (`Shift` in Trim/Mix/Amp = Normalize to 0 dB); leave kit-bus headroom (Kit Volume = `Shift+K2`, don't slam to +6).
3. Closed + open hats → same Mute Group so closed chokes open.
4. Per-pad Vel Sens 0–127 (127 = most dynamic; 0 = always-full for a machine-tight hat).
5. Per-pad Filter is your EQ (no parametric EQ): HPF hats/perc, LPF a busy melodic bed.
6. Pan per pad (50L–C–50R): kick/snare/sub center, hats/perc/FX out to the sides.

## Notes
- ⚠️ Don't Normalize sub-heavy hits (worsens low-end output clipping).
- Judge bass on headphones/LSR305s, not the mono speaker (dies below ~200 Hz).

## Sources
- 🟣 designed from `research/links/craft-punchy-drum-samples-on-the-ac50.md` + `research/links/craft-finger-drumming-layout-and-mixing.md` (Normalize fw1.3, NearTao mpcforums t/220503)
- Transformed from Pedalxly MPC-Sample-Patches.md (designed)
