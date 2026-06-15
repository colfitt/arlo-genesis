---
type: patch
title: Tape-Bait Octave-Down Drone
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: "Purpose-built for the Big Time → MOOD two-clock chain: MOOD's Tape micro-looper snatches a slice of the already-degraded, clock-locked Big Time repeats and drops it an octave via half-speed (MODIFY 0.5×) for a pulsing sub-heavy tape drone, loop length locked to the shared rig clock. (DOUG-designed; Tape octave-quantized MODIFY / SYNC / MIDI CCs are factory features, knob feels are a dialable recipe.)"
tags: [tape, octave-down, half-speed, drone, sync, midi-clock, micro-loop, rig-integration, designed, signature]
hidden:
  SYNC (Wet MODE toggle): LEFT — Micro-Looper synced to Wet
controls:
  - { name: "Looper MODE", type: switch, value: "Tape", options: ["Env", "Tape", "Stretch"] }
  - { name: "Wet MODE", type: switch, value: "Reverb (thin glue wash; flip to Delay if you want the slice to re-echo on-grid)", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Looper MODIFY", type: knob, value: "0.5× (octave-quantized half-speed = the octave-down drop; MODIFY is octave-quantized .5× / 1× / 2× / 4×, forward or reversed)" }
  - { name: "CLOCK", type: knob, value: "kept HIGHER (preserve low-end; do NOT slam CCW)" }
  - { name: "MIX", type: knob, value: "~1:00 (dialed by ear)" }
  - { name: "Looper LENGTH", type: knob, value: "resizes the captured slice (dialed by ear)" }
  - { name: "MIDI clock (CC51 follow / CC54 div loop)", type: switch, value: "CC51>0 to follow; CC54 sets the loop division to an even subdivision of the Big Time CC54 grid" }
---

# Tape-Bait Octave-Down Drone

## Concept
Purpose-built for the Big Time → MOOD two-clock chain. MOOD's Tape micro-looper grabs a slice of the already-degraded, clock-locked Big Time multitap pattern and drops it an octave via half-speed playback, turning the played rhythm into a slow pulsing drone that sits underneath you. SYNC ties the Tape loop to the Wet channel and MIDI clock makes the loop length an even subdivision of the Big Time grid, so the octave-down drone pulses WITH the repeats rather than smearing across them. CLOCK is kept HIGHER (not slammed CCW) on purpose: half-speed Tape already drops the octave, and aggressive low-CLOCK downsampling thins the bass fundamental you are trying to feature — the grit comes from the pre-degraded source (Generation Loss + Big Time 0.5X), not from starving the clock.

## How to play it
1. Set Looper MODE = **Tape** and Wet MODE = **Reverb** (a thin wash to glue the pulses; use **Delay** if you want the slice to also re-echo on-grid).
2. Engage **SYNC = LEFT**: hold both footswitches until the LEDs go green (hidden-options mode), then move the Wet MODE toggle to LEFT so the Micro-Looper syncs to the Wet channel.
3. Feed **MIDI clock** from the rig master (DT2): send **CC51>0** to follow the clock and **CC54** to set the loop division so the Tape loop length is an even (2:1 / 4:1) subdivision of the Big Time grid.
4. Set Tape **MODIFY = 0.5×** for the octave-down half-speed drop. Keep **CLOCK higher** rather than slammed CCW to preserve the bass fundamental.
5. With Big Time's clock-locked repeats running, tap the **RIGHT (Micro-Looper)** footswitch to grab a slice of the pattern.
6. **Hold LEFT** to freeze the Tape loop into a sustained pulsing drone; ride **LENGTH** to resize the captured slice and flip **MODIFY 0.5× ↔ 1×** to drop or restore the octave live.
7. Solo / comp over the drone while the Big Time repeats keep ticking on top; to collapse, tap MOOD off and hold Big Time MODE to panic-reset.

## Notes
- ⚠️ MIDI clock is **IGNORED in Synth Mode**, and a stray MIDI Note auto-engages Synth Mode — keep the DT2 sending clock + CC only (no Notes) to MOOD's channel.
- Keep **CLOCK higher, not slammed CCW**: half-speed Tape playback already drops the octave; low-CLOCK downsampling on top thins the very low end you are trying to feature.
- The octave-down is real (Tape MODIFY 0.5×) and the rhythmic lock is real (one shared clock, CC54 on both MOOD and Big Time) — this is not a pitch shifter or a free-running glitch.
- Knob feels (**CLOCK / MIX / LENGTH**) are a dialable recipe, not factory-recallable numbers; Tape MODIFY octave-quantization, SYNC, and the MIDI CCs are sourced factory features.

## Sources
- 🟣 designed (DOUG) for the Big Time → MOOD two-clock rhythmic tape-drone chain — knob feels are dialable starting points, not published presets.
- Tape octave-quantized MODIFY (.5×/1×/2×/4×, fwd/reverse) and slow-CLOCK-grit mechanics: Patches/Chase Bliss MOOD MkII/gritty-tape-loop.md (manual pp.32–33 "Tape Mode").
- Octave-down Tape variant + keep-CLOCK-higher-to-preserve-low-end + SYNC + MIDI CC51/CC53/CC54 lock: Patches/Chase Bliss MOOD MkII/clock-synced-loop-layer.md (MOOD-MkII-DeepResearch §13(d)/§6 + manual SYNC).
- SYNC toggle mechanics (hold both footswitches → Wet MODE toggle LEFT) and Synth-Mode-ignores-clock / stray-Note caveat: Patches/Chase Bliss MOOD MkII/sync.md (manual p.17, MOOD-MkII-UsageGuide §5).
