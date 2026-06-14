---
type: patch
title: Slip as Real-Time Reverse / Harmonizer
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: Real-time reverse and pitch-stepped harmonies under sustained playing — TIME sets sampling size, MODIFY sets playback speed/direction in semitone steps (CCW = reverse). (The Unperson / Ali)
tags: [slip, reverse, harmonizer, pitch, factory, signature]
dips:
  CLASSIC: off (add for aliased/uneven crunch)
controls:
  - { name: "Wet MODE", type: switch, value: "Slip", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Wet TIME", type: knob, value: "sampling size — LOW = instant pitch-shifter-like, HIGH = harmonized phrases that follow behind you" }
  - { name: "Wet MODIFY", type: knob, value: "playback speed/direction in semitone steps — CCW of noon = REVERSE, noon = neutral, CW = forward (up to 2x each way)" }
---

# Slip as Real-Time Reverse / Harmonizer

## Concept
Slip gives real-time reverse and pitch-stepped harmonies under sustained playing. **TIME = sampling size**: LOW is near-instant and pitch-shifter-like; HIGH produces harmonized phrases that follow behind you. **MODIFY = playback speed/direction in semitone steps**: CCW of noon = REVERSE, noon = neutral, CW = forward, up to 2× each way. "A common use is real-time reverse."

## How to play it
1. Set Wet MODE = **Slip**.
2. Set TIME for the sampling size: low for instant reverse/pitch-shift on each note, high for trailing reversed phrases.
3. Move MODIFY in semitone steps — left of noon for reverse, right for forward harmonies, up to 2× each direction.
4. Play sustained notes and let the harmonized/reversed voices follow.

## Notes
- The Unperson confirms MODIFY-left = reverse.
- Add **CLASSIC** for an aliased/uneven crunch on the Slip voices.

## Sources
- manual pp.26–27 "Slip Mode"; chasebliss-mood-mkii-video-manual-pt1.md; unperson-mood-mkii-reverb-delay-looper.md
- Ref: The Unperson (Ali)
- Transformed from Pedalxly MOOD-MkII-Patches.md (factory/artist)
