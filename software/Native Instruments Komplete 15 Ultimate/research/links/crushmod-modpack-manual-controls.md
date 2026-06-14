https://native-instruments.com/ni-tech-manuals/mod-pack-manual/en/ (phasis / choral / flair)
native-instruments.com · NI Tech Manual — Mod Pack · current

# MOD PACK — Phasis / Choral / Flair full control reference (from the manual)

The modulation trio (predecessor to Crush Pack). **NONE confirmed installed on disk (referenced in navigator; only Bite verified in CONTENTS.md).**

## PHASIS (phaser)
- **Rate:** modulation frequency. **ULTRA mode** extends Rate and Center into audio frequencies → FM-synthesis-like tones (per specs, max modulation speed rises from 8.37 kHz to **477.3 kHz**).
- **Center:** shifts the all-pass peaks/notches in the spectrum.
- **Spread:** density of peaks/notches — left = closer, right = further apart.
- **Notches:** number of peak/notch pairs — **up to 12 pairs.**
- **Feedback:** resonance/prominence of the peaks/notches.
- **Amount:** depth of modulation.
- **Mod Mix:** distributes modulation between Center and Spread (toward Spread = cleaner).
- **Spread mod polarity / Invert:** invert modulation polarity / reverse peak-notch positions.
- **Stereo:** L/R phase offset → width. **LFO Sync:** to host tempo (numerator/denominator). **Mix.**

## CHORAL (chorus)
- **Four modes:** **Synth** (dark vintage polysynth), **Ensemble** (warm/lush '70s string-synth), **Dimension** (bright/transparent early-'80s rack), **Universal** (clean modern).
- **Voices:** 1 → 3 chorus voices (voices 2/3 modulate differently → wider, livelier).
- **Width:** pans voices in opposite directions (0 = preserve input stereo).
- **Rate:** modulation speed (slow pitch changes → fast vibrato). **Amount:** modulation depth on Delay.
- **Delay:** delay times of the chorus voices = spatial depth.
- **Feedback:** sustain/space. **Scatter:** special feedback routing → **reverb-like** behavior without the metallic quality of normal high-feedback chorus.
- **Invert:** inverts the effect signal (character change). **Mix:** equal-power dry↔wet.

## FLAIR (flanger)
- **Modes:** **Standard** (basic per-voice flanging, harmonic peaks/notches), **Thru Zero** (voices duplicated; modulated voices shift against base-pitch duplicates → cancellation; has an **Offset** slider), **Scan** (voices sequenced one→next, arpeggiator-like).
- **Voices:** 1 → 4 comb filters; in Standard/Thru Zero they form a chord, in Scan they sequence.
- **Chord:** harmonic relationship between voices — **24 chord settings.**
- **Detune:** ±~60 cents per voice (synth-osc-detune richness).
- **Pitch:** fundamental frequency of the first voice, in semitones.
- **Feedback:** resonance → metallic; high feedback + Voices/Chord = **tuned resonator** (rings a chord). **Damping:** rolls high-frequency feedback for softer textures.
- **Rate / Amount:** modulation speed/depth (LFO Sync to host). **Width:** stereo + cross-feedback. **Invert:** drops perceived pitch an octave / cancellations in Thru Zero. **Mix.**
