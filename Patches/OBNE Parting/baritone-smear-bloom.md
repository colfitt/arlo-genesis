---
type: patch
title: Baritone Smear Bloom (Drone Bed)
device: OBNE Parting
date: 2026-06-14
description: Designed for the rig — long sustained baritone chords (VG-800 baritone model) feed Smear into a lush delay→reverb bloom; low fundamentals survive light Dissolve crush as grit, forming the drone/doom underbed for Board 2.
tags: [drone, doom, baritone, bloom, envelope, bed, signature, designed]
controls:
  - { name: "Smear", type: knob, value: "2:00–3:00" }
  - { name: "Dissolve", type: knob, value: "10:00" }
  - { name: "Chance", type: knob, value: "12:00 (Envelope sensitivity, tuned for held chords)" }
  - { name: "Shape", type: switch, value: "Envelope", options: ["Sine", "Square", "Rev Saw", "Saw", "Random Sine", "Random Square", "Envelope"] }
  - { name: "Time", type: knob, value: "1:00" }
  - { name: "Glitch", type: knob, value: "10:00" }
  - { name: "Filter", type: knob, value: "11:00" }
  - { name: "Filter", type: switch, value: "LP", options: ["LP", "HP"] }
  - { name: "Mix", type: knob, value: "11:00" }
  - { name: "Mix", type: switch, value: "Standard", options: ["Standard", "Modified"] }
  - { name: "Mod", type: switch, value: "Vibrato", options: ["Tremolo", "Vibrato"] }
  - { name: "Depth", type: knob, value: "8:00" }
  - { name: "Rate", type: knob, value: "8:00" }
  - { name: "Routing", type: switch, value: "Stereo", options: ["Mono", "Stereo-sum", "Stereo"] }
  - { name: "Trails", type: switch, value: "On", options: ["On", "Off"] }
  - { name: "Slot", type: knob, value: "Preset slot or live mode" }
---

# Baritone Smear Bloom (Drone Bed)

## Concept
DESIGNED for this rig: long sustained baritone chords (VG-800 baritone model) feed Smear into a lush delay→reverb bloom; low fundamentals survive light Dissolve crush as grit. This is the drone/doom underbed the rest of Board 2 (Microcosm, QI, Dark Star) builds on. Envelope shape lets the sustained baritone dynamics gate the wash, and Standard Mix preserves the bass fundamental (analog dry-through) so the crush doesn't swamp the low end. A dark Filter LP keeps it sitting as a bed under everything.

## How to play it
1. Set global defaults: Routing Stereo, Trails ON.
2. Set Shape to **Envelope** so sustained baritone dynamics gate the wash; Chance at noon sets sensitivity, tuned for held chords.
3. Push Smear to 2:00–3:00 for a lush reverb wash; Time at 1:00 for long, slow repeats blooming together.
4. Dissolve at 10:00 (just below noon) adds light sample-rate grit to the low fundamentals, NOT full crush.
5. Keep it dark and heavy with Filter LP at 11:00; keep Mix Standard at 11:00 to preserve the dry low end.
6. Slow Vibrato drift: Depth 8:00, Rate 8:00.

## Notes
- 🟣 DESIGNED — never found. ⭐ Baritone-weight + sustained-wall pillars.
- Standard Mix is the documented move to preserve the bass fundamental (analog dry-through) so the crush doesn't swamp the low end.
- Dark Filter LP keeps it sitting as a bed under everything.
- Clocks are DOUG's tuning of documented behavior.
- Reference: making aesthetic "baritone weight / sustained walls / drone-doom"; post-punk cluster 5.
- Save target: Preset slot or live mode.

## Sources
- 🟣 designed from `research/Parting-DeepResearch.md` §6 ("Baritone Jazzmaster: Home territory… long fundamentals survive Dissolve's bit-crush as grit"; keep dry low end via Standard Mix)
- `research/Parting-UsageGuide.md` §5 ("Baritone Smear bloom"). Clocks are DOUG's tuning of documented behavior.
- Transformed from Pedalxly Parting-Patches.md (designed)
