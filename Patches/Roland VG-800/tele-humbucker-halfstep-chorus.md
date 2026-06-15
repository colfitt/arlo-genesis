---
type: patch
title: "Tele + Neck Humbucker, Half-Step Down, Stereo Chorus"
device: Roland VG-800
date: 2026-06-15
description: "An audiochronicle review patch: a Telecaster body with a neck-humbucker voicing, tuned a half-step down, into a JC-120-style clean with stereo chorus — a lush, slightly dark clean rhythm voice. A specific reviewer combo distinct from the bright neck-single-coil Stereo Telecaster Clean."
tags: [telecaster, humbucker, clean, chorus, stereo, half-step-down]
dips:
  ALT TUNE: "-1 STEP lowers all strings a half step (manual-verified STEP range)."
  OUTPUT SELECT: "JC-120 return, or LINE/PHONES with a clean amp model."
controls:
  - { name: "INST TYPE", type: switch, value: "E.GUITAR → TELE model, neck-humbucker pickup voicing" }
  - { name: "ALT TUNE SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "ALT TUNE TYPE", type: switch, value: "-1 STEP (half-step down), or USER PITCH -1 on all strings" }
  - { name: "AMP", type: switch, value: "JC-120-style clean amp model (dial from recipe — no published values)" }
  - { name: "CHORUS", type: switch, value: "ON (stereo)", options: ["ON", "OFF"] }
  - { name: "OUTPUT SELECT", type: switch, value: "JC-120 return, or LINE/PHONES with a clean amp model", options: ["LINE/PHONES", "GUITAR AMP"] }
  - { name: "NORMAL MIX", type: knob, value: "low (dial by ear — no published value)" }
---

# Tele + Neck Humbucker, Half-Step Down, Stereo Chorus

## Concept

An audiochronicle hands-on patch: a Telecaster body with a neck-humbucker voicing, tuned a half-step down, into a JC-120-style clean with stereo chorus — a lush, slightly dark clean rhythm voice. `INST = E.GUITAR → TELE` with the pickup set to a neck-humbucker voicing, `ALT TUNE TYPE = -1 STEP` (half-step down, no physical retuning), into a JC-120-style clean amp model with stereo chorus for width. A specific reviewer combo, distinct from the bright neck-single-coil Stereo Telecaster Clean.

## How to play it

1. Choose the `TELE` model under `INST = E.GUITAR` and set the pickup to a neck-humbucker voicing.
2. Set the tuning a half-step down: `ALT TUNE SW = ON`, `ALT TUNE TYPE = -1 STEP` (or `USER PITCH = -1` on all strings).
3. Run into a JC-120-style clean amp model (`OUTPUT SELECT = JC-120` return, or `LINE/PHONES` with a clean amp model).
4. Add stereo chorus for width.
5. Use for dark-clean rhythm and arpeggios; the half-step-down is per-patch — no physical retuning.

## Notes

- A specific instrument/tuning/amp/effect combo described in an audiochronicle hands-on. The `TELE` model and pickup-position/resonance params are repo-verified; the `-1 STEP` half-step-down and the stereo chorus are sourced.
- Distinct from "Stereo Telecaster Clean" — that's a bright neck single-coil with no detune; this is a darker neck-humbucker voice tuned down a half step.
- ⚠ Recipe, not capture: exact mix/level values are not published — `NORMAL MIX` and chorus depth/rate are dialable starting points. Dial by ear.

## Sources

- 🟢 https://www.audiochronicle.com/articles/boss-vg-800-review-a-virtual-guitar-rig-that-actually-feels-alive (Tele + neck humbucker, half-step down, JC-120 + stereo chorus)
- 🟢 `research/links/parameter-guide-alt-tuning-values.md` (-12..+12 STEP per-half-step; USER per-string PITCH)
- 🟢 `research/VG-800-DeepResearch.md` §2 (E.GUITAR list incl. Tele; pickup-position params)
