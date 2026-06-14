---
type: patch
title: PrismShift Self-Generating Stereo Arp Bed
device: Eventide H90
date: 2026-06-14
description: Feed a banjo/baritone chord -> cascading stereo-panned arpeggio bed over a drone (self-generating ambient). Built from factory "Sequential Chimes."
tags: [pitch, prismshift, arpeggio, ambient, self-generating, drone, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "25" }
  - { name: "Preset A Algorithm", type: switch, value: "PrismShift (factory 'Sequential Chimes' as starting point)" }
  - { name: "Mix", type: knob, value: "pull down a little" }
  - { name: "Arpeggio Type", type: switch, value: "change by ear" }
  - { name: "Spread", type: knob, value: "1 (FULL — arps pan L<->R across the field)" }
  - { name: "Step Length", type: knob, value: "lower = faster arpeggiation; raise/slow for an ambient bed" }
  - { name: "Arpeggio Order", type: switch, value: "e.g. Low-Mid-High -> Mid-Low-High" }
  - { name: "Gain bands", type: knob, value: "a little less High, a bit more Mid, leave Low" }
  - { name: "Feedback", type: knob, value: "per part (feedback tap on the first or second sequence)" }
---

# PrismShift Self-Generating Stereo Arp Bed

## Concept
Feed a banjo/baritone chord and PrismShift spins out a cascading stereo-panned arpeggio bed over a drone — self-generating ambient. Built from the factory "Sequential Chimes": pull Mix down a little, set Spread full so arps pan L<->R, and slow the Step Length for an ambient bed.

## How to play it
1. Load factory "Sequential Chimes" on Preset A.
2. Pull Mix down a little; change Arpeggio Type by ear.
3. Set **Spread = 1 (FULL)** so arps pan across the field.
4. Lower Step Length for faster arpeggiation, or raise/slow it for an ambient bed.
5. Adjust Arpeggio Order (e.g. Low-Mid-High -> Mid-Low-High), shape the Gain bands, and add Feedback per part.

## Notes
- Leon Todd deep-dive (xIso_kHM158). "Spread full + slow Step Length over a drone = self-generating ambient bed" (UsageGuide §5).
- High/Low voices Freeze; Mid stays live/playable (see "PrismShift / Polyphony Freeze Pad").

## Sources
- Ref: Eventide factory preset "Sequential Chimes" (as starting point)
- research/transcripts/leon-todd-h90-prismshift-algorithm.md
- Transformed from Pedalxly H90-Patches.md (community)
