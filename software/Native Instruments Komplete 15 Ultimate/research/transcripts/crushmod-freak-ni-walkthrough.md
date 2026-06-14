https://www.youtube.com/watch?v=Hv896gdH_Wk
Native Instruments (Tim Cant) · "Walkthrough: FREAK from EFFECTS SERIES – CRUSH PACK" · 2018

# FREAK — official NI walkthrough (distilled)

Freak = frequency shifter + ring/amplitude modulator + AM-radio modeler, on an analog diode-ring model. The single most flexible degrade unit in Crush Pack for inharmonic/sci-fi/drone work. **NOT confirmed installed on this rig's disk — Crush Pack is referenced but only Bite is verified in CONTENTS.md.**

## The morph at the heart of it — TYPE
One control common to all three modes lets you "move seamlessly from amplitude modulation → ring modulation → frequency shifting." That continuous morph is the core sound-design gesture.

## Three FX modes (re-task the left knobs)

### Oscillator mode (internal sine)
- Internal sine oscillator shifts/modulates the input.
- **Freq range switch:** coarse = ±5000 Hz, fine = ±200 Hz. (Bipolar — shift up OR down.)
- **Antifold:** "reduces artifacts in the lower frequency range when turned up, which results in a thinner sound" (i.e. cleans sub-0 Hz sideband folding; back it off for fatter, dirtier lows).
- **Stereo:** phase offset L/R → space and width.
- **Harmonics:** add even harmonics to "slightly distort and enrich the sound."
- **Feedback:** "produces all kinds of sounds from phasing to even more distortion." Higher feedback in frequency-shift = barber-pole/phasing → distortion.

### Sidechain mode (★ the drone weapon)
- Lets a source *other than* the internal sine modulate the input.
- Demo: take a **pad from Massive + use a decaying sine wave as the sidechain input**.
- **Contour at 100%:** "the modulation follows the envelope of the sidechain input." At 0% it fades to the raw sidechain signal → "transitioning into more inharmonic ring-modulation territory."
- **SC switch OFF = self-modulation:** "the input signal modulates itself" — contour at 0% "multiplies the signal with itself, which leads to a distortion that sounds particularly interesting." (Self-ring-mod distortion with NO host routing needed.)
- **Release:** how quickly the modulation follows the sidechain envelope (drum-loop demo).
- **Band-pass filter:** "single out particular parts of the sidechain spectrum" to drive the modulation.

### Radio mode (AM-radio model)
- Emulates noisy/distorted AM-radio demodulation.
- **Tuning/Carrier:** "just like on your granny's old radio" — carrier changes center frequency (visualized in GUI). Off-center = interference/detuned.
- **Demod style:** default vintage-radio type → switch to the more aggressive multiplication style for extreme.
- **Feedback** here also controls noise amount (turn down for less noise).
- **Width:** band-pass bandwidth — narrow = strong effect, wide = cleaner.

## Rig relevance
- **Sidechain self-mod (SC off, contour 0%)** on a banjo/baritone/drone = ring-mod distortion that needs zero host setup — perfect in Logic AU.
- **Sidechain a decaying sine into a held pad** = the modulation breathes with an envelope → evolving inharmonic wall.
- **Frequency-shift + feedback** = barber-pole/endless-rising phasing under a drone.
- **Coarse ±5000 Hz frequency shift** = aggressively metallic, detuned, clangy; **fine ±200 Hz** = slow, subtle inharmonic drift (more usable under sustained doom).
