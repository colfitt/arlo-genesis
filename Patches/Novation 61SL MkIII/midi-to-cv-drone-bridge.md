---
type: patch
title: MIDI-to-CV Drone Bridge (modular mono voice)
device: Novation 61SL MkIII
date: 2026-06-14
description: Drive analog/modular gear — a calibrated mono CV pitch voice + Gate + a Mod-CC for filter/VCA + analog Clock Out; the rig's only MIDI-to-CV bridge. Plan mono lines/drones, not chords.
tags: [cv-gate, modular, drone, mono-voice, clock-out, community, signature]
controls:
  - { name: "Calibrate (Global → CV)", type: knob, value: "Per port: CV-Low vs 220 Hz (A2), CV-High vs 880 Hz (A4) with Tune knob → Apply" }
  - { name: "CV1", type: knob, value: "→ VCO 1V/oct in (notes 24–108 → 0–7 V)" }
  - { name: "Gate1", type: knob, value: "→ envelope/gate in (high while held)" }
  - { name: "Mod1", type: knob, value: "→ filter cutoff / VCA CV" }
  - { name: "Mod1 CC + Range (Global)", type: knob, value: "Set Mod1 CC = the CC you'll send; Range = −5/+5 V (bipolar) or 0/+5 V (unipolar)" }
  - { name: "CV/Gate count (Part)", type: knob, value: "Shift+Sessions → CV/Gate = 1 (MONO last-note, 2 voices max)" }
  - { name: "Pitch-bend → CV", type: knob, value: "Global ±2 semis (fw 1.4; up to ±12)" }
  - { name: "Clock Out PPQN", type: switch, value: "/1 or /2 ONLY (phase-locked); divide down in the rack", options: ["/1", "/2"] }
  - { name: "Mapped expression", type: knob, value: "Map a fader/encoder/aftertouch to the Mod1 CC in the template" }
  - { name: "Gate length (texture trick)", type: knob, value: "Long gates swell through reverb/delay; short gates ping — gate length IS modulation" }
  - { name: "Session Slot", type: knob, value: "Session slot 9" }
hidden:
  Both Mod outs from one Part: "set the Part's CV mode to 'both'"
  From DAW: "host 'To CV/Gate' port plays it (MIDI ch.1→CV1, ch.2→CV2)"
---

# MIDI-to-CV Drone Bridge (modular mono voice)

## Concept
Driving any analog/modular gear: a calibrated mono CV pitch voice + Gate + a Mod-CC for filter/VCA + analog Clock Out — the rig's ONLY MIDI-to-CV bridge. Plan mono lines/drones, not chords. CV is MONO last-note, 2 voices max (CV1+CV2), and Clock-Out only phase-locks at /1 and /2.

## How to play it
1. CALIBRATE FIRST (Global → CV): per port set CV-Low against 220 Hz (A2) and CV-High against 880 Hz (A4) with the Tune knob into a VCO/tuner → Apply.
2. PATCH: CV1 → VCO 1V/oct in; Gate1 → envelope/gate in; Mod1 → filter cutoff / VCA CV; Clock Out → modular clock-in.
3. PART: Shift+Sessions → CV/Gate = 1; keybed or sequencer plays the MONO last-note voice (notes 24–108 → 0–7 V; Gate high while held).
4. MOD1: Global set Mod1 CC = the CC you'll send, Mod1 Range = −5/+5 V (bipolar) or 0/+5 V (unipolar); map a fader/encoder/aftertouch to that CC in the template → real-time voltage; sequencer automation on that CC also drives Mod1.
5. PITCH-BEND → CV: Global ±2 semis (firmware 1.4; up to ±12) for playable bends.
6. CLOCK OUT PPQN: match the rack — use /1 or /2 ONLY (only those stay phase-locked; /4–/24 drift) and divide down in the rack.
7. TEXTURE TRICK (DivKid): long gates make notes swell/breathe through reverb/delay, short gates "ping" — gate length IS modulation.
8. From the DAW: host "To CV/Gate" port plays it too (MIDI ch.1→CV1, ch.2→CV2).

## Notes
- Documented CV workflow.
- CV is MONO last-note, 2 voices max (CV1+CV2).
- Clock-Out phase-lock only at /1 and /2.
- To use BOTH Mod outs from one Part, set the Part's CV mode to "both."

## Sources
- research/links/int-recipe-modular-softsynth.md §A + research/links/cv-gate-mod-calibration.md + research/links/novation-faq-cv-gate-calibration.md + transcripts/divkid-eurorack-cv.md + DeepResearch §6/§13(c).
- Ref: Taste — drone/doom sustained voltage walls; DivKid CV reference.
- Transformed from Pedalxly 61SL-MkIII-Patches.md (community)
