Digitakt-2-User-Manual_ENG_OS1.15A_250708.pdf (§11.9–11.11 MOD/LFO pages) + manualslib DT LFO pages
elektron.se · Elektron official manual (OS 1.15A) · 2025-07-08

# DT2 — LFO MODE / SPH / FADE reference + the FADE→FM trick

The authoritative LFO-page param definitions, so the community LFO recipes (underrated-LFO
file, 59perlen, sample-slot scanning) can be entered exactly. Plus the documented FADE→FM
move. The DT2 has **3 LFOs per audio track** (2 per MIDI track).

## LFO page params (manual)
- **SPD** — speed, BIPOLAR (negative = LFO runs backward). **"Try 8, 16 or 32 to sync the
  LFO to straight beats."**
- **MULT** — multiplies SPD, either by current tempo (BPM) or by a fixed 120 BPM. High MULT
  (512 / 1k / 2k) pushes the LFO into audio rate.
- **FADE** — fade in/out of the LFO modulation, BIPOLAR **(−64 … 63)**: positive = fade-OUT,
  negative = fade-IN, 0 = none.
- **DEST** — modulation destination (SRC/FILTER/AMP params).
- **WAVE** — Triangle, Sine, Square, Sawtooth, Exponential, Ramp, **Random**.
- **SPH** — **Start Phase**: the point in the cycle where the LFO starts when trigged
  (the value you p-lock for the "reliably lock LFO start point" trick).
- **MODE** (Trig Mode):
  - **FREE** — runs continuously, never restarts (best for slow drone evolution).
  - **TRIG** — restarts from SPH on every note (per-hit variation; pair with Random wave).
  - **HOLD** — runs free in the background, but **latches/holds its output value at note-on
    until the next note** (this is what makes the square-wave polymetric-mute gate work).
  - **ONE** — runs one cycle then stops (use as a slow one-shot ENVELOPE, e.g. > the ~20 s
    AMP-envelope ceiling for very long swells).
  - **HALF** — runs half a cycle then stops.

## FADE → FM-style evolving tone (documented trick)
- Push **MULT very high (512 / 1k / 2k)** so the LFO hits AUDIO RATE, **DEST = Pitch**,
  **WAVE = Sine**, then use **FADE** so the modulation **evolves in over time** → a 2-operator-
  FM-style timbre that blooms (the carrier = your sample/single-cycle, the audio-rate LFO =
  the modulator). Frequency ratio is set by note pitch vs MULT/SPD; dial for harmonic vs
  clangorous metallic FM.

## Concrete community value worth pinning here
- **Humanizing percussion:** **DEST = AMP DEC (or ATK), WAVE = Random, MODE = HOLD,
  DEP = 0.10–4** (small) → each hit gets a slightly different envelope (per the underrated-LFO
  thread / manual HOLD behavior). Low depth is the key — big depth kills the hits.

NOTE: param ranges/definitions are manual-verbatim (FADE −64…63 is the one hard range).
The audio-rate-MULT + FADE = FM and the HOLD-latch gate are the two highest-leverage,
on-aesthetic LFO behaviors for this rig (metallic FM drones; self-muting polymetric walls).
