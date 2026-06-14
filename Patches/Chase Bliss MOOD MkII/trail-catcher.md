---
type: patch
title: Trail Catcher (bake ambience into the loop)
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: Resample reverb trails permanently into a micro-loop — run the loop through the Reverb, then briefly toggle the Micro-Looper OFF and back ON to resample the trails. ⚠️ Permanent.
tags: [capture, resample, reverb, looper, factory, signature]
controls:
  - { name: "ROUTING", type: switch, value: "includes Wet on the loop (run the micro-loop through the Reverb)", options: ["IN", "IN+micro-loop", "micro-loop only"] }
  - { name: "Wet MODE", type: switch, value: "Reverb", options: ["Reverb", "Delay", "Slip"] }
  - { name: "RIGHT footswitch (Micro-Looper)", type: button, value: "briefly turn the Micro-Looper OFF and back ON to resample the reverb trails into the loop" }
---

# Trail Catcher (bake ambience into the loop)

## Concept
Resampling reverb trails permanently into a micro-loop. Run a micro-loop through the Reverb (ROUTING includes Wet on the loop), then briefly turn the **Micro-Looper OFF and back ON** — it resamples the reverb trails into the loop. Because the looper records while bypassed/always-listening, any Wet or upstream effect is baked in permanently.

## How to play it
1. Set ROUTING so the micro-loop runs through the Reverb, and Wet MODE = **Reverb**.
2. Let the loop pick up reverb trails.
3. **Briefly turn the Micro-Looper OFF and back ON** — the reverb trails are resampled into the loop.

## Notes
- ⚠️ **Plan the moment — it's permanent.**
- Nuance: while **overdubbing**, Wet effects are NOT recorded (clean input only); baking happens only in the bypassed always-listening state.

## Sources
- manual pp.28–31 + p.41; chasebliss-mood-mkii-video-manual-pt1.md; community-mood-mkii-pitfalls-and-gotchas.md
- Transformed from Pedalxly MOOD-MkII-Patches.md (factory)
