---
type: chain
title: VocalShift "Singing Wall" Baritone Drone with 61SL-Played Harmony
date: 2026-06-14
artists: [Bon Iver, Sufjan Stevens]
instrument: baritone
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - Eventide H90
  - Chase Bliss MOOD MkII
  - Hologram Chroma Console
  - MXNHLT PORTA424
  - Novation 61SL MkIII
---

# VocalShift "Singing Wall" Baritone Drone with 61SL-Played Harmony

Harmonize a single sustained baritone (or banjo) drone into a wide, scale-locked, multi-voice "singing wall" — and play the harmony intervals *live* from the keyboard while the lead note is held. A drone that becomes a choir, with the player conducting the harmony. ⭐ signature-fit.

This is a 🟣 designed integration of owned-gear patches; no artist ever played *this* chain. The Taste-ref names the sound it chases, and the per-unit patch sheets carry their own provenance.

## Signal path

Baritone JM (GK-5) → **VG-800 (#5 VIO Bowed Swell Drone** or **#7 Doom Baritone Wall** for weight) → Clean (#6 Baritone Drone Sustainer) → [Board 2 thru] → [Board 3] → **H90 (#31 VocalShiftMIDI Live-Harmony Drone, played from the 61SL)** → **MOOD (TB3 / #12 frozen Reverb pad)** → Chroma → PORTA424 → tape. **61SL (#2 VG-800 Audition & Control + #11 clock)** plays the harmony intervals into the H90.

## Per-unit

- VG-800 **#5 VIO Bowed Swell Drone** (attackless sustained source) or **#7 Doom Baritone Wall** (−7 STEP weight); recall GK **#2 BARI JM**. `NORMAL MIX` low so the H90 harmonizer tracks a clean fundamental.
- Clean **#6 Baritone Drone Sustainer** — limiting + slow release for a sustained, even bed for the harmonizer to lock onto; full-range Envelope Balance.
- H90 **#31 VocalShiftMIDI Live-Harmony Drone** — 4 MIDI-played voices over the held baritone; Root learn, Spread Wide, **Hold** so voices sound only while a MIDI note is held; map Glide/Freeze to footswitches for pitch-rise swells and frozen vowel-drones. (Stack into the H90 wet-only "super-algorithm" trick for a thicker singing wall.)
- MOOD **TB3 (frozen Reverb pad)** / **#12 Freeze Pad** — Reverb washed (MODIFY CW), HOLD LEFT to freeze into an infinite pad; slowly turn CLOCK down for the moving/detuning drift under the harmonized voices.
- 61SL **#2 VG-800 Audition & Control** + **#11 clock master** — plays the harmony intervals into the H90 VocalShiftMIDI; SL = clock master so any synced FX follow one tempo.

## Routing

Baritone drone mono front → stereo into Board 3. The **61SL plays MIDI notes into the H90** (VocalShiftMIDI receives MIDI-note intervals) — route the SL's DIN/USB to the H90's MIDI in; the SL is clock master (Tx on; never Tx and Rx clock at once). The H90 harmonizes the live audio drone to the played intervals. Keep the VG-800 `NORMAL MIX` low and the source clean so the harmonizer tracks. ⚠️ This is **not** the VG-800's own ALT-TUNE harmony (that's one fixed interval, VG #30/#31) — here the *played MIDI* sets the chord live, which is the richer move.

## Sound

One held baritone note becomes a wide, scale-locked 3–4-voice stereo chord — a "singing wall" you conduct from the keyboard — over a slowly-detuning frozen MOOD pad. Drone as choir.

Taste-ref: indie-folk-confessional (the vocal-halo / played-harmony cloud, Bon Iver/Sufjan layered harmony) rendered on the baritone/banjo drone instead of a voice. Honest note: the H90 VocalShiftMIDI is a *real* multi-voice formant harmonizer (not an approximation) — but it is harmonizing a *string drone*, not a sung vocal, so the timbre is the rig's, not Bon Iver's.

## Play

Hold one baritone note (bowed in via Clean / VIO slow-gear) → play harmony intervals on the 61SL → the H90 sings them over the drone → freeze the MOOD pad (HOLD LEFT, LATCH) under it → use the H90 Glide/Freeze footswitches for pitch-rise swells or to lock a frozen vowel-drone. For a banjo variant, swap the VG-800 source to the EBM5 banjo lead and let the harmony cloud halo it.

## Sources

- Basis: designed integration; chains VG-800 #5/#7 + #2(GK) → Clean #6 → H90 #31 (61SL-played) → MOOD TB3/#12. H90 #31 VocalShiftMIDI is explicitly "play harmony intervals live from the Novation 61SL over a held banjo/baritone note" (H90 sheet #31); 61SL #2/#11 supply the played notes + clock; the "richer than VG fixed-interval harmony" note contrasts VG-800 #30/#31.
- `Research/Chains/banjo-baritone-leads.md` (C6)
