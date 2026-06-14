---
type: patch
title: Dusty Pre-Dirt Sputter
device: Chase Bliss Clean
date: 2026-06-14
description: A crumbly, faltering, blooming overdrive that sputters and breaks when you dig in — on-brand "recorded-wrong" texture feeding the Hizumitas/108, also a standalone vintage OD/boost voice.
tags: [overdrive, texture, dusty, lo-fi, sputter, community, signature]
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
  - { name: "Dynamics", type: knob, value: "CRANK into Sag (~2:00)" }
  - { name: "Sensitivity", type: knob, value: "ROLL BACK (= the Dusty 'amount'/clip-threshold)" }
  - { name: "Wet", type: knob, value: "BOOST to compensate (~1:00)" }
  - { name: "Dry", type: knob, value: "11:00 (turn up to let the dust bleed onto the dry signal too)" }
  - { name: "Attack", type: knob, value: "to taste" }
  - { name: "EQ", type: knob, value: "to taste" }
  - { name: "Release", type: switch, value: "to taste", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "R (Modulated, drifting EQ) optional", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "R (twitchy) for sputter OR L (subtle) for gentler bloom", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
  - { name: "Slot/Bank", type: knob, value: "Onboard RIGHT preset slot (Dusty pre-dirt) per Bass Fox's 3-preset live layout" }
---

# Dusty Pre-Dirt Sputter

## Concept
Dusty mode turns Clean into a blooming overdrive that sputters and breaks when you dig in. With DUSTY engaged, cranking Dynamics into Sag pushes the stage-2 clip into a "looming" distortion; rolling back Sensitivity sets the Dusty amount/clip threshold, and boosting Wet compensates for the level loss. Stacked degradation for an on-brand "recorded-wrong" texture into the Hizumitas/108 — or a standalone vintage OD/boost voice. A flavor, not a default.

## How to play it
1. **Engage the DUSTY dip.**
2. CRANK Dynamics into Sag (~2:00).
3. BOOST Wet to compensate (~1:00).
4. ROLL BACK Sensitivity (this is the Dusty "amount"/clip threshold).
5. Dry ~11:00 — turn up to let the dust bleed onto the dry signal too.
6. Physics RIGHT (twitchy) for sputter OR LEFT (subtle) for gentler bloom; Mode RIGHT (Modulated, drifting EQ) optional; EQ to taste.
7. Balance Sensitivity/Wet/Dry by ear — it is finicky.

## Notes
- Dusty hits the DRY signal too — signal flow is COMPRESSOR → EQ → MIXER → LIMITER, so every comp/EQ/mix change reshapes the dirt.
- Python (Elektronauts) blends Dry up to keep nuance/avoid dropouts, with Physics LEFT subtle.
- Save to the onboard RIGHT slot per Bass Fox's layout (Left = leveler, Right = Dusty, Middle = live/creative).

## Sources
- Clean manual pp.32–33 DUSTY walkthrough ("Crank DYNAMICS, boost WET, roll back SENSITIVITY… blooming overdrive that sputters and breaks when you dig in", `research/links/cb-manual-clean-compression-recipes.md`)
- `research/transcripts/rhett-shull-clean-who-its-for-dusty-boost.md` (Dusty as standalone OD/boost)
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (Dusty = stage-2 clip; go into Sag for "looming" distortion)
- `research/links/elektronauts-clean-community-recipes.md` (Python: Dusty + Dry blended up to keep nuance/avoid dropouts, Physics LEFT subtle)
- Transformed from Pedalxly Clean-Patches.md (community)
