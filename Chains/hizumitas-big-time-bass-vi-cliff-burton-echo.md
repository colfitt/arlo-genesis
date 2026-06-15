---
type: chain
title: "Hizumitas → Big Time Cliff Burton Bass Echo"
date: 2026-06-15
artists: [Cliff Burton, Metallica]
instrument: bass / Bass VI
gear:
  - Chase Bliss Clean
  - EarthQuaker Devices Hizumitas
  - Chase Bliss Big Time
---

# Hizumitas → Big Time Cliff Burton Bass Echo

The "Cliff Burton vibes" Hizumitas setting — the demonstrator's own descriptor for a sustained, recording-preamp-style distorted bass — extended into stereo delay without ever losing the clean fundamental. A held bass / Bass VI note becomes a saturated wall of round low end, then Big Time fans slow, compressed echoes into stereo space around it. The trick that makes it work on bass: **DRY CLEAN** keeps the dry note out of Big Time's preamp, so the fundamental stays clean and tight under saturated repeats while the wet echoes carry all the fuzz weight.

🟣 DOUG-designed integration. No artist played this exact chain — Burton's name appears only because it is the documented *descriptor* for the Hizumitas bass voice (Andy Bassist demo), not a claim of his actual gear. The per-unit patch refs carry their own provenance; the Taste-ref names the sound it chases.

## Signal path

bass / Bass VI → **CB Clean — "Bass Compression with EQ Low-Cut"** (mono, level + low-B taming) → **EQD Hizumitas — "Cliff-Burton Bass Fuzz"** (Tone ~10:00, mono) → **CB Big Time — "Cliff Burton Bass Echo (DRY CLEAN)"** (IN-L, auto-MISO mono→stereo) → amp / interface (stereo).

The only "real-artist signal order" invoked is the general **fuzz-before-delay** standard (a documented pedal-order best-practice) — the compressor lives *first* here, before the fuzz, because on bass it is a leveler/feeder, not a wall-builder.

## Per-unit

- **CB Clean — "Bass Compression with EQ Low-Cut"** — Bass Fox's stored bass leveler: Dynamics fairly high (~10:00–noon, ≈4:1), mid Attack, mid Release, EQ nudged CW to shave a hair of high end. The load-bearing move is in Hidden Options: **Envelope Balance toward MORE** so a low B / boomy lows high-pass the *control* signal and don't choke the engine (audio unaffected). This delivers an even, "warm/full/punchy" bass into the fuzz so the Hizumitas blooms consistently instead of spiking on the hardest notes. **AVOID Sag on bass** (it favors highs, reacts poorly to low end). *Honesty: Bass Fox's positions are "mid / fairly-high" descriptors, not exact published clock values — dial by the left LED at playing volume.*
- **EQD Hizumitas — "Cliff-Burton Bass Fuzz"** — **Volume 12:00 · Sustain ~3:00 (≈¾) · Tone ~10:00 (treble side)**. The treble-side Tone is deliberate: it keeps the low strings *defined* under heavy sustain, which is exactly the "recording-preamp distorted low end that stays defined" voice. Feedback stays low even at this gain, only slight hiss. (All three Hizumitas values are published — Andy Bassist demo.) Maps cleanly onto a Bass VI's low courses; on a Bass VI keep the picking even since the higher courses can spit.
- **CB Big Time — "Cliff Burton Bass Echo (DRY CLEAN)"** *(new patch)* — MODE **Long**, STATE **Compressed**, VOICING **Warm or Analog** (flatters the dark bass tone), **DRY CLEAN ON** (Options menu — dry bypasses the preamp so the bass fundamental stays clean and tight while only the wet repeats saturate), **TILT EQ pushed UP** (cut the low mud out of the repeats per manual p.39 "cut the mud from your bass"), **COLOR modest ~30–40%** (the fuzz already supplies saturation), FEEDBACK ~55–60% for slow stacked echoes, WET ~40–45%, CLUSTER low-mid, SPREAD widen for the stereo space. Compressed STATE is the "safe" self-osc state — it holds the sustaining bass fuzz together and stops runaway.

## Routing

Mono fuzz → **Big Time IN-L auto-engages MISO** (mono-in / stereo-out) — the clean way to fan one mono bass-fuzz into a stereo echo field; stereo from Big Time onward. No clock needed (sustained, not rhythmic) — tap a slow TIME by feel.

**Gain-staging is the whole game, and on bass it has two jobs.** (1) The Clean *levels* the bass before the fuzz so the Hizumitas blooms evenly — the compressor is a feeder here, not the wall. (2) Big Time's **DRY CLEAN** is what makes this a *bass* patch and not a guitar wall: the analog dry-thru bypasses the input preamp, so the clean low fundamental passes through tight while COLOR + the limiter only act on the wet repeats. Keep COLOR modest — too much COLOR + a hot fuzz clamps the limiter "to porridge." Push TILT UP so the saturated repeats don't pile low-mid mud on top of an already-round bass. If you want a pure wet echo bed with the dry coming straight off the amp instead, swap DRY CLEAN for **DRY KILL** (wet-only out).

## Sound

A sustained distorted-bass wall: round, defined low end up front, thickened by slow saturated echoes spreading into stereo space — and underneath it all, a clean bass fundamental that never turns to mud. The fuzz wall and the clean root coexist because the dry path stays out of the preamp.

**Taste-ref:** the "proper Cliff Burton vibes" Hizumitas bass voice (Andy Bassist's descriptor) — sustained recording-preamp bass fuzz — stretched into a saturated stereo echo bed. Doom-adjacent low-end weight with a clean root intact.

## Play

1. Set the Clean by the left LED at playing volume; dial Envelope Balance toward MORE if a low B over-triggers.
2. Set the Hizumitas (Vol 12 / Sustain ¾ / Tone ~10:00) and let a held low note bloom to full sustain.
3. On Big Time, confirm **DRY CLEAN is ON** in the Options menu (tap both footswitches), then hold a sustained note and let the compressed echoes stack into stereo.
4. Ride COLOR up only until the repeats just begin to thicken — no further (past that the limiter clamps to porridge).
5. Dig in vs. play gently to ride the dynamics: the clean fundamental stays put while the wet wall swells around it. Hold MODE (2s) to panic-reset Big Time to a clean delay if anything runs away.

## Sources

- **Basis:** designed integration; chains **CB Clean "Bass Compression with EQ Low-Cut"** + **EQD Hizumitas "Cliff-Burton Bass Fuzz"** + new **CB Big Time "Cliff Burton Bass Echo (DRY CLEAN)"**.
- Hizumitas bass settings (Vol 12 / Sustain ¾ / Tone ~10:00) and the "proper Cliff Burton vibes" descriptor are published — Andy Bassist bass demo (`Patches/EarthQuaker Devices Hizumitas/cliff-burton-bass-fuzz.md`; `research/transcripts/andy-bassist-hizumitas-bass-demo.md`).
- **DRY CLEAN keeps a clean bass fundamental while only repeats saturate** — sourced from `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` §"Bass (Jazz bass) / SG" (line 78) and Options-menu §2 (line 36); **TILT up to cut bass mud** from manual p.39 (DeepResearch §6, line 75) — *"cut the mud from your bass."* COLOR-modest-under-fuzz + Compressed-under-sustain + MISO auto-engage from `research/links/centerpiece-minimal-chains-and-sampler-integration.md` §A.
- Clean bass leveler + Envelope Balance low-B fix from `Patches/Chase Bliss Clean/bass-simple-compression-low-cut.md` (Bass Fox preset; compressorpedalreviews / TalkBass).
- `Research/Taste-Profile/taste-profile.md` (doom / low-end making-aesthetic thesis)
