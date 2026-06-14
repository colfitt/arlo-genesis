---
type: patch
title: Shoegaze Special
device: Chase Bliss Lost & Found
date: 2026-06-14
description: CB's on-aesthetic factory combo — a swirling reverberant bed (Slow-verb into Ensemble Expander) feeding the Microcosm, for shoegaze/post-punk wash from sustained banjo/baritone chords.
tags: [ambient, reverb, shoegaze, post-punk, wash, factory, signature]
dips:
  SPREAD: on
  TRAILS: on
  UNSYNC: off
hidden:
  GLUE: "10:00 (light cohesion)"
  ALT (L diffusion): "2:00–3:00 (smeared)"
  ALT (R Ensemble voices): "noon (≈ 4 voices)"
  EQ: "to taste (push CCW to darken for doom weight)"
controls:
  - { name: "ROUTING", type: switch, value: "L>R series", options: ["L>R", "L+R", "L<R"] }
  - { name: "L slot mode", type: switch, value: "1A Slow-verb" }
  - { name: "R slot mode", type: switch, value: "6A Ensemble Expander" }
  - { name: "MODIFY (L)", type: knob, value: "1:00 (toward A, moderate pre-diffusion feedback)" }
  - { name: "TIME (L)", type: knob, value: "1:00 (medium size)" }
  - { name: "MODIFY (R Ensemble depth)", type: knob, value: "11:00" }
  - { name: "TIME (R Ensemble LFO)", type: knob, value: "10:00" }
  - { name: "BLEND", type: knob, value: "1:00 (toward the chorus / 2nd-effect mix in series)" }
  - { name: "MIX (RAMP)", type: knob, value: "1:00–2:00" }
  - { name: "Slot/Bank", type: knob, value: "Preset L (live recallable)" }
---

# Shoegaze Special

## Concept
CB's named factory Combo and on-aesthetic starting point — *"A swirling, living ambience that is both surreal and loaded with emotion."* The L slot's Slow-verb provides the diffused reverberant bed, and the R slot's Ensemble Expander (≈ 4 voices, Juno-chorus LFO) smears it into swirl. Runs `L>R` series with native channels (Slow-verb = L1, Ensemble = L6, so no SWAP). It sits at the front of Board 2, feeding the Microcosm a shoegaze/post-punk wash from sustained chords.

## How to play it
1. Engage the L>R series chain — play sustained banjo/baritone chords to build the reverberant bed.
2. Let the Slow-verb's pre-diffusion feedback (MODIFY ~1:00) and large smear (ALT diffusion ~2–3:00) bloom.
3. The Ensemble Expander on the R slot adds the swirl — leave it at ~4 voices with a slow LFO.
4. Use BLEND (~1:00, toward the chorus) to set how much of the 2nd effect's mix lands in the series chain.

## Notes
- For doom weight, push MODIFY(L) higher (more feedback) and EQ CCW to darken (cut highs).
- GLUE ~10:00 adds light cohesion to the wet wall.
- Sits at the front of Board 2 → into the Microcosm.
- **Honesty:** Modes + routing = CB Field Guide verbatim; the exact MODIFY / TIME / ALT / BLEND clock positions are suggested starting points (DOUG's), not in the Combo doc.

## Sources
- CB Field Guide "Combos" p.36–37 — `research/links/cb-manual-combos-official-recipes.md`
- Ensemble Juno-chorus map (TIME ~10:00 / MODIFY ~8:00 / ALT ~noon ≈ 4 voices) from BachelorMachinesTV Pt2 — `research/transcripts/bachelormachinestv-science-part2.md`
- Ref: CB Field Guide named Combo "SHOEGAZE SPECIAL"
- Transformed from Pedalxly Lost-and-Found-Patches.md (factory)
