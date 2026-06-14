https://brevemusicstudios.com/from-tuning-to-sound-design-making-the-most-of-melodyne/
https://la.garnishmusicproduction.com/production/creative-uses-for-melodyne/
https://www.soundonsound.com/techniques/creative-pitch-processing
https://www.macprovideo.com/article/audio-software/how-to-create-interesting-ambient-textures-melodyne

Composite of creative/sound-design sources (Breve Music Studios, Garnish Music Production, Sound On Sound, macProVideo) · accessed 2026-06-11

The interesting part — Melodyne as a sound-design / texture tool, not a vocal tuner. All of this is highly relevant to a drone/doom/shoegaze rig.

## 1. Formant manipulation (timbre without pitch)
- The **Formant tool** shifts the resonant formant frequencies up/down by cents while **leaving pitch alone** — it changes the *character* of a sound.
- Drag the **formant line up** → "lighter/smaller body" (a guitar note can read as a ukulele); drag it **down** → "darker, larger resonating chamber." Push it drastically for an obviously synthetic/alien timbre.
- Apply a **steadily changing formant value across a passage** for a smooth tonal sweep — works best on **monophonic** sources. Heard on records by Kendrick Lamar, Zeroh, etc.
- Rig move: formant-down a banjo/baritone sustain to give it an unnatural, cavernous body for a drone bed.

## 2. Time-stretch into pads / ambient beds
- Melodyne time-stretches on playback to fit project tempo; you can **drag note edges to stretch a blob without changing pitch**. Stretch a single plucked note into a long sustained tone → instant **pad**.
- **Texture Mode** (a detection/manipulation mode) is built for **ambiguous-pitch material** — polyphonic orchestral, atmospheric pads — and offers rich creative manipulation of those sounds. Use it (or Universal) to stretch a whole texture into a longer evolving bed.
- Rig move: take one banjo/guitar/synth note, stretch it 4–8×, formant-shift, then bus into Valhalla/Big Sky for a wall.

## 3. Build chords / harmonies from a single recording
- **Duplicate** the audio onto a parallel track, **delete the notes you don't want**, and **move the kept notes** up/down to the harmony intervals (within key). Stack several copies = full chord/choir from one source.
- With **Editor (DNA)** you can also reach into an existing polyphonic recording and **re-voice the chord** note-by-note, or use **chord-track adaptation** to bend a sampled riff to your song's chord changes.

## 4. Retune a sample to a scale / new tonality
- Set a **scale/key** (Pitch Grid + the **scale/tuning-fork** editor) and snap notes to it — re-tonalise a found sample or detune it into a custom temperament. Studio has full scale/tuning/temperament editing for microtonal/just-intonation drones.
- Rig move: retune a field-recording or noisy sample to your drone's root + fifth.

## 5. "Wrong-analysis" glitch generator (very on-aesthetic)
- Feed **non-musical / ambiguous audio** (speech, street noise, birdsong, a squeaking chair, a noisy pedal swell) into Melodyne, let it **guess wrong**, and harvest the **octave jumps, rhythmic displacements and ornaments** that result. Export to MIDI → drive a monophonic synth/Kontakt for glitchy, aleatoric material. This intentional-misdetection move is the most "recorded-wrong" technique in the box.

## 6. Audio-to-MIDI (Assistant+)
- **Settings → Save as MIDI** writes each blob as a MIDI note (position, length, pitch; velocity from amplitude). Re-import to drive a synth or **Kontakt** instrument — doubling a bass/banjo line, or turning a detected texture into a playable MIDI part. Clean the source (stabilise drift, minimal artifacts) for a cleaner export.

## Honesty note
Melodyne is **destructive-style monophonic-ish editing**, not a real-time modular texture box. For evolving, automatable, generative drones it complements but doesn't replace Reaktor/granular tools — its strength is *taking a real recording and re-pitching/re-timing/re-forming it offline*. Extreme stretches/pitch moves do artifact (that can be a feature here). The Sound Editor (true overtone resynthesis) is **Studio-only**.
