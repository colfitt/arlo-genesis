---
type: chain
title: "Clean → Hizumitas Always-On Huge (Banjo)"
date: 2026-06-15
artists: [Boris, Swans]
instrument: banjo (GK-5 → VG-800) / guitar
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - EarthQuaker Devices Hizumitas
  - Caroline Somersault
---

# Clean → Hizumitas Always-On Huge (Banjo) ⭐

Comp-before-fuzz, taken to its logical extreme. A banjo is all attack and no sustain — a spiky pluck that's gone in ~1.5 s — which is the worst possible source for a Big-Muff wall: the fuzz only ever hears the spike, so the wall lurches in and out with your dynamics. Here Clean runs hot Sensitivity into hard limiting *first*, flattening every pluck — loud or whisper-quiet — to the same hot, even level before it reaches the Hizumitas. Now the fuzz is always slammed, so the wall is **massive and consistent regardless of how softly you play.** Then a mostly-wet, darkened seasick Somersault smears that wall into wobbly, tape-flavored lo-fi ambience. No Big Time: Hizumitas and Clean are the spotlight.

🟣 DOUG-designed integration. No artist played this exact chain — the per-unit patch sheets carry their own provenance, and the Taste-ref names the sound it chases.

## Signal path

Banjo (GK-5) → **VG-800** (clean modeled banjo source, real 5th-string drone in via NORMAL MIX) → **CB Clean — "Always-On Huge Fuzz Feeder"** (hot Sensitivity, Dynamics into hard limiting) → **EQD Hizumitas — "Doom Wall (max heavy)"** (the always-on Big-Muff wall) → **Caroline Somersault — "Worn Cassette Under the Wall"** (mostly-wet seasick lo-fi smear) → amp / interface.

The only "real artist signal-order" invoked is the general **fuzz-before-modulation** standard — a documented pedal-order best practice (EQD / Reverb signal-chain guides), not an artist-specific path. The novel move is the *compressor-into-limiting before the fuzz*, which is the whole point of the chain.

## Per-unit

- **VG-800:** run the banjo essentially *clean* (no synth model) so a normal, spiky banjo arrives at Clean — the limiting, not a VG-800 SUSTAIN model, is what evens the source here. Keep `NORMAL MIX ~20–40%` so the real, un-tracked 5th-string drone stays in the signal. A darker AMP model upstream helps if the banjo top end reads piercing.
- **Clean — "Always-On Huge Fuzz Feeder":** the heart of the chain. **Re-LED `Sensitivity` first** — run it HIGH by the left LED, hot enough that even quiet picking still moves it (GK-5 per-string output ≠ a passive pickup, so re-LED any time you change the GK calibration or instrument). `Dynamics ~noon–1:00` (**hard limiting**) — this is the "always massive" knob: it clamps every pluck to the same ceiling so soft and hard picking hit the fuzz identically. `Wet ~1:00–2:00` (hot, to slam the Hizumitas — honest: this is comp make-up gain, not a transparent boost), `Dry OFF`, `Attack ~9:00` (fast — no transient escape; we *want* the spike flattened, unlike the singing-lead variant), `EQ noon`. Release toggle Mid, all dips OFF.
- **Hizumitas — "Doom Wall (max heavy)":** `Volume max · Sustain max · Tone fully CW` (max bass — the scooped/dark CW voicing keeps the wall *controllable* and tames the banjo's piercing 2–4 kHz). With Clean already slamming an even, hot source in, the Muff is permanently saturated — the long dense tail is the always-on wall. Pre-shape mid character with the **Filter knob** (scooped ↔ thick) to taste; thicker reads heavier under the Somersault smear. Avoid maxing Sustain against a *CCW* Tone (that's the runaway/chaos combo, reserved elsewhere) — here we want a stable wall, not oscillation.
- **Somersault — "Worn Cassette Under the Wall":** the lo-fi smear. `MIX ~1:00` (mostly-wet blend — keep some dry anchor so chords don't fully seesaw), `OFFSET ~3:00` (high — this is the "danger" knob; high offset pushes into detuned slapback-chorus / seasick territory and is what reads as a delay-flavored *smear*), `DEPTH ~12:00`, `SPEED ~9:00` (slow, woozy waver), `WAVE triangle`, `TONE Dark` (hi-cut on the wet line — this sells the "worn cassette under a clean dry" illusion). **Honest:** the Somersault is a lo-fi chorus/vibrato, *not* a delay — it has no repeats, time, or feedback control; the "smears it into wobbly ambience" here is its detuned, pitch-unstable wet-line warble, not literal echoes. Stab **HAVOC** (momentary, slams Speed to max) for tape-flutter / ray-gun bursts at phrase ends.

## Routing

Mono front board the whole way (VG-800 → Clean → Hizumitas → Somersault), then out to amp/interface. No clock, no stereo split, no Big Time — this is the minimal "two-pedals-are-the-show" wall the concept calls for, with the Somersault as the lo-fi finishing veil.

**Gain-staging is the whole argument, and the order is the point:** Clean limits and flattens dynamics FIRST → the Hizumitas sees a hot, even source on *every* note → so the wall is always huge no matter how quietly you pick. Putting the compressor *before* the fuzz (and pushing it into hard limiting) is the unconventional move — most players compress after dirt — but it's exactly why even quiet picking triggers full saturation. The Somersault sits *after* the fuzz so the pitch-warp lands on the finished wall rather than getting eaten by the Muff's saturation. If you want the fuzz to **breathe with your attack** instead of staying permanently slammed, back Clean's `Dynamics` DOWN out of limiting (toward 10:00 comp) — but then you've left the "always-on huge" thesis of this chain.

## Sound

A massive, consistent Big-Muff wall that does not flinch with your dynamics — feather-light picking and a hard strum produce the same thundering saturation — smeared by a darkened, pitch-unstable lo-fi wobble into wobbly, tape-flavored ambience. Even, huge, and a little seasick.

**Taste-ref:** the doom/drone sustaining-fuzz voice (Boris / Wata's Hizumitas wall; Swans-adjacent crushing sustain) wrapped in a "recorded-wrong" cassette haze (Car Seat Headrest / Modest Mouse tape degrade; Radiohead tape flutter).

## Play

1. Set the VG-800 to a clean banjo source; confirm the 4 main strings track and the 5th-string drone sits in via NORMAL MIX.
2. **Re-LED Clean's `Sensitivity`** against the banjo, then test the thesis: play one note *as quietly as you can* and confirm the Hizumitas wall arrives just as huge as a hard strum. If quiet notes drop out, Sensitivity is too low or Dynamics isn't into limiting.
3. Hold chords or sustained single notes and let the always-on wall bloom; play *sparser* than you think — the wall and the smear fill the space.
4. Stab **HAVOC** on the Somersault at the end of a phrase for a tape-flutter / ray-gun burst, then release back to the slow woozy base.

## Sources

- **Basis:** designed integration; chains **Clean "Always-On Huge Fuzz Feeder"** + **Hizumitas "Doom Wall (max heavy)"** + **Somersault "Worn Cassette Under the Wall"**. Comp-into-limiting before fuzz = consistent always-on drive (high Sensitivity so even quiet picking triggers full saturation) is documented in the Clean "Always-On Huge Fuzz Feeder" sheet (`research/Clean-DeepResearch.md` §9 + §13(c); `links/daily-clean-dialing-in-everyday-compression.md`). Banjo decays in ~1.5 s and the Hizumitas "completes the note" per the Hizumitas GearProfile; doom-wall Volume/Sustain/Tone-CW per EQD Noodlers + EQD product copy (`research/links/eqd-noodlers-settings.md`). Somersault as mostly-wet seasick lo-fi smear (m. it is a chorus/vibrato, NOT a delay — no repeats/time/feedback) per `Somersault-DeepResearch.md` §2 + §13(c) and `links/somersault-stacking-recipes.md`.
- `Research/Taste-Profile/taste-profile.md` (doom/drone + "recorded-wrong" cassette lenses)
</content>
</invoke>
