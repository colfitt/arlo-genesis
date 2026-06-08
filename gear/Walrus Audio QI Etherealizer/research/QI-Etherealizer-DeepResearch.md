# Walrus Audio Qi Etherealizer — Deep Research

A working dossier for the Qi (pronounced "chee") in slot 4 of Board 2 — the Middle/Texture board whose stated job is "Filter · Granular · Smear." The Qi sits immediately after the Hologram Microcosm and immediately before the OBNE Dark Star V3, which makes it the *second* of two granular/smear stages and the last full multi-engine box before the stereo handoff to the End Board. Its role here is not "another reverb" — it's the box that takes the Microcosm's already-mangled granular bed, runs chorus/delay/grain/reverb across it (in series or parallel), and either smooths it into a hall or freezes a slice of it into a sustained pad to hand to the Dark Star. Most of this document is concerned with how it layers against the Microcosm in front and the Dark Star behind, and how it behaves with a hot, line-level, modeled source (VG-800) rather than the single-guitar use case the marketing copy assumes.

## 1. Lineage: Walrus's Ambient Line and the Yvette Young Collaboration

The Qi Etherealizer is a **2025 release**, debuted at NAMM 2025, available to pre-order from January with shipping starting **February 3, 2025** ([guitar.com](https://guitar.com/news/gear-news/i-cant-wait-to-hear-the-dreamy-things-people-make-with-it-yvette-young-partners-with-walrus-audio-on-new-signature-pedal-the-qi-etherealizer/)). It is a **signature collaboration with Yvette Young** (Covet), "over a year in the making," and it is the **first product built on Walrus's new proprietary MDSP platform** — an ARM Cortex-M7-based DSP/microcontroller module that Walrus is rolling out as the basis for a new generation of digital pedals ([Walrus product page](https://www.walrusaudio.com/products/qi-etherealizer)). That "first on a new platform" status matters for the firmware discussion below: this is genuinely new code, and coverage is thinner than for a mature Walrus box.

On the name: **"Qi" officially refers to "the vital life energy that flows through all living things"** — the chi/qi concept — per Walrus's own product page. **It does NOT stand for "Quad-Image."** The brief's "Quad-Image" gloss appears to be a misreading and I could not verify it in any Walrus source, the manual, or any review. Flagging that explicitly: *the "Quad-Image" name is unverified and most likely incorrect.* What is true is that the pedal runs **four engines** (chorus, delay, grain, reverb) in a **stereo image** — which may be where the "quad-image" shorthand came from — but Walrus does not use the term.

Where it sits in Walrus's catalog: this is the ambitious end of a line that runs from the Slö reverb and the Fathom, through the Mako-series R1 (reverb) and D1 (delay), to the larger Slötvå/Lumos. The Qi is the company's most feature-dense pedal to date and the first to combine modulation, delay, **granular sampling**, and reverb in one box with series/parallel routing and full MIDI. It is closest in *ambition* to the Hologram Microcosm sitting right in front of it on this board — both are "ambient creative-playground" multi-FX — which is exactly why the redundancy question in §5 is the central one.

## 2. Controls and Engines

Confirmed against the manual. The Qi has **four engines plus two always-available global processors** (a reverb and a tone filter), arranged across eight knobs, four toggles, and three footswitches.

**Global / structural:**
- **Mix / Dry (Series / Parallel).** Behavior depends on the Flow routing. In **Series**, this is a master wet/dry blend (min = dry only, max = wet only). In **Parallel**, this sets the dry signal level (min = wet only, max = dry at unity).
- **Flow button** — toggles **Series vs Parallel** (Series is labeled **"Forward"** on the pedal). Series chain order is fixed: **Chorus → Delay → Grain → Reverb → Tone → Dry → Output.** In Parallel, the **chorus/delay/grain run discretely off the dry input and sum** — but the **Space reverb is still the LAST block in both modes**, processing the summed wet (the dry path bypasses the reverb in Parallel). Confirmed by the manual + on-camera manual-check (Pedal Collaborative) + guitar.com / Guitar World. *This is exactly why Parallel tames the dominant reverb* — less wet material is fed into the always-last Space, and your dry stays clean.
- **Tone** — cutoff of a **resonant low-pass filter** on the wet signal. Counter-clockwise removes highs. This is the "Filter" piece, and it only touches the wet path.
- **Space** — the **always-on hall reverb**, applied only to the wet effects (not dry). Small room at minimum, long ambient decays at maximum.

**Chorus** (knob = Mix; Rate, Depth; toggle = Tri / Stereo):
- **Tri** — three delay lines with phase-offset modulation; wide and lush.
- **Stereo** — classic chorus with the right channel's modulation offset 180°; turning Chorus Mix fully clockwise in Stereo mode yields **vibrato**.
- **Rate** / **Depth** control the modulating LFO.

**Delay** (knob = Mix; Time, Feedback; toggle = Quarter / Dotted-Eighth / Eighth):
- Clean, crisp **digital delay, up to 2 seconds.** Tap tempo via the Tap/Osc footswitch (quarter-note intervals).
- **Feedback** from one repeat (min) to long multi-second trails (max).

**Grain** — the granular sampler (knob = Mix; **X**; **Playback** rotary; toggle = Grain Cloud / Phrase Sample):
- **Grain Cloud** — triggers small grains *randomly* from your playing; the **X** knob sets time between grains (dense clusters → sparse accents).
- **Phrase Sample** — triggers grains *rhythmically* off detected peaks in your playing; **X** sets playback tempo, and turning **X fully min syncs Phrase Sample to the Delay time.**
- **Playback** (5-way rotary): **x1** (normal), **x2** (double-speed, +1 oct), **x.5** (half-speed, −1 oct), **REV** (reverse), **RNDM** (random combination of the four).

**Reverb** — controlled by the **Space** knob above; no separate decay/tone knobs for it beyond Tone/Space.

## 3. Sonic Character

The Qi is two pedals wearing one enclosure. Set conservatively it's a competent, slightly hi-fi **chorus + digital delay + hall reverb** — reviewers single out the chorus's "sweetly wobbly core sound" and the genuinely lush Tri/Stereo modes ([guitar.com review](https://guitar.com/reviews/effects-pedal/the-big-review-walrus-audio-qi-etherealizer/)). Pushed, it's a "dynamic dreamscape generator" — granular glitch, frozen pads, galaxy-sized stereo washes.

The character notes that matter for this rig:
- **The reverb tends toward hugeness and *dominates*.** Multiple reviews flag that the Space reverb overwhelms the other engines even at moderate settings, and that **Parallel routing balances the engines far better than Series** because Series lets the reverb swallow everything downstream of it ([guitar.com](https://guitar.com/reviews/effects-pedal/the-big-review-walrus-audio-qi-etherealizer/), [Guitar World](https://www.guitarworld.com/gear/effects-pedals/walrus-audio-qi-etherealizer-review)). Worth internalizing before you stack it against the Dark Star.
- **The delay is clean and unfiltered** — "completely straight," no tape/BBD voicing. This is deliberately *not* a degraded delay, which is relevant because everything around it in this rig (Deco, Generation Loss, the JHS 424, the PORTA424) *is* degraded. The Qi's delay is the clean digital one in a chain otherwise built on dirt.
- **The grain is the personality.** Glitchy, pitch-shifted, textural — and reviewers consistently note grain sounds "a bit weird" in isolation but "unleashes the engine's true beauty" when blended into the reverb ([synthanatomy](https://synthanatomy.com/2026/02/walrus-audio-qi-etherealizer-review-with-synths-a-hands-on-granular-multi-fx-pedal.html)). It is a *different flavor* of granular from the Microcosm's — see §5.
- **Digital, 32 kHz, lo-fi-leaning headroom.** The MDSP codec runs at a **32 kHz sample rate** per the product page — lower than the 48 kHz norm. In practice this trims the very top octave and gives the wet path a faintly soft, "off-spec" ceiling, which is on-brand for a degraded/recorded-wrong aesthetic but is worth knowing.

## 4. Behavioral Notes (Freeze, Oscillation, Trails)

This is where the Qi earns its slot, and the behavior is footswitch-driven rather than knob-driven.

- **Freeze (Grain).** Short-press the Freeze switch to **freeze the grain buffer** — a captured slice of your playing loops indefinitely (LED blue). You play over it. This is the pedal's headline trick and the heart of its pad-generation use.
- **Freeze → Reverb ramp.** **Long-press** Freeze to ramp the **reverb to 100%** (LED green), layering a frozen grain loop under a maxed wash. Long-press again releases the reverb ramp while the frozen grain keeps looping. A short press releases both.
- **Tap/Osc → self-oscillation.** Press-and-hold the Tap/Osc switch drives **Delay Feedback to maximum**, oscillating the delay. So yes — it self-oscillates, but specifically the *delay* engine, on a momentary footswitch, not a runaway-on-a-knob fuzz-style oscillation.
- **Bypass long-press clears the grain buffer.** Useful housekeeping if a frozen grain has gone stale.
- **Trails / No-Trails is selectable** (manual): hold Bypass for 1 s while applying power to toggle. Default is **Trails** — delay/grain/reverb decay naturally on bypass. NOTE: Walrus's product page calls bypass **"buffered bypass,"** while the manual documents the selectable trails/no-trails behavior — treat it as **buffered bypass with a trails toggle.** (Minor source conflict; flagging it.)
- **No internal modulation/LFO routing** to animate parameters, and **no expression input** to sweep them by foot — animation comes only from the engines' own LFOs, the freeze gestures, or external MIDI CC. Reviewers note the absence of parameter-animation as the main expressive limitation.

## 5. Signal-Chain Placement — Its Smear/Space Role on Board 2

The order is `… Microcosm → Qi Etherealizer → Dark Star V3 → (stereo to Board 3)`. The Qi is the middle of a three-stage granular/smear cluster, and the honest read is **there is real overlap here that needs deliberate division of labor.**

- **Versus the Microcosm (immediately upstream).** Both do granular. They are *not* the same granular. The Microcosm is sample-and-resequence — looping, arpeggiating, glitch-rhythm "phrase" engine with its own delay/reverb and a sub/octave layer; it builds *evolving rhythmic patterns* out of your playing. The Qi's grain is **texture and freeze** — random grain clouds (Grain Cloud) or peak-triggered rhythmic samples (Phrase Sample), with the killer feature being the **sustained frozen pad.** Division of labor: let the **Microcosm generate the rhythmic/melodic granular motion**, and let the **Qi take that bed and either freeze a chord-pad out of it or wash it into the Space reverb.** They stack beautifully *if* you don't ask both to be the "main glitch." Running both engines hot simultaneously is where it turns to mud.
- **Versus the Dark Star V3 (immediately downstream).** The Dark Star is a **pad/drone reverb** — pitch-shimmer, modulated, drifting ambient reverb, the canonical "smear" box of this board. The Qi *also* has a big hall reverb (Space) that wants to dominate. **This is the redundancy to manage.** Recommendation: **do not run the Qi's Space reverb wide open into the Dark Star** — you'll have two large reverbs in series and the result is a featureless cloud. Better: keep the Qi's Space low-to-moderate (use it as glue on the grain, not as the main space), and let the **Dark Star be the reverb of the board.** Or, conversely, freeze a pad on the Qi (grain freeze, Space modest) and feed *that sustained source* into the Dark Star's pitch-shimmer — now they're complementary, not competing. The Qi makes the *source*; the Dark Star makes the *space.*
- **Parallel routing helps here.** Because Series lets the Qi's own reverb dominate, running the Qi in **Parallel** keeps its grain/chorus/delay present and discrete in the signal you hand to the Dark Star, rather than pre-drowning them.
- **Stereo handoff is clean.** The Qi is true stereo in/out, so the stereo field built at the CE-2W and widened through Board 2 survives intact into Board 3.

## 6. Source-Specific Notes (banjo, baritone, modeled VG-800, bass)

No published documentation covers the Qi with banjo, baritone, or the VG-800 specifically, so this is inference from the manual plus the one synth-focused review.

- **The level-mismatch warning is the big one.** The Qi has **no line/instrument level switch.** A reviewer testing it with synths found it **"clips like crazy with a hot synth signal"** ([synthanatomy](https://synthanatomy.com/2026/02/walrus-audio-qi-etherealizer-review-with-synths-a-hands-on-granular-multi-fx-pedal.html)). **In this rig, the source feeding Board 2 is the VG-800's modeled output run through Board 1 — a hot, line-leaning signal.** Even though there are several pedals between the VG-800 and the Qi, watch the level into the Qi carefully; if you hear digital clipping on loud passages, pull back the Mix/Dry of upstream boosts or the VG-800's patch level. The EHX Effects Interface on the bench exists precisely to reconcile VG-800 line level with pedal instrument level — if Qi clipping becomes a problem, that's the tool. **Flag this as the single most likely real-world issue.**
- **Banjo (GK-5 / EBM-5 via VG-800).** Banjo's fast, bright, percussive transients are ideal **peak-detection fodder for Phrase Sample mode** — the grain engine triggers on attack peaks, so a banjo roll becomes a rhythmic grain pattern. The **Tone low-pass** is your friend for taming banjo's 2–4 kHz spike before it grains. Freeze a banjo chord and play a banjo lead over the frozen pad — directly serves the "banjo-as-lead over sustained walls" aesthetic.
- **Baritone Jazzmaster.** Home territory for ambient pads. Low fundamentals freeze into thick drones; watch that the **Space reverb doesn't turn low baritone notes to wash** — keep Tone open and Space modest for definition.
- **Bass (Jazz bass).** Granular and freeze work, but the Qi has no dry-bass-preservation trick of its own beyond the Mix/Dry; in **Parallel** you can keep dry bass at unity and layer wet grain on top, which is the right move so the low end stays defined.

## 7. Famous Users (honest)

Thin, because it's a 2025 pedal. The honest list:
- **Yvette Young (Covet)** — the signature artist. She co-designed it, demos it on her own channel, and her three factory presets (Red/Green/Blue) ship as the default voicings ([guitar.com](https://guitar.com/news/gear-news/i-cant-wait-to-hear-the-dreamy-things-people-make-with-it-yvette-young-partners-with-walrus-audio-on-new-signature-pedal-the-qi-etherealizer/), [Yvette's demo](https://www.youtube.com/watch?v=zum5SglooYc)).
- **Jeremy Galindo (This Will Destroy You)**, **Chavez Soliz**, **Alex Akins** — credited players in the official Walrus "Qi Tech Demo" (Jan 16 2025). Galindo (post-rock/drone) is the most rig-relevant. No published settings.
- **Attribution correction:** an earlier draft of this dossier credited an "Ambient Adventure" demo to **Andrew Huang** ([r0FiTzG9YfQ](https://www.youtube.com/watch?v=r0FiTzG9YfQ)). That is wrong — yt-dlp metadata shows the video is uploaded by **Nobes Music** and the content is credited to **Yvette Young and Walrus Audio**. **There is no verified Andrew Huang Qi demo** (the candidate xcKdQAicxq8 is actually a SYNTH ANATOMY synth demo). Drop Andrew Huang as a user.
Beyond that there is **no developed user mythology yet** — it's too new, and most footage is demo content rather than artist-rig sightings. Anyone claiming a deeper famous-user list for this pedal is guessing.

## 8. Live / Power / I/O

- **Power: 9V DC center-negative, 300 mA minimum.** This is a heavy draw — plan an isolated 9V/≥300 mA slot. It will *not* run off a low-current daisy-chain tap.
- **Audio I/O:** 2× 1/4" unbalanced TS in (IN MONO L / IN STEREO R), 2× 1/4" unbalanced TS out (OUT MONO L / OUT STEREO R). True **stereo in/stereo out**; runs mono if needed.
- **MIDI: full.** TRS MIDI **IN** + MIDI **THRU**, 1/8" **TRS Type A**. PC for presets (Live=0, Red=1, Green=2, Blue=3, then 4–127), and a deep CC map covering Flow, Mix/Dry, Tone, Space, all three engines' mode/mix/params, Freeze mode, Delay oscillation, per-engine bypass, and Tap. Channel-assign via Freeze-during-power-up; default channel 1. **This is the only way to get "expression-like" continuous control** of Qi parameters in this rig.
- **EXPRESSION: NONE.** **There is no expression pedal input.** The GearProfile's `expression: true` is **incorrect for a TRS/jack expression input** — confirmed by the manual (no EXP jack) and multiple reviews ([Guitar World](https://www.guitarworld.com/gear/effects-pedals/walrus-audio-qi-etherealizer-review), [synthanatomy](https://synthanatomy.com/2026/02/walrus-audio-qi-etherealizer-review-with-synths-a-hands-on-granular-multi-fx-pedal.html)). The only sweep-by-foot path is an external MIDI controller sending CC. **Recommend correcting the GearProfile.**
- **USB-C** for firmware (Chrome-based walrusaudio.io updater only).
- **Bypass:** buffered, with a selectable trails / no-trails mode (default trails).
- **Presets:** 3 onboard (Red/Green/Blue) + white live mode; scroll by pressing both stomps together; save via Bypass+Freeze hold; 128 presets total over MIDI.
- **Size:** 5.82–5.83" W × 4.87" D × 2.29–2.30" H, ~1.3 lb. Mid-large board footprint — bigger than a standard EQD box, smaller than an H90.

## 9. Pairing Recommendations (by name)

- **After the Microcosm (upstream):** let the Microcosm own the *rhythmic* granular and the Qi own *freeze + texture*. Don't double the glitch. Microcosm's sub/octave layer gives the Qi's grain something fatter to sample.
- **Into the Dark Star V3 (downstream):** keep the Qi's **Space reverb modest**; let the Dark Star be the board's reverb. Best combo: Qi grain-freeze pad (Space low) → Dark Star pitch-shimmer for the actual "space." Two big reverbs in series = mud; avoid.
- **Vs the H90 (End Board):** the H90 is the surgical, high-fidelity reverb/algorithm engine — use it for the *final, controlled* ambient (BlackHole, shimmer, MangledVerb). The Qi is the *unpredictable front-half texture generator*. They're not redundant if the Qi is doing freeze/grain and the H90 is doing the polished tail.
- **Vs the Chroma Console (End Board):** Chroma is the other "playground" granular/character box, but it lives after the delays/looper. Let the Qi seed material on Board 2 and the Chroma re-mangle the printed result. Again: keep one of them as the primary glitch at a time.
- **With the Blooper (End Board):** freeze a Qi grain pad, capture it in the Blooper, layer — exactly the stated drone/loop aesthetic. The Qi is a strong *sustained source* for the Blooper to chew on.
- **OBNE Parting / CB Lost & Found (upstream on Board 2):** the Parting's filter and the Lost & Found's random gating feed the Qi unpredictable, pre-filtered material that grains in interesting ways. Good front-of-board chaos before the Qi structures it.

## 10. Reviews and Demos

- [guitar.com — The Big Review: Qi Etherealizer](https://guitar.com/reviews/effects-pedal/the-big-review-walrus-audio-qi-etherealizer/) — best written review on routing (Series vs Parallel), the dominant reverb, and freeze "beds of sound."
- [Guitar World — Qi Etherealizer review (4.5/5)](https://www.guitarworld.com/gear/effects-pedals/walrus-audio-qi-etherealizer-review) — verdict + engine breakdown; confirms no EXP input.
- [SYNTH ANATOMY — hands-on with synths](https://synthanatomy.com/2026/02/walrus-audio-qi-etherealizer-review-with-synths-a-hands-on-granular-multi-fx-pedal.html) — **the most relevant review for this rig**: documents the no-line/instrument-switch clipping problem and synth/non-guitar behavior.
- [SYNTH ANATOMY — launch coverage](https://synthanatomy.com/2025/01/walrus-audio-qi-etherealizer-stereo-multi-fx-with-granular-in-collaboration-with-yvette-young.html) — spec/announcement detail.
- [guitar.com — Yvette Young interview/announcement](https://guitar.com/news/gear-news/i-cant-wait-to-hear-the-dreamy-things-people-make-with-it-yvette-young-partners-with-walrus-audio-on-new-signature-pedal-the-qi-etherealizer/) — design intent.
- [MusicRadar — NAMM 2025 coverage](https://www.musicradar.com/guitars/namm-2025-i-want-people-to-sound-a-little-less-guitar-y-and-more-magical-yvette-young-and-walrus-audios-qi-etherealizer-might-well-be-the-atmospheric-guitar-pedal-youll-want-to-use-with-any-instrument-or-voice) — "use it with any instrument or voice" framing.
- [Yvette Young — "explore my signature pedal with me"](https://www.youtube.com/watch?v=zum5SglooYc) — designer's own walkthrough (sound demo ~12 min mark).
- [Nobes Music — "Ambient Adventure with the Qi" (Yvette Young & Walrus content)](https://www.youtube.com/watch?v=r0FiTzG9YfQ) — *(previously mis-credited here to Andrew Huang; see §7)*.
- [Walrus Audio & Yvette Young — Reverb demo](https://www.youtube.com/watch?v=8Uc1JEdlrDg).
- [Walrus official demo](https://www.youtube.com/watch?v=l_wA7lTC6_0).

## 11. Mods / Quirks / Firmware

- **Firmware** via USB-C on **walrusaudio.io**, Chrome-only cloud updater. Manual ships referencing **Qi-v1.0** (the in-app screenshot shows a beta build `Qi_beta-v0.12`). No public changelog of post-launch firmware revisions was findable as of this writing — **flag firmware history as unverified/thin** given the platform's newness. Check the updater for the current build.
- **MDSP platform, first product.** As Walrus's debut MDSP pedal, expect this to be the model that gets the most firmware attention as the platform matures. Being early-adopter on a v1 platform is the relevant caveat.
- **32 kHz sample rate** is a deliberate quirk, not a bug — gives the wet path a slightly soft ceiling.
- **The reverb-dominance behavior** is the most-reported "quirk" — manage with Parallel routing and modest Space (see §3, §5).
- **No line/instrument level switch** — the most-reported hardware omission; clips with hot sources (see §6).
- No reported reliability/failure pattern yet — too new, and Walrus build quality is reliably good. Treat hardware-fault data as **unestablished** at this age.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Released | NAMM 2025; shipping Feb 3, 2025 |
| Engines | Chorus, Delay, Grain (granular sampler), Reverb (always-on "Space" hall) |
| Routing | Series or Parallel (Flow button) |
| Power | 9V DC, center-negative, **300 mA min** (isolated supply required) |
| Audio inputs | 2× 1/4" unbalanced TS (stereo L/R) |
| Audio outputs | 2× 1/4" unbalanced TS (stereo L/R) |
| Input impedance | 1 MΩ |
| Output impedance | 220 Ω |
| Frequency response | 20 Hz – 20 kHz |
| Sample rate | 32 kHz (MDSP / ARM Cortex-M7) |
| MIDI | TRS MIDI IN + THRU, 1/8" Type A; full PC + CC map; 128 presets |
| Expression input | **None** (continuous control via MIDI CC only) |
| USB | USB-C, firmware updates (walrusaudio.io, Chrome) |
| Presets | 3 onboard (Red/Green/Blue) + white live mode |
| Bypass | Buffered; selectable trails / no-trails (default trails) |
| Dimensions | 5.82–5.83" W × 4.87" D × 2.29–2.30" H |
| Weight | ~1.3 lb |
| Price | $449 (Terracotta/Yvette art or Matte Black) |
| Warranty | Limited lifetime |

Sources: [Walrus product page](https://www.walrusaudio.com/products/qi-etherealizer), instruction manual (local PDF).

## 13. Starting-Point Settings

Knob positions are clock-face from above. The Qi has no "presets are sacred" rule — but Yvette's factory voicings are good anchors: **Red** = freeze/granular pads, **Green** = THE chorus tone, **Blue** = randomized freeze-and-play-over moments.

**(a) Frozen banjo/baritone pad** — sustained source for the Dark Star (this rig's bread-and-butter)
- Flow: **Parallel**
- Grain: Mix 1–2 o'clock, **Grain Cloud**, Playback **x1**, X ~11
- Chorus: Mix ~10 (Tri), Rate 9, Depth 10
- Delay: Mix off or ~9
- Space: **10–11** (modest — let the Dark Star own the space)
- Tone: ~1 o'clock
- Use: hit a chord, **short-press Freeze**, play a banjo lead over the loop. Feed the held pad into the Dark Star.

**(b) Lush stereo chorus + light delay** — the "down-to-earth" useful tone
- Flow: Series
- Chorus: Mix noon, **Stereo**, Rate 10, Depth 11
- Delay: Mix ~9, Time dotted-eighth, Feedback 9
- Grain: off
- Space: 9–10
- Mix/Dry: ~1 o'clock (mostly wet, some dry)
- Use: shimmer behind clean baritone arpeggios before the dirt boards engage.

**(c) Glitch-cloud texture** — pairs with the Microcosm's rhythmic granular
- Flow: Parallel
- Grain: Mix 1–2 o'clock, **Grain Cloud**, Playback **RNDM**, X ~1 o'clock (sparse, surprising)
- Delay: Mix 11, Feedback noon
- Chorus: off or low
- Space: noon
- Tone: noon (roll back if harsh)
- Use: let the Microcosm drive the rhythm; the Qi sprinkles reverse/octave grains over it.

**(d) Galaxy wash / oscillating drone** — max ambient, the "let the Qi take over" mode
- Flow: Series
- Grain: Mix 2 o'clock, Phrase Sample, Playback x.5 (−1 oct)
- Delay: Mix noon, Feedback 2–3 o'clock
- Space: 3 o'clock (big)
- Mix/Dry: full wet
- Use: **long-press Freeze** to ramp reverb to 100% over a frozen grain; **hold Tap/Osc** to oscillate the delay. Control with proximity and the Tone knob. Hand the result to the End Board to print.

## 14. Versus Alternatives — Why It Earns the Board-2 Slot

- **Hologram Microcosm (already on the board, in front).** The obvious "do I need both?" question. Answer: the Microcosm is a *rhythmic granular looper* (resequence/arpeggiate/phrase); the Qi is a *texture + freeze + four-engine wash* with a dominant hall reverb. Keep both **only if** you split roles — Microcosm = motion, Qi = freeze/smear. If you ever cut for space, the Qi is the more redundant of the two *against the Dark Star+H90 reverb stack*, but it's the less redundant against the Microcosm's rhythmic granular. It earns its slot as the **freeze-pad generator and the bridge between granular motion and reverb space.**
- **Chase Bliss / Old Blood "smear" boxes (Dark Star V3 is downstream).** The Dark Star is a better *reverb*; the Qi is a better *source-mangler* (grain/freeze/chorus/delay in one). Complementary, not competing — provided the Qi's Space stays low.
- **Strymon Big Sky / Night Sky.** Cleaner, deeper, more hi-fi reverbs with more reverb-specific control — but no granular sampling and no freeze-pad workflow. The Qi is the more *characterful, four-in-one playground*; Big Sky (on the bench) is the cleaner pure-reverb sub-in. Different jobs.
- **Hologram Chroma Console (End Board).** The other "playground" box. Chroma is more of a character/modulation/granular *processor* late in the chain; the Qi *generates* material earlier. Run one as primary glitch at a time.
- **Empress Reverb / Meris Mercury / EQD Afterneath.** All do ambient reverb-with-texture; none combine **chorus + clean digital delay + granular freeze + hall** with series/parallel routing and full MIDI in one stereo box. The Qi's specific edge is the **freeze-pad-into-reverb workflow** and the four-engine flexibility.

In this rig — banjo/baritone/VG-800 sources, drone/doom/shoegaze, a stereo texture board feeding a tape-print End Board — the Qi earns its slot specifically because of (1) the **grain-freeze pad workflow** that turns a banjo or baritone chord into a sustained source for the Dark Star, (2) **four engines + series/parallel** flexibility that no single-purpose box on the bench replaces, and (3) **true stereo + full MIDI** that fit the board's stereo, MIDI-controlled architecture. Its honest weaknesses — the **dominant reverb**, **no expression input**, **no level switch / clipping on hot sources**, and **overlap with the Microcosm** — are all manageable with Parallel routing, modest Space, MIDI for sweeps, and a deliberate Microcosm-vs-Qi division of labor.

## Sources

- [Walrus Audio — Qi Etherealizer product page](https://www.walrusaudio.com/products/qi-etherealizer)
- Walrus Audio — Qi Etherealizer Instruction Manual (local PDF: `manuals/Walrus Audio Etherializer QI.pdf`)
- [guitar.com — The Big Review: Walrus Audio Qi Etherealizer](https://guitar.com/reviews/effects-pedal/the-big-review-walrus-audio-qi-etherealizer/)
- [Guitar World — Walrus Audio Qi Etherealizer review (4.5/5)](https://www.guitarworld.com/gear/effects-pedals/walrus-audio-qi-etherealizer-review)
- [SYNTH ANATOMY — Qi Etherealizer review with synths (hands-on)](https://synthanatomy.com/2026/02/walrus-audio-qi-etherealizer-review-with-synths-a-hands-on-granular-multi-fx-pedal.html)
- [SYNTH ANATOMY — Qi Etherealizer launch coverage](https://synthanatomy.com/2025/01/walrus-audio-qi-etherealizer-stereo-multi-fx-with-granular-in-collaboration-with-yvette-young.html)
- [guitar.com — Yvette Young partners with Walrus Audio (announcement)](https://guitar.com/news/gear-news/i-cant-wait-to-hear-the-dreamy-things-people-make-with-it-yvette-young-partners-with-walrus-audio-on-new-signature-pedal-the-qi-etherealizer/)
- [Guitar World — Walrus and Yvette Young launch Qi Etherealizer](https://www.guitarworld.com/gear/guitar-pedals/walrus-audio-yvette-young-qi-etherealizer)
- [MusicRadar — NAMM 2025 Qi Etherealizer](https://www.musicradar.com/guitars/namm-2025-i-want-people-to-sound-a-little-less-guitar-y-and-more-magical-yvette-young-and-walrus-audios-qi-etherealizer-might-well-be-the-atmospheric-guitar-pedal-youll-want-to-use-with-any-instrument-or-voice)
- [Perfect Circuit — Qi Etherealizer listing/specs](https://www.perfectcircuit.com/walrus-qi-etherealizer.html)
- [Sweetwater — Qi Etherealizer (Black)](https://www.sweetwater.com/store/detail/QiEtherealBlk--walrus-audio-qi-etherealizer-multi-effects-pedal-black)
- [Yvette Young — "explore my signature pedal with me" (YouTube)](https://www.youtube.com/watch?v=zum5SglooYc)
- [Andrew Huang — Ambient Adventure with the Qi Etherealizer (YouTube)](https://www.youtube.com/watch?v=r0FiTzG9YfQ)
- [Walrus Audio & Yvette Young — Qi Etherealizer Reverb Demo (YouTube)](https://www.youtube.com/watch?v=8Uc1JEdlrDg)
- [Walrus Audio — Qi Etherealizer official demo (YouTube)](https://www.youtube.com/watch?v=l_wA7lTC6_0)
