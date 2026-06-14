---
type: patch
title: Phasing Two-Part Drift (Reich/Eno) (Recipe B)
device: Novation 61SL MkIII
date: 2026-06-14
description: DOUG-designed two-Part Session — two related voices start aligned and slowly phase apart over many bars, re-converging periodically; the Steve-Reich / Eno drift for evolving walls.
tags: [generative, phasing, reich, eno, sequencer, drift, designed, signature]
controls:
  - { name: "Parts", type: knob, value: "Part1 + Part2 → two related voices, SAME notes/scale on both" }
  - { name: "Part 1 Sync Rate", type: knob, value: "1/16" }
  - { name: "Part 2 Sync Rate", type: knob, value: "1/16T (or 1/8 vs 1/8T) — they phase apart and re-converge" }
  - { name: "Part 2 Pattern Shift", type: knob, value: "3–5 (nudges start/end against Part1)" }
  - { name: "Part 2 Swing (per-Part, fw 1.4)", type: knob, value: "~58% (Part1 Off)" }
  - { name: "Chance (both)", type: knob, value: "~80% (occasional dropouts keep it off an obvious loop)" }
  - { name: "Scales", type: switch, value: "On + Snap on BOTH", options: ["Off", "On"] }
  - { name: "Scale Root", type: knob, value: "Song key" }
  - { name: "Scale Type", type: switch, value: "Natural Minor / Dorian / Phrygian", options: ["Natural Minor", "Dorian", "Phrygian"] }
  - { name: "Part 1 Destination", type: switch, value: "DIN → VG baritone Ch", options: ["USB", "DIN1", "DIN2", "CV"] }
  - { name: "Part 2 Destination", type: switch, value: "USB → soft synth or 2nd DIN", options: ["USB", "DIN1", "DIN2", "CV"] }
  - { name: "Clock", type: switch, value: "SL master", options: ["SL master", "Off"] }
  - { name: "Session Slot", type: knob, value: "Session slot 6" }
---

# Phasing Two-Part Drift (Reich/Eno) (Recipe B)

## Concept
Two related voices that start aligned and slowly phase apart over many bars, re-converging periodically — the Steve-Reich / Eno drift for evolving walls. E.g. a baritone-VG drone + a high bell/pluck soft-synth. Per-Part independent Sync Rate plus per-Part swing is what makes the two grids drift; both are firmware 1.4 features.

## How to play it
1. PART1 + PART2 → two related voices, SAME notes/scale on both.
2. SYNC RATES DIFFERENT: Part1 = 1/16, Part2 = 1/16T (or 1/8 vs 1/8T) → they phase apart and re-converge.
3. PATTERN SHIFT on Part2 = 3–5 (nudges its start/end against Part1).
4. SWING (per-Part, firmware 1.4): On for Part2 only (~58%), Off for Part1 → grids breathe against each other.
5. CHANCE ~80% on both (occasional dropouts keep it off an obvious loop).
6. SCALES: On + Snap on BOTH (guaranteed consonant as they drift), Root = song key, Type = Natural Minor/Dorian/Phrygian.
7. Destinations: route each Part to its own voice (e.g. Part1 DIN→VG baritone Ch, Part2 USB→soft synth or 2nd DIN). CLOCK: SL master.

## Notes
- DESIGNED.
- Per-Part independent Sync Rate + per-Part swing is what makes the two grids drift — both firmware 1.4 features.
- Banjo (VG) can carry one of the two voices as a lead line in the drift.

## Sources
- designed from research/links/seq-generative-recipes.md Recipe B + novation-firmware-1.4-generative-instrument.md (per-Part swing) + seq-manual-pattern-view.md; taste-profile.
- Ref: Taste — Steve Reich / Brian Eno phase music; post-punk/experimental motorik repetition.
- Transformed from Pedalxly 61SL-MkIII-Patches.md (designed)
