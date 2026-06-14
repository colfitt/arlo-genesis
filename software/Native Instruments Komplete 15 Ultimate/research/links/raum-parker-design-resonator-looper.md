https://blog.native-instruments.com/dr-julian-parker-reflects-on-the-creation-of-our-raum-reverb/
blog.native-instruments.com · Dr Julian Parker (RAUM designer) interview · n.d.

# RAUM design interview — the resonator/looper/Cosmic internals (Julian Parker)

The designer's own intent. Goes deeper than the manual on WHY the creative tricks work.

## Cosmic = all-pass cascade in a feedback loop
*"Each time you get an echo with the pre-delay it gets more blurred and more diffuse."* Cosmic
puts cascaded all-pass filters INSIDE the predelay feedback loop — so on Cosmic, the predelay
feedback is the wash generator. (Grounded/Airy put the reverb AFTER the predelay, no feedback
inclusion → that's why only they get Freeze.)

## Pre-delay as resonator/comb — Parker's favourite use
*"I definitely like using the pre-delay section as a resonator or a comb filter."*
- **Lossless / sample-quantized delay:** instead of interpolating delay times (which low-pass-
  filters the signal), RAUM quantizes the predelay to integer sample counts → keeps
  *"high frequency clarity which is a bit unusual."* So the comb stays crisp/pitched, not dull.
- **Adaptive limiter (not distortion)** in the feedback path: *"adapts based on the delay time,
  so it never really sounds like limiting."*

## Looping — up to 4 bars w/ auto-overdub
At 100% feedback the predelay supports **up to four-bar loops**; the adaptive limiter *"kind of
acts like an auto overdub feature,"* letting you layer without the HF degradation interpolated
delays would cause. → RAUM doubles as a clean 4-bar looper/overdubber.

## Modulation — three zones
Subtle echo-breaking (low) → chorusing (mid) → **above ~70% = "weird, uncanny territory, where
it sounds detuned and dissonant."** The seasick/detuned-shimmer wall lives >70%.

## Size = up to granular
*"Really tight to so sparse that it is almost like a granular effect"* and stays musical across
the range.

## Freeze is a performance tool
*"Does not even make much sense in a set-and-forget way"* — built to be triggered/automated live.
Everything in RAUM is automation-friendly by design.
