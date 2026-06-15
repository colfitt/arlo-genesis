---
type: patch
title: Oceanic Outro Hall
device: Strymon Big Sky
date: 2026-06-15
description: "A huge Arena Hall used as the catch-space for a saturated, climbing delay wall — paired downstream of the Big Time Loop Diffuser. DIALABLE RECIPE: knob values are designed starting points from the documented Hall machine parameter set and a documented Hall (Concert) starting patch, not a captured factory/.syx slot. Fills a gap — no existing Big Sky patch uses the Hall machine."
tags: [reverb, hall, ambient, drone, doom, outro, designed, big-room]
hidden:
  HOLD: FREEZE (optional — lock the room and change parts over it)
controls:
  - { name: "Machine", type: switch, value: "HALL", options: ["Cloud","Shimmer","Bloom","Chorale","Swell","Magneto","Nonlinear","Reflections","Room","Hall","Plate","Spring"] }
  - { name: "Size", type: switch, value: "Arena (larger of Concert/Arena)", options: ["Concert","Arena"] }
  - { name: "DECAY", type: knob, value: "long, ~10-15 S (dialable; Hall range 500 mS-20 S)" }
  - { name: "MIX", type: knob, value: "held back (depth, not level — sits behind a thick wall)" }
  - { name: "TONE", type: knob, value: "above noon (keep the bloom open)" }
  - { name: "LOW END", type: knob, value: "below noon (load-bearing — heavy source feeds it)" }
  - { name: "MID", type: knob, value: "flat-to-slightly-up" }
  - { name: "PRE-DELAY", type: knob, value: "short-to-moderate, ~9:00-12:00" }
  - { name: "MOD", type: knob, value: "light, ~11:00" }
---

# Oceanic Outro Hall

## Concept
A huge concert/arena Hall used as the catch-space for a saturated, climbing delay wall (paired downstream of the Big Time Loop Diffuser). Where the rig's other long-tail Big Sky patches are Cloud grain-washes, this one is a literal big room: the Hall machine at Arena size with a long decay opens the doom bloom into a believable oceanic space rather than another diffusion smear. Fills a gap — no existing Big Sky patch uses the Hall machine.

## How to play it
1. Set the machine to HALL and Size to Arena for the largest space.
2. Dial DECAY long (~10-15 s) so the catch-space sustains under the climbing Big Time loop.
3. Pull MIX back so the Hall adds depth, not level, behind the thick wall feeding it.
4. Pull LOW END below noon and lift TONE so the doom bloom stays defined instead of turning to porridge.
5. Place it AFTER the Big Time (saturate + diffuse first, then the room) — never reverse the order.
6. Optional: HOLD = FREEZE to lock the room and play/change parts over the frozen space.

## Notes
- DIALABLE RECIPE, not sourced: the knob values are designed starting points drawn from the Hall machine's documented parameter set (Low End, Mid, Size Concert/Arena; 500 mS-20 S decay) and a documented Hall (Concert) starting-point patch — no exact factory/.syx dials were captured for this specific outro voicing. Grab/save your own preset once dialed.
- Fills a genuine gap: every other Big Sky patch in the corpus uses Cloud / Bloom / Shimmer / Chorale / Magneto / Nonlinear / Swell — none uses the Hall machine. This is the rig's "real big room" Hall for when a Cloud wash is too grainy.
- Built to pair with CB Big Time "Loop Diffuser" — keep the Big Sky MIX low because the source is already a saturated, climbing wall.
- Two ambient stages stack low end fast — the below-noon LOW END is load-bearing, not optional, with a heavy source feeding it.

## Sources
- gear/Strymon Big Sky/research/Big-Sky-DeepResearch.md — machine table (Hall: Low End, Mid, Size Concert/Arena; 500 mS-20 S decay) and §13a starting-point Hall (Concert) settings (Decay ~3.5s, Pre-Delay 9:00, Mix 10:00, Tone 12, Mod 11, Low End centered, Mid flat)
- gear/Strymon Big Sky/research/Big-Sky-DeepResearch.md — baritone/low-source caution: "Watch Low End on Hall/Cloud... pull Low End back and lean on Tone"
- Pairing / gain-staging rationale from gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md (low-COLOR / high-FEEDBACK climb into limiter; feed into a hall for the doom wall)

<!-- provenance: 🟣 DOUG-designed (dialable recipe). Built for this chain to give the Big Time Loop Diffuser a Hall to bloom into. Hall machine parameters and a Hall starting-point are documented; the specific outro knob values are designed, not captured from a factory/artist slot. -->
