---
type: patch
title: Extract Slice to Own Pad
device: Akai MPC Sample
date: 2026-06-14
description: Freeing one chop slice for independent tune/filter/re-chop — the no-Convert workaround around the single-kit limitation.
tags: [sampling, chop, extract, workaround, factory]
controls:
  - { name: "Extract (in Chop, Shift)", type: button, value: "select slice → Shift → Extract → lands on first available pad" }
  - { name: "Independent edit", type: knob, value: "tune freely or chop it again" }
  - { name: "Slot/Bank", type: knob, value: "First free pad" }
---

# Extract Slice to Own Pad

## Concept
Freeing one slice for independent tune/filter/re-chop — the manual route around the single-kit / no-auto-Convert limitation. There is NO chop→kit "Convert" on the AC50 (that's a full-MPC feature, Akai-support confirmed), so Extract is how you give a slice its own independent sample to work on.

## How to play it
1. In Chop, select the slice → `Shift` → Extract → it lands on the first available pad as an independent sample.
2. Tune it freely or chop it again.

## Notes
- Factory feature; the no-Convert limitation is Akai-support confirmed.
- This is the manual route around the single-kit / no-auto-Convert limitation.

## Sources
- 🟢 `research/transcripts/akaipro-mpc-sample-chop-mode.md` + `research/links/akai-support-chop-to-kit-convert-transfer-caveat.md`
- Transformed from Pedalxly MPC-Sample-Patches.md (factory)
