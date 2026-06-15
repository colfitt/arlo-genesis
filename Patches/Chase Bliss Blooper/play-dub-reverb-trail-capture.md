---
type: patch
title: "Reverb-Trail Capture — PLAY/DUB straight-to-dub"
device: Chase Bliss Blooper
date: 2026-06-15
description: "Set the PLAY/DUB dip so a finished initial recording drops straight into overdubbing the second layer instead of playback — ideal for capturing decaying reverb tails into the loop with no manual mode switch; the manual explicitly recommends this for ambient music (factory manual dip recipe)."
tags: [ambient, looper, reverb, dub, dip-switch, factory]
dips:
  PLAY/DUB: "DUB (straight-to-overdub after the first recording, instead of dropping into playback)"
controls:
  - { name: "Mode", type: switch, value: "NORM or ADD", options: ["NORM", "ADD", "SAMP"] }
  - { name: "LEFT footswitch", type: button, value: "tap to record initial loop; tap again to set endpoint — Blooper auto-continues into overdubbing the second layer; tap again to drop into playback" }
  - { name: "REPEATS", type: knob, value: "high for sustained layers — to taste, no published value" }
  - { name: "STABILITY", type: knob, value: "low for clean capture — to taste, no published value" }
---

# Reverb-Trail Capture — PLAY/DUB straight-to-dub

## Concept

Set the PLAY/DUB dip so a finished initial recording drops straight into overdubbing the second layer instead of playback. This is ideal for capturing ambient reverb trails: hit record, play a chord, and the decaying reverb tail keeps getting captured into the loop without a manual mode switch. The manual explicitly recommends this configuration for ambient music.

## How to play it

1. Set the PLAY/DUB dip to the Dub position (straight-to-overdub after the first recording).
2. Tap RECORD (LEFT footswitch) and play a sustained chord — ideally with an upstream reverb/pad feeding Blooper — then tap again to set the endpoint.
3. Blooper drops straight into overdubbing the second layer; the reverb trail keeps being captured seamlessly with no manual mode switch.
4. Build an ambient bed from decaying tails, then tap RECORD again to drop into playback when ready.

## Notes

- Dub mode is explicitly recommended in the manual for ambient music — it lets reverb trails be captured smoothly into the loop instead of cutting off at playback.
- Pairs with Andy Othling's momentary-record-a-reverb-sliver technique (distinct mechanism — SAMP-mode momentary record) and the existing Momentary-record patch.
- The PLAY/DUB dip is a fixed-setup decision, NOT MIDI-addressable / not a per-song recall.
- REPEATS/STABILITY are to taste — no published values; the load-bearing setting here is the dip.

## Sources

- `research/links/blooper-manual-named-patches-dip-recipes.md` (PLAY/DUB dip — straight-to-overdub for reverb-trail/ambient, manual pp.40-42)
- `research/Blooper-DeepResearch.md` §2 (PLAY/DUB straight-to-dub useful for ambient reverb-trail capture)
- Chase Bliss Blooper manual, dip switches > "Play / Dub" (squarespace PDF; ambient recommendation)
