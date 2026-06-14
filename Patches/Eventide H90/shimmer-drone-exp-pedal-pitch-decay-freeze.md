---
type: patch
title: Shimmer Drone — exp-pedal -> Pitch Decay -> Freeze
device: Eventide H90
date: 2026-06-14
description: Reliably ring out shimmer drones without the pitch-loop overload — an expression pedal sweeps Pitch Decay up, then past 100 into Freeze before the loop clashes. Eventide staff move.
tags: [drone, shimmer, freeze, expression-pedal, performance, artist, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "9" }
  - { name: "Preset A Algorithm", type: switch, value: "Shimmer" }
  - { name: "Pitch Decay (expression pedal target)", type: knob, value: "start ~80-100, end through Pitch Freeze / Pitch+verb Freeze (past 100)" }
  - { name: "Decay", type: knob, value: "splits into Low / Mid / High Band Decay" }
  - { name: "Expression Pedal", type: button, value: "sweep up to bring shimmer tails in, then push past 100 to Freeze" }
---

# Shimmer Drone — exp-pedal -> Pitch Decay -> Freeze

## Concept
The reliable way to perform shimmer drones live, recommended by Eventide staff. Map an expression pedal to Pitch Decay: sweeping up brings the shimmer tails in, and pushing the pedal **past 100** crosses into Pitch Freeze / Pitch+verb Freeze, locking the wall **before** the documented pitch-loop overload can clash.

## How to play it
1. Engage Shimmer on Preset A.
2. Map an **expression pedal to Pitch Decay** — start point ~80-100, end point set through Pitch Freeze / Pitch+verb Freeze (past 100).
3. Sweep the pedal up to bring shimmer tails in.
4. Push past 100 to Freeze before the pitch loop overloads.

## Notes
- This is a technique-level recipe (control scheme), not a full knob table.
- Decay splits into Low / Mid / High Band Decay on the H90.
- Provenance = manufacturer-staff forum post -> artist/factory tier.

## Sources
- research/links/eventide-forum-shimmer-swell-modechoverb-techniques.md (eventideaudio.com forum, staff "brock")
- Transformed from Pedalxly H90-Patches.md (artist/factory)
