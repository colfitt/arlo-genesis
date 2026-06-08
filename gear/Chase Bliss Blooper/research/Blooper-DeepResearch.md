# Chase Bliss Blooper — Deep Research

A working dossier for slotting the Blooper into Board 3 (End / Time → Tape) of a hex-pickup banjo/baritone rig. The Blooper sits 4th on the End Board — after CB MOOD MkII, before the Hologram Chroma Console — and it is the rig's **song-length looper**, the device that captures whole sustained passages and rebuilds them in real time rather than the micro-loop and granular work happening upstream. The unavoidable structural fact about this placement: the rig runs **stereo** from the CE-2W split all the way through Board 2 and the first three End-Board pedals, but **Blooper is mono in / mono out**, so the entire stereo image collapses to a single channel here. This document treats that collapse head-on — whether it's a problem, a deliberate commit point, or both — and works out the looper labor division against the MOOD MkII micro-looper one slot upstream and the Microcosm granular engine back on Board 2.

## 1. Lineage: the "bottomless looper" and who built it

The Blooper is not a looper that grew modifiers; it's a sound-design engine that happens to loop. It was a three-way collaboration — **Chase Bliss, KNOBs (Scott Harper, the pedal-demo videographer), and 3 Degrees Audio** — first shown as a prototype at NAMM 2019 and shipped late 2019 into 2020 ([Reverb collaboration announcement](https://reverb.com/news/chase-bliss-audio-knobs-and-3-degrees-audio-are-collaborating-on-a-pedal-the-blooper), [Chase Bliss product page](https://www.chasebliss.com/blooper)). KNOBs' fingerprints are all over the concept: the marketing line is "merge high-fidelity looping with creative manipulation," and the manual opens by reframing looping itself — *"it can be helpful to think of looping like gathering raw materials. Once you get some sounds in there, you can really get started"* (manual, p. 2). The pedal is built so the looping functions are "surrounded by machinery that lets you mold your loops into new and unexpected shapes" — remix, edit, pile up variations, or "let Blooper take the lead and leave your source material behind completely."

The defining architectural move is the **two modifier slots (Channel A + Channel B) plus a Stability circuit**, all of which can be applied either to the playing-back loop *or* recorded into it. This is what separates Blooper from a JamMan or a Ditto: the modifiers are not effects sitting after the loop, they are part of the loop's editable DNA.

Firmware has been an active story. Chase Bliss ships the Blooper as a platform you reflash over USB via the **BLIP interface** (blooper.chasebliss.com / blip.chasebliss.com); the company shipped a "MASSIVE" v3.0 upgrade with new resources and modifier banks, and the current public build is **v3.2** ([BLIP firmware page](https://blip.chasebliss.com/), [Chase Bliss Facebook v3.0 post](https://www.facebook.com/chasebliss/posts/3456518237781637/)). The manual in this folder is the 2023 web-guide revision and reflects the current modifier roster. (Flag: a precise dated changelog per firmware version is not published in one place — version *numbers* are verified, granular per-version release notes are not.)

## 2. Controls, modes, and dip switches

Three knobs, two footswitches, three toggle switches, and a bank of dip switches on the top edge. Per the manual (pp. 6–13):

**Shared knobs:**
- **VOLUME** — loudness of the loop; noon is unity, max is +2x boost. (When ramping is engaged this knob's function changes — it controls the *speed* of the ramp movement instead, p. 42.)
- **LAYERS** — the navigation/undo knob. Counter-clockwise removes overdub layers one at a time, clockwise adds them back: effectively up to 8 levels of non-destructive undo/redo on the face of the pedal. Critical gotcha from the manual (p. 7): *"If you go back to an earlier layer and press record, all subsequent layers will be erased."* The knob "goes to sleep" when idle so its physical position doesn't matter when you're not touching it (p. 23).
- **REPEATS** — the fade control. Counter-clockwise makes overdubs fade out as you build, creating evolving, decaying loops; max = standard infinite looping (no fade). This is also the knob that makes Blooper behave like a delay (see §3). Note: loops only fade while *overdubbing*, not during plain playback.

**Mode toggle (NORM / ADD / SAMP):**
- **NORM (Normal)** — modifiers and Stability are treated like external effects sitting over the loop. Set the sound, hear it, and turn it off and the clean loop is waiting underneath. Best starting point.
- **ADD (Additive)** — modifiers, Stability, *and your knob movements* are recorded into the overdub. "If you hear it, so does Blooper." This is the pedal's signature mode and the heart of the sound-design pitch (manual pp. 30–31).
- **SAMP (Sampler)** — performance mode; no overdubbing. Each record press clears the old loop and starts fresh; hold-to-record for momentary capture; the right footswitch triggers/retriggers. Hold the right footswitch to turn looping off entirely and turn Blooper into a manual sample player (manual pp. 14–15, 34–35).

**STABILITY toggle/knob** — a multi-effect that introduces "an analog and increasingly broken feel (includes wow, flutter, noise, and filtering)." Minimum = bypassed for clean looping. This is the lo-fi degradation engine reviewers single out as irreplaceable (manual p. 8).

**Modifier controls (MOD A / MOD B):** each channel has a knob (controls the modifier, noon = neutral with opposite behaviors either side), a 3-way mini-toggle to select which of three modifiers is active (1/2/3 for A, 4/5/6 for B), and an arcade button to engage it — quick press latches, hold = momentary (manual pp. 10–11, 16).

**Footswitches:** left = RECORD/PLAY (tap to start recording, tap again to set loop length and play, then toggles overdub/playback); hold left = one-shot overdub (exactly one pass, then auto-returns to playback — the clean way to "print" a modifier in ADD mode). Right = STOP; hold right = undo/redo submenu. Both at once = delete loop and start over (manual pp. 12–13).

**Dip switches (Customize, pp. 40–41):**
- **DRY KILL** — removes the clean signal from Blooper's output (wet-only). Relevant for the chain discussion below.
- **CV CLOCK** — repurposes the CV jack as a clock-sync input.
- **PLAY / DUB** — chooses whether a finished initial recording drops into playback (default) or straight into overdubbing the second layer. PLAY/DUB → straight-to-dub is useful for ambient reverb-trail capture.
- **BANK A / BANK B** — engages the alternate modifier banks per channel (see §3).
- A second dip bank governs **ramping** (Layers, Repeats, Stability, Mod A, Mod B, Bounce, Random, Wiggle, Sync, Sweep, polarity) — internal modulation that automates any knob (pp. 42–45).

## 3. Sonic character — why it's a "sound-design" looper, not a recorder

The thing that makes Blooper unusual is that **a loop is raw material, and the twelve modifiers are the tools that resculpt it.** The modifier roster (manual pp. 18–21, the "Bloop Troop"):

**Channel A default bank:**
- **A1 Smooth Speed** — fluid, tape-machine-style speed/direction change; crawl, find sweet spots, or introduce dissonance.
- **A2 Dropper** — playback errors / brief silences; CCW random drops, CW consistent patterns; at max, granular crumbling.
- **A3 Stepped Trimmer** — shortens the loop by trimming off the end and start in musical subdivisions (halve it, etc.).

**Channel B default bank:**
- **B4 Stepped Speed** — speed/direction in musical steps tuned to octaves and fifths; one extra octave of range vs the smooth/chromatic speeds.
- **B5 Scrambler** — rearranges the loop into a pattern; CCW random, CW a repeating sequence; high settings chop everything up.
- **B6 Filter** — simple multi-mode (CCW high-pass, CW low-pass); can self-oscillate in ADD mode.

**Alt banks (dip-selected):**
- **A1 Chromatic Speed** (speed in chromatic steps, for transposing), **A2 Pitcher** (pitch ±3 octaves without speed change), **A3 Stutter** (loop-within-a-loop, repeat the current moment).
- **B4 Stretcher** (speed change with no pitch change — the "microscopic world" inside each loop), **B5 Stopper** (two ways to stop the loop — volume fade or tape-stop), **B6 Swapper** (interactive muting / envelope-controlled swaps, great for replacing parts in ADD mode).

Caveat from the manual (p. 21): **Stretcher and Pitcher each use a lot of DSP, so you can't run both at once, and you can't combine them with the Speed modifiers (except to go into reverse).**

The "sound-design" character comes from three places. First, **the record head is always steady** (manual p. 28): Blooper uses two heads, one to record and one to play, and time-based modifiers split them — so when you overdub *while* a speed/trimmer/scrambler modifier is running, you record a different part of the loop than you're hearing, producing "unorthodox loops" you couldn't plan. Second, **STABILITY** is a genuine lo-fi degradation engine that ages the loop with wow/flutter/noise/filtering on every pass — the manual's "Repair Me" and "Tape Machine" recipes turn it into a tape deck on the edge of death. Third, the **NOISE GENERATOR trick** (p. 32): record silence, crank STABILITY, and overdub — Blooper records its own noise floor into the loop and becomes a no-input instrument. None of this is what a normal looper does.

It is also, per the manual (pp. 36–39), **a delay**: max REPEATS = infinite loop, lower it and Blooper bleeds into echo territory; "Blippertronics," "Tape Machine," and "Delooping" are the named patches. With MOOD and Big Time already on the board, this is a secondary use here — but worth knowing the REPEATS knob blurs the loop/delay line on purpose.

## 4. Behavioral notes — layers, stability, clock, mono

- **Layer ceiling.** 16 overdub layers total. Layers 1–7 are stored independently (full undo/redo to each); layers 8–16 are lumped into one "super layer" / mega-layer (manual pp. 22–23). So you have 7 discrete points of recall plus a bottomless dumping ground after that — "bottomless looper" is literal in that you can record into a single layer forever, but discrete *recall* tops out at 7.
- **A layer is only committed when you stop overdubbing.** You can circle a loop endlessly on one layer; it's only frozen when you enter playback or stop. This is what lets one layer "contain a whole heap of sound" (p. 23) and is the basis of the "Loop Capsules" technique (capture totally distinct scenes on separate layers, navigate between them with the LAYERS knob — pp. 38–39).
- **Stability vs chaos is a continuous dial, not a switch.** Min = clean. Push it and you get progressively broken; in ADD mode self-oscillation and runaway are on the table (Filter and Stopper especially). The "Repair Me" ramp recipe deliberately rides the line so the loop is "sometimes pure and clean, other times wobbly and disheveled, and occasionally volatile and obnoxious" (p. 45).
- **Clock sync.** CV can be repurposed as a clock input (CV CLOCK dip). When synced, pressing record *arms* Blooper — it waits for the next clock pulse to start, and playback is also synced to avoid drift ([manual p. 40](https://www.chasebliss.com/blooper); [Chase Bliss MIDI quick-start](https://blooper.chasebliss.com/midi/docs/midi-quick-start.pdf)). MIDI clock works too but requires the **Chase Bliss MIDIbox** to convert 5-pin DIN to the 1/4" TRS jack (see §8).
- **Mono.** One input, one output. There is no stereo mode and no firmware toggle that adds one. This is the load-bearing fact for §5.

## 5. Signal-chain placement — the mono collapse and the commit point

End Board order: `Generation Loss → Big Time → MOOD MkII → **Blooper** → Chroma Console → H90 → PORTA424 → 424 → Apollo/FOH`. The rig is stereo from the CE-2W split (Board 1), through all of Board 2, and through Generation Loss / Big Time / MOOD MkII. Then it hits Blooper.

**The collapse is real and it is total.** Blooper is mono in / mono out. Whatever stereo width Generation Loss, Big Time, and MOOD MkII have built — and the wide Board-2 textures from Microcosm, Etherealizer, and Dark Star feeding into them — **sums to a single channel the instant it enters Blooper.** Everything downstream (Chroma Console, H90) then *re-expands* that mono signal into stereo. So the rig's stereo field is not continuous: it's stereo → mono (at Blooper) → stereo again.

**Is this a problem?** Honest answer: mostly no, and arguably it's the right place to commit to mono. Three reasons:

1. **The collapse point is well-chosen.** Putting the mono device *fourth* on the time board means the most stereo-dependent material — the chorus/flanger/granular smear of Boards 1 and 2 — only matters up to the moment you decide to loop. Once you're capturing a song-length wall to layer over, mono is a fine canvas; Chroma Console and especially the H90 will re-spread it convincingly. The Strymon/Eventide-grade reverbs and modulations downstream are *designed* to manufacture width from a mono source.
2. **The owner already loses nothing he can't rebuild.** The two things hurt by mono summing are (a) hard-panned stereo information and (b) any out-of-phase content that can partially cancel when summed. The Deco/CE-2W chorus width and the Dark Star smear can phase-cancel slightly on the way into a mono jack — so there *is* a theoretical thinning. But the loop is being captured to be *transformed*, not preserved hi-fi, and STABILITY/degradation aesthetics make pristine stereo fidelity moot. This board is, by name, "Time → Tape": committing to a mono print before the tape stage is philosophically consistent.
3. **It's a deliberate "commit" gesture.** Drone/doom/shoegaze looping benefits from a *decision*. The mono fold-down forces the looped wall to be one coherent thing rather than a smeared stereo blur, which the downstream reverbs then re-inflate. Treat Blooper as the rig's "bounce to mono and recommit" stage.

**Practical mitigations the owner should know:**
- **What enters Blooper is what gets looped — in mono.** If a specific stereo move (a hard-panned ping, a wide chorus shimmer) is essential to a loop's character, capture it *before* this board (e.g. as a Microcosm/Octatrack loop) rather than expecting Blooper to preserve it.
- **DRY KILL dip.** If Blooper is left always-in-line, the dry signal passes through mono *even when not looping*, which means the dry path of the whole rig is mono from this point. The owner has two clean options: (a) leave Blooper's dry path intact and accept the rig is mono-from-Blooper-onward whenever it's powered (simplest, and consistent with the commit-point reading); or (b) if he wants the *dry* chain to stay stereo and only the *loop* to be mono, Blooper would need to live in a parallel/aux path (a stereo mixer or the H90's routing) rather than in the main series chain — that's a re-patch, not a dip switch. As wired today (series, 4th on Board 3) the rig is genuinely mono from Blooper's input onward. This is the single most important thing to be deliberate about.
- **Phase check.** Because a slightly out-of-phase stereo source thins when summed, if the looped wall ever sounds thinner than the live signal, the culprit is mono summing of the Deco/Dark Star width — nudge those toward a more correlated (less ultra-wide) setting before the loop board, or accept it as part of the degraded aesthetic.

**Relationship to MOOD MkII immediately upstream:** MOOD sits one slot before Blooper and is *also* a Chase Bliss looper-adjacent device, but the labor division is clean (see §9). MOOD's micro-loop/clock feeds Blooper a continuously-evolving source; Blooper captures the result at song length. Run MOOD into Blooper, not the reverse.

## 6. Source-specific use (banjo leads, baritone drones, VG-800, bass)

This rig's whole reason for a song-length looper is the banjo-as-lead-plus-sustained-walls workflow, and Blooper is unusually well-suited to it.

- **Looping banjo leads.** The Gold Tone EBM-5 → GK-5 → VG-800 chain produces bright, fast-attack, fast-decay signal. By the time it reaches Blooper it's been thickened by everything on Boards 1–2, so the looper sees a sustaining wall rather than a percussive pluck. Build the loop in **NORM** (clean capture), then bring in **STABILITY** and **Smooth Speed** to age and slow the banjo wall under a fresh live lead. The fast-attack banjo transients are exactly what **Scrambler** and **Stutter** chew into rhythmic, granular figures — turning a single banjo phrase into a self-generating pattern the player can solo over.
- **Baritone Jazzmaster drones.** This is Blooper's home turf. Capture a sustained baritone chord (post-Hizumitas/Longsword wall), drop into playback, then overdub with **Stepped Speed** for octave-down sub-drones tuned to fifths/octaves — instant doom thickness without a second instrument. The "Accumulator" recipe (mild modifier left running over many overdubs, STABILITY climbing) is the literal sound of a drone collapsing over minutes.
- **Modeled VG-800 signal.** Because the VG-800's COSM/synth patches are continuous waveforms, Blooper loops them cleanly. A VG-800 pad looped and then **Pitcher**-shifted ±octaves (alt bank A2) builds a synth-pad stack from one held note. Caveat: Pitcher and Stretcher are DSP-heavy and mutually exclusive (manual p. 21), so plan one or the other per loop.
- **Bass (Jazz Bass).** Mono is *ideal* for bass loops — no phase/width concerns at low frequencies anyway. Capture a bass figure in SAMP mode for momentary one-shots, or NORM for a held foundation; **Filter** (B6) low-pass keeps overdubbed layers from masking the fundamental.
- **Sampler integration.** The owner benches the CB Onward because "sampling covered by OP-1 + Octatrack + Blooper." Blooper's SAMP mode + Carryover (record a complex multi-layer loop in NORM/ADD, then switch to SAMP and trigger it) is the bridge — it lets a Blooper-built wall become a triggerable sample alongside the OP-1 Field and Octatrack MkII.

## 7. Famous users (honest)

Blooper's user mythology is mostly the **ambient/experimental and pedal-demo world** rather than a single signature artist. The pedal was co-designed by **KNOBs (Scott Harper)**, whose own demos are the canonical reference for what it does ([Reverb](https://reverb.com/news/chase-bliss-audio-knobs-and-3-degrees-audio-are-collaborating-on-a-pedal-the-blooper)). Equipboard lists a modest number of pro users ([Equipboard Blooper page](https://equipboard.com/items/chase-bliss-audio-blooper)) but no household-name has claimed it as *the* signature voice the way Wata claimed the Hizumitas — it's a tool-of-choice for ambient/shoegaze/experimental players (Chase Bliss's broader artist roster skews that way) rather than a star vehicle. **Honest verdict: do not expect a marquee "so-and-so's Blooper tone."** Its reputation rests on its capability and the KNOBs/Chase Bliss demo canon, not on a famous user's record. (Flag: specific named-artist usage beyond the design team is not reliably documented and is not asserted here.)

## 8. Live, power, and I/O

- **Power:** 9V DC, center-negative, **~150 mA** (manual cover; [Chase Bliss product page](https://www.chasebliss.com/blooper)). This is a *heavy* draw — far more than a typical analog pedal — and it must land on an isolated high-current supply slot (most isolated supplies have one or two 250–500 mA digital outputs; use one of those). Do not run it off a daisy chain. With several other Chase Bliss digital pedals on the End Board (Generation Loss, Big Time, MOOD MkII all also draw heavy), supply current budgeting is a real concern on this board.
- **I/O:** Mono in, mono out (see §5). Buffered bypass with analog dry-thru (the dry signal passes analog; the wet/loop is the digital part). DRY KILL dip removes the dry path for wet-only/aux use.
- **MIDI:** PC, CC, and Clock — but the 1/4" TRS MIDI jack requires the **Chase Bliss MIDIbox** to convert standard 5-pin DIN ([manual p. 47](https://www.chasebliss.com/blooper); [MIDI quick-start PDF](https://blooper.chasebliss.com/midi/docs/midi-quick-start.pdf)). The MIDIbox needs its own power. Once connected, Blooper takes PC for loop-slot/preset recall, CC for every knob and the footswitches, and **MIDI Clock** for tempo-synced looping/ramping.
- **CV / expression:** The single EXP/CV jack does CV control of any knob, CV clock sync (CV CLOCK dip), or expression-pedal control. A TRS cable carries expression; CV wants a floating-ring TRS-to-TS cable. **CV range is 0–5V — higher or negative voltage can damage the pedal** (manual p. 46). The MIDI jack can also take a normally-open momentary external footswitch to control the left footswitch hands-free.
- **Presets:** 16 loop slots saved/recalled via the SAVE/LOAD toggle workflow (preview, then save or load) with all layers preserved (manual pp. 8–9). Combined with MIDI PC, the owner can recall specific Blooper loops per song.
- **Live caveat (the big one):** Every reviewer flags this — Blooper "cannot really exist as a floor-based stompbox" because it rewards constant hands-on manipulation ([Delicious Audio](https://delicious-audio.com/chase-bliss-audio-blooper-pedal/), [popwave review](https://popwave.ai/benn-jordan/blog/blooper-pedal-review-guide)). For purely-foot use, NORM-mode straight looping + preset recall is the reliable subset; the modifier/ADD magic wants hands (or MIDI/CV automation via ramping).

## 9. Pairing recommendations by name

- **After MOOD MkII (one slot upstream):** MOOD's micro-loop / tape-style continuous engine is the *source generator*; Blooper is the *capture-and-rebuild* stage. Run MOOD → Blooper. Let MOOD's evolving micro-loop play, then hit Blooper record to freeze a song-length window of it, and overdub. Do not invert — MOOD downstream of Blooper would just re-process an already-committed loop, which Chroma/H90 do better.
- **Vs Microcosm (Board 2):** Microcosm is the *granular/generative* device — it shatters incoming audio into clouds and arpeggiated grains in stereo, in real time, and never "commits." Blooper is the *deliberate-capture* device — it holds a fixed loop you build and recall. Use Microcosm to generate texture *into* the chain; use Blooper to *keep* a passage. They don't compete; Microcosm's granular output (collapsed to mono at Blooper) is excellent Blooper source material.
- **Into Chroma Console:** Chroma is the right immediate downstream partner — it re-stereo-izes the mono loop and adds character (its own degradation/modulation palette) on top of Blooper's STABILITY. Stack Blooper STABILITY (loop-internal aging) under Chroma's per-block processing for compounding lo-fi.
- **Into H90:** The H90 is where the mono loop gets its widest re-expansion — Blackhole, MangledVerb, and the granular/pitch algorithms turn a mono Blooper wall into a stereo cathedral. This is the rig's "mono → stereo" recovery stage; lean on it.
- **MIDI clock with the CB stack:** The owner has many Chase Bliss MIDI pedals. A master clock (Octatrack, Digitakt 2, or a MIDIbox-fed controller) distributing MIDI Clock lets Blooper's loop length, ramping, and the tempo-synced devices (Generation Loss, MOOD, Big Time) all lock together. Worth the MIDIbox investment specifically because this rig already lives on synced Chase Bliss gear — scene/PC recall across the stack is the payoff.

## 10. Reviews and demos (real links)

- [Chase Bliss official Blooper page](https://www.chasebliss.com/blooper) — authoritative spec/feature list and the modifier roster.
- [Blooper web manual / modifier guide](https://blooper.chasebliss.com/modifiers) — the living modifier documentation.
- [BLIP firmware portal](https://blip.chasebliss.com/) — current firmware (v3.2), modifier customization, session export.
- [Reverb — Chase Bliss, KNOBs & 3 Degrees collaboration announcement](https://reverb.com/news/chase-bliss-audio-knobs-and-3-degrees-audio-are-collaborating-on-a-pedal-the-blooper) — the development/origin story.
- [Delicious Audio — Blooper writeup](https://delicious-audio.com/chase-bliss-audio-blooper-pedal/) — concise feature overview and the "needs hands, not feet" caveat.
- [Vintage King — Blooper review](https://vintageking.com/blog/chase-bliss-audio-blooper-pedal/) — studio-context review.
- [Premier Guitar — NAMM '19 Automatone Preamp & Blooper demos](https://www.premierguitar.com/gear/namm-19-chase-bliss-audio-automatone-series-preamp-mk-ii-blooper-demos) — first-look video coverage.
- [Guitar Pedal X — Chase Bliss looper/delay trifecta blog](https://www.guitarpedalx.com/news/gpx-blog/thoughts-on-the-chase-bliss-experimental-looper--delay-trifecta) — contextualizes Blooper vs MOOD vs the delay line.
- [Get Offset — Blooper demo podcast](https://getoffsetpodcast.com/demo-chase-bliss-blooper/) — hands-on demo discussion.
- [MIDI quick-start PDF (clock sync specifics)](https://blooper.chasebliss.com/midi/docs/midi-quick-start.pdf) — official MIDI/clock arming behavior.

## 11. Mods, quirks, firmware

- **Firmware is the "mod."** Blooper is reflashable over USB (BLIP); v3.0 added a large resource/modifier expansion and the current build is v3.2 ([BLIP](https://blip.chasebliss.com/), [v3.0 announcement](https://www.facebook.com/chasebliss/posts/3456518237781637/)). Through BLIP you can **reassign which 12 modifiers live in the two banks**, customize behaviors, and download/export your saved loops. There is no need (and no real community practice) of opening the box for hardware mods — the platform is the mod surface.
- **DSP exclusivity quirk.** Pitcher + Stretcher can't co-exist, and neither combines with the Speed modifiers except for reverse (manual p. 21). Plan loops around this.
- **The "erase-on-record-from-earlier-layer" trap** (manual p. 7) bites everyone once: navigate back with LAYERS, hit record, and every layer above it is gone. Use it deliberately (it's how you fork a loop), not accidentally.
- **ADD-mode self-oscillation.** Filter and Stopper can run away in ADD mode. Feature for the doom aesthetic; surprise for the unwary.
- **Record-head-always-steady behavior** (manual p. 28) means overdubbing under time-modifiers records a *different* part of the loop than you hear — intended, but counterintuitive until internalized.
- **Heavy current draw (~150 mA)** is the most common real-world setup snag — undersupplied slots cause glitches.

## 12. Spec sheet

| Spec | Value |
|---|---|
| Type | Bottomless looper with modifiers + Stability (sound-design looper) |
| I/O | **Mono in / Mono out** |
| Power | 9V DC, center-negative, 2.1mm barrel |
| Current draw | **~150 mA** (high — isolated digital slot required) |
| Bypass | Buffered bypass with analog dry-thru (DRY KILL dip for wet-only) |
| Modes | Normal (NORM), Additive (ADD), Sampler (SAMP) |
| Modifiers | 12 total, 2 channels × 3 + alt banks (Smooth/Stepped/Chromatic Speed, Dropper, Stepped Trimmer, Scrambler, Filter, Stutter, Pitcher, Stretcher, Stopper, Swapper) |
| Stability | Analog-style degradation (wow, flutter, noise, filtering), continuously variable |
| Layers | 16 overdub layers (1–7 independent / 8–16 super-layer); up to ~8 undo/redo on face |
| Loop saving | 16 slots, layers preserved |
| Internal mod | Ramping (bounce / ramp, sync, wiggle) on any knob |
| MIDI | PC, CC, Clock — **requires Chase Bliss MIDIbox** (TRS↔5-pin) |
| CV / Exp | CV control + CV clock sync (0–5V only); expression control; external footswitch via MIDI jack |
| USB | BLIP interface — firmware, modifier customization, loop export (current v3.2) |
| Designed by | Chase Bliss × KNOBs (Scott Harper) × 3 Degrees Audio |
| Released | NAMM 2019 prototype; shipped late 2019–2020 |

Source: [Chase Bliss Blooper page](https://www.chasebliss.com/blooper) and the 2023 Blooper web manual (this folder).

## 13. Starting-point settings

Clock-face knob positions, looking at the pedal from above. Mode toggle and modifier selections noted per patch.

**(a) Clean drone loop** — pristine song-length capture to layer over
- Mode: **NORM** · STABILITY: off (min)
- VOLUME: 12 · LAYERS: full (all layers in) · REPEATS: max (infinite, no fade)
- MOD A/B: off (arcade buttons up)
- Workflow: capture a sustained baritone/banjo wall, drop to playback, overdub live leads on top. Let Chroma/H90 re-stereo it downstream.

**(b) Modifier-mangled loop** — the ADD-mode signature move
- Mode: **ADD** · STABILITY: 9–10 o'clock (gentle age)
- MOD A: Smooth Speed, ~10 o'clock (slow drift) · MOD B: Filter (B6), sweeping
- REPEATS: ~1–2 o'clock · VOLUME: 12
- Workflow: build a clean loop in NORM, flip to ADD, then sweep the MOD knobs as you overdub — every movement bakes into the loop. Use one-shot overdub (hold left footswitch) to "print" a single modifier pass cleanly.

**(c) Stability-off-the-rails chaos** — broken tape, runaway
- Mode: **ADD** · STABILITY: 2–3 o'clock (heavy, volatile)
- MOD A: Dropper at max (granular crumble) · MOD B: Scrambler, CW (repeating chop)
- REPEATS: ~11 o'clock (fading, decaying) · VOLUME: 12
- Workflow: the "Repair Me" recipe (ramp STABILITY with bounce/random). Loop a wall, then let degradation and the modifiers tear it apart over passes. Expect feedback/self-oscillation — ride VOLUME.

**(d) Banjo layer-builder** — turn one banjo phrase into a self-generating bed
- Mode: **NORM** then **ADD** · STABILITY: 10 o'clock
- MOD B: Stepped Speed, set for octave-down/fifth (sub-drone under the banjo) · alt-bank A3 Stutter for rhythmic chop
- REPEATS: max · VOLUME: 12
- Workflow: capture a banjo lead phrase, overdub a Stepped-Speed octave-down layer for doom thickness, then play fresh banjo lead live over the self-running bed. Carryover into SAMP mode to trigger the finished wall alongside the Octatrack/OP-1.

## 14. Versus alternatives — why it earns the slot

Against generic loopers — **Boss RC-series, TC Ditto, EHX 720** — there is no contest on *purpose*: those are recorders; Blooper is a sound-design engine where the loop is editable raw material. The owner does not need a clean recorder on this board (the DAW/Apollo and Octatrack cover faithful capture); he needs a looper that *degrades and rebuilds*, and that's Blooper's entire reason to exist.

The harder comparison is the **internal loop/granular division of labor**, and this is where Blooper earns its specific slot:

- **Vs Hologram Microcosm (Board 2 granular):** Microcosm is real-time *generative granular* — it never commits, it sprays grains and arps in stereo. Blooper is *deliberate capture and reconstruction* — it holds a fixed, recallable loop. Microcosm makes texture; Blooper keeps a song. They live on different boards for a reason; one feeds the other.
- **Vs CB MOOD MkII (one slot upstream, micro-looper):** MOOD is the *continuous micro-loop / always-running tape* device — short, evolving, hands-off ambient motion. Blooper is the *song-length, hands-on, layered* looper. MOOD generates an evolving source; Blooper captures and overdubs it at scale. Running MOOD → Blooper is the correct order and gives the rig both ends of the loop spectrum (micro-evolving + macro-built).
- **Vs benching the CB Onward sampler:** the owner correctly benches Onward because Blooper's SAMP mode + Carryover, alongside the OP-1 Field and Octatrack MkII, covers triggerable sampling. Blooper isn't a sampler-replacement on its own, but in concert with the hardware samplers it closes the gap Onward would fill.
- **The mono cost is the only real knock,** and §5 argues it's an acceptable (even useful) commit point rather than a flaw, given the H90/Chroma re-expansion downstream and the degrade-everything aesthetic. A stereo looper (e.g. a second Microcosm-class device, or an H90 loop algorithm) could keep width — but none offers Blooper's modifier-driven sound-design depth. The trade is **stereo width for editability**, and on a "Time → Tape" board built to commit and degrade, editability wins.

Net: Blooper earns its slot as the rig's one **macro-scale, deliberately-editable, degrade-in-place looper** — the device that turns a banjo lead or baritone drone into a self-generating, aging bed for live playing over. Nothing else in the rig does that, and the mono collapse it introduces is recoverable downstream by design.

## Sources

- [Chase Bliss — Blooper product page](https://www.chasebliss.com/blooper)
- [Blooper web manual — modifiers](https://blooper.chasebliss.com/modifiers)
- [Blooper MIDI quick-start (clock/arming behavior)](https://blooper.chasebliss.com/midi/docs/midi-quick-start.pdf)
- [BLIP firmware portal (current v3.2)](https://blip.chasebliss.com/)
- [Chase Bliss Facebook — v3.0 firmware announcement](https://www.facebook.com/chasebliss/posts/3456518237781637/)
- [Reverb — Chase Bliss, KNOBs & 3 Degrees Blooper collaboration](https://reverb.com/news/chase-bliss-audio-knobs-and-3-degrees-audio-are-collaborating-on-a-pedal-the-blooper)
- [Delicious Audio — Blooper](https://delicious-audio.com/chase-bliss-audio-blooper-pedal/)
- [Vintage King — Chase Bliss Blooper review](https://vintageking.com/blog/chase-bliss-audio-blooper-pedal/)
- [Premier Guitar — NAMM '19 Blooper demos](https://www.premierguitar.com/gear/namm-19-chase-bliss-audio-automatone-series-preamp-mk-ii-blooper-demos)
- [Guitar Pedal X — Chase Bliss looper/delay trifecta](https://www.guitarpedalx.com/news/gpx-blog/thoughts-on-the-chase-bliss-experimental-looper--delay-trifecta)
- [Get Offset — Blooper demo](https://getoffsetpodcast.com/demo-chase-bliss-blooper/)
- [Equipboard — Chase Bliss Blooper](https://equipboard.com/items/chase-bliss-audio-blooper)
- [popwave — Blooper review/guide](https://popwave.ai/benn-jordan/blog/blooper-pedal-review-guide)
- Blooper 2023 web manual PDF (this folder: `manuals/Blooper_Manual_2023_Pedal_Chase+Bliss.pdf`) — authoritative for controls, modes, modifiers, layers, dip switches, MIDI/CV, ramping.
