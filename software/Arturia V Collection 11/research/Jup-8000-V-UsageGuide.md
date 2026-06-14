# Jup-8000 V — Usage Guide

The Jup-8000 V is Arturia's Roland JP-8000 — home of the **SUPERSAW**, the detuned-saw wall
that built late-'90s trance and, pulled back, makes a gorgeous lush shoegaze/ambient pad. For
this rig it's the supersaw-wall source: sustained legato chords, modest detune, then degraded
through Decapitator/Valhalla. A free-running random phase per note means it never sounds
bit-identical — organic out of the box.

---

## 1. How the supersaw actually works (so you can tame it)

From the hardware reverse-engineering (applies directly — Arturia confirms the same architecture):
- **7 sawtooth oscillators.** **DETUNE is non-linear** — the lower third barely spreads the saws
  (the **pad/ambient region**); the upper travel spreads fast (trance/lead). 
- **MIX** raises the 6 side-saws as a parabola while the center saw drops linearly → **high Mix =
  widest/thickest**, low Mix = focused center pitch (keeps the root defined under a lead).
- **Phase is free-running random** per note → organic, never identical.
- Each saw has a **high-pass filter at its own fundamental** (anti-alias) → the supersaw is
  slightly thin at the bottom; add an octave-down saw for body.
[links/jup8000-szabo-supersaw-thesis.md; links/jup8000-shore-supersaw-trance-pads-thesis.md; transcripts/jup8000-nutrix-jp8000-owner-walkthrough.md]

**OSC 1 has 7 modes:** Supersaw · Triangle Mod (LFO the shape for movement) · **Feedback** (raise
feedback + sweep harmonics — the experimental/drone mode) · Noise · Square(PWM) · Saw · Triangle.
OSC 2 adds sync + PWM; **Ring / Cross-Mod (≈FM)** + a dedicated **AD pitch envelope** for
sync-sweeps and attack bite. [transcripts/jup8000-nutrix-jp8000-owner-walkthrough.md]

**FX rack:** 4 slots / 18 FX — **Trance Gate** (32-step, 5 env shapes), **Super Unison**,
Multi-Band Comp, **JUN-6 Chorus**, delay, phaser, reverb, bitcrush, tape. Modulation =
2 ADSR + 2 LFOs + Function gen + 4-layer Multi-Arp (the hardware's "Motion Control" is replaced
by parking an Advanced-panel Function/Random on any panel knob). [links/jup8000-arturia-spec-fx-modulation.md]

---

## 2. Signature settings

- **Ambient/shoegaze pad:** Supersaw · **Detune in the lower third** (lush, not trance-bright) ·
  **Mix moderate–high** for width · sustained **legato chords** · long amp release · add **OSC2
  saw an octave down** to counter the bottom-end thinning. [links/jup8000-shore-supersaw-trance-pads-thesis.md]
- **Evolving drift:** slow **Function on Detune** and/or triangle-mod shape → free-running phase +
  the modulator = compounding non-repetition.
- **Drone/harsh:** **Feedback** oscillator with harmonics swept, or Cross-Mod + pitch-env for
  FM-style grit, filter fully open.

---

## 3. Rig-specific recipes

- **Into the degrade chain:** supersaw wall → **Decapitator** (the slightly-thin supersaw won't
  mud up — a good Decap candidate) → **SketchCassette / RC-20** → **Valhalla VintageVerb/Room**
  (the trance-pad "EQ → big reverb" finish, reframed lo-fi).
- **Build a wall:** stacked legato chord on Supersaw + OSC2 octave-down; **Super Unison** FX slot
  for extra width; Trance Gate only if you want rhythmic chop.
- **Banjo/baritone over it:** ease **Mix** back so the center pitch stays defined under the lead,
  or let the supersaw be the bed below the banjo.
- **Logic AU / CPU:** 16 voices → freeze/bounce walls. **Single-timbral (no split/layer)** → load
  two instances for bass+lead splits.

---

## 4. Notable users & techniques
The supersaw **defined late-'90s/2000s trance** — that's the documented lineage. **Honest flag:
no ambient/shoegaze artist is tied to the JP-8000/Jup-8000 V specifically;** rig value is the
authentic, degradable wide pad, not the genre heritage. A real-hardware owner (Nu-Trix) calls
the emulation accurate. [transcripts/jup8000-nutrix-jp8000-owner-walkthrough.md; links/jup8000-soundgale-tuxaudio-reviews.md]

## 5. Pitfalls / gotchas
- **No split/layer** (single-timbral) → two instances.
- 16 voices = real CPU on thick supersaw chords → freeze.
- **Over-detuning measurably worsens** the iconic sound — for ambient, stay below stock.
- A constant phase offset between dual osc can cause cancellation on some patches.

## 6. Captured sources & QC
- Transcript: `jup8000-nutrix-jp8000-owner-walkthrough` (real-hardware owner — the authority source)
- Links: `jup8000-szabo-supersaw-thesis`, `jup8000-shore-supersaw-trance-pads-thesis`, `jup8000-arturia-spec-fx-modulation`, `jup8000-soundgale-tuxaudio-reviews` (builds on `vc-nav-jup8000-supersaw-walls`).

**QC:** the Szabo & Shore PDFs describe the **original JP-8000 hardware**, not the plugin — but
Arturia + SoundGale independently confirm the same "7 detuned saws" architecture, so detune/mix/
phase findings apply directly (PDFs extracted via pdftotext). **Tux Audio + Gearspace 403'd →
triangulated** (labeled). No ambient artist credit (technique-based).

## Sources
See §6. Originals: youtube.com (Nu-Trix), adamszabo.com, A. Shore thesis PDF, arturia.com,
soundgale.com. URLs on line 1.
