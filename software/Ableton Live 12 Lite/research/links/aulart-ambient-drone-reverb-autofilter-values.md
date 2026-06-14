https://www.aulart.com/blog/easy-ambient-drones-in-ableton-2/
aulart.com · Steve Angstrom · 2020-07-03

# Ambient drone — copyable Reverb + Auto Filter values (mostly Lite-safe)

The single most COPYABLE drone recipe found, with real numeric settings. Source
instrument is Suite (Operator) but the FX rack is stock and Lite-adaptable.

## Source instrument (SWAP for Lite)
- Original: **Operator** (Suite-only) — Saw osc, Coarse 1 / Fine 0, Level -12 dB,
  Attack 1.00 s / Decay 30.0 s / Release 7.00 s (slow, sustaining).
- **LITE SWAP:** use **Drift** (Lite's synth) — single saw osc, set Amp envelope to
  Attack ~1 s, very long Decay/Sustain at max, Release ~7 s for the same endless
  swell. OR hold a sustained sample in **Simpler** (loop region on). Either is Lite.

## Reverb (STOCK — IN LITE) — "frozen" lush tail
Per Reverb instance:
- Low/High Cut: Off
- Pre-Delay: 2.5 ms
- Spin: On, 0.10 Hz, amount 3.00
- Quality: High · Size: 100 · Stereo: 1000
- Diffusion: High ON / Low OFF · **Decay: 12.0 s** (huge)
- Freeze: Off · Flat: Off · Cut: On
- Chorus (in Reverb): 0.10 Hz, 0.05
- Reflect 0 dB · Diffuse 4 dB · **Wet: 100%**
(For a true infinite drone: turn Reverb FREEZE on to lock the tail forever — Lite
supports the Reverb device's Freeze button.)

## Auto Filter (STOCK — IN LITE) — 3 parallel filtered chains for movement
- LOW chain: Lowpass 12 dB · Freq 300 Hz · Res 8% · LFO Amount 20 · Triangle · Rate 6 bars
- MID chain: Morph 12 dB (73 lp/bp) · Freq 820 Hz · Res 4% · LFO 30 · Triangle · Rate 4 bars · Phase 120°
- HIGH chain: Morph 12 dB (39 bp/hp) · Freq 820 Hz · Res 4% · LFO 30 · Triangle · Rate 4 bars · Phase 120°
(Slow multi-bar LFOs = the evolving, breathing drone motion. All in Lite's Auto Filter.)

## Lite verdict
The whole FX side (Reverb freeze + 3x Auto Filter w/ slow LFOs) is 100% Lite-loadable
and copyable verbatim. Only the Operator source needs swapping to Drift/Simpler.
This is the reference "Lite drone" rack for the digest.

## Certainty
HIGH — explicit numeric settings from the tutorial. Reverb/Auto Filter confirmed in
Lite; Operator confirmed Suite (swap documented).
