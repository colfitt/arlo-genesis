---
type: chain
title: Keys Rig
date: 2026-06-11
artists: [Peter Gabriel, Prince, The Police]
instrument: keys
gear:
  - Novation 61SL MkIII
  - Caroline Somersault
  - Boss CE-2W
---

# Keys Rig

61-key controller through two compact modulation pedals. Gabriel's synth pads get lo-fi wobble from the Somersault; Prince's keys get classic chorus from the CE-2W. Two pedals, minimal footprint, big texture.

## Signal Path

### 1. Novation 61SL MkIII
Semi-weighted 61-key controller. Drives soft synths (Arturia V Collection, Native Instruments Komplete) via USB, or hardware synths via 5-pin MIDI DIN. Audio comes from the synth source (plugin output from interface, or hardware synth audio out) — the Novation itself produces no audio.

### 2. Caroline Somersault
Lo-fi modulation with character. [Vibrato mode](guide:Caroline%20Somersault/vibrato-mode) adds pitch wobble to pads — instant VHS-era Gabriel/Tears for Fears texture. The chorus side is warm and imperfect, not pristine — it degrades the signal slightly, which keeps keys from sounding too "produced." Havoc footswitch for momentary pitch-dive chaos on transitions.

### 3. Boss CE-2W
[CE-2 mode](guide:Boss%20CE-2W/ce-2-mode) for classic 80s synth chorus — the same circuit that defined the era these artists come from. On electric piano patches (Rhodes, Wurli from V Collection), this is the sound. On pads, it widens the stereo image without overwhelming. CE-1 mode for deeper, more dramatic chorus on ambient parts.

## Routing

Audio path: synth/plugin output → Somersault → CE-2W → back to interface (or PA).

If running soft synths, route a stereo output from your interface (e.g., [RME Babyface Pro FS outputs 3-4](guide:RME%20Babyface%20Pro%20FS/output-routing)) through the two pedals and return on separate inputs. This keeps the pedal color on keys only, not your whole mix.

For hardware synths (OP-1 Field, etc.), run their audio out through the same two pedals before hitting the interface.

## The Vibe

- **Gabriel pads**: Somersault vibrato slow + CE-2W chorus — warped, wide, atmospheric
- **Prince keys**: Somersault off, CE-2W CE-2 mode — clean chorus on stabs and comps
- **Police keys**: Both on, subtle settings — shimmery movement under guitar

## Sources

- `gear/Novation 61SL MkIII/GearProfile.md`
- `gear/Caroline Somersault/GearProfile.md`
- `gear/Boss CE-2W/GearProfile.md`
- `gear/RME Babyface Pro FS/GearProfile.md`
