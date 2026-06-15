---
type: patch
title: "Poly Slow-Gear Swell Pad — roll-your-own attackless swell"
device: Roland VG-800
date: 2026-06-15
description: "A do-it-yourself polyphonic slow-gear/auto-swell built from the synth engine's RISE TIME / FALL TIME envelope params (there's no dedicated poly-slow-gear block) — removes the attack on every note so chords bloom in. The attackless drone-machine source the rig wants, generated cleanly inside the box. Power-user technique from VGuitarForums (jwhitcomb3): \"could craft your own poly slow gear\" from RISE/FALL TIME; the standard mono-trigger SLOW GEAR FX is also available for single-note swells."
tags: [drone, ambient, swell, synth, slow-gear, designed, textural]
dips:
  OUTPUT SELECT: "LINE/PHONES"
  ONBOARD REV/DLY: "OFF (let the End Board smear)"
  EXP ALT: "assign EXP pedal to FV1 for manual swells"
controls:
  - { name: "INST TYPE", type: switch, value: "SYNTH" }
  - { name: "RISE TIME", type: knob, value: "dial from recipe — raise so each note fades in (poly slow gear); no published value" }
  - { name: "FALL TIME", type: knob, value: "dial from recipe — sets the release/decay tail; no published value" }
  - { name: "SLOW GEAR (FX slot)", type: switch, value: "ON for a per-note (mono-trigger) volume swell — alternative to the RISE/FALL build", options: ["ON", "OFF"] }
  - { name: "EXP / FV1", type: knob, value: "optional — assign EXP pedal to FV1 for manual hand-played swells" }
  - { name: "OUTPUT SELECT", type: switch, value: "LINE/PHONES", options: ["LINE/PHONES", "GUITAR AMP"] }
---

# Poly Slow-Gear Swell Pad — roll-your-own attackless swell

## Concept

A do-it-yourself polyphonic slow-gear/auto-swell built from the synth engine's `RISE TIME` / `FALL TIME` envelope params — because there is no dedicated poly-slow-gear block on the VG-800. Raising `RISE TIME` removes the attack on every note so chords bloom in attackless; `FALL TIME` shapes the release tail. This is the attackless drone-machine source the rig wants, generated cleanly inside the box. The standard mono-trigger `SLOW GEAR` FX is also available in an FX slot for single-note swells.

## How to play it

1. Set `INST TYPE = SYNTH` and raise `RISE TIME` so each note fades in (the poly slow-gear effect), with `FALL TIME` for the release tail.
2. Or drop a `SLOW GEAR` effect into an FX slot for a per-note (mono-trigger) volume swell.
3. Hold chords; they bloom in attackless for a pad.
4. Into Dark Star V3 / QI Etherealizer the attackless swell becomes an infinite drone — double the swell with the instrument's volume knob.
5. Optional: assign an EXP pedal to `FV1` for manual, hand-played swells.

## Notes

- Documented power-user technique: "Int pedal replaced by RISE TIME / FALL TIME parameters… could craft your own poly slow gear" (VGuitarForums, jwhitcomb3). `SLOW GEAR` is confirmed available as an FX (Gear Sounds; BOSS article).
- ⚠ Honesty caveat (forum-confirmed): there is NO dedicated polyphonic slow-gear block — only the standard mono-trigger Slow Gear effect. The poly version must be built from `RISE TIME` / `FALL TIME` envelopes.
- ⚠ Recipe, not capture: exact `RISE TIME` / `FALL TIME` values are not published — dial by ear. The values above are dialable starting points, not sourced settings.
- Related to the existing VIO Bowed Swell Drone, but uses the synth-envelope method on any synth voice.

## Sources

- 🟣 `research/links/vguitarforums-vg800-main-thread.md` (RISE TIME / FALL TIME = roll-your-own poly slow gear)
- 🟢 `research/transcripts/gear-sounds-full-tutorial.md` (SLOW GEAR available as an effect)
- 🟢 `research/links/boss-article-vguitar-advanced-features.md` (Slow Gear named officially)
- 🟣 https://www.vguitarforums.com/smf/index.php?topic=38100.125 (poly slow gear omitted; only standard Slow Gear effect)
