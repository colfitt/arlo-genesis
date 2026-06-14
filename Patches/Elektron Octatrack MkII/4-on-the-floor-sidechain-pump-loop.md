---
type: patch
title: 4-on-the-Floor Sidechain-Pump Loop
device: Elektron Octatrack MkII
date: 2026-06-14
description: Faking the house pump on the OT — a loop breathes with the kick via the input compressors or an LFO-ramp duck (taste-profile, designed-to-emulate).
tags: [filter-house, sidechain, pump, taste-profile, lfo, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "OT-E2 (Taste-Profile)" }
  - { name: "Loop track machine", type: switch, value: "Flex/Static, loop on a track", options: ["Flex", "Static"] }
  - { name: "Kick track", type: switch, value: "kick on a track for the four-on-the-floor" }
  - { name: "Pump method (a)", type: switch, value: "route the loop through an input COMPRESSOR (one per input pair; OT factory template ships sidechain pumping on every pattern, default 4-on-the-floor)" }
  - { name: "Pump method (b)", type: switch, value: "LFO → AMP volume on the loop track, WAVE = RAMP, synced 1/4, DEP high, retrigged on the kick step (recover before the next beat)" }
---

# 4-on-the-Floor Sidechain-Pump Loop

## Concept
Faking the house pump on the OT: a loop breathes with the kick. The OT has no true sidechain key, so either route the loop through an input compressor (the factory template ships sidechain pumping on every pattern) or duck the loop's AMP volume with an LFO ramp synced to the kick. Designed-to-emulate the four-on-the-floor pump of filter-house / LCD.

## How to play it
1. Put a loop on a Flex/Static track; put a kick on a track for the four-on-the-floor.
2. **Pump (a):** route the loop through an input COMPRESSOR (one per input pair; OT factory template ships 'sidechain pumping on every pattern, default 4-on-the-floor').
3. **Pump (b):** LFO → AMP volume on the loop track, WAVE = RAMP, synced 1/4, DEP high, retrigged on the kick step. Recover before the next beat.

## Notes
- OT-E2. APPROXIMATION: no true sidechain key — the input comp / LFO-ramp fakes the duck. Flagged.
- Designed-to-emulate; starting point, dial to taste.

## Sources
- Ref: Filter-house / LCD four-on-the-floor pump
- Research/Taste-Profile/sources/sidechain-pump-settings-house-techno.md
- Transformed from Pedalxly Octatrack-MkII-Patches.md (DOUG-designed)
