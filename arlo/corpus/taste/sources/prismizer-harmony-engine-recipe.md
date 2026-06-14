https://www.sageaudio.com/blog/music-production/how-to-actually-create-the-prismizer-vocal-effect.php
sageaudio.com · Sage Audio · n.d. (corroborated by musicproductionknowledge.com, soundbridge.io)

# How the Prismizer is actually built (Antares Harmony Engine + MIDI)

Distilled concrete info:

- **Core plugin = Antares Harmony Engine Evo**, inserted as a **MIDI-controlled instrument** (not a
  normal insert).
- Recipe:
  1. Record a clean vocal, minimal processing.
  2. Harmony Engine on an instrument track; **Harmony Source = "MIDI Omni"** (keyboard-controlled).
  3. Sidechain it to monitor the vocal.
  4. **Play chords on a MIDI keyboard while the vocal plays** → up to **4 pitch-shifted harmony
     layers** in real time = the "halo."
- **Key settings:**
  - **Glide / transition rate = LONG** → notes slur/glide between pitches (the signature smear).
  - **Throat length** per register: **shorter = more artificial/cartoonish** (pitched-up
    harmonies), **longer = pitched-down** harmonies. The formant manipulation is what makes it
    read "synthetic choir" rather than backing vocals.
- The name = **prism + harmonizer**: the polyharmonic pitch gives prism-like dispersion/saturation.
- Origin: **Francis Starlite** (Francis & the Lights) perfected reaching bright polyphony without a
  vocoder or plain Auto-Tune. Heard on Frank Ocean *Blonde*, Bon Iver *22, A Million*, Francis's
  *Farewell, Starlite!*

Rig takeaway (honesty): the Prismizer is SOFTWARE with NO hardware equivalent the user owns. Index-
only. The closest HARDWARE approximation of the RESULT (a pitched harmony cloud around one note) is
the **Walrus QI Etherealizer** (grain-freeze + chorus pads pitched up/down) — but it cannot be
MIDI-played into chords, so it produces a fixed/drifting cloud, not played harmony. Dark Star's dual
±2-oct shifters give two fixed pitched voices; VG-800 ALT-TUNE HARMONY gives one fixed diatonic
voice on the banjo. All approximate; none reproduce the played 4-note halo.
