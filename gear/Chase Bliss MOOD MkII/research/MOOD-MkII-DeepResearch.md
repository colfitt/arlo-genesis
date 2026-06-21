# Chase Bliss MOOD MkII — Deep Research

A working dossier for the MOOD MkII as it lives at position 3 on Board 3 (End / Time → Tape), wedged between the CB Big Time delay upstream and the CB Blooper looper downstream. Its job in this rig is not "make a loop" — Blooper does that — it's to be the **real-time smear/granular/micro-loop mangler** that grabs short fistfuls of the already tape-degraded, delayed stereo signal and warps them on the fly, before the whole mess reaches the full looper and the tape-print stage. This document is mostly concerned with that division of labor — MOOD vs Blooper vs the Hologram Microcosm two boards upstream — because the rig has three loop/granular-ish devices and they must not step on each other.

## 1. Lineage: MOOD (2019) → MOOD MkII (2023)

The original MOOD landed June 2019, unveiled via a [Knobs demo film](https://www.youtube.com/watch?v=G_BLyPxShG4), and was a genuine three-way collaboration: Chase Bliss built the platform, **Old Blood Noise Endeavors designed the Wet Channel** (the spatial side), and **Belgian builder David Rolo / Drolo FX designed the Micro-Looper Channel** (the always-listening loop side). Per [GuitarPedalX](https://www.guitarpedalx.com/news/gpx-blog/chase-bliss-reboots-its-mood-micro-looper--ambience-generator-with-significant-enhancements-including-stereo-and-overdubbing) and [Synth Anatomy](https://synthanatomy.com/2024/03/chase-bliss-mood-mkii-micro-looper-multi-fx-pedal-takes-the-stereo-route.html) that authorship carried straight into the MkII. It remains a "musical chemistry set" (the manual's own phrase) of two channels that are aware of each other and pass audio back and forth.

The MkII was announced March 2023 and shipped **late April 2023** at $399 ([Chase Bliss product page](https://www.chasebliss.com/mood-mkii); release timing per [Synth Anatomy](https://synthanatomy.com/2024/03/chase-bliss-mood-mkii-micro-looper-multi-fx-pedal-takes-the-stereo-route.html)). What changed from V1, verified against both the manual and web:

- **Fully stereo** in and out — the single biggest, most-requested upgrade (manual p.36; [Guitar.com](https://guitar.com/reviews/effects-pedal/the-big-review-chase-bliss-mood-mkii/)).
- **Overdubbing** on the Micro-Looper — you can now pile sounds onto a captured loop (manual p.30).
- **Loops up to twice as long**, and a **hold/freeze** function on *both* channels (web; manual pp.11, 13).
- **Noise-free Clock** by default — the V1's notorious clock-knob grunge is gone, but **Classic Mode** (a dip switch) brings back the old aliasing, gradual loop deterioration, ringy reverb trails, and rubbery delay pitch-bends for those who want them (manual pp.42–43).
- New utility everywhere: syncing the two channels, fading loops, hi-cut filtering the Wet Channel, channel level balance, blending clean micro-loop back in, and smoothing the Clock sweep (manual pp.14–17, 44–45).

A free **firmware 1.1** later restored the original "cloudy/wispy" character of Stretch mode inside Classic Mode ([Chase Bliss on X](https://x.com/chasebliss/status/1770843989480005855)). A limited **Light Bright Edition** (2,000-run, less-purple cosmetic variant) also exists ([GuitarPedalX](https://www.guitarpedalx.com/news/gpx-blog/chase-bliss-releases-super-appealing-2nd-limited-variant-of-the-mood-mkii---the-2000-run-light-bright-edition)).

> Manual-vs-web note: one source URL is dated 2024/03, but that reflects the *one-year-anniversary* firmware-1.1 coverage, not the release. The pedal shipped April 2023. Treat April 2023 as the ship date.

## 2. Controls, Channels & Dip Switches (from the manual)

MOOD is two side-by-side channels plus a shared center column. Both channels are footswitchable, both have a hold function, and the two are "aware of each other."

**Shared controls (center column, manual pp.8–9):**
- **MIX** — balance between dry input and MOOD (affects both channels). When ramping is engaged, this knob instead sets ramp *speed*.
- **CLOCK** — the master. Sets MOOD's sample rate, which controls *both* the Micro-Looper's loop length/resolution *and* the Wet Channel's quality and time. Moves in harmonized half/double steps (64k → 32k halves your loop and your effect together). Lower = grittier, aliased, "computer noises"; higher = cleaner/hi-fi (manual pp.18–21).
- **ROUTING toggle** — `IN` / `IN+micro-loop` / `micro-loop only`. Decides what the Wet Channel processes when both channels are on (manual pp.40–41).
- **PRESETS toggle** — left/right store a preset, middle is live. Hold footswitches to save (manual p.9). Only **2 presets**.

**Wet Channel** (OBNE-designed spatial side, manual pp.10–11, 22–27) — knobs are **TIME** and **MODIFY**, plus a 3-way **MODE** toggle and a footswitch (TAP = engage, HOLD = freeze). Three engines:
- **Reverb** — "multi-tap ambience." TIME = decay/size; MODIFY = smear (min for clean multi-tap echo clusters, max for washed reverb).
- **Delay** — "clean, looping delay." TIME = delay time (clean transitions, no pitch artifacts); MODIFY = feedback (at max it piles up like a looper). This is the mode that passes audio back and forth between channels.
- **Slip** — "auto-sampler." Continuously samples input and spits it back at a chosen speed/direction; TIME = sampling size; MODIFY = playback speed/direction in semitone steps (pitch-shifter / whimsical harmonies). Freezes into "glitchy synth."

**Micro-Looper Channel** (Drolo-designed loop side, manual pp.12–13, 28–35) — knobs are **LENGTH** and **MODIFY**, a 3-way **MODE** toggle, and a footswitch (TAP = toggle record/playback, HOLD = overdub). It is **always listening** — continuously recording in the background with no "stop." Loop length is set by the **CLOCK** position, not a record-time. Three engines:
- **Env** — "audio-controlled looper." LENGTH = slice size; MODIFY = audio-detector sensitivity. Chops the loop into slices and repeats the current slice whenever input goes quiet (stutters, frozen notes, time-stretch-by-touch).
- **Tape** — "tape-style looper." LENGTH = loop length (shrinks the loop "micro-er"); MODIFY = playback speed/direction in octave steps (half-speed up to 4×, forward or reversed).
- **Stretch** — "time-stretching looper." LENGTH = slice size; MODIFY = stretch amount + direction (at noon it freezes on a slice; counter-clockwise = classic grainy time-stretch).

**Dip switches (manual pp.42–45):** `MISO` (mono-in → stereo-out split), `SPREAD` (turns each mode into a stereo effect — ping-pong/scatter/panning per mode, manual pp.36–39), `DRY KILL` (removes clean signal even when bypassed), `TRAILS`, `LATCH` (footswitch hold latches), `NO DUB` (refresh mode), `SMOOTH` (de-steps the Clock sweep), and `CLASSIC` (V1 misbehavior). Plus a second dip bank + hidden-options menu (hold both footswitches) for `TONE` hi-cut, `STEREO WIDTH`, `DIRECT MICRO-LOOP` blend, `FADE`, `RAMPING WAVEFORM`, `LEVEL BALANCE`, `LOOP LENGTH` half/full, `SYNC` direction, and `SPREAD SOLO` (manual pp.14–17).

## 3. Sonic Character

MOOD does not have one sound; it has a *behavior*. Across all six engines the through-line is **lo-fi, sample-rate-degraded smear** — the Clock knob is "tone, length, and quality all in one" (manual p.20). At high Clock it's a clean stereo delay/reverb/sampler. Roll Clock back and everything turns gritty, aliased, and "real textural" — the loops downsample, the reverb tails get ringy, pitches step. [Guitar.com](https://guitar.com/reviews/effects-pedal/the-big-review-chase-bliss-mood-mkii/) (9/10) calls the MkII "a cinematic loop-scaping leviathan… not so much an effects pedal as an experimental instrument," and notes the reverb "can be fractured into delicate granular textures via the modify control," while at low sample rates the character is "grittily lo-fi… without introducing hiss."

The defining trick is the two channels feeding each other: route a micro-loop *through* the Wet reverb, freeze it, then play *into* the frozen bed — "interactive oddness arrives quickly" ([Guitar.com](https://guitar.com/reviews/effects-pedal/the-big-review-chase-bliss-mood-mkii/)). For this rig's drone/doom/shoegaze, "recorded-wrong" aesthetic, MOOD is squarely on-brief: it makes already-degraded signal *more* degraded, in stereo, in real time.

## 4. Behavioral Notes

- **Always-listening looper** — there's no record-arm and no stop. It's continuously buffering; tap to grab "whatever was played most recently," set by the **CLOCK** length (manual pp.28–29). The owner should treat it as "fishing for music," not as a deliberate looper.
- **Clock-synced loops** — `SYNC` (hidden option, manual p.17) ties one channel's timing to the other: in one position the Micro-Looper's length is set by the Wet TIME knob (capture rhythmic ideas in time with the effect); in the other, the Wet TIME moves in steps related to the loop length. Combined with **MIDI clock** this locks MOOD's loops to the rest of the CB ecosystem.
- **Freeze on both** — HOLD the Wet footswitch to infinitely repeat (reverb→ambient pad, delay→looping echo, slip→repeating tone, manual p.22). The Micro-Looper's HOLD is overdub, not freeze, but its bypassed always-listening state still records the Wet effects into new loops (the "Trail Catcher" trick, manual p.29).
- **Stereo behavior** — `SPREAD` exaggerates/creates stereo per mode: Reverb scatters taps, Delay ping-pongs, Slip/Env/Stretch pan, Tape plays the right channel forward and the left in reverse (manual pp.38–39). Width is adjustable in hidden options. With a stereo input (as in this rig) and SPREAD *off*, the incoming image is preserved.
- **Ramping** — internal modulation can auto-sweep any knob(s) as a one-shot ramp or continuous bounce, with selectable waveform (triangle/square/sine/random/smooth-random). MIX takes over ramp-speed duty when engaged (manual pp.46–47).

## 5. Signal-Chain Placement — Board 3, between Big Time and Blooper

Order on Board 3: `Generation Loss → Big Time → MOOD MkII → Blooper → Chroma Console → H90 → PORTA424 → JHS 424 → Apollo/FOH`. Observations for this exact slot:

- **After Big Time is correct.** MOOD wants something to chew on. Feeding it the Big Time's delay repeats (themselves fed by Generation Loss's tape wobble) gives the Micro-Looper rich, already-rhythmic, already-degraded material to grab — captured micro-loops inherit the delay/tape character "baked in" (manual p.41 warns the loop captures whatever the Wet/upstream signal is doing).
- **Before Blooper is the whole point.** MOOD is the *real-time mangler*; Blooper is the *committed song-length looper*. MOOD smears and warps in the moment, Blooper captures the result and lets you build it into a multi-minute structure. Running MOOD → Blooper means Blooper records MOOD's granular/slip textures as raw material. (Reverse order would make MOOD re-mangle Blooper's full loop — also valid, but loses the "capture the smear" workflow this rig is built around.)
- **Stereo through-path.** MOOD is one of the stereo-capable pedals on a stereo board; keep `MISO` **off** (you already have stereo in), and decide SPREAD per-patch. Note: **Blooper immediately downstream is mono** — so any stereo image MOOD creates collapses at Blooper unless you bypass Blooper or run MOOD's stereo width modestly. Flag for the owner: if wide MOOD stereo matters, it lives *upstream* of the mono Blooper and gets summed; the truly wide stereo lands later at Chroma Console / H90.
- **Downstream printing.** Chroma Console, H90, then the PORTA424 / JHS 424 tape stages all want a stable line-level stereo source, which MOOD delivers. MOOD's lo-fi degradation stacks with the tape-print aesthetic rather than fighting it.

## 6. Source-Specific Notes

- **Banjo loops (EBM-5 + GK-5 → VG-800):** the banjo-as-lead idea is where MOOD shines. Its always-listening Micro-Looper grabs a banjo phrase mid-performance; Tape mode at half-speed/octave-down turns a bright banjo roll into a low drone bed; Stretch mode smears a single banjo plucked note into a "sprawling epic." Because the banjo's signal is already heavily processed by the VG-800 → drive → tape chain by the time it reaches Board 3, MOOD is grabbing a *textured* banjo, not a raw one.
- **Baritone drones (Baritone Jazzmaster):** freeze the Wet reverb into an ambient pad, then play the baritone over the frozen bed — instant drone wall. Slip mode with MODIFY off the neutral position adds slow pitch-stepped harmonies under sustained baritone.
- **Modeled VG-800 pads:** continuous synth/pad output is ideal looper food — the Micro-Looper captures a sustained pad cleanly, and Stretch/Env then granularize it. This is the most direct route to the "sustained wall" aesthetic.
- **Bass (Jazz Bass):** MOOD is documented on bass (Mike Gordon of Phish, below). Keep Clock higher to preserve low-end definition; aggressive low-Clock downsampling thins bass fundamentals. Tape-mode octave-down on bass gets sub-drone territory fast.

## 7. Famous Users (honest)

MOOD has a real, if specific, following — ambient/experimental rather than rock-canon:

- **Andy Othling** (ambient guitarist, "Lowercase Noises") — wrote several of the **preset suggestions in the official manual**; a defining MOOD voice in the ambient-guitar world.
- **James Blake** — documented using a MOOD MkII in studio sessions (per [Equipboard](https://equipboard.com/items/chase-bliss-audio-mood-mkii)).
- **Mike Gordon** (Phish, bass) — documented running bass through the MOOD MkII (Equipboard).
- **Mike Stringer** (Spiritbox) — documented MOOD MkII user (Equipboard), notable as a heavier/metal-adjacent use.
- **Knobs** (Toronto videographer) — created the launch films for both V1 and the MkII; his demos define the pedal's public sound.

Beyond these, the MkII (2023) is recent enough that most of its mythology is in the ambient/looper YouTube and forum scene rather than named-artist signature use. *(Specific named-artist attributions above are sourced to Equipboard's listings, which are user-maintained — treat as documented-but-not-official.)*

## 8. Live / Power / I/O

| Aspect | Detail |
|---|---|
| Power | 9V DC, center-negative, **~270 mA** — high draw, needs a beefy isolated slot (manual p.4) |
| I/O | Stereo in / stereo out (TRS or dual-mono); mono and mono→stereo via `MISO` |
| Bypass | **Buffered bypass with trails**; true-bypass available by tapping both footswitches 3× (looper won't run in true-bypass, manual p.17) |
| MIDI | Full — note, PC, CC, **clock sync**; requires a Chase Bliss MIDIbox to convert to the ⅛" TRS jack (manual pp.48–49). **The full official CC chart now lives at [`research/links/midi-official-cc-chart.md`](links/midi-official-cc-chart.md)** — this DeepResearch is no longer the sole MIDI authority; consult that link for the per-parameter CC numbers. |
| CV / Expression | EXP/CV jack, 0–5V (any negative/over-voltage can damage it); controls any knob(s) or defaults to MIX (manual pp.48–49) |
| External footswitch | The MIDI/EXT jack accepts a normally-open momentary footswitch to engage the Wet Channel (manual p.49) |
| Presets | 2 (left/right toggle); dip settings save with presets |
| Dimensions / build | Standard Chase Bliss aluminum enclosure; two footswitches |

Live caveats: it's a **270 mA** pedal — do not under-power it. Buffered bypass means it passes signal sanely in a chain but the always-listening looper needs power to function. For a heavily-MIDI'd CB rig, MOOD slaving to **MIDI clock** is the move (see §9).

## 9. Pairing Recommendations (by name)

- **Big Time (immediately upstream):** the ideal feed — rhythmic, degraded delay repeats are perfect Micro-Looper bait. Sync MOOD's loop length to the Big Time's timing via MIDI clock for in-time captures.
- **Blooper (immediately downstream) — the key relationship:** MOOD = real-time *smear/granular mangler* on short fistfuls of audio; Blooper = the *committed, song-length looper* (16 overdubs, 8 layers of undo/redo, additive recording — per [Chase Bliss Blooper page](https://www.chasebliss.com/blooper)). Workflow: MOOD warps the moment → Blooper captures and builds it into a structure. Don't ask MOOD to be your main looper; don't ask Blooper to do real-time granular.
- **Hologram Microcosm (Board 2, upstream) — the other key relationship:** Microcosm is the **generative granular/loop engine** that builds evolving rhythmic phrases and pads *early* in the chain; MOOD is the **lo-fi smear/time-warp** *late* in the chain. Microcosm sets up textures going in; MOOD degrades and freezes textures coming out. They occupy opposite ends of the rig deliberately.
- **MIDI clock across the CB ecosystem:** with Generation Loss, Big Time, MOOD, Blooper (and Brothers AM / Clean upstream) all CB and MIDI-capable, slave MOOD's Clock-derived timing to a master clock so loops, delays, and ramps lock together — and use PC messages for scene recall across the system.
- **Into Chroma Console / H90:** MOOD's frozen/granular output is excellent material for the H90's spectral algorithms and Chroma Console's character processing downstream.

## 10. Reviews & Demos

- [Guitar.com — "Chase Bliss Mood MkII review: A knob-twiddler's delight"](https://guitar.com/reviews/effects-pedal/the-big-review-chase-bliss-mood-mkii/) — 9/10; best written review, strong on the two-channel interaction and stereo.
- [Synth Anatomy — MOOD MkII overview](https://synthanatomy.com/2024/03/chase-bliss-mood-mkii-micro-looper-multi-fx-pedal-takes-the-stereo-route.html) — clearest summary of what changed from V1.
- [GuitarPedalX — MOOD MkII reboot writeup](https://www.guitarpedalx.com/news/gpx-blog/chase-bliss-reboots-its-mood-micro-looper--ambience-generator-with-significant-enhancements-including-stereo-and-overdubbing) — feature-by-feature V1→MkII.
- [Sinesquares — First Look & Thoughts](https://www.sinesquares.net/musicgear/chase-bliss-mood-mkii-release) — hands-on impressions, clock-noise comparison.
- [MusicRadar — MOOD MkII reveal](https://www.musicradar.com/news/chase-bliss-mood-mkii) — launch coverage.
- [YouTube — "Chase Bliss Mood MKII: Reverb, Delay & Looper"](https://www.youtube.com/watch?v=RQcTZRnyauo) — walkthrough demo.
- [Knobs — original MOOD launch film](https://www.youtube.com/watch?v=G_BLyPxShG4) — the canonical demo aesthetic.
- [Chase Bliss MOOD MkII product page](https://www.chasebliss.com/mood-mkii) — official specs and feature list.

## 11. Mods / Quirks / Firmware

- **Firmware 1.1** (free) restored the original cloudy/wispy **Stretch** character inside **Classic Mode** — install it if you want the V1 Stretch flavor ([Chase Bliss on X](https://x.com/chasebliss/status/1770843989480005855); update via the [Bliss Programmer](https://firmware.chasebliss.com/)).
- **Classic Mode** is itself the "mod" — it reintroduces V1 misbehaviors (full clock noise, gradual loop deterioration, ringy reverb, warped delay pitch-bends, uneven slip, length-knob chopping). Great for the "recorded-wrong" aesthetic; flick the `CLASSIC` dip (manual pp.42–43).
- **Always-listening quirk:** because the Micro-Looper is always recording, what you capture depends on what was playing a moment ago — including any Wet/upstream effects "baked in." Capturing through the Reverb bakes the ambience into the loop permanently (manual p.41). Plan captures accordingly.
- **No DUB / refresh mode** and **LATCH** interact: NO DUB drops looper feedback to 0 for a pseudo-live refresh; in Classic + NO DUB the loop output mutes while overdubbing to replicate a V1 record-and-release behavior (manual pp.43–45).
- **Hidden-options reset:** flick the preset toggle left-and-back 3× to reset all hidden options, then confirm with both footswitches (manual p.14).
- **Light Bright Edition** — limited cosmetic variant; functionally identical.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Type | Two-channel micro-looper + spatial multi-effect |
| Wet Channel modes | Reverb, Delay, Slip (OBNE-designed) |
| Micro-Looper modes | Env, Tape, Stretch (Drolo FX-designed) |
| Shared controls | Mix, Clock; Routing toggle; Presets toggle |
| Per-channel controls | Time/Length, Modify, Mode toggle, footswitch |
| Power | 9V DC center-negative, **~270 mA** |
| I/O | Stereo in / stereo out (TRS or dual TS); mono & MISO modes |
| Bypass | Buffered + trails (true-bypass selectable via footswitch combo) |
| MIDI | Note, PC, CC, clock sync (via Chase Bliss MIDIbox) |
| CV / Expression | EXP/CV jack, 0–5V; assignable to any knob(s)/MIX |
| Presets | 2 |
| Internal modulation | Ramping (one-shot ramp / continuous bounce; 5 waveforms) |
| Stereo features | Spread (per-mode), Stereo Width, Spread Solo |
| Firmware | 1.1 (restores V1 Stretch in Classic Mode) |
| Price (launch) | $399 |
| Released | March 2023 (announced), shipped late April 2023 |

Source: [Chase Bliss MOOD MkII product page](https://www.chasebliss.com/mood-mkii) and the [MOOD MkII manual](../manuals/MOOD+MKII_Manual_Pedal_Chase+Bliss.pdf).

## 13. Starting-Point Settings

Reference patches for this rig. Knob positions are clock-face. Assume stereo in from Board 2, fed by Big Time upstream.

**(a) Frozen micro-loop drone** — sustained wall under the baritone/banjo
- Wet: **Reverb**, TIME 2:00, MODIFY 1:00 (heavy smear)
- Micro-Looper: **Tape**, LENGTH noon, MODIFY at half-speed (octave-down)
- Clock: 11:00 (a little grit); Mix 1:00; Routing `IN+micro-loop`
- Play a phrase, tap Micro-Looper to capture, HOLD Wet to freeze the reverb into a pad, then play over it.

**(b) Slip-reverb smear** — pitch-stepped harmonized haze
- Wet: **Slip**, TIME 11:00 (instant-ish), MODIFY just off neutral for a +/- a few semitones
- Micro-Looper: off (or Env at low sensitivity)
- Clock: noon; Mix noon; `SPREAD` on for scatter
- For the doom drift, freeze Slip into its "glitchy synth" and play under it.

**(c) Granular stutter** — chopped, arcade-glitch texture
- Micro-Looper: **Env**, LENGTH 9:00 (small slices), MODIFY low (high sensitivity)
- Wet: **Reverb**, MODIFY low (multi-tap clusters)
- Clock: 10:00 (aliased/lo-fi); play, then go quiet so Env freezes the last slice and stutters it.
- Add `CLASSIC` dip for extra grit.

**(d) Clock-synced loop layer** — in-time loop locked to the rig
- Micro-Looper: **Tape**, LENGTH set by Clock; `SYNC` (hidden) → Micro-Looper synced to Wet
- Wet: **Delay**, TIME quarter-note feel, MODIFY 1:00 (piling repeats)
- Feed MIDI clock from the rig's master so the loop locks to Big Time/Blooper.
- Capture in time, then commit to Blooper downstream.

## 14. Versus Alternatives — Why It Earns Its Slot

The honest competition for MOOD is the rig's own two other loop/granular devices, not outside pedals — so the "versus" here is the division of labor:

- **vs Chase Bliss Blooper (downstream):** Blooper is the **full looper** — long loops, 16 overdubs, 8-layer undo/redo, additive live-editing, song-length structure ([Blooper page](https://www.chasebliss.com/blooper)). MOOD is the **micro / real-time** counterpart — short always-listening loops, instant smear, granular and pitch-warp engines, freeze. MOOD warps the moment; Blooper builds the song. They're complementary, and the chain order (MOOD → Blooper) lets Blooper capture MOOD's textures.
- **vs Hologram Microcosm (Board 2, upstream):** Microcosm is the **generative granular sequencer** — it builds evolving rhythmic loops/pads from your playing with built-in delay/reverb and tap-tempo, early in the chain to *set up* textures. MOOD is the **lo-fi time-warp/smear** late in the chain to *degrade and freeze* textures. Microcosm is more "in-context" and production-ready; MOOD is more immediate and more willing to break ([Gearspace/KVR discussions](https://gearspace.com/board/so-many-guitars-so-little-time/1353956-anyone-using-hologram-microcosm.html)). Putting them on opposite boards is deliberate — generate going in, mangle coming out.
- **vs a generic stereo reverb/delay (e.g. bench Big Sky / Del-Verb):** those are clean, polished space. MOOD is *intentional degradation* — sample-rate crush, granular fracture, pitch-stepped slip. It earns its slot precisely because nothing else in the rig does real-time lo-fi micro-looping and granular smear in stereo.

In this rig — banjo-as-lead, baritone drones, a "recorded-wrong" tape-and-degradation aesthetic — MOOD is the right pedal for Board 3 position 3 because it (1) feeds on the already-degraded Big Time output, (2) hands committed loops to Blooper cleanly, and (3) occupies the granular/loop niche opposite the Microcosm without overlapping it. Three loop/granular devices, three clearly different jobs: **Microcosm generates, MOOD warps, Blooper commits.**

## Sources

- [Chase Bliss — MOOD MkII product page](https://www.chasebliss.com/mood-mkii)
- [MOOD MkII manual (local PDF)](../manuals/MOOD+MKII_Manual_Pedal_Chase+Bliss.pdf)
- [Chase Bliss — Blooper product page](https://www.chasebliss.com/blooper)
- [Guitar.com — Chase Bliss Mood MkII review (9/10)](https://guitar.com/reviews/effects-pedal/the-big-review-chase-bliss-mood-mkii/)
- [Synth Anatomy — MOOD MkII takes the stereo route](https://synthanatomy.com/2024/03/chase-bliss-mood-mkii-micro-looper-multi-fx-pedal-takes-the-stereo-route.html)
- [GuitarPedalX — Chase Bliss reboots the MOOD micro-looper](https://www.guitarpedalx.com/news/gpx-blog/chase-bliss-reboots-its-mood-micro-looper--ambience-generator-with-significant-enhancements-including-stereo-and-overdubbing)
- [GuitarPedalX — MOOD MkII Light Bright Edition](https://www.guitarpedalx.com/news/gpx-blog/chase-bliss-releases-super-appealing-2nd-limited-variant-of-the-mood-mkii---the-2000-run-light-bright-edition)
- [Sinesquares — MOOD MkII First Look & Thoughts](https://www.sinesquares.net/musicgear/chase-bliss-mood-mkii-release)
- [MusicRadar — Chase Bliss MOOD MkII reveal](https://www.musicradar.com/news/chase-bliss-mood-mkii)
- [Equipboard — Chase Bliss MOOD MkII (artist listings)](https://equipboard.com/items/chase-bliss-audio-mood-mkii)
- [Chase Bliss on X — 1-year firmware 1.1 / Light Bright announcement](https://x.com/chasebliss/status/1770843989480005855)
- [Bliss Programmer (firmware updater)](https://firmware.chasebliss.com/)
- [YouTube — Chase Bliss Mood MKII: Reverb, Delay & Looper demo](https://www.youtube.com/watch?v=RQcTZRnyauo)
- [YouTube — Knobs: original MOOD launch film](https://www.youtube.com/watch?v=G_BLyPxShG4)
- [Gearspace — Hologram Microcosm discussion (MOOD/Microcosm comparison)](https://gearspace.com/board/so-many-guitars-so-little-time/1353956-anyone-using-hologram-microcosm.html)
- [KVR Audio — Generative looping discussion (Microcosm vs Mood)](https://www.kvraudio.com/forum/viewtopic.php?t=568505)
