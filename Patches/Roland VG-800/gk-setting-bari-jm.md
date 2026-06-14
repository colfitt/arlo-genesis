---
type: patch
title: GK SETTING — BARI JM
device: Roland VG-800
date: 2026-06-14
description: GK-5 calibration profile for the Baritone Jazzmaster — the rig's low-weight / doom source; recall before any baritone patch.
tags: [calibration, baritone, doom, gk-setting, enabler, designed, signature]
controls:
  - { name: "GK TYPE", type: switch, value: "GK-5", options: ["GK-5", "GK-3", "GK-2A", "13-pin"] }
  - { name: "SCALE", type: switch, value: "LP (628 mm) or longest preset (baritone 27–30\")" }
  - { name: "DISTANCE (highs)", type: knob, value: "~12 mm" }
  - { name: "DISTANCE (lows)", type: knob, value: "15–18 mm (back the element off for big slow excursions)" }
  - { name: "SENS (highs)", type: knob, value: "~75–80" }
  - { name: "SENS (lows)", type: knob, value: "~60–70 (lower)" }
  - { name: "GLOBAL GAIN", type: knob, value: "2–3" }
  - { name: "NORMAL MIX", type: knob, value: "~30%" }
  - { name: "GK SET SELECT", type: knob, value: "slot 2 (of 10)" }
---

# GK SETTING — BARI JM

## Concept

A GK-5 calibration profile for the Baritone Jazzmaster — the rig's low-weight / doom source. The documented MusicRadar issue is low-string wobble; this profile backs the element off the low strings and lowers their sensitivity to tame it. Calibrate at the PLAYED tuning, not the shifted one. Recall before any baritone patch.

## How to play it

1. `MENU → GK SETTING`, NAME `BARI JM`. Set `GK TYPE = GK-5`.
2. `SCALE = LP (628 mm)` or the longest preset (baritone 27–30" — a longer SCALE expectation reduces low-string pitch confusion).
3. `DISTANCE` ~12 mm on highs; raise to 15–18 mm on the LOW strings (big slow excursions need the element backed off).
4. Per-string `SENS`: highs ~75–80, lows LOWER ~60–70.
5. `GLOBAL GAIN = 2–3`.
6. Low-string wobble fix order (the documented MusicRadar issue): (1) lower `SENS` on the offending string in steps of 5, (2) raise its `DISTANCE`, (3) lower `GAIN` globally, (4) `SCALE` up a preset, (5) pick nearer the bridge.
7. Companion `NORMAL MIX ~30%`.
8. Save to `GK SET SELECT` slot 2 (of 10).

## Notes

- Hybrid — the low-string-wobble fix order is MusicRadar-documented; baritone numbers are inference (verify by ear).
- Extreme `-STEP` tunings stack two pitch-shifts → more artifacts, which is a *feature* into the Hizumitas wall.
- Calibrate at the PLAYED tuning, not the shifted one.

## Sources

- designed from `research/calibration-baritone-JM.md` + `research/links/vguitarforums-gk5-tracking-calibration.md`; MusicRadar (https://www.musicradar.com/guitars/guitar-pedals/boss-vg-800-v-guitar-processor-review); UsageGuide §2
- Transformed from Pedalxly VG-800-Patches.md (DOUG-designed)
