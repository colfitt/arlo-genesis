---
type: patch
title: Rhythmic Bit-Crush Mover (3-LFO degrade stack)
device: Elektron Digitakt 2
date: 2026-06-14
description: Moving digital grit / "recorded-wrong" jagged harmonics on a drone — three LFOs stacked on Bit Reduction, SRR, and Pitch.
tags: [degrade, bit-crush, drone, lfo, community, signature]
controls:
  - { name: "LFO1 DEST", type: switch, value: "Bit Reduction" }
  - { name: "LFO1 WAVE", type: switch, value: "RANDOM" }
  - { name: "LFO1 SPD", type: knob, value: "32 (synced)" }
  - { name: "LFO2 DEST", type: switch, value: "SRR amount (Sample Rate Reduction)" }
  - { name: "LFO2 WAVE", type: switch, value: "SQUARE" }
  - { name: "LFO2 MODE", type: switch, value: "TRIG (rhythmic distortion variation)", options: ["FREE","TRIG","HOLD","ONE","HALF"] }
  - { name: "LFO3 DEST", type: switch, value: "Pitch" }
  - { name: "LFO3 DEP", type: knob, value: "tiny (very low — vintage pitch drift)" }
  - { name: "LFO3 SPD", type: knob, value: "low" }
  - { name: "Optional LFO", type: switch, value: "EXPONENTIAL one-shot → Bit Reduction (transient-enhanced crush)" }
---

# Rhythmic Bit-Crush Mover (3-LFO degrade stack)

## Concept
Three on-aesthetic degraders stacked on one drone/texture track: a RANDOM LFO on Bit Reduction for moving grit, a SQUARE TRIG LFO on the SRR amount for rhythmic distortion variation, and a tiny slow LFO on Pitch for vintage drift. An optional exponential one-shot LFO on Bit Reduction adds transient-enhanced crush.

## How to play it
1. LFO1: `DEST = Bit Reduction`, `WAVE = RANDOM`, `SPD = 32` (synced).
2. LFO2: `DEST = SRR amount`, `WAVE = SQUARE`, `MODE = TRIG` (rhythmic distortion variation).
3. LFO3: `DEST = Pitch`, tiny `DEP`, low `SPD` (vintage pitch drift).
4. Optional: EXPONENTIAL one-shot LFO → Bit Reduction for transient-enhanced crush.

## Notes
- `SPD 32` is quoted; the pitch-drift depth is "very low" (relative).
- Works on any drone/texture track.

## Sources
- `research/links/59perlen-lfo-sound-design-digitakt.md` (`SPD 32`)
- `research/links/elektronauts-underrated-lfo-settings-destinations.md` (t/241235)
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
