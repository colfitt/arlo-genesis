---
type: patch
title: Thermae Octave-Dive Ramp
device: Chase Bliss Big Time
date: 2026-06-15
description: "Big Time as a playable pitch instrument — SCALE = Octave makes the TIME fader a scale-quantized octave transposer, and SCALE IGNORE frees the MOTION matrix from the TIME clock so a slow sine LFO keeps wobbling underneath while you sweep octave-up/dive ramps live from the 61SL's CC15 fader. Designed from the Mark Johnston deep-dive + verified Big Time CC map; the opposite intent from Bouncy/Banjo Thermae (MOTION Square pitch-jumps) — this is MOTION Sine + TIME-as-pitch-fader for a composed glide."
tags: [pitched, thermae, octave, ramp, sine, cc-controlled, synth, designed, signature, big-time]
hidden:
  SCALE IGNORE: "ON (Options / 'E' page) — the load-bearing option: frees the MOTION/sine from the TIME clock so TIME becomes a pure pitch fader instead of also dragging the modulation rate"
  TIME center-throw hack: "Tap the LEFT footswitch to snap TIME to the center of the fader's throw — a recallable pivot to bend an octave up/down around and return to cleanly (documented as 'useful with SCALE = octaves')"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27, or dial it on PC0 LIVE (flying faders fly to it on recall)" }
  - { name: "MODE", type: switch, value: "Short (or Long for a slower wash)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Digital or Compressed (keep pitch artifacts clean — no Saturated/misbias)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Octave (octave jumps only — the core of this patch)", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine (smooth wobble under everything)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "low-mid" }
  - { name: "TIME", type: knob, value: "the whole performance — swept live via 61SL CC15 (octave-up = push, dive = pull)" }
  - { name: "CLUSTER", type: knob, value: "low-mid" }
  - { name: "TILT EQ", type: knob, value: "~noon" }
  - { name: "FEEDBACK", type: knob, value: "~45–55% (tails ring long enough to hear each transposed step)" }
  - { name: "WET", type: knob, value: "below dry to start (an octave-down delay is heavy low-end)" }
  - { name: "RATE", type: knob, value: "slow (the sine, alt under TIME)" }
  - { name: "DEPTH", type: knob, value: "moderate (alt under CLUSTER)" }
  - { name: "SPREAD", type: switch, value: "widen (slight stereo on transposed tails)", options: ["off", "widen", "ping-pong"] }
  - { name: "LEFT footswitch", type: button, value: "Tap once to snap TIME to center-throw — a recallable octave pivot to bend up/down around (see hidden: TIME center-throw hack)" }
  - { name: "61SL enc1", type: knob, value: "CC15 = TIME — the live pitch fader; Fader Pickup ON on the SL" }
---

# Thermae Octave-Dive Ramp

## Concept
Big Time as a playable pitch instrument: **SCALE = Octave** means dragging the **TIME** control transposes the entire delay in clean scale-quantized octave steps, while **SCALE IGNORE** frees the MOTION matrix from the TIME clock so a slow **sine** LFO keeps wobbling underneath. Hands-on octave-up/dive ramps driven from the 61SL's **CC15 (TIME)** fader — musical pitch ramps, not square-wave arpeggiation or chaos. The opposite intent from the existing **Bouncy Thermae** / **Banjo Thermae Cascade** patches, which use **MOTION Square** for per-note pitch-jump cascades; this one is **MOTION Sine + TIME-as-pitch-fader** for a composed glide.

## How to play it
1. Recall the patch (or dial it on PC0 LIVE); confirm **SCALE = Octave**, **MOTION = Sine**, and **SCALE IGNORE = ON** in Options.
2. Feed one held/sustained synth note from the 61SL into Big Time's input.
3. Ride **61SL enc1 (CC15 = TIME)**: push up for an octave-rising ramp, pull down for the dive — Octave SCALE quantizes the steps so you can't land off-key.
4. Tap the **LEFT footswitch** once to snap TIME to the center of the fader throw, giving a recallable pivot to bend an octave up/down around and return to cleanly (the documented "useful with SCALE = octaves" hack).
5. Keep the sine slow and low (**RATE** down) so it breathes under the transposition rather than fighting it.
6. Panic reset: press-and-hold **MODE** to recall a plain clean delay if a ramp runs away.

## Notes
- **SCALE IGNORE is the key to musical ramps:** without it, dragging TIME also drags the modulation rate (TIME is the modulation clock), so the sine speeds up/slows down as you transpose. With it ON, the sine stays put and TIME is a pure pitch fader.
- SCALE-on-Octave tracks musical subdivisions when clocked, vs OFF/CHROMATIC which snap to the quarter — Octave is what we want here.
- Keep STATE Digital/Compressed and COLOR modest: drive (Saturated/misbias) smears the octave steps into noise and defeats the "musical ramp" goal.
- **Honesty flag:** all knob/fader numerics are a DIALABLE RECIPE, not published settings — designed starting points. On preset recall Big Time's motorized flying faders override them. The control surface (switch positions, hidden SCALE IGNORE / center-throw hack) is verified against the deep-dive transcript + verified CC map; the specific VALUES are designed.

## Sources
- 🟣 designed from `gear/Chase Bliss Big Time/research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` — MOTION/SCALE § ("SCALE quantizes the pitch movement of both TIME and MOTION"; off = glides, Octave = octave jumps only), OPTIONS / "E" page § ("SCALE IGNORE: lets the MOTION/modulation matrix ignore the TIME control… smooth sine modulation… without the full chaos"), and the tap-tempo hack ("snaps TIME to the center of the fader's throw… Useful with SCALE = octaves").
- CC15 = TIME / Fader Pickup / SCALE-on-Octave subdivision tracking: verified Big Time CC map in `Patches/Novation 61SL MkIII/big-time-centerpiece-performance-template.md`.
- Taste-ref ("more mature Thermae"): `gear/Chase Bliss Big Time/research/transcripts/centerpiece-harp-lady-emily-hopkins-big-time-as-instrument.md`.
- Provenance: 🟣 designed — behavior verified from Big Time deep-dive transcript + verified CC map; knob/fader numerics are a dialable recipe (not published values).
