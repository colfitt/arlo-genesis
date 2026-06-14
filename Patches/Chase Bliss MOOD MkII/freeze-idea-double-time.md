---
type: patch
title: Freeze Idea: Double Time
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: Two independent loop layers — capture a micro-loop first, then play into the Delay and freeze it into a secondary micro-loop. Combine with SYNC to lock the delay to the loop length.
tags: [freeze, delay, looper, layering, factory, signature]
controls:
  - { name: "Wet MODE", type: switch, value: "Delay", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Wet TIME", type: knob, value: "delay length (experiment with different lengths)" }
  - { name: "Wet MODIFY", type: knob, value: "feedback" }
  - { name: "Looper MODE", type: switch, value: "capture a micro-loop first", options: ["Env", "Tape", "Stretch"] }
  - { name: "LEFT footswitch (Wet / freeze)", type: button, value: "HOLD to freeze the Delay into a secondary micro-loop" }
hidden:
  SYNC (Wet MODE toggle): lock the delay to the loop length
---

# Freeze Idea: Double Time

## Concept
Two independent loop layers — the Micro-Looper plus a frozen-delay layer. **Capture a micro-loop first.** Then set Wet MODE = **Delay**, play notes into the Delay (TIME = length, MODIFY = feedback) and **HOLD LEFT FS to freeze** it → it becomes a secondary micro-loop running alongside the first.

## How to play it
1. Capture a micro-loop **first**.
2. Set Wet MODE = **Delay**; set TIME for the delay length and MODIFY for feedback.
3. Play notes into the Delay, then **HOLD the LEFT footswitch** to freeze it into a secondary micro-loop.
4. Experiment with different delay TIME lengths; combine with **SYNC** (hidden) to lock the delay to the loop length.

## Notes
- Pairs with Perry Frank's Delay+Tape rhythmic-drone idea (delay-tape-rhythmic-drone).

## Sources
- manual pp.22–23 "Freeze Ideas — Double Time"; research/links/mood-mkii-official-manual-try-this-recipes.md (Recipe 4)
- Transformed from Pedalxly MOOD-MkII-Patches.md (factory)
