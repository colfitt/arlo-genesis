---
type: patch
title: Banjo → ALT TUNE Harmony Drone
device: Roland VG-800
date: 2026-06-14
description: A self-harmonizing banjo lead/drone — banjo plus a fixed diatonic harmony voice, into the smear/fuzz for thickness without a second instrument.
tags: [drone, banjo, harmony, alt-tuning, designed, signature]
controls:
  - { name: "INST TYPE", type: switch, value: "E.GUITAR (or VIO for attackless)" }
  - { name: "ALT TUNE SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "ALT TUNE MODE", type: switch, value: "HARMONY", options: ["ALT TUNE", "HARMONY"] }
  - { name: "HARMONY", type: knob, value: "+1oct or a USER SCALE diatonic interval" }
  - { name: "KEY", type: knob, value: "set to the tune's key (for USER SCALE)" }
  - { name: "NORMAL MIX", type: knob, value: "~30% (keep the dry banjo under the harmony)" }
  - { name: "SUSTAIN / SLOW GEAR", type: switch, value: "optional (for drone)" }
  - { name: "Slot/Bank", type: knob, value: "User Memory (guitar mode), e.g. U06-1" }
---

# Banjo → ALT TUNE Harmony Drone

## Concept

A self-harmonizing banjo lead/drone — the banjo plus a fixed diatonic harmony voice, into the smear/fuzz for thickness without a second instrument. `ALT TUNE MODE = HARMONY` with a `+1oct` or `USER SCALE` diatonic interval adds a Bon-Iver-/Sufjan-style vocal-halo thickness to a banjo lead.

## How to play it

1. Recall the EBM5 BANJO GK profile.
2. Set `INST = E.GUITAR` (or VIO for attackless).
3. `ALT TUNE SW = ON`, `ALT TUNE MODE = HARMONY`, `HARMONY = +1oct` or a `USER SCALE` diatonic interval (set `KEY` to the tune's key).
4. `NORMAL MIX ~30%` to keep the dry banjo under the harmony.
5. Optional `SUSTAIN`/`SLOW GEAR` for a drone.
6. Into Hizumitas → smear reverb.

## Notes

- Designed; `HARMONY` mode + `USER SCALE` are manual-verified.
- Verify the harmony tracks cleanly on the banjo by ear.

## Sources

- 🟣 designed from UsageGuide §3 + HARMONY block in `research/links/parameter-guide-alt-tuning-values.md`
- Transformed from Pedalxly VG-800-Patches.md (DOUG-designed)
