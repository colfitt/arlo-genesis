https://valhalladsp.com/2020/05/06/valhallasupermassive-the-controls/
valhalladsp.com · Sean Costello · 2020-05-06

# Valhalla Supermassive — The Controls (authoritative)

The official control reference from Valhalla's own blog. Supermassive is a
**feedback-delay-network (FDN)** delay/reverb hybrid — every "mode" is a different
FDN topology with different attack/sustain/decay character.

- **MODE** — selects the algorithm. *"The most powerful Supermassive control"* because
  the algorithms have very different **attack, sustain, and decay** characteristics.
- **MIX** — wet/dry. 0% dry, 100% wet. Has a **Mix Lock** so the mix stays put when you
  browse presets or run it as a 100%-wet send.
- **WIDTH** — output width. 100% = max width, 0% = mono, **negative values swap L/R.**
- **DELAY** — length of the longest delay line in the FDN, in ms. Whether you hear
  discrete echoes depends on MODE and WARP.
- **DELAY SYNC** — time unit: ms, notes, dotted, or triplets (tempo-sync).
- **WARP** — scales the delay lengths *relative* to DELAY. Behaviour by range:
  - **0%** — all delays = the DELAY length (cleanest discrete echoes).
  - **5–15%** — *"harmonic delays"*; resonances shift *downwards* as the sound decays.
  - **20–50%** — *"delay clusters where the initial delay is smeared, and repeats
    gradually become more reverberant."*
  - **>50%** — fully reverberant.
- **FEEDBACK** — amount of feedback around the delays in the FDN. Larger = longer decay;
  can affect initial attack time in some modes. (At 100% = infinite — see infinite post.)
- **DENSITY** — perceived number of echoes; changes how the delays mix together. **0% =
  delays isolated** (discrete); **100% = all delays fully mixed** (conventional reverb).
  Also increases L/R crossfeed.
- **MOD RATE** — rate of delay-length modulation, in Hz. A multi-phase sinusoidal
  oscillator → lush chorusing / ensemble.
- **MOD DEPTH** — depth of the modulation; depth auto-scales with Mod Rate so faster mod
  doesn't go "out of tune." **0% = drier and makes WARP artifacts more audible.**
- **EQ HIGH CUT** — −6 dB/oct low-pass on the OUTPUT of the FDN.
- **EQ LOW CUT** — −6 dB/oct high-pass on the OUTPUT of the FDN.
  ★ **Both EQ filters are OUTSIDE the feedback loop** — so they shape the output without
  the tail darkening/thinning over time. (This is *why* infinite drones stay full — see
  the infinite-reverb post.)
