---
type: patch
title: Degraded
device: Strymon TimeLine
date: 2026-06-14
description: The namesake worn-tape factory preset (25A) — long dirty sustained repeats that build into shoegaze/doom walls; the rig's anchor degraded-tape tone.
tags: [degraded, tape, drone, doom, shoegaze, wall, factory, signature]
controls:
  - { name: "TYPE", type: switch, value: "dTape", options: ["dTape","dBucket","Digital","Dual","Pattern","Reverse","Ice","Lo-Fi","Swell","Trem","Filter","Duck"] }
  - { name: "TIME", type: knob, value: "1000 ms" }
  - { name: "TP SPD", type: switch, value: "Normal", options: ["Normal","Fast"] }
  - { name: "LO END", type: knob, value: "slightly low (bar-graph)" }
  - { name: "TAPDIV", type: switch, value: "Qrtr" }
  - { name: "BOOST", type: knob, value: "0.0 dB" }
  - { name: "REPEATS", type: knob, value: "~2–3:00 (performed — let chords ring)" }
  - { name: "Slot/Bank", type: knob, value: "25A" }
---

# Degraded

## Concept
The TimeLine's namesake worn-tape preset: long, dirty, sustained dTape repeats that pile up into a shoegaze/doom wall. This is the rig's anchor degraded-tape tone — set the time long, push the repeats, and let held chords smear into one another.

## How to play it
1. Load 25A (or save the settings to a user slot).
2. Push REPEATS up to ~2–3:00 and let chords ring for the full wall.
3. Hold sustained notes/chords so the worn-tape character builds across the repeats.

## Notes
- Front-panel constants: MIX 3:00 = 50/50, REPEATS 3:00 = the self-oscillation ceiling, FILTER full-left = OFF / noon = darkest / full-right adds highs.
- HP ~80–120 Hz keeps the baritone out of the mud.
- LO END is printed as a bar-graph on the factory card (read "slightly low"), not a number.
- Firmware v1.88; the pedal only receives MIDI clock (always a slave).

## Sources
- research/links/strymon-factory-presets-full-list.md (Strymon factory bank 25A)
- Transformed from Pedalxly TimeLine-Patches.md (factory)
