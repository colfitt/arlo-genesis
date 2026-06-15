---
type: patch
title: "Wide 12-String — stereo modeled 12-string"
device: Roland VG-800
date: 2026-06-15
description: "The factory wide stereo 12-string preset Marcus Curtis (a 12-string owner) calls \"really sounds pretty good\" — the 12STR simulator spread across the stereo path for a big, jangly chime that rings \"really nice\" with no latency (reviewers). The classic source for the rig's tape-degrade stage, distinct from the Wide White 24-String doubled-jangle preset."
tags: [12-string, jangle, stereo, factory, tape-source, signature]
dips:
  OUTPUT: "stereo (both L+R direct), or R/MONO for the mono front-chain"
  ROUTING: "DIV/DUAL for the stereo spread; small 12STR DELAY for shimmer"
controls:
  - { name: "INST TYPE", type: switch, value: "E.GUITAR or ACOUSTIC", options: ["E.GUITAR", "ACOUSTIC"] }
  - { name: "12STR SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "12STR PITCH", type: knob, value: "octave on the lower courses, unison on the top two (authentic 12-string voicing); range ±24" }
  - { name: "12STR LEVEL", type: knob, value: "dial from recipe — no published values; range 0–100" }
  - { name: "12STR DELAY", type: knob, value: "small per-string for jangle (dial from recipe — no published values); range 0–100 ms" }
  - { name: "NORMAL MIX", type: knob, value: "low (let the modeled 12-string sparkle dominate)" }
  - { name: "Slot/Bank", type: knob, value: "Factory bank (wide 12-string memory)" }
---

# Wide 12-String — stereo modeled 12-string

## Concept

The factory wide stereo 12-string preset Marcus Curtis (a 12-string owner) calls "really sounds pretty good" — the `12STR` simulator spread across the stereo path for a big, jangly chime that rings "really nice" with no latency (reviewers). `12STR SW = ON` with small per-string `12STR DELAY` supplies the jangle; `12STR PITCH` adds octave strings to the lower courses and unison to the top two for an authentic 12-string voicing. The classic source for the rig's tape-degrade stage, distinct from the Wide White 24-String doubled-jangle preset.

## How to play it

1. Recall the factory wide 12-string memory, or build: `12STR SW = ON` with small per-string `12STR DELAY` for jangle.
2. Use `12STR PITCH` to add octave strings to the lower courses and unison to the top two for an authentic 12-string voicing.
3. Spread the two voices across the stereo path for width; keep it pristine and bright, `NORMAL MIX` low.
4. Clean → Generation Loss → JHS 424 / PORTA424 to degrade, or direct-to-Apollo for the stereo chime.

## Notes

- Named factory preset (Marcus Curtis: "Wide 12-string — stereo 12-string, really sounds pretty good"). 12-string sims are a reviewer-praised strength — good enough for QOTSA jangle (MusicRadar), ring "really nice" with best-in-class pitch tracking (Sound on Sound).
- Distinct from the existing Wide White 24-String (that's the doubled-jangle, CTL-1-toggle preset).
- ⚠ Exact 12STR factory values are **not published** — `12STR LEVEL` and `12STR DELAY` above are a dialable recipe, not captured settings. Recall the factory memory and tweak to taste. The `12STR SW/PITCH/LEVEL/DELAY` mechanism and ranges are manual-verified.

## Sources

- 🟢 `research/transcripts/marcus-curtis-setup-and-demo.md` ("Wide 12-string — stereo 12-string")
- 🟢 `research/links/parameter-guide-alt-tuning-values.md` (12STR SW/PITCH/LEVEL/DELAY ranges)
- `research/VG-800-DeepResearch.md` §3 (12-string sims a standout; QOTSA jangle)
- https://www.soundonsound.com/reviews/boss-vg-800 (12-string rings "really nice", best VG pitch tracking)
- https://www.musicradar.com/guitars/guitar-pedals/boss-vg-800-v-guitar-processor (12-string + octave/unison string config)
