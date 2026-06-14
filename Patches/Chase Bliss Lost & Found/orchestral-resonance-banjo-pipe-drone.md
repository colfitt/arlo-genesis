---
type: patch
title: Orchestral Resonance (Banjo Pipe Drone)
device: Chase Bliss Lost & Found
date: 2026-06-14
description: Factory combo (CB "ORCHESTRAL RESONANCE"; Knobs' favorite mode) — turns sustained banjo/baritone chords into two layered pitch-tracked synth/pipe voices (Orchestral Swell + Sympathetic Resonator); banjo-as-lead into a glassy drone, cleanest on slow chordal input.
tags: [drone, pitch-tracking, synth, banjo-as-lead, ambient, factory, signature]
dips:
  SPREAD: on
  TRAILS: on
  UNSYNC: off
hidden:
  GLUE: "10:00"
  ALT (L feedback): "1:00"
  ALT (R octave): "sweep DURING resonance for expression"
  EQ: "CCW if the banjo plink gets shrill"
controls:
  - { name: "ROUTING", type: switch, value: "L+R parallel", options: ["L>R", "L+R", "L<R"] }
  - { name: "L slot mode", type: switch, value: "2A Orchestral Swell (native — no SWAP)" }
  - { name: "R slot mode", type: switch, value: "5B Sympathetic Resonator (native — no SWAP)" }
  - { name: "MODIFY (L pitch interval)", type: knob, value: "oct-up for shimmer or unison for a synth pad" }
  - { name: "TIME (L swell)", type: knob, value: "12:00–1:00" }
  - { name: "MODIFY (R feedback)", type: knob, value: "2:00–3:00 (HIGH — longer ring)" }
  - { name: "TIME (R onset)", type: knob, value: "noon (very subtle)" }
  - { name: "BLEND", type: knob, value: "noon (balance both voices)" }
  - { name: "MIX (RAMP)", type: knob, value: "FULL (CB marks *)" }
  - { name: "Slot/Bank", type: knob, value: "Preset bank 2 (BANK dip)" }
---

# Orchestral Resonance (Banjo Pipe Drone)

## Concept
CB's named factory Combo and Knobs' favorite mode — *"keen tracking and two flexible, layered voices."* Sustained banjo/baritone chords become two layered pitch-tracked voices: the Orchestral Swell (2A, oct-up shimmer or unison pad) layered in parallel with the Sympathetic Resonator (5B, long glassy ring). Banjo-as-lead into a glassy drone, cleanest on slow chordal input. Both modes live on native channels, so no SWAP is needed.

## How to play it
1. Set ROUTING `L+R` parallel, MIX FULL.
2. Play slow sustained banjo/baritone chords — pitch modes track cleanest here.
3. Orchestral Swell: choose MODIFY = oct-up (shimmer) or unison (synth pad).
4. Sympathetic Resonator: MODIFY feedback HIGH (~2–3:00) for a longer ring; sweep the ALT octave **during resonance** for expression.
5. BLEND ~noon balances the two voices.

## Notes
- Pitch modes track cleanest on slow sustained banjo/baritone — fast banjo rolls will artifact (on-aesthetic).
- Resonator onset (TIME) is very subtle on shipping units — leave ~noon.
- Use EQ CCW if the banjo plink gets shrill.

## Sources
- CB Field Guide "Combos" (ORCHESTRAL RESONANCE = Orchestral Swell + Sympathetic Resonator, `L+R` parallel, `*`) — `research/links/cb-manual-combos-official-recipes.md`
- Resonator shipping map (MODIFY = feedback max = resonates forever, TIME = onset subtle, ALT = octave only audible when swept during ring) from BachelorMachinesTV Pt2 + Knobs "12 pipes / forgiving note-gated drone source" — `research/transcripts/bachelormachinestv-science-part2.md` & `cb-lost-found-walkthrough-knobs.md`
- Ref: CB Field Guide named Combo "ORCHESTRAL RESONANCE"; Knobs "my favorite mode" (Sympathetic Resonator)
- Transformed from Pedalxly Lost-and-Found-Patches.md (factory)
