https://www.youtube.com/watch?v=V0QMTiJicVA
Ron Cavagnaro · Using Octatrack As A Mixer: Thru Machine Basics // Elektron Octatrack Tutorial · 2018-03-03

A tight beginners' walkthrough of using the OT as a live mixer/FX processor for external gear via **Thru machines**. (Filmed on an MkI; the Thru machine and engine are identical on the MkII.) ~5 min.

## Project + MIDI sync setup
- New project: hold `[FUNC]`, press `PROJECT` (red labels = function-tier commands). PROJECT → CHANGE → "playback will be stopped, continue?" `YES` → CREATE EMPTY PROJECT → `YES` (default name fine).
- PROJECT → MIDI → SYNC: enable **transport send, transport receive, clock send, clock receive** (his OT is slaved to a Deluge and forwards MIDI to a Novation Circuit + EMX). Exit twice.

## Thru machine per input
- Two external synths feeding the inputs: EMX into **input A**, Circuit into **input B** (the A/B input LEDs light when each plays).
- Track 1: double-tap → machine list → scroll down to **THRU** → `[ENTER]`. The track now shows the Thru screen (the four encoders show exactly the on-screen params). Set the input to **A**.
- **Place ONE trig** on the track — the Thru passes audio only across the triggered step, so a single trig opens the channel for the whole step (i.e. continuous pass-through).
- Track 2: same → THRU → set input to **B**. Now both external synths pass through the OT.

## Muting + real-time FX
- Mute a track: hold `[FUNC]` + the track key — muted = yellow, active = red.
- FX1 default = **filter**: tweak **CUE (cutoff)** and **WIDTH** to filter that input's audio in real time.
- FX2 default = **delay**: turn up **SEND** per track to feed the delay.
- Change an effect: double-tap the FX slot, scroll up/down to any effect; the setup screen stays on the chosen effect. `EXIT` to leave.

## Rig relevance
This is the literal "Octatrack as the rig's live mixer/FX unit" patch — the simplest version of the rig-defining setup: pedalboard stereo print → input A/B → a Thru machine per pair with one trig each → filter + delay applied live, channels mutable from the front panel. From here you graduate to the EZBOT/Cavagnaro/Cuckoo resampling and scene moves on top of the Thru'd signal.
