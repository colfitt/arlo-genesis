---
type: patch
title: "TPS Boost-After-Dirt — lift another overdrive"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: "That Pedal Show's demonstration of the King of Tone boost trick — set another drive (e.g. a Bluesbreaker) dirty, then place the AM's BOOST after it so the boost lifts the already-overdriven signal and \"gives it all the love,\" with a frequency that gets you heard 100%. The general boost-after-dirt technique; the rig-specific Longsword version is its own patch."
tags: [boost, clean-push, lead-lift, king-of-tone, community, transparent]
dips:
  MASTER: "on (optional — only if you run both channels; a single boost-after-dirt uses the channel's own VOL for the lift)"
controls:
  - { name: "TREBLE BOOSTER", type: switch, value: "MIDDLE (off) for a neutral lift, or DOWN (Rangemaster) for extra cut", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
  - { name: "CHANNEL 1 MODE", type: switch, value: "BOOST (no diodes — most headroom, most open); used as the boost after another already-dirty drive", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "low — clean lift (dial from recipe)" }
  - { name: "VOL 1", type: knob, value: "set for the lift amount (dial from recipe)" }
  - { name: "TONE 1", type: knob, value: "to taste (dial from recipe)" }
  - { name: "CHANNEL 2 MODE", type: switch, value: "off (single-channel boost after dirt)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
---

# TPS Boost-After-Dirt — lift another overdrive

## Concept
That Pedal Show's demonstration of the famous King of Tone boost trick: set another drive (e.g. a Bluesbreaker) dirty, then place the AM's BOOST after it — the boost lifts the already-overdriven signal and "gives it all the love," with a frequency that gets you heard 100%. The KOT principle: a clean boost AFTER a dirt pedal increases volume and cut without adding much distortion. This is the generic boost-after-another-pedal move; the rig-specific Clean Push into the Longsword is its own patch. Note: the AM has more bottom end than a Prince of Tone, per TPS.

## How to play it
1. Get a good dirty sound from another overdrive earlier in your chain (TPS used a Bluesbreaker).
2. Set one AM channel to BOOST and place the AM after that dirt.
3. Use the BOOST to lift the already-overdriven signal — it adds volume and cut, not much distortion, and "gives it all the love."
4. Keep GAIN low; this is a clean lift. Add the Rangemaster (booster DOWN) if you want even more cut.

## Notes
- No published knob numbers — controls are a dialable recipe, not sourced values. TPS-quoted character + the analogman.com principle (boost-after-dirt trick) are what's quoted; the clocks are starting points to dial in.
- This is the generic "boost after another pedal" move; the rig-specific Clean Push into the Longsword already exists as its own patch — this is the general technique.
- Analogman's own framing: a clean boost AFTER a dirt pedal increases volume without adding much distortion (vs INTO a dirt pedal, which adds distortion).

## Sources
- research/transcripts/tps-vs-prince-duke-of-tone.md ("use the Brothers to boost the Bluesbreaker… the boost after the Bluesbreaker just lifts it and gives it all the love… that frequency that's going to get you heard, 100%")
- research/links/king-of-tone-lineage.md (analogman.com: clean boost AFTER a dirt pedal increases volume without adding much distortion)
- research/links/tps-demo-settings.md (boost-stacking another drive)
- Ref: That Pedal Show — Brothers AM vs Prince/Duke of Tone (2025-04-25)
