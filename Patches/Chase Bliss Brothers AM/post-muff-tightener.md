---
type: patch
title: Post-Muff Tightener (always-on default)
device: Chase Bliss Brothers AM
date: 2026-06-14
description: The rig's everyday always-on job — tighten, re-level, and add cut to the Hizumitas Muff wall WITHOUT adding gain, handing a clean predictable line level to the Longsword; the 2-IN-1 idea executed as a low-gain single-channel tightener.
tags: [tightener, always-on, low-gain, re-leveler, post-muff, designed, signature]
dips:
  MASTER: on
  PRES LINK 2: on (optional — more open, full-range on the modeled VG-800 source)
controls:
  - { name: "TREBLE BOOSTER", type: switch, value: "MIDDLE (off); flip DOWN/Rangemaster only when banjo needs cut", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
  - { name: "CHANNEL 2 MODE", type: switch, value: "BOOST (or very low OVERDRIVE), only channel ON", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 2", type: knob, value: "9 o'clock (low — tighten, not gain)" }
  - { name: "VOL 2", type: knob, value: "carefully level-matched so Hizumitas-engaged vs AM-engaged is unity (global master)" }
  - { name: "TONE 2", type: knob, value: "noon then to taste" }
  - { name: "CHANNEL 1 MODE", type: switch, value: "OFF", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "PRESENCE 2", type: knob, value: "nudged UP slightly (hold Ch2 footswitch + TONE 2) to recover upper-mid cut the Hizumitas darkened" }
---

# Post-Muff Tightener (always-on default)

## Concept
The rig's everyday always-on job: tighten, re-level, and add cut to the Hizumitas Muff wall WITHOUT adding more gain. Hands a clean, predictable line level to the Longsword and the whole time/tape chain. The 2-IN-1 idea executed as a low-gain single-channel tightener — the AM should be on more often than not, and the whole point is no extra gain, just EQ, level, and a rounded-off decay handed cleanly downstream.

## How to play it
1. Run Channel 2 only (BOOST, or very low OVERDRIVE) with GAIN 2 low at ~9 — goal is tighten, not gain.
2. Carefully level-match VOL 2 so Hizumitas-engaged vs AM-engaged is unity.
3. Nudge PRESENCE 2 up slightly (hold Ch2 footswitch + TONE 2) to recover the upper-mid cut the Hizumitas darkened.
4. Keep the MASTER dip ON (VOL 2 is global master — prevents the VOL-1 level-snap trap, keeps downstream level stable).
5. Optionally turn PRES LINK 2 ON for a more open, full-range response on the modeled VG-800 source.

## Notes
- These are designed starting points, not found settings — the manual prints diagrams, not numbers.
- Flip the treble booster DOWN/Rangemaster only when the banjo needs cut.
- PRES LINK is the move for the modeled source.
- Slot: intended as a MIDI preset (suggested).

## Sources
- designed from Brothers-AM-DeepResearch.md §5–6 (post-Muff tightener role)
- Brothers-AM-UsageGuide.md §6
- MASTER-dip recipe per research/links/preset-stacking-recipes.md (chasebliss.com)
- Transformed from Pedalxly Brothers-AM-Patches.md (designed)
