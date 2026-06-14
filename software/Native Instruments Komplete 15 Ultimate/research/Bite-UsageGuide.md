# Bite — Usage Guide

Bite is NI's anti-aliased **bitcrusher / sample-rate reducer** — and the one NI degrade effect
**confirmed installed on disk** (the Crush/Mod packs and RAUM/Replika XT are in the bundle but
not installed — see those guides). For this rig it's the in-the-box "tape-disintegrate /
old-sampler" tool: the headline move is automating the sample-rate down under a held drone for a
progressive collapse, with the Post filter rolling the harsh top into warmth. It's also a **free
standalone NI plugin**, so its presets/patches are widely shareable.

---

## 1. Layout & controls

- **Left = resampler:** **Freq** (sample rate, 0.1 → 44.1 kHz), **Jitter** (clock instability →
  "broken tape," per-channel so it adds stereo width), **Pre / Post filters**.
- **Right = bit section:** **Bits** (2–16), **Crunch** (smooth, stepless, zipper-free
  bit-resolution — the automatable lo-fi knob), **DC Mode** (sustain-buzz vs fade-to-silence),
  **Dither**, **Expand** (cleans up the quiet tail), **Saturation**.
- **Mix** = equal-power dry/wet (parallel-friendly).
[links/bite-manual-controls.md; transcripts/bite-ni-official-walkthrough.md]

**Key behavior:** the **Pre/Post filters track the resampling frequency**, and their **MIDDLE
position = "authentic vintage sampler" tuning**. Only open them past tracking when you *want* the
harsh aliasing top. Aliasing IS the grit — use the **Post filter** to keep it warm, not fizzy.
[transcripts/bite-ni-official-walkthrough.md]

---

## 2. Signature settings

- **★ Tape-disintegrate (the headline):** automate **Freq 44.1 kHz → ~300 Hz** under a held
  drone = progressive collapse; roll the harsh top off with the **Post filter** so grit reads as
  warmth. [links/bite-recipes-ranges-triangulated.md]
- **Lo-fi warmth:** **Jitter up + Saturation ~6 dB**, filters middle-tracked.
- **Lo-fi drums:** **Freq ~12 kHz**, filters ~22.1 kHz.
- **Max noise / destroyed:** **6-bit**.
- **Sub/bass grit (dubstep-style):** Freq **~1.47 kHz**.
- **Crunch** is the smooth automatable degrade — ride it for a stepless lo-fi sweep without
  zipper noise.
[links/bite-recipes-ranges-triangulated.md; links/bite-... ; transcripts/bite-ni-official-walkthrough.md]

---

## 3. Rig-specific recipes

- **In the degrade chain (Logic AU):** banjo/baritone/synth source → (widener) → **Bite**
  (Crunch + Post-filter warmth) → delay-wash → reverb. On sampled hardware (MPC/Kontakt
  one-shots): Bite stamps the "old-sampler" grit before chopping.
- **Tape-collapse drone:** held synth/Mellotron/Cells bed → Bite Freq-automation arc
  (44.1 kHz→300 Hz) → into a long reverb so the disintegration smears into the tail.
- **Chaos-tail inversion (breaks the usual order):** put **Bite *after* the reverb** on an aux —
  NI's own "distort a heavily-reverbed signal for a chaotic effect"; good for a collapsing wall.
  [links/bite-recipes-ranges-triangulated.md]
- **Parallel:** use **Mix** to blend crushed under dry so the lead keeps definition while the
  grit sits underneath.

---

## 4. Notable users & techniques
No drone/doom/shoegaze artist documented against Bite specifically — relevance is by technique
(it's a utility degrade tool). The aesthetic anchor is the rig's own "recorded-wrong" lo-fi
philosophy, shared with RC-20 / SketchCassette / Lossy.

## 5. Pitfalls / gotchas
- **Aliasing = the sound** — keep the Post filter engaged (and filters middle-tracked) so grit is
  warm, not fizzy. [transcripts/bite-ni-official-walkthrough.md]
- Don't crush every layer — degrade one wall element, keep the lead/sub clean (general NI
  distortion guidance).
- **Logic AU** confirmed (Bite.component on disk). **Ableton Lite:** plugin/track limits apply if
  used as the secondary host.
- Overlaps **RC-20 Digital / SketchCassette** for sample-rate crush — pick one per layer; don't
  double the same artifact.

## 6. Captured sources & QC
- Transcript: `bite-ni-official-walkthrough` (control-by-control — reveals DC Mode, Expand, Saturation, filter-tracking).
- Links: `bite-manual-controls`, `bite-recipes-ranges-triangulated` (builds on the existing nav link `km-nav-bite-bitcrushing-blog`).

**QC:** controls/ranges from NI's manual + official walkthrough (primary); Bite ranges
(0.1 Hz–44.1 kHz, 2–16 bit) corroborated by two sources. The specific recipe values are
triangulated from NI blog + the bitcrushing blog; the rig-chain placements are inferred from the
navigator chain idiom. **Install status: Bite is the one NI degrade effect confirmed on disk.**

## Sources
See §6. Originals: youtube.com (NI official), native-instruments.com manual/blog. URLs on line 1.
