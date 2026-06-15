---
type: patch
title: "Boost Mode Clean — diode-free headroom & cleanup"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: "The AM's BOOST mode on its own — no clipping diodes in the path, so it's the cleanest, loudest, most open and headroomy circuit, capable of low-gain overdrive only when pushed hard. The most dynamic and touch-responsive mode: it cleans up beautifully with guitar-volume rolls and lighter picking, working as a transparent clean boost / make-up gain stage. Documented mode behavior ('no diodes, more headroom, open') and the cleanup/touch-response are quoted from CB's demo + a Premier Guitar review; a dialable recipe — no published knob values."
tags: [boost, clean-push, transparent, headroom, cleanup, factory]
dips:
  MASTER: "optional on — BOOST is loud; keep level controlled if stacking (not required standalone)"
controls:
  - { name: "CHANNEL MODE", type: switch, value: "BOOST (no diodes = max headroom, open) — single channel", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN", type: knob, value: "low for a transparent clean lift; push hard for low-gain overdrive (dial from recipe, no published value)" }
  - { name: "VOL", type: knob, value: "set the amount of lift you need (dial from recipe)" }
  - { name: "TONE", type: knob, value: "to taste (dial from recipe)" }
  - { name: "PRESENCE", type: knob, value: "DOWN" }
  - { name: "TREBLE BOOSTER", type: switch, value: "MIDDLE (off); flip DOWN for a Rangemaster-style cut variant", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
---

# Boost Mode Clean — diode-free headroom & cleanup

## Concept
The AM's BOOST mode used by itself. Unlike OVERDRIVE and DISTORTION, BOOST has no clipping diodes in its path — "no diodes… a bunch more headroom and an open sound" — making it the cleanest, loudest, and most open circuit on the pedal, capable of low-gain overdrive only when pushed hard. It's also the most dynamic and touch-responsive mode: roll your guitar volume down or pick lighter and it cleans up beautifully. Used standalone it's a transparent clean boost / make-up gain stage, and it's the same building block underneath the AMP PUSHER and COMBO stacking recipes.

## How to play it
1. Set one channel to BOOST — the diode-free circuit with the most headroom and the most open, dynamic response.
2. Keep GAIN low for a transparent clean boost / make-up gain; push GAIN hard if you want a touch of low-gain overdrive.
3. Set VOL for the lift you need.
4. Roll your guitar volume down to hear it clean up — BOOST/OD are the most touch-responsive modes.

## Notes
- Documented mode behavior is quoted ("no diodes, more headroom, open" and the cleanup/touch-response); no exact knob numbers are published — dial GAIN/VOL/TONE from the recipe.
- The cleanest and loudest mode — also the building block for the AMP PUSHER and COMBO stacking recipes.
- PG review: cleans up well with picking and volume rolls in BOOST/OD, and avoids muddiness at low volumes.
- MASTER dip is optional — useful only if you stack this loud BOOST into another stage; not needed standalone.

## Sources
- research/transcripts/cb-technical-demo.md (BOOST = "no diodes… bunch more headroom and an open sound")
- research/links/premier-guitar-review-tips.md (touch response; cleans up with picking/volume rolls)
- research/transcripts/doug-hanson-demo.md ("Boost is a clean boost capable of low-gain overdrive")
- Ref: Brothers AM manual, "Controls – Modes"
