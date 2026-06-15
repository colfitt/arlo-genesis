---
type: patch
title: Physics Spring Wobble — Organic Instability
device: Chase Bliss Clean
date: 2026-06-15
description: "Physics electrically models the physical response of a wobbling coil spring to sabotage the envelope follower's tracking, producing organic wobbles and bursts of motion on your own playing. The manual describes the spring model directly; ReviewRevival frames LEFT as 'more felt than heard' and RIGHT as 'kooky and delightful' glitch, and a bass deep-dive notes RIGHT gets brittle fast while a little LEFT adds bottom end — toggle positions are published, knob values are dialable, no published clock-face settings."
tags: [physics, modulation, experimental, wobble, glitch, texture]
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
  - { name: "Physics", type: switch, value: "LEFT for subtle wobble (felt-more-than-heard movement) or RIGHT for twitchy/glitchy randomness", options: ["L subtle wobble", "Mid stable", "R twitchy/unstable"] }
  - { name: "Dynamics", type: knob, value: "up so there's clear compression for the spring to disrupt — Physics intensity tracks the Dynamics position (dial from recipe)" }
  - { name: "Sensitivity", type: knob, value: "moderate-high to feed the envelope follower so the spring model has signal to react to (dial from recipe)" }
  - { name: "Attack", type: knob, value: "to taste underneath" }
  - { name: "Release", type: switch, value: "to taste underneath", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Wet", type: knob, value: "up to taste (you want the compressed/processed signal present)" }
  - { name: "Dry", type: knob, value: "blend to taste for body" }
  - { name: "EQ", type: knob, value: "to taste" }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
---

# Physics Spring Wobble — Organic Instability

## Concept
Engage the Physics toggle to model the physical response of a wobbling coil spring, sabotaging the envelope follower's ability to track you and producing organic wobbles and bursts of motion. LEFT is subtle, felt-more-than-heard movement; RIGHT is twitchy, glitchy randomness layered on top of the compression — a standalone movement voice on your own playing, distinct from the Physics reverb-tail use. Physics intensity tracks the Dynamics position, so you need real compression dialed in for the spring to have something to disrupt, and enough Sensitivity feeding the envelope for the model to react against.

## How to play it
1. Turn Dynamics up enough to get clear, audible compression.
2. Flip Physics LEFT for subtle wobble, RIGHT for chaotic twitch.
3. Raise Sensitivity so the spring model has signal to react to.
4. Play sustained notes/chords to hear the spring fluctuations.

## Notes
- **No published clock-face values** — this is a dialable recipe. Only the Physics toggle directions (L subtle wobble / Mid stable / R twitchy) and the Physics-tracks-Dynamics behavior are sourced; every knob value above is directional ("up", "moderate-high", "to taste"), not a sourced setting.
- Manual: Physics 'models the physical response of a spring to interfere with the envelope's ability to follow you, creating organic wobbles and bursts of motion.'
- ReviewRevival: LEFT is 'more felt than heard'; RIGHT is 'kooky and delightful' glitchy randomness.
- compressorpedalreviews (bass): Physics RIGHT gets brittle fast; a little LEFT adds bottom end.
- Distinct from the Physics reverb-tail patch — this is the standalone instability voice on your own playing. Combine with Sag (deep Dynamics) for maximum disrepair.

## Sources
- Chase Bliss Clean official manual (Physics p.13 + Physical Education p.27) — spring model interferes with the envelope follower, creating organic wobbles and bursts of motion
- `reviewrevival.ca/reviews/chase-bliss-clean-definitive-review-2025` (LEFT felt-more-than-heard; RIGHT kooky glitch)
- `research/links/compressorpedalreviews-clean-deep-dive.md` (Physics RIGHT brittle on bass; a little LEFT adds bottom; intensity tracks Dynamics)
- Provenance: manufacturer-described tone + reviewer detail (Physics toggle) — toggle positions published, knob values dialable, no published values
