---
type: chain
title: "Big Time Wet-Dry-Wet Parallel Aux Wall"
date: 2026-06-15
artists: [Brian Eno, The Cure]
instrument: "guitar / synth (studio)"
gear:
  - UA Apollo x8
  - Radial X-Amp
  - Chase Bliss Big Time
---

# Big Time Wet-Dry-Wet Parallel Aux Wall

A studio routing, not a stompbox order: a pristine dry center prints straight to the converters with no preamp on it, while a saturated, self-degrading wet-only delay is flown in on a parallel DAW aux — hardware Big Time on an aux send, returned around the dry. Wet-dry-wet ambience where the dry never gets colored, and the only "sound" in the room is the delay crumbling on its own fader. The trick is **DRY KILL**: it turns Big Time into a pure wet return so the pedal's analog preamp (COLOR) and limiter (STATE) only ever touch the echoes, never the printed dry.

🟣 DOUG-designed integration. No artist played this exact aux routing — the per-unit patch ref carries its own provenance, and the Taste-ref names the sound it chases. The wet-dry-wet send structure is standard mix-engineer territory (a hardware delay on a parallel aux); what's specific here is using Big Time's DRY KILL to make a *self-degrading* pedal behave like a clean studio send.

## Signal path

source (guitar / synth DI) → **Apollo x8 line in** (MIC/LINE = LINE, preamp bypassed straight to the A/D) → DAW **dry track** (pristine, uncolored, printed once) → DAW **aux send** → Apollo **spare line out** (kept off the monitor bus) → **Radial X-Amp** (line → instrument level/impedance) → **Big Time IN-L/IN-R** (running **CB Big Time — "Dry-Kill Disintegrating Aux"**, STATE Saturated/`#!&%`, **DRY KILL ON**) → **Big Time stereo OUT** → **Apollo stereo line in** (wet-return inputs) → DAW **wet aux** returned and panned around the dry → mix.

The dry center sits dead center, dead clean. The wet return is panned wide L/R around it — wet-dry-wet. Nothing about the dry ever passes through the X-Amp or the pedal; only the send copy does.

## Per-unit

- **Apollo x8** (no patch — it's the recording terminus / routing hub). Two jobs here: print the **dry** clean (LINE input, preamp bypassed to the A/D for the most transparent capture), and host the **parallel aux** — a Console/DAW send out a spare line output (kept **off** the monitor bus so it can't feed back) to drive the hardware pedal, plus a pair of line inputs to take the wet return. Meter the dry pre-fader, peaks ~−12 to −6 dBFS, 96 kHz/24-bit. Console faders are monitor-only and don't change what prints, so set send/return level on the DAW aux.
- **Radial X-Amp** (no patch — passive-feeling reamp/level box). It does the one job that makes this routing honest: converts the Apollo's **line-level** aux send down to **instrument level** with the right impedance so Big Time's 1 MΩ front end sees a proper guitar-level source instead of a hot line feed. Without it you'd either slam the pedal's preamp or have to lean on COLOR to compensate; the X-Amp lets you keep **COLOR low** and let the *patch* do the coloring. (If you ever feed a genuinely line-hot source, Big Time also takes balanced/line input directly — but the X-Amp is the clean, repeatable studio path.)
- **CB Big Time — "Dry-Kill Disintegrating Aux"** (new) — the whole reason this works as wet-only. **DRY KILL ON** (Options) so the pedal returns **100% wet** — its preamp and limiter never touch the dry. STATE **Saturated** for "echoes that slowly disintegrate and expand into a big harmonic mass," or flip to **`#!&%` (misbias)** for the rawer, self-sabotaging "broken, drifting delay lines" voice — that's the "self-degrading" character. **COLOR low** (the X-Amp already staged the level; over-COLORing a clean source just slams the limiter to porridge). **FEEDBACK ~55–65%** so the wet blooms and decays without climbing into a runaway wall. **TILT EQ at/above noon** to keep the disintegrating tail from clouding the dry center. **TEXTURE** mid (Saturated = clipping symmetry → ragged; misbias = misbias sensitivity). VOICING **Focus** "shaves highs+lows over time → focused floating repeats" so the wet sits *around* the dry instead of fogging it. Slow **MOTION Sine** for tape-wow drift. The values are a dialable recipe, not published numbers — Chase Bliss publishes character, not knob positions, and flying faders override on recall (flagged in the patch).

## Routing

The whole point is **gain-staging and keeping the dry uncolored.** The dry is captured once, clean, and never re-amped — it goes straight to the converters with the preamp bypassed. The wet lives entirely on a **parallel aux**: a DAW send taps a copy of the dry, the X-Amp drops that line-level copy to instrument level, the pedal eats it with **DRY KILL ON** so only echoes come back, and the stereo return lands on its own fader panned around the dry. Because the dry doesn't pass through Big Time, you avoid the multi-pass problem the title's "no preamp coloring four times" calls out — there's no series stack of preamps stamping the dry on every pass; the dry is pristine and the delay is the only colored element, by design.

Three guardrails:
1. **Keep the send line out OFF the monitor bus** — same discipline as the X-Amp reamp loop; if the wet return feeds back into the send you get a runaway loop.
2. **COLOR low.** The X-Amp already set a sane level; lean on STATE/TEXTURE/VOICING for the disintegration, not on COLOR slamming the limiter.
3. **FEEDBACK below a wall.** This is wet-dry-wet *ambience*, not a doom bed — keep FEEDBACK in the bloom-and-decay zone (~55–65%) so the wet supports the dry instead of swallowing it. If you *do* want it to climb, hold Big Time's **RIGHT footswitch** to ramp COLOR+FEEDBACK for a momentary swell, then release.

Optional: clock the pedal to the session (native 5-pin DIN, **CC111 = 0** to follow) so the disintegrating taps lock to the song tempo, and recall section presets via **Program Change** (PC# = slot, PC 0 = LIVE) to re-voice the aux verse→chorus→outro hands-free. Print the wet return to its own track if you want to commit the disintegration and free the hardware.

## Sound

A pristine, uncolored dry center with a saturated, self-degrading wet-only delay blooming and crumbling in parallel around it — wet-dry-wet studio ambience where the dry is dead clean and the only character in the picture is the delay slowly falling apart on its own fader. Because DRY KILL makes the return 100% wet, the delay isn't an effect *printed onto* the dry — it's a separate, disintegrating layer you can solo, EQ, automate, and re-pan independently.

**Taste-ref:** Eno-style "treatments on a return" ambient production (the dry stays the dry; the character lives on a parallel send) crossed with The Cure / 4AD wide stereo delay-throw — the recorded-wrong, slowly-disintegrating wet wash sitting *around* a clean source rather than smeared *through* it.

## Play

Play the part clean — the disintegrating wet return does all the atmosphere. Ride the **wet aux fader** to swell the delay in for choruses; pull it down and the dry stands alone, pristine. For a degrading outro, hold the part, push the wet fader up, and let the Saturated/misbias tail expand and crumble — or hold Big Time's **RIGHT footswitch to FREEZE** the last phrase into a held bed and play the next idea clean over it. Flip STATE Saturated → `#!&%` between takes to choose how violently the repeats self-destruct. Hold **MODE** to panic-reset the pedal to a clean delay if the aux runs hot. Commit by printing the wet return to its own track once you like it.

## Sources

- **Basis:** designed integration; routes a clean DAW dry + a parallel aux through **CB Big Time — "Dry-Kill Disintegrating Aux"** (new). DRY KILL = wet-only return, COLOR-low for non-fuzz sources, native-DIN clock (CC111), and section recall via Program Change from `gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md` §C [V/R]. STATE Saturated = "echoes that slowly disintegrate and expand into a big harmonic mass"; `#!&%` misbias = "broken, drifting delay lines / raw electric character" from `gear/Chase Bliss Big Time/research/links/cb-big-time-factory-presets-recipes.md` + `centerpiece-big-time-as-song-centerpiece-one-pedal.md`.
- **Apollo / X-Amp routing:** clean LINE capture (preamp bypassed to A/D), parallel aux out a spare line output kept off the monitor bus, and the X-Amp line→instrument level conversion into hardware from `gear/UA Apollo x8/research/Apollo-x8-UsageGuide.md` (print/reamp/cue-aux sections) + `gear/UA Apollo x8/research/transcripts/record-apollo-no-latency.md` (Console aux sends for monitor FX).
- Patch ref: `Patches/Chase Bliss Big Time/dry-kill-disintegrating-aux.md` (new).
- `Research/Taste-Profile/taste-profile.md` (Eno treatments-on-a-return / 4AD wide stereo delay-throw aesthetic).
