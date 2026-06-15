---
type: patch
title: "DRY KILL — wet-only output / volume-as-swell"
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: "Remove the clean signal entirely so MOOD's output is 100% wet and MIX becomes a wet 0–100 fader — with DRY KILL on, MIX all the way down is silence and rolling MIX up swells in pure wet/loop texture. Useful for parallel-FX-loop use and volume-swell-style wet-only entrances, but a surprising silence trap live. A factory dip-switch feature documented in the official video manual pt.2 + community walkthrough + manual p.44."
tags: [dip, dry-kill, wet-only, swell, parallel, factory, technique]
dips:
  DRY KILL: on
controls:
  - { name: "DRY KILL (dip switch)", type: switch, value: "on", options: ["on", "off"] }
  - { name: "MIX (blend knob)", type: knob, value: "becomes a wet-only fader — 0 = silence, 100 = full wet/loop; no published value, set to taste" }
  - { name: "Wet / Looper mode", type: switch, value: "any wet/loop texture — DRY KILL works with any mode" }
---

# DRY KILL — wet-only output / volume-as-swell

## Concept
Flip the **DRY KILL** dip on and MOOD's clean signal is pulled out of the output entirely, so what you hear is **100% wet**. That re-purposes the **MIX** knob: instead of blending dry↔wet it becomes a pure wet **0–100 fader**. All the way down is *silence* (there's no dry to fall back on); rolling it up swells in nothing but wet/loop texture. Great for running MOOD in a parallel FX loop, or for volume-swell-style wet-only entrances — but it's a surprising silence trap on stage, so know it's on before you commit. Exact knob positions aren't published; treat MIX as a dialable wet level rather than a fixed value.

## How to play it
1. Flick the **DRY KILL** dip on.
2. Set up any wet/loop texture (any Wet or Looper mode works).
3. Use **MIX** as a wet-only fader: all the way down = silence; roll up to swell pure wet/loop in.
4. Reach for it when MOOD lives in a parallel FX loop, or when you want only the effect with no dry blend.

## Notes
- ⚠️ With DRY KILL on and **MIX** down you get **silence** — there's no dry signal to fall back on. Surprising live; re-check before a performance.
- DRY KILL removes the clean signal **even when bypassed** (per the spec sheet).
- Turns **MIX** from a dry↔wet blend into a pure wet level control.
- **No published knob values** — MIX is a dialable wet-only recipe (0 = silence, up = more wet), not a fixed setting.

## Sources
- gear/Chase Bliss MOOD MkII/research/transcripts/youtube-mood-mkii-hidden-options-dip-walkthrough.md (DRY KILL — "takes out your dry signal… your MIX just becomes a wet 0 to 100"; with dry killed + MIX down "you're hearing nothing")
- gear/Chase Bliss MOOD MkII/research/transcripts/chasebliss-mood-mkii-video-manual-pt2.md (DRY KILL — removes clean signal from output)
- gear/Chase Bliss MOOD MkII/research/links/community-mood-mkii-pitfalls-and-gotchas.md (DRY KILL turns MIX into wet-only 0–100; MIX down = silence)
- gear/Chase Bliss MOOD MkII/research/MOOD-MkII-DeepResearch.md §2 (DRY KILL removes clean signal even when bypassed)
- Chase Bliss MOOD MkII manual, "Customize" p.44 (DRY KILL) — chasebliss.com
