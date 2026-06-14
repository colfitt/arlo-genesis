https://audiopluginnews.com/in-depth-review-of-soundtoys-decapitator-tips-for-saturation/
audiopluginnews.com · Audio Plugin News · in-depth review

# Decapitator — power-user tips & hidden features (control-by-control)

## Controls
- **DRIVE** — raises input level into the saturation circuit; more drive = more
  distortion. Crucially, **the EQ/tone curve of each style changes with the DRIVE
  amount.** Low drive = flatter/neutral EQ; high drive = a unique, ever-changing
  textured EQ. So the *tone* is drive-dependent, not just the dirt.
- **OUTPUT / AUTO** — with **AUTO on (default), output auto-drops as you raise
  Drive**, level-matching so you A/B color vs loudness honestly. The most useful
  control for not fooling yourself.
- **PUNISH** — hidden button that **boosts input gain by +20 dB**, independent of
  Auto. For quiet sources or instant heavy overdrive.
- **MIX** — blends saturated + original (parallel saturation in-plugin). Key trick:
  **push DRIVE hard and pull MIX toward DRY** = keep transients/clarity of the dry
  signal but inject unique textured saturation underneath. Restores transients the
  saturation stage chops off.
- **TONE** — tilt EQ (dark↔bright); the EQ-curve *shape* depends on the chosen
  preamp style.
- **LOW CUT + THUMP** — Thump adds resonance/LF-boost *at the low-cut frequency,
  before* the saturation circuit → tighter, punchier low-end.
- **HIGH CUT + STEEP** — Steep changes the Q / makes the high-cut slope steeper
  (gentle 6 dB/oct → steep 30 dB/oct). The fizz-killer.

## Gain staging (matters a lot)
Saturators are very sensitive to incoming level. **Target ~0 VU (−18 dBFS)** going
in. Higher incoming signal = more distortion, so set levels deliberately.

## Concrete example settings
- **Colored/obvious saturation:** Drive 6 / Mix ~90%.
- **Subtle textural enhancement:** Drive 4 / Mix ~10%.

## Chaining / placement
- **After a delay:** insert Decapitator *post-delay* to add overtones and analog
  character, taming the "too crisp" digital-delay sound.
- **Parallel via aux/send:** route to an aux instead of inserting, so you can stack
  more processing on the saturated copy without touching the dry.
- **Aliasing mitigation:** Decapitator lacks internal oversampling — apply HIGH
  CUT, keep saturation midrange-focused (on an aux), and/or work at higher sample
  rates.
