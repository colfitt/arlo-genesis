---
type: patch
title: "Raw Model FX-Bypass Retune — pure alt-tuned source into the wall"
device: Roland VG-800
date: 2026-06-15
description: "The manufacturer's own stated use case (Premier Guitar NAMM interview): bypass every amp/effect and use the unit purely to retune the guitar before feeding the rest of your rig. Use the VG-800 as a retuner/instrument-model source only — engage FX BYPASS with [▲]+[CTL 1] so you hear just the raw INST model into the downstream fuzz wall."
tags: [alt-tuning, clean, performance, tape-source, signature]
dips:
  OUTPUT SELECT: "LINE/PHONES, R/MONO for mono into Board 1"
  FX BYPASS: "[▲]+[CTL 1]"
  TUNER: "[▼]+[▲]"
controls:
  - { name: "INST", type: switch, value: "the model you want — dial from recipe, no published value", options: ["E.GUITAR", "ACOUSTIC", "SYNTH"] }
  - { name: "ALT TUNE SW", type: switch, value: "ON to the target tuning (e.g. Open D, or -5 STEP)" }
  - { name: "FX BYPASS", type: switch, value: "engaged via [▲]+[CTL 1] — hear only the raw INST model, no amp/FX" }
  - { name: "NORMAL MIX", type: knob, value: "to taste — no FX values to set, it's the bypass path" }
---

# Raw Model FX-Bypass Retune — pure alt-tuned source into the wall

## Concept

Use the VG-800 purely as a retuner/instrument-model source with every amp/effect bypassed ([▲]+[CTL 1] FX BYPASS), feeding the raw model straight into the downstream fuzz wall. The manufacturer's own stated use case ("bypass every amp/effect and use the unit purely to retune") — the cleanest front-of-rig move for this board. This is the architectural backbone of the rig: raw model → fuzz wall, with the VG-800 doing only retuning/modeling and the downstream pedals doing all the dirt, time, and space.

## How to play it

1. Pick the INST model and ALT TUNE you want (e.g. ACOUSTIC + Open D, or E.GUITAR + −5 STEP).
2. Engage FX BYPASS with [▲]+[CTL 1] so you hear only the raw modeled/retuned instrument — no VG-800 amp or effects.
3. Feed the raw model into Polytune → CB Clean → the fuzz/tape chain; let the downstream pedals do all the dirt and time/space.
4. Use [▼]+[▲] for the tuner before playing.

## Notes

- Manufacturer-stated use case: Premier Guitar NAMM interview — "press two buttons together to bypass every amp/effect and use the unit purely to retune the guitar before feeding the rest of your rig." This is the [▲]+[CTL 1] FX BYPASS.
- This is the architectural backbone for the whole rig (raw model → fuzz wall) — a performance/routing patch, not a tone recipe.
- ⚠ No knob values to publish. INST model and ALT TUNE target are a dialable recipe; NORMAL MIX is to taste. The value here is the routing (FX BYPASS into the front of the board), not captured settings.

## Sources

- 🟢 `research/transcripts/premier-guitar-namm-2025.md` (all-effects bypass = retune-only into your rig)
- 🟢 `research/VG-800-DeepResearch.md` §2 ([▲]+[CTL 1] = FX BYPASS)
- `research/links/vguitarforums-gotchas-output-modes.md` (LINE/PHONES into a pedal front-end)
