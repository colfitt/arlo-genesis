https://www.spencerbruce.com/blog1/logic-pro-x-the-secret-tape-saturation-plugin · https://whylogicprorules.com/saturation/ · https://boombox.io/blog/logic-pro-x-stock-plugins-hidden-gems/
spencerbruce.com (Neil Bruce) + whylogicprorules + boombox.io · community · current

# Stock lo-fi / tape saturation in Logic (no third-party needed for the "wrong" sound)

The user owns SketchCassette / RC-20 / Lossy, but Logic's STOCK tools already do
a lot of the degraded/tape aesthetic — useful before reaching for a plugin, and
free of AU-validation risk.

## The Tape Delay = secret tape saturator trick (Neil Bruce)
Logic's **Tape Delay** plugin is a tape emulation with the delay bolted on.
Kill the delay and you're left with the TAPE saturation + wow/flutter:
- **Dry = all the way DOWN, Wet = all the way UP.**
- **Delay time / Tempo Sync = 0 ms** (no delay).
- **Feedback = all the way DOWN.**
- Now the signal just passes through the tape stage. Add:
  - **Wow & Flutter** — subtle pitch modulation for vintage feel; "use sparingly."
  - **Clip Threshold** and **Tape Head Mode** — clip transients to increase
    saturation amount.
- Result: tape warmth + flutter from a plugin nobody thinks to use as a
  saturator. Stack heavier for the "recorded-wrong" wobble.

## Phat FX for fattening/saturation (whylogicprorules)
- Access via **Multi Effects > Phat FX**. Great on tracks, busses, or full mix.
- On a full mix: DON'T use all 3 distortion modes — turn **2 distortion knobs to
  0.0%** and set **one to "Soft Saturation."**
- Has bias/drive + its own filter/comp for thickening drones and beds.

## Other stock degrade tools (hidden gems)
- **Bitcrusher** — sample-rate/bit reduction for digital lo-fi.
- **Distortion / Overdrive / Clip Distortion** — Clip Distortion's filtered
  drive is good for grit on textures.
- **Ringshifter / Modulation > Ensemble/Chorus** — smear and detune for
  shoegaze width.

## Rig note
Chain into the live aesthetic: record clean → **Tape Delay (delay off)** for
flutter+warmth → **Bitcrusher** for digital decay → into a Summing Stack so a
whole texture layer degrades together. Then if you want MORE, bring in
SketchCassette/RC-20 (AU). Or reamp the clean track OUT through the End/Time→
Tape pedalboard (Big Time / Deco / Generation-Loss-style) for real tape.
