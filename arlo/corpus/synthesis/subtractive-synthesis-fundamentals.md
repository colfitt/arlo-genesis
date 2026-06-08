# Subtractive Synthesis Fundamentals

**Scope:** synthesis
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Gordon Reid, *Synth Secrets* (Sound on Sound, 1999–2004); Fred Welsh, *Synthesizer Cookbook*; Ableton Learning Synths
**Tags:** `synthesis`, `subtractive`, `oscillator`, `filter`, `envelope`, `LFO`, `principle`

---

## The Oscillator → Filter → Amplifier Signal Path

Subtractive synthesis follows a fixed three-stage path: an oscillator generates a harmonically rich raw tone, a filter sculpts that tone by attenuating selected harmonics, and a voltage-controlled amplifier (VCA) shapes the resulting signal's loudness over time. Gordon Reid frames this as starting with a "buzz" and carving it into a musical sound — the opposite of additive synthesis, which builds up sound from sine partials ([Sound on Sound, "What's In A Sound?"](https://www.soundonsound.com/techniques/whats-sound)). Each stage is normally driven by its own control source: keyboard pitch tracks the oscillator, an envelope generator opens and closes the filter and amp, and an LFO can wobble any of them. This signal-then-control split is the architecture every classic mono-synth (Minimoog, SH-101, MS-20, Pro-One) and most software synths (Ableton Analog, u-he Diva, Arturia Mini V) inherit ([Ableton Learning Synths — Oscillators](https://learningsynths.ableton.com/)). Understanding the order matters: an oscillator change alters the raw harmonic budget, a filter change carves what survives, and an amp change governs only loudness. If you want a tone brighter you adjust the filter, not the oscillator level.

## Waveform Harmonic Content: Saw, Square, Triangle, Sine

The four classic oscillator shapes carry very different harmonic loads, and choosing one is the most consequential decision in a subtractive patch.

- **Sawtooth** contains every harmonic of the fundamental — both odd and even — with amplitudes falling at 1/n. This is the buzziest, most harmonically dense classical waveform and the standard starting point for strings, brass, supersaw leads, and aggressive basses ([WolfSound — Basic Waveforms](https://thewolfsound.com/sine-saw-square-triangle-pulse-basic-waveforms-in-synthesis/)).
- **Square** contains only odd harmonics (1st, 3rd, 5th, 7th...) at 1/n. The missing evens give it a hollow, woody character that suits clarinets, retro leads, and 8-bit chip basses ([Perfect Circuit — Synth Waveforms](https://www.perfectcircuit.com/signal/difference-between-waveforms)).
- **Triangle** also contains only odd harmonics, but amplitudes drop much faster (1/n²), giving a sound that is nearly sinusoidal but with a touch of edge — useful for soft basses, flutes, and sub-style leads.
- **Sine** contains only the fundamental, with no harmonics at all. It can't be filtered into anything else, so it's normally used for sub-bass layers or as an FM carrier ([WolfSound — Basic Waveforms](https://thewolfsound.com/sine-saw-square-triangle-pulse-basic-waveforms-in-synthesis/)).

Pulse waves are squares with adjustable width; narrower pulse widths emphasize higher odd harmonics and thin the sound out toward a nasal, reedy timbre, which is why pulse-width modulation (PWM) is a common pad and string technique.

## Filter Types: LP, HP, BP, Notch

A filter attenuates frequencies on one side of its cutoff. Subtractive synthesis lives almost entirely in the low-pass filter — the workhorse — but all four types have idiomatic uses.

- **Low-pass (LP)** passes lows and rolls off highs above cutoff. It is the default for "warming up" or "closing down" a bright oscillator. Slopes are usually 12 dB/oct (2-pole) or 24 dB/oct (4-pole) ([Perfect Circuit — Learning Synthesis: Filters](https://www.perfectcircuit.com/signal/learning-synthesis-filters)).
- **High-pass (HP)** passes highs and rolls off lows. Useful for thinning a bass into a pluck, or for keeping a pad from cluttering the low end.
- **Band-pass (BP)** passes a band around the cutoff and rolls off both sides. Good for vocal-formant approximations, telephone effects, and snare-like tunings.
- **Notch (band-reject)** removes a narrow band at the cutoff, leaving everything else. It's used more for resonant sweeps and phaser-style movement than for tonal shaping.

The Minimoog's 24 dB/oct ladder LP filter is the canonical example of an "East Coast" sculpting filter: aggressive, musical, and so identifiable that "Moog bass" still means "saw or square through a ladder filter at moderate resonance" ([Sound on Sound — Moog The Ladder](https://www.soundonsound.com/reviews/moog-ladder)).

## Cutoff, Resonance, and Self-Oscillation

Two knobs do most of the work in any synth filter: **cutoff** and **resonance**. Cutoff sets the frequency where the filter starts to attenuate. Resonance (also Q or emphasis) boosts a narrow band right at the cutoff, creating a peak that can be subtle (gentle character) or extreme (whistle, scream) ([Sound on Sound — Of Responses & Resonance](https://www.soundonsound.com/techniques/responses-resonance)).

At high enough resonance settings most analog-modeled filters will **self-oscillate** — the resonant peak grows until the filter rings at its cutoff frequency on its own, producing a near-pure sine wave even with no oscillator input. The Moog ladder and Korg MS-20 filters are famous for musical self-oscillation; some modern emulations let you key-track the self-oscillation so the filter itself becomes a playable sine voice ([Sound on Sound — Of Responses & Resonance](https://www.soundonsound.com/techniques/responses-resonance)). Practically, raising resonance also thins the sound below the cutoff (it eats low end as it boosts the peak), which is why bass patches typically use low resonance and lead/acid patches use high resonance.

## Envelope Generators: ADSR as Shape Vocabulary

The ADSR envelope is the standard time-varying control source. Each stage has a specific job:

- **Attack** — time from key-down to peak level. Short attack (0–10 ms) gives a percussive front; long attack (200 ms–several seconds) gives a swell ([Native Instruments — ADSR Explained](https://blog.native-instruments.com/adsr-explained/)).
- **Decay** — time to fall from peak down to the sustain level.
- **Sustain** — the level held as long as the key remains pressed. Note this is a *level*, not a time.
- **Release** — time to fall from sustain to silence after key-up.

Envelopes are usually routed to at least two destinations: the VCA (so the note has an amplitude shape) and the filter cutoff (so the tone evolves over time). On most synths, a separate envelope amount knob on the filter sets how much the envelope opens the cutoff — this is the source of the classic "wow" filter sweep on a Minimoog brass patch. More than two envelopes (e.g., DX7's eight-stage, Roland JP-8000's pitch envelope) become available on richer architectures, but the ADSR is the lingua franca ([Sound on Sound Synth Secrets Series](https://www.soundonsound.com/series/synth-secrets-sound-sound)).

## LFO Modulation Targets: Pitch, Filter, Amp, Pan

A low-frequency oscillator runs below the audible range (commonly 0.01–20 Hz) and is used as a control source, not heard directly ([Sweetwater — A Simple Guide to Modulation: LFO](https://www.sweetwater.com/insync/a-simple-guide-to-modulation-lfo/)). The four canonical destinations:

- **Pitch → vibrato.** A triangle or sine LFO at 4–6 Hz with small depth produces musical vibrato. Faster rates with deeper amounts produce trills or seasick wobble.
- **Filter cutoff → wobble/sweep.** Slow LFOs (under 1 Hz) on cutoff create the evolving filter movement that defines pads and acid lines; tempo-synced LFOs on filter are the foundation of dubstep wobble bass ([iZotope — Creative Ways to Use LFOs](https://www.izotope.com/en/learn/creative-ways-to-use-lfos-on-synths-and-beats.html)).
- **Amplitude → tremolo.** A sine LFO on the VCA gives the classic vibraphone/Rhodes amplitude pulsing.
- **Pan → auto-pan.** A slow LFO on pan spreads a sound dynamically across the stereo field — common on pads and arpeggios.

LFO depth and rate should usually be modest unless the wobble *is* the sound. Most natural-sounding modulations sit under ±10 cents of pitch, under 20 percent of filter range, or a few decibels of amp depth.

## Pluck Patches: Fast Attack, Fast Decay, Low Sustain

A pluck is an envelope-defined sound: attack near zero, decay short (a few hundred ms), sustain at or near zero, release short. The filter envelope follows the same shape with moderate envelope amount so the note opens bright and closes quickly. Welsh-style recipes typically use a single sawtooth or pulse oscillator, LP filter at mid-cutoff, modest resonance, and the same fast-decay shape on both filter and amp envelopes ([LANDR — ADSR Envelopes](https://blog.landr.com/adsr-envelopes-infographic/)). Plucks live in pop, house, and trance because they cut through without sustaining; they also work as melodic fills that don't compete with vocals.

## Bass Patches: One Saw or Square, Low Cutoff, Short Envelope

Classic monosynth bass uses one oscillator (saw or square), low-pass filter with cutoff at a medium-low setting, slight resonance for character, and an amp envelope with fast attack and a medium-short decay. The Minimoog bass sound is essentially this: oscillator 1 sawtooth, filter cutoff around the lower third of its range, envelope opening the filter slightly on each note for a percussive front ([Vintage Synth Explorer — Minimoog](https://www.vintagesynth.com/moog/minimoog); [Perfect Circuit — Vintage Moog Modular Filters](https://www.perfectcircuit.com/signal/vintage-moog-modular-filters)). Pulse-width-modulated square gives "P-funk" rubber bass; two slightly detuned saws give the "supersaw bass" of late-90s trance. Keep low-end resonance modest — high resonance thins the fundamental, which is the opposite of what bass needs.

## Pad Patches: Long Attack, Long Release, Slow Modulation

A pad reverses the pluck shape: long attack (500 ms to several seconds), high sustain, long release, slow filter sweep, and usually two or three detuned oscillators plus chorus. The filter is often opened most of the way with slow LFO movement on cutoff for evolving brightness. Pulse-width modulation on a square oscillator gives the "Polymoog pad" character. Stereo width comes from detuning two oscillators a few cents apart and panning them, or from chorus on the output ([EDMProd — ADSR Envelopes](https://www.edmprod.com/adsr-envelopes/)). Welsh's recipes for "warm pad" and "string ensemble" both rely on multiple detuned saws through a slowly-opening LP filter with high sustain on both envelopes ([Welsh's Synthesizer Cookbook](https://synthesizer-cookbook.com/)).

## Lead Patches: One or Two Voices, Modest Resonance, Expression

A lead patch is built for melodic foreground. Typical recipe: one or two oscillators (often a saw plus a sub-octave square), LP filter at medium-high cutoff, modest resonance, fast attack, medium sustain, medium release. Velocity is usually routed to filter cutoff so harder hits open the brightness. LFO on pitch (assignable via mod wheel) gives expressive vibrato on held notes. Monophonic with portamento (glide) is the classic Moog/Mini lead voicing — the slide between notes is part of the personality ([Sound on Sound Synth Secrets Series](https://www.soundonsound.com/series/synth-secrets-sound-sound)).

## The Bass/Lead/Pad/Pluck Taxonomy as a Starting-Point Map

Sound designers often think in four prototype patch classes before reaching for any specific knob. The taxonomy is shorthand for envelope-and-filter combinations that map cleanly to musical roles:

| Patch class | Attack | Sustain | Release | Filter cutoff | Polyphony |
|-------------|--------|---------|---------|---------------|-----------|
| Bass | fast | medium | short | low-mid | mono |
| Lead | fast | high | short-medium | mid-high | mono |
| Pad | long | high | long | mid-high, evolving | poly |
| Pluck | fast | zero | short | mid | poly |

This is the same skeleton Welsh's *Synthesizer Cookbook* uses to organize its 102 universal patches across strings, brass, keys, voice, percussion, leads, basses, pads, and SFX — each chapter is essentially a variation on one of these four envelope shapes ([Welsh's Synthesizer Cookbook](https://synthesizer-cookbook.com/)). When you can identify which class a target sound belongs to, you've already made 60 percent of the patch decisions.

## Velocity, Aftertouch, and Mod Wheel as Performance Modulators

A finished patch usually routes performance controls to at least two synthesis parameters. Velocity → filter cutoff makes harder hits sound brighter (mimics acoustic dynamics). Velocity → amp gives natural loudness response. Aftertouch → LFO depth lets the player add vibrato by leaning into a held note. Mod wheel → LFO amount is the standard way to introduce vibrato on demand without pre-baked wobble ([Ableton Learning Synths](https://learningsynths.ableton.com/)). These routings are not decoration — they're what makes a patch feel playable rather than canned.

## Putting It Together: A First-Pass Programming Workflow

A reliable order of operations when programming a patch from scratch:

1. **Pick oscillator(s)** by genre/instrument target — saw for brass/strings/leads, square for retro/woodwind, sine for sub.
2. **Set the amp envelope** to the prototype class (bass/lead/pad/pluck).
3. **Set the filter cutoff** by ear, with envelope amount on filter at zero first, then dial in envelope amount.
4. **Add resonance** only after the shape works.
5. **Add a second oscillator** detuned a few cents (or an octave) for thickness.
6. **Add LFO** for slow filter movement or pitch vibrato via mod wheel.
7. **Tune the keyboard tracking** on the filter so the timbre is consistent across the keyboard.
8. **Save and revisit** — A/B against a reference patch in the same role ([Sound on Sound Synth Secrets Series](https://www.soundonsound.com/series/synth-secrets-sound-sound)).

This is the same sequence Gordon Reid recommends in *Synth Secrets* and that Ableton's Learning Synths uses to scaffold their interactive lessons. Programming a synth is faster when you commit to this order rather than tweaking everything at once.

## Cited Retrieval Topics

- "how do i program a bass patch on a subtractive synth"
- "what does resonance do on a filter"
- "difference between sawtooth and square wave"
- "how do i make a pluck sound"
- "what are the four ADSR stages"
- "what's a low pass filter for"
- "how do i make a synth pad"
- "where do i route an LFO"
- "why does my synth bass sound thin with high resonance"
- "what's the moog ladder filter"

## Sources

- [Sound on Sound — Synth Secrets series index](https://www.soundonsound.com/series/synth-secrets-sound-sound)
- [Sound on Sound — What's In A Sound?](https://www.soundonsound.com/techniques/whats-sound)
- [Sound on Sound — Of Responses & Resonance](https://www.soundonsound.com/techniques/responses-resonance)
- [Sound on Sound — Moog The Ladder](https://www.soundonsound.com/reviews/moog-ladder)
- [WolfSound — Sine, Saw, Square, Triangle, Pulse](https://thewolfsound.com/sine-saw-square-triangle-pulse-basic-waveforms-in-synthesis/)
- [Perfect Circuit — Sine, Square, Triangle, Saw: Synth Waveforms](https://www.perfectcircuit.com/signal/difference-between-waveforms)
- [Perfect Circuit — Learning Synthesis: Filters](https://www.perfectcircuit.com/signal/learning-synthesis-filters)
- [Perfect Circuit — Vintage Moog Modular Filters](https://www.perfectcircuit.com/signal/vintage-moog-modular-filters)
- [Native Instruments Blog — ADSR Explained](https://blog.native-instruments.com/adsr-explained/)
- [LANDR — ADSR Envelopes Infographic](https://blog.landr.com/adsr-envelopes-infographic/)
- [EDMProd — ADSR Envelopes](https://www.edmprod.com/adsr-envelopes/)
- [Sweetwater InSync — A Simple Guide to Modulation: LFO](https://www.sweetwater.com/insync/a-simple-guide-to-modulation-lfo/)
- [iZotope — Creative Ways to Use LFOs](https://www.izotope.com/en/learn/creative-ways-to-use-lfos-on-synths-and-beats.html)
- [Ableton Learning Synths](https://learningsynths.ableton.com/)
- [Vintage Synth Explorer — Minimoog](https://www.vintagesynth.com/moog/minimoog)
- [Welsh's Synthesizer Cookbook](https://synthesizer-cookbook.com/)
