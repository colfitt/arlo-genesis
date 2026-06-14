https://www.youtube.com/watch?v=v3i-ka1GMvM
You Guide (YouGuide) · "A deep dive to Valhalla SHIMMER reverb tutorial guide" · chaptered control-by-control walkthrough

Distilled prose (auto-captions, cleaned of duplicate lines; settings paraphrased, not verbatim).

## What Shimmer is
A pitch-shifted reverb — "a reverb with a pitch shifter in the feedback path." Best
used AS a shimmer reverb, not a realistic room. The presenter builds every sound from
zero so you hear what each control does in isolation.

## Dialing it from zero (the workflow)
Start with everything down: Mod Rate/Depth at zero, Size all the way down, Diffusion all
the way down, Feedback all the way down. With a synth held in, that's basically the raw
source. Then:
- **Feedback up** → repeats start to recirculate (more intensity). Push it for sustain.
- **Size up** = the size of the reverb / the *time* of the repeats. Bigger Size = longer
  time / longer decay; smaller Size = shorter times. "It's like changing the time" of the
  delay network.
- **Diffusion up** = smears the discrete repeats into a reverb wash. Low Diffusion = you
  hear separate echoes; high Diffusion = it turns into a smooth shimmer reverb. The
  graininess of low Diffusion also depends on Size.
- So the three interact: more Feedback + bigger Size + more Diffusion = a fuller, more
  reverberant shimmer; less of each = a sparser pitch-shifted echo ("Shimmer land" vs a
  more reverb-like wash). You trade between "pitch-shifted delay" and "pitch-shifted
  reverb" by balancing Size + Diffusion + Feedback.

## The Pitch / Shift control (the shimmer itself)
- **Shift** is in semitones; each repetition is pitch-shifted by that amount, and the
  shift *compounds* through the feedback path (so +1 climbs by a semitone each repeat,
  +12 climbs an octave each repeat = the classic rising shimmer). Range up to ±12 (an
  octave). You can do +7 (a fifth) for less extreme, "+12" for the octave shimmer, or
  negative for a descending/darker wall. "It can go really really crazy."
- Demo: with Mix ~50, Diffusion down, Feedback up, Shift ~+7 → a clearly pitch-climbing
  "pitch delay" effect; each repeat steps up a fifth.

### Pitch Modes
- **Single** = the default. Shifts every repeat up (or down) by the Shift amount; the
  spectrum visibly climbs (or descends) over time. The classic single-direction shimmer.
- **Dual** = shifts UP *and* DOWN at the same time — you see one set of spectral peaks
  rising and another falling simultaneously. Symphonic/wider harmonic texture.
- **SingleReverse** = same as Single but "reverses the grain in time" (Valhalla's words),
  giving **smoother / cleaner** pitch shifting than plain Single. Audibly less grainy.
- **DualReverse** = the Dual process done with the reversed-grain method = same up+down
  spread but smoother/cleaner.
- **Bypass** = pitch shifting off; plain reverb decay. NOTE: even at Shift = 0 in a
  Pitch mode the shifting engine is still "applying the process behind the scenes" — set
  the mode to Bypass to get genuinely clean (real-delay-sounding) repeats.

## Reverb Modes
- **Mono** = mono-in / stereo-out. Already pretty dense and slow. (The default the
  presenter builds with.) Source can be mono or stereo; comes out stereo.
- **Big Stereo** = denser, bigger — cathedral/monumental scale.
- (Medium Stereo / Small Stereo = progressively smaller base size; Small good for
  short chorused ambiences — covered briefly.)

## Tone / Color
- **Low Cut / High Cut** filter the feedback path (high-cut tames aliasing/brightness in
  the climbing tail; low-cut keeps the wall out of the mud).
- **Color**: Bright = full bandwidth/modern; Dark = rolls off highs (vintage-digital
  flavor) and, crucially, *kills most of the aliasing noise* the pitch shifter would
  otherwise add to the feedback — so Dark is the cleaner-sounding choice for big shimmer.
- **Mod Rate / Depth** = modulation; keep low for shimmer because the pitch shifting
  already supplies movement.

## Takeaway recipe (presenter's)
Octave shimmer = Single (or SingleReverse for smoother) · Shift +12 · Feedback high ·
Diffusion ~0.9 · Size to taste (bigger = longer) · Color Dark · Mod low · Mix to taste
(50 for an obvious effect, lower on a send). Drop Shift to +7/+5 for subtler harmonic
climbs.
