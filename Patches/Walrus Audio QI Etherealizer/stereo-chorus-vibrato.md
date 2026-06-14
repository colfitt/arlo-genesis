---
type: patch
title: Stereo Chorus → Vibrato (hidden move)
device: Walrus Audio QI Etherealizer
date: 2026-06-14
description: Pitch-vibrato instead of chorus — an officially documented hidden sound where Chorus Mix fully clockwise tips the balance to pure pitch-modulated wet.
tags: [chorus, vibrato, hidden, modulation, designed, signature]
hidden:
  Chorus Mix fully CW = vibrato: dry/wet balance tips fully to the pitch-modulated wet
controls:
  - { name: "Chorus mode", type: switch, value: "Stereo", options: ["Tri", "Stereo"] }
  - { name: "Chorus Mix", type: knob, value: "fully clockwise (= vibrato)" }
  - { name: "Rate", type: knob, value: "adjust for vibrato speed" }
  - { name: "Depth", type: knob, value: "adjust for vibrato amplitude" }
  - { name: "Slot/Bank", type: knob, value: "Building block (apply over any chorus-active patch)" }
---

# Stereo Chorus → Vibrato (hidden move)

## Concept
Pitch-vibrato instead of chorus — an officially documented hidden sound. With Chorus mode on **Stereo** and **Chorus Mix fully clockwise**, the dry/wet balance tips fully to the pitch-modulated wet, giving vibrato. Pushed Rate gets into vibrato/"cool ugliness" territory, which fits the degraded aesthetic.

## How to play it
1. Set Chorus mode to **Stereo**.
2. Turn **Chorus Mix fully clockwise** = vibrato.
3. Adjust Rate/Depth for vibrato speed/amplitude.

## Notes
- Officially documented by Walrus.
- Pushed Rate gets into vibrato/"cool ugliness" territory (Reverb demo) — fits the degraded aesthetic.

## Sources
- designed from walrus-marketing-patch-descriptions.md + DeepResearch §2
- Transformed from Pedalxly QI-Etherealizer-Patches.md (designed)
