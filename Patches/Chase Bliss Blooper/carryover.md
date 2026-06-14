---
type: patch
title: Carryover
device: Chase Bliss Blooper
date: 2026-06-14
description: Turn a built-up multi-layer loop into a retriggerable sample alongside the OP-1/Octatrack — build in NORM/ADD, then switch to SAMP and trigger with effects applied.
tags: [technique, sampler, samp-mode, performance, factory, signature]
controls:
  - { name: "Mode", type: switch, value: "NORM or ADD (build) → SAMP (perform)", options: ["NORM", "ADD", "SAMP"] }
  - { name: "RIGHT footswitch", type: button, value: "triggers; hold RIGHT toggles loop vs one-shot (right LED green = one-shot)" }
  - { name: "LEFT footswitch", type: button, value: "DO NOT tap in SAMP — instantly wipes everything" }
  - { name: "MOD A", type: knob, value: "modifiers + Stability still work in SAMP (e.g. Trimmer so just a sliver plays per trigger)" }
  - { name: "Slot/Bank", type: knob, value: "mode toggle NORM/ADD → SAMP · save the built wall to a MIDI PC slot before performing" }
---

# Carryover

## Concept

Turn a built-up multi-layer loop into a retriggerable sample alongside the OP-1/Octatrack (benches the CB Onward). Build a complex loop in NORM or ADD, then switch to SAMP — the loop carries over and becomes triggerable, with effects still applied (which is unique to Blooper).

## How to play it

1. Build a complex multi-layer loop in NORM or ADD first.
2. Switch the mode toggle to SAMP — the loop carries over.
3. Trigger with the RIGHT footswitch; hold RIGHT to toggle loop vs one-shot (right LED green = one-shot).
4. Modifiers and Stability still work in SAMP — e.g. set Trimmer so just a sliver plays per trigger.

## Notes

- WARNING: Do NOT tap the RECORD (LEFT) footswitch in SAMP — it instantly wipes everything.
- The bridge that lets a Blooper wall become a triggerable sample with the hardware samplers.
- Save the built wall to a MIDI PC slot before performing.

## Sources

- `research/transcripts/knobs-better-bloops-sampler-mode.md`
- Transformed from Pedalxly Blooper-Patches.md (factory/artist)
