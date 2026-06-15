---
type: patch
title: Mature Thermae Oct+4+5 Ladder Lead
device: Chase Bliss Big Time
date: 2026-06-15
description: "Big Time as the 'more mature Thermae' — feed evened single banjo plucks and the repeats arpeggiate into Oct+4+5 ladders that ping-pong L↔R while SCALE IGNORE adds a clean sine wobble; STEP MODE is the primary performance move (walk pitch up by hand on the LEFT footswitch). Designed from the Mark Johnston deep-dive + harp-lady transcript."
tags: [pitched, sequenced, melodic, banjo, thermae, ping-pong, step-mode, designed, signature]
hidden:
  SCALE IGNORE: "ON (smooth sine modulation + scaled transposition, none of the chaos — this is the clean wobble)"
  STEP MODE: "ON (Options → STEP MODE ON → tap LEFT footswitch to walk pitch up through the SCALE by hand — the PRIMARY performance move here, not a variant)"
  MISO: "auto-engages off IN-L (mono-in / stereo-out) so the ladders open to the full stereo field"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27 (flying faders fly to it on recall)" }
  - { name: "MODE", type: switch, value: "Short (or Mod for tighter ramps)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Digital or Compressed (keep pitch artifacts low)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi or Focus", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Oct+4+5 (octave + perfect 4th + 5th ladders — the core of this patch)", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Square (Thermae pitch jumps), used WITH STEP MODE", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~40%" }
  - { name: "TIME", type: knob, value: "mid (lower = snappier steps, higher = legato)" }
  - { name: "CLUSTER", type: knob, value: "low-mid (let the core ladder read)" }
  - { name: "TILT EQ", type: knob, value: "noon → up (keep bright banjo transients defined so SCALE fires)" }
  - { name: "FEEDBACK", type: knob, value: "~50–60% (ladder length)" }
  - { name: "WET", type: knob, value: "~45%" }
  - { name: "RATE", type: knob, value: "moderate (alt under TIME)" }
  - { name: "DEPTH", type: knob, value: "moderate (alt under CLUSTER)" }
  - { name: "SPREAD", type: switch, value: "ping-pong (ladders bounce L↔R across the field)", options: ["off", "widen", "ping-pong"] }
  - { name: "LEFT footswitch", type: button, value: "PRIMARY performance — with STEP MODE on, tap to walk pitch up through the SCALE by hand, one composed step at a time" }
---

# Mature Thermae Oct+4+5 Ladder Lead

## Concept
Big Time as the 'more mature Thermae': feed clean, evened single banjo plucks and the repeats arpeggiate into Oct+4+5 ladders that ping-pong L↔R, while **SCALE IGNORE** adds a smooth sine wobble under the scaled transposition (no chaos). Distinct from the existing **Banjo Thermae Cascade Lead** / **Bouncy Thermae** patches (which lean SCALE Octave and treat STEP as a secondary variant): here **SCALE Oct+4+5 + SPREAD ping-pong + STEP-MODE-as-primary-performance** are the core. You play seeds, not phrases — the ladders are the melody, walked up by hand on the LEFT footswitch.

## How to play it
1. Recall the GK profile + clean banjo voice upstream and feed single, well-articulated plucks — sparse, let each ring.
2. Set **SCALE = Oct+4+5** and **MOTION = Square**; the repeats arpeggiate each seed into octave/4th/5th ladders.
3. Turn **SCALE IGNORE ON** (Options) for the smooth sine wobble under the scaled steps — keeps it musical, not feral.
4. Set **SPREAD = ping-pong** so the ladders bounce L↔R across the stereo field (MISO opens it to stereo off IN-L).
5. Enable **STEP MODE** (Options) and tap the **LEFT footswitch** to walk the pitch up through the SCALE by hand — this is how you "play the melody" through the repeats, one composed step at a time.
6. Lower **TIME** for snappier steps, raise for legato; **FEEDBACK ~50–60%** sets ladder length; keep **CLUSTER** low-mid so the core ladder reads.
7. Hands-free variant: drop STEP MODE and let MOTION Square free-run the ladders (slave via CC54 to land on a grid).

## Notes
- The whole patch depends on an EVENED source — pair it after Clean 'Banjo Transient Tamer' so every seed note arrives at the same level/envelope; ragged transients make the SCALE steps misfire and drop notes.
- TILT EQ noon → up keeps the bright banjo transients defined — defined transients are what the SCALE engine listens for.
- SCALE IGNORE ON is the key to a MUSICAL sine wobble + scaled ladders without the pedal going feral.
- STEP MODE here is the primary performance interface, not an afterthought — it turns the pedal into a hand-played pitch sequencer.
- **Honesty flag:** numeric knob values are a DIALABLE RECIPE, NOT published settings — the Big Time's motorized flying faders override them on recall. The control surface (switch positions, hidden SCALE IGNORE / STEP MODE) is verified against the existing Big Time patch sheets and GearProfile; the specific VALUES are designed starting points.
- Distinct from 'Banjo Thermae Cascade Lead' (SCALE Octave) and 'Bouncy Thermae' (Factory #4) by the Oct+4+5 ladders + ping-pong + STEP-as-lead emphasis.

## Sources
- 🟣 designed from `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (SCALE / MOTION / STEP / SCALE IGNORE behavior).
- `centerpiece-harp-lady-emily-hopkins-big-time-as-instrument.md` ("more mature Thermae" framing).
- DeepResearch §6 (banjo bright transients = ideal MOTION/SCALE/SCALE-stepping fuel).
- Built for the chain `clean-banjo-big-time-mature-thermae-lead` (Clean evens the attack → Big Time SCALE Oct+4+5 ladders).
