https://www.sweetwater.com/insync/5-things-probably-didnt-realize-melodyne/
https://www.musicradar.com/tuition/tech/how-to-create-vocal-harmonies-with-melodyne-423531
https://producersociety.com/export-midi-from-melodyne-tutorial/

Composite: Sweetwater "5 Melodyne tips that aren't about pitch correction" + MusicRadar harmonies + Producer Society MIDI export · accessed 2026-06-11

## Sweetwater — 5 non-pitch tips
1. **Timing/groove fixes** — move/lengthen/shorten blobs with neighbour notes auto-adjusting; quantise timing musically without the robotic feel of hard audio quantize.
2. **Formant editing** — change timbre without pitch (see creative-sound-design note); subtle for natural doubles, drastic for effect.
3. **Tempo detection / tempo map** — Melodyne reads the tempo curve of a free-time recording; use it to make a click/grid follow a rubato performance, or to extract a groove map. (Editor/Studio for full tempo editing.)
4. **Audio-to-MIDI** — turn an audio part into MIDI to double or re-voice it with a synth/sampler.
5. **Note-by-note dynamics (Amplitude)** — rebalance individual notes' loudness inside a phrase — cleaner than riding a fader or clip-gain after the fact.

## MusicRadar — harmonies from one line (copyable workflow)
- Keep the lead Melodyne instance. **Copy the audio to a new parallel track**, open Melodyne on that copy.
- **Select notes and transpose** them to the harmony interval (e.g. +3/+4 semitones for a third within the key, +7 for a fifth, +12 for an octave). Snap to the **key/scale** so thirds stay diatonic.
- **Shift formants slightly** on the harmony copy so it doesn't sound like a pitch-shifted clone of the lead (gives each voice its own "throat").
- Repeat for a third/fourth voice → choir/stack. On a banjo or baritone this builds **harmonised drone stacks** from one take.

## Producer Society — MIDI export, dead simple
- **Settings menu → "Save as MIDI…"**, name + location, then **import the .mid** back onto an instrument/Kontakt track in the DAW.
- Each blob → one MIDI note (position, length, pitch; **velocity from blob amplitude**).
- For clean results: stabilise **pitch drift** first and keep the source clean — the export mirrors whatever pitch imperfections remain.
