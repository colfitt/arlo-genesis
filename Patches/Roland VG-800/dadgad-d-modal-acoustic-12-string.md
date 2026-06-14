---
type: patch
title: DADGAD / D-MODAL Acoustic 12-String
device: Roland VG-800
date: 2026-06-14
description: Pristine open-tuned 12-string acoustic to feed the tape stage (Generation Loss → JHS 424 / PORTA424) — the clean source the tape pedals want to ruin.
tags: [acoustic, 12-string, alt-tuning, tape-source, clean, factory, signature]
controls:
  - { name: "INST TYPE", type: switch, value: "ACOUSTIC (J-45 or D-28 model)" }
  - { name: "ALT TUNE SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "ALT TUNE TYPE", type: switch, value: "D-MODAL (drops 1st/2nd/6th a whole step = DADGAD-type; or OPEN D / OPEN G)" }
  - { name: "12STR SW", type: switch, value: "ON (assign toggle to CTL-1)", options: ["ON", "OFF"] }
  - { name: "12STR TYPE", type: switch, value: "NORMAL" }
  - { name: "12STR LEVEL", type: knob, value: "~70" }
  - { name: "12STR DELAY", type: knob, value: "~10–20 ms (per-string jangle/shimmer)" }
  - { name: "NORMAL MIX", type: knob, value: "low" }
  - { name: "CTL-1", type: button, value: "toggles 12STR SW" }
  - { name: "Slot/Bank", type: knob, value: "Factory DADGAD acoustic bank, or User Memory" }
---

# DADGAD / D-MODAL Acoustic 12-String

## Concept

A pristine open-tuned 12-string acoustic to feed the tape stage (Generation Loss → JHS 424 / PORTA424) — the clean source the tape pedals want to ruin. `ALT TUNE TYPE = D-MODAL` drops the 1st/2nd/6th a whole step (DADGAD-type), and the `12STR` block with a small per-string `12STR DELAY` supplies the jangle/shimmer. MusicRadar notes the 12-string sims nail QOTSA jangle.

## How to play it

1. Set `INST TYPE = ACOUSTIC` (J-45 or D-28 model).
2. `ALT TUNE SW = ON`, `ALT TUNE TYPE = D-MODAL` (or OPEN D / OPEN G).
3. `12STR SW = ON`, `12STR TYPE = NORMAL`, `12STR LEVEL ~70`, `12STR DELAY ~10–20 ms` for the per-string jangle/shimmer.
4. Keep it pristine — `NORMAL MIX` low, no dirt.
5. Assign the `12STR SW` toggle to CTL-1.

## Notes

- DADGAD acoustic is a real factory patch (Juca: "beautiful sounding, 12-string toggle"); the `12STR DELAY` ms-per-string is the jangle/shimmer mechanism (manual).
- See "DADGAD Acoustic (factory, behavior-only)" for the named factory anchor.

## Sources

- 🟢 D-MODAL + 12STR params from `research/links/parameter-guide-alt-tuning-values.md`; factory patch from `research/transcripts/juca-nery-creative-tool-patch-tour.md`
- Transformed from Pedalxly VG-800-Patches.md (factory)
