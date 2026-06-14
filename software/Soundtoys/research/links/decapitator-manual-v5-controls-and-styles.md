https://www.soundtoys.com/wp-content/uploads/Decapitator-Manual.pdf
soundtoys.com · "Decapitator User's Guide, Version 5" · 2015 (the authoritative reference)

Extracted from the official v5 manual (PDF → text). This is the canonical source for the
style descriptions, the signal-chain order, and the exact control behaviors.

## The 5 styles (verbatim sense of the manual)

- **A — Ampex 350 tape-drive preamp.** Iconic 1950s tape recorder, a studio fixture at
  Sun, Stax, Motown, and Chess. Preamp sections were often pulled out, rewired and used as
  standalone mic pres (Soundtoys has several). Designed for ribbon mics → a jaw-dropping
  amount of gain. **"The best way to describe the tube-driven distortion of the Ampex 350 is
  ultra-ultra-smooth."**
- **E — Chandler/EMI TG Channel.** Wade Goeke's (Chandler Designs) gear based on the vintage
  EMI/Abbey Road consoles. **"A beefy low end coupled with a smooth but airy top-end sheen"**
  — excellent mic preamp, DI and EQ, loads of character.
- **N — Neve 1057 input channel.** Early Neve, very different from the later/ubiquitous 1073.
  Built around **Germanium transistors** (think vintage Fuzz Face) → a unique, distinctive
  sound, **especially on guitars.** "A weighty but solid low end with focused but not narrow
  mids, just begging for the needle to be pegged to hear those Germaniums sing."
- **T — Thermionic Culture Vulture, triode setting.** The first dedicated studio (not just
  guitar) distortion device. Models an overdriven **triode** tube. **"Triodes typically add
  loads of EVEN harmonic distortion."** Warm and punchy — **"especially useful to add some
  attitude to drums or other percussive instruments."**
- **P — Thermionic Culture Vulture, pentode setting.** Models an overdriven **pentode** tube
  (output stage of guitar/other amps). **"Usually characterized by ODD harmonic distortion,"**
  a different sound from the more-even triode designs.

## Signal-chain order (manual-confirmed)

`Tone + Low Cut + Thump (PRE) → [SATURATION: Style + Drive + Punish] → High Cut + Steep (POST) → Output/Auto → Mix`

- **Low Cut** removes lows **before** they hit the saturation circuit — prevents "flabbiness"
  when distorting bass-heavy sources. **"At extreme settings you can get some very low-fi
  telephone and AM radio effects, especially when used together with the High Cut control."**
  (← the manual's own lo-fi / "recorded-wrong" recipe: aggressive Low Cut + aggressive High
  Cut = bandpassed telephone/AM-radio tone.)
- **Thump** = a few dB low-frequency boost right at the Low Cut frequency, like the **"head
  bump" of analog tape** — one reason tape sounds fat. It increases the lows hitting the
  saturation circuit (can add flab or sound incredible depending on the Low Cut setting).
- **Tone** = a very gentle sloping EQ / **tilt EQ** (like an old AM-radio tone control): Dark
  boosts lows + attenuates highs; Bright cuts lows + boosts highs. It is **pre-saturation**,
  so it changes WHICH frequencies get distorted — a dramatic effect.
- **High Cut** removes high frequencies and operates **AFTER the saturation** — for taming
  "fizzy" distortion artifacts (in contrast to Low Cut and Tone, which are pre-saturation).
- **Steep** = High Cut slope: OFF = gentle **6 dB/oct**; ON = super-steep **30 dB/oct**.
  Useful for emulating a guitar speaker cab / direct-to-board guitar.
- **Drive** = input control into the analog circuit; harder push → more saturation; the
  distortion character depends entirely on the Style. It is a gain control, so it raises the
  output level (compensate via Output or Auto).
- **Punish** = **"adds an extra 20 dB of gain"** → "things will get loud, brutal, distorted."
  Each analog style "screams out in beautiful agony differently when punished."
- **Output** = manual output trim (used when Auto is off).
- **Auto** = Auto-Gain: automatically turns the output DOWN as you raise Drive (the Output
  knob moves opposite to Drive). On by default.
- **Mix** = balance of original vs processed → parallel saturation **"without the need for
  routing or submixes."** "A great trick to restore the transients of your original sound
  that get chopped off by the saturation stage" — similar to parallel compression.
- **Attitude Meter** = a responsive VU (modeled on a vintage Simpson VU as in the Ampex 35X)
  that shows level relative to Drive — it does **NOT** measure Decapitator's output.

## Manual's own use hints
- T → drums / percussive instruments (attitude).
- N → guitars (Germanium character).
- A → ultra-ultra-smooth color, anything.
- Low Cut + High Cut (extreme) → telephone / AM-radio lo-fi.
- Steep + High Cut 4-5 kHz → guitar cab / direct-to-board emulation.
