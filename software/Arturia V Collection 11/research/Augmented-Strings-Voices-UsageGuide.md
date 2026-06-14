# Augmented STRINGS / VOICES — Usage Guide

The Augmented instruments are Arturia's hybrid **two-layer (sample + synth) morphing texture
engines**. STRINGS builds evolving string **walls**; VOICES builds choir/vocal-texture walls
(built for "percussive and sustained textures, **not words**"). For this rig they're fast
evolving-pad sources — but they are the **worst CPU offenders in V Collection**, so the workflow
is: build the wall, **freeze/bounce immediately**, then degrade and play over the printed audio.

---

## 1. Architecture (STRINGS and VOICES are identical)

- **4 Engines** = **2 Layers (A/B) × 2 Engines each.** Each engine is a **Sampler** or a **Synth**
  (Analog / Granular / Harmonic / Simpler / Wavetable), with its own VCA/env/filter.
- **Mod:** 2 LFOs + 2 Functions + 2 Randoms + envelopes. **8 macros:** Color / Time / Motion /
  **Morph** + FX A / FX B / Delay / Reverb. Arp; Super Unison.
- **FX:** 2 per layer (14 available) + global 3 delays / 2 reverbs.
[links/augmented-manual-architecture-morph-modes.md; transcripts/augmented-strings-arturia-walkthrough-p2.md]

---

## 2. Essential workflow — the evolving wall

- **Layer A** = sustained ensemble — string section (STRINGS) or "Ah/Oo" choir with pitch
  **Drift** (VOICES). **Layer B** = a synth engine: **granular** (glitch/shimmer), **wavetable**
  (motion), **harmonic/additive** (glassy air).
- **3 Morph Modes:** **Crossover** (equal-power A→B), **Additive** (A stays, B blooms on top → a
  swelling wall), **Custom** (per-part min/max + curves — the acoustic recedes as the synth
  blooms). **Additive/Custom are the wall-builders.**
- **Never-repeat motion:** assign a slow **LFO + Function (unsynced)** to **Morph** + a filter;
  put the **Motion** macro on their *rates*, **Time** on attack/release, **Color** on engine/
  filter → the wall evolves without looping.
[links/augmented-manual-architecture-morph-modes.md; links/augmented-ambient-use-cpu-freeze-reviews.md]

---

## 3. Rig recipes

- **Wall → degrade:** hold a low cluster, long attack/release, generous global reverb+delay →
  **freeze/bounce immediately** → degrade through **Valhalla / EchoBoy / Decapitator / RC-20 /
  SketchCassette** → play banjo/baritone leads over the printed wall.
- **VOICES choir:** use multi-syllable morphing samples (Ah-Eh-Ah, Glo-Roh-Doh) + eerie pitch
  **Drift** for a built-in evolving choir under the banjo. [links/augmented-ambient-use-cpu-freeze-reviews.md]

---

## 4. Notable users & techniques
No named shoegaze/doom artist documented for either instrument; relevance is purely by technique
(they're modern preset-forward texture engines aimed at film/ambient/pop scoring).

## 5. Pitfalls / gotchas
- **CPU: the worst offenders in V Collection** — "brought a 2019 MacBook Pro to a crawl."
  Mitigate: **freeze/bounce washes early**, lower the **Polyphony** pop-up, raise the buffer,
  don't stack live instances. The CPU meter (bottom-left) doubles as a PANIC button.
- **Macro-first design** — limited deep per-parameter editing; some call it "a bunch of presets."
  Fine here (it's a texture source, not a deep-edit synth).
[links/augmented-ambient-use-cpu-freeze-reviews.md]

## 6. Captured sources & QC
- Transcript: `augmented-strings-arturia-walkthrough-p2` (official Advanced-panel walkthrough — architecture identical for VOICES)
- Links: `augmented-manual-architecture-morph-modes` (authoritative — engines + the 3 Morph Modes + VOICES content + CPU), `augmented-ambient-use-cpu-freeze-reviews`.

**QC:** architecture/Morph-modes from the **official Augmented Series manual** (high confidence).
CPU/freeze + ambient technique synthesized from Engadget/KVR/Sweetwater. No artist credit
(technique-based). Covers STRINGS + VOICES together (shared engine); the other Augmented titles
(BRASS/WOODWINDS/GRAND PIANO/MALLETS/YANGTZE) share the architecture — see the navigator.

## Sources
See §6. Originals: youtube.com (Arturia official), dl.arturia.net Augmented manual,
engadget.com / kvraudio.com / sweetwater.com. URLs on line 1.
