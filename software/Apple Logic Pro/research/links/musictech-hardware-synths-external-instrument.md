https://musictech.com/tutorials/hardware-synths-logic-continued/
musictech.com · Mark Cousins · 2018-02-08

# Integrating hardware synths/sequencers in Logic via the External Instrument

The cleanest way to play hardware (VG-800, S08, OP-1, Elektron in synth role)
from Logic AS IF it were a virtual instrument — MIDI in, audio back, plugins on
the return — all on one track.

## External Instrument plugin setup
- On a Software Instrument track, instead of an AU instrument, choose
  **"External Instrument"** plugin.
- In it, set **MIDI Output** = the physical MIDI port going to your hardware,
  and **Input** = the audio input the hardware returns on (e.g. Apollo x8 line
  in 3/4).
- Result: "makes your hardware synth like a virtual instrument. MIDI can be
  recorded and MIDI and audio plug-ins added" to the signal chain — so you can
  stack ChromaVerb/Space Designer/etc. on the live hardware return.

## Capturing to audio (the catch)
The External Instrument is a live monitor path; it does NOT print audio on its
own. To commit: "either perform a **Realtime Bounce**, or create a new **Audio
Track set to the same input** as the synth and record as before." (Realtime —
NOT offline — because the audio is coming from outside the box in real time.)

## Environment (for mapping hardware knobs / custom MIDI control)
- **Window > Open MIDI Environment**, go to the **MIDI Instr** layer.
- Add a **Monitor** object after the instrument object (New > Monitor) to see
  incoming MIDI.
- Build **Vertical faders** (New > Fader > Vertical 6), cable them serially
  from the Monitor output, and create a **MIDI Instrument** object for the
  output assignment — this is how you route/transform CC to the hardware.

## Clock
Use **Project Settings > Synchronization > MIDI** to transmit MIDI Clock to the
chosen output so hardware sequencers/LFOs lock to Logic. (See
apple-sync-midi-clock-external-hardware.md.)

## Tip
Save the finished routing as a **template** so the External Instrument + MIDI
ports + audio returns are ready every session.
