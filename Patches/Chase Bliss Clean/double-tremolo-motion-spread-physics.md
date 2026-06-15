---
type: patch
title: Double Tremolo (Motion + Modulated EQ + Spread)
device: Chase Bliss Clean
date: 2026-06-15
description: Bass Fox's stacked-tremolo guitar move — MISO + SPREAD + MOTION with the Modulated EQ tremolo AND Physics on top, so the compression amplitude (Motion/Physics) and the EQ both modulate and pan across the stereo field for a lush, chaotic stereo double-tremolo from a mono source. Dial from recipe — no published clock-face values.
tags: [modulation, tremolo, motion, stereo, spread, community]
dips:
  MISO: on
  Spread: on
  Motion: on
  Dusty: off
  Swell Aux: off
  Noise Gate: off
  Sidechain: off
  Latch: off
controls:
  - { name: "Mode", type: switch, value: "R (Modulated — EQ auto-modulates at the Attack rate)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "EQ", type: knob, value: "off-noon to pick the modulated center (dial from recipe — no published value)" }
  - { name: "Attack", type: knob, value: "sets both the EQ tremolo rate and the Motion mod RATE (CCW faster) — dial from recipe" }
  - { name: "Dynamics", type: knob, value: "Motion mod DEPTH (more CW = deeper throb) — dial from recipe" }
  - { name: "Sensitivity", type: knob, value: "by LED (motion only happens while playing above threshold; fades when you stop)" }
  - { name: "Wet", type: knob, value: "up — dial from recipe" }
  - { name: "Dry", type: knob, value: "to taste — dial from recipe" }
  - { name: "Release", type: switch, value: "to taste", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Physics", type: switch, value: "engage for added spring-glitch on the compression amount (combine freely)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
---

# Double Tremolo (Motion + Modulated EQ + Spread)

## Concept
Bass Fox's stacked-tremolo guitar move: run MISO + SPREAD + MOTION with the Modulated/tremolo EQ AND Physics layered on top, so you get DOUBLE tremolo in stereo — the compression amplitude moving (Motion/Physics) AND the EQ moving (Modulated), both panning across the stereo field. A lush, chaotic stereo-tremolo texture from a mono source. Distinct from the Leslie patch (single Modulated EQ) and the Tremolo Pad patch (Motion only) — this stacks BOTH modulation engines in stereo.

## How to play it
1. Wire mono in / stereo out and flip MISO, then flip SPREAD and MOTION.
2. Set the Mode toggle RIGHT (Modulated EQ) so the EQ tremolos at the Attack rate.
3. Set Dynamics (Motion depth) and Attack (rate) for the amplitude tremolo.
4. Add Physics for extra spring-glitch on the compression amount.
5. Play: amplitude AND EQ both modulate, panning in stereo = double tremolo.

## Notes
- No published clock-face values — treat all knob settings above as a dialable recipe and set by ear/LED.
- End-of-chain / stereo only — MISO + SPREAD need the stereo redeploy slot, not the front-of-board mono slot.
- Combine Motion freely with Physics, EQ modes, Sag and Dusty (BachelorMachines).
- SPREAD sounds "particularly nice on Swell and especially on the EQ/MOTION tremolos" (BachelorMachines).

## Sources
- `research/transcripts/bassfox-quincas-moreira-studio-tool-sidechain.md` (Guitar: MISO + SPREAD + MOTION on for the tremolo-EQ effect, Physics added for DOUBLE tremolo — compression amplitude AND EQ moving, in stereo)
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (mix-and-match MOTION with Physics/EQ modes/Sag/Dusty; SPREAD nice on EQ/MOTION tremolos)
- demo: Bass Fox (double tremolo) — dialable recipe, no published values (community)
