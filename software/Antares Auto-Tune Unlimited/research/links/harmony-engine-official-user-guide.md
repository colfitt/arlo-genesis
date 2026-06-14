https://antares-web-frontend.sfo3.cdn.digitaloceanspaces.com/documentation/pdfs/Harmony-Engine-User-Guide.pdf
antarestech.com (official) · Harmony Engine User Guide (current Auto-Tune-Central / Unlimited era) · n.d.

The authoritative spec — exact ranges and mode behaviors, deeper than any video. Distilled (the load-bearing settings detail):

**Audio Input section**
- **Input Vocal Range:** Soprano / Alto-Tenor / Baritone/Bass / **Instrument** — sets the pitch-tracking + voice-modeling algorithm. (Confirms an explicit "Instrument" mode for non-vocal sources — set this for banjo/baritone/synth.)
- **Model Glottal:** soft / medium / loud / intense — models the glottal *waveform* (vocal-cord vibration character), NOT level. Start **Medium** to preserve the source's character; push toward loud/intense for a more "sung-hard" timbre on the generated voices.
- **Tracking:** how much waveform variation still counts as "periodic." Default for a clean isolated signal. Raise it for noisy/breathy/not-well-isolated input; **lower it if you get clicks/pops** (artifacts). Key for getting it to lock onto a non-vocal source.
- **De-Noise:** reduces noise/artifacts from the formant-correction + pitch-shift process.

**Harmony Source — 7 modes (the whole point)**
- *Interval Modes* — **Fixed Interval** (semitones, ignores key/scale → voices move in strict parallel; per-voice Interval menu = **−24 to +24 semitones**, i.e. ±2 octaves) and **Scale Interval** (scale degrees, conforms to Key/Root + Scale; Interval menu = **16vb to 16va**, i.e. ±2 octaves in scale steps).
- *Chord Modes* — **Chord Degrees** (pick Key/Root + Scale, then which scale degree to build the chord on, e.g. "4th degree of Bb minor") and **Chord Name** (pick a chord by name e.g. "Eb Minor 7" with no regard to scale). Both auto-assign a pitch to each of the 4 voices from Inversion / Register / Spread.
- *MIDI Modes* — **Chord Via MIDI** (you hold a chord on MIDI, it distributes those notes to the 4 voices per Spread/Register), **MIDI Omni** (receives notes on all channels, assigns pitches directly — max 4 notes sound at once = the 4 voices; play it like a 4-voice synth), **MIDI Channels** (each Harmony Voice listens to its own MIDI channel 1–4 → total per-voice control).
- **Inversion:** Root / 1st / 2nd / 3rd Inv (sets which chord tone is the lowest voice) — Chord modes only.
- **Spread** = how widely spaced the chord voicing is; **Register** = shifts overall pitch up/down. Active in Chord modes + Chord Via MIDI.
- **MIDI Velocity Sensitivity:** 0 = ignore velocity (levels = channel gains); higher = velocity drives voice levels. MIDI modes only.

**Voice Controls — 5 channel strips (Input + 4 Harmony Voices)**
- Per voice: **Interval** menu, **Gain** + level meter, **Solo**, **Mute**, **Pan** (Pan only available on a **stereo** instance — so always instantiate stereo for a wall), and **Throat Length** (formant): **>1.00 lengthens** the throat → **lower** formants; **<1.00 shortens** → **higher** formants. Per-voice throat = give each stacked voice a different body (a couple low/dark, a couple high/airy) for a real ensemble spread.

**Vibrato Controls (per voice, independently generated)**
- **Rate** (Hz), **Onset Delay** (ms before vibrato starts), **Pitch Amount** (vibrato pitch width), **Amplitude Amount** (loudness wobble). Note: **turn Naturalize to 0** when using generated vibrato so natural + generated don't fight.

**Humanize / Glide / Freeze (global)**
- **Naturalize:** how much of the *original's* natural vibrato + pitch drift passes into the harmony voices. Low = remove it (tighter/more synthetic); high = let it through.
- **Pitch Variation** + **Timing Variation:** random per-voice pitch/timing spread — higher = bigger max random offset, different per voice (this is what turns a stiff stack into a breathing ensemble/wall).
- **Glide Transition Rate:** time for voices to slide note-to-note on legato; **higher = slower transitions** (THE Prismizer/portamento control — crank it for the smeared glide).
- **Freeze Pitch:** freezes the Harmony Voices at their current pitch while the Input Voice keeps moving — explicitly "for creating **sustained chords** in the Harmony Voices underneath a lead." This is the drone-hold move: hit Freeze to lock a held choral chord under a moving/continuing source.

**Choir (the multiplier, 5 channels — one per voice incl. Input)**
- **Choir On** per voice + global **Bypass**. **Choir Size = 2 / 4 / 8 / 16** unison voices generated *per* Harmony/Input voice. So 4 harmony voices × 16 = up to 64 generated voices (+ Input ×16 = 80 total in theory).
- **Choir Vibrato / Pitch / Timing Variation** (global): random per-choir-voice spread in each; higher = bigger possible variation.
- **Choir Stereo Spread:** each voice's **Pan position is the center** of its choir's spread — pan a Harmony Voice left and its 16 choir voices spread out around the left. So per-voice pan + choir spread = control where each sub-cluster of the wall sits.

**Presets / automation**
- **15 Harmony Preset buttons** (store Harmony Source, Key/Root, Scale, Chord, Inversion, Register, Spread, MIDI Vel Sens, per-voice Interval) and **6 Voice Parameter Preset buttons** (all Voice Controls except Interval, plus Vibrato + Choir). Both are **DAW-automatable** → program a whole chord/voicing progression by automating preset buttons (no MIDI needed — see Plugins-Masters transcript).
- **Logic Pro insert:** Audio Units > Antares > Harmony Engine, on an audio/instrument track or bus. (Mono vs stereo: stereo instance required for pan/spread.)
- **Auto-Key Detection** preference: listens for key/scale from the separate Auto-Key plugin. **Knob Control:** Linear vs Circular drag.

Honest: vocal-framed throughout, but it explicitly supports "single vocal **or monophonic instrument**" and ships an **Instrument** input-range mode — so the banjo/baritone/synth-lead use is sanctioned by the manual, not just extrapolated.
