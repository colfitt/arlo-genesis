---
type: patch
title: Self-oscillating drone bed (infinite hold)
device: Strymon TimeLine
date: 2026-06-14
description: Freeze a wash and play over it — the headline drone-wall move; HOLD the active footswitch for infinite repeats regardless of the REPEATS knob.
tags: [self-oscillation, freeze, infinite-hold, drone, wall, community, signature]
hidden:
  EXP (CC 100) → REPEATS: optional — swell into/out of oscillation
controls:
  - { name: "TYPE", type: switch, value: "dTape / dBucket / Digital", options: ["dTape","dBucket","Digital","Dual","Pattern","Reverse","Ice","Lo-Fi","Swell","Trem","Filter","Duck"] }
  - { name: "REPEATS", type: knob, value: "toward max" }
  - { name: "Footswitch HOLD", type: button, value: "hold active preset (A or B) → infinite repeats; release snaps back to saved REPEATS" }
  - { name: "EXP (CC 100)", type: button, value: "optional → REPEATS to swell into/out of oscillation" }
  - { name: "Slot/Bank", type: knob, value: "any (technique on top of a saved preset)" }
---

# Self-oscillating drone bed (infinite hold)

## Concept
Freeze a wash and play over it — the headline drone-wall move. With REPEATS pushed toward max on any of dTape / dBucket / Digital, holding the active preset footswitch gives infinite repeats regardless of the REPEATS knob; releasing snaps it back to the saved REPEATS value.

## How to play it
1. On a saved preset (dTape / dBucket / Digital), push REPEATS toward max.
2. HOLD the active preset footswitch (A or B) → infinite repeats.
3. Play over the frozen bed; release the footswitch to return to the saved REPEATS.
4. Optionally map EXP (CC 100) → REPEATS to swell into/out of oscillation.

## Notes
- Infinite-hold is a footswitch HOLD, not a CC — the circulating "CC#97 = infinite repeats" claim is unverified.
- dTape drifts pitch most musically of the three machines.

## Sources
- research/links/community-timeline-hidden-features-oscillation.md (Strymon product page; Morningstar forum)
- Transformed from Pedalxly TimeLine-Patches.md (community)
