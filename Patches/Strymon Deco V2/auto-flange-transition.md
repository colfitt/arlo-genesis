---
type: patch
title: Auto-Flange Transition
device: Strymon Deco V2
date: 2026-06-14
description: A one-shot studio-style through-zero flange WHOOSH to mark a section change — works even with the doubletracker bypassed (grab just the flange for transitions). Strymon Auto-Flange feature.
tags: [flange, transition, one-shot, performance, factory]
hidden:
  Auto-Flange Time: 1-2:00 (slow cinematic rise; CCW = faster sweep / CW = slower; LEDs GREEN fast -> AMBER slow; default 12:00)
controls:
  - { name: "Tape Saturation", type: switch, value: "any", options: ["ON","OFF"] }
  - { name: "Doubletracker", type: switch, value: "ON or BYPASSED (firmware v1.20+ allows Auto-Flange while bypassed)", options: ["ON","BYPASSED"] }
  - { name: "Doubletracker footswitch (trigger)", type: button, value: "PRESS AND HOLD DOUBLETRACKER ON for the momentary sweep, release to end (MIDI alt CC#97 = 127)" }
  - { name: "Slot/Bank", type: knob, value: "PC19" }
---

# Auto-Flange Transition

## Concept
A one-shot studio-style through-zero flange WHOOSH to mark a section change — a factory feature rather than a knob patch per se. It works even with the doubletracker bypassed (firmware v1.20+), so you can grab just the flange for transitions over whatever underlying patch is loaded. Great for marking the build of a sustained wall without committing the doubletracker.

## How to play it
1. Set Tape Saturation to anything; Doubletracker can be ON or BYPASSED (v1.20+ allows the sweep while bypassed).
2. Set Auto-Flange Time: hold Tape Saturation ON until LEDs flash, then turn LAG TIME — CCW = faster sweep / CW = slower (LEDs GREEN fast → AMBER slow; default 12:00). Set ~1–2:00 for a slow cinematic rise.
3. Pre-set the underlying patch (e.g. Pretty Tape Flange) so the flange lands somewhere musical.
4. Trigger: PRESS AND HOLD the DOUBLETRACKER ON footswitch for the momentary sweep (release to end). MIDI alt: CC#97 = 127.

## Notes
- A factory feature, not a knob patch per se.
- Be on firmware v1.20+ for bypassed-flange and v1.22+ to avoid the unintentional-engage-on-fast-footswitch bug.

## Sources
- links/strymon-deco-v2-manual-revd-secondary-midi.md (Auto-Flange Time on LAG TIME; CC#97)
- links/strymon-deco-v2-firmware-release-notes.md (v1.20 bypass-flange)
- transcripts/strymon-tape-flanging-chorus-examples.md; transcripts/superdanger
- Ref: Strymon Auto-Flange feature + firmware v1.20 bypass-flange
- Transformed from Pedalxly Deco-V2-Patches.md (factory/artist)
