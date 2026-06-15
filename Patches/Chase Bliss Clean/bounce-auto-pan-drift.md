---
type: patch
title: "Bounce — Continuous LFO Drift / Auto-Pan"
device: Chase Bliss Clean
date: 2026-06-15
description: "Uses the CONTROL/ramping dip bank's BOUNCE function to continuously LFO-modulate a chosen knob (vs Ramp's one-time move on engage): pick the knob, set SWEEP for the range, Sensitivity = ramp rate. On EQ + SPREAD it's an auto-panning/widening drift; on Wet it's a volume tremolo. Manual (Ramping pp.36-37) + Tape Op notes — dialable recipe, no published clock-face values; Bounce clock-sync is feature-listed but UNCONFIRMED at the CC level."
tags: [modulation, bounce, auto-pan, lfo, ambient, factory]
dips:
  CONTROL bank — Bounce: on
  CONTROL bank — target knob (Dynamics/Attack/EQ/Dry/Wet): "on (pick one)"
  CONTROL bank — Sweep: "set range (top/bottom of modulation)"
  CONTROL bank — Polarity: "to taste (flips direction)"
  CUSTOMIZE bank — Spread: "on only for the auto-pan / widen version"
  (all other dips): off
controls:
  - { name: "Sensitivity", type: knob, value: "ramp/LFO rate (hold the left footswitch to adjust Sensitivity normally while Bounce free-runs)" }
  - { name: "EQ", type: knob, value: "physical position sets one end of the SWEEP range — common Bounce target (with SPREAD = the auto-pan/widen drift)" }
  - { name: "Wet", type: knob, value: "alt Bounce target — modulating Wet = a volume tremolo; its position sets one end of the range" }
  - { name: "Dynamics", type: knob, value: "alt Bounce target — sweeps the compression character over time; its position sets one end of the range" }
  - { name: "Attack", type: knob, value: "alt Bounce target; its position sets one end of the range" }
  - { name: "Dry", type: knob, value: "alt Bounce target; its position sets one end of the range" }
---

# Bounce — Continuous LFO Drift / Auto-Pan

## Concept
The CONTROL (ramping) dip bank has two flavors of automated knob motion. **Ramp** moves a chosen knob one time when you turn Clean on. **Bounce** instead modulates that knob continuously, LFO-style, so the parameter drifts on its own — motion that's independent of your playing dynamics. You pick the target knob with its dip, set the SWEEP dip to define the top/bottom of the modulation range (the knob's physical position sets one end), and use Sensitivity as the ramp/LFO rate. On EQ + SPREAD this is the auto-panning / widening "drift"; on Wet it's a volume tremolo; on Dynamics it sweeps the compression character over time.

## How to play it
1. In the CONTROL dip bank, flip **BOUNCE on** plus the dip for the knob you want modulated (e.g. EQ or Wet).
2. Set the **SWEEP** dip and the target knob's physical position to define the modulation range.
3. Use **Sensitivity** to set the LFO/ramp rate (hold the left footswitch to adjust Sensitivity normally while it's ramping); flip **POLARITY** to change direction.
4. For auto-pan / widening drift, also flip **SPREAD** (CUSTOMIZE bank) and target the **EQ**.
5. The knob now drifts continuously on its own, independent of your playing dynamics.

## Notes
- **No published clock-face values** — this is a dialable recipe. Target knob, SWEEP endpoints, and Sensitivity rate are all set by ear / by LED, not from sourced settings.
- **Bounce = continuous LFO; Ramp (no Bounce) = a one-time move** of the knob when you turn Clean on.
- Distinct from **Motion** (which modulates compression AMOUNT keyed to your playing) — Bounce free-runs and can target any assignable knob.
- **Clock-sync UNCONFIRMED:** Chase Bliss feature-lists clock-sync for Bounce, but it is not verified at the CC/MIDI level — don't assume it locks to the grid.

## Sources
- `research/links/daily-clean-stereo-spread-miso-and-chain-placement.md` (Bounce = LFO-style continuous motion: activate Bounce dip, pick knob, set SWEEP, Sensitivity = ramp rate; on EQ+SPREAD = auto-panning/widening drift; clock-sync UNCONFIRMED)
- `research/Clean-DeepResearch.md` §2 (CONTROL dip bank: Dynamics/Attack/EQ/Dry/Wet/Bounce/Sweep/Polarity; Bounce+knob = LFO modulation, Ramp = one-time, Sensitivity = ramp-speed)
- `research/transcripts/doug-hanson-control-runthrough-demo.md` (green dip bank = ramp Clean's parameters)
- Chase Bliss Clean official manual (Ramping pp.36-37)
