---
type: patch
title: Doom Baritone Wall (−7 STEP)
device: Roland VG-800
date: 2026-06-14
description: Banjo or Baritone JM dropped subterranean for a sustained doom/sludge wall into the fuzz section — the core low-wall signature.
tags: [doom, sludge, baritone, alt-tuning, fuzz, designed, signature]
controls:
  - { name: "INST TYPE", type: switch, value: "E.GUITAR (LP or ES-335 model, dark)" }
  - { name: "ALT TUNE SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "ALT TUNE MODE", type: switch, value: "ALT TUNE", options: ["ALT TUNE", "HARMONY"] }
  - { name: "ALT TUNE TYPE", type: switch, value: "-7 STEP (down a 5th; -5 for a 4th, -12 for an octave)" }
  - { name: "AMP1", type: switch, value: "dark / mid-forward (treble pulled)" }
  - { name: "NORMAL MIX", type: knob, value: "~30% (keeps real attack / Jazzmaster body / banjo 5th drone under the model)" }
  - { name: "DIV MODE", type: switch, value: "DUAL (optional: clean low strings, dirty-ready high strings)", options: ["SINGLE", "DUAL"] }
  - { name: "Slot/Bank", type: knob, value: "User Memory (guitar mode), e.g. U03-1" }
---

# Doom Baritone Wall (−7 STEP)

## Concept

Banjo or Baritone JM dropped subterranean for a sustained doom/sludge wall into the fuzz section — the core low-wall signature. `ALT TUNE TYPE = -7 STEP` lowers ALL strings down a 5th (the doom transposer); a dark, mid-forward `E.GUITAR` model with treble pulled keeps it from getting brittle. `NORMAL MIX ~30%` keeps the real attack, the Jazzmaster body, and the banjo's 5th drone under the model.

## How to play it

1. Set `INST TYPE = E.GUITAR` (LP or ES-335 model, dark).
2. `ALT TUNE SW = ON`, `ALT TUNE MODE = ALT TUNE`, `ALT TUNE TYPE = -7 STEP` (use `-5` for a 4th, `-12` for an octave).
3. Choose a dark / mid-forward `AMP1` with the treble pulled.
4. `NORMAL MIX ~30%` to keep the real attack / body / 5th drone under the model.
5. Optional `DIV MODE = DUAL`: clean model on the low strings, dirty-ready model on the high strings.
6. Onboard REV/DLY off; back gain off downstream (the wall already saturates).
7. Into MXR 108 → Hizumitas (Tone 1–2:00 to tame brightness) → Longsword.

## Notes

- `-STEP` tuning is manual-verified as the all-string transposer (the doom transposer); the rig-specific numbers are designed.

## Sources

- 🟣 designed; `ALT TUNE -12/+12 STEP` verified in `research/links/parameter-guide-alt-tuning-values.md`; recipe = UsageGuide §3a / DeepResearch §13b
- Transformed from Pedalxly VG-800-Patches.md (DOUG-designed)
