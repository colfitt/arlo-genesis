---
type: patch
title: Banjo Phrase-Sample Roll → Rhythmic Grain
device: Walrus Audio QI Etherealizer
date: 2026-06-14
description: Turn a banjo roll's percussive transients into a rhythmic grain pattern — the grain engine triggers on attack peaks.
tags: [granular, banjo, phrase-sample, rhythmic, designed, signature]
controls:
  - { name: "Flow", type: switch, value: "Parallel", options: ["Series", "Parallel"] }
  - { name: "Grain mode", type: switch, value: "Phrase Sample", options: ["Grain Cloud", "Phrase Sample"] }
  - { name: "Grain Mix", type: knob, value: "1:00" }
  - { name: "X", type: knob, value: "mid (or X-min to lock to Delay time)" }
  - { name: "Playback", type: knob, value: "x1 or x2" }
  - { name: "Delay Mix", type: knob, value: "10:00 (tap-tempo to the roll)" }
  - { name: "Tone", type: knob, value: "10–11:00 (rolled back to tame banjo 2–4 kHz spike)" }
  - { name: "Space", type: knob, value: "modest" }
  - { name: "Slot/Bank", type: knob, value: "Suggested user PC 16" }
---

# Banjo Phrase-Sample Roll → Rhythmic Grain

## Concept
Turn a banjo roll's percussive transients into a rhythmic grain pattern — the grain engine triggers on attack peaks. Phrase Sample is peak-triggered, so a banjo roll becomes a rhythmic grain pattern. Pre-filter with Tone so the bright banjo doesn't grain harshly.

## How to play it
1. Set Flow to **Parallel**, grain mode to **Phrase Sample** (Grain Mix ~1:00).
2. Set X mid (or X-min to lock to Delay time); Playback x1 or x2.
3. Tap-tempo the Delay to the roll.
4. Roll Tone back (~10–11:00) to tame the banjo 2–4 kHz spike before it grains.

## Notes
- Phrase Sample is peak-triggered — a banjo roll becomes a rhythmic grain pattern.
- Pre-filter with Tone so the bright banjo doesn't grain harshly.
- Don't double the Microcosm's rhythm here.

## Sources
- designed from DeepResearch §6 (banjo notes) + §2 (Phrase Sample) + UsageGuide §5
- Transformed from Pedalxly QI-Etherealizer-Patches.md (designed)
