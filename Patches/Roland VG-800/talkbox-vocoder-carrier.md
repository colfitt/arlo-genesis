---
type: patch
title: Talkbox/Vocoder Carrier (filter-modulated synth)
device: Roland VG-800
date: 2026-06-14
description: INDEX-ONLY / APPROXIMATE Daft Punk talkbox vocal — the VG-800 has no vocoder/talkbox, so this only mimics the result via rhythmic filter modulation.
tags: [synth, daft-punk, electronic, talkbox, approximate, designed]
controls:
  - { name: "INST TYPE", type: switch, value: "SYNTH (saw / GR-300 as the CARRIER)" }
  - { name: "FILTER CUTOFF", type: knob, value: "driven by a sequenced CC from the 61SL/Digitakt (CONTROL ASSIGN, CC#1–31 window) — opens/closes rhythmically in time" }
  - { name: "ALT TUNE HARMONY / 12-STRING", type: switch, value: "optional (adds a harmonizer-choir flavor)" }
  - { name: "Slot/Bank", type: knob, value: "User Memory (guitar mode), VG-E3" }
---

# Talkbox/Vocoder Carrier (filter-modulated synth)

## Concept

INDEX-ONLY / APPROXIMATE: the Daft Punk talkbox vocal. The VG-800 has no vocoder/talkbox — this only mimics the result via rhythmic filter modulation (Daft Punk talkbox vocal, "Around the World" Juno-106 + tube). A SYNTH carrier whose `FILTER CUTOFF` is driven rhythmically by a sequenced CC reads as an envelope/filter robot voice, not a bank-of-bandpass vocoder. Reproduces the result, not the method.

## How to play it

1. Set `INST TYPE = SYNTH` (saw / GR-300) as the CARRIER.
2. Have the 61SL/Digitakt send a sequenced CC to the VG `FILTER CUTOFF` (`CONTROL ASSIGN`, CC#1–31 window) so the filter opens and closes rhythmically in time with a phrase = an envelope/filter robot voice, not a bank-of-bandpass vocoder.
3. The VG `ALT TUNE HARMONY` / `12-STRING` blocks add a harmonizer-choir flavor.

## Notes

- 🟣 INDEX-ONLY, APPROXIMATE — no tube, no mouth-formant, no true vocoder. Filter-CC fake only. Flagged.

## Sources

- 🟣 designed; `Research/Taste-Profile/sources/daft-punk-talkbox-vocoder-per-song-bjango.md`
- Ref: Daft Punk talkbox vocal ("Around the World" Juno-106 + tube)
- Transformed from Pedalxly VG-800-Patches.md (DOUG-designed)
