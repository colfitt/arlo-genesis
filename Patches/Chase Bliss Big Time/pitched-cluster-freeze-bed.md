---
type: patch
title: Pitched Cluster Freeze Bed
device: Chase Bliss Big Time
date: 2026-06-15
description: "The pitched bed engine for a FREEZE-solo chain — build a SCALE-Octave cluster of pitched repeats, let the octave taps stack into a chord-like cloud, then hold RIGHT to FREEZE it into a harmonized, non-degrading infinite chord-pad you solo over. Fills the gap between 'Oceanic Drone Bed' (freeze-and-solo but SCALE off / unpitched) and 'Bouncy Thermae' (SCALE Octave but for arpeggiated lead cascades, not a frozen held bed). Designed from the Big Time DeepResearch + Mark Johnston deep-dive + Emily-Hopkins centerpiece."
tags: [freeze, pitched, cluster, scale, octave, drone, ambient, designed, signature]
hidden:
  SCALE IGNORE: "optional — leave OFF so the scaled transposition fully quantizes the cluster to octaves; turn ON only if you want a smoother sine wobble under the pitched steps"
  MISO: "auto-engages off IN-L (mono-in / stereo-out) so the octave taps spread across the full stereo field once frozen"
  MODE button (hold): "panic-reset to a clean delay if the cluster runs away before you freeze it"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27 (flying faders fly to it on recall)" }
  - { name: "MODE", type: switch, value: "Long (long TIME = phrase-length buffer for the bed)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed (stable pitched repeats, no runaway pre-freeze — go Saturated for grit on the bed)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Focus (keeps the octave pitches legible)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Octave (quantizes TIME + MOTION to octave jumps → repeats stack as a real pitched cluster)", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Square (Thermae octave jumps that lay out the cluster)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~35–45% (modest so repeats build and populate the cluster instead of compressing into porridge before the freeze)" }
  - { name: "TIME", type: knob, value: "mid–long (sets octave-step spacing)" }
  - { name: "CLUSTER", type: knob, value: "high ~70–80% (the multitap lines that ARE the chord — the arrangement fader)" }
  - { name: "TILT EQ", type: knob, value: "noon to slightly below (body)" }
  - { name: "FEEDBACK", type: knob, value: "~60–70% (populates the cluster before freeze)" }
  - { name: "WET", type: knob, value: "set carefully — LOUD" }
  - { name: "DIFFUSE", type: knob, value: "mid-high ~60% (smears the taps into a pad — alt under FEEDBACK)" }
  - { name: "DIFFUSE TYPE", type: switch, value: "on (ghostly pad smear)", options: ["off", "on"] }
  - { name: "RATE", type: knob, value: "slow (alt under TIME)" }
  - { name: "DEPTH", type: knob, value: "moderate (alt under CLUSTER)" }
  - { name: "SPREAD", type: switch, value: "widen (octave taps spread stereo)", options: ["off", "widen", "ping-pong"] }
  - { name: "RIGHT footswitch (hold)", type: button, value: "FREEZE — nothing new enters the buffer, the current pitched cluster revolves infinitely = harmonized, non-degrading infinite chord-pad; solo the live harmony over it" }
---

# Pitched Cluster Freeze Bed

## Concept
Build a harmonized infinite bed by FREEZING a SCALE-pitched cluster (not just a held chord). SCALE Octave quantizes the delay's TIME/MOTION to octave jumps, MOTION Square lays out Thermae-style octave steps, and high CLUSTER stacks those pitched repeats into a chord-like cloud; DIFFUSE smears the taps into a pad. Hold RIGHT to FREEZE into a non-degrading, harmonized infinite chord-pad, then solo the live harmony over it. Fills the gap between **'Oceanic Drone Bed'** (freeze-and-solo but SCALE off / unpitched) and **'Bouncy Thermae'** (SCALE Octave but for arpeggiated lead cascades, not a frozen held bed).

## How to play it
1. Set **MODE Long, SCALE Octave, MOTION Square, CLUSTER high (~70–80%), COLOR modest (~35–45%), FEEDBACK ~60–70%, DIFFUSE mid-high with DIFFUSE TYPE on**.
2. Play a note or chord and let the octave repeats populate the cluster — a few seconds, watch it stack into a pitched cloud (the pitches must stay distinct enough that the freeze captures a real chord, not mud).
3. Hold the **RIGHT footswitch to FREEZE** → harmonized, non-degrading infinite chord-pad.
4. Solo the live harmony over the held cluster; feed the wet into a galaxy-wash halo downstream (e.g. QI Etherealizer) for the full centerpiece.
5. If it gets unruly before the freeze, hold the **MODE button** to panic-reset to a clean delay and rebuild.

## Notes
- First-principles from verified control behavior — not artist-attributed. Numeric faders are designed starting points; on recall the motorized flying faders override them.
- SCALE quantizes the pitch movement of TIME and MOTION: **Octave** = octave jumps only, **Oct+4+5** = 4ths/5ths/octaves (also maps to tap subdivisions), **Chromatic**. The key move here is FREEZING the cluster **after** the octave repeats populate, so the freeze captures a real harmonized chord, not mud.
- Keep **COLOR modest** so repeats populate the cluster instead of compressing into porridge before the freeze — the pitches must stay distinct enough to capture a real chord.
- **FREEZE** (hold RIGHT) = nothing new enters the buffer, current sound revolves infinitely → functions like a non-degrading phrase bed at long TIME.
- **IN-L auto-engages MISO** (mono-in / stereo-out); **WET is LOUD** — set carefully before performing.
- **Honesty flag:** knob numerics are a DIALABLE RECIPE, NOT a published preset — only the SCALE / MOTION / CLUSTER / DIFFUSE / FREEZE behaviors are sourced. The control surface (switch positions, hidden SCALE IGNORE / MISO / hold-MODE panic) is verified against the existing Big Time patch sheets and GearProfile; the specific VALUES are designed starting points.

## Sources
- 🟣 designed (DOUG) — purpose-built as the pitched bed engine for the 'Big Time Pitched FREEZE Solo Bed' chain.
- Behavior-sourced: SCALE = Octave / Oct+4+5 / Chromatic pitch-quantize of TIME + MOTION (manual p.30) and MOTION Square = Thermae octave jumps — `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` + `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (MOTION / SCALE) + `centerpiece-harp-lady-emily-hopkins-big-time-as-instrument.md` (octave / 4th / 5th quantize "as an instrument").
- CLUSTER = added / multitap delay lines (the "arrangement fader") + DIFFUSE smears taps into a pad — `mark-johnston-secret-weapons-big-time-deep-dive.md`.
- FREEZE = hold RIGHT, "nothing new into the buffer, current sound revolves infinitely" → non-degrading infinite bed (manual p.16) + the 'Oceanic Drone Bed' patch's freeze-then-solo move; MISO auto-engage and hold-MODE panic-reset from the same Big Time research.
