---
type: patch
title: Acoustic-Top / Dirty-Rock-Bottom Split
device: Roland VG-800
date: 2026-06-14
description: One-instrument-sounds-like-two — clean acoustic high strings + overdriven low strings; the "recorded-wrong"/unexpected-source aesthetic ("Ultimate Split"/"Metal Acoustic" family).
tags: [dual-guitar, string-split, acoustic, overdrive, factory, signature]
controls:
  - { name: "INST TYPE", type: switch, value: "DUAL GUITAR (split by string group)" }
  - { name: "Channel A (high 3 strings)", type: switch, value: "ACOUSTIC model (clean)" }
  - { name: "Channel B (low 3 strings)", type: switch, value: "E.GUITAR model into a dirty AMP (DS on)" }
  - { name: "DIV MODE", type: switch, value: "DUAL (each group gets its own amp+FX)", options: ["SINGLE", "DUAL"] }
  - { name: "AB BALANCE", type: knob, value: "to taste (centered = 50)" }
  - { name: "ACOUSTIC RESONANCE", type: switch, value: "OFF (it collapses stereo and kills AB/per-string PAN)", options: ["ON", "OFF"] }
  - { name: "CTL-1", type: button, value: "rig change" }
  - { name: "Slot/Bank", type: knob, value: "Factory split bank (\"Ultimate Split\"), or User Memory" }
---

# Acoustic-Top / Dirty-Rock-Bottom Split

## Concept

One instrument that sounds like two — clean acoustic high strings plus overdriven low strings; the "recorded-wrong"/unexpected-source aesthetic. The "Ultimate Split"/"Metal Acoustic" family. Official BOSS verbatim: "clean acoustic guitar on the top three strings and an overdriven rock guitar on the bottom three strings." `DIV MODE = DUAL` gives each string group its own amp + FX.

## How to play it

1. Set `INST TYPE = DUAL GUITAR`, split by string group.
2. High 3 strings = `ACOUSTIC` model (clean); low 3 strings = `E.GUITAR` model into a dirty `AMP` (channel B / `DS` on).
3. `DIV MODE = DUAL` so each group gets its own amp + FX.
4. `AB BALANCE` to taste (centered = 50).
5. Assign CTL-1 = rig change.
6. ⚠ Keep `ACOUSTIC RESONANCE` off — it collapses stereo and kills the AB/per-string PAN.

## Notes

- String-group model assignment is officially documented (BOSS).
- Factory variants named by Juca: "Ultimate Split," "Metal Acoustic" (acoustic-model-driven heavy — "surprisingly heavy"), "Pickup Splitter."

## Sources

- 🟢 official BOSS `research/links/boss-article-vguitar-advanced-features.md` (https://articles.boss.info/exploring-the-advanced-features-of-the-boss-v-guitar-system/); factory names from Juca Nery transcript
- Transformed from Pedalxly VG-800-Patches.md (factory)
