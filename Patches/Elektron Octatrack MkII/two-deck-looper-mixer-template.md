---
type: patch
title: Two-Deck Looper/Mixer Template (Deck A T1-4 / Deck B T5-8)
device: Elektron Octatrack MkII
date: 2026-06-14
description: Laptop-free A/B crossfade between two live sources — e.g. a fuzz-wall deck vs a banjo deck, split into two four-track decks (audio destrukt / newcome).
tags: [looper, mixer, template, crossfader, thru-machine, flex, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Dedicated Project · Tracks 1-8 split into two decks" }
  - { name: "Deck A", type: switch, value: "T1-4 (fader LEFT)" }
  - { name: "Deck B", type: switch, value: "T5-8 (fader RIGHT)" }
  - { name: "Track 1 & 5 machine", type: switch, value: "THRU", options: ["Thru", "Flex"] }
  - { name: "Track 2 & 6 machine", type: switch, value: "FLEX" }
  - { name: "Per loop track", type: button, value: "one-shot RECORD trig at step 1 + a note trig at step 1" }
  - { name: "Pattern length", type: knob, value: "64 steps (4 bars)" }
  - { name: "Thru input level", type: knob, value: "+64 (max)" }
  - { name: "Crossfader XVOL lock", type: knob, value: "Deck A MAX@A/MIN@B, Deck B opposite (equal-power deck crossfade, no center dip)" }
---

# Two-Deck Looper/Mixer Template (Deck A T1-4 / Deck B T5-8)

## Concept
A laptop-free A/B crossfade between two live sources — e.g. a fuzz-wall deck vs a banjo deck. Tracks 1-4 are Deck A (fader left), tracks 5-8 are Deck B (fader right), each with a Thru head and a Flex looper. XVOL min/max locks per deck give an equal-power crossfade with no center dip. A clean A/B-deck shell for the rig.

## How to play it
1. **Deck A = T1-4 (fader LEFT), Deck B = T5-8 (fader RIGHT).**
2. **T1 & T5 = THRU, T2 & T6 = FLEX.**
3. Per loop track: one-shot **RECORD trig at step 1 + a note trig at step 1**; pattern length = **64 steps (4 bars)**.
4. **Thru input level = +64 (max).**
5. Crossfader: lock **XVOL min/max per deck** (Deck A MAX@A/MIN@B, Deck B opposite) = equal-power deck crossfade, no center dip.

## Notes
- Concrete on layout / +64 input / 64-step / step-1 trig pairing / XVOL min-max; conceptual on FX choice.
- A clean A/B-deck shell for the rig.

## Sources
- Ref: audio destrukt / newcome — "OT as looper/mixer" (Feb 2024)
- research/links/looper-mixer-deck-ab-newcome.md
- Transformed from Pedalxly Octatrack-MkII-Patches.md (community)
