https://drolez.com/blog/music/ableton-live-lite-vs-intro.php
drolez.com · Ludo · updated 2025-07-17

# Live Lite vs Intro — the exact device gap (matters for shared racks)

Confirms what Lite LACKS even versus the next tier up (Intro). Critical because many
"free Ableton ambient racks" are built/tested in Standard/Suite and quietly assume
devices Lite doesn't have.

## Counts
- Lite: **8 tracks**, 2 GB library. Intro: 16 tracks, 5 GB library.
- (Scenes: Lite 16 per the official features page.)

## The 5 audio effects Intro adds that LITE DOES NOT HAVE
1. **Auto Pan**
2. **Gate**
3. **Grain Delay**  ← kills any granular-smear rack relying on it
4. **Looper**       ← confirms NO native loop pedal in Lite
5. CC Control

## Other things in Intro (and up) but NOT in Lite
- **LFO device** (the M4L-style modulation device) — so racks that auto-modulate
  macros via the LFO device won't work; use device-internal LFOs instead.
- **Expressive Chords** (MIDI).
- **7 CV utilities** + CV tools (Eurorack control).
- Video import/export.

## Implication for shared ambient racks
A "shared ambient rack" is Lite-safe ONLY if every device in it is in Lite's 15-effect
roster (Auto Filter, Beat Repeat, Channel EQ, Chorus-Ensemble, Compressor, Delay,
EQ Three, Erosion, Limiter, Phaser-Flanger, Redux, Reverb, Saturator, Tuner, Utility)
+ Audio Effect Rack. If it contains Looper / Gate / Grain Delay / Auto Pan / EQ Eight /
Echo / Frequency Shifter / Spectral* / Overdrive / Drum Buss / Corpus / any M4L → it
will throw a missing-device error in Lite. ALWAYS check the device list before trusting
a downloaded .adg.

## Certainty
HIGH — explicit edition comparison, corroborated by Ableton's own features page (which
omits Looper/Gate/Grain Delay/Auto Pan from Lite).
