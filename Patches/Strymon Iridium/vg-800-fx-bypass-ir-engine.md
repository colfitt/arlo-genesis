---
type: patch
title: VG-800 FX-Bypass → IR Engine
device: Strymon Iridium
date: 2026-06-14
description: Cab the VG-800's raw INST model with Strymon's premium IRs instead of the weak Boss cab — Amp-Bypass mode turns the Iridium into the IR engine so the banjo can ride Strymon IRs.
tags: [integration, convolution, amp-bypass, vg-800, designed, signature]
hidden:
  Output Mode (global power-up): Amp Bypass (ON LED GREEN — amp model OFF, CAB + ROOM only; set via HOLD-ON at power-up + DRIVE)
  VG-800 — FX BYPASS: [▲]+[CTL 1] (hear only the raw INST model, no Boss cab)
  VG-800 — OUTPUT SELECT: LINE/PHONES
controls:
  - { name: "Cab", type: switch, value: "a clean balanced slot (factory or a York/Celestion custom IR)", options: ["a", "b", "c"] }
  - { name: "Drive", type: knob, value: "inactive (amp bypassed — IR engine only convolves)" }
  - { name: "Bass", type: knob, value: "inactive (amp bypassed)" }
  - { name: "Middle", type: knob, value: "inactive (amp bypassed)" }
  - { name: "Treble", type: knob, value: "inactive (amp bypassed)" }
  - { name: "Level", type: knob, value: "to Apollo unity" }
  - { name: "Room", type: knob, value: "~10:00 (SIZE medium)" }
  - { name: "Input Level", type: switch, value: "Line (VG-800 line out is hot and WILL clip Instrument)", options: ["Instrument", "Line"] }
  - { name: "Output Mode", type: switch, value: "Amp Bypass (ON LED GREEN)", options: ["Normal", "Amp Bypass", "Cab Bypass"] }
  - { name: "Rear Input Selector", type: switch, value: "MONO or STEREO per the VG-800 out", options: ["MONO", "STEREO", "SUM"] }
  - { name: "Slot/Bank", type: knob, value: "FAV stores CAB/ROOM/LEVEL; Amp-Bypass mode is a global power-up setting (not per-preset)" }
---

# VG-800 FX-Bypass → IR Engine

## Concept
The one non-redundant VG-800 + Iridium pairing — cab the VG-800's raw INST model with Strymon's premium IRs instead of the Boss cab (the VG-800's weak link), letting the banjo-as-lead ride Strymon IRs. The VG-800 runs FX BYPASS so you hear only the raw INST model with no Boss cab; the Iridium runs Amp Bypass (CAB + ROOM only) as a pure IR engine.

## How to play it
1. ON VG-800: `[▲]+[CTL 1]` = FX BYPASS (hear only the raw INST model, no Boss cab); OUTPUT SELECT = LINE/PHONES.
2. ON IRIDIUM: OUTPUT MODE = Amp Bypass (ON LED GREEN — amp model OFF, CAB + ROOM only; set via HOLD-ON at power-up + DRIVE).
3. CAB = a clean balanced slot (factory or a York/Celestion custom IR); LEVEL to Apollo unity; ROOM ~10:00, SIZE medium.
4. DRIVE/BASS/MIDDLE/TREBLE inactive (amp bypassed — IR engine only convolves).
5. CRITICAL switch: INPUT LEVEL = Line (the VG-800 line out is hot and WILL clip the Instrument input; the bench EHX Effects Interface reconciles level if it still clips); rear = MONO or STEREO per the VG-800 out.

## Notes
- DESIGNED patch.
- The only sane way to combine the two boxes — never stack two cab sims.
- INPUT LEVEL = Line is mandatory or it clips.
- The Amp-Bypass output mode is a global power-up setting, not per-preset — set it once at power-up; the FAV/slot only stores CAB/ROOM/LEVEL.

## Sources
- designed from the output-mode + integration docs — research/links/stack-placement-output-modes.md; research/links/ir-impulse-manager-and-output-modes.md; Iridium-DeepResearch.md §9 + the VG-800 dossier.
- Transformed from Pedalxly Iridium-Patches.md (designed)
