---
type: patch
title: Shimmer Pad
device: Chase Bliss MOOD MkII
date: 2026-06-10
description: Ethereal shimmer pad — lush reverb wash with octave-up micro-loop feeding back through it. Hold the Wet footswitch to freeze into a sustained, shimmering bed and play over the top.
tags: [ambient, pad, shimmer, drone]
dips:
  MISO: off
  SPREAD: on
  DRY KILL: off
  TRAILS: on
  LATCH: off
  NO DUB: off
  SMOOTH: on
  CLASSIC: off
hidden:
  TONE (Wet MODIFY): 1:00 (roll off highs slightly to keep shimmer from getting brittle)
  STEREO WIDTH (Wet TIME): 2:00 (wide)
  LEVEL BALANCE (CLOCK): noon (even)
controls:
  - { name: "MIX", type: knob, value: "2:00" }
  - { name: "CLOCK", type: knob, value: "2:00" }
  - { name: "Wet TIME", type: knob, value: "3:00" }
  - { name: "Wet MODIFY", type: knob, value: "2:00" }
  - { name: "Wet MODE", type: switch, value: "Reverb", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Looper LENGTH", type: knob, value: "1:00" }
  - { name: "Looper MODIFY", type: knob, value: "2x (octave up)" }
  - { name: "Looper MODE", type: switch, value: "Tape", options: ["Env", "Tape", "Stretch"] }
  - { name: "ROUTING", type: switch, value: "IN+micro-loop", options: ["IN", "IN+micro-loop", "micro-loop only"] }
---

# Shimmer Pad

## Concept

Classic shimmer effect built from two MOOD channels working together: the **Reverb** provides a long, washed-out pad, and the **Tape micro-looper at 2x speed (octave up)** adds the bright, crystalline shimmer overtone. Routing is set to `IN+micro-loop` so the Wet reverb processes both your dry signal and the octave-up loop together, creating the feedback-shimmer illusion.

## How to play it

1. **Engage both channels.** Play a chord or sustained note — the Micro-Looper captures it and plays it back an octave up, which feeds into the Reverb wash.
2. **Hold the LEFT footswitch** to freeze the reverb into an infinite shimmering pad.
3. **Play over the frozen bed** — new notes add fresh shimmer layers on top.
4. **For evolving texture**, hold the RIGHT footswitch to overdub new material into the micro-loop while frozen.

## Notes

- **CLOCK at 2:00** keeps it clean and hi-fi — shimmer wants clarity, not grit. Drop to noon if you want a darker, degraded shimmer.
- **SMOOTH dip on** so Clock sweeps don't step audibly if you adjust live.
- **SPREAD on** scatters the reverb taps across the stereo field for width. Note that Blooper downstream will collapse this to mono — this patch is best heard through the H90/Chroma Console path or on headphones.
- **TRAILS on** so the shimmer pad sustains when you bypass.
- **Hidden TONE rolled to 1:00** tames any ice-pick frequencies from the octave-up content.
- Tape MODIFY is set to the 2x detent (one click CW of noon) for a clean octave-up. Push to 4x for a more extreme, synth-like two-octave shimmer.

## Sources

- Reverb + Tape mode pairing per Perry Frank's drone cookbook (perry-frank-ambient-drone-howto)
- Freeze/hold technique per official video manual (video-manual-pt1)
- Hidden TONE and SPREAD behavior per usage guide (MOOD-MkII-UsageGuide.md)
- Routing and channel interaction per deep research (MOOD-MkII-DeepResearch.md)
