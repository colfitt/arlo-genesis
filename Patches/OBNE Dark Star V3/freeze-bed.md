---
type: patch
title: Freeze bed (Aux = Hold frozen wash)
device: OBNE Dark Star V3
date: 2026-06-14
description: Freeze the current wash into a static near-infinite bed — the rig's most performance-critical move; play a roll, freeze, solo over the static pad.
tags: [freeze, drone, hold, performance, community, signature]
hidden:
  Aux mode: Hold
controls:
  - { name: "Decay", type: knob, value: "high (build the bed first)" }
  - { name: "Multiply", type: knob, value: "raise CAREFULLY (high Multiply + Decay = self-oscillation)" }
  - { name: "Aux", type: button, value: "Hold — tap to latch freeze / hold for momentary (maxes Decay beyond knob + mutes new input)" }
  - { name: "Routing", type: switch, value: "Stereo", options: ["Mono", "Mono-In-Stereo-Out", "Stereo"] }
---

# Freeze bed (Aux = Hold frozen wash)

## Concept
Freeze the current wash into a static, near-infinite bed — the rig's most performance-critical move. Play a roll, freeze, then solo over the static pad. Hold maxes Decay beyond the knob AND mutes new input, so the wash freezes; releasing returns Decay.

## How to play it
1. Assign Aux = Hold (hold the Aux footswitch and turn Decay; the assignment saves per preset).
2. Build the bed with high Decay first.
3. Raise Multiply CAREFULLY — high Multiply + high Decay tips into self-oscillation.
4. Tap Aux to latch the freeze, or hold it for momentary; release to return Decay.

## Notes
- GOTCHA: while Hold is engaged, new notes you play pass BONE-DRY (input is locked out of the reverb), by design.
- Lean on the dry path + downstream H90/Chroma for the lead, or use expression swells instead of re-triggering.
- Aux assignment saves per preset — store on any onboard slot.

## Sources
- research/links/russomusic-review-recipes.md + research/links/premierguitar-review-recipes.md + research/transcripts/obne-official-dan-explains-it-all.md + manual p.3
- Transformed from Pedalxly Dark-Star-V3-Patches.md (community)
