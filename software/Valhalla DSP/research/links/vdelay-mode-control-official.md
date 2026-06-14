https://valhalladsp.com/2019/04/16/valhalladelay-the-mode-control/
valhalladsp.com · Sean Costello · official "The MODE Control"

The MODE control = the base delay algorithm. (ERA = sub-variations within a mode.)

## The modes
- **Tape** — detailed model of RE-201/RE-301 tape echo. **Wow/flutter rate is a function
  of the delay time** (authentic — faster delay = different warble), and so is the EQ.
  Age adds asperity noise + tape splice artifacts. MOD Wow/Flutter scale the amount of
  "wear." Three eras: Past/Present = darker, noisier; Future = refined/cleaner.
- **HiFi** — a "higher-fidelity" tape echo (reel-to-reel-in-a-studio vibe). Unlike Tape,
  modulation rate/depth are **independent of delay time** (you control them directly). Age
  adds asperity noise but NO splice artifacts. Cleaner than Tape.
- **BBD** — bucket-brigade (analog) delay model: characteristic artifacts + limited high
  end. MOD Rate/Depth = a smoothed triangle LFO for subtle vibrato / pitch slews. Higher
  Drive → compander ducking. Eras from dark-vintage → brighter Future.
- **Digital** — based on 1980s units with "floating-point converters" = a bit of grit +
  smooth delay. **Age controls bit resolution; 50% ≈ 12-bit** (the lo-fi crunch knob).
- **Ghost** — analog delay + **frequency shifting** (FREQ Shift/Detune). The repeats grow
  "increasingly enharmonic and metallic as they decay." Three diffusion ERAs (Past =
  standard; Present = some frequency-dependence; Future = far more) = the spectral-shimmer
  wash. ★ Valhalla's answer to the "spectral shimmer in the feedback" delay.
- **Pitch** — digital delay + **pitch shifting in semitones** in the feedback (PITCH
  Shift/Detune). Set to +12 = a shimmer-DELAY (octave climbing repeats, like Shimmer but
  on the delay engine); detune in cents = micropitch/doubling.
- **RevPitch** — reverses AND pitch-shifts the input (adjustable splice size) = reverse-
  pitch swooshes.

## Takeaway for this rig
For the tape/lo-fi aesthetic: **Tape** (RE-201 with wear) or **BBD/Digital** for grittier
character. For ambient walls: **Ghost** (spectral metallic shimmer wash) and **Pitch +12**
(octave shimmer-delay). The mode picks the *flavor of degradation* baked into every repeat.
