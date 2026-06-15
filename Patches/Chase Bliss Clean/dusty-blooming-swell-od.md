---
type: patch
title: "Dusty + Swell — Blooming Overdrive Swell"
device: Chase Bliss Clean
date: 2026-06-15
description: "A swelling, looming distortion that grows on each note — run DUSTY for crumbly overdrive while the Swell engine blooms the dirty signal in from silence, with Dynamics pushed into Sag underneath to make it loom. A pad-like overdrive voice that swells rather than attacks. Demonstrated by BachelorMachines (\"Dusty + Swell combine\"; go into Sag for \"looming\" distortion) — a dialable recipe, not published clock-face values."
tags: [overdrive, dusty, swell, ambient, texture, community]
dips:
  Dusty: on
  Swell Aux: "off (Dynamic Swell) — ON for a manually triggered swell"
  Latch: "off (momentary) — ON to make AUX a toggle"
  Motion: off
  Noise Gate: off
  Sidechain: off
  Spread: off
  MISO: off
hidden:
  Swell In time (Wet knob): "set the bloom-in shape — longer = slower, more pad-like"
  Swell Out time (Dry knob): "set the decay shape of the swell"
controls:
  - { name: "Dynamics", type: knob, value: "push into Sag (recipe — no published value) for the 'looming' character underneath" }
  - { name: "Sensitivity", type: knob, value: "= the Dusty amount / clip threshold (roll back to dial in the dirt; recipe, no published value)" }
  - { name: "Wet", type: knob, value: "BOOST to compensate for Dusty's level loss (main page) — repurposed as Swell In time on hidden page" }
  - { name: "Dry", type: knob, value: "turn up to dust the dry signal too (main page) — repurposed as Swell Out time on hidden page" }
  - { name: "EQ", type: knob, value: "to taste underneath" }
  - { name: "Attack", type: knob, value: "to taste" }
  - { name: "Release", type: switch, value: "to taste", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "to taste", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "to taste (L subtle for a gentler bloom, R twitchy for more sputter)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
  - { name: "AUX footswitch", type: button, value: "engages the Swell (blooms the distorted signal in from silence)" }
---

# Dusty + Swell — Blooming Overdrive Swell

## Concept
BachelorMachines' combination: run DUSTY for the crumbly overdrive AND engage the Swell so the dirty signal blooms in from silence — a swelling, looming distortion that grows on each note. With DUSTY engaged, Sensitivity sets the Dusty amount/clip threshold, Wet is boosted to compensate, and Dry can be turned up to dust the dry path too. Pushing Dynamics into Sag underneath makes the distortion "loom." The Swell engine (AUX) blooms the overdriven signal in rather than letting it strike, so you get a pad-like overdrive voice that swells instead of attacks. The combination is demonstrated, not numbered — dial it from the recipe.

## How to play it
1. **Flip the DUSTY dip ON** and dial the dirt: Sensitivity = the Dusty amount, BOOST Wet to compensate, and turn Dry up to dust the dry path.
2. **Engage the AUX swell** so the distorted signal blooms in from silence (Dynamic Swell is the default/momentary; flip LATCH to make AUX a toggle).
3. **Hidden Options** (hold both footswitches until the LEDs go green): Wet = Swell In time, Dry = Swell Out time — set the bloom shape.
4. **Push Dynamics into Sag** underneath for a "looming" distortion that grows as you play harder.
5. Play **held notes**: the overdrive swells in and looms rather than striking.

## Notes
- **Dialable recipe — no published clock-face values.** BachelorMachines demonstrates the combination ("Dusty + Swell combine"; go into Sag for a "looming" distortion) but does not publish numbered settings. Treat the control values above as a recipe to balance by ear, not as sourced positions.
- Distinct from the **Dusty Pre-Dirt Sputter** patch (attacking, breaking sputter) and the clean **Sag Swell** patches — this one is dirty *and* swelling at once.
- **Finicky to balance** (Sensitivity / Wet / Dry) like all Dusty patches — Dusty hits the DRY signal too, and signal flow is COMPRESSOR → EQ → MIXER → LIMITER, so every change reshapes the dirt.

## Sources
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (Dusty lowers stage-2 clip into distortion; go into Sag for a "looming" distortion; "Dusty + Swell combine")
- `research/links/cb-manual-clean-compression-recipes.md` (DUSTY recipe: crank Dynamics, boost Wet, roll back Sensitivity; SWELL setups; Hidden Options Wet = Swell In, Dry = Swell Out)
- Transformed from Pedalxly Clean-Patches.md (community)
