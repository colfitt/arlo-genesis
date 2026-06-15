---
type: patch
title: "Real Sidechain — Kick-Ducked Pump"
device: Chase Bliss Clean
date: 2026-06-15
description: "The actual-jack sidechain move: flip the SIDECHAIN dip and feed an external kick / drum machine / sequencer into the 1/8\" sidechain input so the pad or bus ducks on every kick hit — classic sidechain pumping, in hardware, in stereo. Bass Fox's headline production trick (Quincas Moreira demo): a stereo pad through Clean keyed by the kick, recorded back to its own track. Distinct from the jack-free pseudo-sidechain approach."
tags: [sidechain, ducking, pumping, bus, electronic, pump, artist]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: "on (real sidechain — external key into the 1/8\" TS jack)"
  Latch: off
  Spread: "off (ON optional for a stereo pad)"
  MISO: "off (ON optional for a stereo pad)"
hidden:
  Envelope Balance (EQ knob): "HPF the trigger (CW) so a full loop ducks mainly on the kick, not the bass"
controls:
  - { name: "Sensitivity", type: knob, value: "set by the left LED so the kick pushes the bus down on every hit" }
  - { name: "Dynamics", type: knob, value: "into LIMITING for pump depth (dial to taste — no published value)" }
  - { name: "Attack", type: knob, value: "shapes the pump onset (dial to taste — no published value)" }
  - { name: "Wet", type: knob, value: "output level" }
  - { name: "Dry", type: knob, value: "DOWN for the pure ducked sound (parallel up for a softer pump)" }
  - { name: "EQ", type: knob, value: "to taste (Envelope Balance lives on its Hidden Option page)" }
  - { name: "Release", type: switch, value: "to taste — sets how fast the bus recovers between hits", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
---

# Real Sidechain — Kick-Ducked Pump

## Concept
Flip the SIDECHAIN dip and feed an external source — a kick drum, drum machine, or sequencer — into Clean's 1/8" TS sidechain input so the pad or full bus ducks on every kick hit. This is true hardware sidechain pumping, in stereo: Bass Fox's headline production trick (from the Quincas Moreira demo) runs a stereo pad through Clean keyed by the kick and records the ducked output back to its own track. It is distinct from the Pseudo-Sidechain Bus Limiter patch — that one uses no jack and lets a hot kick over-trigger the bus; this one uses the actual jack and an external key.

## How to play it
1. **Flip the SIDECHAIN dip ON.**
2. Patch the kick / clock / sequence (Digitakt, MPC, ZOIA) into the 1/8" sidechain input.
3. Run the pad or full bus through Clean's main I/O — stereo (Spread/MISO optional for a stereo pad) if you want the production result.
4. Set Dynamics into LIMITING and Sensitivity by the left LED so the kick pushes the bus down on every hit; shape the pump with Attack and the Release toggle.
5. If a full loop triggers it, use **Envelope Balance** (Hidden Option under the EQ knob — hold both footswitches until the LEDs go green) to HPF the trigger so mainly the kick pumps it.
6. Dry DOWN for the cleanest ducking; record Clean's output to its own track.

## Notes
- **No published clock-face values** — Bass Fox's settings were stored in a preset, so the Dynamics/Attack/Sensitivity figures here are a dialable recipe, not sourced numbers. Set Sensitivity and pump depth by the LED and by ear.
- Distinct from the Pseudo-Sidechain patch: this uses the actual jack and an external key. Ricky Tinez prefers the jack-free version "so the sounds fight against one another."
- The sidechain input keys EQ and swells too, not just compression — you can duck a filter or trigger a swell from the external source.
- Pedal Collaborative demoed sidechaining bleep/bloop sounds from an Empress ZOIA into Clean.

## Sources
- `research/transcripts/bassfox-quincas-moreira-studio-tool-sidechain.md` (keys/pad through Clean with SIDECHAIN engaged, keyed by kick; pad ducks on every kick; recorded stereo output to a track)
- `research/transcripts/chase-bliss-clean-official-video-manual.md` (SIDECHAIN: external signal controls comp/EQ/swells via the 1/8" input)
- Chase Bliss Clean official manual (Customize SIDECHAIN pp.34–35, Envelope Balance p.19)
- thepedalcollaborative.com/sidechain-compression-on-chase-bliss-clean
- gearnews.com/chase-bliss-clean-revolutionary-compression
- Ref: Quincas Moreira / Bass Fox (real-sidechain production move) — dialable recipe, no published values
