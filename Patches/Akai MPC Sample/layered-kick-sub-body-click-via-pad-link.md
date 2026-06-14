---
type: patch
title: Layered Kick — Sub-Body + Click via Pad Link
device: Akai MPC Sample
date: 2026-06-14
description: A fat, full-range kick built from two samples living in different frequency bands, linked so one strike fires both, then resampled into one tight one-shot.
tags: [drum-craft, kick, layering, pad-link, designed]
controls:
  - { name: "Pad A Filter", type: switch, value: "LPF2", options: ["LPF2", "LPF4", "HPF2", "HPF4", "BPF"] }
  - { name: "Pad A Cutoff", type: knob, value: "~50–60 (of 127, sub/body only)" }
  - { name: "Pad A Tune", type: knob, value: "to song key" }
  - { name: "Pad A Amp Decay", type: knob, value: "medium" }
  - { name: "Pad B Filter", type: switch, value: "HPF2", options: ["LPF2", "LPF4", "HPF2", "HPF4", "BPF"] }
  - { name: "Pad B Cutoff", type: knob, value: "~70–90 (of 127, attack/click only)" }
  - { name: "Pad B Amp Attack", type: knob, value: "0" }
  - { name: "Pad B Amp Decay", type: knob, value: "very short" }
  - { name: "Pad Link (Tune pg, Shift+K2)", type: knob, value: "Pad A → B's pad number" }
  - { name: "Per-pad Volume", type: knob, value: "−INF…+6 dB (even the two layers)" }
  - { name: "Resample (Pad 11)", type: button, value: "Bake the pair into one one-shot" }
  - { name: "Slot/Bank", type: knob, value: "Two linked pads → resampled to one free pad" }
---

# Layered Kick — Sub-Body + Click via Pad Link

## Concept
A fat, full-range kick built from two samples in different frequency bands: a sub/body layer (low-passed) and a click/top layer (high-passed). Pad Link is the AC50's only layering route (no keygroups), so one strike fires both pads. Resample-to-one is the AC50-specific commit step that frees the linked pad and allows further chop/tune.

## How to play it
1. Pad A = sub/body kick: Filter LPF2, Cutoff ~50–60 (of 127) to keep only the low end; tune to song key; medium Amp Decay.
2. Pad B (same bank) = click/top: Filter HPF2, Cutoff ~70–90 to keep only the attack; Amp Attack=0, very short Decay.
3. Link them: on Pad A, Tune page → `Shift+K2` Pad Link = B's pad number so one strike fires both.
4. Even the levels with per-pad Volume (−INF…+6 dB) so the layers don't cancel.
5. Resample (Pad 11) the pair into one tight one-shot to free the linked pad and allow further chop/tune.

## Notes
- Pad Link is the AC50's only layering route (no keygroups).
- Frequency-band split = a general layering principle; resample-to-one is the AC50-specific commit step.

## Sources
- 🟣 designed from `research/links/manual-fx-parameter-reference-knob-fx-color-vintage.md` (Pad Link + Filter, UG v1.3 p.28-29) + `research/links/craft-punchy-drum-samples-on-the-ac50.md`
- Transformed from Pedalxly MPC-Sample-Patches.md (designed)
