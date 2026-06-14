https://www.izotope.com/en/learn/advanced-mastering-tips.html
izotope.com (Learn) · "5 Advanced Mastering Tips Using Ozone" · iZotope

Power-user Dynamics/EQ/Imager tricks. Most of these are about adding life BACK rather
than crushing — directly relevant to degraded/dynamic music you don't want squashed.

## 1. Multiband Upward Expansion (put transients back)
- In the Dynamics module, drop the Limiter ratio BELOW 1.0:1 to turn it into an upward
  expander. Set Compressor ratio to 1.0:1 and threshold to -130 dB to bypass it.
- Use 3-4 bands (kick thump, snare body, mid percussion, high cymbals). Fast attack
  0.5-10 ms, release 50-100 ms.
- Goal: "inject a little life back" into over-compressed mixes by poking transients out
  WITHOUT crushing body. (Useful on a flat/over-limited drone bounce.)

## 2. Multiband Upward Compression (lift quiet parts)
- Compressor ratio below 1.0:1 boosts signal below the threshold. Thresholds rise from
  silence upward, stopping before transients enter.
- CAUTION: "there is no limit on the amount of gain applied below the threshold" — automate
  output to avoid "dynamic inversion" (soft parts ending up louder than loud parts).

## 3. Complex Transfer Curves
- Dynamics supports layered behavior: upward compression + downward expansion, approximate
  parallel compression, extended soft-knee (vintage-tube-like). Different ratios/thresholds/
  time-constants per section.

## 4. Mixed-Phase EQ
- Turn on the digital EQ mode; the phase slider blends linear (0%) <-> minimum (100%) phase.
  Linear preserves spatial definition; minimum creates more diffuse imaging. Especially
  useful for mid/side where phase wrecks stereo cohesion. (For a smeared wall, leaning
  minimum-phase adds diffusion.)

## 5. Transient-Sustain Imaging
- Imager's Transient/Sustain mode: width the attack vs the sustained/ambient portion
  independently, per band. Narrow transients while widening body — or the reverse. Lets
  you widen the SUSTAIN (the wall/tails) without smearing the few transients.
