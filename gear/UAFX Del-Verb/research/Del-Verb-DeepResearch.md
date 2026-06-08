# Universal Audio UAFX Del-Verb — Deep Research

A working dossier for a pedal that lives **on the bench** in this rig, not on a board. The Del-Verb is UA's "Ambience Companion": the reverb engines from the [Golden Reverberator](https://www.musicradar.com/reviews/universal-audio-uafx-golden-reverberator-starlight-echo-station-and-astra-modulation-machine-pedals) and the delay engines from the [Starlight Echo Station](https://www.musicradar.com/reviews/universal-audio-uafx-del-verb-ambience-companion-delay-and-reverb-pedal) fused into one stereo box, app-controlled, dead simple. In a rig that already runs an Eventide H90, a Chase Bliss Big Time, an OBNE Dark Star V3 and a Walrus QI Etherealizer, it has no honest seat at the table — the rig sheet's verdict is exactly right: *"Subsumed by H90. Travel board only."* So most of this document is about the one place it genuinely wins: a tiny fly/travel board, ideally next to the owner's UA Apollo x8.

## 1. Lineage: two UAFX flagships in one suitcase

The Del-Verb is not a new algorithm set — it's a **greatest-hits compilation**. UA took the three reverbs from the Golden Reverberator and the three delays from the Starlight Echo Station, dropped the per-pedal preset switch, and bolted them into a single dual-engine enclosure. Per [MusicRadar's review](https://www.musicradar.com/reviews/universal-audio-uafx-del-verb-ambience-companion-delay-and-reverb-pedal), the delay side emulates "an Echoplex EP-3, an Electro-Harmonix Memory Man Deluxe and a digital delay," and the reverb side "a Fender '65 Spring reverb, an EMT 140 plate and the Lexicon 224 digital reverb." It was announced at [NAMM 2023](https://www.musicradar.com/news/universal-audio-reveals-4-new-uafx-pedals-with-the-del-verb-ambience-companion-galaxy-74-tape-echo-and-reverb-and-max-preamp-and-dual-compressor) alongside the Galaxy '74 and Max, and lands at **$349 / £325 / €379**.

The bigger lineage story is the **ecosystem**. UAFX runs on UA's dual-DSP guitar platform, and while UA is careful to say the pedal algorithms are "recoded and tweaked specifically for guitar" rather than literal ports, several of these reverb/delay names trace to the same heritage as UAD plug-ins ([FAQ: UAFX Pedals](https://help.uaudio.com/hc/en-us/articles/360058000092-FAQ-UAFX-Pedals)). For an owner with an [Apollo x8](https://www.uaudio.com), that matters: the Del-Verb is the same sonic family as the UAD spring/plate/hall and tape-echo processors they can already print in the box. More on that synergy in §9.

## 2. Controls and the two engines

The face has six knobs and two footswitches, but the layout is deliberately lopsided — the delay gets the deep controls, the reverb gets almost nothing.

**Delay knobs (left cluster):**
- **Delay Time** — range varies by model (see table in §3). Quarter-note tempo can also be tapped with the right footswitch when Tap Tempo mode is enabled in the app.
- **Feedback** — number of repeats. Tape EP-III and Analog DMM self-oscillate past ~3 o'clock; Precision repeats indefinitely at max but does **not** self-oscillate.
- **Mix** — delay level against dry. Fully clockwise = 100% wet / kill dry.
- **Color** — input gain / tone depending on model (overdrive + harmonics on Analog DMM; treble tilt on Precision).
- **Mod** — a two-zone bipolar knob: left half = one modulation type, right half = another, **noon = off** (e.g. on Analog DMM, left = Vibrato, right = Chorus).

**Reverb controls (right side):** a 3-way **Reverb Effect** mini-toggle and a single **Reverb** level knob. That's it. Fully counter-clockwise = no reverb; fully clockwise = 100% wet / kill dry. There is **no decay, no tone, no pre-delay on the hardware** — those live in the app's "voicings." This is the single biggest functional gap versus an H90 and the cleanest reason it gets benched (§5).

**Footswitches** are mode-dependent (set in the UAFX Control app):
- **Delay | Reverb (default):** left toggles delay, right toggles reverb.
- **Effects | Tap Tempo:** left toggles both effects; right taps delay tempo.
- **Delay | Tap Tempo:** left toggles delay; right taps tempo; reverb is always on, leveled by the Reverb knob.

## 3. Sonic character — the six models

The delays mirror the Starlight; the reverbs mirror the Golden. Model descriptions and ranges are from the [official manual](https://help.uaudio.com/hc/en-us/articles/13621234251284-UAFX-Del-Verb-Ambience-Companion-Manual).

**Delays:**
- **TAPE EP-III** — full circuit emulation of an early-'70s Maestro EP-III tape echo: wow/flutter randomness, splice artifacts, the whole eccentric package. The Mod knob crossfades **New tape (left) ↔ Worn tape (right)** for color. Delay pitch shifts with time changes (true tape behavior).
- **ANALOG DMM** — bucket-brigade delay modeled on late-'70s/early-'80s EHX Deluxe Memory Man units, "right down to the unpredictable clock rate dumping" for those "whoosh" effects. Color adds overdrive past noon; Mod = **Vibrato (left) / Chorus (right)**. Pitch shifts with time.
- **PRECISION** — UA's own clean modern digital delay: pristine mirror-image repeats, studio-grade flange/chorus textures, ping-pong. Pitch does **not** shift with time changes (except "glide" voicings). The most "transparent" of the three.

**Reverbs:**
- **SPRING '65** — "golden unit" spring tank pulled from a classic '60s American guitar amp; drip, clang, whistle and tube-clipping overtones. Surfy, splashy, the least ambient of the three.
- **PLATE 140** — dense EMT-140-style studio plate sourced from The Plant studio in Sausalito, CA. Warm, hazy, the most musically flattering for sustained chords.
- **HALL 224** — a bit-for-bit Lexicon-224-style digital hall: lush, grainy tails and "mesmerizing modulation textures." The closest thing the pedal has to an ambient-wash machine, and the one a drone/shoegaze player will live on.

| Delay model | Time range | Pitch shifts with time? |
|---|---|---|
| Tape EP-III | 80–700 ms | Yes |
| Analog DMM | 110–1068 ms | Yes |
| Precision | 120–1500 ms | No* |

\*Precision pitch shifts only on "glide" voicings. (Source: manual.)

## 4. Behavioral notes — stereo, trails, app, the missing presets

- **Dual stereo engines.** Each reverb and delay runs as a separate stereo instance — true stereo or dual-mono, with "stunning three-dimensional stereo depth" per UA's copy. The input is always **analog dry-through** and the output is always buffered, in both trails modes.
- **Trails on/off** is app-selectable. Trails Off kills delay/reverb the instant you bypass; Trails On lets tails ring out. Self-oscillation runs in the background even when bypassed in Trails Off, and returns when you re-enable.
- **Voicings, not presets (mostly).** The deep parameters — reverb decay/tone/pre-delay, alternate tape characters, modulation flavors — are **factory "voicings"** you assign per effect in the [UAFX Control app](https://help.uaudio.com/hc/en-us/articles/360058187832-UAFX-Control-Manual). MusicRadar reports "12 choices for Analog DMM and 12 for Spring 65," for example. Knob and tempo settings are remembered per effect when you switch types.
- **No onboard user presets — this is the pedal's defining limitation.** Reviewers flag it consistently ([MusicRadar](https://www.musicradar.com/reviews/universal-audio-uafx-del-verb-ambience-companion-delay-and-reverb-pedal): "lacking onboard user presets"). You dial sounds by hand or recall app voicings.
- **The November 2025 UAFX 2.0 firmware narrows but does not close the gap.** Per [UA's announcement](https://www.uaudio.com/blogs/press/new-uafx-pedal-update-adds-midi-connectivity-and-more), pedals *without* preset saving — explicitly **Max, Galaxy '74, and Del-Verb** — gained **MIDI CC snapshots** (recallable via an external controller) plus **MIDI clock tempo sync**. So the Del-Verb still can't store a footswitch-recallable preset on its own; it needs a MIDI brain in front of it to behave like a preset machine. *(Verified to the Nov 2025 update; check for newer firmware.)*

## 5. Bench placement — why it's off the board, and where it belongs

**Why it's benched (the honest case).** The Del-Verb's job is delay + reverb. In this rig that job is already done three times over by deeper tools, all of them stereo and all of them already on boards:

- **Eventide H90 (Board 3)** is a dual-engine delay/reverb/pitch machine with hundreds of algorithms, **onboard presets**, deep parameter editing, MIDI, and per-program routing. Anything the Del-Verb does, the H90 does with a decay control, a tone control, and a preset slot the Del-Verb doesn't have. This is the literal "subsumed by H90" verdict, and it's correct.
- **OBNE Dark Star V3 (Board 2)** owns the pad/smear reverb territory the Del-Verb's Hall 224 only gestures at.
- **Walrus QI Etherealizer (Board 2)** owns the ambient/granular wash.
- **Chase Bliss Big Time (Board 3)** covers stereo delay with far more control and CB's modulation/routing depth.

Add the **no-onboard-presets** problem and the **no-reverb-decay-knob** problem, and on a full board the Del-Verb is a worse version of tools the rig already owns. Benching it is not a knock on the pedal — it's a knock on redundancy.

**Where it's the right tool (the travel/fly case).** Strip the rig down to a carry-on board and the math inverts. The Del-Verb gives you a **legitimately great spring, plate, and hall plus a tape, BBD, and digital delay in one ~400 mA box** with stereo I/O — that is an entire ambient rig in a single enclosure. For a fly date, a writing trip, or a backup board, it covers 90% of what most players need for delay+reverb and sounds like UA's flagships doing it. The simplicity that makes it redundant at home is exactly what makes it *correct* on the road: one box, six classic sounds, no menu-diving, no laptop. That is the role this dossier endorses.

## 6. Source-specific notes (banjo, baritone, VG-800, bass)

This pedal sits at the *end* of a chain, after everything else, so it sees a summed, processed signal — its behavior is source-agnostic in the way a fuzz isn't. Still, for this rig's instruments:

- **Gold Tone EBM-5 banjo (GK-5 → VG-800).** Banjo is bright and transient-dense. **Plate 140** is the friendliest reverb here — it rounds the attack and fills space without the splashy ice-pick that Spring '65 can add to banjo's 2–4 kHz spikes. For banjo-as-lead, **Precision delay** (clean, pitch-stable) keeps fast rolls articulate where the tape models would smear them.
- **Baritone Jazzmaster.** The low fundamental loves **Hall 224** for drone walls and **Tape EP-III** worn-tape for grit on the repeats. Watch Feedback near self-oscillation — on a baritone the runaway gets subsonic fast.
- **VG-800 modeled signal.** Because the Del-Verb is all post-cab, it treats a VG-800 amp/synth model like any line source. Pad and synth patches into **Hall 224 + dotted Precision delay** is the most "instant ambient" combo the box offers — and it's the patch you'd actually want on a travel board.
- **Bass (Pro Jazz Bass).** Keep delay Mix low and lean on **Plate 140** at modest level; the analog dry-through preserves low-end punch, which is why the pedal is bass-friendly per [TalkBass](https://www.talkbass.com/threads/uas-del-verb-ambience-companion-demo-review.1608895/).

## 7. Famous users (honest)

There is no signature-artist mythology here — the Del-Verb is a curated convenience box, not a tone-chaser's grail, and it's young (2023). The credible endorsement is the **UA-featured demoist roster** (e.g. the [R.J. Ronquillo in-depth demo](https://www.youtube.com/watch?v=8q2FBlLoGWI) — *his own channel, not a UA-official upload; verified via yt-dlp*) and the broader UAFX artist pool that uses the Golden/Starlight engines this pedal is built from. (Note: UA's *named* endorsers — Pete Thorn, Blues Saraceno, James Santiago — attach to the AMP pedals like the Lion, not the Del-Verb.) Anyone you see citing "the Golden's plate" or "the Starlight's EP-III" is, sonically, citing the Del-Verb. Don't expect a Wata-style "this is *the* pedal" story; that's not what this is.

## 8. Live / power / I/O

- **Power:** Isolated **9V DC, center-negative, 400 mA minimum**, 2.1 × 5.5 mm barrel. This is a heavy draw — budget a high-current isolated slot. UA requires an LPS-compliant supply.
- **I/O:** 2 × ¼" unbalanced TS inputs (input 2 = right for stereo), 2 × ¼" unbalanced TS outputs (output 2 = right for stereo). Mono or true-stereo/dual-mono.
- **Impedance:** 500 kΩ input (mono) / 1 MΩ (stereo); 500 Ω output. Max in/out level 12.2 / 12.1 dBu. Frequency response 20 Hz–20 kHz ±1 dB.
- **Bypass:** Buffered bypass with switchable trails. Analog dry-through always. Silent switching.
- **USB-C** for registration/firmware (and, post-2.0, MIDI over USB). **Bluetooth v5** for the UAFX Control app.
- **MIDI:** No 5-pin DIN; MIDI is **over USB** only (CC, program/snapshot, clock sync) per the 2.0 update.
- **Dimensions:** standard full-size dual-footswitch UAFX enclosure; height ~2.56 in / 6.5 cm. *(Full width/depth/weight not captured from the manual page — flag as unverified; treat as the same footprint as the Golden/Starlight.)*

## 9. Pairing recommendations (by name)

- **vs. H90 (Board 3):** don't. On a full board the H90 wins on every axis. Keep the Del-Verb off the main board.
- **vs. Dark Star V3 / QI Etherealizer (Board 2):** the Del-Verb's Hall 224 is a *cleaner, more conventional* ambient than either OBNE/Walrus texture box — useful as a "normal pretty reverb" reference, but those two own the broken/granular aesthetic this player actually wants.
- **The travel board (recommended home):** Del-Verb + a single drive + a tuner = a complete fly rig. Pair it with the **JHS Kilt v10** or **Brothers** (also bench-able for travel) for dirt in front, and you have walls-of-sound capability in a backpack.
- **UA Apollo x8 synergy (the real edge):** the Del-Verb's reverb/delay heritage overlaps UA's UAD spring/plate/hall and tape processors. On a travel/writing setup you can track the **same sonic family** through the pedal live and then re-create or extend it in the box on the Apollo — a coherence no H90 gives you. For an all-UA mobile workflow, this is the Del-Verb's quiet superpower.

## 10. Reviews and demos (real links)

- [MusicRadar — Del-Verb review](https://www.musicradar.com/reviews/universal-audio-uafx-del-verb-ambience-companion-delay-and-reverb-pedal) — "the greatest selection of reverb and delay sounds in one pedal," also the clearest on the no-presets / no-reverb-controls limitations.
- [MusicTech — Del-Verb review](https://musictech.com/reviews/studio-recording-gear/universal-audio-uafx-del-verb-review/) — "all-in-one ambience machine."
- [GuitarPlayer — Del-Verb review](https://www.guitarplayer.com/reviews/universal-audio-del-verb-ambience-companion-review).
- [Guitar.com — "an appetising ambient buffet"](https://guitar.com/reviews/effects-pedal/universal-audio-uafx-del-verb-review/).
- [Magnetic Magazine — review](https://magneticmag.com/2024/05/del-verb-ambience-companion-review-unpacking-universal-audios-amazing-spatial-pedal/).
- [R.J. Ronquillo — in-depth demo (YouTube)](https://www.youtube.com/watch?v=8q2FBlLoGWI) — *UA-featured demoist's own channel (not a UA-official upload); the tone reference, light on spoken settings. Corrected from "official UA demo" via yt-dlp.*
- [Bonedo Synthesizers — no-talking demo (YouTube)](https://www.youtube.com/watch?v=ge_ORIwQyws) — *note: this is an **OB-6 synth-source** demo on the Bonedo Synthesizers channel, not a guitar sound demo. Corrected from "Del-Verb sound demo, no talking" via yt-dlp.*
- [Thomann — Del-Verb / Max / Galaxy '74 gear check (YouTube)](https://www.youtube.com/watch?v=Myx7zKVW1Vs).
- [TalkBass — Del-Verb demo/review thread](https://www.talkbass.com/threads/uas-del-verb-ambience-companion-demo-review.1608895/) — best for bass use.
- [MusicRadar — Golden / Starlight / Astra review](https://www.musicradar.com/reviews/universal-audio-uafx-golden-reverberator-starlight-echo-station-and-astra-modulation-machine-pedals) — the source pedals, deeper on each engine.

## 11. Mods / quirks / firmware

- **No mods** — it's a sealed digital pedal; "no user-replaceable parts" per the manual.
- **Firmware is the story.** Keep it current with UA Connect / UAFX Control. The **UAFX 2.0 firmware (Nov 11, 2025)** added MIDI-over-USB (CC, snapshots, clock sync) to the Del-Verb; the pedal still has no onboard preset switch ([UA press](https://www.uaudio.com/blogs/press/new-uafx-pedal-update-adds-midi-connectivity-and-more), [Magnetic](https://magneticmag.com/2025/11/universal-audio-upgrades-uafx-pedals-with-full-usb-midi-control/)). The **online/PDF manual is now dated Dec 22 2025** (newer than the Nov-2025 press) and adds a dedicated "Del-Verb MIDI CCs" section: the official send order is **bypass → effect-select → params** (effect-select snaps knobs to their physical panel positions, so params must follow it), and **CC-20 Reverb Bypass works regardless of footswitch mode**. The "snapshot" is **CC-only (no Program Change)** and lives on the *controller*, not the pedal. *(Verified to the Dec 2025 manual; later firmware may change this.)*
- **Quirk — runaway audio survives bypass.** With high feedback set to self-oscillate, turning the pedal off doesn't stop it (it runs in the background in Trails Off, keeps playing in Trails On). To kill it, drop Feedback to minimum. Worth knowing before a quiet section.
- **Quirk — kill-dry at max Mix/Reverb.** Both wet knobs mute the dry signal when fully clockwise. Useful for parallel/aux setups, surprising if you don't expect it.
- **Quirk — the missing reverb knobs.** If a sound is "almost right but the tail is wrong," you cannot fix it on the hardware — you must change the app voicing. Plan voicings before a gig.

## 12. Spec sheet

| Spec | Value |
|---|---|
| Effects | 3 delays (Tape EP-III, Analog DMM, Precision) + 3 reverbs (Spring '65, Plate 140, Hall 224) |
| Engines | Dual stereo (separate stereo instances of delay and reverb) |
| Power | Isolated 9V DC, center-negative, 400 mA min, 2.1 × 5.5 mm barrel |
| Inputs | 2 × ¼" unbalanced TS (input 2 for stereo) |
| Outputs | 2 × ¼" unbalanced TS (output 2 for stereo) |
| Input impedance | 500 kΩ (mono in) / 1 MΩ (stereo in) |
| Output impedance | 500 Ω |
| Max input / output level | 12.2 dBu / 12.1 dBu |
| Frequency response | 20 Hz – 20 kHz, ±1 dB |
| Bypass | Buffered, switchable trails; analog dry-through; silent switching |
| Presets | None onboard; factory "voicings" via app; MIDI CC snapshots (Nov 2025 fw) |
| MIDI | Over USB only (CC, program/snapshot, clock sync); no 5-pin DIN |
| Connectivity | USB-C (firmware/MIDI), Bluetooth v5 (app) |
| App | UAFX Control (iOS/Android) — voicings, footswitch mode, trails, tap |
| Dimensions | Full-size UAFX enclosure; height ~2.56 in / 6.5 cm (full W/D/weight unverified) |
| Price | $349 / £325 / €379 |

Sources: [official manual](https://help.uaudio.com/hc/en-us/articles/13621234251284-UAFX-Del-Verb-Ambience-Companion-Manual), [product page](https://www.uaudio.com/guitar-pedals/del-verb-ambience-companion.html).

## 13. Starting-point settings

Clock-face positions, looking down at the pedal.

**(a) Simple ambient travel patch** — the reason to own it on a fly board
- Reverb: **Hall 224**, level 11–12
- Delay: **Precision**, Time = dotted-eighth (tap to song), Feedback 9–10, Mix 9, Color noon, Mod off (noon)
- Trails: On. One box, instant ambience, nothing to think about.

**(b) Slap + plate** — clean studio shimmer for tracking into the Apollo
- Reverb: **Plate 140**, level 10–11
- Delay: **Precision**, Time ~120–150 ms (slap), Feedback minimum, Mix 9, Color slight treble
- Great for clean banjo-as-lead and rhythm comping.

**(c) Dub delay** — tape feedback play
- Reverb: **Spring '65**, level 9 (drip behind the repeats)
- Delay: **Tape EP-III**, Time to taste, Feedback 2–3 o'clock (edge of self-oscillation), Mix 11, Mod toward Worn tape
- Ride Feedback by hand; drop it to min to kill runaway.

**(d) Shimmer wash** — drone/doom wall on a minimal board
- Reverb: **Hall 224**, level 1–2 o'clock (big)
- Delay: **Analog DMM**, Time long (~800 ms+), Feedback 1–2 o'clock, Mix noon, Mod toward Chorus, Color past noon for grit
- Baritone neck pickup, let it bloom. Closest the Del-Verb gets to the home rig's aesthetic.

## 14. Versus alternatives — and the verdict

- **vs. Eventide H90:** not a contest on capability — H90 wins on depth, presets, routing, algorithm count. The Del-Verb wins *only* on size, simplicity, instant-on workflow, and price. On a full board, H90; on a fly board, Del-Verb.
- **vs. Strymon Big Sky / TimeLine (also benched):** the Strymon pair is the deeper, more flexible single-purpose option — but it's *two* pedals and a bigger power/space footprint. The Del-Verb is one box doing both jobs adequately. For travel, the Del-Verb's all-in-one nature beats carrying two Strymons.
- **vs. Boss/Walrus/Keeley combo verbs (e.g. Walrus Slö + a delay):** the Del-Verb's authenticity and UA-ecosystem coherence edge those out *for this owner specifically*, because of the Apollo synergy.
- **vs. selling it:** don't. The bench is the right place, not the classifieds. It's the cheapest path to a credible UA-voiced ambient rig that fits in a gig bag.

**Verdict on the bench decision: correct, and well-reasoned.** In the full three-board rig the Del-Verb is genuinely subsumed — the H90 alone covers everything it does with controls and presets the Del-Verb lacks, and the Dark Star/QI own the textural ambient this player actually chases. There is no honest argument for putting it back on a board. But it is **not** a sell candidate: its real, defensible role is a **single-box travel/fly delay+reverb** that sounds like UA's flagships and slots cleanly into the owner's all-UA Apollo workflow. Keep it benched, keep it travel-ready, and reach for it the day the carry-on board matters more than the wall of sound.

## Sources

- [Universal Audio — Del-Verb Ambience Companion product page](https://www.uaudio.com/guitar-pedals/del-verb-ambience-companion.html)
- [Universal Audio Support — UAFX Del-Verb Ambience Companion Manual](https://help.uaudio.com/hc/en-us/articles/13621234251284-UAFX-Del-Verb-Ambience-Companion-Manual)
- [Universal Audio Support — UAFX Control Manual](https://help.uaudio.com/hc/en-us/articles/360058187832-UAFX-Control-Manual)
- [Universal Audio Support — FAQ: UAFX Pedals](https://help.uaudio.com/hc/en-us/articles/360058000092-FAQ-UAFX-Pedals)
- [Universal Audio — New UAFX Pedal Update Adds MIDI Connectivity and More (UAFX 2.0, Nov 2025)](https://www.uaudio.com/blogs/press/new-uafx-pedal-update-adds-midi-connectivity-and-more)
- [Universal Audio — Unlock UAFX with USB MIDI Control](https://www.uaudio.com/blogs/ua/unlock-uafx-with-usb-midi-control)
- [MusicRadar — UAFX Del-Verb Ambience Companion review](https://www.musicradar.com/reviews/universal-audio-uafx-del-verb-ambience-companion-delay-and-reverb-pedal)
- [MusicRadar — Golden Reverberator / Starlight / Astra review](https://www.musicradar.com/reviews/universal-audio-uafx-golden-reverberator-starlight-echo-station-and-astra-modulation-machine-pedals)
- [MusicRadar — NAMM 2023 UAFX Del-Verb / Galaxy '74 / Max announcement](https://www.musicradar.com/news/universal-audio-reveals-4-new-uafx-pedals-with-the-del-verb-ambience-companion-galaxy-74-tape-echo-and-reverb-and-max-preamp-and-dual-compressor)
- [MusicTech — UAFX Del-Verb review](https://musictech.com/reviews/studio-recording-gear/universal-audio-uafx-del-verb-review/)
- [GuitarPlayer — Del-Verb review](https://www.guitarplayer.com/reviews/universal-audio-del-verb-ambience-companion-review)
- [Guitar.com — Del-Verb review](https://guitar.com/reviews/effects-pedal/universal-audio-uafx-del-verb-review/)
- [Magnetic Magazine — Del-Verb review](https://magneticmag.com/2024/05/del-verb-ambience-companion-review-unpacking-universal-audios-amazing-spatial-pedal/)
- [Magnetic Magazine — UAFX full USB MIDI control (Nov 2025)](https://magneticmag.com/2025/11/universal-audio-upgrades-uafx-pedals-with-full-usb-midi-control/)
- [TalkBass — Del-Verb demo/review thread](https://www.talkbass.com/threads/uas-del-verb-ambience-companion-demo-review.1608895/)
- [Universal Audio — Del-Verb in-depth demo (YouTube)](https://www.youtube.com/watch?v=8q2FBlLoGWI)
- [Del-Verb sound demo, no talking (YouTube)](https://www.youtube.com/watch?v=ge_ORIwQyws)
- [Thomann — New UAFX pedals gear check (YouTube)](https://www.youtube.com/watch?v=Myx7zKVW1Vs)
- [Sweetwater — Del-Verb product/reviews](https://www.sweetwater.com/store/detail/UADelVerb--universal-audio-del-verb-ambience-companion-reverb-and-delay-pedal)
