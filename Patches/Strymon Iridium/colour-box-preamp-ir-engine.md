---
type: patch
title: Colour Box Preamp → IR Engine
device: Strymon Iridium
date: 2026-06-14
description: A degraded "recorded-wrong" console-overload DI — the JHS Colour Box V2 does the lo-fi preamp crunch, the Iridium (Amp Bypass) just convolves a cab IR + room so it sits like a mic'd amp.
tags: [lo-fi, integration, convolution, amp-bypass, preamp, designed, signature]
hidden:
  Output Mode (global power-up): Amp Bypass (ON LED GREEN — amp model off, CAB + ROOM only)
controls:
  - { name: "Cab", type: switch, value: "a guitar cab IR that fits the source (York/Celestion clean, or a dark 4×12 for crushed console tones)", options: ["a", "b", "c"] }
  - { name: "Drive", type: knob, value: "inactive (amp bypassed)" }
  - { name: "Bass", type: knob, value: "inactive (amp bypassed)" }
  - { name: "Middle", type: knob, value: "inactive (amp bypassed)" }
  - { name: "Treble", type: knob, value: "inactive (amp bypassed)" }
  - { name: "Level", type: knob, value: "to interface unity" }
  - { name: "Room", type: knob, value: "~10:00 (SIZE small/medium)" }
  - { name: "Input Level", type: switch, value: "Line if the Colour Box output is hot (it often is) — else it clips", options: ["Instrument", "Line"] }
  - { name: "Output Mode", type: switch, value: "Amp Bypass (ON LED GREEN)", options: ["Normal", "Amp Bypass", "Cab Bypass"] }
  - { name: "Rear Input Selector", type: switch, value: "MONO/STEREO", options: ["MONO", "STEREO", "SUM"] }
  - { name: "Slot/Bank", type: knob, value: "FAV stores CAB/ROOM/LEVEL; Amp-Bypass mode is a global power-up setting" }
---

# Colour Box Preamp → IR Engine

## Concept
A degraded / "recorded-wrong" console-overload DI — the JHS Colour Box V2 (or any preamp/dirt, Riverside-style) does the lo-fi preamp crunch (the lo-fi cluster's signature), and the Iridium adds a real cab IR + room so it sits like a mic'd amp. Amp Bypass turns the Iridium into a standalone IR loader so any dirt box becomes amp-in-a-box.

## How to play it
1. CHAIN: Colour Box V2 (its own preamp/EQ/dirt) → Iridium IN.
2. ON IRIDIUM: OUTPUT MODE = Amp Bypass (ON LED GREEN — amp model off, CAB + ROOM only).
3. CAB = a guitar cab IR that fits the source (York/Celestion clean, or a dark 4×12 for crushed console tones); LEVEL to interface unity; ROOM ~10:00, SIZE small/medium.
4. DRIVE/tone-stack inactive (amp bypassed).
5. INPUT LEVEL = Line if the Colour Box output is hot (it often is) — else it clips; rear = MONO/STEREO.

## Notes
- DESIGNED patch.
- Watch INPUT LEVEL — a hot Colour Box wants Line.
- The Amp-Bypass mode is a global power-up setting; the FAV stores only CAB/ROOM/LEVEL.

## Sources
- designed from the Amp-Bypass external-preamp recipe — research/links/stack-placement-output-modes.md; research/links/customir-impulse-manager-workflow.md. No artist dial.
- Transformed from Pedalxly Iridium-Patches.md (designed)
