---
type: patch
title: SOLO Lead Synth (sustained banjo line)
device: Roland VG-800
date: 2026-06-14
description: Banjo-as-lead mono synth line with long sustain that survives the banjo's fast decay — into a smear reverb or the fuzz.
tags: [synth-lead, banjo, sustain, factory, signature]
controls:
  - { name: "INST TYPE", type: switch, value: "SYNTH" }
  - { name: "SYNTH TYPE", type: switch, value: "SOLO" }
  - { name: "FILTER CUTOFF", type: knob, value: "100 (setup), then back down to ~70" }
  - { name: "FILTER RESO", type: knob, value: "0" }
  - { name: "TOUCH SENS", type: knob, value: "0 (setup), then ~50 for pick-responsive filter" }
  - { name: "COLOR", type: knob, value: "~40–60 (raise while playing until voiced)" }
  - { name: "SUSTAIN", type: knob, value: "80–100 (the banjo-decay fix — larger = longer sustain)" }
  - { name: "NORMAL MIX", type: knob, value: "low" }
  - { name: "Slot/Bank", type: knob, value: "User Memory (guitar mode), e.g. U01-2" }
---

# SOLO Lead Synth (sustained banjo line)

## Concept

A banjo-as-lead mono synth line with long sustain that survives the banjo's fast decay — into a smear reverb or the fuzz. The setup follows the manual's verbatim procedure: zero the filter and touch, raise `COLOR` until voiced, push `SUSTAIN` high, then dial the filter back for pick response. High `SUSTAIN` is the banjo-decay fix.

## How to play it

1. Recall the EBM5 BANJO GK profile. Set `INST TYPE = SYNTH`, `SYNTH TYPE = SOLO`.
2. Manual's verbatim setup: `FILTER CUTOFF = 100`, `FILTER RESO = 0`, `TOUCH SENS = 0`.
3. Raise `COLOR` while playing until the voice is right (~40–60).
4. `SUSTAIN = 80–100` (larger values = longer sustain — the banjo-decay fix).
5. Back `FILTER CUTOFF` down to ~70 and add `TOUCH SENS ~50` for a pick-responsive filter.
6. Keep `NORMAL MIX` low.

## Notes

- The CUTOFF-100 / RESO-0 / TOUCH-0-then-COLOR-up setup is the manual's own procedure (factory-grade).
- Pair with a `SLOW GEAR` FX to remove the pick attack for a violin-swell drone.

## Sources

- 🟢 SOLO params + verbatim MEMO from `research/links/parameter-guide-synth-engine-values.md` (https://www.manualslib.com/manual/3657983/Roland-Boss-Vg-800.html)
- Transformed from Pedalxly VG-800-Patches.md (factory)
