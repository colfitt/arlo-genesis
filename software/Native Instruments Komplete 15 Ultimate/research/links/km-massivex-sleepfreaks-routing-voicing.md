https://sleepfreaks-dtm.com/en/softsynth/massive-x-report/
sleepfreaks-dtm.com · MASSIVE X Tutorial — Basics & Features · accessed 2026-06-11

The clearest practical reference on Massive X's ROUTING tab, VOICING/unison, the noise→PM-AUX trick, and Tracker/VR randomization — all directly useful for big evolving walls. Distilled.

## Oscillator + PM
- Two wavetable oscillators; rotate the OSC knob (Wavetable Position) to morph the waveform. Modes (Bend, Formant, etc.) transform character.
- PM sources: PM1 / AUX / PM2. The PM waveform is selectable (vs original Massive's sine-only). PM pitch uses Ratio: 1 = played MIDI pitch, 2 = octave up, 1/2 = octave down.

## Noise → PM AUX trick (key texture move)
- Two noise oscillators with pitch control. **Connect the noise OSC to PM AUX, then modulate the main OSC from the AUX setting** → "quite extreme sounds," great for experimental/inharmonic texture.
- v1.3+ added Key Track for pitched noise and importing custom audio files as noise sources.

## Routing tab
- Core rule: "sound reaching the bottom-right arrow is what you hear." Double-click a connection to delete it; drag to patch.
- OSC1 → Filter → X = filtered; add OSC2 → X = only OSC1 filtered (parallel). OSCs, noise, filters and feedback all patch by drag-and-drop.

## Effects
- Six slots: **A/B/C inserts** + **X/Y/Z stereo** (X/Y/Z has three routing-pattern options). Click a label to bypass for A/B.

## Performer
- Tempo-synced parameter automation up to 8 bars; drag the top range indicator for loop length; grid follows time signature; center line = neutral. Store up to 12 variations; switch via MIDI notes (default C-2..C-1, remappable).

## Pad / texture tips
1. **Unison** 2–6 voices, Stereo Width + Spread for detune; **Wide mode** spreads detune up to one octave → huge walls.
2. **Chord Morph** knob turns unison voices into harmonic chord voicings from a single MIDI note → instant chord pads.
3. **Tracker** scales a parameter by pitch height or velocity — e.g. low notes dry (no reverb), high notes wet.
4. **VR (Voice Randomization)** applies per-note randomization to any parameter — subtle nuance or extreme FX.
