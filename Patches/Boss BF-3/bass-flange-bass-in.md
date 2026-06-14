---
type: patch
title: Bass Flange (BASS IN)
device: Boss BF-3
date: 2026-06-14
description: Movement on bass (Jazz Bass or VG-800 baritone) WITHOUT losing the fundamental — the BASS IN jack re-ranges MANUAL and is voiced to retain low end where a guitar-input flanger eats the bottom; low-end-safe drift under a baritone drone. Designed patch.
tags: [flanger, bass, low-end, drift, baritone, drone, designed]
controls:
  - { name: "MODE", type: switch, value: "Standard", options: ["Standard", "Ultra", "Gate/Pan", "Momentary"] }
  - { name: "MANUAL", type: knob, value: "~10:00" }
  - { name: "RES", type: knob, value: "9–10:00 (modest — too high thins the fundamental)" }
  - { name: "DEPTH", type: knob, value: "~11:00" }
  - { name: "RATE", type: knob, value: "~8:00 (slow)" }
  - { name: "Input", type: switch, value: "BASS IN (disables GUITAR IN — either/or repatch)", options: ["GUITAR IN", "BASS IN"] }
  - { name: "Output", type: switch, value: "OUTPUT A (mono)", options: ["OUTPUT A (mono)", "OUTPUT A+B (stereo)"] }
---

# Bass Flange (BASS IN)

## Concept
Movement on bass — a Jazz Bass or VG-800 baritone — without losing the fundamental. The BASS IN jack re-ranges MANUAL and is voiced to retain low end where a guitar-input flanger would eat the bottom. Here it's a low-end-safe drift under a baritone drone, adding motion while keeping the weight intact.

## How to play it
1. Plug into BASS IN (this disables GUITAR IN — it's an either/or repatch).
2. Set MODE to Standard, RATE slow (~8:00), DEPTH ~11:00, RES modest (9–10:00), MANUAL ~10:00.
3. Play a bass or baritone drone through it for low-end-safe drift.

## Notes
- Designed. Delay range on BASS IN is shorter (0.3–6.3 ms vs 0.3–14.4 ms) to keep bass clear.
- Keep RES modest so notches don't gut the fundamental — too high thins it out.
- Under-used asset for baritone-weight drone.

## Sources
- Designed from `research/BF-3-DeepResearch.md` §13(d) "Bass flange" + §6 "Jazz bass via BASS IN"; low-end-retention + "nice for slap" `research/links/bf3-modes-bass-input-digital-sheen.md`
- Transformed from Pedalxly BF-3-Patches.md (designed)
