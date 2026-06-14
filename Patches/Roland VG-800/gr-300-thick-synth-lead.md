---
type: patch
title: GR-300 Thick-Synth Lead
device: Roland VG-800
date: 2026-06-14
description: Banjo via GK-5 as a SOLO/poly synth LEAD that artifacts gloriously through the fuzz wall — the box's signature voice in the Pat-Metheny GR-300 lineage (heritage only, not an endorser).
tags: [synth-lead, banjo, gr-300, fuzz, factory, signature]
controls:
  - { name: "INST TYPE", type: switch, value: "SYNTH" }
  - { name: "SYNTH TYPE", type: switch, value: "GR-300" }
  - { name: "MODE", type: switch, value: "V+D (hexa-VCO + hexa-distortion)", options: ["V", "D", "V+D"] }
  - { name: "DUET SW", type: switch, value: "ON (adds same-pitch sawtooth = richer)", options: ["ON", "OFF"] }
  - { name: "PITCH SW", type: switch, value: "A", options: ["A", "B"] }
  - { name: "PITCH A", type: knob, value: "+12 (or +7 for a 5th / +5 for a 4th — manual's thick-synth tip)" }
  - { name: "FINE A", type: knob, value: "+5 (skew for depth)" }
  - { name: "COMP SW", type: switch, value: "ON (extends hexa-VCO decay — the banjo fast-decay fix)", options: ["ON", "OFF"] }
  - { name: "ENV MOD SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "ENV MOD SENS", type: knob, value: "~60" }
  - { name: "ENV MOD ATTACK", type: knob, value: "~20 (pick-triggered wah)" }
  - { name: "CUTOFF", type: knob, value: "~60" }
  - { name: "RESONANCE", type: knob, value: "~40" }
  - { name: "NORMAL MIX", type: knob, value: "low (let the model dominate the banjo attack)" }
  - { name: "Slot/Bank", type: knob, value: "User Memory (guitar mode), e.g. U01-1" }
---

# GR-300 Thick-Synth Lead

## Concept

Banjo via GK-5 as a SOLO/poly synth LEAD that artifacts gloriously through the fuzz wall — the box's signature voice, in the Pat-Metheny GR-300 lineage (heritage only, not an endorser). `MODE = V+D` runs the hexa-VCO plus hexa-distortion together; `DUET SW = ON` adds a same-pitch sawtooth for a richer voice; `PITCH +12` (or +7 / +5) with a `FINE +5` skew gives the thick detuned depth. `COMP SW = ON` extends the hexa-VCO decay — the fix for the banjo's fast decay. Poly chords through the Muff are a feature.

## How to play it

1. Recall the EBM5 BANJO GK profile first.
2. Set `INST TYPE = SYNTH`, `SYNTH TYPE = GR-300`, `MODE = V+D`.
3. `DUET SW = ON`, `PITCH SW = A`, `PITCH A = +12` (or `+7` for a 5th / `+5` for a 4th), `FINE A = +5`.
4. `COMP SW = ON` to extend the decay so the synth survives the banjo's fast attack.
5. `ENV MOD SW = ON`, `ENV MOD SENS ~60`, `ENV MOD ATTACK ~20` for a pick-triggered wah; set `CUTOFF ~60`, `RESONANCE ~40`.
6. Keep `NORMAL MIX` low so the model dominates the banjo attack. Onboard REV/DLY off.
7. Run into MXR 108 → Hizumitas → Longsword — poly chords through the Muff = a feature.

## Notes

- The `PITCH +12/+7/+5` + `FINE ±5` + `COMP SW ON` recipe is the manual's own verbatim MEMO (factory-grade). The `ENV/CUTOFF` values are designed starting points.

## Sources

- 🟢 mechanism + MEMO from `research/links/parameter-guide-synth-engine-values.md` (https://www.manualslib.com/manual/3657983/Roland-Boss-Vg-800.html); build order `research/transcripts/gear-sounds-how-to-create-patch.md`
- Ref: GR-300 lineage (heritage, not an endorser)
- Transformed from Pedalxly VG-800-Patches.md (factory)
