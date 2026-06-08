# Patch Design Vocabulary — Translating Adjectives to Moves

**Scope:** synthesis
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Welsh's *Synthesizer Cookbook* (102 universal patches); Gordon Reid, *Synth Secrets* (Sound on Sound); Ableton Learning Synths
**Tags:** `synthesis`, `patch-design`, `recipe`, `vocabulary`, `methodology`

---

## Why a Move-Vocabulary Beats a Knob-Vocabulary

Sound designers who can program quickly almost never reach for one knob at a time. They reach for **moves** — bundled gestures of two or three coordinated parameter changes that produce a recognizable character — and then refine. "Warm" is not a knob; it's a habitual cluster of moves (close the filter, detune the oscillators, add light saturation). Welsh's *Synthesizer Cookbook* is organized this way: each of its 102 universal patches describes the sound by its harmonic and envelope signature, then lists the move-bundle to get there ([Welsh's Synthesizer Cookbook](https://synthesizer-cookbook.com/)). Gordon Reid's *Synth Secrets* uses the same approach when reverse-engineering specific timbres ([Sound on Sound — Synth Secrets series](https://www.soundonsound.com/series/synth-secrets-sound-sound)). This document maps the most common adjectives producers use ("make it warmer," "more glassy," "huge") to the canonical move-bundles, so the vocabulary becomes actionable rather than vibe-based.

## "Warm" → Filter Down, Detune, Light Saturation

When someone asks for a warmer patch they almost always want three things at once: less high-frequency content, more harmonic density in the mids, and a touch of analog-style nonlinearity. The move:

1. **Close the low-pass filter** to roughly half-open or lower, taking the brittle high partials out of the sound.
2. **Detune a second oscillator** 5–10 cents from the first to thicken the midrange (the slight beating between detuned saws is what listeners hear as "analog character").
3. **Add light saturation** at the output — tape, tube, or transformer-style — for harmonic enrichment of the surviving partials ([99Sounds — Warm Up Your Sounds with Filters and Saturation](https://99sounds.org/filters-and-saturation/)).

A long amp release (300–800 ms) reinforces the perception of warmth because the tail blooms rather than clicking off. Resonance is kept low — high resonance reads as "edgy," not warm. If the patch is still too thin, a sub-octave sine layer at -10 to -15 dB below the main oscillators fills the bottom. This same move-bundle defines Welsh's "warm pad" and "soft brass" recipes.

## "Bright" → Cutoff Up, Saw or Pulse Source, Slight Chorus

"Bright" is the inverse move: open the filter, choose a harmonically rich oscillator, and shimmer the high end without making it harsh.

1. **Set the low-pass cutoff high** — at least 75 percent open, often fully open — so upper harmonics make it through.
2. **Use sawtooth or narrow pulse waves** for maximum harmonic content. Sine and triangle can't be made bright; they don't contain the harmonics to brighten ([WolfSound — Basic Waveforms](https://thewolfsound.com/sine-saw-square-triangle-pulse-basic-waveforms-in-synthesis/)).
3. **Add chorus or a stereo enhancer** to spread the high frequencies across the stereo image — this reads as "shimmery" rather than "loud high-end."

A small amount of velocity-to-cutoff modulation keeps the brightness expressive across keyboard dynamics. If brightness tips into harshness, the usual fix is a narrow EQ dip around 2.5–4 kHz rather than closing the filter (which kills the move). A high-shelf boost above 8 kHz is a separate question — that's "air," not brightness.

## "Evolving" → Slow LFO on Filter, Wavetable Position, or Pitch

"Evolving" means the patch keeps changing while you hold the note. The single best move is a **slow LFO** (under 0.5 Hz, sometimes as slow as 0.05 Hz) routed to one or two slow-moving destinations:

1. **LFO 1 on low-pass cutoff** — moderate depth, slow rate, triangle or sine wave for smooth motion.
2. **LFO 2 on wavetable position** (if available) at a slightly *different* rate — the desync between the two LFOs ensures the patch never repeats over the course of a held note ([Native Instruments — What is Wavetable Synthesis?](https://blog.native-instruments.com/what-is-wavetable-synthesis/)).
3. **Optional: slow pitch LFO** with small depth (under ±5 cents) for organic drift.

For chord pads, add stereo width via a chorus or detuned-oscillator pair, then let the slow filter LFO do most of the storytelling. This is the same recipe the PPG Wave and Korg Wavestate use natively, and what Massive's preset designers recommend ([Native Instruments — Massive X Wavetable Oscillators](https://native-instruments.com/ni-tech-manuals/massive-x-manual/en/wavetable-oscillators)).

## "Glassy" → FM with Non-Integer Ratio, Fast Decay

"Glassy" maps almost cleanly onto FM synthesis with a bell-style operator configuration.

1. **Two-operator FM** — sine carrier, sine modulator.
2. **Set the modulator-to-carrier ratio to a high non-integer** (4:1 or higher, ideally inharmonic like 4.7:1 or 7.3:1).
3. **Modulator envelope decays faster than carrier envelope** — the bright "ping" attack rings out into a pure-tone tail ([Sound on Sound — Synthesizing Bells](https://www.soundonsound.com/techniques/synthesizing-bells)).
4. **Modulation index** (modulator level) is moderate at attack, low at sustain — so harder velocity hits make the sound glassier.

This is essentially the DX7 bell recipe, scaled. For "glassy pluck" reduce the carrier sustain to zero so the whole patch is attack-and-decay. For "glassy pad" lengthen both envelopes and add slow chorus. Glassy is one of the few adjectives that's genuinely hard to fake with subtractive synthesis — FM, phase distortion, or wavetable with a bell-flavored table will get there faster than any LP filter ([Sound on Sound — More On Frequency Modulation](https://www.soundonsound.com/techniques/more-frequency-modulation)).

## "Huge" → Unison Detune, Octave Stack, Stereo Width

"Huge" is the supersaw move. Three combined gestures:

1. **Unison stack** of 5–9 voices per oscillator, with **unison detune** set to where the oscillators just-barely start to sound out of tune ([Syntorial — Supersaw Trance Lead](https://www.syntorial.com/tutorials/synth-quickie-supersaw-trance-lead/); [Perfect Circuit — Super Saw History](https://www.perfectcircuit.com/signal/super-saw-history)).
2. **Octave layer** — a second oscillator pitched one octave below (or above) the first, at lower level, to fill out the spectrum.
3. **Maximum unison width** so the detuned voices pan hard across the stereo field — this is the difference between "fat" and "huge."

The Roland JP-8000's supersaw, born from this template, defined late-90s trance and is still the dominant move for any "wall of synth" lead or pad in EDM ([MusicRadar — Supersaw Synth Sound](https://www.musicradar.com/how-to/supersaw-synth-sound)). For a fully "huge" build add a sub-bass sine layer below 80 Hz, a noise oscillator high-pass-filtered above 3 kHz for top-end air, and reverb on a long pre-delay so the dry transient stays defined. Be aware huge patches eat mix space — they belong on the lead or the pad, not on both.

## "Plucked" → Fast Attack, Fast Decay, Zero Sustain

A pluck is defined by its envelope, not its oscillator. The move:

1. **Amp envelope** — attack near zero (0–5 ms), decay short (100–400 ms), sustain at zero, release short (50–200 ms).
2. **Filter envelope** — same fast-decay shape on the filter cutoff with moderate envelope amount, so the note opens bright on each hit and closes immediately.
3. **Oscillator** — usually a single saw or pulse; double-saw plucks are common but the second osc is usually sub-octave for body, not detuned for thickness ([Syntorial — Stromae Alors on Danse Pluck](https://www.syntorial.com/preset-recipe/stromae-alors-on-danse-pluck/)).

Velocity on filter cutoff makes harder hits sound brighter, which is the difference between a plastic preset pluck and a playable one. Adding a touch of stereo delay (1/8 dotted, ~30 percent feedback) turns a dry pluck into a melodic ear-worm without thickening the patch itself. Plucks live in pop, house, and trance because they cut through without sustaining or competing with vocals.

## "Punchy" → Fast Attack Envelope, Pitch Envelope on Onset, Slight Distortion

"Punchy" is mostly about the first 50 ms of the sound.

1. **Amp envelope** attack at zero — no fade-in at all.
2. **Pitch envelope** with a 1–3 semitone drop over 30–80 ms decay on a sub-bass or kick-style patch. This is the "click" of a kick drum and the bite of an FM bass.
3. **Distortion or saturation** at the output adds harmonic content that translates to "presence" on small speakers ([Vintage King — Best Analog Saturators](https://vintageking.com/blog/best-analog-saturators-harmonic-enhancers/)).

For sub-bass punch, the pitch envelope is essential — a steady sine plays as "thump" but adding a pitch-drop transforms it into a kick-style hit. For lead-synth punch, an aggressive filter envelope (decay 50–100 ms, envelope amount high) gives a sharp filter sweep on each note onset.

## "Dirty" → Bit Reduction, Wave Folding, Aggressive Distortion

"Dirty" is harmonic content that doesn't behave like a clean oscillator — non-musical artifacts that read as character.

1. **Bit reduction or sample-rate reduction** introduces aliasing and quantization noise. Modern plugins like D16's Decimort or Ableton's Redux do this directly.
2. **Wave folding** (Buchla-style, common on Serum's WaveTable warp modes) bends the wave back on itself, generating intense odd harmonics.
3. **Pre-filter distortion** — saturate or distort *before* the low-pass filter so the filter cleans up the harshest highs while keeping the gritty mids ([99Sounds — Warm Up Your Sounds with Filters and Saturation](https://99sounds.org/filters-and-saturation/)).

Acid bass and growl bass are both "dirty" — but acid uses a resonant filter sweep as the dirty element, while growl uses LFO-modulated wave folding or comb filtering. Distinguishing the two depends on whether the dirt is *static* (acid: same harshness across notes) or *modulated* (growl: harshness moves with LFO).

## "Wide" → Stereo Detune, Chorus, Haas Trick

"Wide" lives in the stereo image, not the spectrum. Three reliable moves:

1. **Stereo detune** — two oscillators panned hard left and right, detuned 5–15 cents apart. The slight pitch difference between channels creates a phase-rich stereo image.
2. **Chorus** with rate around 0.5–1 Hz and depth around 20–40 percent. This is the foundation of every 80s pad ever programmed.
3. **Haas-effect double** — duplicate the patch, pan the copies hard L/R, and offset one by 10–30 ms. The ear interprets the delay as width rather than echo ([SoundBridge — Design Super Saw Sound](https://www.soundbridge.io/design-super-saw-sound)).

Stack two of these together and the patch reads as huge stereo. Stack three and it starts to lose mono compatibility — always check the mono fold-down before committing. Width applied to bass is usually a mistake; keep low frequencies (under 120 Hz) in mono.

## "Vintage" / "Lo-Fi" → Pitch Wobble, Tape Saturation, Filter Drift

"Vintage" character is mostly *imperfection* — the kinds of inaccuracies that analog hardware introduces and digital synths don't.

1. **Slow random LFO on pitch** with tiny depth (under ±5 cents) for oscillator drift. Sample-and-hold LFOs work well here.
2. **Tape saturation** plugin (e.g., Softube Tape, Universal Audio Studer A800) at light settings adds high-frequency rolloff and warm second/third-harmonic distortion.
3. **Slow LFO on filter cutoff** at very low depth (5–10 percent) simulates voltage drift in vintage VCFs ([99Sounds — Warm Up Your Sounds with Filters and Saturation](https://99sounds.org/filters-and-saturation/)).

For lo-fi specifically, add bit reduction (12-bit is the classic SP-1200 setting) and a high-shelf cut above 8 kHz. The combination of pitch drift, tape character, and filter wobble is what makes a software supersaw sound "vintage Roland" rather than "preset Serum."

## "Aggressive" / "Cutting" → Resonance, FM, Mid-Range Boost

When the patch needs to cut through a dense mix, three moves stack:

1. **Resonance on the filter** in the 50–75 percent range, with cutoff tracking the keyboard so the resonant peak shifts with pitch.
2. **FM between oscillators** (most modern wavetable synths offer osc-to-osc FM) for inharmonic edge.
3. **Mid-range EQ boost** at 2–4 kHz after the synth — this is where the ear localizes "cutting" instruments ([Sound on Sound — Of Responses & Resonance](https://www.soundonsound.com/techniques/responses-resonance)).

Velocity on FM amount makes harder hits more aggressive. A short, fast amp envelope reinforces the cut — long sustained notes blur the front edge of the attack. Aggressive patches are almost always mono lead voicings; polyphonic aggression turns into wash.

## Move-Vocabulary as a Teaching Tool

A productive way to internalize this vocabulary is to **reverse-engineer** five reference patches per adjective. Pick five "warm" pads from different records, A/B them against your patch, and adjust until your patch sits in the same character zone. The exercise builds an ear for which moves matter most. Welsh's *Synthesizer Cookbook* is structured as exactly this kind of catalog: every patch has a verbal description ("warm clarinet," "glassy bell," "huge brass") and a recipe of moves to reach it ([Welsh's Synthesizer Cookbook](https://synthesizer-cookbook.com/)). Once the vocabulary is internalized, communication with collaborators shortens dramatically — "make it warmer with a bit more cut at the top" becomes a 30-second adjustment instead of an exploratory hunt. The vocabulary also makes it easier to *describe* a missing element in an arrangement: "we need something glassy in the chorus" tells everyone in the room what category of sound to dial up, before anyone touches a synth.

## When Adjectives Conflict: Stacked Patches

Some requests describe patches that can't be one voice — "warm but glassy," "huge but plucky." When two adjectives pull in opposite directions, the practical answer is usually **two layers**, not one compromised patch:

- **Warm + glassy** = a warm subtractive pad layered with a short FM bell on the attack only. The bell envelope decays in 200 ms, leaving the warm pad to sustain.
- **Huge + plucky** = a wide unison saw pluck (short envelopes) layered with a longer-release supersaw pad at -10 dB underneath. The pluck defines the rhythm, the pad fills the space between hits.
- **Dirty + smooth** = a clean sub-sine fundamental with a distorted/folded mid-layer high-passed above 200 Hz. The low end stays clean; the dirt lives upstairs.

Modern synths and DAW racks make this layering trivial — Ableton's Instrument Rack, Logic's Stack, and Bitwig's nested instruments all let you key-split or velocity-layer multiple patches into a single "instrument" ([Ableton Learning Synths](https://learningsynths.ableton.com/)). The vocabulary still applies; it just applies per layer.

## Cited Retrieval Topics

- "how do i make a synth sound warmer"
- "what makes a synth bright"
- "how do i make a pluck patch"
- "how do i make a glassy bell sound"
- "what's the supersaw recipe"
- "how do i make an evolving pad"
- "how do i make a synth aggressive in the mix"
- "how do i make a vintage analog sounding patch"
- "how to make a synth wide stereo"
- "warm but glassy synth layering"

## Sources

- [Welsh's Synthesizer Cookbook](https://synthesizer-cookbook.com/)
- [Sound on Sound — Synth Secrets series](https://www.soundonsound.com/series/synth-secrets-sound-sound)
- [Sound on Sound — Synthesizing Bells](https://www.soundonsound.com/techniques/synthesizing-bells)
- [Sound on Sound — More On Frequency Modulation](https://www.soundonsound.com/techniques/more-frequency-modulation)
- [Sound on Sound — Of Responses & Resonance](https://www.soundonsound.com/techniques/responses-resonance)
- [Ableton Learning Synths](https://learningsynths.ableton.com/)
- [Native Instruments Blog — What is Wavetable Synthesis?](https://blog.native-instruments.com/what-is-wavetable-synthesis/)
- [Native Instruments — Massive X Wavetable Oscillators](https://native-instruments.com/ni-tech-manuals/massive-x-manual/en/wavetable-oscillators)
- [Syntorial — Synth Patch Checklist](https://www.syntorial.com/tutorials/synth-patch-checklist/)
- [Syntorial — Supersaw Trance Lead](https://www.syntorial.com/tutorials/synth-quickie-supersaw-trance-lead/)
- [Syntorial — Stromae Alors on Danse Pluck](https://www.syntorial.com/preset-recipe/stromae-alors-on-danse-pluck/)
- [MusicRadar — Supersaw Synth Sound](https://www.musicradar.com/how-to/supersaw-synth-sound)
- [Perfect Circuit — Super Saw History](https://www.perfectcircuit.com/signal/super-saw-history)
- [SoundBridge — Design Super Saw Sound](https://www.soundbridge.io/design-super-saw-sound)
- [99Sounds — How to Warm Up Sounds with Filters and Saturation](https://99sounds.org/filters-and-saturation/)
- [Vintage King — Best Analog Saturators & Harmonic Enhancers](https://vintageking.com/blog/best-analog-saturators-harmonic-enhancers/)
- [WolfSound — Basic Waveforms](https://thewolfsound.com/sine-saw-square-triangle-pulse-basic-waveforms-in-synthesis/)
