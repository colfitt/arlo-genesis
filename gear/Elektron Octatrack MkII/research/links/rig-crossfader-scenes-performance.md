Manual: Octatrack MkII User Manual, §10.3 SCENES (p.53–54), §17.2.2 (p.108), §16.4 (p.100–101)
Elektron manual

# The crossfader as a rig performance tool — scenes that morph the live pedalboard

The contactless crossfader morphs between **Scene A** (fader left) and **Scene B** (fader right), interpolating every locked parameter in between. Each Part holds **16 scenes**; you assign two to the A/B slots. **Scene locks have priority over p-locks during a fade**, so morphs stay smooth. This is the OT's single most expressive control for the rig.

## Assign + lock
- Assign: **[SCENE A] + [TRIG n]**, **[SCENE B] + [TRIG m]**.
- Lock: hold the [SCENE] key, turn DATA ENTRY knobs — inverted graphics show locked values. Remove a lock: hold [SCENE] + press the knob.
- See which tracks/pages hold scene locks: hold a [SCENE] key → half-bright green [TRACK] keys; select one → green [PARAMETER] page keys.
- **Scene mute** ([FUNC]+[SCENE A/B]): temporarily ignore a scene's locks (snap back to the part's base values) — great for slamming a wash in/out.

## Equal-power volume locks (no center dip)
Special scene-only params for fades, visible **only while a [SCENE] key is held**:
- **XLV** — overlay on every track's LEVEL (post-FX). MIN = mute, MAX = pass at set LEVEL.
- **XVOL** — in AMP MAIN (pre-FX). MIN = mute, MAX = pass at set VOL.
- **XDIR AB / XDIR CD** — in MIXER, for the DIR-monitored inputs. MIN = mute, MAX = pass at set DIR.
Lock XLV=MAX on A / MIN on B for one track and the inverse on another → equal-energy crossfade with no dip at center.

## Rig performance moves (all on the live Thru-track wall + captures)
1. **Drone swell** — Scene A: track LEVEL/XLV low, FX dry. Scene B: XLV up, Dark Reverb mix up, freeze-delay feedback up. Slow fader push = the wall blooms into a wash.
2. **Filter sweep** — A: FX1 cutoff open. B: cutoff swept low + resonance high. The fader is a giant filter knob across the whole live pedalboard.
3. **Stutter / collapse** — A: clean Thru. B: Lo-Fi crush on, bit/SR low, freeze-delay capturing a fragment, fast LFO depth up. Snap the fader to shatter the wall.
4. **Clean ↔ destroyed capture** — A = live Thru track (clean wall), B = the sliced/re-pitched resample on another track, XLV-balanced. One gesture dissolves the real guitar into its mangled ghost (see rig-recipe-mangle-fuzz-wall.md).
5. **DJ-style A/B between two feeds** — pedalboard on A/B + a second feed (VG-800 / Apollo send) on C/D, each a Thru track; XLV/XDIR-locked so the fader hard-mixes between the two live sources (manual §16.4 method).

## Slice-morph (instant rhythm shapes)
Per §17.2.2: slice a loop (16 slices, SLIC=ON), sample trig per step, then lock **STRT = SL1** to Scene A and **STRT = SL16** to Scene B. The fader now sweeps which slices play across the bar — new rhythms by hand, live.
