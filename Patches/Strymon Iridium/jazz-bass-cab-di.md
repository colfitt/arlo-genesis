---
type: patch
title: Jazz Bass Cab DI (AMP DISABLE + bass IR)
device: Strymon Iridium
date: 2026-06-14
description: A clean bass-cab DI for a passive Jazz Bass — AMP DISABLE (fw 1.32+) runs a real bass-cab IR + tight stereo room with the amp model off.
tags: [bass, di, cab, amp-disable, convolution, designed, signature]
hidden:
  AMP DISABLE: on (Live Edit, or MIDI CC21) — amp model off, CAB + ROOM remain
  Impulse Manager — bass-cab IR: load 24-bit/96 kHz WAV ≤500 ms into a cab slot, click SYNC CHANGES (no factory bass cab exists)
controls:
  - { name: "Cab", type: switch, value: "the bass-cab slot", options: ["a", "b", "c"] }
  - { name: "Bass", type: knob, value: "noon" }
  - { name: "Middle", type: knob, value: "inactive (amp disabled — tone-stack off)" }
  - { name: "Treble", type: knob, value: "inactive (amp disabled — tone-stack off)" }
  - { name: "Level", type: knob, value: "to interface unity" }
  - { name: "Room", type: knob, value: "~10:00 (SIZE small — keep tight on bass)" }
  - { name: "Input Level", type: switch, value: "Instrument (passive bass isn't hot)", options: ["Instrument", "Line"] }
  - { name: "Output Mode", type: switch, value: "Normal", options: ["Normal", "Amp Bypass", "Cab Bypass"] }
  - { name: "Rear Input Selector", type: switch, value: "MONO (OUT L)", options: ["MONO", "STEREO", "SUM"] }
  - { name: "Slot/Bank", type: knob, value: "FAV when tracking bass (AMP DISABLE state stores in the snapshot) — or MIDI Bank 0 · PC 7" }
---

# Jazz Bass Cab DI (AMP DISABLE + bass IR)

## Concept
A clean (or grindy) bass DI for the passive Jazz Bass — the baritone-weight low end the VG-800 isn't built to serve for a magnetic passive bass. AMP DISABLE (fw 1.32+) turns off the amp model so only CAB + ROOM run, convolving a real bass-cab IR with a tight stereo room on a non-guitar source.

## How to play it
1. PREP: load a bass-cab 24-bit/96 kHz WAV (≤500 ms) into a cab slot via Impulse Manager, click SYNC CHANGES (no factory bass cab exists).
2. PLAY: engage AMP DISABLE (Live Edit, or MIDI CC21) → amp model off, CAB + ROOM remain.
3. CAB = the bass-cab slot; BASS noon; MIDDLE / TREBLE inactive (tone-stack off when amp disabled).
4. LEVEL to interface unity; ROOM ~10:00, SIZE small (keep tight on bass).
5. INPUT LEVEL = Instrument (passive bass isn't hot), rear = MONO (OUT L), OUTPUT MODE = Normal.
6. ALT grindy-bass variant: skip AMP DISABLE, use AMP punch lightly (DRIVE ~10:00, BASS back to ~9:00 so it doesn't flub) for a Plexi bass-amp grind that feeds doom low-end into the wall.

## Notes
- DESIGNED patch. Requires fw ≥1.32.
- Needs a bass-cab IR loaded; keep ROOM tight so the low end stays defined.
- AMP DISABLE state stores in the FAV snapshot.

## Sources
- designed from AMP DISABLE + custom-IR docs — research/links/ir-impulse-manager-and-output-modes.md; research/links/tips-hidden-behaviors.md; research/links/stack-placement-output-modes.md. No artist dial (IDLES' Bowen uses AMP DISABLE on non-guitar sources but publishes no values).
- Transformed from Pedalxly Iridium-Patches.md (designed)
