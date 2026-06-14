---
type: patch
title: Pre-Granular Fodder (Steady Reverse-Crush for Microcosm)
device: OBNE Parting
date: 2026-06-14
description: Designed for the rig — hands the Hologram Microcosm a steady stream of degraded reverse/bit-crush grains it can reliably capture and loop; Parting GENERATES, Microcosm GRANULARIZES, with Chance parked at noon so the stream stays consistent.
tags: [granular, fodder, reverse, bit-crush, envelope, integration, signature, designed]
controls:
  - { name: "Dissolve", type: knob, value: "3:00 (long reverse variant) — or 9:00 for heavy bit-crush variant" }
  - { name: "Chance", type: knob, value: "12:00" }
  - { name: "Smear", type: knob, value: "11:00" }
  - { name: "Glitch", type: knob, value: "11:00" }
  - { name: "Time", type: knob, value: "12:00" }
  - { name: "Shape", type: switch, value: "Envelope", options: ["Sine", "Square", "Rev Saw", "Saw", "Random Sine", "Random Square", "Envelope"] }
  - { name: "Filter", type: knob, value: "1:00" }
  - { name: "Filter", type: switch, value: "LP", options: ["LP", "HP"] }
  - { name: "Mix", type: knob, value: "12:00" }
  - { name: "Mix", type: switch, value: "Standard", options: ["Standard", "Modified"] }
  - { name: "Mod", type: switch, value: "Tremolo", options: ["Tremolo", "Vibrato"] }
  - { name: "Depth", type: knob, value: "8:00" }
  - { name: "Routing", type: switch, value: "Stereo", options: ["Mono", "Stereo-sum", "Stereo"] }
  - { name: "Trails", type: switch, value: "On", options: ["On", "Off"] }
  - { name: "Slot", type: knob, value: "Preset slot or live mode" }
---

# Pre-Granular Fodder (Steady Reverse-Crush for Microcosm)

## Concept
DESIGNED for this rig: hands the Hologram Microcosm a STEADY stream of degraded reverse/bit-crush grains it can reliably capture and loop. Parting GENERATES, Microcosm GRANULARIZES — roles kept distinct. Chance is parked at noon so the stream is consistent enough for Microcosm to lock onto. Filter-LP-before-granular keeps QI Etherealizer off harsh aliasing. This is the documented headline Board-2 pairing (Parting → Microcosm).

## How to play it
1. Set global defaults: Routing Stereo, Trails ON.
2. Pick ONE Dissolve flavor: 3:00 for long reverse, OR 9:00 for heavy bit-crush (this patch documents the reverse variant; swap Dissolve for the crush variant).
3. Park Chance at noon — STEADY is the whole point; a predictable stream for Microcosm to capture.
4. Smear at 11:00 for some diffusion (not a full wall — leave grain detail for Microcosm to chew); Glitch 11:00 fixed clock; Time noon.
5. Shape Envelope so banjo/baritone dynamics gate the grains.
6. Filter LP at 1:00 tames aliasing BEFORE Microcosm/QI re-sample it (keeps Etherealizer off harsh highs).
7. Push Chance high only when you want chaos that Microcosm then freezes.

## Notes
- 🟣 DESIGNED — never found. ⭐ The documented headline Board-2 pairing (Parting → Microcosm).
- Filter-LP-before-granular keeps QI Etherealizer off harsh aliasing.
- Chance-at-noon is what makes the stream capturable rather than chaotic.
- Feedback discipline: with Lost & Found + Microcosm downstream, keep Chance at noon unless deliberately stacking chaos.
- Clocks are DOUG's tuning.
- Reference: rig recipe (DeepResearch §9 "into Hologram Microcosm — the headline pairing"); making aesthetic degraded/reverse + indie-folk cluster 2 ambient room.
- Save target: Preset slot or live mode.

## Sources
- 🟣 designed from `research/Parting-DeepResearch.md` §9 (park Chance near noon for a steady wash Microcosm can capture; keep Filter LP so Etherealizer isn't fed harsh aliasing), §13(d)
- `research/Parting-UsageGuide.md` §5 ("Pre-granular fodder for the Microcosm"). Clocks are DOUG's tuning.
- Transformed from Pedalxly Parting-Patches.md (designed)
