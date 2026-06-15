---
type: patch
title: VHS Tape-Age (Gen Lite, Full Wet)
device: Chase Bliss Lost & Found
date: 2026-06-15
description: A single-slot Gen Lite (6B) VHS-age of the live source — slow wow, tape crinkle, full wet — built as the dedicated AGING stage in front of a separate tape echo. Derived from the factory 'Light Sleeper' combo's Gen Lite half, but minus the Orchestral Swell so the played source keeps its pick attack and dynamics.
tags: [degraded, lo-fi, vhs, tape, wow, gen-lite, designed, signature]
dips:
  SPREAD: off
  TRAILS: on
  UNSYNC: off
hidden:
  GLUE: "10:00–11:00 (light cohesion, tame spikes)"
controls:
  - { name: "ROUTING", type: switch, value: "single channel (reads as believable tape, not per-side chorus)", options: ["L>R", "L+R", "L<R"] }
  - { name: "R slot mode", type: switch, value: "6B Gen Lite (native — no SWAP)" }
  - { name: "TIME (R wow↔flutter)", type: knob, value: "toward MAX = slow wow (the VHS pitch-warp)" }
  - { name: "MODIFY (R depth)", type: knob, value: "12:00–1:00 (warble depth)" }
  - { name: "ALT (R failure/crinkles)", type: knob, value: "10:00–11:00 (tape crinkle)" }
  - { name: "BLEND", type: knob, value: "2:00 toward Gen Lite (sets degrade amount)" }
  - { name: "MIX (RAMP)", type: knob, value: "FULL (Gen Lite wants full wet to read as real tape)" }
  - { name: "FREEZE (HOLD R footswitch)", type: button, value: "TAPE STOP — slowdown gesture" }
  - { name: "Slot/Bank", type: knob, value: "Preset R (live recallable)" }
---

# VHS Tape-Age (Gen Lite, Full Wet)

## Concept
A single-slot Gen Lite (6B) VHS-age of the live played source — slow wow, tape crinkle, full wet — used as the dedicated AGING stage in front of a separate tape echo. Unlike the factory 'Light Sleeper' combo (which pairs Gen Lite with an Orchestral Swell that strips the pick attack), this runs Gen Lite alone so the played guitar/synth keeps its attack and dynamics while getting seasick VHS pitch-warp + crinkle. Built to feed a downstream delay (Big Time) that does the repeats, so the two tape jobs stay split (no GenLoss-on-GenLoss mud).

## How to play it
1. Set R slot = 6B Gen Lite, ROUTING = single channel, MIX FULL, SPREAD OFF, TRAILS on.
2. Play a sustained chord or slow synth pad.
3. Push TIME (R) toward MAX for slow wow — the seasick VHS pitch-warp.
4. Set MODIFY (R) ~12:00–1:00 for warble depth; ALT (R) ~10:00–11:00 for tape crinkle/failure.
5. Set BLEND ~2:00 toward Gen Lite to taste — this sets how degraded the source gets.
6. Feed the output into a separate tape echo (Big Time) for the repeats — don't also run a full Generation Loss in front (Gen Lite IS a mini Gen Loss; doubling = mud).
7. **HOLD the R footswitch = TAPE STOP** as a slowdown gesture.

## Notes
- Gen Lite (6B) is a mini Generation Loss MkII — so this is the ONLY tape-age stage; do not stack a full Generation Loss in front (GenLoss-on-GenLoss mud, the thing this chain is built to avoid).
- SPREAD **OFF** so it reads as believable mono tape rather than per-side chorus.
- Single-slot Gen Lite (not the Light Sleeper Orchestral-Swell combo) keeps the played source's pick attack and dynamics intact for a downstream delay to repeat.
- HONESTY: the clock-face values are a dialable DOUG recipe interpreting the documented Gen Lite control map — NOT factory-published numbers. Dial by ear.

## Sources
- Gen Lite (6B) control map: TIME = wow↔flutter, MODIFY = depth, ALT = failure/crinkles, BLEND = degrade amount, MIX FULL + SPREAD off for believable tape — BachelorMachinesTV Pt1/Pt2 (`research/transcripts/bachelormachinestv-science-part1.md` & `-part2.md`) and the Lost & Found patch maps.
- CB Field Guide: Gen Lite = mode 6B, a mini Generation Loss MkII (`gear/Chase Bliss Lost & Found/GearProfile.md`).
- Designed (DOUG) — single-slot Gen Lite age, derived from the Light Sleeper combo's Gen Lite half minus the Orchestral Swell.
