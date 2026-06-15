---
type: patch
title: "UltraTap — Chop=Swell Violining (+ DynaVerb alt)"
device: Eventide H90
date: 2026-06-15
description: "Auto-swell every note like a violin or volume-pedal player without your hands, via UltraTap's Chop set to a Swell shape — great for ambient pads and cinematic builds. Eventide staff (Brock) recipe, with the DynaVerb swell engine as an alternative and the apalazzolo 'play distinct rests' gate technique."
tags: [ultratap, dynaverb, swell, violining, ambient, pad, signature]
dips:
  TECHNIQUE: "play distinct rests between notes to reset the gate; map Rise or Mix to expression for manual control"
controls:
  - { name: "Algorithm", type: switch, value: "UltraTap (start from factory 'UltraSwell')", options: ["UltraTap", "DynaVerb"] }
  - { name: "Chop", type: knob, value: "set to a Swell option (this is the swell engine)" }
  - { name: "Rise", type: knob, value: "dial for swell speed/attack (longer = slower, more violin-like)" }
  - { name: "Spread", type: knob, value: "tap spacing — centered = even, CW bunches later, CCW bunches early" }
  - { name: "(most other params)", type: knob, value: "0 as a clean start" }
  - { name: "DynaVerb Threshold (alt)", type: knob, value: "trigger level for the swell" }
  - { name: "DynaVerb Release (alt)", type: knob, value: "gate re-trigger time" }
---

# UltraTap — Chop=Swell Violining (+ DynaVerb alt)

## Concept
Auto-swell every note like a violin or volume-pedal player without your hands. UltraTap's Chop, set to a Swell shape, becomes the swell engine — each note fades in instead of attacking, so the H90 plays the volume pedal for you. Great for ambient pads and cinematic builds. The DynaVerb algorithm offers an alternative swell engine via its Threshold/Release gate, and the two can run parallel. Distinct from the existing ultratap-gate-bowed-string-swell (which uses the GATE) — this is the Chop=Swell + DynaVerb pairing.

## How to play it
1. Load **UltraTap** and set most params to 0 for a clean start (or start from the factory "UltraSwell" program).
2. Set **Chop** to a Swell option, then dial **Rise** for the swell speed/attack (longer Rise = slower, more violin-like).
3. Play notes with clear **rests between them** to retrigger each swell independently — note length loosely sets swell length.
4. Add a reverb after (or run a **parallel DynaVerb**) to smooth the release into a pad.
5. **Alt engine:** use DynaVerb's **Threshold** (trigger level) and **Release** (gate re-trigger) as the swell instead of UltraTap.

## Notes
- **No published values** — Brock's staff post gives the control *targets* ("Adjust Chop - Swell and Rise"; DynaVerb Threshold/Release as an alternative) but not a full knob table. Treat the values above as a dialable recipe, not sourced numbers.
- Play **distinct rests** to reset the gate so each note swells on its own; map **Rise** or **Mix** to an expression pedal for manual control.
- apalazzolo's looper trick: track into a looper, swap presets, and play over the loop — using rests to reset the gate keeps each new note swelling cleanly.
- Spread is the tap-spacing control (centered = even taps, CW bunches them later, CCW bunches them earlier) — useful for shaping the swell's body.

## Sources
- https://www.eventideaudio.com/forums/topic/swell-or-violoning-effect-with-the-h90/ (brock: Chop=Swell + Rise; DynaVerb Threshold/Release as alternative — staff, technique-level)
- https://patchstorage.com/nine-h90-ambient-pad-soundscape-programs/ (apalazzolo: UltraSwell technique, play rests to reset gate)
- research/links/eventide-forum-shimmer-swell-modechoverb-techniques.md (swell/violining thread, staff brock + tbskoglund)
- Provenance: Eventide staff (Brock/tbskoglund) + PatchStorage (apalazzolo) — control targets published, values dialable
