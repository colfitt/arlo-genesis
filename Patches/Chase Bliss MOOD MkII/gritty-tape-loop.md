---
type: patch
title: Gritty Tape Loop
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: Grit and vibe in a tape-style micro-loop — combine a slower CLOCK with a faster octave-quantized playback speed; add CLASSIC for deteriorating MkI loops.
tags: [tape, looper, degrade, lofi, factory, signature]
dips:
  CLASSIC: off (add for deteriorating MkI loops)
controls:
  - { name: "Looper MODE", type: switch, value: "Tape", options: ["Env", "Tape", "Stretch"] }
  - { name: "CLOCK", type: knob, value: "slower (combine with faster playback speed)" }
  - { name: "Looper MODIFY", type: knob, value: "octave-quantized playback speed — .5x / 1x / 2x / 4x, forward or reversed (toward 2x/4x)" }
  - { name: "Looper LENGTH", type: knob, value: "shortens the slice CCW" }
---

# Gritty Tape Loop

## Concept
Grit and vibe in a tape-style micro-loop. Combine a **slower CLOCK** with a **faster playback speed** (MODIFY toward 2×/4×). MODIFY is octave-quantized: **.5× / 1× / 2× / 4×**, forward or reversed. LENGTH shortens the slice CCW. The slow clock degrades the loop while the fast playback keeps it moving.

## How to play it
1. Set Looper MODE = **Tape**.
2. Lower **CLOCK** to introduce grit.
3. Push **MODIFY** toward 2×/4× (octave-quantized) for faster playback.
4. Set **LENGTH** for the slice size (CCW shortens it).

## Notes
- Add **CLASSIC** for deteriorating MkI loops. Heavily cited across the notes.
- The inverse trick (slow CLOCK + raise MODIFY back to recorded speed) is Balance Beam (balance-beam-tape-loop).

## Sources
- manual pp.32–33 "Tape Mode"; chasebliss-mood-mkii-video-manual-pt1.md; mood-mkii-recipe-sources-and-shared-settings.md
- Transformed from Pedalxly MOOD-MkII-Patches.md (factory)
