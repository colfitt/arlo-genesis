---
type: patch
title: Vibrato + Space + Filter
device: Hologram Chroma Console
date: 2026-06-14
description: The official electric-piano build — vibrato-into-reverb with a moving "manual tremolo" filter; FILTER-before-SPACE filters the source not the tail, and a GESTURE sweeps the filter as an auto-filter.
tags: [vibrato, reverb, filter, modulation, factory, signature]
hidden:
  Texture FILTER style: LOW PASS (blue knob left, in FX Setup)
  Module order: FILTER (Texture) BEFORE SPACE (Diffusion) — filters source not tail, reverb last
  DRIFT (Movement, on VIBRATO): 0 = straight sine; up = random + stereo width
  DRIFT (Diffusion, on SPACE): pitch-modulation on the reverb tail
  GESTURE (C+D): sweeping FILTER AMOUNT = "manual tremolo" / auto-filter sweep
controls:
  - { name: "MIX", type: knob, value: "fully up to start; drop to taste for reverb" }
  - { name: "Movement effect", type: switch, value: "VIBRATO", options: ["VIBRATO", "PHASER", "PITCH", "TREMOLO", "DOUBLER"] }
  - { name: "Movement RATE", type: knob, value: "speed, to taste" }
  - { name: "Movement AMOUNT", type: knob, value: "depth — back off (full depth is extreme)" }
  - { name: "Diffusion effect", type: switch, value: "SPACE", options: ["SPACE", "REVERSE", "REELS", "CASCADE", "COLLAGE"] }
  - { name: "Diffusion TIME", type: knob, value: "reverb time, to taste" }
  - { name: "Texture effect", type: switch, value: "FILTER", options: ["FILTER", "CASSETTE", "SQUASH", "BROKEN", "INTERFERENCE"] }
  - { name: "Texture AMOUNT", type: knob, value: "fully down (fully open in LPF), then gesture it" }
  - { name: "Slot/Bank", type: knob, value: "C3" }
---

# Vibrato + Space + Filter

## Concept
The second official build-from-scratch patch — vibrato into reverb, with a moving "manual tremolo" filter. FILTER is placed before SPACE so it filters the source (not the reverb tail), and a recorded GESTURE sweeping the FILTER AMOUNT acts as an auto-filter / manual tremolo.

## How to play it
1. Start blank: all effect controls at minimum, **MIX** fully up.
2. MOVEMENT **VIBRATO** — RATE = speed, AMOUNT = depth (full depth is extreme, so back AMOUNT off); secondary DRIFT at 0 = straight sine, turn up to morph toward random + stereo width.
3. DIFFUSION **SPACE** — dial reverb TIME; secondary **DRIFT on SPACE = pitch-modulation on the tail**; drop MIX to taste.
4. **FX Setup:** set FILTER style = **LOW PASS** (blue knob left); reorder so **FILTER (TEXTURE) is BEFORE SPACE** (filters the source, not the tail — reverb last).
5. Engage FILTER with AMOUNT fully down (fully open in LPF).
6. Record a **GESTURE (C+D)** sweeping FILTER AMOUNT = "manual tremolo"/auto-filter sweep; exit, then bring the reverb back.

## Notes
- A related SWELL + PITCH + SPACE + INTERFERENCE preset is referenced as Bank A slot 4 in the same video (no dial-ins given).

## Sources
- research/transcripts/hologram-sound-from-scratch-3-electric-piano.md (YouTube wXX49jLXVsA, official)
- Ref: Hologram Electronics — Sound from Scratch #3
- Transformed from Pedalxly Chroma-Console-Patches.md (factory)
