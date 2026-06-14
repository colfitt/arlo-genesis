---
type: patch
title: Pseudo-Synth Chop (Darkwave)
device: OBNE Parting
date: 2026-06-14
description: Furious, shimmery chopping waves — Russo's darkwave-suited "pseudo-synth" voice from fast tremolo coupled with signal reversal; rhythmic, pulsing, synth-like texture from a sustained source.
tags: [tremolo, darkwave, pseudo-synth, rhythmic, community]
hidden:
  Width (stereo, hold Aux + Depth — wide for ping-pong chop): "wide (optional)"
controls:
  - { name: "Mod", type: switch, value: "Tremolo", options: ["Tremolo", "Vibrato"] }
  - { name: "Dissolve", type: knob, value: "1:00–3:00" }
  - { name: "Rate", type: knob, value: "2:00" }
  - { name: "Shape", type: switch, value: "Sine OR Random Sine", options: ["Sine", "Square", "Rev Saw", "Saw", "Random Sine", "Random Square", "Envelope"] }
  - { name: "Depth", type: knob, value: "1:00" }
  - { name: "Chance", type: knob, value: "12:00" }
  - { name: "Smear", type: knob, value: "10:00" }
  - { name: "Glitch", type: knob, value: "11:00" }
  - { name: "Time", type: knob, value: "11:00" }
  - { name: "Filter", type: knob, value: "12:00" }
  - { name: "Filter", type: switch, value: "LP", options: ["LP", "HP"] }
  - { name: "Mix", type: knob, value: "12:00" }
  - { name: "Mix", type: switch, value: "Standard", options: ["Standard", "Modified"] }
  - { name: "Routing", type: switch, value: "Stereo", options: ["Mono", "Stereo-sum", "Stereo"] }
  - { name: "Trails", type: switch, value: "On", options: ["On", "Off"] }
  - { name: "Slot", type: knob, value: "live mode / MIDI slot" }
---

# Pseudo-Synth Chop (Darkwave)

## Concept
Furious, shimmery chopping waves — Russo Music's (Eric Lapp) darkwave-suited "pseudo-synth" voice: fast tremolo coupled with signal reversal. The result is a rhythmic, pulsing, synth-like texture from a sustained source. Random Sine shape makes the chop depth constantly change for unpredictable results; the optional stereo Width secondary control widens it into a ping-pong chop.

## How to play it
1. Set global defaults: Routing Stereo, Trails ON.
2. Keep Mod on Tremolo; set Rate moderate-fast (2:00) and Depth deep (1:00) for the chop.
3. Push Dissolve above noon (1:00–3:00) into reverse and combine with the chop.
4. Choose Shape: Sine for steady chops, or Random Sine for constantly changing depth / unpredictable chops.
5. Optional: hold Aux + turn Depth to set stereo Width wide for a ping-pong chop (avoids disorienting headphone ping-pong — the documented reason that control exists).

## Notes
- A documented reviewer (Eric Lapp) explicitly describes coupling these controls; clock-face values are INFERRED from his "fast tremolo + reversal" prose.
- The Width secondary control (hold Aux + Depth) avoids disorienting headphone ping-pong.
- Reference: Eric Lapp / Russo Music — "pseudo-synth" darkwave recipe.
- Save target: live mode / MIDI slot.

## Sources
- 🔵 `research/links/russo-music-parting-review.md` (couple Tremolo with signal reversal → "furious, shimmery, chopping waves," darkwave-suited)
- `research/links/parting-named-sound-recipes.md` (recipe #1). Exact clocks INFERRED.
- Transformed from Pedalxly Parting-Patches.md (community — control-direction recipe, exact clocks inferred)
