---
type: patch
title: Sag — One Part, Three Instruments
device: Chase Bliss Clean
date: 2026-06-15
description: BachelorMachines' electric-piano Sag trick — deep Sag with a fast-ish attack and fast release splits a single performance into three voices at once. Demonstrated on electric piano; treat the exact positions as approximate (dial by feel and by the LED).
tags: [sag, pad, texture, swell, electric-piano, community]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: off
  MISO: off
controls:
  - { name: "Dynamics", type: knob, value: "PAST 3:00 (deep Sag)" }
  - { name: "Attack", type: knob, value: "fast-ish (not minimum) — approximate, dial by feel" }
  - { name: "Sensitivity", type: knob, value: "~10:00 (demonstrated — quiet noodling stays under threshold, struck/held notes cross it)" }
  - { name: "Release", type: switch, value: "L (Fast)", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Wet", type: knob, value: "up" }
  - { name: "Dry", type: knob, value: "to taste" }
  - { name: "EQ", type: knob, value: "to taste" }
---

# Sag — One Part, Three Instruments

## Concept
BachelorMachines' electric-piano Sag trick: deep in Sag with a fast-ish attack, mid Sensitivity and a fast release, a single part splits into three voices. The initial attacks become a transient gate, long held chords swell into a pad, and quiet noodling that never crosses the threshold passes through untouched. One loop sounds like three instruments — add delay downstream for even more layers. Sensitivity ~10:00 is the demonstrated position so the quiet material stays beneath the threshold while struck and held notes cross it.

## How to play it
1. Push Dynamics PAST 3:00 into deep Sag.
2. Set Attack fast-ish (not minimum) and Release toggle LEFT (Fast).
3. Set Sensitivity ~10:00 so quiet noodling stays under the threshold and only struck/held notes cross it.
4. Play a mix of hard hits, held chords and quiet noodling: attacks gate, held notes swell into a pad, quiet passes through.
5. Add delay downstream to multiply the textures.

## Notes
- Sag inverts dynamics and favors higher frequencies — works on electric piano, guitar, banjo, VG-800; AVOID on boomy bass.
- Demonstrated on electric piano but generalizes to any source with mixed dynamics.
- Distinct from the Sag Swell / Slapback patch (which targets transient-boost + slapback return) — this is the three-voices-from-one-part behavior.
- The ~10:00 Sensitivity and fast-ish attack / fast release are taken from the demo; treat exact positions as APPROXIMATE — dial by feel and by the LED. No precise published values.

## Sources
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (Sag on electric piano: Attack fast-ish, Dynamics in Sag, Sensitivity ~10:00, Release fast — initial attacks = transient gate, long chords = swelling pad, quiet noodling untouched; add delay)
- Provenance: demo:BachelorMachines (Sag electric-piano "three instruments") — Sensitivity ~10:00 + fast-ish attack / fast release demonstrated; treat as approximate
