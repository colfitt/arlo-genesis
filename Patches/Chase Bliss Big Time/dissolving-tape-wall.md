---
type: patch
title: Dissolving Tape Wall
device: Chase Bliss Big Time
date: 2026-06-15
description: "The headline Snyder degradation move on one pedal — hold a sustaining fuzz wall into Big Time and let the #!&% misbias limiter re-degrade each repeat until the loop eats itself into crumbling failing-tape echoes. Designed from the John Snyder EAE interview + Mark Johnston deep-dive; switch states and degradation mechanics are sourced, numeric fader values are a dialable recipe."
tags: [delay, misbias, degraded, tape, disintegration-loops, drone, doom, lo-fi, designed, signature]
controls:
  - { name: "Chain / Input", type: switch, value: "Sustaining fuzz (Hizumitas) mono → IN-L (auto MISO mono-in/stereo-out)", options: ["mono → IN-L (MISO)", "stereo in"] }
  - { name: "MODE", type: switch, value: "Long (~12 s; ~24 s with 0.5X — time must outlast the bias-sag envelope so the loop self-destructs)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "#!&% (misbias) — sidechain-shifted limiter sag-and-return [drop to Saturated for a tamer crumble]", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Warm (brick-wall ~10k roll-off; the misbias pairing Snyder says 'rips itself in half')", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "0.5X", type: switch, value: "ON (half sample rate + bit reduction = failing-tape crush; also doubles delay time)", options: ["off", "on"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine subtle", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~30–40% (RECIPE — modest; a hot fuzz already supplies the dirt. Lower to explore the dynamic destruction threshold, too high clamps to porridge)" }
  - { name: "TIME", type: knob, value: "long" }
  - { name: "CLUSTER", type: knob, value: "~40%" }
  - { name: "TILT EQ", type: knob, value: "noon → up (cut muff/rumble mud)" }
  - { name: "FEEDBACK", type: knob, value: "~70% (repeats stack and re-degrade pass after pass)" }
  - { name: "TEXTURE", type: knob, value: "~55% = misbias amount / sag depth (alt under COLOR, RECIPE)" }
  - { name: "DIFFUSE", type: knob, value: "mid (alt under FEEDBACK)" }
  - { name: "WET", type: knob, value: "~45%" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
  - { name: "Panic-reset", type: button, value: "hold MODE → drop back to a clean delay if the misbias runs away" }
---

# Dissolving Tape Wall

## Concept
The headline Snyder degradation move on one pedal: hold a sustaining fuzz wall into Big Time and let the misbias limiter re-degrade each repeat until the loop eats itself — Disintegration-Loops / failing-tape crumbling stereo echoes. Long MODE so the delay time outlasts the bias-sag attack/recovery envelope (that's what lets the buffer "continue to eat itself alive"); #!&% misbias STATE for the sidechain-shifted limiter sag-and-return; Warm voicing (the pairing Snyder says "rips itself in half" with misbias); 0.5X for the half-sample-rate + bit-reduced failing-tape crush. COLOR stays modest because a hot fuzz already supplies all the saturation — Big Time's job here is erosion, not more dirt. Distinct from the existing "Hizumitas Fuzz Wall" (Compressed, anti-runaway, holds-together) and "Oceanic Drone Bed" (non-degrading FREEZE pad) — this one is built to crumble, not to hold.

## How to play it
1. Run a sustaining fuzz (Hizumitas) mono → **IN-L**, which auto-engages **MISO** (mono-in/stereo-out).
2. Set **MODE Long + 0.5X ON** so the time outlasts the bias-sag envelope and the loop can eat itself; **STATE #!&% (misbias)**, **VOICING Warm**.
3. Hold one chord, let the wall build, then ride the misbias threshold with your attack: play gently for grit-without-loss, dig in for fast dropout and crackle — the performance IS the destruction.
4. Walk **COLOR** up slowly until the repeats *just* begin to crumble, no further (past that the limiter clamps to porridge).
5. With the Long time, punch in a clean held section and come back later to find Big Time has degraded it; feed the wet into a Blackhole hall downstream.
6. **Panic-reset (hold MODE)** to drop back to a clean delay if the misbias runs away.

## Notes
- **#!&% (misbias)** uses the compressor sidechain to shift the limiter's bias — when you dig in the limiter excursions out of the reproducible region then crawls back, giving the crackling "sag-and-return" that reads as disintegration-loop / failing-tape texture.
- Snyder: misbias + Warm + TEXTURE makes "the mix sound like it's ripping itself in half"; lower COLOR to explore the dynamic threshold; at ~12 s the low rumble is "the contents of the delay continuing to eat themselves alive."
- **0.5X** halves the sample rate and adds bit reduction — Snyder says 32→12-bit, Mark Johnston says 16-bit; treat the *exact* reduced bit depth as **UNVERIFIED**.
- **COLOR** is input gain feeding both the feedback loop AND the output limiter — keep it modest with a hot fuzz so Big Time erodes rather than over-saturates.
- Numeric fader positions are a designed **RECIPE**; on recall the motorized flying faders override anything written. The switch states (Long / #!&% / Warm / 0.5X) and their behavior ARE sourced.
- Distinct role from "Hizumitas Fuzz Wall" (Compressed = anti-runaway, holds together) and "Oceanic Drone Bed" (#!&% but FREEZE = non-degrading pad). This patch is built to crumble continuously, not to hold.

## Sources
- 🟣 designed from `research/transcripts/sonicstate-superbooth-john-snyder-eae-interview.md` (STATE/VOICING: misbias sidechain bias-shift, "sag-and-return" = disintegration-loop/failing-tape; misbias+Warm+TEXTURE "rips itself in half"; lower COLOR explores the dynamic threshold; at 12 s "the contents of the delay continuing to eat themselves alive"; 0.5X = half sample rate + 12-bit).
- `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (STATE limiter character, TEXTURE = misbias amount, 0.5X mechanics — notes 16-bit discrepancy; COLOR feeds feedback+limiter).
- `research/links/centerpiece-minimal-chains-and-sampler-integration.md` §A (fuzz→Big Time gain-staging, COLOR modest, MISO auto-engage).
