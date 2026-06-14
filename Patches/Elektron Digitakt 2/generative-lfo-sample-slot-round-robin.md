---
type: patch
title: Generative LFO → Sample-Slot Round-Robin (banjo-lead variation)
device: Elektron Digitakt 2
date: 2026-06-14
description: Never-identical banjo / percussion lead from several real plucks — a RANDOM LFO on sample SLOT plays a different sample per step.
tags: [generative, round-robin, banjo, lfo, community, signature]
controls:
  - { name: "Sample slots", type: switch, value: "Target samples (e.g. 4 banjo plucks) in CONSECUTIVE slots; MIDDLE sample assigned to track" }
  - { name: "LFO1 WAVE", type: switch, value: "RANDOM (RAMP for the deterministic variant)" }
  - { name: "LFO1 MODE", type: switch, value: "TRIG", options: ["FREE","TRIG","HOLD","ONE","HALF"] }
  - { name: "LFO1 DEST", type: switch, value: "Sample SLOT" }
  - { name: "LFO1 DEP", type: knob, value: "≈ 2.9 for 7 samples (NON-LINEAR scaling — not 7)" }
  - { name: "Trig conditions", type: switch, value: "FILL / conditional trigs (not on step 1) to re-fire variation" }
  - { name: "LFO retrig (LFO.T)", type: switch, value: "step 1 only (RAMP variant → clean restart each loop)", options: ["ON","OFF"] }
---

# Generative LFO → Sample-Slot Round-Robin (banjo-lead variation)

## Concept
A never-identical banjo/percussion lead: place several real plucks in consecutive sample slots and let a RANDOM LFO on the sample SLOT destination pick a different sample each step. The slot-scaling is non-linear, so the depth value is the load-bearing trick. A RAMP variant (BPM-synced, LFO retrig on step 1) gives a deterministic amen-style scan instead.

## How to play it
1. Place target samples (e.g. 4 banjo plucks) in CONSECUTIVE slots; assign the MIDDLE sample to the track.
2. LFO: `WAVE = RANDOM`, `MODE = TRIG`, `DEST = sample SLOT`.
3. `DEP` scaling is non-linear — for 7 samples set `DEP` ≈ 2.9 (not 7).
4. Tuning trick: temporarily point `DEST` at sample START so you can see the LFO move on the waveform, then switch back to slot.
5. Add FILL / conditional trigs (not on step 1) to re-fire variation.
6. Repeatable variant: `WAVE = RAMP`, BPM-synced, enable LFO retrig (`LFO.T`) on step 1 only → clean restart every loop (amen-style scan).

## Notes
- `DEP ≈ 2.9-for-7` is the load-bearing concrete value (the scaling quirk catches everyone).
- The RAMP version is deterministic; the RANDOM version is generative.
- Use 4 consecutive sample slots; one track plays the middle slot.

## Sources
- `research/links/elektronauts-plock-sample-changes-per-step.md` (t/171663 — Doug, re5et, motokobis)
- `research/links/elektronauts-dt2-generative-and-drone.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
