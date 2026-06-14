---
type: patch
title: Micro-Loop Transfer (copy loop into Delay)
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: Duplicate a micro-loop inside the Delay so you hear two loops at once — crank feedback to copy the loop, then switch ROUTING to IN to hear both layers.
tags: [delay, looper, layering, factory]
controls:
  - { name: "ROUTING", type: switch, value: "micro-loop only (or IN+micro-loop), then switch to IN to hear both", options: ["IN", "IN+micro-loop", "micro-loop only"] }
  - { name: "Wet MODE", type: switch, value: "Delay", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Wet MODIFY", type: knob, value: "crank (feedback) to copy the loop" }
---

# Micro-Loop Transfer (copy loop into Delay)

## Concept
The cheapest way to get two independent loop layers. Route a micro-loop through the Delay and **crank MODIFY (feedback)** to copy the loop into the delay buffer. Then switch ROUTING to **IN** so you hear both the original micro-loop and the delay-copy together.

## How to play it
1. Set ROUTING to **micro-loop only** (or IN+micro-loop) and Wet MODE = **Delay**.
2. With a micro-loop running, **crank MODIFY (feedback)** to copy the loop into the Delay.
3. Switch ROUTING to **IN** — you now hear the micro-loop and its delay-copy at the same time.

## Notes
- Pairs with Double Time (freeze-idea-double-time) for stacking even more independent layers.

## Sources
- manual pp.24–25 "Loop Tricks — Micro-Loop Transfer"; research/links/mood-mkii-official-manual-try-this-recipes.md (Recipe 8)
- Transformed from Pedalxly MOOD-MkII-Patches.md (factory)
