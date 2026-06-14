https://www.elektronauts.com/t/dt2-single-cycle-waves/214718
elektronauts.com · community thread (Billy1992, Humanprogram, OldmanChompski) · 2024

# DT2 — single-cycle waveforms as a synth OSCILLATOR / drone source

Turns the DT2 into a playable subtractive/wavetable synth from tiny single-cycle WAV files —
i.e. an oscillator for the banjo-register lead and for sustained drone beds, no sampling of
the rig required. Most parameter-specific single-cycle thread found. Authors in parentheses.

## Source material
- **Adventure Kid Waveforms (AKWF)** — free, **2000+ single-cycle WAVs** — the recommended
  library (Billy1992). Plus the DT2 factory wavetables.
- Load several single-cycles as a **sample chain** for a multi-wave palette on one track.

## Core oscillator setup (Humanprogram)
- **SRC machine = Grid**, put the factory wavetables / AKWF chain in it, **LFO → grid SLOT**
  to sweep through the waveforms — "produces better results" than scanning sample-start.
- Play **chromatically** across the trig keys; keytracking gives true pitch.

## Billy1992's concrete synth tricks ★
- **Pseudo-wavetable / pseudo-PWM:** set the **sample LENGTH to 60 or 30** (very short) and
  **modulate the sample START** with an LFO → the playback window sweeps the cycle = a PWM/
  wavetable-scan timbre from one static single-cycle.
- **Fake extra oscillators with the comb filter:** **Comb+ with HIGH FEEDBACK and filter
  KEYTRACK = 100%** → the comb's tuned resonance adds a second pitched voice that tracks the
  note, mimicking a multi-osc synth. (Ties straight into the comb/banjo-resonator recipe.)
- **Built-in drive chain:** "**BR, Overdrive and SRR are applied just after the sample
  reading**" (pre-filter) — so crush/drive the raw single-cycle BEFORE the comb/filter for a
  grittier oscillator. Use **LFOs as LFOs OR as envelopes** on these to shape the wave live.

## Multi-osc by resampling (OldmanChompski)
- Sample **two single-cycles onto two tracks**, then **resample the combined pattern** back
  into one slot → a stacked multi-oscillator tone living in a single sound slot (frees voices
  for a thicker drone stack).

## Rig fit
- AKWF single-cycle + Grid + LFO→slot + **Comb+ keytrack 100% / high FDBK** = a tuned,
  detunable drone oscillator that pairs with or doubles the banjo lead. Set **AMP DECAY = INF**
  (per the drone files) to hold it as a bed; modulate sample-START (length 30/60) for the slow
  PWM shimmer.

NOTE: concrete values quoted = sample LENGTH 30/60, comb KEYTRACK 100% + high FDBK, AKWF
2000+ waves. The Grid-slot-LFO sweep and the pre-filter BR/OD/SRR ordering are manual-
consistent (FX page sits before the filter machine on the voice path).
