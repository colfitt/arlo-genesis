---
type: chain
title: "Big Time Env Dive-Bomb Lead"
date: 2026-06-15
artists: [Adrian Belew, Nels Cline]
instrument: guitar / guitar-synth
gear:
  - Chase Bliss Clean
  - Chase Bliss Big Time
---

# Big Time Env Dive-Bomb Lead

Echoes whose time bends with your picking dynamics — dig in and the repeats dive-bomb and warp like a delay with a failing power supply. The trick is **MOTION = Env (envelope follower)** on Big Time: because TIME is a clock, modulating it with your playing envelope makes the delay *clock* speed up and slow down with how hard you play, so the pitch of the repeats sags and snaps. Out front, **Clean** evens the level *without* killing dynamics — a slow-attack ~2:1 squeeze that levels the body but lets the pick transient punch through — so the envelope follower always has a clean, musical dynamic curve to track. Dig in for a dive-bomb; ease off and the repeats settle back to pitch.

🟣 DOUG-designed integration. No artist played this exact two-pedal chain, and **no existing chain in the corpus uses Big Time's Env MOTION** — every other Big Time patch runs Off/Sine/Square. The artists/taste-ref name the sound it chases; the per-unit patch refs carry their own provenance.

## Signal path

guitar / guitar-synth → **CB Clean — "Transparent Enhancer"** (level the body, keep the pick attack — sets the dynamic curve) → **CB Big Time — "Env Dive-Bomb Lead"** (MODE Short, MOTION Env, DEPTH high, SCALE off, STATE Digital) → amp / interface

Mono in is fine; Big Time IN-L auto-engages **MISO** (mono-in/stereo-out) so the dive-bombs fan out in stereo. This is a two-pedal centerpiece box, not a wall — the "real artist signal-order" invoked is just the standard dynamics/compression-before-delay rule, here weaponized: the compressor *is* the conditioning stage for the modulator that follows.

## Per-unit

- **CB Clean — "Transparent Enhancer"** — the maker's own "lead lines" compression recipe: **Dynamics ~10–11:00 (~2:1, just into compression)**, **Attack SLOW (CW ~1:00) so the pick attack stays uncompressed**, **Release toggle RIGHT (Slow 1.5 s)**, **Wet noon–1:00 / Dry off**, **EQ noon (off)**, all dips off. Set **Sensitivity by the left LED** per instrument. Why this patch and not a brickwall: the whole chain depends on Big Time's envelope follower *seeing* your dynamics. A hard limiter (e.g. Clean's "Feedforward Snappy Limiter") would flatten the curve and the dive-bombs would all bend the same amount no matter how you play. The Transparent Enhancer's slow attack lets the transient escape uncompressed and only evens the *body*, so soft picking gives a small bend and digging in gives a full dive-bomb — the dynamics stay legible to the follower. The ~2:1 squeeze still helps by keeping note-to-note level consistent so identical-effort hits warp by identical amounts. The Dynamics/Attack/Wet positions here are the maker's published recipe character (Clean manual p.22, Recipe 1); Sensitivity is by-ear/LED as the patch flags.
- **CB Big Time — "Env Dive-Bomb Lead"** (new) — **MODE Short** (46–736 ms; long enough that a time-bend is an audible pitch dive, short enough to stay a lead delay not a wash). **MOTION = Env** — the headline: MOTION mode 3 is the envelope follower (Mark Johnston deep-dive: "1 = Sine, 2 = Square, 3 = Envelope follower"), and because TIME is a master clock, the follower modulates the *clock*, so playing dynamics bend delay time = pitch dive-bombs/warps. **DEPTH high** (Alt menu, under CLUSTER — "RATE/DEPTH get insane quickly," so high = deep, dramatic dives). **SCALE off** so the bends are smooth glides, not quantized Thermae steps — the failing-power-supply warp, not an arpeggiator. **STATE Digital** (no limiter) keeps the repeats clean and the pitch movement legible — the bend is the effect, you don't want a limiter pumping on top of it. **VOICING HiFi** to keep the warp articulate. **COLOR low–modest (~30–40%)** and **FEEDBACK ~40–55%** so the line dives, warps, and *settles* — this is a reactive lead delay, not a runaway wall (keep FEEDBACK in that first-10%-is-most-of-the-throw zone). **TILT EQ at/just above noon**, **CLUSTER low** (let the core repeat read so the dive is obvious). MOTION-mode is a published feature; the numeric COLOR/FEEDBACK/TILT/DEPTH positions are a **dialable recipe** (Chase Bliss publishes character, not numbers; on recall the flying faders override) — flagged in the patch.

## Routing

Straight series, mono in → Big Time MISO stereo out. **Gain-staging is the whole game, and it runs backwards from a wall chain:** instead of slamming the delay, you're *conditioning the modulator*. Clean must come BEFORE Big Time so the envelope the follower reads is already leveled-but-dynamic — put the delay first and the follower would chase raw, uneven transients and the bends would be erratic. Set Clean's Sensitivity so the LED rides the comp lightly on soft playing and clamps harder when you dig in; that delta is exactly what the Env follower converts into bend depth. Keep Big Time's COLOR low and STATE on Digital so the limiter isn't fighting the pitch movement — the moment COLOR climbs, the repeats clamp and the dive-bombs lose their swing. If the dives feel too violent, drop **DEPTH** first (it's the bend-amount fader), then ease Clean's Sensitivity back so less of your dynamic range maps to time. If they feel inert, push DEPTH up and back Clean's Dynamics off noon so more raw dynamics survive into the follower. Want a pure wet warp with no clean dry underneath? Flip **DRY KILL ON** in Big Time's Options and run it as an aux — but in this two-pedal box the dry-retained series path (your in-tune note over its own dive-bombing ghost) is the intended sound.

## Sound

A lead voice whose echoes won't sit still in pitch: play a clean line and its repeats trail off, then *dive* and warp downward as you dig into the next phrase, snapping back toward pitch as you ease off — the queasy lurch of a tape or BBD delay whose clock is starving. Stereo-fanned, articulate, and entirely playing-reactive: the dynamics ARE the mod source, so the part writes its own pitch automation. **Taste-ref:** Adrian Belew's seasick whammy-and-delay lead warps (King Crimson / solo) crossed with Nels Cline's unstable, pitch-smearing ambient lead delays — expressive, slightly-broken, dynamics-driven lead texture rather than a static effect.

## Play

Play deliberate single-note lead lines and *use your right hand as the pitch wheel*. Let a note ring soft and the repeats stay near pitch; dig hard into the next attack and watch the echoes dive-bomb and warp on the way out. Vary pick force across a phrase to "draw" the bend contour — accents become dives, ghost notes stay flat. For a signature gesture, end a phrase with a hard accent and let the dive-bomb trail dissolve under your next soft note (which itself stays in tune over the warping ghost). Roll guitar volume to fade the whole reactive cloud in like a swell. If it ever gets away from you, **hold Big Time's center MODE button** to snap back to a clean simple delay — the panic-reset.

## Sources

- **Basis:** 🟣 designed integration; chains **CB Clean — "Transparent Enhancer"** → **CB Big Time — "Env Dive-Bomb Lead"** (new). The corpus-novelty claim (no existing chain uses Env MOTION) verified by scanning every `Patches/Chase Bliss Big Time/*.md` — all use Off/Sine/Square.
- **Big Time Env mechanics:** MOTION mode 3 = envelope follower; TIME is a clock so modulating it bends pitch/time; RATE/DEPTH live in the Alt menu (under TIME / CLUSTER) and "get insane quickly"; SCALE off = smooth glides — all from `gear/Chase Bliss Big Time/research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (§MOTION, §faders). STATE Digital = no limiter / cleanest, stable feedback from `cb-big-time-factory-presets-recipes.md` + `sonicstate-superbooth-john-snyder-eae-interview.md`. COLOR-vs-FEEDBACK gain rule (low COLOR keeps repeats legible) from `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md` §1.
- **Clean side:** "subtle 2:1 compression that thickens, focuses, and extends… slower ATTACK means your pick attack is uncompressed" — Clean manual p.22 Compression Recipe 1, via `Patches/Chase Bliss Clean/transparent-enhancer.md`. Brickwall-kills-dynamics caveat contrasts against `Patches/Chase Bliss Clean/feedforward-snappy-limiter.md`.
- **Honesty flag:** Big Time MOTION = Env is a published feature, but no published numeric fader recipe exists for this use — COLOR/FEEDBACK/TILT/DEPTH are a dialable recipe, set by ear/LED. Clean's Dynamics/Attack/Wet follow the maker's published recipe character; Sensitivity is by-ear/LED.
- Patch refs: `Patches/Chase Bliss Clean/transparent-enhancer.md`, `Patches/Chase Bliss Big Time/big-time-env-divebomb-lead.md` (new).
- `Research/Taste-Profile/taste-profile.md` (Belew/Cline expressive unstable lead-delay aesthetic).
