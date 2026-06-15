---
type: patch
title: "Freeze Double-Time x SYNC — looper + frozen-delay layers"
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: "Two synced loop layers running at once — capture a micro-loop with the Drolo Micro-Looper, then play into the Delay and HOLD the LEFT footswitch to freeze it into a secondary micro-loop. Vary Delay TIME for different secondary lengths and engage the hidden SYNC option so the frozen delay locks rhythmically to the loop length. From the official manual's 'Freeze Idea: Double Time' recipe (pp.22–23) plus the SYNC hidden option (p.17)."
tags: [delay, looper, freeze, sync, layers, factory, technique]
controls:
  - { name: "Looper MODE", type: switch, value: "Tape/Stretch — capture loop 1 first", options: ["Env", "Tape", "Stretch"] }
  - { name: "Wet MODE", type: switch, value: "Delay", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Wet TIME", type: knob, value: "delay length — vary for different secondary-loop lengths (dial from recipe)" }
  - { name: "Wet MODIFY", type: knob, value: "feedback (dial from recipe)" }
  - { name: "LEFT footswitch (Wet / freeze)", type: button, value: "HOLD to freeze the Delay into a second micro-loop" }
hidden:
  SYNC (Wet MODE toggle, RIGHT): Wet TIME steps related to loop length — locks the frozen delay rhythmically to the micro-loop
---

# Freeze Double-Time x SYNC — looper + frozen-delay layers

## Concept
Run **two independent loop layers simultaneously**: the Drolo Micro-Looper holds one captured loop while a **frozen Delay** holds a second, acting as a secondary micro-loop. Two clocks of repetition at once. What sets this apart from a plain double-time freeze is the **SYNC** hidden option — set it so the frozen delay's TIME steps relate to the loop length, locking the two layers rhythmically into one combined groove.

## How to play it
1. Capture a micro-loop with the **Micro-Looper** (Looper MODE = **Tape/Stretch**) — this is loop 1.
2. Set Wet MODE = **Delay**, play a phrase into it, then **HOLD the LEFT footswitch** to freeze the delay into a second loop.
3. Adjust **Delay TIME** to try different secondary-loop lengths.
4. In the hidden menu, set **SYNC** (Wet MODE toggle, RIGHT) so the frozen delay locks rhythmically to the micro-loop length — two synced loop layers.

## Notes
- The manual's "Freeze Idea: Double Time" explicitly suggests pairing with the **SYNC** hidden option — that combination is what this patch captures beyond the plain double-time freeze (see sibling patch freeze-idea-double-time).
- A frozen delay behaves as a **secondary micro-loop**, independent of the Micro-Looper channel.
- **No published knob values** — TIME, MODIFY, and the loop lengths are by feel / locked by SYNC. Treat the controls above as a dialable recipe, not sourced settings.

## Sources
- manual pp.22–23 "Freeze Idea: Double Time" ('Try experimenting with different delay lengths (TIME), as well as syncing (SYNC hidden option)… A frozen delay acts as a secondary micro-loop'); research/links/mood-mkii-official-manual-try-this-recipes.md (Recipe 4)
- SYNC hidden-option behavior: manual p.17; research/transcripts/chasebliss-mood-mkii-video-manual-pt2.md
- Chase Bliss MOOD MkII manual, "Wet Channel — Double Time" pp.22–23 + "Hidden Options — Sync" p.17 — chasebliss.com (factory)
