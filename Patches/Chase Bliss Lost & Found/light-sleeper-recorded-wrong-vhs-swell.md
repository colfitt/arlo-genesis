---
type: patch
title: Light Sleeper (Recorded-Wrong VHS Swell)
device: Chase Bliss Lost & Found
date: 2026-06-14
description: The most "recorded-wrong" factory combo — a digital Orchestral Swell smeared through Gen Lite (mini Generation Loss) into a VHS-dream-sequence drone for the Microcosm; CB's "VHS-era dream sequence that blends heavily digital and analog sounds."
tags: [degraded, lo-fi, vhs, swell, drone, factory, signature]
dips:
  SPREAD: off
  TRAILS: on
  UNSYNC: off
hidden:
  GLUE: "10:00–11:00 (tame swell spikes)"
  ALT (L feedback): "1:00–2:00"
  ALT (R Gen Lite failure/crinkles): "10:00–11:00"
controls:
  - { name: "ROUTING", type: switch, value: "L>R series", options: ["L>R", "L+R", "L<R"] }
  - { name: "L slot mode", type: switch, value: "2A Orchestral Swell" }
  - { name: "R slot mode", type: switch, value: "6B Gen Lite" }
  - { name: "MODIFY (L pitch interval)", type: knob, value: "UNISON (or oct-down for a synthy non-pitched swell)" }
  - { name: "TIME (L swell/attack)", type: knob, value: "1:00 (removes the pick attack)" }
  - { name: "TIME (R wow↔flutter)", type: knob, value: "toward MAX = slow wow" }
  - { name: "MODIFY (R depth)", type: knob, value: "12:00–1:00" }
  - { name: "BLEND", type: knob, value: "2:00 (toward Gen Lite — sets degrade amount)" }
  - { name: "MIX (RAMP)", type: knob, value: "FULL (CB marks this Combo *)" }
  - { name: "FREEZE (HOLD R footswitch)", type: button, value: "TAPE STOP — slowdown gesture" }
  - { name: "Slot/Bank", type: knob, value: "Preset R (live recallable)" }
---

# Light Sleeper (Recorded-Wrong VHS Swell)

## Concept
CB's named factory Combo and the most "recorded-wrong" of them — *"A VHS-era dream sequence that blends heavily digital and analog sounds together."* A digital Orchestral Swell (2A) is set to UNISON (or oct-down) for a synthy non-pitched swell, then smeared through Gen Lite (6B, a mini Generation Loss MkII) for tape wow and crinkle. Runs `L>R` series, MIX FULL.

## How to play it
1. Set ROUTING `L>R` series, MIX FULL.
2. Play sustained chords — TIME(L) ~1:00 removes the pick attack so the swell reads as orchestral/synthy.
3. Set MODIFY(L) to UNISON (or oct-down) for a non-pitched swell.
4. Gen Lite degrades it: TIME toward MAX = slow wow, ALT ~10–11:00 = failure/crinkles.
5. BLEND ~2:00 toward Gen Lite sets the degrade amount.
6. **HOLD the R footswitch = TAPE STOP** for a slowdown gesture.

## Notes
- SPREAD **OFF** so Gen Lite reads as believable tape rather than per-side chorus.
- Gen Lite ≈ a mini Generation Loss MkII — don't also hammer the full Gen Loss on Board 3 at once (double-degrade).
- GLUE ~10–11:00 tames swell spikes.

## Sources
- CB Field Guide "Combos" (LIGHT SLEEPER = Orchestral Swell > Gen Lite, `L>R` series, `*` = MIX maxed) — `research/links/cb-manual-combos-official-recipes.md`
- Orchestral Swell + Gen Lite maps and "Gen Lite needs full wet, SPREAD off for real tape" from BachelorMachinesTV Pt1/Pt2 — `research/transcripts/bachelormachinestv-science-part1.md` & `-part2.md`
- Ref: CB Field Guide named Combo "LIGHT SLEEPER"
- Transformed from Pedalxly Lost-and-Found-Patches.md (factory)
