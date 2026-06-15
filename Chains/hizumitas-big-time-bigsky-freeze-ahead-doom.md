---
type: chain
title: "Hizumitas → Big Time → Big Sky Freeze-Ahead Doom"
date: 2026-06-15
artists: [Swans, Boris]
instrument: baritone / guitar
gear:
  - EarthQuaker Devices Hizumitas
  - Chase Bliss Big Time
  - Strymon Big Sky
---

# Hizumitas → Big Time → Big Sky Freeze-Ahead Doom

The inverted build. Every other doom wall here grows from the bottom up: you hit a fuzz chord and the space arrives *after*, blooming out of the note. This one runs the order backwards. You lay the cathedral FIRST — swell a single chord into the Big Sky and FREEZE it into a held, empty-feeling pad — and only *then* bring up the Hizumitas-and-Big-Time wall, which rises into a space that already exists. Space before sound. The frozen reverb is the room; the fuzz-and-delay wall is what walks into it.

🟣 DOUG-designed integration. No artist played this exact chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases. The move it's built on (a reverb frozen *ahead* of the source) is the documented Antoine Michaud FREEZE behavior, repurposed: instead of freezing to solo a clean lead over the pad, we freeze to give a doom wall a pre-built cathedral to swell into.

## Signal path

Baritone / guitar → **EQD Hizumitas — "Doom Wall (max heavy)"** → **CB Big Time — "Hizumitas Fuzz Wall"** (IN-L auto-**MISO** mono→stereo, MODE Long, STATE Compressed, FREEZE bed) → **Strymon Big Sky — "Freeze-Ahead Cathedral (pre-frozen pad)"** (Cloud, long DECAY, HOLD = FREEZE held before the wall arrives) → tape.

The whole chain is mono until it hits the Big Time, which fans the fuzz into a stereo field; the Big Sky receives that stereo wall and the held pad lives across it.

## Per-unit

- **EQD Hizumitas — "Doom Wall (max heavy)":** Volume max · Sustain max · Tone fully CW (max bass). The full-CW Tone is deliberate — the scooped, dark voicing keeps the wall *controllable* and thundering rather than chaotic, and the long dense tail blends straight into the Big Time without competing with the dry note. This is the saturated source that has to swell up into the frozen room.
- **CB Big Time — "Hizumitas Fuzz Wall":** MODE **Long**, STATE **Compressed** (holds the sustaining fuzz together, no runaway), VOICING **Focus** (shaves highs+lows → keeps the muff wall defined), **COLOR LOW ~25–35%** (the fuzz already saturates — bring it up only until the repeats just begin to compress), **TILT EQ pushed UP** (cut the muff's low mud), FEEDBACK ~60%, WET ~45%, SPREAD widen. Hold the **RIGHT footswitch to FREEZE** the delay bed so the wall is self-sustaining while you free your hands.
- **Strymon Big Sky — "Freeze-Ahead Cathedral (pre-frozen pad)":** Machine **CLOUD**, **DECAY 20 s+**, Diffusion high (smooths the grain into a pad), MIX ~1:00 (this is the dominant voice at the top of the build), TONE ~11:00, MOD ~1:00, **HOLD = FREEZE**. Set HOLD = FREEZE via VALUE → scroll past Boost & Persist → Hold → FREEZE. The pad is frozen *before* the wall comes up, so it sits there as an existing space. Clock positions are a DOUG-dialed starting point, not published artist dials.

## Routing

The performance order is the inverse of the signal order, and that's the point. **Freeze the Big Sky first:** swell one chord (guitar volume knob or a slow pick) into the Cloud machine and hold the footswitch to FREEZE — now an oceanic pad hangs in the air with nothing under it. **Then build up from the bottom:** bring in the Hizumitas wall and let the Big Time's MISO stereo field and FREEZE bed climb. Because the Big Sky is in FREEZE (not INFINITE), the rising wall played "on top" of the held pad comes through cleanly rather than being endlessly re-fed into the wash — the cathedral stays fixed while the wall swells *into* it instead of *adding to* it. INFINITE would smear every new layer back into the pad and turn the build to mud; FREEZE keeps the two layers legible.

**Gain-staging:** keep COLOR modest — a hot fuzz plus high COLOR makes the Big Time's limiter clamp the wall to porridge, and you need the wall to read as a distinct rising body against the static pad. Hizumitas max-bass Tone + Big Time TILT-up + Focus together keep the low mud out so the fuzz wall and the Cloud pad don't fight in the same frequency mud. Mono front → Big Time IN-L auto-engages MISO; stereo from the Big Time onward. No clock needed — this is a free-running drone, not a rhythmic figure.

## Sound

A frozen reverb pad blooms first and just hangs there — an empty lit cathedral — then the fuzz-and-delay wall swells up into it from underneath, the saturated body rising to fill the room that was already waiting. The reverse-order doom build: the existing walls grow the space out of the note, but here the space is the first thing you hear and the doom is what arrives to fill it. **Taste-ref:** drone/doom (Swans-adjacent sustaining crescendo; Boris/Wata wall) — but staged as an inverted swell rather than a bottom-up bloom.

## Play

1. Swell one chord into the Big Sky with the guitar volume knob (attack disappears into the Cloud), then **hold the Big Sky footswitch to FREEZE** the pad. Let it hang — space first, no wall yet.
2. With the cathedral held, bring up the Hizumitas wall (full Volume/Sustain/max-bass) and let the Big Time build; **hold the Big Time RIGHT footswitch to FREEZE** the delay bed so the wall self-sustains. The saturated wall now rises into the existing pad.
3. To collapse: release the Big Time FREEZE (or hold MODE to panic-reset to a clean delay) and let the wall fall away — leaving the frozen Big Sky cathedral hanging alone again, the way it started.

## Sources

- **Basis:** designed integration; chains **Hizumitas "Doom Wall (max heavy)"** + **Big Time "Hizumitas Fuzz Wall"** + **Big Sky "Freeze-Ahead Cathedral (pre-frozen pad)"** (new). The fuzz→delay gain-staging (COLOR modest, STATE Compressed under sustaining fuzz, TILT-up + Focus to tame mud, MISO auto-engage) is documented in the Big Time "Hizumitas Fuzz Wall" patch / `Gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md` §A. The FREEZE-vs-INFINITE Hold behavior (hold the footswitch to freeze any patch in the background; FREEZE leaves what you play on top unaffected, INFINITE re-feeds it and goes chaotic) is documented in `Gear/Strymon Big Sky/research/transcripts/antoine-michaud-bigsky-infinite-vs-freeze.md` — here repurposed as freeze-ahead (pad frozen *before* the source arrives) rather than freeze-to-solo.
- Hizumitas max-bass doom voicing: `Gear/EarthQuaker Devices Hizumitas` — EQD Noodlers quoted doom clip + product copy.
- `Research/Taste-Profile/taste-profile.md`
