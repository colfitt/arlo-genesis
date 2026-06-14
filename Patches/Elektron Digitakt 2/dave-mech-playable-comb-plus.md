---
type: patch
title: Dave Mech Playable Comb+ (key-tracked, depth 8)
device: Elektron Digitakt 2
date: 2026-06-14
description: Play the Comb+ filter as a tuned 12-tone string/pluck instrument across the keys — key-track FREQUENCY at DEPTH 8, per Dave Mech.
tags: [banjo, comb, string, keytrack, playable, factory, artist, signature]
controls:
  - { name: "OS", type: switch, value: "1.10+" }
  - { name: "FLTR", type: switch, value: "Comb+ (Comb- = more tube-like, acts as delay at high feedback)", options: ["Lowpass 4","Lowpass 2","Highpass","Bandpass","Comb+","Comb-"] }
  - { name: "Key-track destination", type: switch, value: "Comb+ FREQUENCY (key-tracking mod matrix)" }
  - { name: "Key-track DEPTH", type: knob, value: "8 (each note maps to the 12-note scale)" }
  - { name: "Source", type: switch, value: "A very short 'blip' sample" }
  - { name: "LP filter", type: knob, value: "sets how plucky↔stringy — dial by ear" }
  - { name: "FEEDBACK", type: knob, value: "sets how long it rings — dial by ear" }
  - { name: "Send FX", type: knob, value: "add to taste" }
---

# Dave Mech Playable Comb+ (key-tracked, depth 8)

## Concept
Plays the Comb+ filter as a tuned 12-tone string/pluck instrument across the keys. In the key-tracking mod matrix, Comb+ `FREQUENCY` is set as a key-track destination at DEPTH 8, so each note maps to the 12-note scale and you literally play the comb filter. Excited by a very short blip sample, with LP setting plucky↔stringy and FEEDBACK setting ring time.

## How to play it
1. OS 1.10+. In the key-tracking mod matrix, set Comb+ `FREQUENCY` as a key-track destination at DEPTH = 8 → each note maps to the 12-note scale, so you *play* the comb filter.
2. Excite it with a very short "blip" sample.
3. `LP` filter sets how plucky↔stringy; `FEEDBACK` sets how long it rings.
4. Add send FX.
5. (Comb− = more tube-like; works as a delay at high feedback.)

## Notes
- `DEPTH = 8` is the one verified number; `LP`/`feedback` are dial-by-ear.
- Feed a real banjo pluck through it for a detuned metallic resonator (the dossier move).
- Same "Comb Banjo" preset family; assign to a melodic track.

## Sources
- Ref: Dave Mech — "Digitakt II OS 1.10 Deep Dive" (yt `g5v11gs8MXc`).
- `research/transcripts/davemech-dt2-os110-deep-dive.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (factory/artist)
