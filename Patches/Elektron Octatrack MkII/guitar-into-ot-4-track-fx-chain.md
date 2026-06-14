---
type: patch
title: Guitar-into-OT 4-Track FX Chain (ModWiggler)
device: Elektron Octatrack MkII
date: 2026-06-14
description: Live-mangling front-board strings (banjo/baritone via VG-800) through the OT as a pedalboard-style 4-track chain (Thru → Neighbor → Pickup → Flex), all crossfader-morphable.
tags: [live-fx, neighbor-chain, pickup, flex, guitar, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 2 · Tracks 1-4" }
  - { name: "Track 1 machine", type: switch, value: "Thru — FX1 = Filter, FX2 = Plate Reverb (TIME LONG so downstream tracks swell on the tail)", options: ["Thru", "Neighbor", "Pickup", "Flex"] }
  - { name: "Track 2 machine", type: switch, value: "Neighbor (in = T1) — FX1 = Lo-Fi (Bit-Rate Reduction ~middle), FX2 = Delay; ring-mod as TREMOLO (low ring freq)" }
  - { name: "Track 3 machine", type: switch, value: "Pickup — FX1 = Filter, FX2 = Spring Reverb" }
  - { name: "Track 3 LFO1", type: switch, value: "→ PITCH, wave = RANDOM" }
  - { name: "Track 3 LFO2", type: switch, value: "→ filter WIDTH" }
  - { name: "Track 3 LFO3", type: switch, value: "→ filter Q" }
  - { name: "Track 4 machine", type: switch, value: "Flex — Record Trig, source = T1 output, FX1 = Lo-Fi, FX2 = Spring Reverb" }
  - { name: "Crossfader", type: knob, value: "all four tracks crossfader-morphable" }
---

# Guitar-into-OT 4-Track FX Chain (ModWiggler)

## Concept
Live-mangling front-board strings (banjo/baritone via VG-800) through the OT as a pedalboard-style chain: a Thru head feeds a Neighbor, a Pickup looper, and a Flex recorder, each adding its own pair of FX, and all four are crossfader-morphable.

## How to play it
1. **T1 THRU:** FX1 = Filter, FX2 = Plate Reverb (TIME set LONG so downstream tracks swell on the tail).
2. **T2 NEIGHBOR (in = T1):** FX1 = Lo-Fi (Bit-Rate Reduction ~middle), FX2 = Delay; use the ring-mod section as TREMOLO (low ring freq).
3. **T3 PICKUP:** FX1 = Filter, FX2 = Spring Reverb; **LFO1 → PITCH wave = RANDOM, LFO2 → filter WIDTH, LFO3 → filter Q**.
4. **T4 FLEX:** Record Trig, source = T1 output, FX1 = Lo-Fi, FX2 = Spring Reverb.
5. Perform all four with the crossfader.

## Notes
- FX assignments recovered from the search excerpt (page 403'd to WebFetch); exact filter/delay numeric values not stated in the source.

## Sources
- Ref: MOD WIGGLER — "Guitar / Octatrack" thread
- research/links/modwiggler-guitar-thru-neighbor-pickup-chain.md (modwiggler.com t=144656)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (community)
