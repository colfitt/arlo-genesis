---
type: patch
title: Sidechain-Pump Bus (LFO-ramp duck)
device: Elektron Digitakt 2
date: 2026-06-14
description: Fake the four-on-the-floor sidechain pump so a loop/bass/pad breathes with the kick (the DT2 has no true sidechain key). Designed-to-emulate.
tags: [sidechain, pump, filter-house, four-on-the-floor, designed, signature]
controls:
  - { name: "LFO DEST", type: switch, value: "track LEVEL (AMP volume)" }
  - { name: "LFO WAVE", type: switch, value: "RAMP (saw that snaps down on the beat then rises)" }
  - { name: "LFO MULT", type: knob, value: "synced so one LFO cycle = one beat (1/4)" }
  - { name: "LFO DEP", type: knob, value: "high (deep duck)" }
  - { name: "LFO MODE", type: switch, value: "TRIG (retriggered on the downbeat)", options: ["FREE","TRIG","HOLD","ONE","HALF"] }
  - { name: "Kick placement", type: switch, value: "on the same step the ramp resets" }
---

# Sidechain-Pump Bus (LFO-ramp duck)

## Concept
Fakes the four-on-the-floor sidechain pump so a loop/bass/pad breathes with the kick — the DT2 has no true sidechain key. A RAMP LFO on the track LEVEL (a saw that snaps down on the beat then rises), synced so one cycle equals one beat, deep depth, retriggered on the downbeat, with the kick placed on the step where the ramp resets.

## How to play it
1. On the track that should breathe: LFO → track LEVEL (AMP volume), WAVE = RAMP (saw that snaps down on the beat then rises), MULT synced so one LFO cycle = one beat (1/4), DEP high (deep duck), MODE = TRIG retriggered on the downbeat.
2. Put the kick on the same step the ramp resets.
3. House pump targets: deep, fast attack, recover before the next beat.

## Notes
- DT2-E2. APPROXIMATION: an LFO-ramp on volume fakes sidechain — no true key input on the DT2. Flagged.
- Designed-to-emulate — not a found preset. Pairs with a four-on-the-floor kick track.

## Sources
- Ref: Filter-house / LCD four-on-the-floor pump (kick ducks the loop)
- `Research/Taste-Profile/sources/sidechain-pump-settings-house-techno.md`
- `splice-filter-house-techniques.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (designed)
