---
type: patch
title: "Nashville High-Strung Sparkle — octave-up low courses"
device: Roland VG-800
date: 2026-06-15
description: "A Nashville (high-strung) tuning on a steel-string acoustic or chimey clean model — the lower four strings raised an octave for a bright, jangly 12-string-like shimmer that layers beautifully with a standard guitar, switchable per-patch with no physical retuning. NASHVL is a named ALT TUNE TYPE (Boss and MusicRadar both cite Nashville among the instant per-patch tunings); tuning is source-verified, tone values are a dialable recipe — no published values."
tags: [nashville, high-strung, jangle, acoustic, sparkle, alternate-tuning]
dips:
  ADJACENT MEMORY: "keep standard tuning for instant switching"
controls:
  - { name: "INST TYPE", type: switch, value: "ACOUSTIC (steel-string) or clean E.GUITAR", options: ["ACOUSTIC", "E.GUITAR"] }
  - { name: "ALT TUNE SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "ALT TUNE TYPE", type: switch, value: "NASHVL (or USER with low four strings PITCH = +12)", options: ["NASHVL", "USER", "..."] }
  - { name: "USER PITCH 1/2/3/4", type: knob, value: "+12 (octave-up on E/A/D/G) — only if building it in USER mode", options: ["-24…+24"] }
  - { name: "COMP", type: knob, value: "light (dial from recipe — no published values)" }
  - { name: "REVERB", type: knob, value: "light, for sparkle (dial from recipe — no published values)" }
  - { name: "NORMAL MIX", type: knob, value: "low (keep the modeled jangle forward)" }
---

# Nashville High-Strung Sparkle — octave-up low courses

## Concept

Set a Nashville (high-strung) tuning on a steel-string or chimey clean model — the lower four strings raised an octave for a bright, jangly 12-string-like shimmer that layers beautifully with a standard guitar, switchable per-patch with no physical retuning. There's no existing Nashville patch in the corpus. `ALT TUNE TYPE = NASHVL` is the manual's named Nashville tuning; or build it in `USER` mode with `PITCH 1/2/3/4 = +12` (octave-up on E/A/D/G). Light compression and reverb add the sparkle. Per-string octave-up is exactly how high-strung tuning works.

## How to play it

1. Select a steel-string acoustic or chimey clean electric model (`INST TYPE = ACOUSTIC` or `E.GUITAR`).
2. `ALT TUNE SW = ON`, `ALT TUNE TYPE = NASHVL` (or `USER` with the low four strings `PITCH = +12`).
3. Add light `COMP` and `REVERB` for sparkle.
4. Layer with a standard-tuned guitar (Dual mode) for a faux 12-string.
5. Strum open chords for instant jangle.
6. Keep standard tuning on the adjacent memory for instant per-patch switching.

## Notes

- `NASHVL` is a named `ALT TUNE TYPE` in the control schema / Parameter Guide; Boss and MusicRadar both cite Nashville among the instant per-patch tunings.
- Per-string octave-up is exactly how high-strung tuning works; combine with the Wide 12-String model patch for big acoustic layers.
- Tone values (`COMP`, `REVERB`, `NORMAL MIX`) are **not published** — they're a dial-by-ear recipe, not sourced values. The tuning itself is source/manual-verified.
- Provenance: factory-feature recipe — named NASHVL tuning (tuning sourced/manual-verified; tone values dialable).

## Sources

- 🟢 `research/links/parameter-guide-alt-tuning-values.md` (ALT TUNE TYPE incl. NASHVL; USER per-string PITCH ±24)
- 🟢 [Exploring the Advanced Features of the Boss V-Guitar System](https://articles.boss.info/exploring-the-advanced-features-of-the-boss-v-guitar-system/) (Nashville among named alt tunings)
- 🟢 [MusicRadar — Boss VG-800 V-Guitar Processor](https://www.musicradar.com/guitars/guitar-pedals/boss-vg-800-v-guitar-processor) (jangly Nashville tuning)
- 🟢 `research/transcripts/premier-guitar-namm-2025.md` (Nashville named among per-string alt tunings)
