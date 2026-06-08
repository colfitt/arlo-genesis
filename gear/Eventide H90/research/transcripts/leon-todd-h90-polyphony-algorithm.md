https://www.youtube.com/watch?v=xyiMDam0jkQ
Leon Todd · Eventide H90 "Polyphony" Algorithm · 2023-02-15 · 12:15

Deep dive on the Polyphony pitch algorithm — the SIFT-based polyphonic shifter (directly relevant to chordal banjo and big stacked tones). Cleaned to prose.

## What it is
Two independent pitch-shifting voices, each delayable with feedback — similar in concept to existing H9/H90 pitch algorithms, BUT it supports POLYPHONIC input: you can play full bar chords and extended chords into it, not just single notes/octaves/fifths. Sounds organ-like with two voices stacked. Think of it as two delays with pitch shifting, where the pitch shifters can be standalone or feed back into one another.

## Per-voice controls
- **Interval** — the pitch interval for the voice.
- **Detune** — slight detune of that interval to fatten.
- **Delay** — per-millisecond up to ~2 seconds, OR tempo-synced subdivisions.
- **Feedback**.
- **Pan**.
- **Feedback switch (in / out)** — places the voice's pitch shifting inside or outside the feedback loop.
- **Auto-EQ** — compensates for timbre change when pitch-shifting (keeps shifted voices natural).
- **Inst Type: Pitched / Percussive** — sets tracking behavior for the input source.

## Settings demonstrated (concrete)
- **Organ-like base patch** — octave down + octave up, with delay added and voices panned; "instantly inspiring." He used a dotted-eighth on one side and a quarter-note delay on the other, then panned and added feedback.
- **Polyrhythm (factory)** modified to a 5th up + octave down; rhythmic delay values, feedback, panned hard left/hard right, NO detune, 50% mix — "might be the most inspiring sound in here."
- **Keyboard/organ patch** — octave up + octave down (like organ drawbars).
- **5th up + perfect 4th down** with feedback — used to demonstrate pitch shifting in vs out of the feedback loop.
- **Mega stereo tone for big riffs/chords (with distortion)** — octave up + octave down, a little detune on each voice, voices panned slightly left/right for width and girth.
- **12 Stringy (factory)** — Voice 1 Unison with a little detune to fatten, Voice 2 octave up with slight detune down, everything else ~zero — a 12-string emulator.
- **POG-style** — octave down + a little octave up with detune.
- **"Terrify your neighbors"** — both intervals set to a tritone, lots of delay feedback, feedback switch = IN, long delays (demoed with diminished chords).

## Takeaway
If you only do single-note pitch shifting, you might prefer Quadravox (up to four voices) and not reach for Polyphony — but for applying pitch shifting to CHORDS, and for the inspiring factory presets, Polyphony is the one. Demoed on H9 hardware editor on-screen; identical algorithm on the H90.

Rig note: this is the banjo-chord and baritone-chord engine. Set Inst Type = Percussive for banjo (preserves transients); use Pitched for smoother large intervals. Octave-up+down with detune and slight pan = the "12-string banjo" or organ-pad treatment for banjo-as-lead chordal phrases.
