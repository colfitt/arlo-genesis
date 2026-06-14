---
type: patch
title: LEVEL BALANCE (fix two-channel balance)
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: Balance Wet vs Micro-Looper loudness — a hidden option (hold both footswitches, turn CLOCK). The channels are NOT auto-balanced and MIX won't fix it; the most common gain-staging gotcha.
tags: [hidden, gain-staging, balance, factory]
hidden:
  LEVEL BALANCE (CLOCK): CCW = more micro-looper, CW = more wet (reverb), NOON = even
controls:
  - { name: "LEFT + RIGHT footswitches (hidden access)", type: button, value: "HOLD both (LEDs green), then turn CLOCK" }
---

# LEVEL BALANCE (fix two-channel balance)

## Concept
Balancing Wet vs Micro-Looper loudness — the channels are NOT auto-balanced, and MIX won't fix it. A hidden option: hold **both footswitches** (LEDs green), then turn **CLOCK**. CCW = more micro-looper, CW = more wet (reverb), NOON = even.

## How to play it
1. **Hold both footswitches** until the LEDs go green (hidden-options mode).
2. Turn **CLOCK** to set the balance: CCW for more micro-looper, CW for more wet/reverb, NOON for even.

## Notes
- The single most common gain-staging gotcha.
- Re-check after using DIRECT MICRO-LOOP (direct-micro-loop-clean-blend), which causes a volume bump.

## Sources
- manual pp.16–17; chasebliss-mood-mkii-video-manual-pt2.md; community-mood-mkii-vs-original-clock-noise-levels.md
- Transformed from Pedalxly MOOD-MkII-Patches.md (factory)
