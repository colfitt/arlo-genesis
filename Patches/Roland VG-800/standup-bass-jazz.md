---
type: patch
title: "Standup / Fretless Bass — upright and fretless bass models"
device: Roland VG-800
date: 2026-06-15
description: 'The VG-800''s bass models Marcus Curtis tours — a standup (upright) bass and a fretless bass, off the banjo or baritone via GK-5. Clean, these give the rig a convincing acoustic-bass / fretless-bass low end for jazz, dub, or sub-octave roots. (For the distorted, "unbelievably fat" version see Fat Distorted Bass.)'
tags: [bass, fretless, jazz, factory, textural]
dips:
  MODE: "BASS MODE (separate bank/menus) for dedicated bass, or AC BASS / E.BASS in GUITAR mode"
  OUTPUT SELECT: "LINE/PHONES"
controls:
  - { name: "Mode", type: switch, value: "GUITAR mode (AC BASS / E.BASS) or BASS mode (separate bank/menus)", options: ["GUITAR", "BASS"] }
  - { name: "INST TYPE", type: switch, value: "AC BASS (upright/standup) or E.BASS → FRETLESS" }
  - { name: "E.BASS model", type: switch, value: "FRETLESS (recipe — dial by ear)", options: ["Jazz", "Precision", "StingRay", "Rickenbacker", "Thunderbird", "Höfner violin", "fretless"] }
  - { name: "EQ", type: knob, value: "dial from recipe — no published values" }
  - { name: "OUTPUT SELECT", type: switch, value: "LINE/PHONES", options: ["LINE", "PHONES"] }
  - { name: "Slot/Bank", type: knob, value: "Factory bass memory (standup or fretless)" }
---

# Standup / Fretless Bass — upright and fretless bass models

## Concept

The VG-800's bass models Marcus Curtis tours — a standup (upright) bass and a fretless bass, off the banjo or baritone via GK-5. Clean, these give the rig a convincing acoustic-bass / fretless-bass low end for jazz, dub, or sub-octave roots ("Fretless bass, standup bass — lots of basses" — Marcus Curtis). `INST TYPE = AC BASS` gives the upright/standup; `E.BASS → FRETLESS` gives the fretless model. (For the distorted, "unbelievably fat" version see Fat Distorted Bass.)

## How to play it

1. Recall a factory bass memory (standup or fretless), or set `INST = AC BASS` for upright / `E.BASS → FRETLESS`.
2. Calibrate the low strings carefully (lower SENS, higher DISTANCE) — single-note tracking is essentially flawless, polyphonic gets "wacky" high up (Gear Sounds).
3. Play single-note walking/dub lines for the most convincing result.
4. Distorted, it gets "unbelievably fat" (MusicRadar) — drive it into the fuzz for a synth-bass wall.

## Notes

- Named models (Marcus Curtis: "Fretless bass, standup bass — lots of basses"; Juca Nery: "Razor Bass"). The E.BASS/AC BASS model lists are manual-verified.
- Honesty: monophonic bass tracking is praised; polyphonic playing high on the neck is the weak spot. Exact knob values not published — dial the EQ/model by ear (recipe only).

## Sources

- 🟢 `research/transcripts/marcus-curtis-setup-and-demo.md` ("Fretless bass, standup bass — lots of basses")
- 🟢 `research/transcripts/gear-sounds-full-tutorial.md` (electric bass model: monophonic flawless, polyphonic "wacky" high up)
- 🟢 `research/VG-800-DeepResearch.md` §2/§3 (E.BASS/AC BASS lists; distorted bass "unbelievably fat")
- Transformed from Pedalxly VG-800-Patches.md (factory / named models — no published knob values)
