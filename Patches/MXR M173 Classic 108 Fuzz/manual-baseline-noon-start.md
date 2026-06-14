---
type: patch
title: Manual baseline (noon start)
device: MXR M173 Classic 108 Fuzz
date: 2026-06-14
description: The manual's own sane starting point — both knobs at noon, buffer on — the patch to dial from on this board before tweaking.
tags: [fuzz, baseline, reference, factory]
controls:
  - { name: "OUTPUT/VOLUME", type: knob, value: "12:00" }
  - { name: "FUZZ/INPUT", type: knob, value: "12:00" }
  - { name: "BUFFER", type: switch, value: "ON", options: ["ON", "OFF"] }
---

# Manual baseline (noon start)

## Concept
The manual's own sane starting point — "start with all controls at 12 o'clock," then engage the BUFFER switch. Both knobs at noon is the deepest-tested A/B reference point (SuperFunAwesome: at 12/12, buffer ON = audibly brighter, buffer OFF = darker/fuller). Low signature-fit on its own, but the correct dial-from point for this rig.

## How to play it
1. Set OUTPUT/VOLUME and FUZZ/INPUT both to 12 o'clock.
2. Engage BUFFER ON — "you may notice a brightening of the fuzz tone." BUFFER ON specifically because the Colour Box buffer + VG-800 line sit in front.
3. Tweak from here for any of the other patches.

## Notes
- This is the dial-from reference, not a destination tone.
- Use the 12/12 A/B to hear what BUFFER ON vs OFF actually does on this board before committing to a voicing.

## Sources
- Dunlop M173 manual — operating directions — `manuals/M173.pdf` + `research/links/settings-m173-manual-factory-presets.md`
- Transformed from Pedalxly 108-Fuzz-Patches.md (factory)
