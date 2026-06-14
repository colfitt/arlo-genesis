---
type: patch
title: Drum-Bus / Stereo-Loop Crush
device: JHS Colour Box V2
date: 2026-06-14
description: Print an MPC / Digitakt drum bus or a stereo loop THROUGH the Colour Box for crushed, console-saturated "recorded-wrong" drums — used as a DAW hardware insert. (Lo-fi cluster home turf: blown-out drums, demo-crunch.)
tags: [drums, drum-bus, stereo-loop, crush, console-saturation, lo-fi, hardware-insert, designed, signature]
controls:
  - { name: "HI/LO", type: switch, value: "HI (crush) / LO (gentle glue)", options: ["HI", "LO"] }
  - { name: "STEP", type: knob, value: "2 (gentle) up to 3 (heavy)" }
  - { name: "PRE-VOL", type: knob, value: "12:00 (glue) to 2:00 (crush)" }
  - { name: "MASTER", type: knob, value: "cranked toward 5:00, then trim at the interface" }
  - { name: "TREBLE", type: knob, value: "to taste" }
  - { name: "TREBLE SHIFT", type: knob, value: "to taste" }
  - { name: "MIDDLE", type: knob, value: "+2 (~1:00, snap)" }
  - { name: "MID SHIFT", type: knob, value: "≈1.5–2 kHz" }
  - { name: "BASS", type: knob, value: "to taste" }
  - { name: "BASS SHIFT", type: knob, value: "to taste" }
  - { name: "HI-PASS", type: knob, value: "~9:00 (≈140 Hz, stop the low end pumping)" }
  - { name: "HI-PASS ON/OFF", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "INST/XLR", type: switch, value: "XLR (mandatory for line level; out → interface in)", options: ["INST", "XLR"] }
  - { name: "20 dB PAD", type: switch, value: "ON (line-level drum bus is too hot otherwise)", options: ["on", "off"] }
---

# Drum-Bus / Stereo-Loop Crush

## Concept
Print an MPC / Digitakt drum bus or a stereo loop THROUGH the Colour Box for crushed, console-saturated "recorded-wrong" drums — lo-fi cluster home turf (blown-out drums, demo-crunch). Run it as a DAW hardware insert (Logic "I/O", Ableton "External Audio Effect") for latency-compensated routing. HI mode crushes; LO mode glues gently.

## How to play it
1. Set input to **XLR** (mandatory for line level) and engage the **PAD ON** — the line-level drum bus is too hot otherwise.
2. Pick **HI** for crush or **LO** for gentle glue. STEP 2 (gentle) up to 3 (heavy).
3. PRE-VOL noon (glue) to 2:00 (crush). Crank MASTER toward 5:00, then trim at the interface (the Off Shift "MASTER max" insert recipe).
4. Engage HI-PASS ~9:00 (≈140 Hz) to keep the low end from pumping; boost MIDDLE +2 with MID SHIFT ≈1.5–2 kHz for snap; BASS to taste.
5. XLR out → interface input via a latency-compensated DAW insert.

## Notes
- **DESIGNED** — documented application, inferred dials.
- Tedious per-track: a hardware insert affects everything routed to it, so print/bounce in real time and photograph knob positions for recall.
- Mono device → sum to mono or process the bus as mono.

## Sources
- Designed — application documented by Produce Like A Pro blog: "kick drums… overhead drums, stereo buses, room mics… recorded with the Colour Box; sweeten drum overheads" (`research/links/colour-box-drum-bus-source-applications.md`); line-level/PAD/MASTER-max insert mechanics from Off Shift "How to Use the Colour Box like a Plugin" (`research/transcripts/off-shift-colour-box-like-a-plugin.md`).
- Transformed from Pedalxly Colour-Box-V2-Patches.md (designed).
