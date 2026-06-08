https://www.youtube.com/watch?v=md2Ecg8G6pI
SON WU (Sam Woo) · sampler // OP-1 field TUTORIAL · 2023-07-30

A focused, OP-1 Field-specific walkthrough of BOTH sampler engines: the SYNTH SAMPLER and the DRUM SAMPLER, with every parameter.

## Recording / sampling setup (both engines)
- Press the MICROPHONE button to enter the sampling menu.
- Source options (BLUE encoder): MICROPHONE, RADIO, USB, or INTERNAL (the EAR — samples whatever you hear inside the unit). Plug a cable into the line input and the mic source switches to LINE IN (choose stereo or mono).
- RECORDING GAIN knob: set the level so the meter reaches quite high without hitting the top (avoid distortion, but not too quiet).
- RECORDING THRESHOLD: recording only STARTS once the input exceeds this level. Turn it all the way up and it won't trigger (stays "standby"); turn it down below your signal and it triggers as soon as you make a sound — useful for auto-starting on the first transient.

## SYNTH SAMPLER
Concept: sample a SINGLE note, then play it chromatically across the keyboard at different pitch intervals. Max 6 seconds per sample.

- The OP-1 maps the ORIGINAL PITCH of your recording to whichever KEY you hold while sampling. So to keep tuning correct, play the matching note (press C key → play C on the source instrument). You can release early; you don't have to use all 6 seconds.

Parameters (top row):
- BLUE = sample START point.
- RED = sample END point.
- Then the loop START and loop END points: set the loop end (gray line) and loop start (brown line) and the sample loops between them while you hold the key — lets you sustain indefinitely.
- Clickiness at the loop boundary = volume/timbre mismatch between loop start and end. Smooth it with [Shift]+GRAY encoder (a crossFADE). Adjust loop points + fade to get a seamless infinite sustain.
- To remove the loop entirely, move the loop start point all the way to the sample end point.

Parameters (shift / hidden row):
- [Shift]+BLUE = playback direction (forward / BACKWARD — reverse can sound great).
- Note: NO time-stretching — pitch up shortens the sample, pitch down lengthens it.
- [Shift]+RED = sample VOLUME (fix a too-loud/too-quiet recording; also makes the waveform easier to see).
- TUNE parameter = correct tuning if you recorded on the wrong key, or detune deliberately (e.g., correct an out-of-tune kalimba after the fact).
- You can still set the envelope, effects, and LFOs as on any synth.

## DRUM SAMPLER
Get to it (if not shown): [Shift]+1 → select Drum.

Concept: record one long sample (max 20 seconds) and the OP-1 AUTO-SLICES it. It takes the whole recording and divides it into 16 EQUAL slices across the lower keys, plus 8 slices (each twice as long) across the upper keys. All slices reference the SAME underlying sample — each key just has its own start/end points within the 20 s.

- Workflow tip: record a full, in-time 4-bar loop and stop at the right moment, so the auto-distributed slice points already land roughly in time — far easier than recording an odd length and hand-setting every slice.
- A white marker on the waveform shows which part of the sample a given slice is playing.

Per-slice parameters (each is PER SLICE, not global):
- BLUE = PITCH of that slice (pitching one slice does NOT affect the others; you must pitch each manually).
- (ochre) = slice START point.
- GRAY = slice END point. (Only one start/end per slice — no separate loop points like the synth sampler.)
- RED = PLAY MODE:
  - arrow alone = plays only while the key is held (cuts off on release).
  - arrow + line = always plays to the end even on a short tap.
  - arrow + G = CHOKE/MUTE group: two slices both set to arrow+G cut each other off (good for hat open/closed, etc.).
  - loop = loops between start/end while the key is held.

Per-slice shift parameters:
- [Shift]+BLUE = playback direction (forward / backward).
- ATTACK = slope at the start; helps eliminate clicks/pops on badly-chopped slices (attack 0 = full volume immediately).
- [Shift]+RED = slice VOLUME (per slice).
- Last knob, two modes:
  - L/R mode = simple PANNING of the slice (counterclockwise = left, clockwise = right).
  - [Shift]+press the brown knob switches to A/B mode = STACK/MORPH between two layered samples through the center. Demonstrated on a stock kit's snare (left and right halves are different samples): in A/B you hear both through the middle and morph from A (one sample) to B (the other), letting you blend two sounds into one slice. This is a DRUM-sampler-only capability the synth sampler lacks.
