---
type: patch
title: Stereo stacked drums — banjo A / fuzz-wall B
device: TE OP-1 Field
date: 2026-06-14
description: Layer two different sample sources in one kit slot — rig-native a banjo one-shot on A + a fuzz-wall hit on B for a layered chromatic kit, with A/B stack-morph on the last knob (Field-only).
tags: [drum-kit, stacked-samples, field-only, ab-morph, designed, signature]
controls:
  - { name: "[Shift]+Ochre (open stacked channels)", type: button, value: "open channels A and B (Field-only)" }
  - { name: "Channel A sample", type: switch, value: "load a banjo one-shot" }
  - { name: "Channel B sample", type: switch, value: "load a fuzz-wall hit" }
  - { name: "[Shift]-press last knob (A/B stack-morph)", type: knob, value: "morph A→B through center; assignable as Value-LFO destination" }
  - { name: "Slot/Bank", type: knob, value: "drum/ folder — banjo-fuzz-stack" }
---

# Stereo stacked drums — banjo A / fuzz-wall B

## Concept

Layer two different sample sources in one kit slot. Rig-native: a banjo one-shot on channel A plus a fuzz-wall hit on channel B for a layered chromatic kit (TE's own example is 808 + 909). A Field-only feature. The per-slice last knob does an A/B stack-morph, and that morph can be a Value-LFO destination for an evolving hit.

## How to play it

1. `[Shift]+Ochre` = open stacked channels **A and B** (Field-only).
2. Load a different sample on each: banjo one-shot on A, fuzz-wall hit on B.
3. On the per-slice last knob, `[Shift]`-press = **A/B STACK-MORPH** — morph A→B through center.
4. Assign that morph as a **Value-LFO destination** to make the hit evolve over time.

## Notes

- Field-only feature; mechanism concrete and on disk (TE via MusicRadar + sonwu A/B-morph demo).
- Samples are user-chosen → tagged designed. Drum-sampler-only. Save as `banjo-fuzz-stack`.

## Sources

- Gear/TE OP-1 Field/research/links/musicradar-8-ways-op1-field.md + transcripts/sonwu-op1-field-sampler-engine-tutorial.md + UsageGuide §3
- Transformed from Pedalxly OP-1-Field-Patches.md (DOUG-designed)
