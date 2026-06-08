https://www.youtube.com/watch?v=tW5IOnCLTyg
Ollie Loops · OP1 FIELD: IMPROVED TAPE WORKFLOW · 2026-05-26

Note: This is a recent (May 2026) OP-1 Field-specific tape deep-dive. It documents firmware features added AFTER the dossier's reference manual (OS 1.5.7) — most importantly tape UNDO, count-in, and the new "amp" synth engine.

## Premise

The OP-1 Field is a digital synth, drum machine, sampler, and four-track audio tape recorder. Making music requires recording audio live — there are sequencers and an arpeggiator, but the workflow is performance-oriented, not program-oriented. Recent firmware brings new features that make this more forgiving. The video frames the new tools as the "eraser, ruler, and colored pencils" of the tape workflow.

## Tape UNDO / REDO (new)

Until recently, OP-1's workflow was "pen-based and permanent" — a mistake while recording meant scrapping material and starting over. UNDO was added to tape mode on OP-1 Field.

- UNDO: press and hold [Tape], then press the LEFT arrow. You can undo up to seven times.
- REDO: press and hold [Tape], then press the RIGHT arrow.
- This mostly benefits OVERDUB recording, where layers are otherwise baked in.

## Metronome / count-in (new)

- Press the metronome button to display the metronome page. Current tempo shows on screen.
- Turn the BLUE encoder to adjust BPM. You can also tap tempo by repeatedly pressing the metronome button.
- Turn the ORANGE encoder to set metronome volume; PRESS the orange encoder to change the metronome sound.
- Press play to engage; press stop to stop.
- COUNT-IN: while in tape mode, press and hold [Shift] then [Record] to arm. Press [Play] to start a four-quarter-note count-in before recording begins. You can practice during the count-in.

## The "amp" synth engine (new — guitar/instrument amp + tone-shaping)

A new synth engine catered to guitar players but usable on any input source including the internal mic (a "Swiss Army knife for shaping tone").

Setup:
1. Plug instrument into the 3.5 mm audio input; open the amp engine in synth mode.
2. Your instrument is likely mono, but the input defaults to stereo. Press the [Input] button and rotate the OCHRE encoder to toggle the input to MONO (you then hear it in both channels).
3. Set INPUT GAIN on this page so it peaks around 60–70% on the meter (this is the first of several gain stages; too high gives undesirable digital distortion).

The four amp encoders (press [Synth] for the main amp page):
- Encoder 1 = amp VOLUME (not input gain — this is after the input stage, the volume of the amp synth).
- Encoder 2 = COMPRESSION.
- Encoder 3 = TONE (EQ from center: counterclockwise rolls off highs / emphasizes lows; clockwise removes lows / boosts highs).
- Encoder 4 = DISTORTION (clockwise, subtle to heavy).

Other amp pages:
- [T2] = a responsive, accurate TUNER. Because amp works with the built-in mic, you can tune acoustic instruments too — always wear headphones when using the mic as input to avoid speaker feedback.
- [T3] = the EFFECT page in the signal chain (e.g., reverb or the new PHASER effect).
- [T4] = LFO page.
- Save your own amp presets to the eight preset buttons like any other synth.

## Four-track strategy (template thinking)

Treat the four tracks like layers / tracing paper. A suggested template: track 1 = melody; track 2 = secondary melody / accompaniment / vocal; track 3 = bass; track 4 = drums and percussion.

## Overdub recording (the "uncut gem")

Recording to a tape track ADDS to existing material instead of overwriting (unlike most tape recorders). You can double- or triple-stack guitars on a single track, freeing other tracks. Each layer is "baked in," but the new UNDO makes them only "half-baked" — you can take risks and undo mistakes.

### Layering a drum kit on one track (worked example)
1. Loop a few bars in tape mode.
2. [Drum] mode: audition kits; switch kits via the eight presets, or load a different preset with [Shift]+preset number. Return to tape with [Tape].
3. Set per-source input gain (4th encoder adjusts input gain before it records to the track); use the metronome's 4th encoder to set metronome level.
4. HI-HAT first (to establish rhythm): use the RECORD+NOTE method — press and HOLD [Record], then play a note; recording starts on the first note pressed, landing the hat on beat one. Press play/stop to end.
5. SNARE: use the COUNT-IN ([Shift]+[Record] to arm, [Play] to count in), then play the snare pattern.
6. KICK: RECORD+NOTE method again to land on beat one.

## Looping & recording sections (build a song from loops)
1. [Tape] mode. Press metronome, set tempo with BLUE encoder, return with [Tape].
2. Preset button 3 toggles LOOPING on/off.
3. Press and hold [Shift] + LEFT/RIGHT arrows to move the playhead along a snapping grid (the "ruler").
4. At free space, press preset button 1 to set the loop IN point; [Shift]+RIGHT moves one measure at a time (work in 4-bar sections); press preset button 2 to set loop OUT.
5. Press play to start the loop; stop to end.
6. [Shift]+[Stop] cycles grid RESOLUTION: whole measures → halves → quarters → eighths.

## Editing: lift, drop, split
- [Lift] removes the current track from the nearest splits at the playhead AND copies it to memory. Use it to remove a bad take (or use UNDO).
- [Drop] pastes the tape stored in memory at the playhead — drop repeatedly to repeat a section.
- [Split] (scissors) cuts the tape at the playhead. Scrub with arrows to the start of a sound, split, scrub to the end, split, then move the playhead over the piece and [Lift] to remove it.
- Advanced: splitting a sound at intervals creates a choppy, DJ-crossfader-like effect.

## Shift + select commands
- [Shift]+[Lift] = lift ALL four tracks at once (to scrap a song, or to MERGE).
- [Shift]+lift then DROP onto a selected track = MERGE tracks down to that track (frees up the other tracks). Record each instrument to its own track for flexibility, then drop-merge when committed.
- [Shift]+[Split] = MERGE tape pieces (join splits near the playhead) to clean up for efficient copy/paste.

## Copy a drum sample into the SYNTH SAMPLER to play it melodically (e.g., an 808-style bass)
1. In drum mode, find a kick with long release / slight distortion (good as an 808 bass note).
2. Move the playhead to free tape, switch to an open track. Press and HOLD [Record], press and HOLD the note of the kick sample, hold 4+ seconds, release.
3. Move the playhead over that tape piece, press [Lift].
4. Press [Synth], select a preset using the SYNTH SAMPLE engine, press [Drop] to paste the tape into the sampler. Play across the keys; tweak to taste; add an effect like PUNCH.
5. Save with [Shift]+hold a preset number (optionally rename).
Then record the bass into a track using RECORD+NOTE to start on beat one.

## Performing the song
- TAPE MUTES: [Shift] + a track button mutes/unmutes that track. Use mutes to bring drums/sections in and out within the same loop.
- Preset numbers 4–8 are TAPE TRICKS for live performance.
- The mixer ([Mixer] button) fine-tunes levels.

## Arpeggiator setup (for hi-hats etc.)
1. [Shift]+[Sequencer]; select ARPEGGIO with the BLUE encoder; press to confirm.
2. [Sequencer] toggles it on/off; when on it shows the arp page.
3. Rotate BLUE encoder for note value (e.g., eighth notes). Trigger mode = all; pattern = 4/4; HOLD off (hold on = self-repeating note; off = holds while key held).
4. Record hats to a track; rotate the BLUE encoder WHILE recording to change note intervals (e.g., eighths → 16ths → eighths) for the changing-hat trick.
5. Toggle the sequencer off when done.

## Punch-in recording
While the tape plays back, press and HOLD [Record] to momentarily record one or more notes without stopping playback — practice along to the loop, then punch in without disrupting flow. Used in the example to layer a chopped piano part.

## Other examples / techniques shown
- Chopped-piano effect: record the second half of a phrase, split at each measure, lift the middle pieces (tails), then punch-in the first half on opposite measures; repeat to layer.
- Built-in mic used for a "scratch" sound (finger scratched over the mic) — "mix recording" of internal + external sources.
- Guitar/bass doubling: record the same riff twice through the amp engine to thicken; bass through amp with high compression + lowered tone.
- Synth-bass example used the Dr Wave engine with heavily tweaked parameters.
- Tambourine wrapped in a bandana, struck with chopsticks, recorded via mic + amp engine, as a loose snare/percussion layer.

## Verdict
The presenter calls the improved workflow + amp engine a strong pairing that brought OP-1 Field to the front of their portable setup — best for those who enjoy playing live and recording in a quasi-Portastudio format.
