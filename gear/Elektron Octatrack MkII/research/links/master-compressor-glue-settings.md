https://www.elektronauts.com/t/glue-compressor-settings-for-octatrack/54758
Elektronauts · users previewlounge, konputa · Apr 2018 · thread "Glue Compressor settings for Octatrack"

# OT COMPRESSOR — three concrete starting patches (master glue + per-track)

The OT's compressor (FX block, on track 8/master or any track) with real posted values. The DeepResearch/UsageGuide mention the master comp as glue but had no numbers; these are starting points.

## 1. "Glue" — full-mix / master-track 8 (previewlounge)
- **ATT = 24, REL = 86, THR (thrs) = 50, RATIO = 45, GAIN = 8, MIX = 112**
- Use: whole mix or master track 8. Described as making everything "tighter, funkier, more pro." MIX=112 (not 127) = slightly parallel so transients survive.

## 2. Snare/transient pop — single track (konputa)
- **ATK = 9, REL = 30, THR = 5, RAT = 73, GAIN = 59, MIX = 127**
- Fast attack, high ratio, low threshold = aggressive transient squash (TR-707 snare). Heavy makeup gain (59).

## 3. Bassline punch — single track (previewlounge, Track 5)
- **ATK = 27, REL = 96, THR = 43, RATIO = 34, GAIN = 6, MIX = 77**
- **RMS = 76** (double-click FX1 to reach RMS/peak mode — higher = RMS/smoother, lower = peak/snappier)
- **Track VOL = -14** — note: track volume is BEFORE the compressor, so it sets how hard you hit it.

## Key gotchas (previewlounge)
- **Individual track VOLUME is pre-FX** → it drives the compressor; lower track vol = less compression even at same threshold.
- The **RMS** parameter (FX1 detail page) switches Peak↔RMS character.

## Rig fit
For the rig the master-glue patch (#1) on track 8 is the relevant one — but recall the existing resampling trap: when capturing through track 8 it re-compresses. Use patch #1 for final glue, and scene-lock **Comp MIX = 0** (or resample via CUE) when sampling. For sustained walls a gentler version (raise THR, lower RATIO toward #3's 34) keeps the drone from pumping; MIX 77–112 = parallel so the wall doesn't choke.

PROVENANCE: community (Elektronauts, cited per-user). Genre-specific (techno/funk) starting points — soften for drone/doom (higher threshold, lower ratio, slower attack).
