https://www.musicradar.com/how-to/how-to-synthesize-an-old-school-rave-pad-using-arturias-dx7-v
musicradar.com · "How to synthesize an old-school rave pad using Arturia's DX7 V" · accessed 2026-06-11
(+ Arturia DX7 V sound-design notes, KVR "mid/late 80s bell synth" thread)

DX7 V = the alien, glassy FM shimmer of the Yamaha DX7. Concrete recipes.

## Glassy/gritty rave-pad recipe (MusicRadar, step-by-step)
1. Init a default DX7 V patch.
2. **Operator 1 waveform → "Rounded Saw"** (more harmonics than the default sine).
3. **Operator 2**: Output level **80**, Coarse tuning **2** (= +1 octave),
   waveform **"Additive 3"** (less shrill, grittier).
4. **Filter**: Bandpass, Cutoff **~2–3 kHz**, Resonance **~20%**.
5. **Op 1 DADSR envelope**: Attack **~2** (slow), Peak **~0.7**, raise **Release**
   so chords blend.
6. **Mod Matrix / LFO1**: LFO1 → Op 2 Detune at **−0.10**; LFO1 → Op 2 Cutoff at
   **+0.10** (subtle motion/animation).
7. **Filter swell**: assign **Mod Env 1 fully → Op 1 Filter**; Op 1 Filter cutoff
   **3 kHz**; Mod Env 1 with **long Attack + medium Sustain** → filter opens
   gradually through each chord (key to the "less abrasive" pad).

## Bell recipe (KVR community / classic FM)
- **Modulator frequency = 3.5× carrier frequency** for the inharmonic bell ring.
- Modulator level + envelopes to taste (**long decay/release on the modulator**).
- Fuller bell: add a sine or low-filtered saw **an octave below** the carrier.

## Ambient-FM design philosophy (Arturia)
- Find a great operator sound **without envelopes first** — just tune the
  **ratios**; make the raw ingredient great before shaping.
- **Added delay + reverb make FM excellent for ambient** ("Boards of Canada an
  obvious inspiration").
- DX7 V extras over hardware: extra mod sources + **MSEG envelopes** to draw
  precise shapes — vital because small level/rate changes hugely shift FM timbre.
