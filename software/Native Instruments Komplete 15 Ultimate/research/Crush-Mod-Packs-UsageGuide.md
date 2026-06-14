# Crush Pack & Mod Pack — Usage Guide

NI's two effect packs: **Crush Pack** = Bite + **Dirt** (wavefolding distortion) + **Freak**
(ring-mod / frequency-shift), and **Mod Pack** = **Phasis** (phaser) / **Choral** (chorus/widener)
/ **Flair** (tuned flanger). For this rig they're the degrade + modulate-into-a-wall stages ahead
of the delay/reverb. **Freak** (inharmonic drone-maker) and **Flair** (tuned-resonator chords) are
the standouts.

> **⚠️ MOSTLY NOT INSTALLED.** On disk, **only Bite is present** (its own guide). **Dirt, Freak,
> Phasis, Choral, and Flair are NOT on disk** (not in CONTENTS.md / Components). They're NI
> Effects-Series packs referenced in the navigator — **verify in Native Access whether they're
> covered by your Komplete 15 Ultimate license** (Bite's presence suggests the Crush Pack license
> exists; the others may just need installing, or may require purchase). Treat this guide as
> "confirm/install, then do this."

---

## CRUSH PACK

### Dirt — wavefolding distortion
- **Drive + Amount** (Amount: saturation in the first half, **wavefolding** in the second), per-
  stage **Modes I/II/III** (subtle / balanced-brightest / extreme-dark-crushed), **Tilt**, **Bias**
  (adds even harmonics — *the fix for thin/hollow wavefold*), **FX Trim** −18→+6 dB, **Routing**
  A>B / B>A / A+B, Safety off = more gain.
- **Recipes:** bass = circuit-A Drive ~40% + circuit-B ~20% + 50/50 Mix; drums 50/50; vocals/lead
  ~80/20. Reversing B→A genuinely changes the tone.
[links/crushmod-dirt-manual-controls.md; transcripts/crushmod-dirt-ni-walkthrough.md]

### Freak — ring mod / frequency shift (the jewel)
- **Type morph AMP → RING → FREQ** is the core gesture. Oscillator mode Freq = **±5000 Hz coarse /
  ±200 Hz fine**; Antifold; Stereo; Harmonics; **Feedback** (freq-shift+feedback = barber-pole /
  phasing → distortion). **Radio** mode = AM warble.
- **★ Drone weapon (no host routing):** **Sidechain mode with SC off + Contour 0% = self-modulation
  distortion**; or feed a **decaying sine into a pad as the sidechain** so the modulation breathes
  with an envelope. MusicRadar: "the jewel in the Crush Pack crown."
[links/crushmod-freak-manual-controls.md; transcripts/crushmod-freak-ni-walkthrough.md]

---

## MOD PACK

### Choral — chorus / widener
- **4 modes:** Synth (dark — bass/sub), **Ensemble** (lush at low/mid Amount, queasy detune at full
  — *the shoegaze widener*), Dimension (invisible "bigger"), Universal (clean). **Voices 1–3.**
- **★ Scatter** = reverb-like feedback routing without metallic ring; **Amount down + Scatter ON +
  long Delay = a soft ambient bloom.**
[links/crushmod-modpack-manual-controls.md; transcripts/crushmod-choral-ni-walkthrough.md]

### Flair — tuned/harmonic flanger
- **1–4 Voices** as comb filters; **Chord (24 settings) = a chord generator**; **Standard /
  Thru-Zero** (signal can vanish) **/ Scan** (arp-like).
- **★ Tuned-resonator wall:** near-zero modulation + **4 Voices + a Chord + high Feedback** → a
  chord rings out of *any* source; **Pitch** sets the root. Subtle widener: Rate low, Amount+Mix
  high, low feedback.
[links/crushmod-modpack-manual-controls.md; transcripts/crushmod-flair-ni-walkthrough.md]

### Phasis — phaser
- Rate / Center / Spread / **Notches (up to 12 pairs)** / Feedback / Amount / Mod Mix. **Many
  notches + high feedback = vocal/vowel** quality. **ULTRA (Rate → 477.3 kHz) on noise/a drone turns
  noise into a tone** (phaser-as-synth); sweep Rate down to morph FM→phasing as a long transition.
  Mod Mix toward Spread = cleaner.
[links/crushmod-modpack-manual-controls.md; transcripts/crushmod-phasis-ni-walkthrough.md]

---

## Rig-specific recipes (navigator degrade chain, Logic AU)

- **Banjo/baritone lead:** source → **Choral Ensemble (low Amount)** or **Flair Standard widener**
  → Bite → Replika XT (Diffusion) → RAUM.
- **Doom/drone wall:** sustained synth → **Flair tuned-resonator (Chord + high feedback, near-zero
  rate)** or **Freak freq-shift (fine ±200 Hz)** → **Dirt Mode III parallel ~50/50** (wavefold
  teeth) → RAUM Freeze.
- **Evolving inharmonic:** Massive/Reaktor pad → **Freak Sidechain** (decaying sine as SC, Contour
  follows envelope) → Bite Freq-sweep → RAUM Cosmic.
- **Chaos-tail inversion:** source → RAUM, then **Dirt/Freak AFTER the reverb** on an aux ("distort
  a heavily-reverbed signal") for a collapsing wall.
[links/crushmod-ni-distortion-blog-recipes.md]

## Notable users & techniques
No drone/doom/shoegaze artist documented against a specific one of these — the only named reference
is generic phaser lineage (**Tangerine Dream, Radiohead**) in NI's Phasis walkthrough. Relevance is
by technique.

## Pitfalls / gotchas
- **Install status (above):** only **Bite** verified on disk — confirm the rest in Native Access.
- **Dirt restraint:** "a little goes a long way — don't distort every element or it gets muddy";
  degrade one wall layer, not all.
- **Freak/ring-mod tuning:** inharmonic by nature — coarse ±5000 Hz is clangy/metallic; **fine
  ±200 Hz** is the usable slow drift under sustained material.
- **NKS:** MusicRadar notes Mod Pack is "at its best with NI controller hardware"; the 61SL MkIII
  still maps NKS parameter pages (no on-key light guide). **Logic AU** when installed; **Lite**
  limits as secondary host.

## Captured sources & QC
- Transcripts: `crushmod-dirt-ni-walkthrough`, `crushmod-freak-ni-walkthrough`, `crushmod-choral-ni-walkthrough`,
  `crushmod-flair-ni-walkthrough`, `crushmod-phasis-ni-walkthrough`, `crushmod-dirt-freak-kompletenow-session`.
- Links: `crushmod-dirt-manual-controls`, `crushmod-freak-manual-controls`, `crushmod-modpack-manual-controls`,
  `crushmod-synthanatomy-review`, `crushmod-musicradar-review`, `crushmod-modpack-musicradar-review`,
  `crushmod-ni-distortion-blog-recipes`. Builds on the existing nav links `km-nav-crush-pack-bite-dirt-freak`,
  `km-nav-mod-pack-phasis-choral-flair`.

**QC:** mode/control names + ranges from NI manuals + official walkthroughs (primary) + two
MusicRadar reviews + SynthAnatomy. Rig-chain recipes inferred from verified per-plugin behavior +
the navigator idiom. **Install status: only Bite confirmed on disk; Dirt/Freak/Phasis/Choral/Flair
absent — verify the license in Native Access.**

## Sources
See above. Originals: youtube.com (NI official walkthroughs), native-instruments.com manuals/blog,
musicradar.com, synthanatomy.com. URLs on line 1 of each captured file.
