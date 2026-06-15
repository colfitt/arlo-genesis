---
type: patch
title: "Dimension — virtual-analog clean pad bed"
device: TE OP-1 Field
date: 2026-06-15
description: "The Field-exclusive Dimension engine is a proper subtractive/virtual-analog synth the original OP-1 never had — the one to reach for to build a USABLE clean bed. Slow-attack pad with built-in stereo chorus width, kept clean on Studio tape so the rig's pedals (or later tape passes) can wreck it. Engine + encoder roles documented (ADG walkthrough, magazinmehatronika review); artist-validated by Andreas Roman across a full Field album."
tags: [pad, ambient, clean, dimension, virtual-analog, field-exclusive, signature]
dips:
  FX_PAIRING: "Mother reverb (TE's intended Dimension pairing)"
controls:
  - { name: "Engine", type: switch, value: "Dimension (Field-only)" }
  - { name: "BLUE (waveform blend)", type: knob, value: "saw/square-leaning for a full pad", options: ["noise","pulse","square","saw","sub-saw"] }
  - { name: "GOLD/OCHRE (stereo width / built-in chorus)", type: knob, value: "up for wide stereo" }
  - { name: "Filter cutoff", type: knob, value: "rolled back" }
  - { name: "Resonance", type: knob, value: "low-to-moderate" }
  - { name: "T2 envelope — Blue (Attack)", type: knob, value: "high (slow bloom)" }
  - { name: "T2 envelope — Orange (Release)", type: knob, value: "high (long tail)" }
  - { name: "FX", type: switch, value: "Mother reverb (Distance high)" }
---

# Dimension — virtual-analog clean pad bed

## Concept

The Field-exclusive **Dimension** engine is a proper subtractive / virtual-analog synth the original OP-1 never had — described as "quintessentially retro, plush virtual analog." It's the one to reach for to build a USABLE clean bed: a slow-attack pad with built-in stereo chorus width, kept clean on Studio tape so the rig's pedals (or later tape passes) can wreck it. The same engine is equally happy as soaring leads and huge basses.

## How to play it

1. Select the **Dimension** engine (`[Shift]+T1`).
2. Set **BLUE** (waveform blend) toward saw/square for a full pad; raise **GOLD/OCHRE** for stereo width (built-in chorus).
3. **T2 envelope:** Attack (Blue) high, Release (Orange) high — slow bloom, long tail.
4. Roll the **cutoff** back and add a touch of **resonance** (low-to-moderate).
5. Send to **Mother reverb** (Distance high); record a clean take to Studio tape, then OP-1 Out → EHX Effects Interface → Board 1 to wreck it.

## Notes

- **No published values** — Field-exclusive engine; the encoder/param roles are documented (ADG, review) but the exact knob positions are method-level. Treat the control block as a dialable recipe, not sourced settings.
- Described as "quintessentially retro, plush virtual analog" — also strong for soaring leads and huge basses, not just pads.
- TE pairs Dimension with the new Mother reverb in its own materials; that's the intended on-board FX for this voice.
- Andreas Roman leaned on Dimension across a full Field album (artist-validated workflow).

## Sources

- Gear/TE OP-1 Field/research/transcripts/adg-op1-field-full-walkthrough-for-owners.md (§DIMENSION synth)
- Gear/TE OP-1 Field/research/OP-1-Field-DeepResearch.md §3 (Dimension), §13c
- Gear/TE OP-1 Field/research/links/cdm-op1-field-album-workflow.md (Andreas Roman — Dimension)
- magazinmehatronika.com/en/op-1-field-review/ (Dimension: wave/stereo/cutoff/resonance, "plush virtual analog")
- teenage.engineering/products/op-1 (Dimension listed as new Field engine)
