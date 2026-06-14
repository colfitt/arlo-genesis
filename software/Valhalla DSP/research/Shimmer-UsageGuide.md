# ValhallaShimmer — Usage Guide

ValhallaShimmer is the dedicated **pitch-shifted ethereal reverb** — pitch shifting inside the
feedback path so the tail climbs in octaves into a rising shimmer wall (the Eno/U2 "infinite
guitar" sound). For this rig it's the *real* shimmer the free Supermassive only fakes.

> **⚠️ NOT INSTALLED — paid Valhalla plugin ($50).** Only VintageVerb + Room are on disk. The
> **free Supermassive** (own guide) makes octave-shimmer walls at $0, and the rig's **H90** pedal
> already does real shimmer — so this is a "buy only if a literal rising-octave shimmer plugin
> becomes essential" wishlist guide (see the Valhalla navigator's buy-order verdict).

> **Control-model correction:** Shimmer has **ONE Shift control (−12…+12 semitones)** + a
> **Pitch-Mode selector** (Single / Dual / SingleReverse / DualReverse / Bypass) — *not* two
> separate "Shift1/Shift2" shifters. **Dual** = up *and* down from one Shift value; for a stacked
> chord you **cascade multiple instances** (the designer's own trick). [links/shimmer-controls-official.md]

---

## 1. Essential workflow (dial from zero)

Everything down, then bring up in order: **Feedback** (intensity/decay) → **Size** (= the
time/length) → **Diffusion** (echo→smooth wash). **Shift is in semitones and compounds through the
feedback path** (+12 climbs an octave *per repeat*). Shimmer is a **diffusion-based reverb** — the
smoothness comes from the diffusor, not a delay-line algorithm like Room. [transcripts/shimmer-deepdive-controls.md; links/shimmer-envelope-and-cascade-official.md]

**No predelay knob — Diffusion is the attack shaper:** **0.5–0.618 = slow fade-in / reverse-reverb
swell**; **~0.9 = fast attack / dense wash**. Drop to ~0.6 to keep a played source legible before
the wall blooms. [links/shimmer-diffusion-as-predelay-official.md]

---

## 2. Signature settings

- **Max octave-shimmer wall:** Big/Medium Stereo · **Single** (or **SingleReverse** for a glassy,
  organ-smooth tail) · **Shift +12** · **Feedback 0.5–0.7** · **Diffusion ~0.9** · Size large ·
  **Color Dark** (kills pitch-shifter aliasing — *this is why Dark exists*) · Mod low · 100% wet on
  a return. **Feedback 0.8+ ≈ near-frozen.** [transcripts/shimmer-deepdive-controls.md; links/shimmer-tips-shimmering-official.md]
- **Tasteful ambient pad (Thales):** Feedback **<50%**, Diffusion **~60%**, **Mix 20–30%** on a send. [links/shimmer-thalesmatos-ambient-recipe.md]
- **Descending/doom wall:** **Shift −12.** **Dual** = +12 AND −12 at once (octave-stacked / organ).
- **Symphonic shimmer chord:** **cascade 3–4 instances** at **±12 / ±7 / ±5** (designer's trick;
  CPU is near-zero). [links/shimmer-envelope-and-cascade-official.md]

---

## 3. Rig-specific recipes

- **Banjo/baritone:** send **20–30%**, **Diffusion ~0.6** so the picked attack stays clear and the
  octave wall blooms behind it.
- **Saturated shoegaze/doom shimmer wall:** 100% wet on an aux → **saturate the return**
  (Decapitator / SketchCassette II / RC-20), **low-cut first**.
- **vs the free Supermassive:** Supermassive/CloudSeed make octave-shimmer walls at $0; Shimmer's
  edge is dedicated **pitch-in-feedback**, the cleaner **Reverse** modes, the **cascade-chord**
  trick, and near-zero CPU for stacking. Buy only as a daily recallable workhorse. Designer Sean
  Costello: "never intended to make real reverbs." [links/shimmer-vs-supermassive-best-for-ambient.md]
- **Logic AU:** run a **stereo source + stereo aux** when 100% wet on a send (mono-on-wet pan
  caveat, inferred from the documented Room AU behavior).

---

## 4. Notable users & techniques
**U2** "With or Without You" (the "infinite guitar"), "4th of July"; **Eno / Lanois** pre-*The
Unforgettable Fire* (1984) — HIGH confidence (the designer's own analysis of the technique
ValhallaShimmer recreates). Coldplay = Valhalla-listed (MEDIUM). **Honest flag: no sourced
drone/doom/shoegaze artist on Shimmer-the-plugin** — the *technique* is everywhere in that scene,
but plugin credits aren't documented. [links/shimmer-eno-lanois-history-artists.md]

## 5. Pitfalls / gotchas
- **Feedback runaway** at ≥~0.7 + high Diffusion → gate/limit the return (users rhythm-gate the wet).
- **Aliasing on the +12 climb** → Color **Dark** + High Cut.
- **Not a realistic reverb** (by design). **NOT installed / paid.** Logic AU fine; Live Lite hosts
  AU/VST (cap = device count, not CPU).

## 6. Captured sources & QC
- Transcripts: `shimmer-deepdive-controls`, `shimmer-beginners-cinematic`.
- Links: `shimmer-controls-official`, `shimmer-tips-shimmering-official`, `shimmer-envelope-and-cascade-official`,
  `shimmer-diffusion-as-predelay-official`, `shimmer-kvr-how-do-you-use`, `shimmer-vs-supermassive-best-for-ambient`,
  `shimmer-thalesmatos-ambient-recipe`, `shimmer-eno-lanois-history-artists`, `shimmer-rig-recipes-gotchas`.

**QC:** controls/modes/Diffusion-as-predelay + the Eno/U2 history from official Valhalla blog posts
(high confidence; the **Shift1/Shift2 → one-Shift+Pitch-Mode correction** is from the official
control list). Thales numbers + the KVR vs-free thread were ECONNREFUSED/snippet-distilled
(labeled). Copyable values synthesized from official ranges + walkthroughs. Logic-AU mono note
inferred. **Install status: NOT on disk; $50 paid.**

## Sources
See §6. Originals: valhalladsp.com blog + product page, youtube.com, kvraudio.com, thalesmatos.com.
URLs on line 1 of each file.
