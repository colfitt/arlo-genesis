---
type: patch
title: Frozen banjo bed (rig recipe d)
device: OBNE Dark Star V3
date: 2026-06-14
description: The defining banjo-as-lead move — play a banjo roll, freeze it into a static drone bed with predelay, then solo over the static pad (DOUG-designed numeric rig recipe).
tags: [banjo, freeze, drone, hold, designed, signature]
hidden:
  Aux mode: Hold
controls:
  - { name: "Mix", type: knob, value: "1:00 (mostly wet)" }
  - { name: "Decay", type: knob, value: "noon (you'll freeze it anyway)" }
  - { name: "Multiply", type: knob, value: "noon" }
  - { name: "Filter", type: knob, value: "noon (favor LPF side if octave-up ice-picks)" }
  - { name: "Pitch 1", type: knob, value: "noon (clean bed) [or +12 right for sparkle]" }
  - { name: "Pitch 2", type: knob, value: "noon" }
  - { name: "Crush", type: knob, value: "noon" }
  - { name: "Lag", type: knob, value: "1:00 (short)" }
  - { name: "Aux", type: button, value: "Hold (freeze the bed)" }
  - { name: "Routing", type: switch, value: "Stereo (trails on)", options: ["Mono", "Mono-In-Stereo-Out", "Stereo"] }
---

# Frozen banjo bed (rig recipe d)

## Concept
The defining banjo-as-lead move: play a banjo roll, freeze it into a static drone bed, then solo over the static pad. The short Lag (1:00) lets the fast banjo transient speak before the wash blooms. DOUG-designed numeric starting point for this banjo/baritone rig, assuming Stereo routing and trails on.

## How to play it
1. Set Mix 1:00, Decay noon, Multiply noon, Filter noon, both Pitch knobs noon, Crush noon, Lag 1:00.
2. Assign Aux = Hold.
3. Play a banjo roll, then engage Aux to freeze it into a static drone bed.
4. Solo over the static pad — the short Lag lets the fast banjo transient speak before the wash blooms.

## Notes
- DOUG-inferred numeric values for THIS rig (clock convention: 12 = noon, 1 ≈ mostly-CW, 11 ≈ mostly-CCW) — not quoted from any external source.
- Pitch 1 can go +12 (a hair right of noon) for sparkle; favor the LPF side of Filter if octave-up content ice-picks.
- Hold dry-pass-through caveat — notes over the frozen pad pass DRY; lean on the dry path + downstream H90 verb for the lead, or use expression swells.
- Suggested onboard slot 1 (live-set recall).

## Sources
- designed from DeepResearch §13(d) + UsageGuide §5
- Transformed from Pedalxly Dark-Star-V3-Patches.md (designed)
