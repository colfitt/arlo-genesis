---
type: patch
title: Tube Sag — Sputtering Overload
device: Chase Bliss Clean
date: 2026-06-15
description: Pushes Dynamics into the last quarter of its sweep (the Sag zone, past 3:00) to leave compression behind and enter a simulated overloaded-tube state — your signal falls out, falters and sputters the harder you dig in. A touch-sensitive "broken" clean that reacts like a starved amp; or hold the BYPASS footswitch to slam max Sag on the fly. Manufacturer-described tone (manual SAG section + bypass-hold gesture) — the sag zone is published as "past 3:00", the exact amounts are dialable.
tags: [sag, tube, experimental, dynamic, lo-fi, glitch]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: off
  MISO: off
controls:
  - { name: "Dynamics", type: knob, value: "final quarter of the sweep (Sag zone, past 3:00)" }
  - { name: "Sensitivity", type: knob, value: "fairly high so digging in triggers the sag" }
  - { name: "Wet", type: knob, value: "BOOST to compensate for the level loss" }
  - { name: "Attack", type: knob, value: "moderate" }
  - { name: "Release", type: switch, value: "Mid (User ~650ms) — moderate", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Dry", type: knob, value: "to taste for body" }
  - { name: "EQ", type: knob, value: "to taste" }
  - { name: "Bypass FS (hold)", type: button, value: "HOLD to momentarily max out Clean's Sag effect — slam full sputter on the fly" }
---

# Tube Sag — Sputtering Overload

## Concept
Past 3:00, Dynamics leaves compression behind and enters Sag — Clean's simulated overloaded-tube state. Per the manual, "your signal falls out, falters, and sputters as you play harder." Push Dynamics into the last quarter of its sweep, set Sensitivity fairly high so digging in trips the sag, and boost Wet to recover the lost level. The result is a touch-sensitive "broken" clean that reacts to dynamics like a starved amp: it holds together when you ease off and collapses when you dig in. For a performed version, just HOLD the BYPASS footswitch to slam max Sag in the middle of a phrase.

## How to play it
1. Turn Dynamics past 3 o'clock into the Sag zone (last quarter of the sweep).
2. Raise Sensitivity so hard picking triggers the falter.
3. Boost Wet to recover the volume that Sag eats.
4. Dig in to make it sputter; ease off and it recovers.
5. Or HOLD the BYPASS footswitch to slam max Sag on the fly during a phrase.

## Notes
- Manual: Sag "simulates an overloaded tube. Your signal falls out, falters, and sputters as you play harder."
- Holding the BYPASS footswitch momentarily maxes out Clean's Sag effect — a performable "fall apart" gesture (no preset change needed).
- More useful on guitar than bass — Sag responds to higher frequencies, so boomy lows react poorly (compressorpedalreviews).
- Distinct from the Sag Swell / Slapback and Sag electric-piano patches — this targets the raw sputtering-overload character plus the BYPASS-hold gesture, not swells or the three-voices trick.
- PHYSICS adds to it for more instability (see the Physics-wobble patch).
- The sag zone is published as "past 3:00 / last quarter"; the Sensitivity, Wet and Attack amounts are a dialable recipe, not published numbers — set them by ear and by the LED.

## Sources
- Chase Bliss Clean official manual (Dynamics/SAG pp.26–27 — "simulates an overloaded tube… falls out, falters, and sputters"; BYPASS p.11 — hold to max the Sag effect)
- `compressorpedalreviews.com/post/chase-bliss-clean-compressor-review` (more useful on guitar than bass — responds to higher frequencies)
- `gearnews.com/chase-bliss-clean-revolutionary-compression`
- Provenance: manufacturer-described tone (manual SAG section + bypass-hold gesture) — sag zone published as "past 3:00", amounts dialable
