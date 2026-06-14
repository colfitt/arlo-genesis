---
type: patch
title: Wide White 24-String (jangle double)
device: Roland VG-800
date: 2026-06-14
description: Doubled jangly 12-string-into-tape template; CTL-1 toggles 12-string ↔ normal 6-string.
tags: [acoustic, 12-string, jangle, tape-source, factory, signature]
controls:
  - { name: "INST TYPE", type: switch, value: "E.GUITAR (or ACOUSTIC)" }
  - { name: "12STR SW", type: switch, value: "ON, assigned to CTL-1 (toggle 12 ↔ 6)", options: ["ON", "OFF"] }
  - { name: "12STR TYPE", type: switch, value: "NORMAL" }
  - { name: "12STR PITCH", type: knob, value: "per-string octave/+12 on the lower courses (doubled shimmer)" }
  - { name: "12STR DELAY", type: knob, value: "small per-string (chorus-y spread)" }
  - { name: "CTL-1", type: button, value: "toggles 12STR SW (12 ↔ 6 string)" }
  - { name: "Slot/Bank", type: knob, value: "Factory bank" }
---

# Wide White 24-String (jangle double)

## Concept

A doubled jangly 12-string-into-tape template — SoS calls it "24-String Guitar — a really attractive jangle," Juca "Wide White 12-String — CTL-1 toggles 12-string and normal 6-string." The `12STR PITCH` per-string set to octave/+12 on the lower courses makes the "doubled" shimmer; a small per-string `12STR DELAY` gives the chorus-y spread. The alt-tuned-12-string → tape-degrade template.

## How to play it

1. Set `INST TYPE = E.GUITAR` (or ACOUSTIC).
2. `12STR SW = ON` assigned to CTL-1 (toggle 12 ↔ 6).
3. `12STR TYPE = NORMAL`; set `12STR PITCH` per-string at octave/+12 on the lower courses for the doubled shimmer.
4. `12STR DELAY` small per-string for the chorus-y spread.

## Notes

- Named factory preset (SoS + Juca call it "24th string" / "Wide White 12-String"), now parametrized via the 12STR PITCH/DELAY block.

## Sources

- 🟢 `research/links/soundonsound-vg800-factory-banks.md` (https://www.soundonsound.com/reviews/boss-vg-800) + `research/transcripts/juca-nery-creative-tool-patch-tour.md`; 12STR params from parameter-guide-alt-tuning-values.md
- Transformed from Pedalxly VG-800-Patches.md (factory)
