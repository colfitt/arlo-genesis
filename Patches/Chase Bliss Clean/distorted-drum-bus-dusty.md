---
type: patch
title: Distorted Drum Bus — Dusty on Drums
device: Chase Bliss Clean
date: 2026-06-15
description: "Run a drum bus through Clean with DUSTY engaged to turn the stage-two limiter into a harmonic overdrive for crunchy, distorted-drum character — Devin Belanger's and Bass Fox's drum move, distinct from the guitar-focused Dusty Pre-Dirt patch. Provenance: demo (Devin Belanger / Bass Fox) + ReviewRevival, with WET ~2-3:00 published and the rest dialed by ear."
tags: [overdrive, dusty, drums, bus, lo-fi, community]
dips:
  Dusty: on
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: off
  MISO: off
controls:
  - { name: "Sensitivity", type: knob, value: "the Dusty 'amount'/clip threshold — roll back for more bloom/dust (by ear)" }
  - { name: "Wet", type: knob, value: "BOOST (~2:00-3:00) to push the limiter into clipping and compensate for level drop (ReviewRevival)" }
  - { name: "Dry", type: knob, value: "turn up to dust the dry signal too (by ear)" }
  - { name: "EQ", type: knob, value: "tilt brighter/darker over the drums to taste (by ear)" }
  - { name: "Mode", type: switch, value: "L (Shifty) optional, as an envelope EQ over the drums", options: ["L Shifty", "Mid Manual", "R Modulated"] }
---

# Distorted Drum Bus — Dusty on Drums

## Concept
Run a (stereo) drum bus through Clean and flip DUSTY ON to turn the stage-two limiter into a harmonic overdrive — crunchy, saturated, distorted-drum character rather than transparent compression. This is the drum-focused flavor of Dusty: Devin Belanger calls it "fantastic for those distorted drum sounds," and Bass Fox uses it for distorted-drum grit (often pairing the Shifty envelope-EQ over the kit). Sensitivity sets the Dusty amount / clip threshold, Wet pushed up activates and compensates for the clipping, and Dry blends the grit onto the dry signal too. Distinct from the guitar-aimed Dusty Pre-Dirt patch — here the target is a stereo percussion bus. A flavor, not a default.

## How to play it
1. Run the drum bus through Clean (stereo) and **flip the DUSTY dip ON.**
2. Set **Sensitivity** as the Dusty amount / clip threshold — roll back for more bloom/dust.
3. **Boost Wet (~2:00-3:00)** to push the limiter into clipping and compensate for the level drop; turn **Dry** up to dust the dry signal too.
4. Optionally engage the tilt **EQ** (brighter/darker) or **Shifty (Mode LEFT)** as an envelope EQ over the drums.
5. **Dial by ear** — Dusty is finicky to balance between Sensitivity, Wet and Dry.

## Notes
- Dusty signal flow is COMPRESSOR → EQ → MIXER → LIMITER, so every comp/EQ/mix change reshapes the distortion.
- Distinct from the guitar-focused Dusty Pre-Dirt patch — this targets a stereo percussion bus for distorted-drum grit.
- Finicky to dial (compressorpedalreviews) — expect trial-and-error on Sensitivity/Wet/Dry.
- **No published values** except the WET ~2:00-3:00 trigger point (ReviewRevival). Treat the rest as a dialable recipe — Sensitivity, Dry, EQ and Mode are set by ear per Bass Fox / Devin Belanger, not from published settings.

## Sources
- `research/transcripts/devin-belanger-clean-most-useful-pedal.md` (drums: Dusty mode turns the limiter into an overdrive, "fantastic for those distorted drum sounds")
- `research/transcripts/bassfox-quincas-moreira-studio-tool-sidechain.md` (drums: tried DUSTY for distorted-drum character; used Shifty EQ as an envelope EQ)
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (Dusty lowers stage-2 clipping threshold into distortion; Sensitivity = threshold selector)
- reviewrevival.ca/reviews/chase-bliss-clean-definitive-review-2025 (WET ~2-3:00 needed to activate clipping)
- Transformed from Pedalxly Clean-Patches.md (community)
