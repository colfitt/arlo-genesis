https://aberrantdsp.com/wp-content/uploads/2020/11/SketchCassette-II-User-Manual.pdf
aberrantdsp.com · Aberrant DSP (Ben, Dan, Jon) · 2020 (manual, current for v2)

Authoritative parameter reference, distilled. This is the single best map of what every control does.

## Tape Type (the filter heart of the plugin)
- 12 unique tape frequency-response profiles, modelled from real tapes.
- TOP ROW = formulation: **Type I (Ferric)**, **Type II (Chrome)**, **Type IV (Metal)**, and a 4th button = **bypass filtering entirely**.
- SECOND ROW = quality: **Cheap, Value, Standard, Master**.
  - Type I = common/cheap; good lows, reduced highs (darkest, most "lo-fi").
  - Type II (Chrome) = much better highs, sometimes boosting highs several dB.
  - Type IV (Metal) = flattest/most extended response, near-CD in some cases (cleanest).
  - Higher Quality = more high-end; but "each profile has unique characteristics — try them all."
- Practical: Type I + Cheap = grimiest; Type IV + Master = barely-there "tape glue." The bypass button lets you run ONLY wow/flutter/dropout/hiss with no tonal filtering.

## Age
- Slider adds low-pass filtering = simulates high-frequency loss of an aged cassette.
- "This effect pairs well with dropouts for a realistic aged sound."

## Hiss
- Filtered noise based on spectral profiles of real cassette hiss. Range **-96 dB to -30 dB**.
- Full left = noise OFF.

## Saturation
- Soft-clipping model from real cassettes; adds harmonics + subtle compression.
- Right button switches algorithm: **Type A (gentle) vs Type B (harsher, brighter)**.
- INCLUDES GAIN COMPENSATION — push it hard, level stays consistent (so saturation is "free" to automate without volume jumps).

## Dropouts
- Models lost signal on worn tape = a combination of fast random amplitude modulations + larger periodic dropouts (signal greatly reduced for UP TO SEVERAL SECONDS).
- **Depth** = overall strength of dropouts.
- **Intensity** = adds the longer/larger dropouts as you raise it.
- **Width** = separation between L/R amplitude modulations → increases stereo width of the dropout effect. Full LEFT = dropout applied in MONO. (This is the key stereo-width control — important for mono-sum safety and for stereo-ization of a mono source.)

## Wow + Flutter (pitch modulation)
- Wow = lower-frequency speed/pitch modulation; Flutter = higher-frequency.
- Each has **Depth** (how much pitch bends) + **Rate** (how fast).
- Modulator SHAPE selectable: **sine** (vibrato-like), **random noise** (closest to a genuinely sick tape player), **smoothed saw** + **reverse smoothed saw** for Wow (periodic pulses of pitch bend).
- **Tempo Sync**: rate snaps to note values (½, ¼, ⅛, ¼-dotted, ¼-triplet…). **Offset knobs** move the start point of the wave — most useful in sync mode to align the modulation with the beat.
- **Flanging** knob: mixes the wow/flutter-modulated signal with dry → flanging; with deep wow/flutter = "watery throwback sounds."
- **FM Mode** (Flutter Modulation): the Wow modulator (renamed "Mod.") instead modulates the *rate* of the Flutter modulator. Realistic uses = sticky capstan, dying battery; plus outlandish stuff. A modulation meter appears next to Flutter Rate when enabled.

## NR Comp (Noise Reduction)
- Emulates the "encode on record, decode off on playback" Dolby misuse → bright, shimmery, compressed signal.
- Implemented as upward + downward MULTIBAND compression.
- **Brightness** = high-frequency boost amount.
- **Amount** = overall strength.

## Mix (TWO dry/wet knobs)
- **Tape mix** = dry/wet for the tape FILTERING — dial back a profile you like but find too exaggerated.
- **Comp. mix** = dry/wet for NR Comp → lets you use it as a PARALLEL compressor, making its extreme settings usable in many scenarios.
- NOTE (per Theatre of Noise blog): there is NO single global dry/wet, and no hiss envelope — these two mix knobs are filter + comp only. Workaround for an overall blend = put it on a parallel/aux and blend the whole instance.

## Formats / OS (manual)
- Windows 7+: VST3, AAX (64-bit). macOS 10.10+: AU, VST3, AAX (64-bit), Intel or Apple Silicon. Restart DAW (or computer) after install.
- Price (site, 2025): $36 (older reviews quote $30).

## Signal-flow / gain-staging notes
- Saturation has built-in gain comp, so it's the safe knob to push.
- Tape profiles change overall tonal balance/level; Tape-mix knob recovers headroom.
- Width-at-full-left = mono dropout; raise Width only when you want stereo motion (mono-compatibility gotcha lives here).
