https://www.youtube.com/watch?v=b8byOjJYUug
ARTFX · "Is this the best analog saturation VST plugin?" (Soundtoys 5 Decapitator) · 2016-10-31 (31:21)

(Auto-caption transcript, cleaned to prose. The longest, most source-by-source demo:
walks Decapitator across a drum loop, bass, electric piano, piano, and a full mix —
the most copyable "what style on what source + why" walkthrough.)

Decapitator is Soundtoys' dedicated saturation plugin — used to thicken sounds, make
things louder/fuller. Soundtoys emulated analog gear with it, and it reacts and is
dynamic to whatever you send it. The project is a drum loop, a bass line, an electric
piano, and a regular piano.

**The five styles (modeled hardware + use):**
- **A — Ampex 350 tape recorder (1950s).** Models the *preamp* (people pulled the
  preamp out of the tape machine and rewired it). Sounds good on **drums**, and great
  on **vocals** ("I've been using style A a lot on vocals recently"). Might also suit a
  **full mix** since it's a preamp.
- **E — Chandler TG Channel.** A channel-strip (preamp + EQ). Distinctive sound: a
  **beefy low end** but a smooth/nice high end. Good on drums too, BUT it adds a lot of
  beefy low end, so if your drums already have warmth/low end it can over-beef and
  trigger the saturation harder than you want. **On drums with already-strong low end,
  prefer A.**
- **N — Neve 1057 input channel.** Early Neve preamp built around **German transistors**
  — distinctive sound, fills out the frequency profile, good for taming brightness.
- **T — Culture Vulture, triode setting.** First real dedicated studio distortion
  device (not just for guitar). Triode = overdriven tube sound. Soundtoys' manual says
  it's good for **drums**: not too much beefy low end, high end stays clear, transients
  stay clean with good saturation.
- **P — Culture Vulture, pentode setting.** **Adds only ODD harmonics** — sounds
  completely different from T. Sounds great on **guitars/instruments** vs T (better on
  drums). Ultimately trial and error.

**Controls.**
- **Drive** = input gain into the saturation. Up = harder into the distortion. Same as
  driving input on analog gear into the transistors/preamp/tubes.
- **Auto** (on by default, switch at top) = auto output compensation. As you raise
  drive, output drops; each style compensates a different amount. Turn off to set output
  manually.
- **Punish** = **another 20 dB boost to the drive**. With Punish on and drive at 0 you're
  already +20 dB into the input, plus up to ~10 dB more on the drive knob. Lets you do
  gigantic amounts of distortion (e.g. a heavy guitar).
- **Attitude VU meter** = just shows level/how hard you're driving; not the unit's output.
- **Output** = manual output trim (used when Auto is off).
- **Low Cut** = cuts lows (clean up post-saturation mud). **Thump** = a small volume boost
  right at the low-cut cutoff frequency — set low cut to ~20 Hz and Thump on to add weight
  if the saturated sound feels thin.
- **Tone** = general dark/bright color shaping.
- **High Cut** = cuts highs. **Steep** switch: OFF = 6 dB/oct gentle high cut, ON = **30
  dB/oct** much steeper, more abrupt — colors the sound and emulates a cab-ish rolloff.
- **Mix** = parallel saturation. Smash the drum loop hard, then blend in the original
  unaffected loop — no complex routing/racks needed.

**Source-by-source (the actual settings demonstrated):**
- **DRUMS:** Start with **T** (Soundtoys' recommended drum style), add a good amount of
  **drive**, then use **Mix** to blend wet/dry because the drum loop has a lot of dynamic
  range — this glues it and brings up the quiet elements. Then he layers a second instance:
  one on **A with Punish on, drive backed down**, and a second on **T (no Punish)**,
  grouped — before/after, the drums get a lot louder and fuller.
- **BASS:** Audition styles, settles on **E**, raises **low cut** to tighten, brings
  **tone** down a touch to lose some highs, and lowers the **high cut** a bit (it was a
  little too much).
- **ELECTRIC PIANO:** Add a lot of drive, then a lot of **low cut** to kill the muddy low
  end; auditions styles (T is the most transparent/clean), keeps the first style, backs
  the **mix** down a bit.
- **PIANO:** It distorts a lot because piano is percussive — only the loud attack triggers
  the saturation, so raise drive to saturate more of the sustain. Back the drive way down,
  raise **low cut** for the muddy low end, back the **mix** down — keep it fairly clean, a
  piano shouldn't be heavily distorted.
- **FULL MIX:** **T** mode is the most transparent — on a full mix it just adds a little
  volume and saturation that gels everything together.
