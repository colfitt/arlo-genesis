# AVOX Choir (Vocal Multiplier) — Usage Guide

Choir does exactly one thing and does it well: turns **one held note into up to 32 detuned
unison voices**. No pitch, harmony, formant, or MIDI — it only multiplies the pitch already
there. In this rig it's the fastest path from a single sustained source (vocal, **banjo,
baritone, synth, drone**) to a shimmering wall — and the wall is *sold by the reverb after
it*, so Choir → Valhalla is the real instrument.

---

## 1. The entire control set (it's tiny)

- **Choir Size:** 4 / 8 / 16 / 32 voices.
- **Pitch / Timing / Vibrato Variation:** per-voice random spread — higher = looser, swimmier.
- **Stereo Spread:** 0 (center / mono-stacked) → 100 (full width).
[links/avox-choir-official-user-guide.md]

---

## 2. Signature settings

- **Believable thicken (double-track):** 4–8 voices, *moderate* Variation.
- **Wall:** **Size 16–32**, push **all three Variations**, **Spread ~70–100** → shimmering
  detuned choir-of-one. At 32 add EQ to keep intelligibility.
- **Build big from multiple instances**, not one maxed track (both reviews + the manual agree).
[links/avox-choir-practical-use-and-reviews.md; links/avox-choir-official-user-guide.md]

---

## 3. Rig-specific recipes

- **Drone / banjo / baritone / synth wall:** held single note → Choir on a **stereo (or
  mono→stereo)** channel → Size 16–32, high Variation, wide Spread → **Valhalla VintageVerb**
  (long, concert-hall). The reverb is what makes it real (SoS: "far more realistic when you
  add concert-hall reverb"). [links/avox-choir-practical-use-and-reviews.md]
- **Stacked choral chord:** 2–3 instances on different held pitches, **or** place Choir
  *after* Harmony Engine's voices to multiply each one.
- **Degrade path:** print the Choir+verb wall, then RC-20 / SketchCassette on the bounce.

---

## 4. Common pitfalls / gotchas

- **Stereo Spread is disabled on a mono track** — run stereo / mono→stereo in Logic for width.
- **Older AVOX flag (SoS):** in stereo mode only the **left channel** is processed → feed a
  true mono source; don't expect per-channel handling of an already-stereo input. [links/avox-choir-practical-use-and-reviews.md]
- **CPU scales with voice count** (32 heaviest) → prefer several smaller instances / print.
- Optimized for voice; works on monophonic instruments but **"results vary by source"** —
  extreme Variation = synthetic/chorus-y (a feature here, a bug for realism).

## 5. Captured sources
- `links/avox-choir-official-user-guide.md` (the complete control set + ranges)
- `links/avox-choir-practical-use-and-reviews.md` (musicngear + Sound On Sound — how sizes sound, instrument use, gotchas)
- Built on existing `transcripts/antares-choir-evo-demo.md` (Music Tech Help Guy).

**QC:** official PDF extracted cleanly (high confidence). Review specifics **triangulated**
across musicngear + Sound On Sound (Antares' own page is JS-walled/thin). No drone/doom/
shoegaze artist credit — relevance is capability-based (it's a utility, not a signature sound).

## Sources
See §5. Originals: antarestech.com Choir PDF, musicngear.com, soundonsound.com. URLs on line 1.
