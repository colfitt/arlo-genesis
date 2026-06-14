---
type: patch
title: Post-FX Evolving Granular Bed
device: Hologram Microcosm
date: 2026-06-14
description: An evolving sustained bed that keeps mutating as it loops — looper routing Post-FX with a constantly-changing granular engine (Haze/Tunnel/Warp), "never sounds the same twice."
tags: [looper, post-fx, evolving-bed, granular, ambient, factory, signature]
hidden:
  Looper routing: Post-FX (default; CC 24 < 64)
  Quantize (CC 27): trims to nearest beat but can drift ~a 16th/minute on external clock
controls:
  - { name: "Looper Routing", type: switch, value: "POST-FX (default; CC 24 < 64)", options: ["Post-FX (whole loop re-granulated)", "Pre-FX (each overdub keeps its own tone)"] }
  - { name: "Engine", type: switch, value: "a constantly-changing granular engine (Haze / Tunnel / Warp)" }
  - { name: "Phrase Looper", type: button, value: "record a loop; engine keeps changing so it never sounds the same twice" }
  - { name: "Slot/Bank", type: knob, value: "BLUE #58 (PC 58)" }
---

# Post-FX Evolving Granular Bed

## Concept
An evolving sustained bed that keeps mutating as it loops. With looper routing Post-FX (default) and a constantly-changing granular engine (Haze / Tunnel / Warp), "the loop keeps playing but never sounds the same way twice."

## How to play it
1. Set looper ROUTING = POST-FX (default; CC 24 < 64).
2. Pick a constantly-changing granular engine (Haze / Tunnel / Warp).
3. Record a loop; because the engine keeps changing, the loop never sounds the same way twice.

## Notes
- Documented official behavior plus the auto-feedback/drift gotchas.
- No feedback knob — oldest overdubs self-fade as you stack ("auto-feedback"); plan long builds around the self-erase.
- Quantize (CC 27) trims to nearest beat but can drift ~a 16th/minute on external clock — re-trigger rather than free-run.
- For TRUE infinite sustain use the Hold Sampler (separate buffer) instead of the looper.

## Sources
- `research/transcripts/youtube-microcosm-looping-prepost-reverse-feedback.md`
- `research/links/hologram-microcosm-looper-prepost-reverse-burst.md`
- Ref: Hologram official looping tutorial
- Transformed from Pedalxly Microcosm-Patches.md (factory)
