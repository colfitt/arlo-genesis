---
type: patch
title: Doom Slip Micro-Loop Mangle
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: "DOUG-designed last-in-chain MOOD voice for the Hizumitas → Big Time → MOOD doom micro-loop chain: route a SLICE of an externally frozen Big Time fuzz-echo bed through the Wet/Slip channel and a Stretch micro-looper, then pitch-bend and stutter it MIDI-clock-locked to the upstream Big Time grid as a featured glitch over the doom wall. (Mode/routing/SYNC/CC mechanics are manual-verified; all clock-face values are a dialable recipe, not published preset values.)"
tags: [slip, micro-loop, stretch, glitch, stutter, pitch-bend, doom, midi-clock, rig-integration, designed, signature]
hidden:
  SYNC (Wet MODE toggle): LEFT — Micro-Looper synced to Wet, so the captured slice length follows the grid (HOLD both footswitches until LEDs green, then move the Wet MODE toggle LEFT)
controls:
  - { name: "Wet MODE", type: switch, value: "Slip (the pitch-bend/stutter engine that mangles the routed slice)", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Looper MODE", type: switch, value: "Stretch (the micro-looper that grabs/resizes the slice)", options: ["Env", "Tape", "Stretch"] }
  - { name: "ROUTING", type: switch, value: "IN+micro-loop (route the captured bed through the Wet/Slip channel)", options: ["IN", "IN+micro-loop", "micro-loop only"] }
  - { name: "MIX", type: knob, value: "~1:00 (featured glitch over the doom slab, not a second wall) — dial by ear, no published value" }
  - { name: "CLOCK", type: knob, value: "~11:00 (a little grit) — dial by ear, no published value" }
  - { name: "Wet MODIFY", type: knob, value: "off neutral, ride in semitone steps to pitch-bend the slice; CCW of noon = reverse (dial by ear, no published value)" }
  - { name: "Looper LENGTH", type: knob, value: "to taste — rotate to resize the held slice (dial by ear, no published value)" }
  - { name: "MIDI clock (CC51 follow / CC54 div loop)", type: switch, value: "CC51>0 to follow; CC54 sets the micro-loop division. Big Time is master via CC110 (60–240 BPM) so MOOD's stutter locks to the Big Time grid" }
  - { name: "RIGHT footswitch (Micro-Looper)", type: button, value: "TAP to grab a slice of the frozen Big Time bed" }
  - { name: "LEFT footswitch (Wet / Slip)", type: button, value: "HOLD to freeze the Slip into its glitchy synth" }
---

# Doom Slip Micro-Loop Mangle

## Concept
Purpose-built for the Hizumitas → Big Time → MOOD doom micro-loop chain. MOOD sits last and treats the frozen Big Time fuzz-echo bed as fodder: a Slip-mode Wet channel plus a Stretch micro-looper grab a sliver of the held wall, then pitch-bend and stutter it on the shared clock grid. Distinct from the existing 'Slip-Reverb Smear' (doom drift, no incoming frozen bed / no clock lock), 'Looper Remixer' (factory chromatic key-changer, no doom framing) and 'Granular Stutter' (Env, Reverb wet) — this one is Slip-on-a-routed-micro-loop, MIDI-clock-locked to an upstream Big Time HOLD bed, voiced as a featured glitch over a doom slab. ROUTING IN+micro-loop so the captured bed runs through the Wet (Slip) channel; SYNC LEFT ties the loop length to Wet; CC51/CC54 lock the loop division to the Big Time master clock. Tap RIGHT to grab a slice, hold LEFT to freeze the Slip, ride MODIFY (semitone steps, CCW of noon = reverse) to pitch-bend and rotate LENGTH to resize.

## How to play it
1. Set Wet MODE = **Slip**, Looper MODE = **Stretch**, ROUTING = **IN+micro-loop**, MIX ~1:00, CLOCK ~11:00.
2. Set **SYNC = LEFT**: hold both footswitches until the LEDs go green, then move the Wet MODE toggle to the LEFT position (Micro-Looper synced to Wet).
3. Feed **MIDI clock** from the upstream Big Time master (CC110, 60–240 BPM); send **CC51>0** to follow and **CC54** to set the loop division so MOOD's stutter locks to the Big Time grid.
4. With the Big Time bed **frozen** (its RIGHT footswitch held), **TAP MOOD's RIGHT** (Micro-Looper) footswitch to grab a slice of the frozen wall.
5. **HOLD MOOD's LEFT** (Wet/Slip) footswitch to freeze the Slip, then ride **MODIFY** off neutral (semitone steps; CCW of noon = reverse) to pitch-bend the slice and rotate **Looper LENGTH** to resize it — the slice stutters on the Big Time grid.
6. Keep **MIX** moderate so the glitch rides on top of the doom bed instead of becoming a second wall. To collapse, tap MOOD's footswitches off.

## Notes
- Built to sit last in the Hizumitas → Big Time → MOOD doom micro-loop chain; the incoming Big Time HOLD bed is the fodder, so the patch only sounds right downstream of a frozen/echo bed.
- ⚠️ A stray MIDI **Note** auto-engages **Synth Mode, which ignores clock** — keep the Big Time master sending clock + CC only (no Notes) on MOOD's channel, or the micro-loop will drift off the grid.
- **MIX stays moderate** — this is a featured glitch over a doom slab, not a second wall; let the Big Time bed own the low-mids.
- All numeric/clock-face positions are a **dialable recipe** (no published MOOD preset values). The Wet MODE / Looper MODE / ROUTING / SYNC-LEFT / CC51-CC54 mechanics are the sourced, load-bearing part.
- Distinct from **Slip-Reverb Smear** (doom drift, no incoming frozen bed, no clock lock), **Looper Remixer** (factory chromatic key-changer), and **Granular Stutter** (Env + Reverb wet).

## Sources
- 🟣 designed (DOUG) — purpose-built for the Hizumitas → Big Time → MOOD doom micro-loop chain. Mode/routing/SYNC/CC mechanics sourced; all knob/clock-face positions are a dialable recipe (no published MOOD preset values).
- Chase Bliss MOOD MkII manual, "Slip Mode" pp.26–27 (semitone-stepped MODIFY, CCW = reverse, TIME = sample size; Looper Remixer = Slip on a routed micro-loop).
- Chase Bliss MOOD MkII manual p.17 + Patches/Chase Bliss MOOD MkII/sync.md (SYNC hidden option: LEFT = Micro-Looper synced to Wet; MIDI clock CC51 follow / CC54 loop division; Synth-Mode-ignores-clock caveat).
- gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md (Big Time as clock master via CC110, 60–240 BPM; CC54 subdivision).
- Patches/EarthQuaker Devices Hizumitas/granular-glitch-capture-drone.md (sustained Hizumitas source makes the downstream capture/micro-loop sound intentional rather than choppy — Wata-adjacent technique).
