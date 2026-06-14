---
type: patch
title: Flange Filtered
device: Strymon Deco V2
date: 2026-06-14
description: A movable/parkable static notch you sweep across a distorted drone/doom wall — "a fixed-notch EQ you can park on a fuzz wall." Strymon named recipe "Flange Filtered".
tags: [flange, comb-filter, doom, drone, eq, factory, signature]
controls:
  - { name: "Tape Saturation", type: switch, value: "ON (heavy, OR feed it the upstream dirt stack)", options: ["ON","OFF"] }
  - { name: "Doubletracker", type: switch, value: "ON", options: ["ON","OFF"] }
  - { name: "Type", type: switch, value: "sum (or try invert for swapped notch frequencies)", options: ["sum","invert","bounce"] }
  - { name: "Wobble", type: knob, value: "0 (MINIMUM — makes the comb STATIC)" }
  - { name: "Blend", type: knob, value: "~12:00" }
  - { name: "Lag Time", type: knob, value: "sweep BY HAND or assign EXP; park in flange->short-chorus region ~9-11:00" }
  - { name: "Slot/Bank", type: knob, value: "PC16" }
---

# Flange Filtered

## Concept
Strymon's named "Flange Filtered" recipe: with Wobble at zero the comb becomes STATIC — a fixed-notch EQ you can park on a fuzz wall. Sweep Lag Time by hand (or expression) to move the notch across a distorted drone/doom wall and park where it scoops best. The more saturated/high-bandwidth the input, the more intense the comb — the top doom-EQ tool on the pedal.

## How to play it
1. Engage Tape Saturation (heavy, or feed it the upstream dirt stack) and Doubletracker.
2. Type sum (or invert for swapped notch frequencies).
3. Wobble to 0 (MINIMUM) — this is what makes the comb static.
4. Blend ~12:00.
5. Sweep Lag Time by hand (or assign EXP → Lag Time: heel = flange ~9:00, toe = chorus ~12:00) to walk the notch live across a Hizumitas / MXR 108 wall; park in the flange→short-chorus region (~9–11:00).

## Notes
- Assign EXP → Lag Time to walk the notch live across the distorted wall.
- The more saturated/high-bandwidth the input, the more intense the comb.

## Sources
- transcripts/strymon-tape-flanging-chorus-examples.md (Strymon "Flange Filtered": distorted signal manually flanged, Wobble down = movable/parkable comb EQ)
- DeepResearch §4 + Sound on Sound
- links/strymon-deco-expression-assignment-procedure.md (assign EXP to Lag Time)
- Ref: Strymon named recipe "Flange Filtered" + Sound on Sound static-comb note
- Transformed from Pedalxly Deco-V2-Patches.md (factory/artist)
