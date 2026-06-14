---
type: patch
title: Step Sequence
device: Chase Bliss Blooper
date: 2026-06-14
description: Turn a single looped tone into a sequence or harmonic stack from one held note via Pitcher — the overdub-safe pitch shift that keeps loop length identical.
tags: [pitch, harmony, pitcher, sequence, factory, signature]
hidden:
  BANK A dip (ALT bank): on
controls:
  - { name: "Mode", type: switch, value: "ADD", options: ["NORM", "ADD", "SAMP"] }
  - { name: "MOD A", type: knob, value: "−3 oct CCW … noon … +3 oct CW (length unchanged — the ADD-mode safe zone)" }
  - { name: "MOD A slot", type: switch, value: "A2 Pitcher (ALT bank)", options: ["A1", "A2", "A3"] }
  - { name: "MOD A engage", type: button, value: "use ramping or manual knob moves and record results in ADD" }
  - { name: "Slot/Bank", type: knob, value: "MOD A2 ALT bank (requires BANK A dip) · MIDI PC 14 (shares ALT-A harmony family)" }
---

# Step Sequence

## Concept

Turn a single looped tone into a sequence or harmonic stack from one held note — no second instrument. Pitcher shifts ±3 octaves while keeping loop length identical, making it the overdub-safe pitch shift (the ADD-mode "safe zone").

## How to play it

1. In ADD mode, set MOD A to Pitcher (ALT bank A2) — requires the BANK A dip.
2. Loop a single tone.
3. Use ramping or manual Pitcher knob moves (−3 oct CCW … noon … +3 oct CW) and record the results in ADD.
4. The single tone becomes a sequence or harmonic stack.

## Notes

- Pitcher keeps loop length identical in ADD, so it's the overdub-safe pitch shift.
- DSP-heavy: mutually exclusive with Stretcher — plan one per loop.
- Requires the BANK dip (physical-only).

## Sources

- `research/links/chasebliss-blooper-modifier-cheat-sheet.md`
- `research/Blooper-UsageGuide.md`
- Transformed from Pedalxly Blooper-Patches.md (factory/artist)
