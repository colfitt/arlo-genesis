# Massive X — Usage Guide

NI's flagship wavetable synth — and a strong fit for the rig's **sustained evolving wall**
aesthetic. Its signature tools (**Performers**, the **noise→PM-AUX** texture trick, freely-
rerouted **feedback**) are exactly what make a pad *not* repeat. Honest caveat: dedicated
doom/drone Massive X tutorials are thin (most "Massive drone" content is the *older*
Massive), so the recipes below come from the pro lush-pad/routing builds + the manual — they
transfer cleanly.

## 1. Architecture — what makes it good at evolving textures

`research/links/km-massivex-edmprod-architecture-overview.md`, `research/links/km-massivex-manual-wavetable-modes.md`
- **2 wavetable oscillators**, each with a **Wavetable Position** knob + **10 modes**
  (Standard, Bend, Mirror, Hardsync, Wrap, Formant Capture, ART, Gorilla, **Random**,
  **Jitter**). **★ Modulating Wavetable Position with an LFO/envelope/Performer is the core
  evolving move** — the spectrum morphs continuously. Random/Jitter/Gorilla = inharmonic/
  glitchy grit; Formant Capture = vocal/organic; Bend = hollow.
- **2 PM oscillators + a PM-AUX bus** that accepts any source → cross-mod/feedback. **★ The
  texture trick: route a Noise oscillator into PM-AUX and modulate the main osc from Aux** →
  glassy/inharmonic timbres. `research/transcripts/km-massivex-soundkiller-routing-feedback-bass.md`
- **2 complex noise voices** ("work especially well on pads") — and you can **import a custom
  audio file as the noise source** (load a sampled banjo/field recording → drone from your own
  material).
- **9 filters** + **feedback**: in the Routing tab the filter feedback returns after the
  filter back into it → self-oscillating "piercing" drones. Feedback is the grit/drone engine.
- **Effects: 3 insert slots (A/B/C) + 3 stereo slots (X/Y/Z)** — inserts can host an **extra
  oscillator** (the "up to 7 oscillators" trick); stereo slots host Dimension Expander, Chorus,
  Delay, Wanderlust reverb.
- **Modulation: 3 Performers + 9 modulators + 4 Trackers + per-voice VR.** **Performers** are
  the signature — tempo-synced step-sequencer-modulators, Basic or Custom (up to 8 sections /
  polyrhythmic), 12 stored patterns switchable via Remote Octave. **★ Several Performers at
  unrelated rates / different bar lengths = effectively non-repeating motion.** Honest
  weakness: no visual feedback on slow mod, and LFOs aren't very customizable → **lean on
  Performers, not LFOs, for slow moves.** `research/links/km-massivex-manual-performers.md`
- **Voicing:** 2–6 voices, **Wide mode** (detune up to an octave → huge walls) + a **Chord
  Morph** knob (unison → chord voicings from one held note).

## 2. Evolving pad / drone technique

`research/transcripts/km-massivex-rishabh-lush-evolving-pad.md`
- **★ Stack THREE modulators on one target** — filter cutoff modulated by a slow **unipolar
  sine LFO** + a long-ADSR **Mod-Envelope** + a **2-bar Performer** → layered, never-aligned
  movement.
- **Modulate Wavetable Position on both oscillators** with separate slow modulators so each
  morphs independently.
- **Multiple Performers at different time signatures** (Custom editor, odd bar lengths) →
  polyrhythmic non-repeating evolution under a held note.
- **VR on pitch + resonance** so every note voicing differs slightly (keeps a sustained chord
  alive); **Unison Wide + detune** for the wall; **Chord Morph** for chords from one finger.
- **Feedback into the filter** and/or **noise→PM-AUX** for grit; **Gorilla/Random/Jitter** for
  degraded character.
- **Layer by duplicating the whole patch** with a *different wavetable* on the copy. `research/transcripts/km-massivex-4lienetic-ambient-pad-build.md`

## 3. Copyable patches (concrete)

- **Huge evolving pad** (Rishabh): OSC1+OSC2 Saw, detuned (down/up); amp env A~50%/R~50%; add
  white noise; **Blue Monark filter**, cutoff modded by (a) slow unipolar sine LFO, (b) long
  Mod-Env, (c) 2-bar Performer; a **3rd oscillator in an Insert slot** (bell wavetable, +1 oct,
  rewired in Routing) with square-LFO pitch ±12; **Wanderlust reverb → Chorus** at the end; VR
  on osc pitch + resonance. `research/transcripts/km-massivex-rishabh-lush-evolving-pad.md`
- **Textural/distorted bass wall** (SoundKiller): Voices Reset OFF; PM Triangle; Monark
  double-notch (LFO'd); Routing split — HP on A, OSC2 as a sine sub, **freq-shifter+crush on B
  (post-HP highs only)**, distortion on C; **filter feedback** for self-oscillation; X/Y/Z =
  Dimension Expander + Chorus + Delay. `research/transcripts/km-massivex-soundkiller-routing-feedback-bass.md`
- **Glassy/inharmonic texture:** Noise → PM-AUX, modulate main osc from Aux; **Random or
  Jitter** mode (J3 = sparse glitter) or **Formant Capture** on a vowel table; Position modded
  by a Performer.
- **Minimal "instant" pad:** ONE wavetable osc + **LFO on Wavetable Position** + **Wanderlust**
  reverb — the fastest usable start.

## 4. Rig-specific recipes (Logic AU)

- **Source for the banjo bed:** build the lush pad → out into **Valhalla → EchoBoy →
  Decapitator** (the AU runs native).
- **★ Resample/freeze:** run Massive X (Performer/Random-LFO driven) → record the evolving
  output to a fresh audio track to capture a one-of-a-kind drone, then chop/reverse/tape-
  degrade (pairs with the Octatrack/MPC/SketchCassette habit). `research/transcripts/km-massivex-clouds-ni-sketches-resample-workflow.md`
- **Custom-audio noise source:** load a sampled banjo/field recording as the noise oscillator.
- **Perform pad evolutions live** via Performer Remote-Octave snapshots from the 61SL MkIII.

## 5. Best learning resources

1. **Rishabh Rajan — "Massive X: Lush Pads (Advanced)"** — the most copyable evolving-pad
   build. ★
2. **SoundKiller — "Advanced Massive X: Bass Sound Design"** — the routing/feedback/aux
   walkthrough (architecture-in-practice).
3. **4lienetic — ambient pads** (duplicate-patch layering) + **NI "Sketches" (Clouds)**
   (resample workflow). Reference: the official **manual** (wavetable modes + Performers).

## 6. Pitfalls / gotchas

- **Effect order is locked unless you go into Routing** — the main friction; learn the Routing
  tab early.
- **LFOs are weak / no slow-mod visual feedback** → use Performers for slow evolution.
- **CPU** with high unison/oversampling → freeze the pad once committed.

## 7. Captured sources

**Transcripts (4)** — `research/transcripts/`: km-massivex-rishabh-lush-evolving-pad ·
km-massivex-soundkiller-routing-feedback-bass · km-massivex-4lienetic-ambient-pad-build ·
km-massivex-clouds-ni-sketches-resample-workflow.
**Links (6)** — `research/links/`: km-massivex-manual-wavetable-modes · km-massivex-manual-performers
· km-massivex-sleepfreaks-routing-voicing · km-massivex-edmprod-architecture-overview ·
km-massivex-ni-blog-sound-design-lab · km-massivex-ni-blog-getting-started-pads.

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/` (first line =
the original URL). Primary: Rishabh Rajan, SoundKiller, 4lienetic, NI manual + Sound-Design
Lab blog, Sleepfreaks, EDMProd. **Honesty flag:** no Massive-X doom/drone artist breakdown
exists (that genre lives in older Massive + Reaktor); the evolving-pad + routing techniques
cover the requested patches regardless.
