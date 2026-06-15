---
type: patch
title: Frozen-Bed Slice Warp
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: "Purpose-built MOOD voice for the Big Time → MOOD freeze chain: micro-loop a SLICE of an externally frozen Big Time bed and time-warp it in Stretch, clock-locked to the Digitakt grid, as a live glitch on top of the held wall. (DOUG-designed; factory features manual-verified, clock-face values are dialable starting points.)"
tags: [freeze, stretch, micro-loop, time-warp, glitch, midi-clock, sync, rig-integration, designed, signature]
dips:
  CLASSIC: "off (clean Stretch transitions) — flip on if you want the slice to detune/alias as it stretches"
hidden:
  SYNC (Wet MODE toggle): LEFT — Micro-Looper synced to Wet, so the captured slice length follows the grid (HOLD both footswitches until LEDs green, then move the Wet MODE toggle LEFT)
controls:
  - { name: "Looper MODE", type: switch, value: "Stretch (the time-warp engine)", options: ["Env", "Tape", "Stretch"] }
  - { name: "Wet MODE", type: switch, value: "Reverb (wash around the slice; switch to Delay if you want the slice to also echo on-grid)", options: ["Reverb", "Delay", "Slip"] }
  - { name: "ROUTING", type: switch, value: "IN+micro-loop", options: ["IN", "IN+micro-loop", "micro-loop only"] }
  - { name: "CLOCK", type: knob, value: "~11:00 (a little grit) — dial by ear" }
  - { name: "MIX", type: knob, value: "~1:00 (featured glitch on top, not a second wall) — dial by ear" }
  - { name: "Looper MODIFY", type: knob, value: "start MAX → ride toward NOON; NOON = frozen grain, infinitely repeats current slice. ⚠️ MAX = no effect" }
  - { name: "Looper LENGTH", type: knob, value: "sizes the held grain (high = clearer phrase, low = blurry/grainy)" }
  - { name: "MIDI clock (CC51 follow / CC53 div wet / CC54 div loop)", type: switch, value: "feed clock from the Digitakt; CC51>0 to follow, CC54 sets loop division" }
  - { name: "RIGHT footswitch (Micro-Looper)", type: button, value: "TAP to grab a slice of the frozen bed" }
  - { name: "LEFT footswitch (Wet)", type: button, value: "HOLD to freeze the Stretch" }
---

# Frozen-Bed Slice Warp

## Concept
Purpose-built MOOD voice for the Big Time → MOOD freeze chain: micro-loop a SLICE of an externally frozen Big Time bed and time-warp it, clock-locked to the Digitakt grid, as a live glitch ON TOP of the held wall. Stretch mode is the time-warp engine; the Micro-Looper grabs the slice; **SYNC + MIDI clock** keep the warped stutter on the same subdivision as the (pre-freeze) Big Time repeats so the glitch sits in the pocket instead of fighting the cloud. Unlike the existing MOOD sheets, this one combines micro-loop capture + Stretch-freeze warp + external MIDI-clock lock specifically over an upstream frozen bed.

## How to play it
1. Set Looper MODE = **Stretch**, Wet MODE = **Reverb**, ROUTING = **IN+micro-loop**, CLOCK ~11:00, MIX ~1:00.
2. Engage **SYNC = LEFT** (HOLD both footswitches until LEDs go green, then flip the Wet MODE toggle LEFT) so the Micro-Looper length follows the grid; feed **MIDI clock** from the Digitakt (CC51>0 to follow, CC54 sets loop division).
3. With the upstream Big Time bed already **FROZEN**, **TAP the RIGHT** (Micro-Looper) footswitch to capture a slice of the held cloud.
4. **HOLD the LEFT** footswitch to freeze the Stretch, then ride **Looper MODIFY toward NOON** to warp/freeze the grain and rotate **LENGTH** to resize it — it stutters on the Digitakt grid.
5. Keep **MIX** moderate: this is a featured glitch on top, not a second wall. Solo over the bed + slice.
6. To collapse: tap the footswitches off (trails ring out).

## Notes
- ⚠️ A stray MIDI **Note** auto-engages MOOD's **Synth Mode, which IGNORES MIDI clock** — send the Digitakt's clock + CC only (no Notes) on MOOD's channel or the glitch grid will free-run.
- **CLASSIC** adds rubbery pitch/aliased grit to the warp — off for clean Stretch transitions, on if you want the slice to detune as it stretches.
- Stereo placement: MOOD sits in the stereo field that Big Time's MISO opens up, so the warped slice can pan against the wide frozen cloud.
- All clock-face knob values are **designed starting points** for this rig — dial by ear, not a published preset.

## Sources
- 🟣 designed (DOUG) for the Big Time → MOOD freeze chain.
- MOOD MkII manual p.17 (SYNC / MIDI clock CC51/CC53/CC54; Synth-Mode-ignores-clock caveat), pp.34–35 (Stretch Mode / Stretching 101 — MODIFY-at-NOON frozen grain, MAX = no effect), Micro-Looper + ROUTING (IN+micro-loop).
- Builds on existing MOOD sheets: stretching-101-frozen-grain-wall, sync, clock-synced-loop-layer, granular-stutter.
- Pairs with CB Big Time — Oceanic Drone Bed (upstream frozen bed) and DT2 MIDI / Clock-Master Rig Template (clock source).
