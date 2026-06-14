---
type: patch
title: GK SETTING — EBM5 BANJO
device: Roland VG-800
date: 2026-06-14
description: GK-5 calibration profile for the Gold Tone EBM-5 electric banjo — the rig's banjo-as-lead source; recall this before any banjo patch (the enabler nothing else works without).
tags: [calibration, banjo, gk-setting, enabler, designed, signature]
controls:
  - { name: "GK TYPE", type: switch, value: "GK-5", options: ["GK-5", "GK-3", "GK-2A", "13-pin"] }
  - { name: "SCALE", type: switch, value: "ST (648 mm) baseline (audition ST vs LP 628)" }
  - { name: "PU DIRECTION", type: switch, value: "NORMAL or REVERSE (match physical mount)", options: ["NORMAL", "REVERSE"] }
  - { name: "DISTANCE 1–6", type: knob, value: "~12–14 mm (raise per string if it splats)" }
  - { name: "SENS (per-string)", type: knob, value: "start ~35–40, tune individually to on-screen bar ≈75% on a normal pick (thin/high strings UP, fat/low strings DOWN)" }
  - { name: "SENS 5 (5th string)", type: knob, value: "~55–65 (its own low value; short hot high-G)" }
  - { name: "GLOBAL GAIN", type: knob, value: "2 (lower if picking distorts)" }
  - { name: "STRING MUTE 5", type: switch, value: "ON if 5th won't behave (or STRING LEVEL 5 = 0)" }
  - { name: "NORMAL MIX", type: knob, value: "~20–40% (keep the real 5th drone)" }
  - { name: "PLAY FEEL", type: switch, value: "FEEL3–4 (or NO DYNA)" }
  - { name: "LOW VELO CUT", type: knob, value: "2–4" }
  - { name: "HOLD", type: switch, value: "HOLD1" }
  - { name: "GK SET SELECT", type: knob, value: "slot 1 (of 10)" }
---

# GK SETTING — EBM5 BANJO

## Concept

A GK-5 calibration profile for the Gold Tone EBM-5 electric banjo — the rig's banjo-as-lead source. GK tracking on a banjo is off-label: the 4 main strings track for leads; the 5th string usually won't track cleanly. This profile is the signature banjo-as-lead enabler — nothing else in the rig works until this tracks. Stored separately (GK SETTING profiles, up to 10) and recalled per-instrument; persists power-off.

## How to play it

1. `MENU → GK SETTING`, NAME `EBM5 BANJO`. Set `GK TYPE = GK-5`.
2. Mount the GK-5 at ~1 mm string clearance, dead level.
3. Set `SCALE = ST (648 mm)` as a baseline (there is no banjo preset — audition ST vs LP 628).
4. Match `PU DIRECTION` to the physical mount (NORMAL/REVERSE).
5. Set `DISTANCE 1–6 = ~12–14 mm`; raise per string if a string splats.
6. Per-string `SENS`: default 65 is too hot. Start ~35–40 and tune each string individually so the on-screen bar reads ≈75% on a normal pick — thin/high strings UP, fat/low strings DOWN.
7. `GLOBAL GAIN = 2` (lower if picking distorts).
8. 5th string (short hot high-G): give it its own low `SENS ~55–65`. If it won't behave, `STRING MUTE 5` or `STRING LEVEL 5 = 0` and keep the real 5th via `NORMAL MIX ~20–40%`.
9. MIDI side: `PLAY FEEL = FEEL3–4` (or `NO DYNA`), `LOW VELO CUT = 2–4`, `HOLD = HOLD1`.
10. Save to `GK SET SELECT` slot 1 (of 10).

## Notes

- Hybrid provenance — param names/ranges are manual-verified; the SENS method (default-too-hot → bar-to-75%, thin-up/fat-down) is community-cited from the GM-800 GK-5 thread (same Serial-GK platform). Banjo values + 5th-string strategy are inference — verify by ear.
- THE signature banjo-as-lead enabler. Recall this slot before any banjo patch.

## Sources

- designed from `research/calibration-banjo-EBM5.md` + `research/links/vguitarforums-gk5-tracking-calibration.md` (https://www.vguitarforums.com/smf/index.php?topic=36028.0); UsageGuide §2
- Transformed from Pedalxly VG-800-Patches.md (DOUG-designed)
