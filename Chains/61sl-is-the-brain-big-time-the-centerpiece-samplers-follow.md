---
type: chain
title: 61SL is the Brain — Big Time the Centerpiece, Samplers Follow
date: 2026-06-14
artists: [LCD Soundsystem]
instrument: synth / drums/sampler
gear:
  - Novation 61SL MkIII
  - Elektron Digitakt 2
  - Elektron Octatrack MkII
  - Akai MPC Sample
  - Roland VG-800
  - Chase Bliss Clean
  - Chase Bliss Big Time
  - Eventide H90
---

# 61SL is the Brain — Big Time the Centerpiece, Samplers Follow ⭐

Run the whole live rig DAW-less with the 61SL as clock master and 8-track sequencer, Big Time as the unifying centerpiece delay, and one foot/encoder gesture re-voicing the delay through the arrangement. One coherent, tempo-locked rig where every sampler line passes through one delay character; the centerpiece changes voice with the song without you touching the pedal.

🟣 DOUG-designed integration. No artist used this exact chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases.

## Signal path

**61SL MkIII** (silent brain, clock + sequencer + CC) → drives Digitakt 2 + Octatrack + MPC over DIN/USB; their audio + the VG-800 string source all sum into Board 1 → Clean (#1) → drives → **Big Time** (as the song's delay, on Board 3) → CB stack → H90 → tape.

## Per-unit

- **61SL #5 Big Time Centerpiece Performance Template** — SL DIN Out → Big Time MIDI IN directly (no MIDIBox). enc1=CC15 TIME, enc2=CC19 WET, enc3=CC14 COLOR; buttons = scene PCs + a LIVE (PC0); Fader Pickup ON. **SL = clock master (Tx On)**, Big Time follows (CC111=0).
- **61SL #11 Elektrons + MPC as Clock Master** — the room template: Part1→Digitakt2 (DIN1, Ch1), Part2→Octatrack (Ch2), Part3→MPC (Ch3); load the factory OT + DT Components templates; one Play/Stop starts the whole rig.
- **Big Time** — runs whichever song patch the scene recalls (e.g. **#2 Lo-Fi Rhythmic Groove** for verses, **#3 Loop Diffuser** for the outro). Save song-section presets via CC27.
- **VG-800 (electronic.md #VG-E1 banjo lead / #VG-E2 acid bass)** — the string source the SL can also sequence/ride via its CONTROL ASSIGN CCs.

## Routing

**SL = the single clock master** (24 PPQN to USB + both DINs); never Tx AND Rx clock at once, never double-path clock (USB+DIN). Big Time CC111=0 (follow). ⚠️ **MPC must NOT be slaved on fw 1.2.1** (kick/bass distortion) — either keep the MPC off the clock for those parts or hand the MPC the master role for MPC-led songs (see the MPC-master groove chain). Map song sections (verse/chorus/build) to Big Time presets 1–4; lay the matching **Program Changes on a DT2 MIDI track** (or 61SL buttons) so the delay re-voices itself hands-free.

## Sound

One coherent, tempo-locked rig where every sampler line passes through one delay character; the centerpiece changes voice with the song without you touching the pedal.

**Taste-ref:** electronic / groove-first (LCD additive builds) routed through the doom/drone delay voice — the rig's live-performance backbone.

## Play

Start the whole room with one **Play**; ride **enc1 TIME / enc2 WET** live; tap a 61SL **button to fire the next song-section PC** (Big Time + the CB stack jump scenes at once via the shared-channel scene trick, 61SL #4). FREEZE on the outro.

## Sources

- **Basis:** designed integration; chains **61SL #5 + #11 (+ #4 scene recall)**, **Big Time #2 / #3**, **VG-E1/VG-E2**. Clock-master discipline + native-DIN wiring + section-PC-on-the-timeline from 61SL #5/#11 and the centerpiece source file §C [V] (Big Time = "perfect centerpiece for a synth setup," balanced I/O; map sections to presets 1–4 on the Digitakt timeline).
- `Gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md`
- `Research/Chains/centerpiece-live.md` (C3)
- `Research/Taste-Profile/electronic.md`
- `Research/Taste-Profile/taste-profile.md`
