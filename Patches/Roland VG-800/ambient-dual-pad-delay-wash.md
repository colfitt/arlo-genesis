---
type: patch
title: "Cinematic Dual Pad + Delay Wash"
device: Roland VG-800
date: 2026-06-15
description: "Clean guitar layered with a synth pad across the strings (DUAL mode), buried in stereo delay and a long reverb for dreamy, cinematic ambient textures — a use Boss and reviewers explicitly highlight for the VG-800. Distinct from the rig's clean/fuzz string-split: this is clean guitar PLUS a synth pad. Factory-feature recipe with manual-verified pad params; mix/level values are not published, so dial from the recipe."
tags: [ambient, pad, dual-guitar, delay, reverb, cinematic, synth]
dips:
  AB BALANCE: "centered"
  ACOUSTIC RESONANCE: "OFF (keeps it from collapsing the stereo image)"
  OUTPUT SELECT: "LINE/PHONES"
  EXP: "ride EXP on FV2 (or REV/DLY mix) for live swells"
controls:
  - { name: "DIV MODE", type: switch, value: "DUAL", options: ["SINGLE", "DUAL"] }
  - { name: "Voice A", type: switch, value: "clean E.GUITAR model" }
  - { name: "Voice B (SYNTH)", type: switch, value: "SYNTH pad — SOLO or CRYSTAL", options: ["SOLO", "CRYSTAL"] }
  - { name: "SUSTAIN", type: knob, value: "high (long pad hold) — dial from recipe; no published value" }
  - { name: "SWEEP", type: knob, value: "slow filter sweep on the pad — dial from recipe; no published value" }
  - { name: "RISE TIME", type: knob, value: "soft attack so the pad fades in — dial from recipe; no published value" }
  - { name: "FALL TIME", type: knob, value: "long release tail — dial from recipe; no published value" }
  - { name: "Stereo Delay", type: knob, value: "stereo delay across the patch — mix dialed from recipe; no published value" }
  - { name: "Reverb", type: knob, value: "long reverb across the patch (or send to Microcosm / Big Sky) — mix dialed from recipe; no published value" }
  - { name: "Phaser", type: switch, value: "optional slow phaser for movement", options: ["ON", "OFF"] }
  - { name: "AB BALANCE", type: knob, value: "50 (centered)" }
  - { name: "ACOUSTIC RESONANCE", type: switch, value: "OFF (silently collapses the stereo image)", options: ["ON", "OFF"] }
  - { name: "OUTPUT SELECT", type: switch, value: "LINE/PHONES", options: ["LINE/PHONES", "GUITAR AMP"] }
---

# Cinematic Dual Pad + Delay Wash

## Concept

Layer a clean guitar with a synth pad across the strings using `DIV MODE = DUAL`, then bury the pair in stereo delay and a long reverb for dreamy, cinematic ambient textures — the "blending clean guitar with synth pads and delays" use Boss and reviewers explicitly call out for the VG-800. Voice A is a clean `E.GUITAR` model; Voice B is a `SYNTH` pad (SOLO/CRYSTAL) with high `SUSTAIN`, a slow `SWEEP` filter, and a soft `RISE TIME` / `FALL TIME` envelope so the pad blooms in and decays slowly. This is distinct from the rig's Dual Stereo Split (clean-low / fuzz-high string split): here it's clean guitar **plus** a synth pad, not two guitar voices.

## How to play it

1. Enable `DIV MODE = DUAL`; set Voice A to a clean `E.GUITAR` model.
2. Set Voice B to a `SYNTH` pad (SOLO or CRYSTAL) with high `SUSTAIN`, a slow `SWEEP` filter, and a soft `RISE TIME` / `FALL TIME` envelope.
3. Add a stereo delay and a long reverb across the whole patch (or send out to Microcosm / Big Sky).
4. Optionally drop a slow phaser into an FX slot for movement.
5. Play sustained chords and let the wash bloom; ride an EXP pedal on `FV2` (or the REV/DLY mix) for live swells.
6. Keep `AB BALANCE` centered and `ACOUSTIC RESONANCE = OFF` so the stereo image holds; `OUTPUT SELECT = LINE/PHONES`.

## Notes

- Boss / SonicState and reviewers cite "dreamy textures blending clean guitar with synth pads and delays" as an ideal VG-800 use. `DUAL` mode A/B and the `SYNTH` pad params (`SUSTAIN`, `SWEEP`, `RISE TIME` / `FALL TIME`) are repo-verified; the specific pad voice choice (SOLO vs CRYSTAL) is your design call.
- Distinct from Dual Stereo Split (clean-low / fuzz-high string split) — this layers a clean guitar with a synth pad rather than splitting two guitar voices.
- ⚠ Recipe, not capture: exact mix/level values (pad `SUSTAIN` / `SWEEP` / `RISE`/`FALL`, delay and reverb mix) are not published — the values above are dialable starting points, not sourced settings. Map an EXP pedal to the REV/DLY mix (or `FV2`) for live swells.
- ⚠ Keep `ACOUSTIC RESONANCE` off — it silently collapses the stereo image you're building here (same gotcha as the Dual Stereo Split patch).

## Sources

- 🟢 https://articles.boss.info/exploring-the-advanced-features-of-the-boss-v-guitar-system/ (clean guitar + synth pads + delays as an ideal use)
- 🟢 https://www.boss.info/global/products/vg-800/ (pad synths: filter sweeps + envelope shaping)
- 🟢 `research/links/parameter-guide-synth-engine-values.md` (SOLO/CRYSTAL SUSTAIN, SWEEP, envelope params)
- 🟢 `research/transcripts/gear-sounds-full-tutorial.md` (DIV two-path DUAL architecture; stereo)
