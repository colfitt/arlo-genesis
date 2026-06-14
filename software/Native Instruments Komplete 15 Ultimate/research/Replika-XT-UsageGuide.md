# Replika XT — Usage Guide

Replika XT is NI's 5-mode delay — and for this rig the **Diffusion mode** (delay-into-reverb-wash)
is the headline: it smears banjo/baritone/synths into a cloud that hands off into RAUM for infinite
sustain. Self-oscillating feedback builds walls; FX-in-the-feedback-loop makes shimmer and seasick
inharmonic drifts in the box.

> **⚠️ NOT CURRENTLY INSTALLED.** Replika XT is **not on disk** (not in CONTENTS.md / Components).
> It's **included in Komplete 15 Ultimate** — install via **Native Access**. (Note: the *free*
> **Replika** is a different, older single-mode plugin; **XT** = 5 styles + 7 FX + dual engine, and
> is Komplete-only.) Treat this guide as "install it, then do this."

---

## 1. The 5 styles & the engine

- **Modern** (Saturation) · **Diffusion** (Amount / Size / Dense–Sparse / Movement — *the ambient
  one*) · **Vintage Digital** (Quality Hi/Med/Low/Crunch) · **Analogue** (BBD Type Clean/Warm/Dark/
  Grunge) · **Tape** (Tape Age / Wow & Flutter / Noise).
- **Engine:** Feedback (**100%+ self-oscillates**), up to **4000 ms**, **Ducking** (Sensitivity/
  Amount/Release), **Pattern** (Shuffle/Feel/Accent — *+CPU*), **Single / Dual Serial / Dual
  Parallel**.
- **Modulation (7 FX) + the Feedback-Loop toggle:** Filter / Freq Shifter / Pitch Shifter can sit
  **inside the feedback loop** → cascading shimmer / detune-per-repeat.
[links/replika-manual-styles.md; links/replika-manual-delay-engine.md; links/replika-manual-modulation-fx.md]

---

## 2. Signature settings (this rig)

- **Diffusion reverb-wash:** Diffusion, **Amount up** (delay→reverb), **Size large**, **Sparse** =
  granular / **Dense** = smeared, **Movement** for drift; a **short time (1/32)** reads as ambience,
  not echoes. "Wonderfully long, evocative spaces."
- **Self-oscillating wall:** **Feedback 100%+** (any style) → builds to self-oscillation; pair
  **Ducking** so it fades up in the gaps behind the source.
- **Shimmer delay (no shimmer-verb needed):** **Pitch Shifter +12 (Smooth)** with **Feedback-Loop
  ON** → each repeat climbs an octave = rising shimmer cloud.
- **Dub-doom decay:** **Analogue**, long Time, **BBD Type Dark/Grunge**, high Feedback (repeats
  darken/distort as they go) — or roll **Hi Cut** down per pass.
- **Inharmonic doom drift:** **Freq Shifter** (small Hz) in the feedback loop → each repeat detunes
  further → seasick wall.
- **Lo-fi tape slap:** **Tape**, short Time, **Wow & Flutter up**, Tape Age + Noise on.
[links/replika-musicradar-review.md; links/replika-soundbridge-complex-delay.md; links/replika-manual-modulation-fx.md]

---

## 3. Rig-specific recipes

- **The navigator chain:** **Replika XT (Diffusion) → RAUM (Cosmic+Feedback / or Freeze)** —
  Diffusion smears the banjo/baritone into a cloud, RAUM makes it infinite.
- **One-instance delay→wash:** **Dual Serial** (Tape A → Diffusion B) builds delay-into-reverb-wash
  in a single instance; **Dual Parallel** = a rhythmic tap + wash simultaneously.
- **Banjo pluck through a wash:** dial **Ducking** so the dry pluck punches through and echoes swell
  back in the gaps; **Feel = Lag** drags repeats behind the beat for slowcore slack.
- **Standalone FX rack:** with delay near-zero, the 7 effects run as a chorus/phaser/freq-shifter
  unit on drones.
- **Logic AU** when installed; no host gotchas surfaced.

## 4. Notable users & techniques
**Richard Devine** and **Funkstörung** ship factory preset banks (real, corroborated credits) —
"hyper-modulated echoes → subtle widening." Honest flag: **no individual preset names documented**
— the guidance is "browse those banks first." [links/replika-producerspot-overview-artists.md]

## 5. Pitfalls / gotchas
- **Feedback 100%+ truly self-oscillates** — runaway gain risk (no adaptive limiter, unlike RAUM);
  watch levels.
- **Pattern menu (+CPU)** — spawns extra delay lines in the background.
- **Not installed**; **not free** (the free Replika is the older single-mode version). Install XT
  via Native Access. **Lite** limits as secondary host.

## 6. Captured sources & QC
- Links: `replika-manual-styles`, `replika-manual-delay-engine`, `replika-manual-modulation-fx`,
  `replika-musicradar-review`, `replika-soundbridge-complex-delay`, `replika-producerspot-overview-artists`.
  Builds on the existing nav link `km-nav-replika-xt-delay`. (No transcript — the one candidate
  video had no captions; covered by the manual + tutorial + review.)

**QC:** styles/controls from NI's manual (primary) + MusicRadar + a tutorial. Devine/Funkstörung
artist credit is solid; per-patch detail is not published (inferred "browse the bank"). Rig-chain
placements inferred from the navigator idiom. **Install status: NOT on disk; in Komplete 15
Ultimate (Native Access).**

## Sources
See §6. Originals: native-instruments.com manual, musicradar.com, soundbridge.io, producerspot.com.
URLs on line 1 of each file.
