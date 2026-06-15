---
type: patch
title: "Diatonic — In-Key Harmony (3rds + 5ths, twin-guitar)"
device: Eventide H90
date: 2026-06-15
description: "Smart, scale-correct harmony that follows the song — pick a Key and Scale and Diatonic adds spelled-in-key 3rds, 5ths or octaves above/below single-note lines for instant Thin Lizzy / Maiden twin-guitar harmonies on banjo/baritone leads. From the official manual (Key+Scale, 12 scales, monophonic, LEARN, Quadravox); exact intervals/mix dial to the song."
tags: [diatonic, pitch, harmony, in-key, twin-guitar, lead]
controls:
  - { name: "Preset A Algorithm", type: switch, value: "Diatonic" }
  - { name: "Key", type: knob, value: "song root (or set live via LEARN)" }
  - { name: "Scale", type: switch, value: "song scale", options: ["Major", "Minor", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Locrian", "Harmonic Minor", "Melodic Minor", "Whole Tone", "Enigmatic", "Neapolitan", "Hungarian"] }
  - { name: "Pitch Shift A", type: knob, value: "+3rd (diatonic, constrained to scale)" }
  - { name: "Pitch Shift B", type: knob, value: "+5th or +octave (diatonic, constrained to scale)" }
  - { name: "Pitch A Mix", type: knob, value: "balance voice A (dial to song)" }
  - { name: "Pitch B Mix", type: knob, value: "balance voice B (dial to song)" }
  - { name: "Delay A", type: knob, value: "optional (dial to song)" }
  - { name: "Delay B", type: knob, value: "optional (dial to song)" }
  - { name: "LEARN", type: button, value: "press-and-hold to set Key live between sections" }
---

# Diatonic — In-Key Harmony (3rds + 5ths, twin-guitar)

## Concept
Smart, in-key harmony that follows the song: pick a Key and Scale and Diatonic adds correctly-spelled 3rds, 5ths or octaves above/below single-note lines — instant Thin Lizzy / Maiden twin-guitar harmonies on banjo/baritone leads. Because the intervals are constrained to the chosen scale, every harmony note lands diatonically as the line moves.

## How to play it
1. Load Diatonic on Preset A; choose Key and Scale to match the song.
2. Set Pitch Shift A to a +3rd and Pitch Shift B to a +5th (or octaves) within the scale.
3. Balance the harmony voices with Pitch A/B Mix; add Delay A/B if you want spread.
4. Play single-note lines (avoid chords) for clean tracking.
5. Use LEARN (press-and-hold) to re-key on the fly between sections.

## Notes
- The 12-scale list, monophonic limit, LEARN, and Quadravox panning are from the manual; **exact intervals/mix values are not published — dial them to the song** (treat the control values here as a dialable recipe, not sourced settings).
- **Diatonic is MONOPHONIC** — play single isolated notes/octaves, not chords. For full chords use the polyphonic Polyphony / PrismShift instead.
- Quadravox extends this to four in-key voices (A & C panned left, B & D right) if you need a thicker stack.
- Distinct from `harmonized-banjo-lead-diatonic-plate` (which adds a Plate + slot context) — this is the core algorithm recipe.

## Sources
- https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/algorithms/pitch.html (Diatonic: Key+Scale, 12 scales, monophonic, LEARN; Quadravox four voices with panning)
