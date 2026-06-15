---
type: patch
title: 'Fat Distorted Bass — "unbelievably fat" octave-down grind'
device: Roland VG-800
date: 2026-06-15
description: Banjo or a 6-string guitar turned into a huge distorted electric bass — a review standout MusicRadar calls a "distorted bass sound that''s unbelievably fat." Drop the modeled tuning into bass range and push the drive for a synth-bass wall, distinct from the clean upright/fretless voice.
tags: [bass, distortion, fat, octave, riff, textural]
dips:
  ALT TUNE: "-12 STEP lowers ALL strings an octave; calibrate low strings (lower SENS, higher DISTANCE) so the drop tracks clean"
  OUTPUT SELECT: "LINE/PHONES"
controls:
  - { name: "INST TYPE", type: switch, value: "E.BASS model (or a guitar model dropped into bass range)" }
  - { name: "ALT TUNE", type: switch, value: "-12 STEP (all strings down an octave); or per-string PITCH" }
  - { name: "OD/DS", type: switch, value: "overdrive or distortion model after the instrument (dial drive from recipe — no published value)" }
  - { name: "COMP", type: switch, value: "ON (for sustain)" }
  - { name: "EQ / TONE", type: knob, value: "keep mids present so the fuzz stays defined (dial from recipe — no published value)" }
  - { name: "Mode", type: switch, value: "BASS mode (separate 150-memory set)", options: ["GUITAR", "BASS"] }
---

# Fat Distorted Bass — "unbelievably fat" octave-down grind

## Concept

Turn the banjo or a 6-string guitar into a huge distorted electric bass — a review standout MusicRadar calls a "distorted bass sound that's unbelievably fat." Drop the modeled tuning into bass range and push the drive for a synth-bass wall, distinct from the clean upright/fretless bass voice. `INST TYPE = E.BASS` for the core model; octave-down via `ALT TUNE -12 STEP` or per-string `PITCH`; an overdrive/distortion model after, with `COMP` for sustain; keep mids present so the grind stays defined, not woolly.

## How to play it

1. Select an E.BASS model (or drop a guitar model into bass range with `ALT TUNE -12 STEP` / per-string `PITCH`).
2. Add overdrive or distortion after the model and a compressor for sustain.
3. Keep mids up so the fuzz stays defined, not woolly.
4. Double riffs or carry the low end solo; into the rig's fuzz it becomes a synth-bass wall.

## Notes

- Review-cited tone: MusicRadar praises the "unbelievably fat" distorted bass; the repo DeepResearch §3 echoes it.
- Per-string / global pitch shifting keeps the drop-tuned bass tracking tight (smooth per-string pitch engine).
- Distinct from Standup / Fretless Bass (that's the clean upright/fretless voice).
- Exact drive/EQ values are **not published** — dial those from the recipe (verify by ear). `ALT TUNE -12 STEP` is manual-verified as the all-string octave drop.

## Sources

- 🟢 review-cited tone: [MusicRadar](https://www.musicradar.com/guitars/guitar-pedals/boss-vg-800-v-guitar-processor) ("distorted bass sound that's unbelievably fat")
- [Boss VG-800 product page](https://www.boss.info/global/products/vg-800/) (bass mode: electric/acoustic/dual/VIO bass)
- `research/VG-800-DeepResearch.md` §3 (distorted bass "unbelievably fat")
- `ALT TUNE -12 STEP` verified in `research/links/parameter-guide-alt-tuning-values.md` (−12..+12 STEP lowers/raises all strings)
