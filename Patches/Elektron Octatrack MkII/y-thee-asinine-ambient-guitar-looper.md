---
type: patch
title: Y thee Asinine Ambient-Guitar-Looper layout
device: Elektron Octatrack MkII
date: 2026-06-14
description: The closest published real-world match to this rig's job — a guitarist using the OT as an FX box + looper for psychedelic ambient guitar (Thru → 3× Neighbor → beat → 2× Pickup → Master).
tags: [ambient, looper, neighbor-chain, pickup, guitar, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 3 · T1 Thru / T2-4 Neighbor / T5 beat / T6-7 Pickup / T8 Master" }
  - { name: "Input", type: switch, value: "guitar (baritone) → OT inputs C/D; mains → end compression + stereo enhance → computer" }
  - { name: "Track 1 machine", type: switch, value: "Thru (guitar in) — compression + Lo-Fi (distortion/grit)", options: ["Thru", "Neighbor", "Pickup", "Master"] }
  - { name: "Track 2 machine", type: switch, value: "Neighbor — chorus + flanger (width/ambience)" }
  - { name: "Track 3 machine", type: switch, value: "Neighbor — phaser + freeze delay" }
  - { name: "Track 4 machine", type: switch, value: "Neighbor — another freeze delay" }
  - { name: "Track 5 machine", type: switch, value: "a simple beat to play in time to (no metronome)" }
  - { name: "Track 6 machine", type: switch, value: "Pickup (record/loop/overdub the guitar)" }
  - { name: "Track 7 machine", type: switch, value: "Pickup (record/loop/overdub the guitar)" }
  - { name: "Track 8 machine", type: switch, value: "Master" }
  - { name: "Scenes", type: button, value: "a few scenes for live loop manipulation via crossfader" }
---

# Y thee Asinine Ambient-Guitar-Looper layout

## Concept
The closest published real-world match to this rig's job: a guitarist using the OT as an FX box plus looper for psychedelic ambient guitar. The routing/track-assignment diagram is the load-bearing payload — a Thru head feeds three Neighbor FX tracks, a simple beat sits on T5, two Pickup loopers handle record/loop/overdub, and T8 is the master.

## How to play it
1. Chain: guitar (baritone) → amp/cab sim (OT has none) → OT inputs **C/D**; OT main outs → back out for end compression + stereo enhance → computer.
2. **T1 = THRU (guitar in):** compression + Lo-Fi (distortion/grit).
3. **T2 = NEIGHBOR:** chorus + flanger (width/ambience).
4. **T3 = NEIGHBOR:** phaser + freeze delay.
5. **T4 = NEIGHBOR:** another freeze delay.
6. **T5 = a simple beat** to play in time to (no metronome).
7. **T6 + T7 = PICKUP** machines (record/loop/overdub the guitar).
8. **T8 = MASTER.**
9. Program a few scenes for live loop manipulation via the crossfader.

## Notes
- **Rig swap:** replace the cab-sim with the three pedalboards feeding the stereo print into Track 1 Thru.
- Mostly a demo — the routing/track-assignment diagram is the load-bearing payload; exact knob values not given. The published blueprint for the OT's role here. yt-dlp verified.

## Sources
- Ref: Y thee Asinine — "Octatrack is an Ambient Guitar Looper!"
- research/transcripts/ythee-ot-ambient-guitar-looper-fm3.md (youtube MvzOChK5P0M)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (community)
