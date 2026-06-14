---
type: patch
title: Grain Doubler (Clock-Locked Grain Mill)
device: Chase Bliss Lost & Found
date: 2026-06-14
description: Factory combo (CB "GRAIN DOUBLER") — two independent granular voices (both slots = Grain Tumbler) interwoven and clock-locked from the Digitakt, feeding the Microcosm's grain engine even rawer material; non-reverb, so it won't stack with Dark Star/Etherealizer downstream.
tags: [granular, texture, clock-locked, microcosm-feed, factory, signature]
dips:
  LATCH: on
  SPREAD: on
  UNSYNC: off
hidden:
  GLUE: "10:00–11:00 (even grain spikes before the Microcosm)"
controls:
  - { name: "ROUTING", type: switch, value: "L+R parallel", options: ["L>R", "L+R", "L<R"] }
  - { name: "Both slots mode", type: switch, value: "4B Grain Tumbler (requires L SWAP on)" }
  - { name: "L SWAP", type: switch, value: "on (so the left slot can host a right-channel mode)", options: ["on", "off"] }
  - { name: "TIME (slot A)", type: knob, value: "11:00 (shorter loop / single bouncing playhead)" }
  - { name: "MODIFY (slot A feedback-into-buffer)", type: knob, value: "1:00 (grains accumulate)" }
  - { name: "ALT (slot A grain fade)", type: knob, value: "2:00 (smoother/ambient)" }
  - { name: "TIME (slot B)", type: knob, value: "1:00–2:00 (longer loop + more playheads)" }
  - { name: "MODIFY (slot B)", type: knob, value: "12:00–1:00" }
  - { name: "ALT (slot B)", type: knob, value: "10:00 (glitchier)" }
  - { name: "BLEND", type: knob, value: "noon" }
  - { name: "MIX (RAMP)", type: knob, value: "1:00" }
  - { name: "FREEZE (LATCH + HOLD)", type: button, value: "freezes a repeatable grain pattern" }
  - { name: "Slot/Bank", type: knob, value: "Preset bank 2 (BANK dip)" }
---

# Grain Doubler (Clock-Locked Grain Mill)

## Concept
CB's named factory Combo — *"custom clusters of interwoven grains."* Both slots run Grain Tumbler (4B) in parallel, clock-locked from the Digitakt, giving the Microcosm's grain engine even rawer material. Because it is non-reverb, it won't stack with Dark Star / Etherealizer downstream. Slot A is the shorter, accumulating, ambient voice; slot B is the longer, multi-playhead, glitchier voice.

## How to play it
1. Set ROUTING `L+R` parallel, enable **L SWAP** so the left slot can host a right-channel mode.
2. Slot A: TIME ~11:00 (single bouncing playhead), MODIFY ~1:00 (grains accumulate), ALT ~2:00 (smooth).
3. Slot B: TIME ~1–2:00 (longer loop, more playheads), ALT ~10:00 (glitchier).
4. **FRESH-VS-FROZEN move:** LATCH + HOLD one slot to freeze a background grain pattern, play live over it on the other slot, then nudge TIME for new clock-quantized patterns.
5. Sync to the same master clock as Big Time / Blooper (`cb-stack-*` files).

## Notes
- UNSYNC off — incoming MIDI clock auto-overrides UNSYNC and locks both slots.
- GLUE ~10–11:00 evens grain spikes before the Microcosm.

## Sources
- CB Field Guide "Combos" (GRAIN DOUBLER = Grain Tumbler + Grain Tumbler, `L+R` parallel, `L SWAP` on) — `research/links/cb-manual-combos-official-recipes.md`
- Grain Tumbler map (TIME governs loop length + playhead rate + grain count; MODIFY = feedback-into-buffer probability; ALT = grain fade; LATCH + HOLD = frozen repeatable pattern; clock overrides UNSYNC) from BachelorMachinesTV Pt2 — `research/transcripts/bachelormachinestv-science-part2.md`
- Ref: CB Field Guide named Combo "GRAIN DOUBLER"; FRESH VS. FROZEN pattern (CB Field Guide)
- Transformed from Pedalxly Lost-and-Found-Patches.md (factory)
