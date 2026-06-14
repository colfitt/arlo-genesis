---
type: patch
title: Glitch / Degraded Texture Generator (Recipe C)
device: Novation 61SL MkIII
date: 2026-06-14
description: DOUG-designed Session — irregular ratchet/glitch bursts over a degraded texture; the "recorded-wrong" move on a percussive/granular source.
tags: [generative, glitch, ratchet, degraded, micro-steps, designed, signature]
controls:
  - { name: "Parts", type: knob, value: "ONE Part → a percussive/granular source (MPC chop / Octatrack slice / Chroma Console feedback)" }
  - { name: "Micro-steps", type: button, value: "On 3–4 steps fill multiple micro-steps (6 top-row buttons over the faders) with same note → ratchet bursts" }
  - { name: "Ratchet-step Chance", type: knob, value: "30–60% (glitches fire irregularly)" }
  - { name: "Pattern Direction", type: switch, value: "Ping-Pong", options: ["Forward", "Reverse", "Ping-Pong", "Random"] }
  - { name: "Pattern Sync Rate", type: knob, value: "1/16 or 1/32 (fast stutter)" }
  - { name: "Record", type: button, value: "Shift+Record loose hits (non-quantised, lands on nearest 1/6 tick), then tidy in micro-steps view" }
  - { name: "Morph (automation lane)", type: knob, value: "Record ONE slow filter/CC sweep, then disable record (24 PPQN automation curve; does NOT copy between tracks)" }
  - { name: "Clock", type: switch, value: "SL master (ratchets lock to the bar)", options: ["SL master", "Off"] }
  - { name: "Scales", type: switch, value: "Optional (On+Snap keeps pitched glitches in key)", options: ["Off", "On"] }
  - { name: "Session Slot", type: knob, value: "Session slot 7" }
---

# Glitch / Degraded Texture Generator (Recipe C)

## Concept
Irregular ratchet/glitch bursts over a degraded texture — the "recorded-wrong" move on a percussive/granular source (MPC sample chop, Octatrack slice, Chroma Console feeding back). Micro-steps + per-step Chance = grid-aligned irregularity; pairs naturally with MPC drum craft and Chroma Console feedback.

## How to play it
1. ONE PART → a percussive/granular source.
2. On 3–4 steps fill MULTIPLE MICRO-STEPS (the 6 top-row buttons over the faders — Steps → Options → pick a step → hold a micro-step + play a key) with the same note → ratchet bursts.
3. Set those ratchet steps to Chance 30–60% so glitches fire irregularly.
4. PATTERN: Direction = Ping-Pong, Sync Rate = 1/16 or 1/32 (fast stutter).
5. RECORD loose hits with Shift+Record (non-quantised, lands on nearest 1/6 tick), then tidy in micro-steps view.
6. MORPH: record ONE slow filter/CC automation lane (a knob sweep), then disable record so the texture evolves (24 PPQN automation curve — not p-locks; automation does NOT copy between tracks).
7. CLOCK: SL master so ratchets lock to the bar. SCALES optional (pitched glitches stay in key if On+Snap).

## Notes
- DESIGNED.
- Micro-steps + per-step Chance = grid-aligned irregularity.
- Pairs naturally with MPC drum craft and Chroma Console feedback.

## Sources
- designed from research/links/seq-generative-recipes.md Recipe C + seq-manual-micro-steps.md + seq-manual-recording-automation.md (Shift+Record 1/6 tick, automation lanes); taste-profile lo-fi/degraded lean.
- Ref: Taste — art-rock glitch-rhythm (Ful Stop); lo-fi/degraded cassette warts.
- Transformed from Pedalxly 61SL-MkIII-Patches.md (designed)
