---
type: patch
title: Pitch-to-MIDI Banjo Sequencer Driver
device: Roland VG-800
date: 2026-06-14
description: Banjo rolls / baritone lines triggering the Digitakt 2 / Octatrack / MPC — sequenced-synth + motoric territory, uniquely available here.
tags: [pitch-to-midi, banjo, sequencer, designed, signature]
controls:
  - { name: "GUITAR TO MIDI", type: switch, value: "ON (System)", options: ["ON", "OFF"] }
  - { name: "MIDI mode", type: switch, value: "MONO (one channel per string, consecutive; receiver in Mono/Mode-4) or POLY (one timbre)", options: ["MONO", "POLY"] }
  - { name: "PLAY FEEL", type: switch, value: "FEEL3–4 (or NO DYNA + NO-DYNA VELOCITY ~100)" }
  - { name: "LOW VELO CUT", type: knob, value: "2–4" }
  - { name: "BEND RANGE", type: knob, value: "12–24" }
  - { name: "HOLD", type: switch, value: "HOLD1 (keeps notes ringing across re-picks — the fast-decay fix)" }
  - { name: "CONTROL ASSIGN → GUITAR TO MIDI → ALT TUNE", type: switch, value: "ON (transmits the retuned pitches)", options: ["ON", "OFF"] }
  - { name: "Slot/Bank", type: knob, value: "System + per-memory MIDI layer; save alongside a banjo Memory, e.g. U03-2" }
---

# Pitch-to-MIDI Banjo Sequencer Driver

## Concept

Banjo rolls / baritone lines triggering the Digitakt 2 / Octatrack / MPC — sequenced-synth + motoric territory, uniquely available here. `GUITAR TO MIDI = ON` with MONO mode puts each string on its own consecutive MIDI channel (receiver in Mono/Mode-4) so each banjo string maps a different sound with per-string bend; POLY gives one timbre. The banjo-drives-the-samplers move.

## How to play it

1. `System → GUITAR TO MIDI = ON`.
2. MONO mode = one MIDI channel per string (consecutive channels, receiver in Mono/Mode-4) so each string maps a different sound with per-string bend; or POLY for one timbre.
3. Tame spiky triggering: `PLAY FEEL = FEEL3–4` (or `NO DYNA` + `NO-DYNA VELOCITY ~100`), `LOW VELO CUT = 2–4`, `BEND RANGE = 12–24`.
4. `HOLD1` keeps notes ringing across re-picks (the fast-decay fix).
5. To transmit the *retuned* pitches: `CONTROL ASSIGN → GUITAR TO MIDI → ALT TUNE = ON`.
6. Save alongside a banjo Memory (it's a System + per-memory MIDI layer).

## Notes

- Designed; all param names manual-verified.
- Latency is sub-perceptible-but-nonzero ("zero latency" is marketing).

## Sources

- 🟣 designed from UsageGuide §4 + `research/links/vguitarforums-guitar-to-midi.md`
- Transformed from Pedalxly VG-800-Patches.md (DOUG-designed)
