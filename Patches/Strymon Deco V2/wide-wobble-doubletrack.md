---
type: patch
title: Wide Wobble Doubletrack
device: Strymon Deco V2
date: 2026-06-14
description: A fat "two players on one part" stereo image to hand the texture board (Microcosm / Dark Star / QI) a WIDE doubled pair instead of a thin mono source. Strymon factory preset (PC0 / Favorite).
tags: [stereo, width, doubler, widener, factory, signature]
hidden:
  Wide Stereo Mode: on (Live-Edit, hold Tape Saturation ON, turn WOBBLE right of 12:00 -> RED/On; splits Reference->OUT L, Lag->OUT R; needs stereo out)
controls:
  - { name: "Tape Saturation", type: switch, value: "ON (touch)", options: ["ON","OFF"] }
  - { name: "Doubletracker", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "Voice", type: switch, value: "classic", options: ["classic","cassette"] }
  - { name: "Type", type: switch, value: "bounce (the widener) OR enable Wide Stereo Mode", options: ["sum","invert","bounce"] }
  - { name: "Lag Time", type: knob, value: "~12:00 (short chorus / just-short-of-slap = widest chorus)" }
  - { name: "Blend", type: knob, value: "~11:00 (favor Reference so it DOUBLES not warbles)" }
  - { name: "Wobble", type: knob, value: "9-10:00 (keep low for doubling)" }
  - { name: "Saturation", type: knob, value: "light" }
  - { name: "Slot/Bank", type: knob, value: "PC0 (factory WIDE WOBBLE / Favorite)" }
---

# Wide Wobble Doubletrack

## Concept
A fat "two players on one part" stereo image, built to hand the texture board (Microcosm / Dark Star / QI) a WIDE doubled pair instead of a thin mono source. Bounce makes "crazy wide swirls" that get much more pronounced in stereo (and still widens a mono source); Wide Stereo Mode instead splits Reference→OUT L and Lag→OUT R for a pure deck split with no combing.

## How to play it
1. Engage Tape Saturation (a touch) and Doubletracker. Voice classic.
2. Choice A — Type bounce: comb-filter character kept, crazy wide swirls.
3. Choice B — Wide Stereo Mode: hold Tape Saturation ON, turn WOBBLE right of 12:00 until it goes RED/On (splits Reference→L, Lag→R); pure motion, no combing. Requires stereo out.
4. Lag Time ~12:00 (short chorus / just-short-of-slap = widest chorus), Blend ~11:00 (favor Reference so it DOUBLES not warbles), Wobble 9–10:00 (keep low; past mid gets seasick on sustained notes), Saturation light.

## Notes
- Requires stereo out — Wide Stereo auto-disables on a mono out (Blend becomes a pan). Stereo needs a TRS adapter on the INPUT.
- Factory-named preset; clock-faces from DeepResearch §13(b) + the official Wide Stereo demo.
- Bounce = comb character kept; Wide Stereo Mode = pure L/R deck split.

## Sources
- links/strymon-deco-v2-manual-revd-secondary-midi.md (factory PC0; Wide Stereo Live-Edit on WOBBLE)
- transcripts/strymon-pete-celi-wide-stereo-mode.md (Reference→L, Lag→R; 12:00 + a bit of Wobble = natural stereo chorus)
- DeepResearch §13(b); transcripts/superdanger
- Ref: Strymon factory preset "Wide Wobble" + Wide Stereo Mode demo (QHLA5JByIYc)
- Transformed from Pedalxly Deco-V2-Patches.md (factory/artist)
