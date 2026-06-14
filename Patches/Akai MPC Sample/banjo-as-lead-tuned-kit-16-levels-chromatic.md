---
type: patch
title: Banjo-as-Lead Tuned Kit — 16 Levels Chromatic
device: Akai MPC Sample
date: 2026-06-14
description: Playing the banjo (GK-5 → VG-800) as a melodic LEAD voice across the pads, spread chromatically via 16 Levels = Tune.
tags: [melodic, banjo-as-lead, 16-levels, rig-integration, designed, signature]
controls:
  - { name: "Warp", type: switch, value: "OFF first (16 Levels refuses with Warp on)", options: ["Off", "Pitch", "BPM"] }
  - { name: "16 Levels Type", type: switch, value: "Tune (one note spreads chromatically across all 16 pads)", options: ["Velocity", "Filter", "Tune"] }
  - { name: "Scale map", type: knob, value: "root on pad 4, ascends; skip out-of-scale pads (≥4 in-key/scale; no native scale lock)" }
  - { name: "Amp Attack", type: knob, value: "0 (keep the pluck transient)" }
  - { name: "Amp Decay", type: knob, value: "medium (rings as a lead)" }
  - { name: "Vinyl Emulator Crackle", type: knob, value: "~20% (degraded character)" }
  - { name: "Vinyl Emulator Tone", type: knob, value: "~40" }
  - { name: "Wider range/chords", type: switch, value: "drive from 61SL MkIII over MIDI In, or pre-sample the chord", options: ["16 Levels", "MIDI In"] }
  - { name: "Slot/Bank", type: knob, value: "16 pads (16 Levels = Tune)" }
---

# Banjo-as-Lead Tuned Kit — 16 Levels Chromatic

## Concept
Playing the banjo (GK-5 → VG-800) as a melodic LEAD voice across the pads. Sample single plinks, spread one note chromatically across all 16 pads with 16 Levels = Tune, keep the pluck transient, and let it ring as a lead. HIGH fit — banjo-as-lead. "Warp off first" is a real gotcha (16 Levels refuses with Warp on).

## How to play it
1. Sample single banjo plinks (line in or built-in mic).
2. Turn Warp OFF first (16 Levels refuses with Warp on).
3. Press 16 Levels → Type = Tune: one banjo note spreads chromatically across all 16 pads (community map: root on pad 4, ascends; skip out-of-scale pads following the major/minor shapes — usually ≥4 in-key notes per scale, no native scale lock).
4. Amp Attack = 0 to keep the pluck transient; medium Decay so it rings as a lead.
5. Add Vinyl Emulator (Crackle ~20%, Tone ~40%) for degraded character.
6. For wider range/chords, drive from the 61SL MkIII over MIDI In or pre-sample the chord.

## Notes
- HIGH fit — banjo-as-lead.
- The exact pad-skip shapes live in the imgur cheat-sheet image (t/220653), not transcribable as text.
- "Warp off first" is a real gotcha.

## Sources
- 🟣 designed from `research/links/mpcforums-ac50-16-levels-melodic-scale-map.md` (t/220653, scale map) + `research/links/manual-fx-parameter-reference-knob-fx-color-vintage.md` (16 Levels needs Warp off)
- Transformed from Pedalxly MPC-Sample-Patches.md (designed)
