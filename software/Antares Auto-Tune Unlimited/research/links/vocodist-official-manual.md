https://antares-web-frontend.sfo3.cdn.digitaloceanspaces.com/documentation/pdfs/Auto-Tune-Vocodist.pdf
Antares (official) · "Auto-Tune Vocodist User Guide" PDF (48 pp) · read page-by-page from the rendered PDF

# Vocodist — official manual (verified control reference + defaults)

The authoritative source. PDF is image-rendered (no OCR text), read visually page by page. All
control names, ranges and screenshot default values below are read directly off the manual. This
is the spec backbone for the UsageGuide.

## Signal architecture (verified)
The **input track** (where Vocodist is inserted) is the **modulator / analysis** signal. The
**synthesis channel** = either the **internal oscillator** OR a **Side-Chain** source. The two are
combined per-band by the filter bank. There are three independent things you can route: the
**modulator** (insert track), the **synthesis source** (oscillator or side-chain), and — when
oscillator is the source — its **pitch** (Voice / MIDI / Key).

## DAW insertion (manual, p.11) — and the Logic caveat
Manual gives only the trivial "insert on an audio/instrument track or bus" instructions per DAW.
**Logic Pro** entry verbatim: *"Choose an empty insert slot on one of your audio tracks, instrument
tracks or buses and select Auto-Tune Vocodist… in Audio Units > Antares."* The manual does **NOT**
document MIDI-input or side-chain routing inline — for both, p.25 explicitly punts: *"Check out the
Auto-Tune Vocodist help page for tips on setting up sidechain input in your DAW."* So the real
Logic MIDI/side-chain workflow lives in the (JS-walled) help page / forums, captured separately.

## Global controls (p.12–15)
- **Preset** menu + like/favorite + **Random Preset** dice. Artist preset folders: **Buddy Ross,
  Chromeo (P-Thugg), Damien Lewis, J. Chris Griffin, Rachel Collier.**
- **Input Type** (Soprano / Alto-Tenor / Low Male / Instrument etc.) — match to source; screenshot
  default = **ALTO/TENOR**. **Key + Scale** (Chromatic default; Auto-Key compatible).
- **Auto-Tune button** (toggles the AT engine) + **Auto-Tune Targets MIDI** (keyboard icon).

## Voice controls (modulator path, p.18–20) — only affect the analysis input / dry channel
- **Low-Cut Filter**: button, cuts <80 Hz; **on by default**. Applies only to the analysis input.
- **Compress**: threshold (dB) before the filter bank; *applies upward compression / makeup gain.*
  Screenshot value 19. Apply "a little more than normal for a vocoder."
- **Emphasize**: HF boost into the analysis bank (cures muddy/unintelligible output). Value 20.
- **Retune Speed** (ms): **0 = classic robotic Auto-Tune Effect**; higher = subtler. *Only affects
  the dry voice channel (hear via Voice Mix), NOT the vocoder output.* Screenshot 0 / page-18 shot 15.
- **Humanize**: relaxes retune speed on sustained notes; *dry channel only; no effect if Voice Mix=0.*

## Noise controls (sibilance substitution, p.21–23)
Replicates unvoiced consonants (s/sh/t/ch). **White/Pink** model; **Sensitivity** (sibilance
detector; default ~42), **Balance** (noise↔synthesis mix at sibilant moments; 0=off, 100=full
replace; default ~59), **Level** (default 50), **Color** (HP filter, default **3500 Hz** / shot 958).
Unvoiced indicator light. Pro tip: crank Sensitivity + Balance + play with Color/Band-Gain for
**ethereal whispery effects**.

## Synth controls (the carrier engine, p.24–27) — VERIFIED routing
- **Source** menu = **Oscillator** (internal 8-voice dual-osc) or **Side Chain** (route any plug-in/
  instrument/sampler as the carrier). *When Source = Side Chain, the Oscillator controls are
  disabled* and you get **Comp** (sidechain compressor threshold) + **Gain** (sidechain input level)
  instead (screenshot Comp 10, Gain 0).
- **Pitch Track** (only when Source = Oscillator): **Voice** / **MIDI** / **Key**.
  - **Voice**: oscillator pitch follows the input voice (Auto-Tune optional). Enables **Hold Time**
    (default ~2.8 — lengthen to kill inter-note squeaks) and the **Gate** button (osc sounds only on
    clear detected pitch; off = just follows dynamics).
  - **MIDI**: play the osc from a MIDI keyboard / MIDI track. Enables **Voices** (poly up to 8),
    **Pitch Bend** range (semitones; default 2), **Release**, and **X CC# / Y CC#** for mapping the
    XY pad to MIDI controller knobs.
  - **Key**: a **Mini Keyboard** sets a **single drone pitch** held continuously. → the rig's
    instant talking-drone mode.

## Filter Design (p.28–33)
- **Model** menu = **20 models**, **18 modeled** after vintage/modern hardware (lineage cited:
  Homer Dudley's 1937 Voder → units used by **Wendy Carlos, Stevie Wonder, Herbie Hancock,
  Kraftwerk, Daft Punk**). Plus Antares' own **Antares Voc-1** and **Barkhausen** (max-intelligibility).
  Editing italicizes the name + asterisk; re-select to reset. Five models have fixed custom curves
  (uneditable): **Barkhausen, ES 2000, SN VSM-201, DF A-129, MM VF11.**
- **Filter Slope**: 4 band-pass shapes. *Higher order (steeper/narrower) = more isolation/
  intelligibility; lower order (wider) = more overlap = grittier, more lo-fi.*
- **Lowpass/Highpass** buttons swap the outer two bands from band-pass to LP/HP.
- **Bands** (6–24; screenshot 24): more = fidelity, fewer = lo-fi vintage. **Q** (default 5.0):
  higher = sharper/narrower bands. **Min Hz / Max Hz** (defaults 100 / 10000): set lowest/highest
  band center freqs; interior bands re-space to stay even.
- **Stretch** (default 1.00) / **Slide** (default 0.00): shift the **synthesis** bands relative to
  the **analysis** bands = **formant shifting** (Slide up = formants up). Filter Graph shows it
  live; white tick marks = synthesis band centers vs. analysis bands.

## Envelope Design (p.34–38)
- **Attack** (ms; shot 0.8): short = percussive/intelligible, long = blurred/soft.
- **Release** (ms; shot 17): short = follows decay tightly; long = sustained, more drone-like.
- **Band Gain Multi-Slider**: per-band gain like a graphic EQ over the vocoder output; **Band Gains
  Up** = reset all to 0 dB; **Band Gains Down** = mute the vocoder (handy to audition just the dry
  Auto-Tuned voice); **Random Band Gains** dice.
- **Freeze**: locks the vocoder onto the current input spectrum/vowel **indefinitely** → sustained
  vowel/wall without holding a breath.
- **Band Shift** (− / + / +1, plus **X1/X2/X3** criss-cross): re-patches analysis→synthesis band
  mapping for formant-shift / **speech-scrambling alien** effects.
- **Smear** (shot 4): staggers per-band release times for **ringing reverb-like** effects (low Smear
  = increasing releases low→high; high = decreasing).

## Oscillator controls (p.39–42) — the internal carrier
Dual osc, **up to 8 voices** (Voices active only with Pitch Track=MIDI). **Glide** (ms portamento,
shot 7), **Octave** (±2), **Release** (MIDI-only fade-out, shot 29), **Detune** (cents between osc1/
osc2 = chorusing, shot 7), **Unison** (detunes 8 stacked voices per osc; Voice/Key modes, shot 3),
**Interval** (per-osc transpose −12..+12 semis; **Scale** button makes intervals key-conforming
scale degrees, e.g. +3rd), **Shape** (continuous: 0=saw → pulse → square; per osc; shots 36 / 0),
**OSC1/OSC2 gain** (shots 75 / 100), **Cross Mod (X)** = **ring modulation** between the two oscs
(shot 0/25).

## Output + FX (p.43–45) — last stage
- **Output Meter.** **Voice Env** (how much of the voice's amplitude envelope is impressed on the
  vocoder output; shot 52). **Spread** (stereo width; max = odd bands hard-L / even bands hard-R;
  shot 28; grays out in mono). **Gain dB** (output level; shot −2.5). **Warmth** = modeled analog
  **tube saturation** drive in dB (shot 3.0). **Voice Mix** (dry input blend; 0 = vocoder only and
  disables Voice HPF + Voice Mod; shot 27). **Chorus** = 3 modeled vintage choruses (shot II);
  **Send Source Vocal to Chorus** (right-arrow) routes the dry vocal through the chorus too.
  **Voice HPF** (HP on dry vocal before mixing; pro tip: 5–6 kHz + raise Voice Mix for intelligibility;
  shot 237). **Voice Mod** = **24 pitch-tracking ring-mod varieties** on the dry source (shot 5;
  needs Voice Mix > 0).

## Settings (p.46–48)
Quick-Start toggle, Enable Auto-Key Detection, Enable Auto-Tune, Tooltips, **Choosy Tracking**,
**Ignore Vibrato**, Detune display, OpenGL graphics, **Save as Default**.

## QC
All names/ranges/defaults read directly off the rendered manual PDF (image-based, no OCR). The
single gap the manual itself leaves is the **DAW side-chain/MIDI routing**, which it defers to the
(JS-walled) help page — supplied by the LogicProHelp + Antares-help forum capture instead.
