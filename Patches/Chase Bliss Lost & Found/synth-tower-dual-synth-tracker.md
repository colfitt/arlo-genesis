---
type: patch
title: Synth Tower (Dual Synth Tracker)
device: Chase Bliss Lost & Found
date: 2026-06-14
description: Factory combo (CB "SYNTH TOWER") — two different synth voices following each chord (Impulse Synth sub-octave weight + Sympathetic Resonator pipes); cinematic doom low-end from baritone/Jazz-bass when the ALT octave is dropped.
tags: [synth, pitch-tracking, doom, cinematic, sub-octave, factory, signature]
dips:
  SPREAD: on
  TRAILS: on
hidden:
  GLUE: "11:00 (Impulse Synth is dynamic — glue evens it)"
  ALT (L attack/release): "long attack = short release; pick a slow attack for pads"
  ALT (R octave): "−1 for sub weight"
controls:
  - { name: "ROUTING", type: switch, value: "L+R parallel", options: ["L>R", "L+R", "L<R"] }
  - { name: "L slot mode", type: switch, value: "5A Impulse Synthesizer (requires L SWAP on)" }
  - { name: "R slot mode", type: switch, value: "5B Sympathetic Resonator" }
  - { name: "L SWAP", type: switch, value: "on (both modes live on the right channel natively)", options: ["on", "off"] }
  - { name: "MODIFY (L brightness)", type: knob, value: "11:00–12:00 (keep darker for doom)" }
  - { name: "TIME (L portamento)", type: knob, value: "10:00" }
  - { name: "MODIFY (R feedback)", type: knob, value: "2:00" }
  - { name: "BLEND", type: knob, value: "noon" }
  - { name: "MIX (RAMP)", type: knob, value: "FULL (CB marks *)" }
  - { name: "Play style", type: button, value: "Play BLOCK CHORDS struck together (rolled chords only voice the last note)" }
  - { name: "Slot/Bank", type: knob, value: "Preset bank 2 (BANK dip)" }
---

# Synth Tower (Dual Synth Tracker)

## Concept
CB's named factory Combo — *"Two different synths following your every move in their own way."* The Impulse Synthesizer (5A) tracks chords with sub-octave weight; the Sympathetic Resonator (5B) adds pipe voices. Drop the ALT octave (−1) on the Resonator for cinematic doom low-end from baritone or Jazz-bass. Runs `L+R` parallel — requires L SWAP on, since both modes live on the right channel natively.

## How to play it
1. Set ROUTING `L+R` parallel, enable **L SWAP**, MIX FULL.
2. **Play BLOCK CHORDS struck together** — rolled chords only voice the last note.
3. Impulse Synth: keep MODIFY (brightness) ~11–12:00 for doom; pick a slow attack (ALT) for pads.
4. Sympathetic Resonator: MODIFY feedback ~2:00, ALT octave −1 for sub weight.
5. BLEND ~noon balances the two synth voices.

## Notes
- Impulse Synth is register-sensitive — play down an octave for fuller tracking.
- **NOT for fast leads** ("it will not keep up").
- For Jazz-bass sub weight, watch GLUE/MIX so the wet doesn't muddy the fundamental.
- GLUE ~11:00 evens the dynamic Impulse Synth.

## Sources
- CB Field Guide "Combos" (SYNTH TOWER = Impulse Synthesizer + Sympathetic Resonator, `L+R` parallel, `L SWAP` on, `*`) — `research/links/cb-manual-combos-official-recipes.md`
- Impulse Synth map (MODIFY = brightness, TIME = portamento, ALT = attack↔release tradeoff, register-dependent, strike block chords) from BachelorMachinesTV Pt2 + community-tips — `research/transcripts/bachelormachinestv-science-part2.md` & `research/links/community-tips-gotchas-firmware.md`
- Ref: CB Field Guide named Combo "SYNTH TOWER"
- Transformed from Pedalxly Lost-and-Found-Patches.md (factory)
