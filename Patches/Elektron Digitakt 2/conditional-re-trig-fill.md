---
type: patch
title: Conditional Re-Trig Fill (gated roll)
device: Elektron Digitakt 2
date: 2026-06-14
description: A riser/fill roll that only fires on some passes — hands-free build-ups using a conditional retrig with a gap-filling preceding retrig.
tags: [conditional, retrig, fill, workflow, community, signature]
controls:
  - { name: "RETRIG (TRIG page 2)", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "RATE", type: knob, value: "subdivision" }
  - { name: "LEN", type: knob, value: "step count" }
  - { name: "VFAD", type: knob, value: "±fade" }
  - { name: "Trig CONDITION", type: switch, value: "e.g. 1:4 / FILL / 25%" }
  - { name: "Preceding trig retrig RATE", type: knob, value: "set to land ON the conditional trig's step (fills the gap when condition is FALSE)" }
  - { name: "Within-track stutter", type: switch, value: "duplicate the step on the next beat, micro-timing fully LEFT, with a PRE/false condition" }
---

# Conditional Re-Trig Fill (gated roll)

## Concept
A riser/fill roll that only fires on some passes, for hands-free build-ups. Set a retrigging trig with a condition (1:4 / FILL / 25%), then put a retrig on the preceding trig whose rate lands exactly on the conditional trig's step — so when the condition is FALSE the preceding retrig plays the normal hit and there's no gap. Pairs with patch 25.

## How to play it
1. Set a retrigging trig (TRIG page 2: `RETRIG` on, `RATE` = subdivision, `LEN` = step count, `VFAD` = ±fade).
2. Add a trig CONDITION (e.g. `1:4` / `FILL` / `25%`).
3. On the preceding trig, set a retrig `RATE` that lands ON the conditional trig's step → when the condition is FALSE the preceding retrig plays the "normal" hit (no gap).
4. Within-track stutter: duplicate the step on the next beat, micro-timing fully LEFT, with a PRE/false condition.

## Notes
- The logic is concrete; `RATE/LEN/VFAD` integers aren't posted — use existing retrig values.
- Works on any track; pairs with patch 25.

## Sources
- `research/links/elektronauts-conditional-retrigs.md` (t/57273 — lindefelt, Hawk)
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
