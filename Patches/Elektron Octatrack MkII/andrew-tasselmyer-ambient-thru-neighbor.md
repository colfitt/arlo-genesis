---
type: patch
title: Andrew Tasselmyer Ambient Thru → Neighbor chain
device: Elektron Octatrack MkII
date: 2026-06-14
description: Ambient/drone live processing of an external source through the OT, crossfader-morphed into a feedback wash — from named ambient artist Andrew Tasselmyer (Studio Diary, Jun 18 2025).
tags: [ambient, drone, live-fx, neighbor-chain, flex, crossfader, artist, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 3 · Tracks 1 (Thru) + 2 (Neighbor)" }
  - { name: "Track 1 machine", type: switch, value: "Thru (external in)", options: ["Thru", "Neighbor", "Flex"] }
  - { name: "Track 2 machine", type: switch, value: "Neighbor (after T1)" }
  - { name: "Track 3/4 machine", type: switch, value: "Flex (record buffers from Input AB or T2)" }
  - { name: "FX (T1–T2)", type: switch, value: "DJ EQ + Filter + Lo-Fi, plus Dark Reverb + Delay" }
  - { name: "Tone", type: knob, value: "cut lows, emphasize mid resonance" }
  - { name: "Delay FB", type: knob, value: "cranked near/past 110 (never self-oscillates → safe to push)" }
  - { name: "Crossfader", type: knob, value: "simultaneously raises Reverb MIX + track VOLUME to max + Delay FB → one throw swells the dry line into a feedback wash" }
  - { name: "Pre-fader hardware send", type: switch, value: "keeps a parallel unprocessed signal for layering" }
---

# Andrew Tasselmyer Ambient Thru → Neighbor chain

## Concept
Ambient/drone live processing of an external source through the OT, crossfader-morphed — the rig's core move — from a named, working ambient artist. The crossfader throw simultaneously raises Reverb MIX, track VOLUME, and Delay feedback so a single gesture swells the dry line into a feedback wash.

## How to play it
1. **T1 = THRU (external in), T2 = NEIGHBOR (after T1), T3/T4 = FLEX** (record buffers from Input AB or T2).
2. FX across T1–2: **DJ EQ + Filter + Lo-Fi, plus Dark Reverb + Delay**; tone = cut lows, emphasize mid resonance.
3. **Delay FB cranked near/past 110** (it never self-oscillates → safe to push).
4. Set up the **crossfader** to simultaneously raise Reverb MIX + track VOLUME to max + Delay FB → one throw swells the dry line into a feedback wash.
5. Keep a pre-fader hardware send for a parallel unprocessed signal to layer with.

## Notes
- Delay type and exact reverb-size numbers not fully specified beyond FB~110 and "Dark Reverb."
- A real named-artist live-FX patch, on-aesthetic for this rig.

## Sources
- Ref: Andrew Tasselmyer (ambient artist) — Studio Diary, Jun 18 2025
- research/links/artist-andrew-tasselmyer-ambient-thru-neighbor.md
- Transformed from Pedalxly Octatrack-MkII-Patches.md (artist)
