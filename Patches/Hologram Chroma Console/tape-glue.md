---
type: patch
title: Tape-Glue
device: Hologram Chroma Console
date: 2026-06-14
description: The official Sound-from-Scratch "recorded a while ago" finishing layer — nearly-always-on cohesion under a loop, with SWEETEN + CASSETTE as the base and a footswitchable phaser+tape-echo section add.
tags: [tape, lo-fi, glue, ambient, factory, signature]
hidden:
  Module order: REELS (Diffusion) first → PHASER (Movement) after it → both under SWEETEN (Character) → into CASSETTE (Texture)
  DRIFT (Diffusion, on REELS): ~50%
  Dual Bypass: PHASER + REELS assigned to BYPASS footswitch (SWEETEN + CASSETTE stay always-on)
controls:
  - { name: "MIX", type: knob, value: "100% wet (full up), then dial AMOUNTs to taste" }
  - { name: "Character effect", type: switch, value: "SWEETEN", options: ["SWEETEN", "HOWL", "FUZZ"] }
  - { name: "Character TILT", type: knob, value: "~50%" }
  - { name: "Character AMOUNT", type: knob, value: "~50% (more = subtle saturation)" }
  - { name: "Movement effect", type: switch, value: "PHASER", options: ["PHASER", "VIBRATO", "PITCH", "TREMOLO", "DOUBLER"] }
  - { name: "Movement RATE", type: knob, value: "start 50%, then down (slower)" }
  - { name: "Movement AMOUNT", type: knob, value: "start 50%, then up a hair (chewy)" }
  - { name: "Diffusion effect", type: switch, value: "REELS", options: ["REELS", "SPACE", "REVERSE", "CASCADE", "COLLAGE"] }
  - { name: "Diffusion TIME", type: knob, value: "delay time, to taste" }
  - { name: "Diffusion AMOUNT", type: knob, value: "feedback, to taste" }
  - { name: "Texture effect", type: switch, value: "CASSETTE", options: ["CASSETTE", "FILTER", "SQUASH", "BROKEN", "INTERFERENCE"] }
  - { name: "Texture AMOUNT", type: knob, value: "~50%" }
  - { name: "Slot/Bank", type: knob, value: "A1" }
---

# Tape-Glue

## Concept
The official build-from-scratch demo patch — a "recorded a while ago" finishing layer meant to sit nearly-always-on under a loop for cohesion. SWEETEN gives a gentle compressor/saturation base, CASSETTE adds tape character, and a chewy slow phaser modulates an aged tape-echo (REELS) you can foot in as a section add.

## How to play it
1. Push **MIX** fully up first, then dial each module's **AMOUNT** to taste.
2. CHARACTER **SWEETEN** — both knobs ~50% (gentle compressor; more AMOUNT = subtle saturation).
3. MOVEMENT **PHASER** — both knobs start at 50%, then bring **RATE** down (slower) and **AMOUNT** up a hair for a "chewy" phaser.
4. DIFFUSION **REELS** (tape echo) — **TIME** sets delay time, **AMOUNT** sets feedback, secondary **DRIFT ~50** for aged/degraded tape + stereo flutter.
5. TEXTURE **CASSETTE** ~50%.
6. In **FX Setup (A+D)** reorder so **REELS is first**, then **PHASER after it** (so PHASER modulates the delay trails), both under SWEETEN, into CASSETTE.
7. **Dual Bypass:** assign PHASER + REELS to the BYPASS footswitch so SWEETEN + CASSETTE stay the always-on base and you foot-in delay+phaser as a section "add."

## Notes
- One of only two sources with real numbers (the 50% values + ~50 DRIFT are stated by Hologram).
- Keep CASSETTE modest if Gen Loss is running heavy tape — otherwise you double the wow/flutter (the "don't double the tape" rig rule).

## Sources
- research/transcripts/hologram-sound-from-scratch-1-build-preset.md (YouTube dqui4XqPoEQ, official); research/Chroma-Console-UsageGuide.md §2
- Ref: Hologram Electronics — Sound from Scratch #1
- Transformed from Pedalxly Chroma-Console-Patches.md (factory)
