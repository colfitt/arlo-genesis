# Operator and Analog — Live's Foundational Synths

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Operator, Analog; Sound on Sound *Ableton: Smooth Operator*; MusicRadar Operator definitive guide; Sound on Sound *A Is For Analog*; Gordon Reid *Synth Secrets* (Sound on Sound, FM and subtractive parts)
**Tags:** `daw-ableton`, `live-12`, `device`, `operator`, `analog`, `fm`, `subtractive`, `synthesis`

---

## Two stock synths, two different philosophies

Operator and Analog are Live's pair of "foundational" stock synths — both have shipped in Live Suite for over a decade, both are still actively maintained, and both predate Wavetable (Live 10), Drift (Live 11.3), and Meld (Live 12) by enough years that the production lineage of "the Ableton sound" was largely shaped by them. **Operator** is Live's FM workhorse — four operators, eleven routing algorithms, additive waveform editing, and a single shared filter. **Analog** is Live's classic dual-oscillator virtual-analog subtractive — two oscillators feeding two filters and two amps in series or parallel, two LFOs, dedicated envelopes per stage. The two devices map cleanly to the canonical synthesis pair: pick Operator when the source needs *generated* harmonic complexity (bells, e-pianos, FM bass, glassy plucks), pick Analog when the source needs *filtered* subtractive shaping (warm leads, thick pads, classic basses). For wavetable-style movement reach for [Wavetable, Drift, or Meld](https://www.ableton.com/en/manual/live-instrument-reference/) (covered in the B10 file).

## Operator's architecture in one paragraph

Operator combines [four oscillators (labeled A–D), an algorithm routing matrix, a global filter, per-operator envelopes, dedicated LFO and pitch envelopes, and global voice/output controls](https://www.musicradar.com/how-to/the-definitive-guide-on-how-to-use-operator-in-ableton-live). Each oscillator can act as a carrier (audible) or a modulator (modulates a carrier's frequency to create FM sidebands). The signal flow within an algorithm runs top-down: operators higher in the icon modulate operators lower down, and only the bottom-row operators reach the output. This compactness is Operator's design genius — eleven algorithms cover most useful FM topologies without the DX7's thirty-two. Each operator also has its own envelope, allowing modulators with long decays to evolve the timbre of carriers with shorter envelopes — the core technique behind FM e-pianos, mallets, and bells. The shared filter sits at the algorithm's output and applies subtractive shaping on top of the FM-generated content.

## Operator's eleven algorithms

The eleven algorithms appear as icons in the global section of Operator and define which operators modulate which. The full set covers: stacked-pair, parallel-pair, and full-cascade configurations of three or four operators acting as modulators, plus the "additive" all-carriers-parallel algorithm where no FM occurs and the four oscillators sum directly. Live's manual diagrams them visually rather than naming them; producers refer to them by position (top-left, second-row-left, etc.). Key picks for common sounds:

- **All four operators as parallel carriers** (the "organ" / additive algorithm) — pure additive sum, no FM. Use for organ stops, pads, additive harmonic design.
- **D→C→B→A serial cascade** — three modulators stacked into a single carrier. Maximum spectral complexity, hardest to predict. Use for evolving textures and metallic sound design.
- **D→A and C→B parallel pairs** — two independent FM pairs summed at output. Most usable for layered patches (e.g., bell tone + sub tone in one patch).
- **D and C as parallel modulators into B which modulates A** — classic e-piano / tine algorithm. Two modulators with different ratios let you shape attack and sustain timbre independently.

## Operator oscillator parameters

Each Operator oscillator exposes: **Coarse** (harmonic ratio — *not* semitones; 0.5 = octave down, 1 = unison, 2 = octave up, 3 = perfect twelfth, etc.), **Fine** (one-octave detune in 1,000 steps), **Wave** (built-in: sine, saw, square, triangle, two noise types; switches to "User" when partials are edited additively), **Phase** with retrigger toggle, **Feedback** (top-row operators only — self-modulation that adds harsh high harmonics), **Osc<Vel** (velocity raises the operator's pitch), and a dedicated multi-stage envelope. The additive editor allows up to **64 partials per waveform**, drawable directly on the operator panel — this is what makes Operator a genuine additive synth and not just an FM synth with sine carriers. **Repeat** radically shifts timbre by repeating the harmonic series above the visible 64-partial display, useful for "buzzy" or formant-like tones. Coarse 0.5/1/2/4/8 are the octave ratios; integer values are most musical; non-integer values create inharmonic spectra (good for bells and percussion).

## Operator's filter and global section

The Operator filter — added in Live 9.5 and unchanged through Live 12 — is a multi-mode resonant filter with four [analog-modelled circuit types](https://performodule.com/2019/03/07/abletons-auto-filter-comparing-circuit-models/): **Clean** (digital, transparent), **OSR** (state-variable, hard-clipping resonance, modelled on the Oxford OSCar), **MS2** (Sallen-Key, soft-clipping, modelled on the Korg MS-20), **SMP** (custom hybrid), and **PRD** (ladder filter, no resonance limiting, modelled on the Moog Prodigy / similar). Filter types include lowpass, highpass, bandpass, notch, and morph. The filter sits at the end of the chain with no amp section after it, which means [high resonance with self-oscillation can sustain after note-off](https://www.musicradar.com/how-to/the-definitive-guide-on-how-to-use-operator-in-ableton-live) — useful for percussive plucks, problematic for held notes. Global section includes Voices (mono = 1, poly up to 32), Glide, Time/Tone (overall envelope scaling), Volume, and Spread (unison detune for thickening).

## Operator patch-design starting points

**FM Bass:** D (Coarse 1, modulator) → A (Coarse 1, carrier, Sine). D Level ~50%, A Decay short, Filter LP at 200 Hz. Push D Level higher for more growl, lower for cleaner sub. The genre archetype across UK bass music.

**E-piano (Rhodes-style):** Two-operator algorithm — D modulates A. A is Sine, D is Sine at Coarse 14 (or 7 for "softer" Rhodes). A envelope: fast attack, ~2-second decay, low sustain, medium release. D envelope: instant attack, ~0.5-second decay (this gives the tine "ping" that fades to the sustained tone). Velocity → Filter cutoff for touch sensitivity. Filter LP around 4 kHz.

**FM Bell / Mallet:** Inharmonic ratio for the modulator (D Coarse 3.5 or 5.6 modulating A Coarse 1). Short, percussive envelopes. Filter open. Add a second carrier at octave for body. The classic Yamaha DX7 "Tubular Bells" archetype.

**Pluck:** Additive algorithm (all four carriers parallel). Quick AD envelope on all four, slightly different decays. Coarse ratios 1, 2, 4, 8 (octaves) for a clean harmonic series. Filter LP with envelope-driven cutoff for an "open then close" character. Velocity → Filter cutoff.

**Pad:** Additive or two-pair algorithm. Slow attack, long sustain, long release. Multiple operators detuned slightly (Fine values +5, +15, -10, -20) for chorus-like movement. Filter LP around 3 kHz with slow LFO modulation. Voices = 8, Spread = 30% for unison thickness.

## Analog's architecture

[Analog](https://www.soundonsound.com/techniques/analog) is a virtual-analog subtractive synth with two oscillators (OSC1, OSC2), a noise source, two multi-mode resonant filters (F1, F2), two amplifiers (A1, A2), two LFOs, and per-section envelopes. The defining feature is its **routing flexibility**: each oscillator feeds the filter section via an **F1/F2 balance slider** (top = all to Filter 1, bottom = all to Filter 2, center = split). Filter 1's output always feeds Amp 1, Filter 2's into Amp 2 — but the **Series/Parallel** switch in the filter section can also send a percentage of Filter 1's output into Filter 2's input, enabling cascade filtering for sharper rolloffs or stacked filter character. The two output paths sum to stereo at the end. Oscillators offer Sync (Osc2 hard-syncs to Osc1) and FM (Osc1 frequency-modulates Osc2). Filter types are lowpass, highpass, bandpass, and notch in either 12 dB or 24 dB slope.

## Analog patch-design starting points

**Bass:** OSC1 saw at base pitch, OSC2 saw or square at -1 octave (Coarse -12). F1/F2 set to F1 only. Filter 1: LP 24 dB, cutoff ~300 Hz, resonance ~40%. Amp envelope: instant attack, ~0.5s decay, 0% sustain, 0.2s release. Glide at ~50 ms for portamento bass lines. Add slight noise (Noise level ~10%) for analog-style hiss-and-pop attack.

**Lead:** OSC1 saw, OSC2 saw detuned by Fine ~+15 cents for analog drift. F1/F2 split center, **Parallel** routing. Both filters LP 24 dB at ~1.5 kHz. Resonance ~50% on F1. LFO1 → Filter 1 cutoff at ~4 Hz, depth ~15%, for natural movement. Amp envelope: fast attack, full sustain, short release. Mono mode with Glide 30 ms for expressive lead playing.

**Pad:** OSC1 saw, OSC2 triangle one octave up. F1/F2 center, Parallel. F1: LP 24 dB at 2 kHz, resonance 25%. F2: HP 12 dB at 200 Hz to clear sub. Long attack (~1.5s), long sustain, long release (~3s). LFO1 → Filter 1 cutoff slow (0.5 Hz). LFO2 → Osc2 pitch ±5 cents for subtle chorus. Voices 8.

**Pluck:** OSC1 square, OSC2 off. F1: LP 24 dB, cutoff modulated by F1 envelope (envelope amount ~80%). F1 envelope: instant attack, 200 ms decay, 0% sustain. Amp envelope mirrors — fast attack, fast decay, no sustain. Velocity → F1 envelope depth. Result: a percussive "synth pluck" with cutoff sweep at every note attack.

## When Operator vs. Analog vs. Wavetable

A working rule:

- **Operator** when you want generated harmonic complexity from sine-based modulation — FM bells, e-pianos, FM bass, glassy textures, inharmonic mallet sounds, additive synthesis. The cheapest CPU-per-voice of the stock synths.
- **Analog** when you want classic subtractive analog character — fat saws, warm leads, hardware-style bass, slow-evolving pads driven by filter movement. The most "vintage" sound of the stock synths.
- **Wavetable** when you want morphing timbres, scan-position modulation, or modern bass/EDM sound design with MPE expressivity.
- **Drift** when you want a quick, lightweight subtractive patch that sounds modern-analog (its "Drift" instability is what gives it character) — Live 11.3+, included in Live 12 standard.
- **Meld** when you want bi-timbral macro-driven sound design with MPE — Live 12 Suite only.

For deeper FM technique, the [Gordon Reid *Synth Secrets* series](https://www.soundonsound.com/series/synth-secrets-sound-sound) remains the gold-standard secondary source — its FM articles explain the math behind ratios, sidebands, and modulator-carrier topologies in a way Live's manual does not. For starting-point subtractive patches across many sounds, [Welsh's *Synthesizer Cookbook*](https://synthesizer-cookbook.com/) provides 102 universal patches that translate directly to Analog. ARLO files for deep FM sound-design technique are in `corpus/daw/ableton/timeless/operator-fm-sound-design-fundamentals.md` (planned).

## Cited Retrieval Topics

- "how do i use operator in ableton for fm bass"
- "what are the 11 algorithms in ableton operator"
- "ableton analog synth patches for bass and pad"
- "how to make an electric piano with operator"
- "operator vs analog vs wavetable when to use which"
- "what filter types does operator have"
- "ableton operator bell sound recipe"
- "analog synth lead patch ableton"
- "operator additive synthesis"
- "what's the difference between drift and analog in ableton"

## Sources

- [Live Instrument Reference — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/live-instrument-reference/)
- [MusicRadar — The definitive guide on how to use Operator in Ableton Live](https://www.musicradar.com/how-to/the-definitive-guide-on-how-to-use-operator-in-ableton-live)
- [Sound on Sound — Ableton: Smooth Operator](https://www.soundonsound.com/techniques/ableton-smooth-operator)
- [Sound on Sound — A Is For Analog](https://www.soundonsound.com/techniques/analog)
- [Sound on Sound — Synth Secrets series (Gordon Reid)](https://www.soundonsound.com/series/synth-secrets-sound-sound)
- [Studio Brootle — Ableton Operator Tutorial](https://www.studiobrootle.com/ableton-operator-tutorial/)
- [PerforModule — Ableton's Auto Filter: Comparing Circuit Models](https://performodule.com/2019/03/07/abletons-auto-filter-comparing-circuit-models/)
- [Welsh's Synthesizer Cookbook](https://synthesizer-cookbook.com/)
- [Ableton Pack — Operator](https://www.ableton.com/en/packs/operator/)

See also: `corpus/synthesis/subtractive-synthesis-fundamentals.md`, `corpus/synthesis/fm-and-wavetable-synthesis.md`, `corpus/synthesis/patch-design-vocabulary.md`, `corpus/daw/ableton/devices/wavetable-drift-meld-synths.md`, `corpus/daw/ableton/timeless/operator-fm-sound-design-fundamentals.md` (planned)
