---
type: patch
title: Gen Lite Tape Warble (Single-Slot, Full Wet)
device: Chase Bliss Lost & Found
date: 2026-06-15
description: "A single-slot Gen Lite (6B, a mini Generation Loss MkII) tape-warble voice that ages a played, modulated source with believable VHS wow + crinkle — full wet, SPREAD off, no swell stage — so it reads as real tape lapping continuously over the source. Derived from the factory 'Light Sleeper' combo's Gen Lite half, stripped of the Orchestral Swell, to sit in front of Big Time and compound the lo-fi collapse on the half-time drop."
tags: [tape, warble, wow, vhs, gen-lite, generation-loss, lo-fi, degraded, designed]
dips:
  SPREAD: off
  TRAILS: on
  UNSYNC: off
hidden:
  GLUE: "10:00–11:00 (light cohesion, tame spikes — optional)"
controls:
  - { name: "ROUTING", type: switch, value: "single channel (run Gen Lite alone — reads as believable tape, not per-side chorus)", options: ["L>R", "L+R", "L<R"] }
  - { name: "R slot mode", type: switch, value: "6B Gen Lite (native — no SWAP)" }
  - { name: "TIME (R wow↔flutter)", type: knob, value: "toward MAX = slow wow (the seasick VHS pitch-warp)" }
  - { name: "MODIFY (R depth)", type: knob, value: "12:00–1:00 (warble depth)" }
  - { name: "ALT (R failure/crinkles)", type: knob, value: "10:00–11:00 (tape crinkle)" }
  - { name: "BLEND", type: knob, value: "1:00–2:00 toward Gen Lite (modest — up-state still reads as clean modulated delay w/ tape character)" }
  - { name: "MIX (RAMP)", type: knob, value: "FULL (Gen Lite wants full wet to read as real tape)" }
  - { name: "Slot/Bank", type: knob, value: "Preset R (live recallable)" }
---

# Gen Lite Tape Warble (Single-Slot, Full Wet)

## Concept
A single-slot Gen Lite (6B, a mini Generation Loss MkII) tape-warble voice that ages WHAT YOU PLAY — a clean, played, modulated source — with believable VHS wow + crinkle, rather than turning it into a swell or pad. Run as one channel (not per-side) at MIX FULL so it reads as real tape. This is deliberately NOT the 'Light Sleeper' factory combo: there is no Orchestral Swell stage, because the chain wants the warble to lap continuously over a played delay, not remove the pick attack. It is the ever-present tape character that sits in front of Big Time and compounds the lo-fi collapse when Big Time drops to half-time.

## How to play it
1. Set R slot to 6B Gen Lite, run as a single channel. SPREAD OFF, MIX FULL, TRAILS on.
2. Push TIME toward MAX for slow wow — the seasick VHS pitch-warp that laps over the source.
3. Set MODIFY ~12:00–1:00 for warble depth; ALT ~10:00–11:00 for tape crinkle/failure.
4. Set BLEND ~1:00–2:00 toward Gen Lite to taste — enough character to read as tape, but not so much the source is already destroyed before Big Time.
5. Play a sustained chord, arpeggio, or synth line into it — the warble ages what you actually play, continuously.
6. Add GLUE ~10:00–11:00 (hidden) for light cohesion if the warble spikes.

## Notes
- Single-slot Gen Lite, NOT the Light Sleeper combo — there is no Orchestral Swell stage here. The point is to warble a played, modulated source, not to swell it into a pad.
- SPREAD **OFF** is essential — it makes Gen Lite read as believable tape instead of per-side chorus.
- Gen Lite IS a mini Generation Loss MkII, so do NOT also run a full Generation Loss in front — that is GenLoss-on-GenLoss mud.
- Keep BLEND modest so the up-state stays "clean modulated delay with tape character"; the real lo-fi collapse happens downstream when Big Time drops to 0.5X half-time.
- MIX FULL: Gen Lite wants full wet to read as real tape.
- HONESTY: the clock-face positions are a DIALABLE DOUG recipe interpreting the documented Gen Lite control map — NOT factory-published numbers. Dial by ear.

## Sources
- Gen Lite = mode 6B, a mini Generation Loss MkII — `gear/Chase Bliss Lost & Found/GearProfile.md`.
- Gen Lite full-wet, SPREAD-off-for-real-tape, TIME-toward-MAX = slow wow, ALT = failure/crinkles — BachelorMachinesTV Pt1/Pt2, via `Patches/Chase Bliss Lost & Found/light-sleeper-recorded-wrong-vhs-swell.md` (Gen Lite stage), stripped of the Orchestral Swell.
- GenLoss-on-GenLoss-mud avoidance precedent — `Chains/lost-found-big-time-stacked-tape-degradation.md`.
- Designed (DOUG) — single-slot Gen Lite warble derived from the documented 6B mode behavior; numeric clock positions are a dialable interpretation, not CB-published.
