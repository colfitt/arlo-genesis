# Emulator II V / CMI V / Synclavier V — Usage Guide

Arturia's vintage **lo-fi samplers** — the "recorded-wrong" core of V Collection for this
rig. The killer move: **sample your own banjo/pedalboard/hardware into them and let the
8/12-bit converters + drift do the degrading.** Three flagships: **Emulator II V** (8-bit
DPCM grit), **CMI V** (Fairlight gritty resampling), **Synclavier V** (additive×FM, the
bundle's best long morphing-drone engine).

## 1. Emulator II V — 8-bit grit (sample your own gear)

`research/transcripts/vc-lofi-emulator-ii-v-demarzo-review.md`, `research/transcripts/vc-lofi-emulator-ii-v-catsynth-demo.md`
- **★ DAC Mode switch: Vintage vs Modern.** **Vintage = the 8-bit "Super-Nintendo" crunch**
  — the whole reason to use it. Leave it on Vintage.
- **8 voices/samples**; per-voice low-pass filter (keytracking), ADSR, LFO. The **chain-link
  icon** links a param across all voices — **unlink** to give one layer a slow swell while
  another hits instantly.
- **Sample your own gear in:** sample browser → **"Add Sample" / "Add Folder"** (WAV) → lands
  under **"User."** **★ Set the root note** for your own recordings or pitch-tracking is off.
- **Assign panel** = keyboard splits/layers + crossfade tapers; **3 global FX** incl. a
  **bit-crusher + downsampler**. **Offset trick:** same sample in multiple voices with slightly
  different filter offsets → a phasing pad. `research/links/vc-lofi-emulator-ii-v-import-samples.md`

## 2. CMI V — Fairlight gritty resampling

`research/transcripts/vc-lofi-cmi-v-ep2-sampling.md`, `research/links/vc-lofi-cmi-v-failedmuso-review.md`
- **No live sampling — import WAV** into any of 10 slots (folder icon per slot); also reads
  original **.VC** Fairlight files.
- **The lo-fi controls (Edit tab):** **Sample Rate** down from 44.1 kHz to ~2 kHz (classic
  ≈14 kHz); **Bit Depth** variable (classic = **8-bit**, usable down to ~6-bit, 1-bit = chaos).
  Right-click-drag for big sweeps — you watch the waveform degrade. There's baked-in converter
  grit even before you touch them. Plus per-slot HP/LP, Reverse, phase Invert,
  backwards-forwards loop.
- **Page R** sequencer (8×32, light-pen) + **Time/Spectral Synth** (FFT a sample → 32 harmonics
  → resynthesize/morph). Iconic presets: Orch5, Sararr.

## 3. Synclavier V — the long morphing-drone engine

`research/links/vc-lofi-synclavier-v-tapeop-evolving-pads.md`
- **12 partials**, each an additive carrier (≤24 harmonics) FM'd by another additive waveform.
- **★ Timbre Slices** (orig "Timbre Frames"): **sequence up to 50 snapshots** with **crossfades
  up to 30 s each, over up to 5 minutes** → the fast path to a **2–5 minute continuously
  morphing ambient/drone bed.** The headline drone feature in the whole bundle.

## 4. Copyable recipes (rig-specific)

- **★ Sample-your-own-gear → 8-bit:** record a banjo phrase / pedalboard drone in Logic → **EMU
  II V → "Add Sample" → DAC Mode = Vintage → set root note** → unlink a voice for a slow swell →
  bit-crusher FX. (Or import the same WAV into **CMI V**, drop **bit depth to 8 / sample rate to
  ~14 kHz** for Fairlight grit.)
- **Fairlight gritty texture bed:** CMI V, import a sustained tone, sample-start past the
  dropout, **6–8 bit / ~14 kHz**, backwards-forwards loop, aux reverb → drone bed under banjo.
- **Evolving drone bed:** Synclavier V Timbre Slices — 10–20 slices, 20–30 s crossfades → a
  3–5 min morphing pad under the banjo lead.

## 5. Also in this cluster (digital glass — see the Navigator for the rest)

- **DX7 V** — alien glassy FM. **Glass-pad recipe:** Op1 "Rounded Saw"; Op2 level 80, +1 oct,
  "Additive 3"; Bandpass ~2–3 kHz/res 20%; long release; **Mod Env 1 → Op1 Filter** for a gradual
  swell. Nail operator ratios first, then delay + reverb = ambient FM (Boards of Canada). `research/links/vc-lofi-dx7-v-fm-glass-recipes.md`
- **CZ V** — warmer/easier phase-distortion glass: fast subtle vibrato + slow DCW sweep →
  Delay/Chorus/Reverb. `research/links/vc-lofi-cz-v-phase-distortion-pads.md`

## 6. Best learning resources

1. **One Man And His Songs — "CMI V Ep.2: First Look at Sampling"** — the best lo-fi/sampling
   walkthrough (import, sample-rate/bit-depth degradation, FFT→wavetable). ★
2. **Emulator II V — Demo/Review (Dean DeMarzo)** + **CatSynth TV** (importing your own audio).
3. **Tape Op — Synclavier V** (Timbre Slices for evolving pads).

## 7. Pitfalls / gotchas

- **EMU II:** **set the root note** on imported samples (factory ones auto-map); keep DAC on
  **Vintage** for the grit. `research/transcripts/vc-lofi-emulator-ii-v-demarzo-review.md`
- **CMI V:** **no live sampling** — import WAV only; the lo-fi *is* the converter (low
  bit/rate), embrace it.
- **CPU:** Synclavier's long Timbre-Slice morphs + high partials are heavy → bounce the drone bed.

## 8. Captured sources

**Transcripts (4)** — `research/transcripts/`: vc-lofi-emulator-ii-v-demarzo-review ·
vc-lofi-emulator-ii-v-catsynth-demo · vc-lofi-cmi-v-ep1-intro · vc-lofi-cmi-v-ep2-sampling.
**Links (5)** — `research/links/`: vc-lofi-emulator-ii-v-import-samples · vc-lofi-cmi-v-failedmuso-review ·
vc-lofi-synclavier-v-tapeop-evolving-pads · vc-lofi-dx7-v-fm-glass-recipes · vc-lofi-cz-v-phase-distortion-pads.

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/` (first line =
the original URL). Primary: One Man And His Songs (CMI V series), Dean DeMarzo, CatSynth TV,
Tape Op, MusicRadar, Arturia sound-design pages. **Honesty flags:** no video captured for
Synclavier/DX7/CZ (covered via official pages + Tape Op/MusicRadar + community packs); some
Integraudio/Reverb pages 403'd (corroborated via snippets + Failed Muso/Tape Op).
