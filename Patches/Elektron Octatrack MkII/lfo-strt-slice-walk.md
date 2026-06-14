---
type: patch
title: LFO → STRT Slice-Walk (auto-resequence a sliced loop)
device: Elektron Octatrack MkII
date: 2026-06-14
description: Auto-marching through an 8-slice banjo/fuzz capture via an LFO on STRT so it plays a line the source never played (Elektronauts "LFOs meet Slices").
tags: [slicing, lfo, generative, banjo, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 4 · LFO1 → STRT (or RETRIG) on a Flex/Static track w/ an 8-slice grid" }
  - { name: "LFO1 wave (working)", type: switch, value: "RMP (Ramp)", options: ["RMP", "SAW", "TRI", "SQR", "RANDOM"] }
  - { name: "LFO1 Speed (SPD)", type: knob, value: "33 (CC28)" }
  - { name: "LFO1 MULT", type: knob, value: "×2" }
  - { name: "LFO1 Depth (DEPTH)", type: knob, value: "16 (scales with slice count — 16 for 8 slices; CC31)" }
  - { name: "LFO1 trig", type: switch, value: "SYNC TRIG" }
  - { name: "LFO1 dest", type: switch, value: "STRT (clean slice 1→2→…→8 march)" }
---

# LFO → STRT Slice-Walk (auto-resequence a sliced loop)

## Concept
The most concrete generative-slice recipe with verified numbers: an LFO on STRT (slice start) auto-marches through an 8-slice banjo/fuzz capture so it plays a line the source never physically played. Pair with the banjo resample for endless banjo-as-lead variation.

## How to play it
1. **WORKING setup (Voov_ov):** LFO wave = **RMP (Ramp), SPD = 33, MULT = ×2, DEPTH = 16, trig = SYNC TRIG, dest = STRT**, on an 8-slice grid → clean slice 1→2→…→8 march.
2. **PORTAMENTO variant (astricii):** Ramp wave set to HALF → sweep 0→max then hold to next trig (glide scrub).
3. **GRANULAR variant (tomes):** RAMP LFO at MAX depth → RETRIG amount + very fast retrig TIME → granular/glitch.

## Notes
- **FAILED (avoid):** Saw, SPD 64, ×2, DEPTH 8 → stuck till trig 9.
- DEPTH scales with slice count (16 is for 8 slices).
- The most concrete generative-slice recipe with verified numbers. Pair with the banjo resample (Resample-the-Banjo-Loop) for endless banjo-as-lead variation.

## Sources
- Ref: Elektronauts — "LFOs meet Slices" (Voov_ov, astricii, tomes)
- research/links/lfo-on-slices-step-walk-values.md (elektronauts.com/t/.../28821)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (community)
