---
type: chain
title: "Clean → MOOD Slip-Harmony Glitch Bloom"
date: 2026-06-15
artists: [The Unperson, Brian Eno]
instrument: clean guitar
gear:
  - Chase Bliss Clean
  - Chase Bliss MOOD MkII
  - Walrus Audio QI Etherealizer
---

# Clean → MOOD Slip-Harmony Glitch Bloom

A swelling, dynamically-even clean tone smeared into pitch-stepped harmonized haze and reverse glitches, then shimmered into a halo. The whole move hinges on **Clean giving MOOD a sustained, consistent source**: Clean swells each note in from silence *and* limits it to a flat ceiling, so by the time the signal reaches MOOD it is a steady, even-leveled bed — which is exactly what Slip's auto-sampler needs to track cleanly. Feed Slip a spiky, uneven pluck and its semitone-stepped harmonies stutter and lose the thread; feed it a swelled, limited, sustained tone and the harmonies (and reverse trails) bloom in coherent, like-pitched layers. QI then puts an octave-up shimmer halo around the whole harmonized bed.

🟣 DOUG-designed integration. **MOOD-spotlight, no Big Time.** The MOOD and QI patches carry their own provenance (factory/designed); the Clean patch is purpose-built for this chain (full spec saved alongside). Clean's knob faces are a dialable recipe — Chase Bliss publishes character, not numbers — flagged below. Artists/taste-ref name the sound it chases, not a chain anyone played verbatim.

## Signal path

Clean guitar → **CB Clean — "Slip Feeder (Swell + Limited Boost)"** (Dynamic Swell ON + limiting Dynamics + Wet make-up boost → a swelled, even, hot, sustained source) → **CB MOOD MkII — "Slip as Real-Time Reverse / Harmonizer"** (Wet MODE = **Slip**, MODIFY stepped off-noon for semitone harmonies, CCW = reverse glitches) → **Walrus Audio QI — "Prismizer Halo Freeze Cloud"** (Parallel, Grain Playback **x2** +1-oct prism layer + Tri chorus glide into the always-last Space → an octave-up shimmer halo around the harmonized bed) → amp / interface.

The real signal-order claim here is the deliberate **condition-the-source → harmonize → shimmer** placement: Clean must come *first* so MOOD's Slip sampler sees an already-swelled, already-limited, sustained tone; QI must come *last* so the shimmer halos the finished harmonized bed rather than getting chopped back into MOOD's auto-sampler.

## Per-unit

- **CB Clean — "Slip Feeder (Swell + Limited Boost)"** (new, purpose-built): engage the **AUX Dynamic Swell** so each note bows in from silence (no volume pedal); push **Dynamics toward noon (limiting, ~4:1+)** so the swelled note hits a flat, sustained ceiling rather than a varying level; **Wet up past noon** for make-up gain so MOOD's input runs hot; **Dry off/low** so the swell reads cleanly. Hidden Options (hold both footswitches): **Wet = Swell-In ~noon** (slowish bloom), **Dry = Swell-Out ~noon** (graceful fall) — a pad-like swell, not a fast violin attack. Sensitivity set FIRST by ear to the left red LED, re-set per instrument. Mode **Manual**, Physics **Mid (stable)**, all CUSTOMIZE dips off except SWELL/LATCH as noted. The point: this is *not* the bare "Home Base" leveler and *not* the plain "Dynamic Volume Swell" — it deliberately fuses swell + limiting + make-up boost so Slip gets a single coherent, sustained, hot note to chew on. **Numeric positions are a dialable recipe — Chase Bliss publishes character, not numbers.**
- **CB MOOD MkII — "Slip as Real-Time Reverse / Harmonizer":** Wet MODE = **Slip** (the headline). **TIME = sampling size** — start mid/high so harmonized phrases trail behind your swelled notes (lower TIME = more instant pitch-shift and glitchier reverse stutters). **MODIFY = playback speed/direction in semitone steps** — park it *off* noon for sustained pitch-stepped harmonies, and sweep **CCW of noon for reverse** glitch trails (up to 2× each way). MIX around 1:00 so the harmonized/reversed haze sits as a bed under the dry swelled line. Because Clean feeds it a sustained, even source, the semitone harmonies track instead of stuttering. Add the **CLASSIC** dip for aliased/uneven crunch on the Slip voices if you want it grittier; **SPREAD** optional to auto-pan the Slip voices. ⚠️ A stray MIDI Note on MOOD's channel would auto-engage Synth Mode — keep notes off its channel if you ever clock it.
- **Walrus Audio QI — "Prismizer Halo Freeze Cloud":** Flow **Parallel** (live dry stays present on top; this rig's better default), Grain **Grain Cloud**, Grain Mix ~1–2:00, **Playback x2 (+1 oct)** = the bright prism-up shimmer layer, Tri chorus (Mix ~11:00, Rate ~9:00, Depth ~11:00) as the slur/glide stand-in, **Space modest ~10–11:00** (the always-last reverb dominates if pushed — keep it the halo, not a second wall), Tone ~1:00 to roll any ice-pick. Short-press **Freeze** to loop the grain cloud as a pitched halo around the held/harmonized note and play over it; or leave Freeze off and let the x2 grains shimmer the bed continuously. This is the named hardware approximation of the Bon Iver/Prismizer octave-up vocal halo — here it halos MOOD's harmonized output instead of a single note.

## Routing

Three stereo boxes in a row, MOOD in the spotlight, no Big Time. **The gain-staging / order reasoning is the whole game:**

1. **Clean first, and it must both swell AND limit AND boost.** Slip is a continuous auto-sampler — it tracks best on a sustained, even-leveled source. A raw pluck (loud transient, fast decay) makes Slip's semitone harmonies stutter and the reverse trails grab inconsistent chunks. Clean's swell removes the hard transient (note bows in), its limiting flattens the level into a sustained ceiling, and its Wet make-up gain drives MOOD hot — together that is the "sustained consistent source so Slip's harmonies track." This is why a plain leveler or a plain swell patch isn't enough; the purpose-built combo is the load-bearing choice.
2. **MOOD owns the middle and the character.** Slip's harmonized/reversed haze is the featured voice. Keep MIX around 1:00 so the harmonies are a bed under the dry swelled line, not a total takeover. TIME trades instant-pitch-shift (low) against trailing harmonized phrases (high); MODIFY's off-noon park sets the harmony interval, CCW = reverse.
3. **QI last, halo not wall.** The shimmer must wrap the *finished* harmonized bed, so QI sits after MOOD. Run **Parallel** and keep **Space modest** — QI's Space is mix-and-decay on one knob and will dominate if pushed, which would bury MOOD's harmonies. The x2 (+oct) grain into the gentle Space is the shimmer; that's the whole assignment. If QI starts to own the mix, pull Space first, then Grain Mix.
4. **Level / clipping:** QI has no input-level switch and clips on hot sources — Clean's Wet boost is sized to drive MOOD, not to slam QI, so trim if QI's grain input distorts. **Stereo:** create width inside MOOD (SPREAD / MISO) and let QI's Parallel image pass it; keep Clean's MISO/SPREAD off in the front-anchor role.
5. **If the harmonies get lost:** drop QI Space first (loudest wet stage), then MOOD MIX — never push QI up to "win," that just washes out the Slip voices the chain exists to feature.

## Sound

A clean note swells up out of silence at an even, sustained level, and instead of decaying it dissolves into a haze of pitch-stepped harmonies and backwards-glitch trails that track the line coherently — then an octave-up shimmer halo blooms around the whole harmonized bed. Even, blooming, harmonized, slightly glitched, and shimmering: a MOOD-Slip showcase where the harmonies actually lock because the source feeding them is dynamically flat and sustained.

**Taste-ref:** The Unperson's real-time-reverse / pseudo-harmonizer Slip moves (semitone-stepped MODIFY, CCW reverse) crossed with Eno-style evolving-ambient beds — a living, harmonized wash that holds and shimmers while a clean swelled voice moves through it.

## Play

1. **Set Clean by the LED first**, then engage the AUX swell and push Dynamics into limiting + Wet past noon — confirm a soft pick now bows in to a flat, sustained, hot level.
2. **Set MOOD = Slip.** Park MODIFY off noon for your harmony interval; sweep CCW toward reverse to taste. Use a higher TIME for trailing harmonized phrases, lower for instant pitch-shift / glitchier stutters. MIX ~1:00.
3. Play **held / swelled notes** — let the swell bow each note in and watch the semitone harmonies and reverse trails bloom and track (because the source is even and sustained).
4. **QI shimmer:** with Playback x2 + modest Space, the harmonized bed gets an octave-up halo continuously; or short-press **Freeze** to lock a pitched halo and solo a clean line over it.
5. To collapse: back MODIFY to noon (harmonies → neutral), drop QI Space, and you're back to a clean swelled tone.

## Sources

- **Basis:** 🟣 designed integration; chains **CB Clean — "Slip Feeder (Swell + Limited Boost)"** (new, purpose-built) + **CB MOOD MkII — "Slip as Real-Time Reverse / Harmonizer"** + **Walrus Audio QI — "Prismizer Halo Freeze Cloud"**. The Slip core (Wet MODE = Slip, TIME = sample size, MODIFY = semitone steps, CCW = reverse) is documented in the MOOD "Slip as Real-Time Reverse / Harmonizer" patch (`slip-real-time-reverse-harmonizer.md`; MOOD-MkII manual pp.26–27; video-manual pt.1; ref: The Unperson / Ali). The QI octave-up shimmer halo (Parallel, Playback x2 +1 oct prism layer, Tri chorus glide, Space modest) is documented in the QI "Prismizer Halo Freeze Cloud" patch (`prismizer-halo-freeze-cloud.md`; QI UsageGuide §grain-Freeze-pad / "feed that sustained source into the pitch-shimmer — source vs space"). Clean's swell-feeds-downstream-boards, limiting-for-a-sustained-source, and Wet/Dry make-up-gain mechanics are documented in the Clean gear profile/UsageGuide (swell hidden options Wet=Swell-In/Dry=Swell-Out; limiting + slow release for a sustained wall; Wet/Dry boost = make-up gain) and the existing "Dynamic Volume Swell" / "Home Base" / "Always-On Huge Fuzz Feeder" patches.
- **Honesty flag:** no published knob numbers exist for the new Clean "Slip Feeder" patch — all of its clock-face positions are a dialable recipe, set by ear (Clean uses single-LED metering, no recallable detents). MOOD's Wet MODE = Slip is a real switch position; TIME/MODIFY are continuous and dialed by ear. QI's Flow/Playback/grain switch positions are real; the knob clock-faces are a dialable recipe.
