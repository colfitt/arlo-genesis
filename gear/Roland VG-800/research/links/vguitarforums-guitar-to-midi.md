https://www.vguitarforums.com/smf/index.php?topic=39126.0
vguitarforums.com · "VG-800 - GUITAR to MIDI" thread (+ official BOSS V-Guitar/synth article) · 2025

How to drive external synths/samplers (Octatrack, Digitakt, MPC, soft-synths) from the GK-5 via the VG-800's GUITAR-TO-MIDI block.

## Mono vs Poly mode — the key decision
- **MONO mode (recommended for expressive playing):** each string sends on its OWN MIDI channel, so each string can bend independently. The receiving synth must be set to **MIDI Mono Mode (MIDI Mode 4)** — *"each string, in effect, drives its own independent mono synth controlled by a separate MIDI channel."*
- **VG-800 MIDI output channels are CONSECUTIVE; the Basic Channel can be set 1–10.** So if Basic = 1, the six strings occupy ch.1–6 (MONO). Pick a Basic Channel that leaves room for 6 consecutive channels.
- **POLY / single-channel mode:** all notes on one channel. Works on any synth (set it to OMNI if it has no Mono mode), but you **lose independent per-string pitch bend** — chords bend as a block.

## ALT TUNING + MIDI out (important gotcha)
- By default the **MIDI output does NOT follow the VG-800's ALT TUNING** — you hear the audio pitch-shifted (e.g. Drop D) but the MIDI still spells the *physical* notes (E).
- Fix: **Tone Studio → CONTROL ASSIGN → GUITAR TO MIDI → set ALT TUNE = ON.** Then *"the MIDI output reports the tuned notes (e.g., Drop D plays D instead of E)"* (HitechGuitar). Turn this ON if you want the sampler/synth to receive the retuned pitches.
- The global **Tuning Style** setting (declaring the guitar's physical tuning) does **NOT** affect MIDI output or the modeling algorithm — don't rely on it for MIDI.

## Triggering / dynamics params (to tame banjo/baritone)
- The GUITAR-TO-MIDI block exposes **HOLD types, PLAY FEEL, velocity (NO-DYNA fixed velocity), and low-velocity cut** — use HOLD to sustain fast-decaying banjo notes so external synths don't retrigger/gate; use low-velocity cut to kill ghost triggers on the drone string.

## Hardware path alternative
- **GK OUT** can chain to a GM-800 (Serial GK passthrough) instead of using MIDI — relevant only if a GM-800 is in the rig.

## Rig takeaway
To drive the Digitakt/Octatrack/MPC expressively from the banjo or baritone: MONO mode, Basic Channel 1, receiving device in Mono/Mode-4 (or OMNI if not supported); turn ALT TUNE = ON in CONTROL ASSIGN so retuned pitches transmit; lean on HOLD + low-velocity cut to stop the banjo's fast decay from machine-gunning the sampler.
