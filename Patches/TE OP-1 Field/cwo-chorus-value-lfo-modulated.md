---
type: patch
title: "CWO — Value-LFO modulated chorus (published values)"
device: TE OP-1 Field
date: 2026-06-15
description: A value-exact CWO chorus recipe with two documented community parameter sets (subtle and thick) — a slow value LFO wobbles CWO's delay knob to turn the Echobode-style overtone-shifting delay into a lush, slightly-detuned chorus. Forum recipe (op1tips), full CWO + LFO values published.
tags: [effect, cwo, chorus, value-lfo, modulation, community]
controls:
  - { name: "FX", type: switch, value: "CWO" }
  - { name: "CWO freq", type: knob, value: "0 (subtle) / ~20% (thick)" }
  - { name: "CWO delay", type: knob, value: "28 (subtle) / 84 (thick)" }
  - { name: "CWO feedback", type: knob, value: "15 (subtle) / 65 (thick)" }
  - { name: "CWO sideband", type: knob, value: "doesn't matter much (subtle) / 4 (thick)" }
  - { name: "LFO", type: switch, value: "value", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Value LFO speed", type: knob, value: "3 clicks right" }
  - { name: "Value LFO amount", type: knob, value: "5" }
  - { name: "Value LFO dest", type: switch, value: "FX" }
  - { name: "Value LFO P.Dest", type: switch, value: "green (CWO delay param)" }
---

# CWO — Value-LFO modulated chorus (published values)

## Concept

CWO is the OP-1's Echobode-style overtone-shifting delay. Drive a slow **value LFO** at its delay knob and the echo collapses into a lush, slightly-detuned chorus instead of a repeat. This is a value-exact recipe with two documented parameter sets: a **subtle** chorus (freq 0 / delay 28 / feedback 15) and a **thick, out-of-tune** chorus (freq ~20% / delay 84 / feedback 65 / sideband 4 — "you want the echoes slightly out of tune"). Distinct from the static `cwo-chorus-lush-stereo` patch, which carries no LFO modulation.

## How to play it

1. Load **CWO**: freq **0**, delay **28**, feedback **15** (sideband doesn't matter much here).
2. Add a **value LFO**: speed **3 clicks right**, amount **5**, Dest = **FX**, P.Dest = **green** (the CWO delay param).
3. The LFO wobbles delay time for a slow chorus shimmer.
4. For a heavier detuned chorus, switch CWO to freq **~20%** / delay **84** / feedback **65** / sideband **4**.

## Notes

- CWO is the OP-1's Echobode-style overtone-shifting delay — modulating its delay yields chorus rather than echo.
- Both parameter sets are documented community recipes (op1tips), so values are sourced, not dialed by ear. Routing the value LFO to FX/green is what targets the CWO delay param.
- The "thick" set is explicitly meant to sit slightly out of tune; nudge feedback down if it gets washy.

## Sources

- github.com/ratbag98/op1tips (Value-LFO chorus: CWO freq 0 / delay 28 / feedback 15, LFO speed 3 right / amount 5 / Dest FX / P.Dest green; thick chorus CWO 20% / 84 / 65 / 4)
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
