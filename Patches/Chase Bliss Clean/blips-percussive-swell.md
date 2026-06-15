---
type: patch
title: "BLIPS — Percussive Muted Swell"
device: Chase Bliss Clean
date: 2026-06-15
description: "The maker's named extreme of the Swell engine — set BOTH Swell In and Swell Out to their fastest speeds and playing turns into short, soft-but-percussive muted blips. A staccato, almost-gated articulation distinct from a slow violin swell; the two swell-time values are the published BLIPS recipe (manual pp.30–31), the comp underneath is dial-by-feel."
tags: [swell, percussive, blips, texture, staccato, factory]
dips:
  Dusty: off
  Swell Aux: "off (Dynamic Swell) — ON for the tap-triggered variant"
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: "off (momentary) — ON for a toggle"
  Spread: off
  MISO: off
hidden:
  Swell In time (Wet knob): "FASTEST (fully to its fastest setting) — published BLIPS value"
  Swell Out time (Dry knob): "FASTEST (fully to its fastest setting) — published BLIPS value"
controls:
  - { name: "AUX footswitch", type: button, value: "Swell (Dynamic Swell = default, momentary; flip LATCH dip for a toggle)" }
  - { name: "Sensitivity", type: knob, value: "by left LED to taste — set so your intended notes cross the threshold and trigger a blip" }
  - { name: "Dynamics", type: knob, value: "to taste underneath (no published value — dial by feel)" }
  - { name: "EQ", type: knob, value: "to taste underneath (no published value — dial by feel)" }
  - { name: "Wet", type: knob, value: "main page to taste — repurposed as Swell In time = FASTEST on hidden page" }
  - { name: "Dry", type: knob, value: "main page to taste — repurposed as Swell Out time = FASTEST on hidden page" }
---

# BLIPS — Percussive Muted Swell

## Concept
The maker's named extreme of Clean's Swell engine. Where ~noon/noon on the two swell times gives a slow violined pad, taking BOTH Swell In and Swell Out to their fastest speeds collapses the gesture into short, soft-but-percussive muted *blips*. Each note becomes a staccato, almost-gated articulation rather than a slow bow-in — distinct in character from a slow swell and "equally useful" per the manual. Good for synthy staccato lines and rhythmic textures, especially feeding the loop/granular boards downstream where the blips become rhythmic seeds.

## How to play it
1. **Engage the AUX footswitch** — Dynamic Swell is the default (momentary). Flip the LATCH dip to make it a toggle instead.
2. **Enter Hidden Options** — hold both footswitches until both LEDs go green.
3. Turn **Wet (Swell In) FULLY to its fastest setting** and **Dry (Swell Out) FULLY to its fastest setting** — this is the published BLIPS recipe (both at min).
4. **Exit Hidden Options**; set Sensitivity by the left LED so your intended notes cross the threshold.
5. Play — each note becomes a short, soft-but-percussive muted blip; vary Sensitivity and the swell speeds for synthy staccato textures.

## Notes
- **Honesty flag:** the only sourced values here are the two swell-time extremes (fastest / fastest) — that pair *is* the published BLIPS recipe. The comp knobs underneath (Dynamics, EQ) are dial-by-feel; there are **no published numbers** for the underlying compression, so treat them as a dialable recipe.
- Manual notes that faster swells "have a distinct and equally useful character" vs slow swells.
- **Tap-triggered variant:** flip the SWELL AUX dip ON to trigger the (fast) swell from the footswitch instead of dynamically.
- Pair with delay/granular downstream so the blips become rhythmic seeds.

## Sources
- Clean manual pp.30–31 Swell — BLIPS recipe, quoted: "Set both SWELL IN and SWELL OUT to their fastest speeds… short muted blips with a soft but percussive character" (`research/links/cb-manual-clean-compression-recipes.md`)
- `research/transcripts/chase-bliss-clean-official-video-manual.md` (Swell: "both fastest = BLIPS")
- Chase Bliss Clean official manual (Swell — BLIPS sidebar, p.31)
- Transformed from Pedalxly Clean-Patches.md (factory)
