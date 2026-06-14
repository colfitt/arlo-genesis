---
type: patch
title: Resample-Through-the-Pedalboard Re-amp Loop (feedback-safe)
device: Elektron Digitakt 2
date: 2026-06-14
description: Run a DT2 track out through the texture boards (Microcosm / H90 / Chroma) and resample it back — the "recorded-wrong" finish through real pedals, with the feedback fixes.
tags: [resample, re-amp, routing, recorded-wrong, community, signature]
controls:
  - { name: "Fix 1 — AUDIO ROUTING", type: switch, value: "Turn OFF 'TO MAIN' for the source so it isn't re-sent out the mains (sample the returning processed signal blind)", options: ["TO MAIN ON","TO MAIN OFF"] }
  - { name: "Fix 2 — external mixer", type: switch, value: "Small mixer between DT2 and pedals for monitoring (cleanest)" }
  - { name: "Fix 3 — USB/Overbridge loop", type: switch, value: "Remove tracks from Main Out, pull audio out over USB, add FX, send back over USB, sample from USB with monitor ON (feedback-free)" }
  - { name: "Fix 4 — looper-as-FX-hub", type: switch, value: "DT → RC-505 → pedals → mixer → DT inputs, looper as MIDI clock master" }
  - { name: "Selective USB output", type: switch, value: "Route only specific track(s) out for external processing" }
  - { name: "Input gain", type: knob, value: "DT input attenuates ≈ −12 dB then normalizes to 0 dB after recording; avoid boost-heavy pedals; lower input in the mixer if needed" }
---

# Resample-Through-the-Pedalboard Re-amp Loop (feedback-safe)

## Concept
The "recorded-wrong" finish through real pedals: run a DT2 track out through the texture boards (Microcosm / H90 / Chroma) and resample the processed signal back in. The catch is feedback — with input monitoring ON the signal you sample also goes out the Main Outs. This patch documents the four feedback fixes plus the gain notes so the re-amp-through-the-board workflow stays clean.

## How to play it
1. Problem: with input monitoring ON, the signal you sample also goes out the Main Outs → feedback. Fixes:
2. (1) In AUDIO ROUTING turn OFF "TO MAIN" for the source so it isn't re-sent out the mains — sample the returning processed signal blind.
3. (2) Put a small external mixer between DT2 and pedals for monitoring (cleanest).
4. (3) USB/Overbridge loop: remove tracks from Main Out, pull audio out over USB, add FX, send back over USB, sample from USB with monitor ON (feedback-free).
5. (4) Looper-as-FX-hub: DT → RC-505 → pedals → mixer → DT inputs, looper as MIDI clock master.
6. Selective USB output: route only specific track(s) out for external processing.
7. Gain: DT input attenuates ≈ −12 dB then normalizes to 0 dB after recording; avoid boost-heavy pedals; lower input in the mixer if needed.

## Notes
- Feedback mechanism + gain notes are OG-origin but apply identically to the DT2's analog I/O; the DT2's selective USB output makes fix #3 cleaner.
- Directly serves the rig's re-amp-through-the-board workflow. Capture to a resample track.

## Sources
- `research/links/elektronauts-dt2-resampling-through-fx.md` (t/213230)
- `research/links/elektronauts-dt2-overlooked-features.md` (t/213177)
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
