---
type: patch
title: Banjo Halo Harmony Drone
device: Roland VG-800
date: 2026-06-14
description: The rig's nearest analogue to the Prismizer's PLAYED harmony (Bon Iver / Sufjan) — a banjo lead with a fixed diatonic harmony voice stacked on it.
tags: [drone, banjo, harmony, indie-folk, prismizer, designed, signature]
controls:
  - { name: "INST TYPE", type: switch, value: "E.GUITAR (or VIO for attackless)" }
  - { name: "ALT TUNE SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "ALT TUNE MODE", type: switch, value: "HARMONY", options: ["ALT TUNE", "HARMONY"] }
  - { name: "HARMONY", type: knob, value: "+1 oct OR a USER SCALE diatonic 3rd/5th" }
  - { name: "KEY", type: knob, value: "set to the tune's key (for USER SCALE)" }
  - { name: "NORMAL MIX", type: knob, value: "~30% (keep the dry banjo under the harmony)" }
  - { name: "SUSTAIN / SLOW GEAR", type: switch, value: "optional (for a drone entry)" }
  - { name: "Slot/Bank", type: knob, value: "User Memory (guitar mode), e.g. U06-2" }
---

# Banjo Halo Harmony Drone

## Concept

The rig's nearest analogue to the Prismizer's PLAYED harmony — a banjo lead with a fixed diatonic harmony voice stacked on it (Bon Iver Prismizer played-harmony halo / Sufjan layered-harmony "echoes of the past"). A 🟣 designed-to-emulate build, not a documented factory patch. Builds on the "Banjo → ALT TUNE Harmony Drone" patch.

## How to play it

1. Recall GK SETTING slot 1 (EBM5 BANJO).
2. Set `INST = E.GUITAR` (or `VIO` for attackless).
3. `ALT TUNE SW = ON`, `ALT TUNE MODE = HARMONY`, `HARMONY = +1 oct` OR a `USER SCALE` diatonic 3rd/5th (set `KEY` to the tune's key).
4. `NORMAL MIX ~30%` to keep the dry banjo under the harmony.
5. Optional `SUSTAIN`/`SLOW GEAR` for a drone entry.
6. Onboard REV/DLY off.

## Notes

- 🟣⭐ APPROXIMATION FLAG: this is ONE fixed interval, NOT the 4-note MIDI-played formant-shifted cloud — layer QI Prismizer-Halo downstream for the cloud, this for the played voice.
- Builds on the existing "Banjo → ALT TUNE Harmony Drone" patch.

## Sources

- 🟣 designed; `Research/Taste-Profile/sources/prismizer-harmony-engine-recipe.md`; `Research/Taste-Profile/sources/sufjan-carrie-lowell-iphone-bartlett-intimate.md`
- Ref: Bon Iver Prismizer played-harmony halo / Sufjan layered-harmony "echoes of the past"
- Transformed from Pedalxly VG-800-Patches.md (DOUG-designed)
