---
type: patch
title: ParaPan + the Edge dual ratios
device: Strymon TimeLine
date: 2026-06-14
description: Parallel Dual hard-panned L/R for the U2/Edge dotted-eighth interplay (factory 24B / Dual reference) — the rig's rhythmic-delay trick paired with the Big Time off the shared Digitakt clock.
tags: [dual, rhythmic, the-edge, u2, dotted-eighth, ping-pong, factory, community, signature]
hidden:
  MIDICL: ON (per-preset — locks to the Digitakt clock)
controls:
  - { name: "TYPE", type: switch, value: "Dual", options: ["dTape","dBucket","Digital","Dual","Pattern","Reverse","Ice","Lo-Fi","Swell","Trem","Filter","Duck"] }
  - { name: "CONFIG", type: switch, value: "Parallel (hard L/R stereo spread)", options: ["Series","Parallel","Ping-Pong"] }
  - { name: "TIME", type: knob, value: "250 ms" }
  - { name: "TIME 2 ratio", type: switch, value: "3/4 (dotted-eighth + quarter Edge feel)", options: ["1/3 (triplet)","1/2 (eighth)","3/4 (dotted-eighth+quarter)","1/4 (sixteenth)","1/1 (unison)","3/2"] }
  - { name: "HP", type: knob, value: "80 Hz (fix for boomy banjo/baritone repeats)" }
  - { name: "Slot/Bank", type: knob, value: "24B (or user A = quarter / B = dotted-eighth)" }
---

# ParaPan + the Edge dual ratios

## Concept
Parallel Dual hard-panned L/R for the U2/Edge dotted-eighth interplay — the rig's rhythmic-delay trick, paired with the Big Time running at the eighth off the same shared Digitakt clock. TIME 2 ratio = 3/4 gives the dotted-eighth + quarter Edge feel. Off-aesthetic, but the canonical rhythmic/failover patch.

## How to play it
1. Load 24B (or set up a user slot: A = quarter, B = dotted-eighth, per Wittek/mscarney).
2. Set CONFIG Parallel (hard L/R spread — keep Parallel, the TimeLine has few ping-pong patterns), TIME 250 ms, TIME 2 ratio = 3/4.
3. Set per-preset MIDICL = ON so it locks to the Digitakt; run the Big Time at the eighth off the same clock.
4. For boomy banjo/baritone repeats, set HP = 80 Hz (mscarney302's Digital bank 2).

## Notes
- Strymon's official ratio table: triplet 1/3 · eighth 1/2 · dotted-eighth+quarter 3/4 · sixteenth 1/4 · unison 1/1.
- 24B factory uses TIME 2 = 3/2 if you want a wider interval.
- The TimeLine only receives MIDI clock (always a slave) — the Digitakt is the master.

## Sources
- U2 / The Edge — "Where the Streets Have No Name"; Strymon Dual-ratio FAQ
- research/links/community-timeline-u2-dual-and-ambient-recipes.md (Strymon official ratio table + professorben/Cirrus recipes)
- Transformed from Pedalxly TimeLine-Patches.md (factory + community)
