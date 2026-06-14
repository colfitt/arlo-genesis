# ValhallaDelay — Usage Guide

ValhallaDelay is Valhalla's character delay — tape/BBD/digital flavors, a **Diffusion** engine that
turns the delay into a reverb without dangerous feedback, plus **Ghost** (spectral drift) and
**Pitch/RevPitch** (shimmer-delay) modes. For this rig it's a tape/ghost wall-maker and a degrader
in its own right — though **EchoBoy already owns the rig's main delay slot**.

> **⚠️ NOT INSTALLED — paid Valhalla plugin ($50).** Only VintageVerb + Room are on disk. For
> *pure infinite walls* the **free Supermassive** is enough; ValhallaDelay earns its $50 only for
> authentic tape/BBD/Digital character, tempo sync, Ghost drift, RevPitch, and Pitch-Duck adaptive
> shimmer — features EchoBoy/Supermassive don't all cover (see the Valhalla navigator).

---

## 1. The three layers

- **MODE** = the base algorithm/flavor: **Tape / HiFi / BBD / Digital / Ghost / Pitch / RevPitch.**
- **ERA** = sub-variations within a mode.
- **STYLE** = routing: **Single / Dual / Ratio / PingPong / Quad.**
[links/vdelay-mode-control-official.md; links/vdelay-style-and-controls-official.md]

**Diffusion = the killer feature:** Amount **0% off · 68% balanced reverb · 91% = a pure diffusion
reverb that doesn't need Feedback for its decay**; **Size** small blurs the attack (still a delay),
large = full reverb. This makes a delay→reverb wash *without* runaway feedback. **Feedback**
self-oscillates ~100% and goes to **200%**; the EQ High/Low cuts sit **in the feedback path** so
repeats darken as they recirculate. [links/vdelay-diffusion-section-official.md; transcripts/vdelay-indepth-controls.md]

---

## 2. Signature settings

- **Tape-ghost wall:** Mode **Ghost** · **Diffusion 91% + large Size** · Feedback 40–70% · a small
  **FREQ Shift/Detune** for metallic enharmonic drift · feedback EQ low-cut ~150 Hz / high-cut
  ~3–4 kHz · 100% wet.
- **Octave shimmer-delay:** Mode **Pitch · Shift +12 · Feedback 0.5+** (spirals up; **−12** down) —
  the Shimmer effect on the delay engine.
- **Dirty self-oscillating tape drone:** Mode **Tape**, Feedback ~100–130%, **ride the DELAY time
  to "play" the howl**, Age + Wow/Flutter up.
- **Golden-ratio pseudo-reverb:** STYLE **Ratio 61.8%** + feedback + Diffusion.
- **Swell wall:** STYLE **Quad / SWELL** (sums all 4 taps into the feedback = building bloom).
- **Frippertronics:** up to **20 s** delay + high feedback + Tape = an evolving tape-loop drone.
[transcripts/vdelay-goodhertz-walkthrough.md; transcripts/vdelay-indepth-controls.md; links/vdelay-sos-musicradar-modes-review.md; links/vdelay-product-ambient-pitch-ghost.md]

---

## 3. Rig-specific recipes

- **Banjo/baritone adaptive shimmer:** **Pitch-Duck (+12 / +7) on a send** — the shimmer-delay
  ducks under your picking and blooms in the gaps (built-in, no external sidechain). [links/vdelay-pitch-duck-adaptive-shimmer.md]
- **As a degrader:** ValhallaDelay *is* one (Tape Age, BBD, Digital ≈12-bit) — use it as the
  tape/echo stage, or run a Ghost/Diffusion wash 100% wet and saturate the return.
- **Delay after reverb (the Tycho move):** re-throw the reverb tail into a bigger drifting wall; one
  instance can do reverb→delay internally via its own Diffusion.
- **vs EchoBoy/Supermassive:** EchoBoy owns the rig's character-delay slot; reach for ValhallaDelay
  specifically for **Ghost drift, RevPitch, Pitch-Duck, golden-ratio multitap, and the 91%-diffusion
  delay-reverb.** **Logic AU:** stereo source + stereo aux on a 100%-wet send.

---

## 4. Notable users & techniques
**Don Gunn (co-designer):** 10–12+ ValhallaDelay auxes per mix with heavy parameter automation for
evolving output — HIGH (Tape Op interview). **Honest flag: no ambient/doom artist sourced on
ValhallaDelay specifically.** [links/vdelay-tapeop-designer-interview.md]

## 5. Pitfalls / gotchas
- **Feedback runaway to 200%** — prefer **Diffusion 91% for the wash** instead of cranking feedback
  (safer).
- **No tap-tempo / no click-free tempo change** (the designer's own named limitation) — automate
  Sync at bar lines.
- **Modes gate controls** — Ducking / Wow / FREQ exist only in some modes.
- **NOT installed / $50 paid.** Logic AU native; Live Lite hosts fine (cap = device count); CPU
  near-zero.

## 6. Captured sources & QC
- Transcripts: `vdelay-goodhertz-walkthrough`, `vdelay-indepth-controls`.
- Links: `vdelay-mode-control-official`, `vdelay-style-and-controls-official`, `vdelay-diffusion-section-official`,
  `vdelay-pitch-duck-adaptive-shimmer`, `vdelay-product-ambient-pitch-ghost`, `vdelay-tapeop-designer-interview`,
  `vdelay-sos-musicradar-modes-review`, `vdelay-vs-supermassive-ambient`, `vdelay-rig-recipes-gotchas`.

**QC:** modes/Diffusion/controls + the golden-ratio 61.8% / Diff 68%-91% values from official
Valhalla blog + walkthroughs (high confidence). Plugin-Report vs-free + Gearspace 403'd →
snippet-distilled (labeled). Copyable rig values synthesized from official ranges. Logic-AU mono
note inferred. **Install status: NOT on disk; $50 paid; EchoBoy covers the main delay slot.**

## Sources
See §6. Originals: valhalladsp.com blog + product page, youtube.com (Goodhertz/Benedict Roff-Marsh),
tapeop.com, soundonsound.com. URLs on line 1 of each file.
