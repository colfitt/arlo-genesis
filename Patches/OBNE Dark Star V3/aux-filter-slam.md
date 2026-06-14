---
type: patch
title: Aux = Filter slam (momentary swell/duck)
device: OBNE Dark Star V3
date: 2026-06-14
description: Footswitch-triggered filter sweep that slams the low-pass closed (duck/swell), reverting on release.
tags: [aux, filter, swell, performance, community]
hidden:
  Aux mode: Filter
controls:
  - { name: "Aux", type: button, value: "Filter — engaged = LPF slams fully closed; released = returns to prior Filter setting; tap to latch / hold for momentary" }
  - { name: "Filter", type: knob, value: "set prior position (returns here on release)" }
  - { name: "Routing", type: switch, value: "Stereo", options: ["Mono", "Mono-In-Stereo-Out", "Stereo"] }
---

# Aux = Filter slam (momentary swell/duck)

## Concept
A footswitch-triggered filter sweep that slams the low-pass fully closed for a duck/swell, then reverts on release. Assign Aux = Filter, and the engaged state forces the LPF fully closed; releasing returns to the prior Filter setting.

## How to play it
1. Assign Aux = Filter (hold the Aux footswitch and move the Filter knob; the assignment saves per preset).
2. Tap Aux to latch the closed-filter state, or hold for momentary.
3. Release to return to your prior Filter setting.

## Notes
- This is a pre-assigned extreme — the filter goes fully closed.
- Widely called less musical than putting Filter on an expression pedal, but it is one of Aux's three jobs.
- Aux assignment saves per preset.

## Sources
- research/transcripts/obne-official-dan-explains-it-all.md + manual p.3 + research/links/community-hold-aux-expression-gotchas.md
- Transformed from Pedalxly Dark-Star-V3-Patches.md (community)
