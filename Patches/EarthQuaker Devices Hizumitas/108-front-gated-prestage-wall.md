---
type: patch
title: "MXR 108 Front Gated Pre-Stage — splat into a smooth wall"
device: EarthQuaker Devices Hizumitas
date: 2026-06-15
description: "The rig's documented architecture — the MXR 108 silicon Fuzz Face sits IN FRONT of the Hizumitas as a gated, splatty pre-stage that the Hizumitas smooths into a sustained wall. Inverted from the usual Muff-first/FF-second order: here the 108's erratic splat becomes the texture the Hizumitas resolves. Dialable recipe (no published Hizumitas positions for this stack)."
tags: [stacking, wall-of-sound, doom, designed]
controls:
  - { name: "Volume", type: knob, value: "unity (recipe, not published)" }
  - { name: "Sustain", type: knob, value: "12:00–2:00 — wall voice (recipe, not published)" }
  - { name: "Tone", type: knob, value: "to taste (recipe, not published)" }
---

# MXR 108 Front Gated Pre-Stage — splat into a smooth wall

## Concept
The rig-specific architecture from the dossier: the MXR 108 silicon Fuzz Face sits IN FRONT of the Hizumitas as a gated, splatty pre-stage that the Hizumitas smooths into a sustained wall. This inverts the usual Muff-first / Fuzz-Face-second order — here the 108's erratic splat becomes the texture the Hizumitas resolves into a long, even sustain. The Hizumitas does the smoothing; the 108 supplies the gated character on the way in.

## How to play it
1. Place the MXR 108 silicon Fuzz Face IN FRONT of the Hizumitas (the rig's existing order).
2. Set the Hizumitas to a sustaining wall voice — Sustain up, Tone to taste — so it smooths the 108's splat into a wall.
3. Set the MXR 108 to taste (no published values); expect erratic behavior because the upstream Colour Box buffer feeds it.
4. Play and let the gated/splatty 108 texture resolve into the Hizumitas's sustained wall.
5. If the 108 sounds thin (buffer in front), swap positions — Hizumitas before 108. The Hizumitas sounds great into the 108's input.

## Notes
- Documented rig architecture: *"the 108 is essentially acting as a gated, splatty pre-stage that the Hizumitas will smooth out into a sustained wall."*
- **Honesty flag:** NO published Hizumitas knob values exist for this stack — the positions above are a dialable recipe (wall voicing), not a sourced setting. The MXR 108 is dial-to-taste.
- The Hizumitas tolerates the upstream Colour Box buffer fine (~150kΩ input); the 108 is the one that may misbehave behind a buffer — hence the swap-if-thin troubleshooting.
- Distinct from the existing Front-Stacked Brutal Wall patch (general front-drive principle for this rig) — this is the specific 108-as-gated-pre-stage idea plus the swap-if-thin fix.

## Sources
- *"the 108 is essentially acting as a gated, splatty pre-stage that the Hizumitas will smooth out into a sustained wall... If the 108 sounds thin, swap their positions (Hizumitas before 108). The Hizumitas will sound great into the 108's input"* (`gear/EarthQuaker Devices Hizumitas/research/Hizumitas-DeepResearch.md` §5).
- 108 in front = gated/splatty pre-stage the Hizumitas smooths into a wall (`research/Hizumitas-UsageGuide.md` §4).
- Provenance: DeepResearch §5 (rig architecture; dialable recipe — no published values).
