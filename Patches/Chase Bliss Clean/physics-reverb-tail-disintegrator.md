---
type: patch
title: Physics — Reverb-Tail Disintegrator
device: Chase Bliss Clean
date: 2026-06-15
description: "Physics electrically models a bouncing spring to destabilize the compression amount — set on long reverb tails it fractures the decay into a complex-space shimmer (stadium/canyon). Demoed by BachelorMachines (great on drum loops + reverb tails, pairs with surf) and supported by Rhett Shull's note that Clean placed AFTER reverb/delay/mod 'can do some really interesting things' — dialable recipe, no published values."
tags: [physics, texture, reverb, ambient, surf, community]
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
  - { name: "Physics", type: switch, value: "LEFT for subtle wobble (organic drift) or RIGHT for twitchy snapping breakup", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
  - { name: "Dynamics", type: knob, value: "up to intensify — Physics (and Sag) both track the Dynamics position (dial from recipe)" }
  - { name: "Sensitivity", type: knob, value: "set the threshold the spring model reacts against (dial from recipe)" }
  - { name: "Attack", type: knob, value: "to taste underneath" }
  - { name: "Release", type: switch, value: "to taste underneath", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Wet", type: knob, value: "up (you want the compressed/processed signal present)" }
  - { name: "Dry", type: knob, value: "blend to taste for body" }
  - { name: "EQ", type: knob, value: "to taste" }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
---

# Physics — Reverb-Tail Disintegrator

## Concept
Physics electrically models a bouncing spring to destabilize the compression amount: LEFT = wobbling (the spring pushed sideways) for gentle drift, RIGHT = twitchy (the spring stretched and snapped) for snapping breakup. BachelorMachines flags it as sounding great on drum loops and especially on long reverb tails — it breaks up the decay to mimic a complex physical space (a stadium or a canyon) and pairs naturally with surf guitar. The trick is placement: run Clean AFTER the reverb so Physics works on the decay/sustain it sees, not on the dry pick attack.

## How to play it
1. Place Clean after a reverb (or on a drum loop) — Physics works on the decay/sustain it sees.
2. Set Physics LEFT for organic wobble or RIGHT for snapping, broken-up motion.
3. Raise Dynamics to intensify the Physics effect (Sag intensity and Physics both track the Dynamics position).
4. On long reverb tails, the decay fractures into a complex-space shimmer; on drum loops it adds spring-like volume variation.

## Notes
- **No published clock-face values** — this is a dialable recipe. The control values above are directional ("up", "to taste"), not sourced settings; only the Physics toggle directions (L subtle / Mid stable / R twitchy) and the Physics-tracks-Dynamics behavior are from the sources.
- Physics models a coil spring; it interacts with the Sensitivity threshold.
- Rhett Shull's broader point: Clean placed AFTER reverb/delay/modulation 'can do some really interesting things' — this patch is the clearest example, so placement is end-of-chain, after the reverb.
- Distinct from the standalone Physics-wobble patch (this one targets reverb tails specifically). Pairs naturally with surf guitar (BachelorMachines).

## Sources
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (Physics models a bouncing spring; left = wobbling, right = twitchy; great on drum loops and long reverb tails — mimics stadium/canyon; pairs with surf)
- `research/transcripts/rhett-shull-clean-who-its-for-dusty-boost.md` (placing Clean after reverb/delay/modulation 'really interesting things')
- `research/links/compressorpedalreviews-clean-deep-dive.md` (Physics: L subtle / Mid stable / R twitchy; Sag intensity tracks Dynamics)
- demo:BachelorMachines + Rhett Shull (Physics on reverb tails, post-reverb placement) — dialable recipe, no published values
