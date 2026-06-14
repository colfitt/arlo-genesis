---
type: patch
title: Self-Stretch (delay-as-looper)
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: Record a time-stretch into a delay-looper pile-up — feedback near max so repeats stack like a looper, then slowly rotate TIME clockwise to bake the stretch into the loop.
tags: [delay, looper, time-stretch, factory, signature]
dips:
  CLASSIC: off (clean stretch unless on)
controls:
  - { name: "Wet MODE", type: switch, value: "Delay", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Wet MODIFY", type: knob, value: "feedback near max (back off ~1:00 to avoid full self-oscillation)" }
  - { name: "Wet TIME", type: knob, value: "slowly rotate clockwise once audio is repeating" }
---

# Self-Stretch (delay-as-looper)

## Concept
Recording a stretch into a delay-looper pile-up. With Delay **MODIFY (feedback) near max** the repeats pile up like a looper; back off to ~1:00 to avoid full self-oscillation. Once audio is repeating, **slowly rotate TIME clockwise** — the stretching effect gets recorded into the loop itself.

## How to play it
1. Set Wet MODE = **Delay**.
2. Set MODIFY (feedback) near max so repeats stack into a loop — pull back to ~1:00 if it tips into runaway self-oscillation.
3. Play until the audio is repeating on its own.
4. **Slowly rotate TIME clockwise** — the stretch bakes permanently into the looping repeats.

## Notes
- Clean stretch unless **CLASSIC** is on (which adds rubbery pitch).
- Delay is the **only** mode that passes audio between the two channels.

## Sources
- manual pp.24–25 "Loop Tricks — Self-Stretch"; research/links/mood-mkii-official-manual-try-this-recipes.md (Recipe 8)
- Transformed from Pedalxly MOOD-MkII-Patches.md (factory)
