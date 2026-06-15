---
type: patch
title: "Tremolo auto-pan stereo double (+40/-40)"
device: TE OP-1 Field
date: 2026-06-15
description: "Turn a mono source into a wide, motion-rich stereo pair using the Tremolo LFO as an auto-panner — record it twice with the white-knob amount negated on the second pass, then hard-pan the two passes L/R for an opposing-phase, animated stereo double. Rig-native width for the mono banjo/baritone. Community recipe (ratbag98/op1tips) with white ~±40 + green 0 documented; rate to-taste."
tags: [width, stereo, tape-trick, sampler, panning]
dips:
  TRACK_LR_FADERS: "on the track-levels screen, hold [Shift] for per-track L/R faders to pan each take precisely"
controls:
  - { name: "Engine", type: switch, value: "Drum sampler (lift the mono sound in)" }
  - { name: "LFO", type: switch, value: "Tremolo", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Tremolo rate", type: knob, value: "= pan speed (to taste)" }
  - { name: "Tremolo green", type: knob, value: "0" }
  - { name: "Tremolo white (pass 1)", type: knob, value: "~+40" }
  - { name: "Tremolo white (pass 2)", type: knob, value: "~-40 (negated)" }
  - { name: "Pass 1 pan", type: knob, value: "hard LEFT ([Shift] on track levels = L/R faders)" }
  - { name: "Pass 2 pan", type: knob, value: "hard RIGHT ([Shift] on track levels = L/R faders)" }
---

# Tremolo auto-pan stereo double (+40/-40)

## Concept

Turn a mono source into a wide, motion-rich stereo pair using the **Tremolo LFO as an auto-panner**: record it twice with the white-knob amount negated on the second pass, then hard-pan the two passes L/R for an opposing-phase, animated stereo double. The +40/-40 flip is what creates the opposing-phase movement that widens the image. Rig-native width for the mono banjo/baritone — an alternative to the dry `[Shift]`+Orange pan double, but this one adds motion.

## How to play it

1. Lift the mono sound and drop it into the **drum sampler**.
2. Set a **Tremolo LFO**: rate = your speed, **green 0**, **white ~40**; record **pass 1**.
3. Negate the white knob (**~-40**) and record a **second pass**.
4. Hard-pan one pass **left** and the other **right** (`[Shift]` on the track-levels screen reveals a per-track L/R fader).
5. Two mono takes now read as a wide, opposing-phase auto-panned double.

## Notes

- Documented community recipe (ratbag98) with white **~±40** / **green 0** values; **rate is to-taste**, not a published number — dial the pan speed by ear.
- The +40/-40 flip creates the opposing-phase movement that widens the image.
- Alternative to the dry `[Shift]`+Orange pan double — this one adds motion.

## Sources

- Gear/TE OP-1 Field/research/links/github-ratbag98-op1tips-distilled.md (§Tremolo auto-pan double)
- github.com/ratbag98/op1tips (Tremolo LFO pan: green 0 / white 40 then -40, hard-pan L/R; Shift on track levels = L/R faders)
