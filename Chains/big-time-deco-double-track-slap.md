---
type: chain
title: "Deco → Big Time Double-Track Slap Wall"
date: 2026-06-15
artists: [My Bloody Valentine, Cocteau Twins]
instrument: guitar
gear:
  - Chase Bliss Clean
  - Strymon Deco V2
  - Chase Bliss Big Time
---

# Deco → Big Time Double-Track Slap Wall

A tape-doubled, wobbling source hitting Big Time in its most underused voice — the **MOD range (3–46 ms)**, which is the pedal's slapback / chorus / flange engine, not a delay. At the short end it reads as a tight slap/double; push COLOR and FEEDBACK and the 3–46 ms taps start beating against the dry like a comb filter and then a flanger. Deco's doubletracker already laid down a second wobbling "player," so Big Time's MOD taps stack on top of an *already-doubled* source — the result is a wide, tape-thickened lead that gets gluier and more liquid the harder you push it.

🟣 DOUG-designed integration. No artist played this exact chain — the artists/taste-ref name the sound it chases. The only "real-artist signal order" invoked is the general doubling-before-delay logic; the per-unit patch refs carry their own provenance.

## Signal path

guitar → **CB Clean — "Transparent Enhancer"** (always-on ~2:1 thickener, slow attack keeps the pick alive) → **Strymon Deco V2 — "Watery Tape Chorus"** (tape-saturated doubletracker + heavy wobble = the doubled, woozy source) → **CB Big Time — "MOD Slap → Comb/Flange Double"** *(new patch)* (MODE Mod, short end = slap/double → push to comb → flange) → amp / interface.

Order is the whole point: Clean steadies the picking level first so the doubletracker reads even, **Deco doubles and wobbles the dry source**, and only then does Big Time's MOD engine multiply that already-doubled, already-moving signal. Put Big Time first and you'd just smear a flat note; doubling *into* the MOD taps is what makes the wall thicken instead of blur.

## Per-unit

- **CB Clean — "Transparent Enhancer":** Dynamics ~10–11:00 (~2:1, just into compression), **Attack SLOW (CW ~1:00)** so the pick transient escapes uncompressed, Release **R (Slow 1.5 s)**, Mode **Mid (Manual)**, all dips OFF, Dry OFF / Wet noon. This is the cleanest lead base in the rig — it thickens and extends the note without squashing the attack, so the doubletracker downstream sees a steady, even source instead of a spiky one. *Published character per the Clean manual's "Compression Ideas" Recipe 1; Sensitivity is set by ear to the left LED, not a sourced number.*
- **Strymon Deco V2 — "Watery Tape Chorus":** Tape Saturation ON (subtle, ~3/10), Doubletracker ON, Type **sum** (cleanest base for the wobble), **Lag Time ~6/10** (past noon = chorus zone, ~20–40 ms doubling), **Blend ~7/10** (favor the Lag deck so the warble is forward), **Wobble ~8/10 (heavy warble)**, Tone ~4/10 (dark-ish), DT Boost ~7/10. This is the "tape-doubled + wobbling" source: a second player at ~20–40 ms with real wow-and-flutter movement. If it gets seasick on held lead notes, drop Wobble toward 4/10 and Blend toward 5/10 for "doubling more than warble." **Honesty flag:** the patch's clock-faces are from a community 0–10 recipe (Guitar Chalk), not Strymon — A/B by ear. Mono out is fine here; the width comes from Big Time's MOD/SPREAD downstream.
- **CB Big Time — "MOD Slap → Comb/Flange Double"** *(new patch)*: **MODE Mod (3–46 ms)** — the headline. **STATE Compressed** (the SLAP/DOUBLE-style "burly expander" behavior — holds the doubled source together and adds room punch without disintegrating it), **VOICING Warm** (the primitive-digital "signature elliptical ripple" that makes the short taps sing), SCALE Off, **MOTION Sine slow** (tape-style drift on the short taps = the chorus/flange motion). **COLOR low–moderate ~30%** (a hot doubled source already has level; low COLOR keeps the limiter from clamping the slap to porridge — push it up to drive harder into the comb/flange), **TIME at the short end of MOD** for slap → roll up toward 46 ms as you want more chorus, **FEEDBACK ~35%** at the slap setting → climb toward 55–65% to feed the comb filter into flange, **CLUSTER low ~20%** (a touch of extra taps thickens the double without turning it into a wash), **TILT EQ above noon** (cut the doubled low-mid mud so the comb peaks read clearly), **SPREAD widen**, WET ~40%. *Numeric positions are a dialable recipe — Chase Bliss publishes character, not numbers; on recall the motorized faders fly to the saved positions and override these starting points.*

## Routing

Three boxes, mono in, stereo out from Big Time's SPREAD. **Gain-staging is the whole game.** Clean sets a steady picking level → Deco doubles and wobbles → Big Time's MOD engine multiplies. Keep Big Time's **COLOR modest** so its analog input preamp doesn't slam the analog limiter (STATE) and clamp the doubled slap flat — COLOR is also your "how hard into comb/flange" control: low = clean slap/double, high + high FEEDBACK = the 3–46 ms taps beat against the dry into a comb filter, then a flanger. **STATE Compressed (not Saturated)** is deliberate: the source is a clean doubled lead, not a fuzz wall, so you want the snappy expander/ducking behavior that keeps the slap articulate, not the disintegrating-mass voice. The single performance variable that thickens the wall is **FEEDBACK** (and a touch of COLOR) — that is the "thickens the more you push it" axis the concept is built around. If you want a pure wet MOD field with no centered dry note pinning the image, flip **DRY KILL ON** in Big Time's Options.

## Sound

A wide, tape-thickened lead: a doubled, gently-seasick source that arrives as a tight slapback, and — the harder you lean on COLOR/FEEDBACK — blooms into a liquid comb-filtered chorus and then a slow flange, all riding on Deco's wow-and-flutter. Two players become a small choir, then a swirling wall, off a single short-delay range nobody uses.

**Taste-ref:** My Bloody Valentine's pitch-bent, glued-double guitar thickness crossed with Cocteau Twins' liquid chorused haze (Robin Guthrie) — the doubled-and-wobbling lead, opened up wide. The Big Time "MOD mode is secretly a modulation pedal" move.

## Play

1. Set the Deco double first in mono — get an even, woozy doubled source (still articulate enough to hear the note, not a soup).
2. Start Big Time at the **short end of MOD with COLOR low / FEEDBACK ~35%** — confirm you hear a tight slap/double, not a delay.
3. Now **ride FEEDBACK up** (toward 55–65%) and nudge COLOR — listen for the taps starting to beat against the dry into a comb filter, then a flanger. That's the "thickens the more you push it" sweet spot.
4. Roll TIME from the short end toward 46 ms to move from slap → chorus; MOTION Sine adds the drift.
5. Play sustained chords or slow lead phrases so the MOD motion and Deco wobble have something to swirl. Hold MODE (2 s) to panic-reset Big Time back to a clean delay if the flange runs away.

## Sources

- **Basis:** 🟣 designed integration; chains **CB Clean "Transparent Enhancer"** + **Strymon Deco V2 "Watery Tape Chorus"** + new **CB Big Time "MOD Slap → Comb/Flange Double"**.
- **Big Time MOD range = slap/chorus/flange voice:** MODE spec "Mod (3–46 ms)" and factory presets **#1 COMPRESSED CHORUS** ("smooth modulation… dreamy… compressed to bring out the details"), **#2 SLAP/DOUBLE** ("a big, burly expander with two stages of clipping and room-like ambience… doubling and almost-real-time textures"), **#5 BROKEN DYNAFLANGE** ("a starved flanger… dynamic oscillations that react to your instrument's loudness") — `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` §spec + `research/links/cb-big-time-factory-presets-recipes.md`.
- **COLOR/FEEDBACK gain-structure (low COLOR = clean, push to drive into the limiter; FEEDBACK is the climb):** manual pp.24–25 quoted in the factory-presets recipe file; Warm voicing "signature elliptical ripple" and TILT-EQ-up to cut mud per manual pp.38–39 (same file).
- **Clean "Transparent Enhancer":** Clean manual p.22 "Compression Ideas" Recipe 1 (subtle 2:1, slow attack = uncompressed pick).
- **Deco "Watery Tape Chorus":** community 0–10 recipe (Guitar Chalk) cross-checked against Pete Celi's "Lag past noon = chorus zone" (`Patches/Strymon Deco V2/watery-tape-chorus.md`) — QC-flagged, A/B by ear.
- `Research/Taste-Profile/taste-profile.md` (wall / tape-thickness / making-aesthetic lens).
