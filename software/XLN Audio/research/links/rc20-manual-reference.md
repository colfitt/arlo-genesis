https://support.xlnaudio.com/hc/en-us/articles/6843806759325-RC-20-Retro-Color-Manual
XLN Audio Support · RC-20 Retro Color Manual (March 18, 2020) · authoritative parameter reference
(also mirrored: https://www.sweetwater.com/sweetcare/articles/rc-20-retro-color-plug-in-quickstart-guide/ — Sweetwater Quickstart Guide)

Distilled from XLN's official manual + Sweetwater quickstart (both 403 to direct fetch; content corroborated across Sweetwater, MusicRadar, Tape Op, and the XNB/Splice transcripts).

## The 3 UI sections
1. **Top** — preset browser + the global **Magnitude** slider.
2. **FX Modules** — the 6 modules, each with one big AMOUNT knob (0% = bypassed; per-module on/off button) + a **Flux** slider + module-specific sub-params.
3. **Master** — Input gain, EQ, Tone, Width, Output gain.

## Magnitude (the master)
"The Magnitude slider controls the amount of the features (FX Modules + the Master sections) all at once. Think of it as the global Dry/Wet of the plug-in." It scales the six amount knobs AND the master-section controls from 0–100% of their set values, macro-style. = the "how much lo-fi" master and the prime automation target. NOTE: Magnitude is NOT a module — the 6th module is **Magnetic**. (Many web sources confuse the two.)

## Signal flow — FIXED ORDER (cannot be reordered)
Noise → Wobble → Distort → Digital → Space → Magnetic. Users cannot rearrange; the one exception: **Noise has a routing option to sit at the very END (post-Master-EQ)** so its output stays unprocessed by the rest of the chain and the EQ (confirmed in the manual, Sweetwater, and the XNB transcript). (One 3rd-party review, superherosamples, wrongly says order is fully fixed with no exception — the manual's Noise-routing option overrides that.)

## The 6 modules + sub-params
- **Noise** (noise generator) — ~16 noise TYPES: vinyl crackle, tape hiss, ambient/studio noise, electric circuit hum, stompbox static, VHS, DC/transformer, "JP8"-style synth white noise, Big Muff noise, etc. Sub: **Tone** (frequency balance of the noise — right = high-end crackle, left = low-mid crackle), **Follow** (envelope follower — noise rides the input and decays with it), **Duck** (inverse/compressor — noise gets out of the way of the input; great on drums), routing **post-Master** option, **Flux**.
- **Wobble** (wow & flutter — PITCH modulation) — **Wow↔Flutter** slider (Wow = slow pitch mod ~0.1–4 Hz; Flutter = fast, up to ~600 Hz), **Rate**, **Stereo** (separates wow/flutter to L/R → chorus-like), **Mix** (dry/wet — at ~50% + Stereo gives a chorus effect), **Flux**.
- **Distort** (saturation/distortion) — **6 distortion TYPES** (valve/tube, transformer, broken speaker, + waveshapers), **Focus filter** (band-target the distortion), **Mix** (parallel), **Flux**.
- **Digital** (degrader/bitcrusher) — **Rate↔Bits** slider (sample-rate reduction vs bit-depth reduction), **Smooth** (softens harsh artifacts), **Focus** filter with a **Cut** option (Cut removes freqs outside the range; Focus crushes inside the range, passes the rest), **Mix**, **Flux**.
- **Space** (reverb/resonator) — **Decay** (tail length), **Pre-delay**, **Stereo** (on by default), **Focus** (which freqs get reverb / damping), **Flux**. (Widely judged the weakest module — fine blended, not a flagship reverb.)
- **Magnetic** (tape wear — VOLUME modulation, NOT pitch) — **Wear↔Flutter** knob (Wear = slow volume fluctuation from tape wear; Flutter = faster volume artifact from the tape mechanism's pinch), **Rate** of the flutter (6–30 Hz), **Dropouts** (extreme, more-random volume drops — "needle skipping"), **Stereo** (mono/stereo independent), **Flux**.

## Flux engine
Per-module slider; from the manual: "adds all kinds of organic and non-linear fluctuations under the hood, customized specifically for each module." NOT a dry/wet — it controls hidden parameters for analog-style unpredictability (random overdrive mod on Distort, pre-delay mod on Space, random volume/dropouts elsewhere).

## Master section
Input gain (drive harder = more saturation reaction) · EQ: low-cut shelves (one plain, one with a resonant low bump) + high-cut (soft / steeper) · **Tone** (two modes: high-shelf, or a narrower mid tilt) · **Width** (stereo widener; scaled by Magnitude) · Output gain. EQ is POST — it shapes everything coming out of the modules unless Noise is routed post-EQ. The default low/high-cut filtering keeps it from getting harsh even at extreme settings. NO auto-gain compensation (intentional, per Tape Op).

## Presets / dice
Factory presets categorized for drums, keys, guitars, bass, full mixes, post-production, plus cassette/noise/digital/space/vinyl banks. The "dice"/random in RC-20 = a randomized NAME generator when saving a user preset (not a full patch-randomizer). The per-module Flux is the closest thing to randomized sound-generation. Large 3rd-party preset economy (ADSR, Adieu, LoFi Weekly, ProducerGrind packs). Formats: VST/VST3/AU/AAX; online-only installer.
