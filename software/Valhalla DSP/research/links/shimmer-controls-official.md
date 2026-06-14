https://valhalladsp.com/2010/11/27/valhallashimmer-the-controls/
valhalladsp.com · Sean Costello (Valhalla DSP) · official "The Controls" reference

Authoritative control list for ValhallaShimmer. NOTE: Shimmer has ONE Pitch/Shift
control with a Pitch *Mode* selector — NOT two separate "Shift1/Shift2" shifters. (The
two-shifter idea in the brief is wrong for Shimmer; dual up+down is the **Dual** Pitch
Mode of the single Shift knob. Stacked intervals = cascade multiple instances, §below.)

## Knobs
- **Mix** — power-complementary crossfade (level stays constant across the sweep).
- **Pitch / Shift** — −12 to +12 semitones; behaviour set by the Pitch Mode. The pitch
  shift "will only be audible with Feedback > 0" (it lives in the feedback path, so it
  compounds: +12 climbs an octave *per repeat*).
- **Feedback** — feedback around the diffusor / pitch-shifter network; sets decay length
  AND the perceived intensity of the pitch shift.
- **Diffusion** — diffusor coefficients: **0.0 = straight delay; 0.5–0.618 = reverb that
  slowly fades in; ~0.9 = a fairly long, smooth decay.**
- **Size** — delay lengths; bigger = larger room / longer decay.
- **Low Cut / High Cut** — highpass / lowpass on the feedback path (tame lows / aliasing).
- **Mod Rate / Mod Depth** — random modulators (Rate is a "rough estimate"; pitch shift
  already supplies movement, so keep Depth low for shimmer).

## Reverb Mode
- **Mono** — mono-in/stereo-out, very large base size, high echo density.
- **Big Stereo** — for cathedrals / monumental spaces.
- **Medium Stereo** — best for traditional "hall" reverbs (smaller than Big).
- **Small Stereo** — small rooms, chorused short ambiences.

## Pitch Mode
- **Single** — classic single-direction shift = the "Shimmer sound."
- **Dual** — simultaneous up+down shift = symphonic / harmonic texture.
- **SingleReverse** — smoother, more organ-like pitch shifting (reversed grain).
- **DualReverse** — well suited to pipe-organ sounds (smooth up+down).
- **Bypass** — no pitch shifting; standard reverb decay.

## Color Mode
- **Bright** — full-bandwidth, modern hi-fi tone.
- **Dark** — large HF loss; resembles classic 1970s–early-80s digital reverbs AND removes
  almost all aliasing noise from the pitch-shifted feedback (the cleaner choice for big
  shimmer walls).

## Format / status
$50 paid plugin. AU/VST2.4/VST3/AAX (Mac); macOS 10.9+ incl. Apple Silicon native.
NOT currently installed in this rig (VintageVerb + Room are).
