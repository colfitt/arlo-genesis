Manual: Octatrack MkII User Manual, §16.1.2 (p.97), §17.5 (p.111), §10.3 SCENES (p.53–54), §9.2 (p.47)
Elektron manual

# RECIPE — "Live-mangle the fuzz wall"

The rig-defining patch. Pedalboard's stereo fuzz wall (Longsword / MXR 108 Fuzz / Brothers AM stacks → through Boards 2/3) flows live through the Octatrack's FX, and the crossfader morphs between the clean wall and a destroyed version.

## Patch
- Pedalboard stereo print → OT **inputs A/B**.
- MIXER: **DIR AB = 0**, AB GAIN to taste (so `<REC>` LEDs sit healthy, not clipping).

## Build
1. **Track 1 = Thru machine**, INAB = A B. One sample trig on step 1. (Full setup: thru-machine-live-fx-setup.md.)
2. **FX1 = multimode filter**, **FX2 = Echo Freeze Delay** (tempo-synced to project BPM).
3. **LFO 1 → FX1 cutoff**, slow triangle — the wall breathes.
4. (Optional capture layer) **Track 2 = Flex machine**, assign **recorder buffer 1**. Drop a **recorder trig** on track 1 (or [TRACK 1]+[REC1] manually) to grab ~16 s of the wall into buffer 1; auto-slice it (see resample-the-rig-master-track.md). Track 2 now plays the *sliced/re-pitched* capture.

## Scene the crossfader (the performance)
Assign Scene A = [SCENE A]+[TRIG 1]; Scene B = [SCENE B]+[TRIG 2].
- **Scene A (fader left) = the clean live wall:** Thru track FX mild, filter open, freeze-delay feedback low.
- **Scene B (fader right) = the ruined wall:** hold [SCENE B], turn knobs to lock — filter cutoff swept down + high resonance, Lo-Fi crush on, freeze-delay feedback near max, LFO depth up. Scene locks interpolate smoothly, and **scene locks have priority over p-locks** during a fade so the transition stays clean.
- Pull the fader from L→R live: a clean drone collapses into a filtered, crushed, frozen smear. That one gesture is the whole performance.

## Equal-power level (avoid the center dip)
If you crossfade between the live Thru track (track 1) and the sliced capture (track 2), lock **XLV** per track so there's no volume dip at fader-center:
- Track 1: hold [SCENE A], LEVEL knob → **XLV = MAX**; hold [SCENE B] → **XLV = MIN**.
- Track 2: hold [SCENE A] → **XLV = MIN**; hold [SCENE B] → **XLV = MAX**.
- Now A = clean wall only, B = mangled capture only, center = equal-power blend.

## Stutter variant
On the Thru track, set track length short (e.g. 1/16 scale) and use **conditional/probability trigs** + **micro-timing** to gate the incoming wall rhythmically. Or p-lock the freeze-delay to capture-and-repeat a fragment on specific steps. LFO → FX cutoff at a fast rate = tremolo/glitch on the wall.

## Aesthetic notes
Sustained fuzz/drone is ideal OT food — dense, no transient gaps, so the freeze delay and filter sweeps stay smooth. This is "degraded, recorded-wrong, sustained wall" made *performable and repeatable* rather than accidental.
