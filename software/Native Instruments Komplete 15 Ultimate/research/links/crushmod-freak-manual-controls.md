https://native-instruments.com/ni-tech-manuals/crush-pack-manual/en/freak
native-instruments.com · NI Tech Manual — Crush Pack: FREAK · current

# FREAK — full control reference (from the manual)

Frequency shifter / ring mod / AM-radio modeler on an analog diode-ring model. **NOT confirmed installed on disk.**

## Common controls (all modes)
- **Type:** morphs **AMP (amplitude mod) → RING (ring mod) → FREQ (frequency shifting)** continuously. RING at low rates = subtle phasing/distortion; at audio rates = sidebands replace the harmonic content → metallic, inharmonic.
- **Harmonics:** intensity of harmonic overtones / sidebands.
- **Feedback:** output→input feedback level (in Radio mode it also controls noise amount).
- **Mix:** equal-power dry↔wet.

## FX Modes (re-task the three left knobs)
**Oscillator mode** (internal sine):
- **Freq:** bipolar modulation rate. Range switch: **ON = ±5000 Hz (coarse), OFF = ±200 Hz (fine).**
- **Stereo:** L/R phase offset → width.
- **Antifold:** reduces sub-0 Hz sideband folding when up → cleaner but thinner lows.

**Radio mode** (AM-radio model):
- **Width:** band-pass bandwidth for demodulation (narrow = strong character, wide = cleaner).
- **Tuning:** AM-radio tuning — center = best reception; off-center = interference.
- **Carrier:** demodulation frequency (higher = better quality).
- **Demod:** product (aggressive) vs. envelope (vintage AM) circuit.
- **Gate:** noise gate.

**Sidechain mode:**
- **Release:** envelope-follower smoothing (low = quick, high = slow).
- **Contour:** blend of direct signal vs. envelope-follower-processed signal.
- **BP Freq:** band-pass cutoff to select the modulation-source frequency band.
- **SC:** external sidechain input vs. self-modulation (off = input modulates itself → distortion).

No numeric ranges for Harmonics/Feedback; (Komplete-Now demo says Freak ships 79 presets; "Old School Maker" is one).
