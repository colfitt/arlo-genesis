https://www.youtube.com/watch?v=REiLiIQxTvA
YouTube · Antares Audio Technologies (official) · "Tutorial | Auto-Tune Vocodist" · 2021-08-31

# Vocodist — official Antares full walkthrough (transcript distilled to prose)

Presented by a Vocodist preset designer at Antares. Demo DAW is **Pro Tools**, but the
routing logic (instrument track + side-chain) is the same AU-MIDI-effect pattern Logic uses.
This is the most complete control-by-control source captured. Auto-subs cleaned to prose.

## What it is / pitch
"The most transformative device Antares has ever created." Great for robotic vocals, and for
turning **drum loops or voices into chords**. 20 of the most famous vocoders in history modeled,
including the original **1939 military prototype** (the Voder). Auto-Tune added for pitch + scale
tracking; an **auto-tracking synthesizer** for easy setup; an **XY pad** (borrowed from Auto-Tune
EFX+) for real-time manipulation.

## Quick Start screen
On instantiation, a Quick Start screen offers three setup choices: **synth controlled over MIDI**,
**synth controlled from the voice**, or **external synth source (side-chain)**. Choosing one
**pre-routes the Synth + Oscillator sections** accordingly. Descriptions are identical between
choices; only the routing differs. Can be turned off permanently (checkbox / Settings tab).

## How a vocoder works (the manual-vocoder demo)
A vocoder splits a signal into frequency sections and varies each section's volume independently —
"like a graphic EQ but instead of gently tailoring frequencies, we're isolating them." Earliest
vocoders used **4 bands** (low / low-mid / high-mid / high). He demos manual vocoding: a **noise
wave** through 4 filter splits, automating the faders to simulate consonants/fricatives/plosives/
vowels = the word "vocoder." Then swaps the noise wave for a **sawtooth** carrier → tonal, musical
result. Three parts: (1) input/carrier wave, (2) the filter sections, (3) the volume/fader section
= **the envelope** (volume vector over time). In Vocodist the analyzed signal is **the track where
the plug-in is instantiated** (the modulator); its energy is tracked like a compressor and used to
drive the envelope, which is superimposed onto the carrier. Vocodist has **6–24 bands** plus
envelope / filter / noise / oscillator sections.

## Filter / Model section
- **Model** = where it all begins. From the 1939 Voder to modern in-house Antares models. Editing
  italicizes the model name. Some models have custom curves and disable further manipulation —
  pick an editable model to tweak.
- **Bands** 6–24: more = fidelity, fewer = vintage vocoder effect.
- **Q** raises/lowers the slope; combine with the natural filter slope for effects.
- **Min / Max Hz**: where the signal split starts and ends; narrow range or full spectrum while
  keeping the same band count.
- **Filter slope**: narrow filters = more mechanical, wide = more intelligible.
- **High/Low-pass filters** swap the outermost band-pass filters to HP/LP to dial intelligibility.
- **Stretch & Slide** move the synthesis filter center frequencies relative to the analysis
  filters → reallocation of formants across the filter section (formant sweeps).
- **i icon** toggles graphical info; a moving pitch indicator shows incoming pitch; **Play icon**
  auditions settings with a pink-noise generator (there's one in the Oscillator section too).

## Envelope section
Controls intensity of each filter band — corresponds to the manual fader section but driven by
input intensity. **Attack/Release** like a compressor: fast attack = sharp transients; slow =
smoother. **Individual band level** ("hallmark of any good vocoder") to tailor band response /
EQ out muddy bands. **Freeze** locks the envelope at its current state. **Band Shift** (from a
historic vocoder) shifts envelope-follower outputs across the filters, breaking the 1:1 follower↔
filter mapping; the **X settings** do complex cross-shifting for severe speech scrambling.
**Smear** smears envelope-follower release times logarithmically across bands — negative = longer
releases (low→high), positive = shorter; zero = none.

## Oscillator / Synth section
Dual-oscillator synth, **up to 8-voice polyphony** (1 voice = mono lines, up to 8 for chords).
**Synth Source** = internal oscillator OR external synth. Pitch can track the original signal's
pitch, follow an **external MIDI keyboard**, or use the internal **drone** synth.
- **Glide** = portamento (smears pitch).
- **Octave** transposes both oscillators.
- **Interval** = semitone offset (−12 to +12); **Scale** button switches Interval to scale-degree
  intervals (unison/2nd/3rd/4th… tracking the key) instead of fixed semitones.
- **Shape**: continuously variable square (50%) → through duty cycles → sawtooth, per oscillator.
- Two oscillator volume controls + **Cross Mod** = a ring modulator between the two oscillators.

## Voice / Auto-Tune section (the modulator path)
"No other vocoder now or in history has such a comprehensive feature set to deal with input
signals." **HP filter** removes rumble. **Compress** the input (want a little more than normal for
a vocoder). **Emphasize** boosts highs. **Retune Speed** in ms — normally 20–30 ms for artifact-free
vocal; for a vocoder **jam it to 0** for a more mechanical sound. **Auto-Tune button** must be on
to engage the engine (on by default; off grays the controls). **Keyboard switch** lets MIDI control
the Auto-Tune section's pitch independently of the vocoder section. **Humanize** relaxes retune
speed on long sustained notes.

## Noise section (sibilance / fricatives)
Consonants define where vowels start/stop; vocoders need high-frequency consonant info. Use a synth
rich in highs (square/saw) or the noise generator. **White vs Pink** noise (white = equal energy
per frequency/brighter; pink = equal energy per octave/darker). **Sensitivity** to consonants,
**Balance** = noise-to-oscillator mix, **Level** = noise volume, **Color** = HP filter on the
noise. Sibilance indicator light helps set Sensitivity.

## Output + FX section
- **Voice Env**: amount of voice amplitude envelope applied to the vocoder output ("like an accent
  control on a drum machine").
- **Spread**: stereo enhancer (grays out in mono instantiation).
- **Output/Gain** + **Warmth** = tube-style overdrive on the output.
- **Voice Mix**: blends the original input back in for clarity — but if the original is out of tune/
  key it competes with the vocoded sound, so **keep Auto-Tune on** for clean blends.
- **Chorus**: three modeled choruses ("reminiscent of one of my favorite 80s" units); mono in a
  mono instantiation. The right-arrow **Send Source Vocal to Chorus** adds the input signal to the
  chorus.
- **Voice Mod**: a ring modulator on the original source signal ("to keep it from sounding so
  real"); Oscillator 1 is the other side of that ring mod. Only active when Voice Mix is active.
- **Voice HPF**: removes rumble from the original signal; also requires Voice Mix active.
- **XY pad**: like EFX+ but more programmable; many parameters assignable to X/Y; unavailable
  params are unused in the patch or already on the other axis.

## ⚠️ Carrier-routing setups (the key part)
He demonstrates the three carriers explicitly:
1. **Internal synth, pitch-tracked from the voice** (default / easiest) — just instantiate on the
   audio track; the synth follows the input pitch. No MIDI, no routing.
2. **Internal synth, MIDI-controlled** — "the much easier way to experience Vocodist." Setup:
   create a **mono audio track** ("vocal in") with Vocodist on it; create a **MIDI track** and
   **assign its output to channel 1 of the Vocodist plug-in** (he names it "MIDI trigger"); play a
   MIDI keyboard for the chords while singing into a mic. Verified live in the video (chords follow
   the keyboard, voice supplies the words). He stresses you check the MIDI node = Auto-Tune Vocodist
   #1, channel 1.
3. **External side-chain carrier** ("the full advanced setup is beyond the scope of this video but
   it involves an instrument track and the side chain"): set the **instrument/source track output
   to a side-chain bus**, then in Vocodist set **Synth Source = Side Chain** and **tell Vocodist to
   look at the side-chain input**; adjust the side-chain **Comp/Gain** if needed; arm record. The
   carrier is now your own synth/sound and Vocodist vocodes the voice onto it.

Easiest possible result: drop Vocodist on a lead vocal and pick a preset.

Also notes a **Gate** + **Hold Time** parameter in the synth section = a gate for the input and a
hold time controlling the gate length (helps eliminate inter-note squeaks when pitch-tracking the
voice).
