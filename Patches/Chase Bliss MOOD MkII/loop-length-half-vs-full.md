---
type: patch
title: LOOP LENGTH — half vs full (V1-length loops)
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: "A hidden option that halves the Micro-Looper's loop length relative to the CLOCK setting, restoring the original MOOD's shorter loops — the MkII doubled loop length, and this returns the V1 response for workflows that prefer the tighter micro-loop. Set with the looper MODE toggle inside the hidden menu (official video manual pt.2 + official tips page + community walkthrough; manual pp.14–17)."
tags: [hidden, looper, loop-length, factory, technique]
hidden:
  LOOP LENGTH (looper MODE toggle): "LEFT = HALF length (V1 response) · other = FULL (MkII default). Loop length is otherwise still governed by CLOCK position."
controls:
  - { name: "LEFT + RIGHT footswitches (hidden access)", type: button, value: "HOLD both until the LEDs go green, then move the looper MODE toggle" }
  - { name: "Looper MODE", type: switch, value: "LEFT = HALF loop length (V1 response); other position = FULL (MkII default)", options: ["Env", "Tape", "Stretch"] }
  - { name: "CLOCK", type: knob, value: "still governs absolute loop length — now at half the MkII spacing when set to HALF" }
---

# LOOP LENGTH — half vs full (V1-length loops)

## Concept
Cut the Micro-Looper's loop length in half relative to the CLOCK setting to match the original MOOD's shorter loops. The MkII doubled loop length; this hidden option returns to the V1 response for workflows that prefer the tighter, shorter micro-loop. Set with the looper **MODE** toggle inside the hidden menu: **LEFT** = HALF length (V1 response), other position = FULL (the MkII default). Loop length is otherwise still governed by CLOCK position.

## How to play it
1. Hold **both footswitches** until the LEDs go green (hidden-options mode).
2. Flip the **looper MODE toggle** to the **LEFT** to halve loop length (FULL is the MkII default).
3. Exit the hidden menu.
4. Set **CLOCK** to govern absolute loop length as usual — now at half the MkII spacing for tighter V1-style micro-loops.

## Notes
- Exists specifically so V1 owners can recover the original shorter loop feel if the doubled length doesn't suit their workflow.
- Pairs with **Classic Mode** for a faithful V1 micro-looper feel.
- Saves per-preset like all hidden options.
- This is a binary hidden toggle (HALF vs FULL) rather than a continuous knob value — no numeric settings are involved, so nothing here is an unsourced dial position.

## Sources
- gear/Chase Bliss MOOD MkII/research/transcripts/chasebliss-mood-mkii-video-manual-pt2.md (Micro-Looper MODE toggle → cut loop length in half, flip left)
- gear/Chase Bliss MOOD MkII/research/transcripts/youtube-mood-mkii-hidden-options-dip-walkthrough.md (7. LOOP LENGTH half/full)
- gear/Chase Bliss MOOD MkII/research/links/chasebliss-setting-the-mood-tips-page.md (LOOP LENGTH option exists to go back to original shorter length)
- gear/Chase Bliss MOOD MkII/research/links/mood-mkii-official-manual-try-this-recipes.md (LOOP LENGTH half/full, manual pp.14–17)
- factory hidden option (official video manual pt.2 + official tips page + community walkthrough; manual pp.14–17)
