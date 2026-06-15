---
type: patch
title: Grain Tumbler → Gen Lite Re-Age
device: Chase Bliss Lost & Found
date: 2026-06-15
description: "Dialable recipe (not a published CB Combo) — a series re-grain-then-re-age cascade for a decayed delay loop: Grain Tumbler (4B) re-chews a crumbling incoming repeat into a longer, accumulating grain bed, then Gen Lite (6B, a mini Generation Loss MkII) applies wow/flutter + crinkle so each pass arrives audibly older. Distinct from the parallel clock-locked Grain Doubler and from Light Sleeper (Orchestral Swell → Gen Lite)."
tags: [granular, degraded, tape, gen-lite, re-age, designed, signature]
dips:
  SPREAD: off
  TRAILS: on
  UNSYNC: off
  LATCH: on
hidden:
  GLUE: "10:00–11:00 (tame grain spikes before the output)"
controls:
  - { name: "ROUTING", type: switch, value: "L>R series", options: ["L>R", "L+R", "L<R"] }
  - { name: "L slot mode", type: switch, value: "4B Grain Tumbler (enable L SWAP if the left slot won't host a right-side mode)" }
  - { name: "R slot mode", type: switch, value: "6B Gen Lite" }
  - { name: "TIME (L loop length / playheads)", type: knob, value: "12:00–1:00 (longer loop / multiple playheads)" }
  - { name: "MODIFY (L feedback-into-buffer)", type: knob, value: "1:00 (grains accumulate)" }
  - { name: "ALT (L grain fade)", type: knob, value: "1:00–2:00 (smoother/ambient)" }
  - { name: "TIME (R wow↔flutter)", type: knob, value: "toward MAX = slow wow" }
  - { name: "MODIFY (R depth)", type: knob, value: "12:00–1:00" }
  - { name: "ALT (R Gen Lite failure/crinkles)", type: knob, value: "10:00–11:00" }
  - { name: "BLEND", type: knob, value: "2:00 (toward Gen Lite — sets re-age depth)" }
  - { name: "MIX (RAMP)", type: knob, value: "1:00" }
  - { name: "FREEZE (LATCH + HOLD L)", type: button, value: "freezes a repeatable grain pattern to solo over or resample" }
  - { name: "TAPE STOP (HOLD R footswitch)", type: button, value: "slowdown gesture to end the loop" }
---

# Grain Tumbler → Gen Lite Re-Age

## Concept
A series re-grain-then-re-age cascade: Grain Tumbler (4B) re-chews an incoming decayed loop into a longer, accumulating grain bed; Gen Lite (6B, a mini Generation Loss MkII) then applies wow/flutter and crinkle so the already-crumbling repeats come out audibly older. Distinct from the existing Grain Doubler (dual Grain Tumbler in parallel, clock-locked Microcosm-feed) and Light Sleeper (Orchestral Swell → Gen Lite) — this is specifically Grain Tumbler INTO Gen Lite in series to extend and re-age a degraded source.

## How to play it
1. Set ROUTING `L>R` series, L slot = 4B Grain Tumbler, R slot = 6B Gen Lite.
2. Feed the decayed Big Time loop into the L input.
3. Grain Tumbler: TIME ~12–1:00 + MODIFY ~1:00 so grains accumulate into a longer bed; ALT ~1–2:00 for grain-fade smoothness.
4. Gen Lite: TIME toward MAX for slow wow, ALT ~10–11:00 for failure/crinkles; BLEND ~2:00 toward Gen Lite sets how much older the output reads.
5. LATCH + HOLD the Grain Tumbler to freeze a repeatable grain pattern to solo over or to resample.
6. **HOLD the R footswitch = TAPE STOP** for a slowdown gesture to end the loop.

## Notes
- **Dialable recipe** — this is *not* a named CB factory Combo. The Grain Tumbler 4B and Gen Lite 6B mode maps are sourced; the `L>R`-series-into-Gen-Lite combination and all knob positions are designed starting points, not published combo values.
- SPREAD **off** so Gen Lite reads as believable tape rather than per-side chorus.
- Gen Lite ≈ a mini Generation Loss MkII — it carries the tape-age; don't also hammer a full Generation Loss elsewhere in the chain (double-degrade).
- GLUE ~10–11:00 evens grain spikes before the output.
- UNSYNC off — incoming MIDI clock auto-locks the slots if you clock it.
- Hosting two modes may need **L SWAP** depending on slot native side (Grain Tumbler is a right-side mode) — enable L SWAP if the L slot won't host 4B.

## Sources
- Grain Tumbler (4B) map — TIME governs loop length / playhead rate / grain count, MODIFY = feedback-into-buffer, ALT = grain fade, LATCH + HOLD = frozen repeatable pattern — from `Patches/Chase Bliss Lost & Found/grain-doubler-clock-locked-grain-mill.md` + BachelorMachinesTV Pt2.
- Gen Lite (6B = mini Generation Loss MkII) re-age map — TIME→MAX slow wow, ALT failure/crinkles, SPREAD off for believable tape, GLUE tames spikes — from `Patches/Chase Bliss Lost & Found/light-sleeper-recorded-wrong-vhs-swell.md` + BachelorMachinesTV Pt1/Pt2.
- ROUTING `L>R` series + BLEND/MIX/RAMP + GLUE + TAPE STOP behavior from `gear/Chase Bliss Lost & Found/GearProfile.md` and L&F patch sheets.
- L&F manual — `gear/Chase Bliss Lost & Found/manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf`.
- 🟣 designed (DOUG-built; mode maps sourced, the Grain Tumbler→Gen Lite series combination + knob positions are a dialable recipe, not a published Combo).
