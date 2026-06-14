https://native-instruments.com/ni-tech-manuals/massive-x-manual/en/wavetable-oscillators
native-instruments.com · Massive X Manual — Wavetable Oscillators · accessed 2026-06-11

The authoritative architecture reference for the two wavetable oscillators, the 10 wavetable MODES, the Wavetable Position parameter, and the Phase-Modulation (PM) system. This is what makes Massive X good at evolving timbres: modulating Position and PM amounts produces constantly-morphing spectra. Distilled.

## The 10 wavetable oscillator modes
1. **Standard** — default; acts like a low-pass by scanning band-limited waveforms (square → sine as Filter is reduced). Controls: Phase Direction (Fwd/Back), Polarity (+/-), Internal Phase (on/off = waveshaping), Filter, Phase.
2. **Bend** — raises/lowers readout speed at different positions; sections compress/expand. Sub-modes: Bend Curve (Strong/Medium/Gentle), Direction (Neutral/Up-Down/For-Back; Up-Down removes even harmonics). Controls: Filter, Bend.
3. **Mirror** — reads the table back and forth; high Ratio forces folding → hard-sync-style. Controls: Bend, Ratio.
4. **Hardsync** — classic hard sync with NO second oscillator. Sub-modes: Window (Hard/Soft/Grain), Direction. Controls: 2nd Level, Ratio (frequency ratio of internal sync osc).
5. **Wrap** — like Hardsync but fewer pitch artifacts under modulation. Sub-modes: Window, Direction. Controls: Filter, Ratio (centered from cycle midpoint).
6. **Formant Capture** — holds constant amplitude across pitches (kills the "Mickey Mouse" effect, reintroducible independently). Best with formant/vowel tables. Controls: 2nd Level, Formant.
7. **ART** (Artificial Resonance Technology) — mimics a resonant filter via hard sync + windowing; bandpass-sweep replication beyond a real filter. Sub-modes: Window (Hard/Bity/Soft), Direction (incl. unique FU-DB), Body. Controls: Width (resonance-like), Pitch (cutoff-like).
8. **Gorilla** — aggressive, exaggerated; best with spectrally-simple inputs. Sub-mode: K!ngs (King/Kong/Kang). Sub-control: Ratio ×1–×6 (×2 recommended). Controls: Over (strength), Bend.
9. **Random** — two internal randomizers → noise sounds, even more extreme than Jitter. Sub-modes: Mode (Fluid/Thunder/Divide), P.Rnd. Controls: Position Jitter/Clock Divide, Jitter.
10. **Jitter** — random deviations at cycle end (faster/softer readout) → glittery on sparse tables. Sub-mode: Jitter Rate (J1 every cycle / J2 every 32 / J3 every 128), P.Rnd. Controls: Filter, Jitter.

## Wavetable Position
"Scans through the waveforms in the selected wavetable." **Modulating Position with envelopes or LFOs creates intricate sweeping, morphing, dynamic timbres** — the core of evolving textures. Changes are shown visually.

## Phase Modulation (PM) architecture
- **2 PM oscillators**. Each: Pitch Mode (Keytrack / Ratio / Fix), Waveform menu (Sine, Tri, TriB1, TriB2, TriB3, SinN — low-harmonic = ideal modulators), PM Amount (depth into the wavetable oscillators; modulatable), Aux Amount.
- **PM Aux bus** — a routing input letting ANY source in the signal path apply phase modulation (assigned on the Routing page). Any generator/processor can feed it → cross-modulation or feedback chains.
- Each wavetable oscillator has a **PM/Aux assignment button** activating the PM oscillators and/or Aux input. PM oscillators output to the phase inputs of both wavetable oscillators.

## Core oscillator controls
Pitch (semis/cents, modulatable), Pitch Mode (Keytrack/Ratio/Fix), Level, Internal Phase on/off (off = waveshaper mode, needs PM osc or Aux input).

Signal flow: WT osc 1 & 2 → PM osc 1 & 2 + PM Aux bus → phase-modulate both WT oscillators → filters / effects / amp via the Routing page.
