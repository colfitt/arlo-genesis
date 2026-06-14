---
type: patch
title: Banjo-As-Lead Reverse (Envelope-Gated)
device: OBNE Parting
date: 2026-06-14
description: Designed for the rig — each banjo pluck (GK-5 → VG-800) gates the glitch, and Dissolve-into-reverse turns banjo rolls into stretched backwards arpeggios; the most playable Parting mode for plucked transients, carrying banjo as a lead voice inside the texture board.
tags: [banjo, lead, reverse, envelope, playable, signature, designed]
hidden:
  Aux Footswitch (optional Half-Speed for instant down-octave reverse swells): "Half-Speed (optional)"
controls:
  - { name: "Shape", type: switch, value: "Envelope", options: ["Sine", "Square", "Rev Saw", "Saw", "Random Sine", "Random Square", "Envelope"] }
  - { name: "Chance", type: knob, value: "1:00 (Envelope mode = sensitivity/threshold)" }
  - { name: "Dissolve", type: knob, value: "2:00" }
  - { name: "Smear", type: knob, value: "11:00" }
  - { name: "Time", type: knob, value: "11:00" }
  - { name: "Glitch", type: knob, value: "10:00" }
  - { name: "Filter", type: knob, value: "1:00" }
  - { name: "Filter", type: switch, value: "LP", options: ["LP", "HP"] }
  - { name: "Mix", type: knob, value: "12:00" }
  - { name: "Mix", type: switch, value: "Standard", options: ["Standard", "Modified"] }
  - { name: "Mod", type: switch, value: "Tremolo", options: ["Tremolo", "Vibrato"] }
  - { name: "Depth", type: knob, value: "8:00" }
  - { name: "Aux", type: button, value: "Tap (optional: set Aux = Half-Speed for instant down-octave reverse swells)" }
  - { name: "Routing", type: switch, value: "Stereo", options: ["Mono", "Stereo-sum", "Stereo"] }
  - { name: "Trails", type: switch, value: "On", options: ["On", "Off"] }
  - { name: "Slot", type: knob, value: "Preset slot or live mode" }
---

# Banjo-As-Lead Reverse (Envelope-Gated)

## Concept
DESIGNED for this rig: each banjo pluck (GK-5 → VG-800) gates the glitch, and Dissolve-into-reverse turns banjo rolls into stretched backwards arpeggios — banjo carried as a lead voice inside the texture board, not a novelty. This is the most PLAYABLE Parting mode for plucked transients: in Envelope mode the signal only enters the buffer when you play loud, and Chance becomes a sensitivity/threshold so medium-hard plucks trigger while soft passing notes don't.

## How to play it
1. Set global defaults: Routing Stereo, Trails ON.
2. Set Shape to **Envelope** so the signal only enters the buffer when you play loud.
3. Set Chance at 1:00 — in Envelope mode this is sensitivity/threshold; tune so medium-hard banjo plucks trigger, soft passing notes don't.
4. Dissolve at 2:00 (above noon = reverse) so banjo rolls become backwards arpeggios; keep Smear light (11:00) so the reverse stays legible.
5. Time at 11:00 (shorter) so each pluck's reverse stays in time with the rolls.
6. Roll off banjo's piercing 2–4 kHz with Filter LP at 1:00 before Microcosm granularizes it.
7. Optional: set Aux = Half-Speed for instant down-octave reverse swells on a footswitch.

## Notes
- 🟣 DESIGNED — never found. ⭐ Directly serves the banjo-as-lead pillar.
- Envelope is the documented dynamics-reactive mode; the clock/filter choices are DOUG's tuning for banjo transients in this chain.
- In Envelope mode Chance no longer controls random buffer entry (it becomes sensitivity).
- Reference: making aesthetic "banjo-as-lead"; rig-specific recipe (UsageGuide §5).
- Save target: Preset slot or live mode.

## Sources
- 🟣 designed from `research/transcripts/harp-lady-emily-hopkins-official-parting.md` (Envelope = delay grabs notes only when you play loud; Chance = sensitivity)
- `research/Parting-DeepResearch.md` §6 (banjo fast-attack transients ideal envelope fodder; LP filter on banjo's 2–4 kHz)
- `research/Parting-UsageGuide.md` §5.
- Transformed from Pedalxly Parting-Patches.md (designed)
