---
type: patch
title: Stereo Rotary / Leslie Spin
device: Boss BF-3
date: 2026-06-14
description: The "real" Gate/Pan — with both outputs patched stereo, the mode alternately pans L/R for a lush rotary/Leslie swirl instead of a mono chop; a wide rotating wash on the final stereo wall. Requires OUTPUT A + OUTPUT B. Ref: Alex Messano "5 Cool Ways."
tags: [flanger, rotary, leslie, stereo, swirl, pan, wash, factory]
controls:
  - { name: "MODE", type: switch, value: "Gate/Pan", options: ["Standard", "Ultra", "Gate/Pan", "Momentary"] }
  - { name: "MANUAL", type: knob, value: "12:00 (wide-swirl Classic-Jet values) — or Messano's slicer values for a choppier pan" }
  - { name: "RES", type: knob, value: "~3–4:00 (wide swirl) — or low for choppier pan" }
  - { name: "DEPTH", type: knob, value: "12:00 (wide swirl)" }
  - { name: "RATE", type: knob, value: "12:00 (wide swirl)" }
  - { name: "Input", type: switch, value: "GUITAR IN", options: ["GUITAR IN", "BASS IN"] }
  - { name: "Output", type: switch, value: "OUTPUT A + OUTPUT B (STEREO — required)", options: ["OUTPUT A (mono)", "OUTPUT A+B (stereo)"] }
---

# Stereo Rotary / Leslie Spin

## Concept
The "real" Gate/Pan: with both outputs patched into a stereo path, the same mode alternately pans L/R for a lush rotary/Leslie swirl instead of a mono chop. A wide rotating wash on the final stereo wall. Use the Classic-Jet knob values for a wide swirl, or Messano's slicer values for a choppier pan.

## How to play it
1. Set MODE to Gate/Pan and patch BOTH OUTPUT A and OUTPUT B into a stereo path.
2. For a wide swirl use the Classic-Jet knobs (MANUAL 12:00, DEPTH 12:00, RATE 12:00, RES ~3–4:00); for a choppier pan use Messano's slicer values instead.
3. Play a sustained stereo wall through it for a rotating Leslie-style wash.

## Notes
- Currently unavailable in the mono Board-1 slot — needs OUTPUT B / a post-CE-2W repatch; in the default mono slot it collapses to the Gate Slicer (Mono Chop).
- The H90/Chroma do stereo rotary-flange better, so this is a "when a part demands it" repatch, not a default.

## Sources
- `research/transcripts/messano-5-cool-ways.md` ("when hooked up in stereo that Gate mode functions as a panning mode … lush swirling"); behavior `research/transcripts/sweetwater-don-carr-review.md` + `research/BF-3-DeepResearch.md` §5
- Ref: Alex Messano "5 Cool Ways" (creator demo)
- Transformed from Pedalxly BF-3-Patches.md (factory/artist)
