---
type: patch
title: "Polyharmonic in E Minor — in-key poly harmonizer"
device: Roland VG-800
date: 2026-06-15
description: "The factory \"Polyharmonic in E minor\" preset Juca Nery tours — ALT TUNE HARMONY mode stacks an in-key diatonic harmony voice on every note, with CTL-1 adding distortion, turning single lines into harmonized leads without a second player. Forum users specifically praise the poly harmonizer."
tags: [harmony, alt-tuning, factory, lead, performance]
dips:
  KEY: "E minor (set in the MST/MASTER block so the harmony stays in-key)"
  CTL-1: "distortion on (factory convention)"
controls:
  - { name: "ALT TUNE SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "ALT TUNE MODE", type: switch, value: "HARMONY", options: ["ALT TUNE", "HARMONY"] }
  - { name: "HARMONY", type: knob, value: "diatonic interval (e.g. +3rd or +5th above; dial from recipe — no published value)" }
  - { name: "KEY", type: knob, value: "E minor (MASTER/MST block KEY field)" }
  - { name: "CTL-1", type: switch, value: "distortion ON" }
  - { name: "Slot/Bank", type: knob, value: "Factory memory \"Polyharmonic in E minor\"" }
---

# Polyharmonic in E Minor — in-key poly harmonizer

## Concept

The factory "Polyharmonic in E minor" preset Juca Nery tours — `ALT TUNE MODE = HARMONY` generating an in-key diatonic harmony voice stacked on every note, with `CTL-1` adding distortion. A self-harmonizing electric that thickens single lines into harmonized leads without a second player. Forum users specifically praise the poly harmonizer as a strong point of the box.

## How to play it

1. Recall the factory "Polyharmonic in E minor" memory.
2. Confirm `ALT TUNE MODE = HARMONY` with the `KEY` set to E minor (the MASTER/MST `KEY` field).
3. Choose the harmony interval (diatonic, e.g. `+3rd` or `+5th` per the HARMONY table).
4. Play single lines; `CTL-1` adds distortion for a harmonized lead. The harmony voice tracks the set key automatically.

## Notes

- Named factory preset; `HARMONY` mode + the `KEY` field are manual-verified (Parameter Guide; KEY lives in the MASTER block per Gear Sounds). `CTL-1 = distortion` is documented behavior. Forum impressions praise the poly harmonizer.
- Distinct from the existing banjo harmony-drone patches (those are banjo-source designed drones); this is the factory poly-harmonizer template in E minor.
- Exact harmony interval and amp model are **not published** — dial from the factory memory. Treat the interval value above as a dialable recipe, not a sourced setting.

## Sources

- 🟢 `research/transcripts/juca-nery-creative-tool-patch-tour.md` ("Polyharmonic in E minor (CTL-1 = distortion)")
- 🟢 `research/links/parameter-guide-alt-tuning-values.md` (HARMONY mode + USER SCALE, manual-verified)
- 🟢 `research/transcripts/gear-sounds-full-tutorial.md` (KEY field in MST page for pitch effects)
- 🟢 https://www.boss.info/global/products/vg-800/ (auto/poly harmony: set key + interval)
- 🟣 https://www.vguitarforums.com/smf/index.php?topic=38100.125 (forum praise for the poly harmonizer)
