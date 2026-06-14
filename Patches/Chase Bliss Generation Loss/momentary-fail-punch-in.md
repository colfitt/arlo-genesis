---
type: patch
title: Momentary FAIL Punch-In
device: Chase Bliss Generation Loss
date: 2026-06-14
description: An instant dropout/snag chaos burst on demand over an otherwise-stable tone — a performance accent the Big Time catches.
tags: [chaos, glitch, momentary, performance, factory, signature]
hidden:
  Aux Onset (Wow knob): abrupt (CCW) vs fade (CW)
controls:
  - { name: "Aux", type: switch, value: "Fail", options: ["Stop", "Filter", "Fail"] }
  - { name: "Model", type: knob, value: "run any base patch (e.g. #1 or #3)" }
  - { name: "Left footswitch (Aux)", type: button, value: "tap = latch the chaos, hold = momentary burst then release" }
---

# Momentary FAIL Punch-In

## Concept
An instant dropout/snag chaos burst on demand over an otherwise-stable tone — a performance accent the Big Time catches. The non-repeatable randomness is the point: fire it as punctuation, not a sustained tone.

## How to play it
1. Run any base patch (e.g. "Subtle Tape Age" #1 or "Dying Cassette" #3) in the live/center preset position.
2. Set the **Aux toggle = Fail**.
3. **Tap** the left footswitch to latch the chaos, or **hold** for a momentary burst that releases when you let go.
4. Set hidden **Aux Onset** (the Wow knob in the hidden menu) for abrupt (CCW) vs faded (CW) onset.

## Notes
- The MIDI/aux jack takes an external momentary for hands-free firing.
- Keep it as an accent over a stable base — sitting on it just makes mush.

## Sources
- 🟢 `research/links/genloss-aux-freeze-classic-trick.md` (CB official + manual) + UsageGuide §5.
- Transformed from Pedalxly Generation-Loss-Patches.md (factory/artist provenance).
