---
type: patch
title: Harmonized Banjo Lead (Diatonic -> Plate)
device: Eventide H90
date: 2026-06-14
description: Banjo-as-lead in key — single-note lead lines harmonized via Diatonic (Key set by Learn) into a short Plate/Room.
tags: [pitch, diatonic, banjo-lead, harmony, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "27" }
  - { name: "Routing", type: switch, value: "Series (pitch -> reverb)", options: ["Series", "Parallel", "Insert"] }
  - { name: "Preset A Algorithm", type: switch, value: "Diatonic (single-note leads)" }
  - { name: "Key (Learn footswitch)", type: button, value: "set Key while playing the root" }
  - { name: "Pitch A", type: knob, value: "+3rd / +5th in the song's scale" }
  - { name: "Delay", type: knob, value: "low" }
  - { name: "Mix (A)", type: knob, value: "~40-60% wet" }
  - { name: "Preset B Algorithm", type: switch, value: "Plate or Room (short, tasteful)" }
---

# Harmonized Banjo Lead (Diatonic -> Plate)

## Concept
Banjo-as-lead in key, for single-note lead lines. Diatonic tracks the input and adds a scale-correct harmony (+3rd / +5th); a short Plate or Room seats the line. Feed the cleanest available banjo tone (a less-saturated VG-800 model) so the tracker stays locked.

## How to play it
1. Set Routing to Series, pitch -> reverb.
2. Engage Diatonic on A; set Key via the **Learn footswitch** while playing the root.
3. Set Pitch A to +3rd / +5th in the song's scale, Delay low, Mix ~40-60% wet.
4. Add a short, tasteful Plate or Room on B.

## Notes
- Inferred (not a cited setting) — treat values as a designed starting point.
- **Diatonic is MONOPHONIC** — for chordal banjo use Polyphony (Percussive) or PrismShift instead.
- Pairs with the two-scales-one-footswitch HotSwitch move.

## Sources
- designed from research/H90-DeepResearch.md §13(d)
- Transformed from Pedalxly H90-Patches.md (designed)
