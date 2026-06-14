---
type: patch
title: Tape-Saturated Reverb Tail (Flint -> Deco)
device: Strymon Deco V2
date: 2026-06-14
description: Running a long reverb/Flint hall INTO the Deco so the tail itself gets tape-saturated and widened — a concrete ambient/wash recipe for the texture board (the one patch that wants the Deco AFTER a reverb, not on the dry source).
tags: [ambient, reverb, wash, stereo, texture, factory, signature]
hidden:
  Wide Stereo Mode: on (Live-Edit on WOBBLE; needs stereo out)
controls:
  - { name: "Tape Saturation", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "Doubletracker", type: switch, value: "ON (Wide Stereo)", options: ["ON","OFF"] }
  - { name: "Saturation", type: knob, value: "~11-12:00 (saturate the tail without crushing the swell)" }
  - { name: "Voice", type: switch, value: "classic (cassette for a more lo-fi wash)", options: ["classic","cassette"] }
  - { name: "Tone", type: knob, value: "~10-11:00 (dark, so the wash stays warm)" }
  - { name: "Lag Time", type: knob, value: "~12:00" }
  - { name: "Blend", type: knob, value: "~11:00" }
  - { name: "Wobble", type: knob, value: "~10:00 (gentle drift on the tail)" }
  - { name: "Volume", type: knob, value: "unity" }
  - { name: "Slot/Bank", type: knob, value: "PC20" }
---

# Tape-Saturated Reverb Tail (Flint -> Deco)

## Concept
Run a long reverb / Flint or Big Sky hall INTO the Deco so the tail itself gets tape-saturated and widened — a concrete ambient/wash recipe for the texture board. This is the one patch that wants the Deco AFTER a reverb, not on the dry source. Superdanger's documented move: Flint hall → Deco → Wide Stereo yields a saturated, widened wash.

## How to play it
1. Feed the Deco a Flint / Big Sky hall upstream.
2. Engage Tape Saturation and Doubletracker (Wide Stereo).
3. Saturation ~11–12:00 (saturate the tail without crushing the swell), Voice classic (cassette for a more lo-fi wash), Tone ~10–11:00 (dark, so the wash stays warm).
4. Enable Wide Stereo Mode: hold Tape Saturation ON, turn WOBBLE right of 12:00 (needs stereo out).
5. Lag Time ~12:00, Blend ~11:00, Wobble ~10:00 (gentle drift on the tail), Volume unity.

## Notes
- Distinct from the front-of-chain patches by routing, not knobs — the Deco sits after the reverb here.
- The exact clock-faces are a completion of the named technique (the source gives routing + intent, not numbers).
- Needs stereo out for Wide Stereo Mode.

## Sources
- transcripts/superdanger-one-pedal-endless-tone-deco-v2.md ("Flint hall → Deco, then Wide Stereo")
- UsageGuide §3/§5 (Reverb/Flint INTO the Deco — tape-saturate a long reverb tail)
- Ref: Superdanger Studios "One Pedal, Endless Tone" (gxS7ueTq6_I)
- Transformed from Pedalxly Deco-V2-Patches.md (factory/artist)
