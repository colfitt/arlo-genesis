---
type: patch
title: Combo — boost-into-boost with Master
device: Chase Bliss Brothers AM
date: 2026-06-15
description: "Chase Bliss's canonical boost-stacking recipe (manual COMBO): set BOTH channels to BOOST and use Channel 1 to push Channel 2 for a versatile, loud, open-sounding drive. CB explicitly recommends turning the MASTER dip on while exploring boost stacking so you can crank VOL 1 (the push amount) without disruptive volume jumps — the canonical fix for the VOL-1 level-snap trap."
tags: [boost, stacked, clean-push, transparent, factory, always-on]
dips:
  MASTER: on
controls:
  - { name: "CHANNEL 1 MODE", type: switch, value: "BOOST (the pusher), on", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "low — dial from recipe, no published value" }
  - { name: "VOL 1", type: knob, value: "raise gradually — this is how hard Ch1 pushes Ch2; dial from recipe, no published value" }
  - { name: "CHANNEL 2 MODE", type: switch, value: "BOOST (the output), on", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 2", type: knob, value: "low — open, loud boost-drive, not a high-gain wall; dial from recipe, no published value" }
  - { name: "VOL 2", type: knob, value: "global output (MASTER on) — set for final stage level; dial from recipe, no published value" }
  - { name: "PRESENCE", type: knob, value: "DOWN to start (hold footswitch + TONE to set)" }
---

# Combo — boost-into-boost with Master

## Concept
Chase Bliss's canonical boost-stacking recipe, listed in the manual as "COMBO": set BOTH channels to BOOST and use Channel 1 to push Channel 2 for a versatile, loud, open-sounding drive. VOL 1 becomes the "how hard do I push" knob, Channel 2 is the output stage, and GAIN stays low on both so the result is open and loud rather than a saturated wall. CB explicitly recommends turning the MASTER dip on while exploring boost stacking, so VOL 2 becomes the global master and you can crank VOL 1 without disruptive volume jumps — the canonical fix for the VOL-1 level-snap trap.

## How to play it
1. Set BOTH channels to BOOST and turn both on.
2. Turn the MASTER dip ON so VOL 2 is the global master.
3. Gradually raise VOL 1 — this pushes Channel 2 harder for a louder, more open drive — without disruptive level jumps (MASTER absorbs them).
4. Set VOL 2 for your final stage level. Keep GAIN low on both channels for the open, loud character; bring PRESENCE up only if the tone closes in.

## Notes
- CB's own canonical boost-stacking recipe: the channel modes and MASTER-dip guidance are quoted, but no exact knob numbers are published — dial VOL/GAIN from the recipe. This is a dialable recipe, not a found/measured setting.
- The MASTER dip is load-bearing — without it, popping Channel 2 off snaps output to VOL 1's (loud) setting.
- Open and loud rather than saturated — distinct from the distortion-stack walls and from amp-pusher (which leans on the AMP).
- Slot: intended as a MIDI preset (suggested).

## Sources
- research/links/preset-stacking-recipes.md (chasebliss.com: "both channels to BOOST… use Channel 1 to push Channel 2… recommend turning on the MASTER dip")
- research/links/factory-preset-settings.md (manual Stacking ideas: "COMBO")
- research/links/cb-technical-demo-settings.md (MASTER dip behavior)
- Ref: Brothers AM manual, "Finding Your Sound" → COMBO; chasebliss.com/brothers-am
