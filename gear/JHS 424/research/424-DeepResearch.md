# JHS 424 Gain Stage — Deep Research

A working dossier for the pedal that has the **last word in the entire three-board rig** — the 8th and final box on Board 3 (End / Time → Tape), sitting after the MXNHLT PORTA424 and feeding straight into the Apollo x8 / FOH. It is marked **always-on** in the rig art, so everything the rig does — the Colour Box console front-end, the granular smear, the Chase Bliss delays, the Generation Loss degradation, the PORTA424 channel strip — passes through this pedal before it gets recorded. The rig's whole conceit is "console-to-tape": JHS Colour Box V2 stands in for the Neve front-end at the very start, and the JHS 424 is the cassette deck that the bus prints to at the very end. This document is mostly about *why a rig that already has four tape voices and a PORTA424 immediately upstream still earns a second Portastudio box as its terminus*, and how to run it mono into a stereo bus.

## 1. Lineage: Tascam Portastudio 424 → Mk.gee → JHS 424 Gain Stage

The JHS 424 Gain Stage is a faithful recreation of the **channel strip of a Tascam Portastudio 424 MKI** — the affordable cassette four-track that was everywhere in DIY/bedroom recording through the late '80s and '90s ([JHS product page](https://jhspedals.info/products/424-gain-stage); [zZounds blog](https://blog.zzounds.com/2025/08/21/the-jhs-424-gain-stage-brings-the-portastudio-to-your-pedalboard/)). It is not modeling tape *transport* (no wow, flutter, or dropouts — that is the Generation Loss's job); it models the **preamp/gain electronics** of one recording channel — the path from the input jack through the trim pot, the channel fader, and the master fader. JHS used the **original UPC4570 and NJM4565 op-amps** found in the real 424 MKI to capture the exact channel character ([JHS](https://jhspedals.info/products/424-gain-stage); [MusicRadar feature](https://www.musicradar.com/guitars/guitar-pedals/hes-not-using-a-guitar-amp-hes-using-a-tascam-424-jhs-pedals-puts-a-portastudio-in-a-pedal-to-help-you-recreate-mk-gees-elastic-lo-fi-tones)).

The pedal exists because of one artist. Mk.gee's 2024 album *Two Star and the Dream Police* sparked a wave of curiosity about his tone: rather than a guitar amp, he plugs his (modified Jaguar/Jazzmaster-style) guitar **directly into a vintage Tascam Portastudio 424 and overdrives its preamp** ([MusicRadar feature](https://www.musicradar.com/guitars/guitar-pedals/hes-not-using-a-guitar-amp-hes-using-a-tascam-424-jhs-pedals-puts-a-portastudio-in-a-pedal-to-help-you-recreate-mk-gees-elastic-lo-fi-tones)). Josh Scott of JHS framed it directly: *"This Mk.gee thing comes along, and it's really new and fresh and different. It's not the classic thing, it's this really interesting new way of using this sound to create guitar parts that really we haven't heard before."* JHS announced the pedal in **August 2025** at **$249** to make that approach available without dragging a cassette deck on stage.

Within the JHS line and this rig's JHS ecosystem, the 424 is the bookend to the **Colour Box V2** (Board 1). The Colour Box is JHS's Neve-1073-style **console preamp** — the front of the recording chain. The 424 is the **cassette channel** at the back of it. Owning both lets the rig literally trace a signal from a high-end console input to a budget four-track output, which is exactly the "console-to-tape" arc the board is built around. The owner's other JHS box (Kilt v10) and the TKOG Oxford Drive sit on the bench and are unrelated to this signal.

## 2. Controls (from the manual)

Five knobs and a footswitch. The manual's most useful detail is that **each control maps to a physical position on the real Portastudio 424** (manual pg. 1):

- **Volume** — Master output level. *On the 424, this is the **MASTER fader**.* Left less, right more. There is plenty of output here for clean-boost duty.
- **Gain 1** — Sets how much **preamplification** is added to the input signal. *On the 424, this is the **TRIM** knob.* This is the first gain stage — the input-sensitivity control that decides how hard the channel is driven.
- **Gain 2** — Sets the level of the **second gain stage**. *On the 424, this is the **CHANNEL fader**.* Pushing Gain 2 past ~3 o'clock is where reviewers report it blooms into "a gated fuzz monster, tight, aggressive, and full of attitude" ([Bass Musician Magazine](https://bassmusicianmagazine.com/2025/12/review-jhs-424-gain-stage-pedal-lo-fi-roots-serious-bass-utility/)).
- **Bass** — Shelving EQ. Cuts or boosts low frequencies; left less, right more.
- **Treble** — Shelving EQ. Cuts or boosts highs. Reviewers describe it as working "like a clarity dial, cutting through the haze when needed" ([Bass Musician Magazine](https://bassmusicianmagazine.com/2025/12/review-jhs-424-gain-stage-pedal-lo-fi-roots-serious-bass-utility/)).

The headline is that **Volume, Gain 1, and Gain 2 interact** — the same total loudness can be reached with very different amounts of grit depending on how the two gain stages are balanced against the master. Per JHS, the pedal is "a multi-stage gain device giving you everything from a clean, lo-fi sound to blown out fuzz, accurately replicating the full signal path of a vintage Portastudio 424 MKI" (manual pg. 1). The footswitch is **silent, soft-touch switching with buffered bypass** (manual pg. 1) — no relay click, and the buffer matters for a terminus pedal feeding a long cable to the Apollo.

## 3. Sonic Character — Cassette Channel, Clean to Blown-Out

This is not a conventional amp-in-a-box, and reviewers are unanimous that it is not chasing traditional guitar/amp tone. It is the sound of a recording channel being abused:

- **Low gain = rubbery, compressed clean.** At low Gain 1 it is "a warm, harmonically rich preamp" adding "subtle bloom before any audible grit" ([Bass Musician Magazine](https://bassmusicianmagazine.com/2025/12/review-jhs-424-gain-stage-pedal-lo-fi-roots-serious-bass-utility/)). MusicRadar calls the bottom of the range "clean but warm." Guitar World's phrase is "squishy DI compression." There is a natural, tape-head-style compression that thickens single notes and lets chords smear together without losing definition.
- **Mid gain = grainy lo-fi grit.** As the gain stages climb, it moves into "grainy lo-fi grit" and "gnarly clipping distortions" ([MusicRadar review](https://www.musicradar.com/guitars/guitar-pedals/jhs-pedals-424-gain-stage-review)) — "fuzzy, chewy, and uneven, with harmonics that spill out in unpredictable ways."
- **High gain = blown-out, gated fuzz.** Maxed, it becomes "blown-out, speaker-ripping clipping fuzz" ([Guitar World](https://www.guitarworld.com/gear/effects-pedals/jhs-pedals-424-gain-stage-review)) — a "particularly snarky fuzz" ([MusicRadar review](https://www.musicradar.com/guitars/guitar-pedals/jhs-pedals-424-gain-stage-review)), gated and "full of attitude" at the top of Gain 2.

The recurring descriptors — *rubbery, gooey, elastic, squishy* — are the point. JHS's own copy promises "unparalleled gooey texture and lo-fi fuzz." It is the **"recorded-wrong"** color in its purest form: not a degraded *tape*, but a degraded *channel* — the front-end that the tape was recorded through. For this rig's drone/doom/shoegaze, degraded-and-ruined aesthetic, it is the final layer of artificiality stamped onto an already-textured signal.

## 4. Behavioral Notes — Always-On Coloration, Gain Staging, Headroom

- **It is a coloration, not an effect.** Run always-on per the rig art, the 424 is a tonal *finish*, like a mix-bus plug-in — every note that leaves the rig has its rubbery-channel character. This is the correct way to use it as a terminus: set it once, leave it, and treat it as part of the rig's baseline voice rather than a stomp.
- **The two gain stages are the whole game.** Gain 1 (trim) decides how hot the channel is hit; Gain 2 (channel fader) decides how hard the *second* stage clips; Volume (master) sets final output independent of both. Low Gain 1 + high Gain 2 ≠ high Gain 1 + low Gain 2 — they sound different at the same loudness. For an always-on print you generally want **modest Gain 1, low-to-moderate Gain 2**, then use Volume to hit the Apollo at a sane level.
- **Headroom and output.** JHS lists "high head room" alongside the fuzz; there is enough output to use it as a conventional boost with tone-shaping ([JHS](https://jhspedals.info/products/424-gain-stage); [MusicRadar review](https://www.musicradar.com/guitars/guitar-pedals/jhs-pedals-424-gain-stage-review)). As the literal last gain stage before conversion, set Volume so peaks don't clip the Apollo's input — the pedal can put out a hot signal.
- **Buffered bypass** means the pedal conditions the signal even at modest settings and presents a low-impedance source to the interface — good for a terminus driving the run to the rack.

## 5. Signal-Chain Placement — The Final Terminus, and the Mono Question

Order on Board 3: `… → H90 → MXNHLT PORTA424 → JHS 424 → Apollo / FOH`. A few observations specific to this exact slot:

- **Two Portastudio boxes back-to-back is deliberate, not redundant** (see §9 and §14). The PORTA424 is the *fuller channel-strip recreation* (input trim → bass/treble shelving → channel slide-fader → master), positioned as a complete signal-path DI tone. The JHS 424 is a *gain-stage drive/lo-fi* pedal that takes the PORTA424's already-tape-ish output and prints it through a second, dirtier cassette channel. Running PORTA424 *into* 424 stacks two channel strips — exactly what you'd get bouncing one 424 track to another. The PORTA424 supplies the polished four-track DI tone; the JHS 424 supplies the *blown-out commit*.
- **It closes the console-to-tape arc.** Colour Box V2 (Neve front-end, Board 1) → all the texture/time effects → PORTA424 + JHS 424 (cassette, end of Board 3) → Apollo print. Conceptually the signal enters a high-end console and leaves through a $249 four-track. The 424 is the last brushstroke.
- **The mono question is real and load-bearing.** The rig is **stereo** from the CE-2W onward, and the rig art tags the PORTA424 "Stereo" — but per the manufacturer the **MXNHLT PORTA424 is a mono pedal** (one recreated channel), and the JHS 424 is **mono** too (single ¼" in, single ¼" out). So the stereo image *must* collapse to mono somewhere in this final pair. Two honest options:
  1. **Commit to mono at the print** (most period-correct). Sum L+R into the PORTA424 → 424 → Apollo. This is exactly what bouncing a stereo mix to a single cassette channel does, and it suits the lo-fi aesthetic — a real Portastudio ping-pong bounce is mono-per-track anyway. Recommended for the "ruined cassette" sound.
  2. **Run a stereo pair of 424s** (a second unit) if stereo width must survive to the Apollo — but that doubles cost and breaks the single-terminus concept. Not recommended; the rig already has abundant stereo width upstream, and the print stage is the natural place to glue it to mono.
- **Use the XLR out into the Apollo.** The 424 has a **balanced XLR direct-out with a ground-lift dip switch** (manual pg. 1); the ¼" and XLR can run simultaneously. For a permanent terminus feeding the x8, the XLR is the cleanest path (balanced, ground-lift available if the rack hums). This is a genuine advantage over the PORTA424, which has no XLR.

## 6. Source-Specific Notes (banjo, baritone, modeled VG-800, bass)

By the time signal reaches the 424 it has been through three boards, so the 424 is coloring a *fully-formed texture*, not a raw instrument — but the source still shapes what arrives:

- **GK-5 banjo (EBM-5) via VG-800.** Banjo's piercing top has long since been rolled off by the Generation Loss and the texture board, so the 424 mostly adds rubbery compression and grit to a sustained, blurred bed. The Treble knob is the "clarity dial" if the print goes too murky; the Bass knob tightens or fattens the cassette bottom. Keep Gain 2 modest — banjo transients into a maxed second stage can get spitty and gated in a way that fights the wall.
- **Baritone Jazzmaster.** Low-end mass benefits from the 424's tape-channel compression — it "sits in the mix beautifully," and flatwound-style low strings get "that near-breakup texture we associate with old tape heads" ([Bass Musician Magazine](https://bassmusicianmagazine.com/2025/12/review-jhs-424-gain-stage-pedal-lo-fi-roots-serious-bass-utility/)). Watch Bass at high Gain — it can get flubby. Pull Bass back a touch before the print.
- **Modeled VG-800 signal.** The 424 is excellent at *de-perfecting* digital modeling — running a clean modeled amp/cab through a worn cassette channel is precisely the trick that makes COSM tones believable. Pad/synth COSM patches turn into gooey, blown-out drones. Mind level: the VG-800 outputs near line level, so it may hit Gain 1 hotter than a passive guitar would — back Gain 1 off if it's clipping unintentionally.
- **Jazz bass / SG / Jazzmaster.** The pedal is a documented bass favorite — "warm, tape-like saturation rather than modern distortion," pairs "shockingly well with modern octavers and synth pedals," and the dual gain lets you separate input saturation from output level ([Bass Musician Magazine](https://bassmusicianmagazine.com/2025/12/review-jhs-424-gain-stage-pedal-lo-fi-roots-serious-bass-utility/)). The XLR DI makes it a one-box bass recording chain on its own.

## 7. Famous Users (honest)

- **Mk.gee** — the *inspiration*, not a confirmed pedal user. His tone (a modified Jaguar/Jazzmaster into a real Tascam Portastudio 424's overdriven preamp) is the entire reason the pedal exists ([MusicRadar feature](https://www.musicradar.com/guitars/guitar-pedals/hes-not-using-a-guitar-amp-hes-using-a-tascam-424-jhs-pedals-puts-a-portastudio-in-a-pedal-to-help-you-recreate-mk-gees-elastic-lo-fi-tones)). He uses the actual hardware four-track, not the JHS box. Flag: no public evidence he plays the pedal.
- **John Mayer** — publicly demoed the 424 Gain Stage in a JHS video ([Guitar World coverage](https://www.guitarworld.com/gear/guitar-pedals/john-mayer-demos-the-jhs-424-gain-stage)). A demo appearance, not a confirmed live/recording user.
- **Tascam Portastudio 424 (the device) — heritage users.** The lineage runs through any record cut on a cassette four-track: Bruce Springsteen's *Nebraska* (cut on the **TEAC 144** — the *first* Portastudio, 1979 — not a 424; same family, mythology carries) and DIY/lo-fi artists throughout the '80s–'90s ([Reverb history](https://reverb.com/news/the-tascam-portastudio-through-the-ages); [MusicRadar on the 144/*Nebraska*](https://www.musicradar.com/music-tech/recordingweekspringsteen-teac-144)). That is the device's mythology, inherited by the pedal — not a JHS-424 artist roster.

The pedal is too new (Aug 2025) to have a developed user mythology of its own. Be honest: its fame is *borrowed* from Mk.gee and the Tascam, not earned by a list of 424-pedal players.

## 8. Live / Power / I/O

| Aspect | Detail |
|---|---|
| Power | 9VDC center-negative, 2.1mm barrel. **Do not exceed 9VDC** (damage / voids warranty) |
| Current draw | **50 mA** — modest, any isolated supply slot handles it |
| Bypass | **Soft-touch silent switching, buffered bypass** — no relay click |
| Inputs/Outputs | ¼" In (top right), ¼" Out (top left), **balanced XLR out (left side)**; ¼" + XLR usable simultaneously |
| Ground lift | Dip switch on left side — lifts XLR ground to kill hum/buzz |
| Channels | **Mono** in / mono out |

For this rig: power from the Board 3 supply (50 mA is trivial); take the **XLR into the Apollo** with ground-lift on hand if the rack buzzes; leave it always-on. Because the bypass is buffered (not relay/true-bypass that needs power to pass), a power failure behaves like a buffer dropout rather than a hard signal kill — but as the literal last box before FOH, give it a reliable supply regardless.

## 9. Pairing Recommendations (by name)

- **After the MXNHLT PORTA424 (immediately upstream).** This is the defined order and it's correct: PORTA424 supplies the *clean-ish full-channel DI tone* (trim → EQ → fader → master), the 424 *commits and dirties* it. Keep the PORTA424 cleaner (it's the "tone") and let the JHS 424 do the gain (it's the "print"). If you want one box doing the heavy lifting, push the 424 and keep the PORTA424 near unity, or vice-versa — don't max both or the bus turns to undifferentiated mush.
- **vs CB Generation Loss (Board 3 opener).** Complementary, not competing. Generation Loss is *transport* degradation (wow/flutter/dropouts/EQ models) applied **first** so the time effects degrade with it; the 424 is *channel* degradation applied **last** to glue the whole bus. Gen Loss breaks the source; the 424 prints the result. Per the rig's Generation Loss dossier, "PORTA424 + JHS 424 = the final Tascam-Porta tape *print*… mastering-bus tape, not effect tape" — stay consistent with that division.
- **vs Hologram Chroma Console (Board 3, mid).** Chroma is a *multi-character texture-morphing* color box used over the delays/loops. The 424 is the single fixed *terminus* color. Let Chroma morph mid-chain; let the 424 finish. Avoid stacking heavy Chroma "tape" character into a maxed 424 or you double the lo-fi.
- **vs Strymon Deco V2 (Board 1).** Deco is *warm analog tape saturation + doubletracker* on the **raw instrument** at the front. The 424 is the cassette channel at the **end**. Deco warms the source; the 424 prints the bus. They bookend the chain and never overlap in job.
- **As the print into the Apollo x8.** The XLR out is the right path. The 424 is the last analog gain stage before A/D — set Volume to hit the converter cleanly, and let its compression act as a gentle program-dependent limiter on the way in.

## 10. Reviews & Demos (real links)

- [JHS Pedals — official 424 Gain Stage page](https://jhspedals.info/products/424-gain-stage) — specs, op-amps, price, official tone copy.
- [Guitar World review](https://www.guitarworld.com/gear/effects-pedals/jhs-pedals-424-gain-stage-review) — "more than just 'Mk.gee in a pedal'"; best on the broad sonic palette and DI use.
- [MusicRadar review (4.5/5)](https://www.musicradar.com/guitars/guitar-pedals/jhs-pedals-424-gain-stage-review) — clean-to-fuzz range, boost use, niche-appeal caveat.
- [MusicRadar — the Mk.gee / Tascam origin feature](https://www.musicradar.com/guitars/guitar-pedals/hes-not-using-a-guitar-amp-hes-using-a-tascam-424-jhs-pedals-puts-a-portastudio-in-a-pedal-to-help-you-recreate-mk-gees-elastic-lo-fi-tones) — Josh Scott quote, op-amp/control mapping, release.
- [Bass Musician Magazine review](https://bassmusicianmagazine.com/2025/12/review-jhs-424-gain-stage-pedal-lo-fi-roots-serious-bass-utility/) — best on bass, gain-staging interaction, octave/synth pairing.
- [Guitar Pedal X — 4 Tascam-424-style preamps compared](https://www.guitarpedalx.com/news/gpx-blog/4-of-a-kind-tascam-424-portastudio-style-preamps) — direct JHS-424-vs-MXNHLT-Porta424 (and Benson, Neutrino) comparison.
- [Happy Mag — "JHS 424 Gain Stage: Full Demo and Review" (YouTube)](https://www.youtube.com/watch?v=LXhkhDbGEUw) — A/B'd against a real Tascam 414 MkII. *(Verified via yt-dlp: this is **Happy Mag**, NOT JHS's official channel — earlier draft mislabeled it. JHS's own upload `TGEne6M1EoY` is now private; the public "official" content is the **John Mayer guest demo**, filmed while Josh Scott recovered from a bike accident.)*
- [John Mayer demos the 424 (Guitar World)](https://www.guitarworld.com/gear/guitar-pedals/john-mayer-demos-the-jhs-424-gain-stage).
- [Loopy Demos — 424 Gain Stage](https://loopydemos.com/demos/jhs-pedals-424-gain-stage/) — dry, settings-focused audio demo.
- [zZounds blog overview](https://blog.zzounds.com/2025/08/21/the-jhs-424-gain-stage-brings-the-portastudio-to-your-pedalboard/) — Portastudio history + pedal context.

## 11. Mods, Quirks, Known Issues

- **No true-bypass.** Buffered bypass only — fine and arguably preferable for a terminus, but worth knowing if you wanted the signal to pass on dead power.
- **No stereo.** Single mono channel; the stereo bus must collapse here (see §5). This is the biggest practical "quirk" for *this* rig.
- **Gain 2 past ~3 o'clock gets gated/spitty** — a "gated fuzz monster" ([Bass Musician Magazine](https://bassmusicianmagazine.com/2025/12/review-jhs-424-gain-stage-pedal-lo-fi-roots-serious-bass-utility/)). Intentional, but it can choke sustained drones; for wall-of-sound print, keep Gain 2 below that and add grit with Gain 1.
- **Niche by design.** MusicRadar's only real con: the harsh clipping "won't suit all players." It is not a transparent drive and will not pretend to be one.
- **Op-amp authenticity.** UPC4570 / NJM4565 are the real 424 MKI parts — no mod target here; the character *is* those chips. No widely reported reliability issues; JHS build quality and a **4-year USA limited warranty** (manual pg. 1).
- **Treble = de-haze.** If the always-on print buries articulation, the Treble knob is the clarity recovery — quirk worth remembering since by default the pedal trends dark/gooey.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Type | Portastudio-424-MKI channel-strip preamp / drive / lo-fi fuzz |
| Controls | Volume (Master), Gain 1 (Trim), Gain 2 (Channel), Bass, Treble |
| Op-amps | UPC4570, NJM4565 (original 424 MKI parts) |
| Inputs | ¼" (top right) |
| Outputs | ¼" (top left) + balanced **XLR** (left side); simultaneous OK |
| Ground lift | Dip switch (left side) for XLR hum |
| Bypass | Soft-touch silent switching, **buffered bypass** |
| Power | 9VDC center-negative; **do not exceed 9V** |
| Current draw | **50 mA** |
| Channels | Mono in / mono out |
| Dimensions | 2.6" × 4.8" × 1.6" (66 × 122 × 41 mm) |
| MIDI | None |
| Price | $249 USD (Aug 2025) |
| Warranty | 4-year limited (USA) |

Source: [JHS Pedals 424 Gain Stage page](https://jhspedals.info/products/424-gain-stage) and pedal manual (jhs424.pdf).

## 13. Starting-Point Settings

Clock-face positions, viewed from above. Day-one references for the terminus slot; tune to taste against the Apollo's input meter.

**(a) Subtle always-on tape warmth** — the default "print," barely-there glue
- Volume: 12 · Gain 1: 9 · Gain 2: 10 · Bass: 12 · Treble: 1
- Just rubbery compression and a little channel grain. Use as the permanent baseline under everything. Hit the Apollo near unity.

**(b) Saturated 4-track grit** — audible cassette dirt, still musical
- Volume: 11 · Gain 1: 12 · Gain 2: 12 · Bass: 11 · Treble: 12
- Grainy lo-fi grit on the bus; chords smear, single notes bloom. The "obviously recorded to a four-track" finish.

**(c) Lo-fi degraded print** — blown-out, ruined-cassette terminus
- Volume: 11 · Gain 1: 2 · Gain 2: 1 · Bass: 1 · Treble: 11
- Speaker-ripping, gated, gooey. The drone/doom "recorded-wrong" wall. Watch Bass — pull back if the low end flubs. Pair with the PORTA424 kept clean so only one stage is destroying.

**(d) Bus terminus / clean DI commit** — color without overt dirt, XLR to Apollo
- Volume: 1 · Gain 1: 10 · Gain 2: 9 · Bass: 12 · Treble: 12
- Warm, compressed, high-headroom channel tone as the final glue. Take the **XLR** out; engage ground-lift if the rack hums. Lets the upstream tape voices read while the 424 simply finishes them.

## 14. Versus Alternatives — Why It Earns the Final Always-On Slot

The decisive comparison is **vs the MXNHLT PORTA424 directly upstream**, since the obvious objection is "why two Portastudio boxes?"

- **MXNHLT PORTA424** — "an almost exact recreation of a single channel" of the Tascam Porta MK1, built to include "the entirety of the signal path with meticulously reconstructed gain staging" (In/trim → bass/treble shelving EQ → channel **slide-fader** → master). It is the *complete, faithful channel-strip DI tone* — and notably **has no XLR**, true-bypass, 125B, 9–18V capable ([MXNHLT page](https://mxnhlteffects.com/products/porta424-channel-strip); [Guitar Pedal X comparison](https://www.guitarpedalx.com/news/gpx-blog/4-of-a-kind-tascam-424-portastudio-style-preamps)). Use it as the *polished four-track tone*.
- **JHS 424 Gain Stage** — the same 424 MKI signal path but voiced and marketed as a **gain device** ("clean, lo-fi → blown out fuzz"), with the **original op-amps**, an **XLR direct-out + ground lift**, and a **buffered (not true) bypass** suited to a terminus. Use it as the *commit/print* that drives the result into the Apollo.

Running PORTA424 → JHS 424 is two cassette channels in series — the period-correct "bounce one track to another" move. The PORTA424 gives the cleaner, fuller, faithful channel; the JHS 424 supplies the extra gain stage, the balanced output to the interface, and the buffered always-on terminus behavior. They are **the same concept tuned for different jobs in the chain**, which is exactly why the rig keeps both.

Other Portastudio-style options, for context ([Guitar Pedal X](https://www.guitarpedalx.com/news/gpx-blog/4-of-a-kind-tascam-424-portastudio-style-preamps)):
- **Benson Portable Distortion 424 MKII ($188)** — slightly simplified (4 controls, adds a Lo-Z impedance option). Reach for it if you want the most player-friendly, attractive take; the JHS has the extra gain-stage control and the XLR.
- **Neutrino Labs MX 424 ($141)** — the budget option, *also* with an XLR out. The closest functional rival to the JHS terminus role at lower cost; the JHS wins on the original op-amps and JHS support/warranty.

**Why the JHS 424 earns the last always-on slot in *this* rig specifically:** (1) it's the only Portastudio box here with a **balanced XLR direct-out + ground lift** — the right interface to the Apollo; (2) its **buffered bypass and high output** make it a stable, set-and-forget terminus; (3) its **gain-stage voicing** lets it *commit* the whole bus to cassette character in a way the cleaner PORTA424 deliberately doesn't; and (4) it completes the **JHS bookend** with the Colour Box V2 — console front-end at the start, four-track channel at the finish. The PORTA424 supplies the tone; the JHS 424 prints it.

## Sources

- [JHS Pedals — 424 Gain Stage product page](https://jhspedals.info/products/424-gain-stage)
- JHS 424 Gain Stage manual (local: `manuals/jhs424.pdf`)
- [MusicRadar — JHS 424 Gain Stage review (4.5/5)](https://www.musicradar.com/guitars/guitar-pedals/jhs-pedals-424-gain-stage-review)
- [MusicRadar — "He's not using a guitar amp. He's using a Tascam 424" (origin / Mk.gee feature)](https://www.musicradar.com/guitars/guitar-pedals/hes-not-using-a-guitar-amp-hes-using-a-tascam-424-jhs-pedals-puts-a-portastudio-in-a-pedal-to-help-you-recreate-mk-gees-elastic-lo-fi-tones)
- [Guitar World — JHS Pedals 424 Gain Stage review](https://www.guitarworld.com/gear/effects-pedals/jhs-pedals-424-gain-stage-review)
- [Guitar World — John Mayer demos the JHS 424](https://www.guitarworld.com/gear/guitar-pedals/john-mayer-demos-the-jhs-424-gain-stage)
- [Bass Musician Magazine — 424 Gain Stage review (bass)](https://bassmusicianmagazine.com/2025/12/review-jhs-424-gain-stage-pedal-lo-fi-roots-serious-bass-utility/)
- [Guitar Pedal X — 4 of a Kind: Tascam 424 Portastudio-style preamps compared](https://www.guitarpedalx.com/news/gpx-blog/4-of-a-kind-tascam-424-portastudio-style-preamps)
- [MXNHLT — PORTA424 channel strip product page](https://mxnhlteffects.com/products/porta424-channel-strip)
- [zZounds blog — the 424 Gain Stage / Portastudio history](https://blog.zzounds.com/2025/08/21/the-jhs-424-gain-stage-brings-the-portastudio-to-your-pedalboard/)
- [Reverb — The Tascam Portastudio Through the Ages](https://reverb.com/news/the-tascam-portastudio-through-the-ages)
- [Happy Mag — JHS 424 Gain Stage full demo/review (YouTube)](https://www.youtube.com/watch?v=LXhkhDbGEUw) *(not JHS's official channel — see §10)*
- [Loopy Demos — JHS 424 Gain Stage](https://loopydemos.com/demos/jhs-pedals-424-gain-stage/)
