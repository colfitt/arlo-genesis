---
type: patch
title: Slicer Rhythmic Glitch Texture
device: Roland VG-800
date: 2026-06-15
description: "Repo-verified SLICER FX on a clean/synth voice for stuttering, gated, industrial/IDM textures — hold a chord and let the tempo-synced Slicer chop it into rhythmic stabs. SLICER is repo-verified (Gear Sounds tutorial + BOSS article); pattern/depth values are dialed from recipe, no published values."
tags: [slicer, glitch, industrial, rhythmic, experimental, synth]
dips:
  SLICER PATTERN: "set to song tempo for locked stutter grooves"
  OUTPUT SELECT: "LINE/PHONES"
controls:
  - { name: "INST TYPE", type: switch, value: "E.GUITAR (clean) or SYNTH", options: ["E.GUITAR", "SYNTH"] }
  - { name: "SYNTH TYPE", type: switch, value: "GR-300 for aggressive lead-glitch hybrids (if SYNTH)", options: ["GR-300", "SOLO"] }
  - { name: "FX = SLICER", type: switch, value: "ON in an FX slot", options: ["ON", "OFF"] }
  - { name: "SLICER PATTERN", type: knob, value: "selectable rhythmic pattern, synced to tempo — dial from recipe (no published value)" }
  - { name: "SLICER DEPTH", type: knob, value: "dial from recipe — raise for harder gating (no published value)" }
  - { name: "DELAY / REVERB", type: knob, value: "add to taste" }
---

# Slicer Rhythmic Glitch Texture

## Concept

Use the VG-800's `SLICER` effect — selectable rhythmic patterns, tempo-syncable — on a clean or synth voice for stuttering, gated, industrial/IDM textures. Hold a chord and let the Slicer chop it into rhythmic stabs from the banjo or baritone source. The GR-300 synth voice pairs well for aggressive lead-glitch hybrids. SLICER itself is repo-verified ("SLICER with selectable patterns" in the Gear Sounds tutorial, and named officially among the FX in the BOSS article); the exact pattern/depth values are dialed by ear.

## How to play it

1. Pick a clean guitar (`INST TYPE = E.GUITAR`) or synth voice (`INST TYPE = SYNTH`; the GR-300 synth pairs well for aggressive lead-glitch hybrids).
2. Add the `SLICER` in an FX slot and choose a rhythmic pattern synced to tempo.
3. Add delay/reverb to taste.
4. Hold chords and let the Slicer chop them into rhythmic stabs.
5. For metallic clang on top, audition a ring-modulator FX if your firmware's FX list includes one (see Notes).

## Notes

- SLICER is repo-verified — "SLICER with selectable patterns" (Gear Sounds tutorial) and named officially among the FX (BOSS article). Great for industrial/IDM/experimental textures from a guitar.
- ⚠ Honesty: a Ring Modulator is mentioned only in a general "150+ FX" web review (Sound on Sound) and is NOT confirmed anywhere in the repo's FX lists — treat it as unverified/audition-on-the-unit, not a sourced VG-800 FX.
- ⚠ Recipe, not capture: pattern/depth values are not published — dial by ear. Set the Slicer pattern to the song tempo for locked stutter grooves.

## Sources

- 🟢 `research/transcripts/gear-sounds-full-tutorial.md` ("SLICER with selectable patterns")
- 🟢 `research/links/boss-article-vguitar-advanced-features.md` (Slicer named officially among the FX)
- 🟡 https://www.soundonsound.com/reviews/boss-vg-800 (150+ effects incl. modulation/rhythmic FX — ring-mod unverified in repo)
- Transformed from Pedalxly VG-800-Patches.md (DOUG-designed; repo-verified Slicer FX, dialable values)
