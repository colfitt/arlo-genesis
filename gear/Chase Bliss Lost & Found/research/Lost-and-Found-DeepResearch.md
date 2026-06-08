# Chase Bliss Lost + Found — Deep Research

A working dossier for the Chase Bliss **Lost + Found** as it sits 2nd on Board 2 (Middle / Texture), wedged between the OBNE Parting filter and the Hologram Microcosm granular engine. The rig art tags this pedal "Random" (an *event* pedal), and that tag is the whole reason it earns this slot: Lost + Found is not a single effect but a stereo, dual-channel, twelve-mode "collection of curiosities" whose modes can be *internally modulated, MIDI-randomized, and clock-synced* — so what it actually injects into the middle of the stereo texture board is **controlled chaos and unexpected texture**, fed straight into the Microcosm's grain mill. Most of this document leans on the manual, because the pedal shipped in late 2025 and serious web coverage is still thin — where that's the case, it's flagged.

## 1. Lineage: what Lost + Found actually is

Lost + Found is **Chase Bliss's first true multi-effect** and the **second release in their "Small Batch Bliss" made-to-order line** (the cover of the field guide reads "Small Batch Bliss 2025 — L+F1"). Small Batch Bliss is a built-to-order model: there's no fixed run size — you order inside a month-long preorder window and they build one for you ([Chase Bliss](https://www.chasebliss.com/lost-and-found), [MusicRadar](https://www.musicradar.com/guitars/chase-bliss-lost-and-found-multi-effects-pedal)). Preorders ran **through August 31, 2025**, shipping in September 2025, at **$399 USD / €469** ([gearnews.com](https://www.gearnews.com/chase-bliss-lost-found-12-effects-144-combinations/), [SYNTH ANATOMY](https://synthanatomy.com/2025/08/chase-bliss-lost-found-a-multi-fx-pedal-packed-with-strange-but-inspiring-algorithms.html)).

The manual frames it as *"a little museum of the rare and strange... twelve modes that can be blended and combined in countless ways"* ([Lost + Found manual, p.2](manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf)). GuitarPedalX bills it as a "Stereo Multi-Modulator" ([GPX](https://www.guitarpedalx.com/news/gpx-blog/chase-blisss-latest-small-batch-limited-release-consists-of-a-2nd-edition-of-the-reverse-mode-c-and-brand-new-lost-found-stereo-multi-modulator-pedal)). Both are right: it's a stereo box with two independent effect **channels** (Left and Right), each able to load one of six modes, each mode with an A and B variant — **12 effects, 144 possible combinations**.

**What it is, precisely:** a stereo, dual-channel, preset-and-MIDI-capable multi-effect spanning reverb, pitch, modulation/"warp," delay, synth, and tape-bend. It is *not* a single chaos generator or a noise box — but its **internal modulation (ramp/bounce), per-mode RANDOM functions, and MIDI random-mode commands** are exactly why this rig tags it "Random." The "chaos" is an emergent property of how you drive it, not a dedicated circuit. (**Manual-vs-web note:** the official product page does *not* use the words "random" or "chaos" — that framing is the owner's, grounded in the MIDI RANDOM commands and the per-mode RANDOM/Drops-and-Snags behaviors documented below.)

One pedigree detail worth flagging for this rig: mode **6B is "Gen Lite," described in the manual as "a condensed version of our Generation Loss MKII tape simulator"** ([manual, p.31](manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf)). The owner already runs a full **CB Generation Loss** on Board 3 — so Lost & Found literally carries a mini-GenLoss upstream of it.

## 2. Controls, dip switches & hidden options

Six knobs, two footswitches, two preset/routing toggles, and **two banks of dip switches** ([manual pp.8–13](manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf)).

**Knobs (per channel, Left = mode 1–3, Right = mode 4–6):**
- **TIME** — sets the timing of the effect. By default all modes are **synced**, so this knob chooses the **subdivision** and stays in time. Turn off with the **UNSYNC** dip for free/asynchronous timing and a smoother sweep.
- **MODIFY** — bidirectional. It selects between the **A and B variant** of the channel's mode (turn one way for A, the other for B) *and* adjusts that effect's character. At **noon you get no effect**, which lets you run the GLUE compressor/saturator on its own.

**Global / center knobs:**
- **MIX (RAMP)** — wet/dry balance for both channels at once. When ramping is engaged, this knob's job changes to **set the ramp speed**.
- **BLEND** — balances the two channels. In **parallel (L+R)** it sets which channel is louder; in **series (L>R or L<R)** it sets the mix of the second effect in the chain.

**Toggles:**
- **ROUTING** — `L>R` (Left into Right, series), `L+R` (parallel), `L<R` (Right into Left, series).
- **PRESETS** — Left and Right positions hold a preset; middle is "live." A second internal bank (Presets 3 & 4) is reached via the **BANK** dip.

**Footswitches (Bypass):** Tap to engage that channel. **Hold for a mode-specific secondary function** — usually **FREEZE / INFINITE** (captures the current wet sound and loops it as a floating pad), but per-mode it's **PAUSE** (phaser), **PITCH FREEZE** (resonator), **TAPE STOP** (Gen Lite), etc.

**Dip switches — Control bank & Customize bank** ([manual pp.40–43](manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf)):
- **MISO** — Mono In, Stereo Out (splits a mono input to stereo).
- **SPREAD** — turns on stereo processing for an expansive image; each mode spreads differently. **SPREAD ROUTING** toggle applies spread to one channel only.
- **LATCH** — footswitch hold becomes latching instead of momentary.
- **L SWAP / R SWAP** — replaces one channel's available modes with the other's (lets you run, e.g., two reverbs, or resonator-into-chorus).
- **UNSYNC** — disconnects the two channels' tempos.
- **TRAILS** — effects fade naturally after bypass.
- **BANK** — switches to the alternate preset bank (Presets 3 & 4).
- **L TIME / L MODIFY / BLEND / R MODIFY / R TIME / BOUNCE / SWEEP / POLARITY** (left bank) — these arm **ramping/bounce** on individual knobs and set its direction and range.

**Hidden Options (hold both footswitches):** **ALT** (a third per-mode parameter, the headline of each mode), **EQ** (two-sided tilt — CW thins/removes lows, CCW darkens/removes highs), **SPILL** (in series, feeds the second effect onto the dry signal too), **GLUE** (end-of-chain compressor → saturator), **SPREAD** routing, plus global **DRY KILL** and **WET VOLUME**. **Tap tempo** is set by double-tapping both footswitches (disabled when synced to MIDI clock).

## 3. Sonic character — what the 12 modes do

Use **MODIFY** to pick A or B within each numbered mode. Manual descriptions ([pp.18–31](manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf)):

**Left channel:**
- **1A Slow-verb** — swelling, out-of-focus shoegaze reverb; max the mix for a soothing blur. (TIME=size, MODIFY=decay, ALT=diffusion.)
- **1B Useful Ambience** — big, clean ambient reverb meant to round out the other modes; infinite ambience, scattering reflections.
- **2A Orchestral Swell** — pitch-shifted swelling reflections with selectable harmony (oct/4th/5th); set pitch to unity for synthy non-pitched swells. (ALT=feedback.)
- **2B Pitch Repeater** — angular inverted pitch-shifter that repeats each note a chosen number of times; rhythmic harmonies, skittering clusters. (ALT=number of repeats.)
- **3A Pinging Phaser** — cartoonish phaser up to **64 poles**; rubbery sweeps, plinking melodies, spatializing. (ALT=resonance; HOLD=PAUSE for a plinky filter.)
- **3B Spectral Modulator** — builds a *synthesized replica* of your signal and modulates it: crystal waterfalls, quivering digital distortion, sparkling low-pass substitute. (ALT=resonance.)

**Right channel:**
- **4A Tape Echo** — classic magnetic tape delay, up to 4s, with warble/age. (ALT=stability/degradation; HOLD=INFINITE loop.)
- **4B Grain Tumbler** — granular delay that samples and rearranges audio into jumbled echoes and rhythmic patterns. (ALT=grain shape; HOLD captures grains, then move TIME for new patterns.)
- **5A Impulse Synthesizer** — polyphonic sub-octave synth from a network of vibrating strings; cinematic, best on chords/slow playing. (ALT=attack/release.)
- **5B Sympathetic Resonator** — polyphonic pitch-tracking resonator (tuned pipes); synth, musical feedback, or an alternative to reverb. (ALT=octave; HOLD=PITCH FREEZE.)
- **6A Ensemble Expander** — tribute to rack-mount chorus; swimming stereo, big sloshing waves. (ALT=number of voices; **HOLD=RANDOM** for smooth, non-cyclical movement instead of an LFO.)
- **6B Gen Lite** — condensed **Generation Loss MKII** tape sim: wow/flutter, noise, drops & snags. (ALT=crinkles and snags; HOLD=TAPE STOP.)

The standout textures for *this* rig: **Spectral Modulator, Grain Tumbler, Sympathetic Resonator, and Gen Lite**. Each is a degrade/scramble/resynthesis engine that the brief's "recorded-wrong / chaotic" aesthetic wants, *before* the signal even reaches the Microcosm.

## 4. Behavioral notes — the "Random" / chaos behavior, and how controllable

This is the slot's reason for existing, so it deserves the detail. "Random" here is **engineered randomness with brakes**, not noise:

1. **MIDI RANDOM mode commands.** CC **112 = Random L Mode**, CC **113 = Random R Mode**, CC **114 = Random Both Modes** ([MIDI manual p.6](manuals/Lost+++Found_MIDI+Manual_Pedal_Chase+Bliss.pdf)). Send any value and the pedal jumps to a new mode/variant. A Chase Bliss demo, [Randomizing Effects with MIDI — Lost + Found & Deluge Jam](https://www.youtube.com/watch?v=g34eqyKSh6g), shows exactly this: sequencing/randomizing the effect itself from a controller.
2. **Internal modulation (Ramp / Bounce).** Any knob can be set to **rise/fall once (Ramp)** or **oscillate continuously (Bounce)** via the Control-bank dips, with **SWEEP** (top/bottom) and **POLARITY** setting direction and the **MIX(RAMP)** knob setting speed ([manual pp.42–43](manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf)). This auto-modulates the effect with no hands.
3. **Per-mode RANDOM behavior.** **6A Ensemble Expander's** ALT/HOLD gives **smooth random movement instead of cyclical LFO**; **6B Gen Lite's** "Drops and Snags" and **4B Grain Tumbler's** captured-grain shuffling are stochastic by design.
4. **FREEZE/INFINITE per channel.** Hold a footswitch to capture and loop the current wet texture as a drone pad — a way to "lock in" a happy accident.

**How controllable:** very, if you want it to be. Everything is **preset-recallable** (122 slots via MIDI), **clock-syncable** (CC 51 MIDI Clock Ignore; subdivisions via TIME), and every knob/toggle is on a MIDI CC. So the chaos can be (a) hands-off and ever-changing, or (b) frozen into a repeatable scene. For this rig that means: dial a deranged dual-mode texture, **save it as a preset**, and recall it on cue — or let Bounce/Random churn it live for a different texture every pass.

## 5. Signal-chain placement — mid-Board-2, chaos before the grain mill

Board 2 order: `(stereo in) → OBNE Parting → **Lost + Found** → Hologram Microcosm → Walrus QI Etherealizer → OBNE Dark Star V3 → (stereo out to Board 3)`.

- **It's already stereo here, and it's in the right place.** The Strymon Deco V2 hands stereo to Board 2 at the front; Lost + Found is a native stereo in / stereo out box, so it preserves and *widens* the image (turn on **SPREAD**) rather than collapsing it. Set the dips for **stereo-in/stereo-out** (default auto-detect handles this).
- **After Parting (filter), before Microcosm (granular):** this is the textbook "texture-injection" slot. Parting carves the spectral window; Lost + Found then **scrambles, resynthesizes, or smears** inside that window; Microcosm chops the result into grains. Feeding the Microcosm a signal that's *already* a Spectral-Modulator shimmer or a Sympathetic-Resonator drone gives its granular engine far more interesting raw material than a dry guitar would.
- **GLUE matters here.** Because so many of these modes are wet and dynamic, the end-of-chain **GLUE** compressor/saturator ([manual p.38](manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf)) tames level spikes before they hit the Microcosm's input — engage it lightly so the granular pedal sees a consistent, gently-saturated feed.
- **Series vs parallel:** with `L+R` parallel you can run two independent textures side-by-side (say, Gen Lite tape on one channel, Slow-verb on the other) into the Microcosm. With `L>R` series you stack them (resonator *into* reverb) for a denser single wall.
- **TRAILS on** so frozen pads and reverb tails don't cut when you bypass mid-phrase.

## 6. Source-specific notes (banjo, baritone, modeled VG-800, bass)

There's no published source-specific data — the pedal is too new — so this is inference from the modes and the rig:

- **GK-5 banjo / baritone Jazzmaster → VG-800 → ... → here.** By the time signal reaches Board 2 it's already summed, modeled, and stereo. The **pitch-tracking modes (5A Impulse Synth, 5B Sympathetic Resonator, 2A Orchestral Swell)** are polyphonic but will track *cleanest* on slow, sustained, chordal input — exactly the drone material this rig generates. Fast banjo rolls will artifact through the resonator/synth modes; for the "recorded-wrong" aesthetic that's a feature.
- **Bright banjo transients:** use the **EQ** hidden option **CCW to darken** before the texture modes get shrill, and favor **Slow-verb / Useful Ambience / Gen Lite** which blur rather than emphasize attack. The **Sympathetic Resonator** can turn a banjo's plink into a sustained, bowed-pipe drone — a strong banjo-into-doom move.
- **VG-800 modeled/synth patches:** continuous synth-pad output from the VG-800 is ideal fuel for **Spectral Modulator** and **Impulse Synthesizer** (synth-on-synth). Polyphonic guitar-synth patches will scramble through the pitch modes — again, on-aesthetic.
- **Jazz bass:** the sub-octave **Impulse Synthesizer** and **Sympathetic Resonator (octave ALT)** can add cinematic low end; watch GLUE/MIX so the wet doesn't muddy the low fundamentals.

## 7. Famous users (honest)

Too new for a developed user mythology — it shipped September 2025. Its public identity right now is **Chase Bliss's own demos** (the Knobs-collaboration prototyping documentary, the stereo demo) and early-adopter shoegaze/ambient players. No artist has yet claimed it as a signature voice. The honest framing: this is a **studio/texture-explorer's pedal** in the lineage of Chase Bliss's experimental crowd (the same audience as Mood, Blooper, Generation Loss), not a tone associated with one famous rig. Flag: **unverified** that any notable touring artist features it as of this writing.

## 8. Live / power / I/O

| Item | Detail |
|---|---|
| Power | 9V DC, center-negative, **~200 mA** ([manual p.1 / chasebliss.com](https://www.chasebliss.com/lost-and-found)) |
| I/O | True stereo in / stereo out (mono, stereo, or **MISO** mono-in/stereo-out) |
| Cabling | Many stereo jacks are dual-mono TRS — may need TRS→dual-TS ([manual p.4](manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf)) |
| Bypass | **True bypass (mode-dependent)** per chasebliss.com; **TRAILS** dip allows tails after bypass |
| MIDI | Via **¼" TRS** (5-pin needs a Chase Bliss MIDIBox); default **channel 2** |
| CV | TRS, **0–5V** range (negative voltage can damage it) |
| Expression | TRS expression jack; **EOM** (Expression Over MIDI) supported |
| Ext. footswitch | AUX (TS, normally-open) can engage the Left channel |
| Clock | Syncs to MIDI clock (CC 51 to ignore); subdivision via TIME |

Current draw is the key live number: **200 mA is heavy** — far more than a typical analog pedal — so on a shared supply, give it a high-current isolated outlet. With this many Chase Bliss/digital pedals on the boards, budget the supply accordingly.

## 9. Pairing recommendations — by name

- **→ Hologram Microcosm (immediately downstream):** feed it a *moving* texture. **Spectral Modulator** or **Sympathetic Resonator** into Microcosm's granular reverb/delay = layered, evolving stereo wash. Sync both to the same MIDI clock so the Microcosm's tempo-based grains lock to Lost & Found's subdivisions.
- **→ Walrus QI Etherealizer / OBNE Dark Star V3 (further down Board 2):** Lost & Found's **reverb modes are redundant** with these — so when those are on, run Lost & Found in a *non-reverb* mode (Grain Tumbler, Gen Lite, Pinging Phaser) and let Dark Star/Etherealizer do the spatial smear. Stacking three reverbs is mud.
- **← OBNE Parting (immediately upstream):** map Parting's **EXP** filter sweep and Lost & Found's **Ramp/Bounce** to move together for coordinated motion.
- **MIDI scene/clock with the other Chase Bliss pedals:** the owner runs **Generation Loss, Big Time, MOOD MkII, Blooper, Onward, Clean, Brothers AM**. Put Lost & Found on its own MIDI channel and build **scene presets** that recall it alongside Big Time/Mood/Blooper via a central controller — all are PC/CC addressable. **Clock-sync** Lost & Found's synced modes to the same master clock that drives Big Time and Blooper so granular grains, delays, and loops all breathe in time. (Confirmed: every knob, toggle, dip, and footswitch is on a CC — [MIDI manual pp.3–6](manuals/Lost+++Found_MIDI+Manual_Pedal_Chase+Bliss.pdf).)
- **Avoid GenLoss-on-GenLoss redundancy:** since **6B Gen Lite ≈ a mini Generation Loss MKII**, don't run Gen Lite *and* the full Generation Loss hard at once unless you want extreme degradation — use one or the other for the "tape" character per pass.

## 10. Reviews & demos (real links)

- [Chase Bliss — official walkthrough](https://youtu.be/Gv7EntFhSLU) and [intro video](https://youtu.be/wQs53zGWGFk).
- [Chase Bliss — Lost + Found mini-documentary](https://www.youtube.com/watch?v=DirzARmPhRU) (the Knobs prototyping collaboration).
- [Chase Bliss // Lost + Found Collection of Curiosities — Stereo Demo](https://www.youtube.com/watch?v=SPQL8wiT19Q).
- [Randomizing Effects with MIDI — Lost + Found & Deluge Jam](https://www.youtube.com/watch?v=g34eqyKSh6g) — the most relevant demo for this rig's "Random" framing.
- [MusicRadar announcement](https://www.musicradar.com/guitars/chase-bliss-lost-and-found-multi-effects-pedal) — best written overview of the mode set and concept.
- [GuitarPedalX — Small Batch release writeup](https://www.guitarpedalx.com/news/gpx-blog/chase-blisss-latest-small-batch-limited-release-consists-of-a-2nd-edition-of-the-reverse-mode-c-and-brand-new-lost-found-stereo-multi-modulator-pedal) ("Stereo Multi-Modulator").
- [SYNTH ANATOMY](https://synthanatomy.com/2025/08/chase-bliss-lost-found-a-multi-fx-pedal-packed-with-strange-but-inspiring-algorithms.html), [gearnews.com](https://www.gearnews.com/chase-bliss-lost-found-12-effects-144-combinations/), [Pedal of the Day](https://www.pedal-of-the-day.com/2025/10/23/chase-bliss-lost-found-collection-of-curiosities/) — news/first-look coverage. (Full long-form reviews were still scarce at time of writing — **flagged as thin web coverage**.)

## 11. Mods / quirks / firmware

- **No user mods** — it's a sealed digital Chase Bliss platform; "modding" = dip switches, Hidden Options, and firmware.
- **Quirk: tap tempo is disabled when synced to MIDI clock** ([manual p.15](manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf)) — expected if you clock it from a controller.
- **Quirk: CV is 0–5V only; negative voltage can damage the pedal** ([manual p.44](manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf)). Use a CV source within range.
- **Quirk: MODIFY at noon = bypassed effect** (so you can use GLUE alone). Easy to think the channel is broken when it's just parked at noon.
- **Dip-switch settings save *with* presets** — so a recalled preset can change routing, swaps, and ramping, not just knob values. Powerful, occasionally surprising.
- **DRY KILL is global and persists** (hold Left footswitch while powering up) — useful in a parallel/wet-only loop, but remember it's set globally, not per-preset.
- **Firmware:** as a 2025 Small Batch release, expect Chase Bliss to issue firmware updates; check chasebliss.com for the current version. **Unverified** which version a given unit ships with.

## 12. Spec sheet

| Spec | Value |
|---|---|
| Type | Stereo dual-channel multi-effect (12 modes, 144 combinations) |
| Power | 9V DC, center-negative, **~200 mA** |
| I/O | Stereo in / stereo out; mono, stereo, or MISO (mono→stereo) |
| Bypass | True bypass (mode-dependent); TRAILS option for tails |
| MIDI | ¼" TRS in (MIDIBox for 5-pin); default channel 2; full CC/PC; clock sync |
| Presets | 4 internal (2 banks × 2) + 122 via MIDI |
| CV | TRS, 0–5V (no negative voltage) |
| Expression | TRS; Expression-Over-MIDI supported |
| Ext. switch | AUX TS normally-open (engages Left channel) |
| Controls | TIME ×2, MODIFY ×2, MIX(RAMP), BLEND; ROUTING & PRESET toggles; 2× 8-way dip banks |
| Internal mod | Ramp (one-shot) / Bounce (continuous) on any knob; per-mode RANDOM |
| Onboard FX extras | GLUE compressor/saturator; two-sided EQ; SPILL; FREEZE per channel |
| Released | September 2025 (Small Batch Bliss, "L+F1") |
| Price | $399 USD / €469 |

Sources: [Lost + Found manual](manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf), [MIDI manual](manuals/Lost+++Found_MIDI+Manual_Pedal_Chase+Bliss.pdf), [chasebliss.com](https://www.chasebliss.com/lost-and-found).

## 13. Starting-point settings

Knob references are clock-face from above. Modes are picked with **TIME-side mode toggle (1–3 / 4–6)** then **MODIFY** for A/B.

**(a) "Recorded-wrong" texture into Microcosm** — degraded, drifting
- Left = **6B Gen Lite** (MODIFY toward B); Right = **3B Spectral Modulator**
- ROUTING: **L+R** parallel · BLEND: noon · MIX: 1–2 o'clock
- EQ: slightly CCW (darker) · GLUE: ~9–10 o'clock (light glue) · SPREAD: on
- Arm **BOUNCE** on R MODIFY for slow self-modulation. Feed into Microcosm.

**(b) Bowed drone** — sustained doom wall from banjo/baritone
- Right = **5B Sympathetic Resonator**, ALT octave −1, MODIFY (feedback) high
- HOLD right footswitch = **PITCH FREEZE** to lock a drone · TRAILS on
- ROUTING: **L>R** into Left = **1B Useful Ambience** for a halo · MIX: 2–3 o'clock

**(c) Synced granular shuffle** — rhythmic, clock-locked
- Right = **4B Grain Tumbler**, synced (UNSYNC off), TIME = a dotted/triplet subdivision
- MIDI-clock from the master controller (same clock as Big Time/Blooper)
- Capture grains (HOLD), then nudge TIME for new patterns · BLEND favors Right

**(d) "Random" live event** — different texture every pass
- Both channels loaded; arm **Random Both Modes** (MIDI CC 114) on a footswitch/controller, or arm **BOUNCE** across L MODIFY + R MODIFY
- 6A Ensemble Expander HOLD = **RANDOM** smooth movement · MIX: noon–1
- Save as a preset so you can also recall a *fixed* version on demand.

## 14. Versus alternatives — why it earns its slot

- **vs. Hologram Microcosm (right next to it):** Microcosm is granular reverb/delay with looping; it's the *grain mill*. Lost & Found is the *texture source* feeding it. They're complements, not competitors — Lost & Found gives Microcosm resynthesized, modulated, randomized material instead of dry guitar. Keep both.
- **vs. Chase Bliss Mood MkII (on Board 3):** Mood is a micro-looping/granular-and-reverb stereo two-engine box — conceptually adjacent. But Mood is about *capturing and mangling loops*; Lost & Found is about *twelve distinct vintage-strange voices, blended*. Different jobs; the owner runs both.
- **vs. Hologram Chroma Console (Board 3):** Chroma is a six-engine modular character/texture multi with gesture control — the closest "many-textures-in-one" rival. Lost & Found wins the Board 2 slot because it's a cleaner *two-voice stereo blend* with deep MIDI/ramp/random automation, and it's positioned to pre-texture the Microcosm; Chroma sits later as a finishing/character stage.
- **vs. a dedicated chaos pedal (e.g. SOMA Cosmos, Hologram-style glitch boxes):** Lost & Found's randomness is *musical and recallable* (presets, clock-sync, GLUE), where pure chaos boxes are harder to harness in a structured drone set. For a rig that wants "controlled chaos," Lost & Found's brakes are the point.
- **vs. running the textures as plugins (the owner has Soundtoys, Valhalla, etc.):** plugins win for precision but can't be *played* with feet mid-take, can't clock-sync to the pedalboard, and can't be randomized live as a performance event. Lost & Found earns its slot as the **hands-and-feet, stereo, MIDI-recallable texture/chaos injector** in the middle of the board.

In this rig — drone/doom/shoegaze, degraded and "recorded-wrong," sustained stereo walls fed by modeled banjo/baritone — Lost & Found earns Board 2's 2nd slot because it's the one box that can (1) **resynthesize/degrade/scramble** in stereo, (2) **randomize itself** as a live event, and (3) **lock to the rig's clock and recall as a scene** — handing the Microcosm exactly the kind of evolving, broken texture the whole aesthetic is built around.

## Sources

- [Chase Bliss — Lost + Found product page](https://www.chasebliss.com/lost-and-found)
- [Lost + Found — A Field Guide (main manual, PDF)](manuals/Lost+++Found_Manual_Pedal_Chase+Bliss.pdf)
- [Lost + Found — MIDI Manual (PDF)](manuals/Lost+++Found_MIDI+Manual_Pedal_Chase+Bliss.pdf)
- [Lost + Found — Quick Start Guide (PDF)](manuals/Lost+++Found_Quick+Start+guide_Pedal_Chase+Bliss.pdf)
- [MusicRadar — Chase Bliss Lost + Found announcement](https://www.musicradar.com/guitars/chase-bliss-lost-and-found-multi-effects-pedal)
- [GuitarPedalX — Small Batch release (Lost + Found "Stereo Multi-Modulator")](https://www.guitarpedalx.com/news/gpx-blog/chase-blisss-latest-small-batch-limited-release-consists-of-a-2nd-edition-of-the-reverse-mode-c-and-brand-new-lost-found-stereo-multi-modulator-pedal)
- [SYNTH ANATOMY — Lost + Found multi-FX](https://synthanatomy.com/2025/08/chase-bliss-lost-found-a-multi-fx-pedal-packed-with-strange-but-inspiring-algorithms.html)
- [gearnews.com — 12 effects & 144 combinations](https://www.gearnews.com/chase-bliss-lost-found-12-effects-144-combinations/)
- [Pedal of the Day — Lost + Found Collection of Curiosities](https://www.pedal-of-the-day.com/2025/10/23/chase-bliss-lost-found-collection-of-curiosities/)
- [Chase Bliss — official walkthrough video](https://youtu.be/Gv7EntFhSLU)
- [Chase Bliss — intro video](https://youtu.be/wQs53zGWGFk)
- [Chase Bliss — Lost + Found mini-documentary](https://www.youtube.com/watch?v=DirzARmPhRU)
- [Lost + Found — Stereo Demo (YouTube)](https://www.youtube.com/watch?v=SPQL8wiT19Q)
- [Randomizing Effects with MIDI — Lost + Found & Deluge Jam (YouTube)](https://www.youtube.com/watch?v=g34eqyKSh6g)
