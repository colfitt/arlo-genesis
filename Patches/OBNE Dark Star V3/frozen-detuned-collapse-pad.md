---
type: patch
title: Frozen Detuned Collapse Pad
device: OBNE Dark Star V3
date: 2026-06-15
description: "Catch the collapse of a one-stomp OVERLOAD wall as a cold, frozen, detuned shimmer pad — Aux=Hold freezes the dying fuzz wall into a static, LPF-dark, lightly-crushed pad at the very end of a fuzz→delay detonation chain (🟣 DOUG-designed / dialable recipe; capabilities spec-documented, knob positions designed)."
tags: [freeze, detune, shimmer, cold-pad, hold, collapse, drone, designed, signature]
hidden:
  Aux mode: Hold
controls:
  - { name: "Mix", type: knob, value: "1:30-2:00 (mostly wet)" }
  - { name: "Decay", type: knob, value: "3:00-4:00 (high, long hang)" }
  - { name: "Multiply", type: knob, value: "noon (do NOT push high — keep it from self-oscillating before you freeze)" }
  - { name: "Filter", type: knob, value: "10:00-11:00 (LPF / dark side — cold, not glassy)" }
  - { name: "Pitch 1", type: knob, value: "+1 oct (shimmer)" }
  - { name: "Pitch 2", type: knob, value: "a smidge off the center notch into the Detune zone (cold chorus, NOT a clean interval)" }
  - { name: "Crush", type: knob, value: "11:00 (barely-there grit — ages the pad)" }
  - { name: "Lag", type: knob, value: "10:00-11:00 (short)" }
  - { name: "Aux", type: button, value: "Hold (freeze the dying wall)" }
  - { name: "Routing", type: switch, value: "Stereo (trails on)", options: ["Mono", "Mono-In-Stereo-Out", "Stereo"] }
---

# Frozen Detuned Collapse Pad

## Concept
Catch the collapse of a one-stomp OVERLOAD wall as a cold, frozen, detuned pad. Tuned to sit at the very END of a fuzz→delay detonation chain: as the Big Time OVERLOAD releases, stomp Aux=Hold to freeze the dying wall into a static, slightly-crushed, detuned shimmer that hangs in the air — a cold pad, not a glassy ascending shimmer or a clean swell. Pitch 1 +1 oct gives shimmer, Pitch 2 nudged a hair off the center notch (Detune zone) gives cold chorus, the Filter sits on the LPF/dark side so it lands cold rather than bright, and a touch of Crush ages it. Hold passes new notes bone-dry, so you can solo clean over the frozen pad or let it ring out. 🟣 DOUG-designed / dialable recipe — these are starting values for this collapse role, not quoted/sourced knob settings.

## How to play it
1. Set Mix ~1:30-2:00 (mostly wet), Decay high (long hang), Multiply at noon (keep it from running away before the freeze).
2. Filter to the LPF / dark side (~10:00-11:00) so the pad lands cold, not glassy.
3. Pitch 1 = +1 oct (shimmer); Pitch 2 = a hair off the center notch into the Detune zone (cold chorus, not a clean interval); Crush ~11:00 for barely-there grit; Lag short.
4. Assign Aux = Hold and run Stereo (trails on); store as a preset with Aux assigned.
5. In the chain: hold Big Time's RIGHT footswitch for OVERLOAD, release at the peak to collapse, and on that release stomp Dark Star Aux to FREEZE the dying wall into the frozen detuned pad.
6. Solo clean over the frozen pad (Hold passes new notes bone-dry) or let it ring out.

## Notes
- GOTCHA: while Hold is engaged, new notes pass BONE-DRY (input is locked out of the reverb) by design — solo over the pad via the dry path, or just let it hang.
- Keep Multiply moderate: high Multiply + high Decay tips the Dark Star into self-oscillation, which fights the clean "catch" you want on the collapse.
- This is the COLD counterpart to infinite-shimmer-drone (glassy/ascending HPF) and the freeze-bed (no shimmer/detune): LPF-dark + off-notch Detune + light Crush is what makes it land as a cold collapse pad rather than a bright build.
- Octave-up content can ice-pick — the LPF/dark Filter setting is what tames it here.
- 🟣 HONESTY: capabilities are spec-documented (dual ±2-oct pitch, bipolar filter, Crush, lag/multiply self-oscillation, Aux = freeze/Hold); the exact knob positions are a DOUG-designed starting point for this collapse role, NOT quoted/sourced settings.
- Ref: post-punk/doom crescendo collapse — the cold detuned pad that catches a self-oscillating fuzz wall on release.

## Sources
- gear/OBNE Dark Star V3/GearProfile.md (dual ±2-oct pitch shifters, bipolar filter, Crush, lag/multiply self-oscillation, Aux = freeze/Hold — spec-documented)
- Designed to catch the Big Time "one-stomp-climax" OVERLOAD collapse (Big Time manual p.16/26: OVERLOAD = hold RIGHT in Long).
- Detune-zone / cold-chorus behavior consistent with detune-chorus-width.md and dual-pitch-shimmer-build.md patches; exact positions are DOUG-designed, not quoted.
</content>
</invoke>
