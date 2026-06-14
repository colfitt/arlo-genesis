---
type: patch
title: Polyphony Organ Pad (oct-down + oct-up)
device: Eventide H90
date: 2026-06-14
description: Organ-like stacked chord pad from banjo/baritone chords — the banjo-as-chordal-lead engine, voices an octave down and up like organ drawbars.
tags: [pitch, polyphony, pad, banjo-lead, organ, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "20" }
  - { name: "Preset A Algorithm", type: switch, value: "Polyphony" }
  - { name: "Voice 1", type: knob, value: "octave DOWN" }
  - { name: "Voice 2", type: knob, value: "octave UP" }
  - { name: "Delay", type: knob, value: "dotted-eighth one side, quarter-note the other (Todd)" }
  - { name: "Pan", type: knob, value: "the two voices panned" }
  - { name: "Feedback", type: knob, value: "added" }
  - { name: "Inst Type", type: switch, value: "Percussive (banjo, preserves transients) — Pitched for smoother large intervals", options: ["Percussive", "Pitched"] }
---

# Polyphony Organ Pad (oct-down + oct-up)

## Concept
An organ-like stacked chord pad built from banjo/baritone chords — the banjo-as-chordal-lead engine. Voice 1 an octave down and Voice 2 an octave up act like organ drawbars; rhythmic delays, panning, and feedback fill it out.

## How to play it
1. Engage Polyphony on A with Voice 1 = octave DOWN, Voice 2 = octave UP.
2. Add a dotted-eighth delay on one side, a quarter-note on the other; pan the two voices; add Feedback.
3. For banjo set Inst Type = Percussive (preserves transients); use Pitched for smoother large intervals.

## Notes
- Leon Todd deep-dive (xyiMDam0jkQ). SIFT = chord-capable, making it the banjo-chord engine (UsageGuide §5).

## Sources
- research/transcripts/leon-todd-h90-polyphony-algorithm.md
- Transformed from Pedalxly H90-Patches.md (community)
