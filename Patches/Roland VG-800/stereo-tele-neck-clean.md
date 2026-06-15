---
type: patch
title: "Stereo Telecaster Clean — neck-pickup stereo clean"
device: Roland VG-800
date: 2026-06-15
description: "The factory stereo Telecaster (neck-pickup) clean Marcus Curtis tours — a bright, spanky Tele neck voice spread to stereo. A clean modeled-electric source with that single-coil chime, useful as a present clean bed or doubled across the stereo split. Factory preset (named, no published values) — dialable recipe."
tags: [clean, stereo, factory, telecaster, tape-source]
dips:
  "DIV/DUAL": "stereo spread"
  "OUTPUT SELECT": "stereo, or R/MONO for a mono front-chain"
controls:
  - { name: "INST TYPE", type: switch, value: "E.GUITAR — TELE model, neck-pickup position, spread to stereo (dial from recipe — no published values)" }
  - { name: "Pickup position", type: switch, value: "neck", options: ["neck", "middle", "bridge"] }
  - { name: "DIV/DUAL", type: switch, value: "DUAL — spread the model across the stereo path" }
  - { name: "NORMAL MIX", type: knob, value: "low (let the model's single-coil chime dominate)" }
  - { name: "OUTPUT SELECT", type: switch, value: "stereo, or R/MONO for a mono front-chain", options: ["stereo", "R/MONO"] }
  - { name: "Slot/Bank", type: knob, value: "Factory bank (\"Stereo Telecaster clean (neck pickup)\")" }
---

# Stereo Telecaster Clean — neck-pickup stereo clean

## Concept

The factory stereo Telecaster (neck-pickup) clean Marcus Curtis tours — a bright, spanky Tele neck voice spread to stereo. `INST = E.GUITAR` set to the TELE model in the neck-pickup position, spread across the stereo path for width. A clean modeled-electric source with that single-coil chime, useful as a present clean bed or doubled across the stereo split.

## How to play it

1. Recall the factory stereo Tele clean memory (or set `INST = E.GUITAR`, `TYPE = Tele`, neck pickup).
2. Spread across the stereo path (`DIV/DUAL`) for width.
3. Keep it bright and present; `NORMAL MIX` low so the model's chime dominates.
4. Clean into the tape stage, or doubled across CE-2W → Deco V2 for stereo width.

## Notes

- Named factory behavior (Marcus Curtis: "Stereo Telecaster clean (neck pickup)"). Tele is in the E.GUITAR model list (Parameter Guide); reviewers say the Tele/Strat models "seemed better than ever."
- Honesty: single-coil models can sound quieter/cleaner than the real thing because the hex pickup rejects hum (Sound on Sound). Exact values not published — dial from the memory.
- Note: the GK-5 won't fit traditional Tele bridges — but here the source is the Jazzmaster/banjo modeling a Tele, so it's irrelevant.
- ⚠ Recipe, not capture: every value above is a dialable starting point. Recall the factory memory and tweak to taste.

## Sources

- 🟢 `research/transcripts/marcus-curtis-setup-and-demo.md` ("Stereo Telecaster clean (neck pickup)")
- `research/VG-800-DeepResearch.md` §2/§3 (E.GUITAR list incl. Tele; single-coil quieter via hex)
