# GK-5 Calibration Profile — Baritone Jazzmaster

**Save as: GK SET SELECT slot 2, NAME "BARI JM"** (System → GK SETTING; persists through power-off). This is the easier of the two — home turf for a divided pickup — with one wrinkle: it's a *baritone*, so the GK is reading lower fundamentals than a standard guitar and the low slow strings are where wobble lives. Grounded in the VG-800 GK SETTING page (SCALE presets incl. **LP 628 mm**, SENS 1–7, DISTANCE 10–30 mm, GAIN 1–4) + MusicRadar's documented low-string wobble.

## GK SETTING values (starting point)
| Parameter | Value | Why |
|---|---|---|
| GK TYPE | **GK-5** | Match the pickup |
| SCALE | **LP (628 mm)** or the closest preset *above* it | Baritone scale is long (typically 27–30"). Pick the **longest** preset available and audition; the SCALE preset helps the tracker expect the lower-tension, longer strings. If the low strings still wobble, this is the first knob — *inference, verify by ear; there is no dedicated baritone preset.* |
| PU DIRECTION | **NORMAL** / REVERSE — match physical mount | — |
| DISTANCE 1–6 | **~12 mm** highs, **raise toward 15–18 mm on the low strings** | Low baritone strings have big, slow excursions; too close = the element sees an unstable waveform = wobble/octave errors. Backing the low strings off stabilizes them. |
| SENS (per string) | highs **~75–80**, **lows lower (~60–70)** | The classic fix: low slow strings over-trigger. Lower their SENS. |
| GAIN | **2–3** | Lower if strong picking on the low strings distorts the divided input |

## The low-string wobble fix (the one documented issue)
This is the exact symptom MusicRadar hit ("wobble on the low strings"). Fix order:
1. **Lower SENS** on the offending low string(s) in steps of 5.
2. **Raise DISTANCE** on those strings (element further from the string = cleaner fundamental, less harmonic confusion).
3. **Lower GAIN** globally if heavy picking is the trigger.
4. **SCALE up** a preset — a longer SCALE expectation reduces low-string pitch confusion.
5. Pick **nearer the bridge** when tracking accuracy matters (tighter, more periodic waveform for the tracker).

## Subterranean tuning without retuning (the doom payoff)
- INST → **ALT TUNE SW ON**, ALT TUNE MODE **ALT TUNE**, ALT TUNE TYPE **-12–+12 STEP** set to **-5 or -7** → instantly drops the *whole* baritone into genuinely cave-deep territory with the magnetic pickup left at its real tuning.
- Or **DROP D–A** / **OPEN D/E/G/A** for drone-friendly open tunings (open strings ring a major chord → ideal pedal-point doom).
- **USER** tuning lets you set each string's PITCH 1–6 (±24 semitones) for custom drones (e.g. low strings to a unison/fifth pedal, high strings to the melody).
- Note: extreme ±STEP shifts artifact — into the Hizumitas wall that's a feature.

## What tracks well vs poorly
- **Well:** everything a standard guitar tracks, plus the low fundamentals once calibrated. Bends, chords, leads all solid (the JM is the reliable workhorse vs the banjo).
- **Poorly (relatively):** very low ±STEP target tunings stack two pitch-shifts (string already low + big downshift) → expect more artifacts the lower you go. Calibrate at the *played* tuning, not the shifted one.

## Companion settings
- INST common: **NORMAL MIX ON ~30%** keeps the real Jazzmaster body/character under the model (dossier §6).
- GUITAR-TO-MIDI shared logic (both instruments): MONO mode = one MIDI channel **per string** (lets the Digitakt/Octatrack/MPC assign different sounds per string, and pass pitch-bend); POLY = all strings on one channel (simpler, single timbre). PLAY FEEL **FEEL2–4** for natural dynamics or **NO DYNA + NO DYNA VELOCITY ~100** for uniform triggering; **LOW VELO CUT 1–4** so light touches don't false-trigger; **BEND RANGE 12–24** if you want bends to read; HOLD **HOLD1** to keep notes ringing across re-picks (banjo especially). DYNAMICS 1–10 raises trigger-ease for higher velocities.
