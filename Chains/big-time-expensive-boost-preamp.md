---
type: chain
title: "Big Time Expensive-Boost Stereo Preamp"
date: 2026-06-15
artists: [Electronic Audio Experiments, Chase Bliss]
instrument: guitar / bass / synth
gear:
  - Chase Bliss Big Time
  - Chase Bliss MOOD MkII
---

# Big Time Expensive-Boost Stereo Preamp

The most expensive clean boost you will ever buy — and worth it. **No delay at all.** With WET pulled fully down, Big Time stops being a delay and becomes exactly what the manual says it can be: a standalone stereo analog preamp. You're paying ~$700 to use a delay as its own front end, which is absurd, and it sounds fantastic, so here we are. COLOR drives the matched input preamp, +12dB adds gain, and STATE picks the saturation flavor — so the dry note arrives at MOOD already warmed, thickened, and stereo-split. MOOD then treats that *colored* signal as richer source material than a clean DI would ever be: its reverb/granular wash has more harmonic content to chew on, so the texture blooms denser and darker from the first note.

🟣 DOUG-designed integration. The WET-down-preamp behavior is published (manual p.24); the new Big Time patch is purpose-built for this chain. COLOR/+12dB/STATE positions are a dialable recipe, not a saved factory preset — set by ear (Chase Bliss publishes character, not numbers).

## Signal path

Guitar / bass / synth → **CB Big Time — "Expensive-Boost Preamp (WET Down)"** (WET **fully down** = standalone stereo analog preamp, +12dB **ON**, COLOR to taste, STATE = Saturated, DRY CLEAN **OFF** so the dry actually gets colored, IN-L auto-**MISO** mono→stereo) → **CB MOOD MkII — "Reverb Wash vs Multi-Tap Clusters"** (Reverb wash → granular grains on the now-saturated source) → amp / interface, stereo.

The only "signal-order" claim here is **saturator/preamp → texture** — color the tone *before* the part, then let the ambient box process the already-colored signal. There is no delay stage at all; Big Time's whole delay engine is muted by WET=0 and only its analog dry path passes.

## Per-unit

- **CB Big Time — "Expensive-Boost Preamp (WET Down)"** (new, purpose-built) — Pull **WET all the way down**; per the manual (p.24) this turns Big Time into a standalone stereo analog preamp — the delay engine is silent and only the analog dry-thru passes. **COLOR is now your only voice:** it sets how hot you hit the input preamp, so it's a saturation/drive control here, not a delay-feedback control — dial it to taste (start ~9:00 for clean-warm, push toward noon-and-up for audible grit). **+12dB ON** (the "second most important button" — Big Time is built to *add* gain, so this is the boost). **STATE = Saturated** for the soft-clip console-warmth voice (switch to **Compressed** for a leveled, glued boost, or **#!&% / misbias** if you want the preamp itself to sag and grind). **VOICING = Warm or Analog** (the EAE Sending V2 callback — gentle ~4k roll-off, the most preamp-like tone). Crucially, leave **DRY CLEAN OFF** in the Options menu — DRY CLEAN routes the dry *around* the preamp, which would defeat the entire patch; we want the dry colored. **SPREAD widen** + IN-L **MISO** so a mono instrument exits as a colored stereo pair. **No saved factory preset for this** — COLOR/STATE positions are a dialable recipe set by ear. (Watch output: +12dB plus COLOR can be loud — set level before you commit to tape.)
- **CB MOOD MkII — "Reverb Wash vs Multi-Tap Clusters"** (reused) — Wet MODE **Reverb**; **MODIFY is smear**: MIN = distinguishable multi-tap clusters, MAX = washed-out reverb, mid = "semisolid hybrids," and a further twist splits the wash into flitty granular grains. **TIME** sets decay/size (CCW short room, CW long bloom). Because the incoming signal is already preamp-saturated and harmonically dense, push MODIFY a touch past the wash point so the reverb tips into grains — the extra harmonics give the granular engine more to fracture, and the texture reads richer than it would on a clean DI. ROUTING **IN** (process the live colored signal), MIX to taste — this is the *texture* of the part, so it can sit forward or sit under, your call. Hold the LEFT (Wet) footswitch to freeze the wash into a sustained bed and play over it.

## Routing

Two boxes, all-stereo from Big Time onward. Mono in → Big Time **IN-L auto-engages MISO** (mono-in / stereo-out), so even on a single guitar the colored dry exits as a stereo pair and MOOD sits in a real stereo field. **Gain-staging is the whole patch:** COLOR is the drive, +12dB is the boost, WET=0 mutes the delay — there is no feedback path to run away, so this is a *safe* loud, but it is still loud (manual warns the +12dB / hot-COLOR combo spikes output). Set Big Time's level with the downstream MOOD MIX and your interface gain in mind before printing. Keep **DRY CLEAN OFF** (the dry must hit the preamp) and **DRY KILL OFF** (DRY KILL would mute the only signal passing, since there's no wet) — both live in Big Time's Options menu and both will silence or sterilize the patch if flipped the wrong way. Order matters: Big Time *must* come first so MOOD receives the already-saturated tone; put MOOD first and you'd be reverbing a clean note and then coloring the reverb, which muddies instead of enriches.

## Sound

A warm, studio-saturator dirt with zero delay — the tone *before* the part. The dry note arrives thick, slightly compressed, gently driven and stereo, then MOOD blooms a dense reverb-into-granular wash off that richer source: the haze has body and harmonic grain a clean signal could never feed it. On bass it's a fat DI-warmth into a granular cloud; on synth it tames line-level and adds analog grit before the texture; on guitar it's an "expensive boost" that makes the ambient box sound like it's processing a finished, mixed tone.

**Taste-ref:** the EAE / John Snyder house style — "a colored preamp/saturation stage feeding the next box" — here pointed at an ambient texture instead of a delay. Think console-warmth DI into a granular reverb: studio-saturator dirt, not pedalboard fuzz.

## Play

1. Pull Big Time **WET fully down**, +12dB **ON**, STATE **Saturated**, VOICING **Warm/Analog**. Confirm **DRY CLEAN OFF** and **DRY KILL OFF** in Options.
2. Set **COLOR** by ear against your input: back it off for clean-warm, push it up until the note just starts to grit. This is your drive/boost amount.
3. Set MOOD Wet MODE **Reverb**, TIME for decay/size, and sweep **MODIFY** from multi-tap → wash → grains; park it where the saturated source tips into a dense granular bloom.
4. Play a sustained chord or single note — listen for the colored tone arriving *thick* and the reverb chewing on the extra harmonics.
5. To hold a bed, **hold MOOD LEFT (Wet) to freeze** the wash and solo over it. To go fully clean, kill +12dB and roll COLOR back — the preamp stays, just transparent.

## Sources

- **Basis:** 🟣 designed integration; chains **CB Big Time — "Expensive-Boost Preamp (WET Down)"** (new) + **CB MOOD MkII — "Reverb Wash vs Multi-Tap Clusters"** (reused). WET-fully-down = standalone stereo analog preamp is **published** (`gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` quoting manual p.24). COLOR = "how hot you hit the input preamp + limiter" and +12dB = "the second most important button… built to add gain" from `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md` §1. STATE saturation characters + Warm/Analog (EAE Sending V2) voicing + analog dry-thru + DRY CLEAN (dry bypasses preamp) / DRY KILL Options behavior from `Big-Time-DeepResearch.md` (§Alt/Options, §DRY routing). MOOD MODIFY = smear (multi-tap → wash → grains) and TIME = decay/size from the reused MOOD patch (manual pp.24–25, video manual pt1).
- Honesty flag: COLOR / +12dB / STATE clock positions are a **dialable recipe** set by ear — the WET-down-preamp *behavior* is sourced, but no saved factory preset captures these knob values.
