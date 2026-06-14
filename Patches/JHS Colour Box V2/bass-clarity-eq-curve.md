---
type: patch
title: Bass Clarity EQ Curve
device: JHS Colour Box V2
date: 2026-06-14
description: Adds presence/articulation to a clean bass DI without thinning the low end ("clarity without taking any booty out") — demonstrates using the BASS band as a low-mid cut by sweeping its SHIFT up to free the MID band of mud.
tags: [bass, di, clarity, eq, semi-parametric, community]
controls:
  - { name: "HI/LO", type: switch, value: "LO", options: ["HI", "LO"] }
  - { name: "STEP", type: knob, value: "2–3 clicks in (≈position 2–3)" }
  - { name: "PRE-VOL", type: knob, value: "9:00" }
  - { name: "MASTER", type: knob, value: "3:00" }
  - { name: "TREBLE", type: knob, value: "+1 (~12–1:00)" }
  - { name: "TREBLE SHIFT", type: knob, value: "~7–8:00 (≈2.5–5 kHz, touch of string)" }
  - { name: "MIDDLE", type: knob, value: "+3 (~1–2:00, clarity boost)" }
  - { name: "MID SHIFT", type: knob, value: "~12–1:00 (≈800 Hz–1.2 kHz)" }
  - { name: "BASS", type: knob, value: "−2 (~10:00, used as low-mid CUT)" }
  - { name: "BASS SHIFT", type: knob, value: "~2–3:00 (≈350–500 Hz, swept UP)" }
  - { name: "HI-PASS", type: knob, value: "~8:00" }
  - { name: "HI-PASS ON/OFF", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "INST/XLR", type: switch, value: "XLR (out → interface)", options: ["INST", "XLR"] }
  - { name: "20 dB PAD", type: switch, value: "off", options: ["on", "off"] }
---

# Bass Clarity EQ Curve

## Concept
A variation on the Clean Bass DI that adds presence and articulation without thinning the low end — "clarity without taking any booty out." It demonstrates the Colour Box's semi-parametric trick: by sweeping the BASS band's SHIFT *up* to ~350–500 Hz and cutting it, the BASS knob acts as a low-mid CUT, which frees the MID band's clarity boost from mud.

## How to play it
1. Start from the Clean Bass DI (LO · STEP 2–3 · PRE-VOL 9:00 · MASTER 3:00), XLR out → interface.
2. Boost MIDDLE +3 with MID SHIFT ~12–1:00 (≈800 Hz–1.2 kHz) — the clarity boost.
3. Sweep BASS SHIFT UP to ~2–3:00 (≈350–500 Hz) and cut BASS −2 (~10:00) so the BASS knob frees the MID band of mud.
4. Add a small TREBLE +1 with TREBLE SHIFT ~7–8:00 (≈2.5–5 kHz) for a touch of string.
5. Engage HI-PASS ~8:00.

## Notes
- Every band bypasses at its noon detent, so you can apply the MID clarity boost in isolation.
- Community-cited: frequencies are named in the source; the clock translation is mine.
- The headline technique is the BASS-as-low-mid-cut move via SHIFT sweep.

## Sources
- The Bass Negus "clarity EQ curve — boost ~1 kHz (MID), cut ~200–300 Hz, small touch of ~2.5 kHz; uses BASS SHIFT swept up so the BASS knob acts as a low-mid CUT, freeing the MID band" (`research/transcripts/bass-negus-bass-tutorial.md`).
- Transformed from Pedalxly Colour-Box-V2-Patches.md (community).
