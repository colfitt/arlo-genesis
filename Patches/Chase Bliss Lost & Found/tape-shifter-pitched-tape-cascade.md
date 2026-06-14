---
type: patch
title: Tape Shifter (Pitched Tape Cascade)
device: Chase Bliss Lost & Found
date: 2026-06-14
description: Factory combo (CB "TAPE SHIFTER") — a synced two-stage cascade of pitch-shifted, repeated reflections (Pitch Repeater) running into a warm Tape Echo; a rhythmic clock-locked delay texture for ambient/electronic-leaning passages into the Microcosm.
tags: [delay, tape, pitch, rhythmic, clock-locked, factory]
dips:
  UNSYNC: off
  SPREAD: on
  TRAILS: on
hidden:
  GLUE: "10:00–11:00"
controls:
  - { name: "ROUTING", type: switch, value: "L<R series (Right into Left)", options: ["L>R", "L+R", "L<R"] }
  - { name: "R slot mode", type: switch, value: "4A Tape Echo (native — no SWAP)" }
  - { name: "L slot mode", type: switch, value: "2B Pitch Repeater (native — no SWAP)" }
  - { name: "MODIFY (L pitch shift)", type: knob, value: "oct-down (great with GLUE) or up-a-5th (airy)" }
  - { name: "TIME (L delay subdivision)", type: knob, value: "noon = beat (left = subdivisions, right = multiples)" }
  - { name: "ALT (L number of taps)", type: knob, value: "chop the repeat finer" }
  - { name: "TIME (R delay time)", type: knob, value: "stepped/synced" }
  - { name: "MODIFY (R feedback)", type: knob, value: "→ infinite (never self-oscillates)" }
  - { name: "ALT (R stability/tape-age)", type: knob, value: "up = older (HPF + warble)" }
  - { name: "BLEND", type: knob, value: "1:00–2:00 (Tape Echo mix in the cascade)" }
  - { name: "MIX (RAMP)", type: knob, value: "noon–1:00" }
  - { name: "Slot/Bank", type: knob, value: "Preset R (live recallable)" }
---

# Tape Shifter (Pitched Tape Cascade)

## Concept
CB's named factory Combo — *"A two-stage cascade of synced reflections, where analog-style tape echoes are pitch shifted and repeated."* The Pitch Repeater (2B) pitch-shifts and re-triggers the reflections, then `L<R` (Right into Left) feeds them into a warm Tape Echo (4A). More of a rhythmic/electronic delay than a drone wall, but it earns inclusion as a clock-locked time texture into the Microcosm.

## How to play it
1. Set ROUTING `L<R` (Right slot feeds Left).
2. Pitch Repeater: choose MODIFY = oct-down (great with GLUE) or up-a-5th (airy); set TIME subdivision (noon = beat); use ALT to chop the repeat into finer taps.
3. Tape Echo: set feedback (MODIFY) toward infinite (it never self-oscillates); raise ALT for older, warbly, high-passed tape age.
4. BLEND ~1–2:00 sets the Tape Echo's mix in the cascade.
5. Latch a new chord loudly to trigger the buffer dump-and-refill (a feature on new chords, a surprise on held drones).

## Notes
- More rhythmic/electronic delay than drone wall (hence no signature tag), but a clean clock-locked time texture.
- UNSYNC off — clock-locked; MIDI clock overrides anyway.
- SPREAD on splits the echo L/R.
- The Tape Echo dumps-and-refills its buffer on a loud new chord — a feature for latching a new chord, a surprise on held drones.

## Sources
- CB Field Guide "Combos" (TAPE SHIFTER = Pitch Repeater < Tape Echo, `L<R` series) — `research/links/cb-manual-combos-official-recipes.md`
- Pitch Repeater + Tape Echo maps from BachelorMachinesTV Pt1/Pt2 — `research/transcripts/bachelormachinestv-science-part1.md` & `-part2.md`
- Ref: CB Field Guide named Combo "TAPE SHIFTER"
- Transformed from Pedalxly Lost-and-Found-Patches.md (factory)
