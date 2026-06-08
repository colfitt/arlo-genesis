# Boss CE-2W (Waza Craft) Chorus — Deep Research

A working dossier for the one pedal on Board 1 that does two jobs at once. The CE-2W is Boss's all-analog Waza Craft reissue of the classic CE-2 chorus, with the original CE-1's chorus and vibrato modes folded in — but in this rig it is just as important as the **mono→stereo split point of the entire signal path**. Everything upstream of it (VG-800 through Caroline Somersault) is mono; the CE-2W is the box where the rig fans out to stereo, feeding the Strymon Deco V2 and the whole stereo Board 2 / Board 3 chain behind it. So this document treats it as a chorus *and* as the most consequential piece of routing infrastructure on the front board, sitting 12th on Board 1 — after the Somersault, before the Deco.

## 1. Lineage: CE-1 → CE-2 → Waza Craft

The CE family starts with the amp. Roland's **JC-120 Jazz Chorus** (1975) had a built-in chorus/vibrato circuit, and one year later Boss lifted that circuit into a floor box: the **CE-1 Chorus Ensemble**, released **June 1976** — the first-ever chorus pedal and the very first product to wear the Boss name ([BOSS Articles](https://articles.boss.info/the-legend-of-the-ce-1-and-re-201-preamps/), [GuitarPlayer Classic Gear](https://www.guitarplayer.com/gear/classic-gear-boss-ce-1-chorus-ensemble)). The CE-1 was a large AC-powered stereo unit built around the **Matsushita/Panasonic MN3002 BBD** (bucket-brigade device), with selectable chorus and vibrato modes — the same chorus-or-vibrato choice the JC-120 offered ([JonDent BBD writeup](https://djjondent.blogspot.com/2017/10/boss-ce-1-chorus-ensemble-panasonic-bbd.html)).

In **late 1979** Boss shrank the concept into the first compact-series chorus, the **CE-2**, re-engineering the circuit around the **MN3007 BBD** for lower noise and better clean headroom ([ElectroSmash CE-2 analysis](https://www.electrosmash.com/boss-ce-2-analysis), [Guitar World CE-2 history](https://www.guitarworld.com/gear/guitar-pedals/boss-ce-2-chorus-pedal-history)). The CE-2 dropped the CE-1's vibrato mode and stereo output, trading them for the compact, mono, set-and-forget chorus that defined the late-'70s/'80s chorus sound.

The **CE-2W** (2016, Made in Japan, Waza Craft line) is the reconciliation of those two ancestors in one enclosure. It keeps **all-analog BBD circuitry** (no digital modeling — Boss's marketing and every review confirm this) and a **three-position mode switch**: **Standard** (CE-2 voicing), **CE-1 Chorus**, and **CE-1 Vibrato** ([BOSS official product page](https://www.boss.info/us/products/ce-2w/), [Sound on Sound review](https://www.soundonsound.com/reviews/boss-ce-2w-waza)). Crucially it adds two things neither original had in this combination: **stereo output for the CE-2 mode**, and **variable chorus depth in the CE-1 modes** (the original CE-1 had a fixed chorus intensity). Guitar World's A/B against an original CE-2 called it "the most perfect match" between an original and a reissue, with maybe "slightly clearer treble" ([Guitar World CE-2W review](https://www.guitarworld.com/gear/review-boss-waza-craft-ce-2w-chorus-pedal)).

## 2. Controls & Modes

Two knobs, one mode switch, one footswitch — that's the whole interface.

- **RATE** — speed of the chorus/vibrato LFO. Ranges from "an extremely slow and gentle, almost phase-like chorus to a fast warble" per [Sound on Sound](https://www.soundonsound.com/reviews/boss-ce-2w-waza).
- **DEPTH** — modulation depth. Across all three modes. On the original CE-1 the chorus depth was fixed, so the CE-1 modes here are a genuine expansion, not just a recreation.
- **Mode switch (Standard / CE-1 Chorus / CE-1 Vibrato):**
  - **Standard** (marked "S") replicates the CE-2: per Boss's manual, "a chorus sound notable for its clarity; it will not impair the crispness of your guitar sound." Subtle, organic, the classic mild Boss chorus.
  - **CE-1 Chorus** reproduces the CE-1's chorus with deeper modulation — "deeper, queasier, and at certain settings seemingly just a little murkier" ([Premier Guitar](https://www.premierguitar.com/gear/boss-ce-2w-waza-craft-chorus-review)).
  - **CE-1 Vibrato** is the CE-1's true pitch-vibrato mode — "a unique chorus with strongly varying modulation" (manual). Lower settings sit close to another chorus voice with a touch of pitch shift; mid settings produce "a metallically tinged rotary speaker" character (Premier Guitar).

There is **no "standard vs custom" pair of voicings** here — the switch is literally labeled Standard / CE-1 / CE-1 (vibrato). The "S" on the panel means *Standard (CE-2)*, not a custom mode. (Some boutique CE-2 clones expose an internal depth trimmer; the CE-2W's depth is set entirely by the front-panel DEPTH knob — *unverified whether any internal trimmer exists on the CE-2W; treat the front-panel DEPTH as the only user-facing depth control.*)

## 3. Sonic Character vs Other Choruses

The CE-2W's signature is **warm, analog BBD chorus that stays musical and uncongested** — the MN-series bucket-brigade voicing rolls off some top end and adds the gentle pitch-shimmer that digital choruses tend to render too cleanly. Placement against the field:

- **vs the original CE-2:** essentially identical, with marginally clearer treble and a much lower noise floor; A/B-confirmed by Guitar World and Sound on Sound. You also get stereo and vibrato the original never had.
- **vs the original CE-1:** the CE-1 Chorus mode is darker, deeper, and "queasier" than the Standard mode — more obvious, more vintage-thick. Frusciante's lush rich CE-1 wash lives here.
- **vs the Caroline Somersault (immediately upstream):** this is the redundancy to be honest about. The Somersault is a lo-fi chorus/vibrato with a deliberately wobbly, degraded, "broken-tape" character and a havoc/limit feature. The CE-2W is the *clean, classic, hi-fi* analog chorus — it is the reference voicing, not the broken one. They are not interchangeable: the Somersault is the texture box, the CE-2W is the proper chorus *and* the stereo splitter. Running both at once stacks two modulations into mush unless one is set very subtle.
- **vs digital stereo choruses (e.g. Strymon-style multi-voice mod, TC Corona):** the CE-2W is one-voiced, less wide, less programmable, and noisier in absolute terms — but it has the analog character and the historical voicing those don't. It earns its slot on character and on being the stereo split, not on flexibility.

## 4. Behavioral Notes

- **Mono chorus vs the stereo output trick.** This is the most misunderstood thing about the pedal, and it matters for this rig. From **OUTPUT A (MONO)** alone you get the conventional sound: **chorus + dry, mixed together**, the familiar Boss chorus. The moment you plug into **OUTPUT B as well**, the routing changes: **OUTPUT A carries the chorus (wet) signal only, OUTPUT B carries the direct (dry) signal only** ([BOSS manual](manuals/CE-2W_eng02_W.pdf), official spec page). So the "stereo" here is a **wet/dry hard split**, not two independently-modulated L/R chorus voices. The width comes from one side being pure modulated signal and the other pure dry — which is exactly the lush, three-dimensional spread the CE-1 was famous for.
- **Vibrato is real pitch wobble.** In CE-1 Vibrato mode the dry signal is removed and you hear only the pitch-shifting BBD path, which is why it can warble like a rotary speaker. It is more dramatic and less "polite" than the chorus modes.
- **Low noise for analog.** Reviewers repeatedly note it's quiet for a BBD pedal; the MN3007-style circuit was always the cleaner of the CE family.

## 5. Signal-Chain Placement — Chorus *and* the Board 1 Stereo Split

This is the pedal's defining role in the rig and the reason it sits where it does. Board 1 runs:

`VG-800 → Polytune 3 → CB Clean → JHS Colour Box V2 → MXR 108 → EQD Hizumitas → CB Brothers AM → EAE Longsword → Oxford Drive → Boss BF-3 → Caroline Somersault → **CE-2W (stereo split)** → Strymon Deco V2 → (stereo to Board 2)`

- **It is the mono→stereo converter.** Everything from the VG-800 down through the Somersault is mono. The CE-2W is the first true stereo node. Wire **OUTPUT A → Deco V2 left/in-1** and **OUTPUT B → Deco V2 right/in-2** (or whatever the Deco's stereo input convention is) and the rest of the chain — Deco, OBNE Parting, Microcosm, Etherealizer, Dark Star, Generation Loss, Big Time, MOOD, Blooper, Chroma Console, H90 — all runs in stereo from here.
- **Wet/dry split feeds the Deco asymmetrically.** Because the CE-2W's stereo is wet-on-A / dry-on-B, the two sides into the Deco are *not* a matched stereo pair — one carries chorus, one carries dry. The Deco's bias/wobble and tape saturation then act on those two different inputs, which is a happy accident for the degraded aesthetic: the two channels diverge before the tape sim even touches them. If you want a more symmetrical stereo image into the Deco, run the CE-2W in mono (OUTPUT A only) and let the Deco/downstream pedals create width — but then you lose the split, so this is the trade-off to make consciously.
- **Buffered bypass means the split persists when the chorus is off… sort of.** When bypassed, the buffered circuit feeds the *same* signal to both outputs (Sound on Sound). So even with the chorus disengaged, OUTPUT A and OUTPUT B both pass dry signal — the stereo pair stays alive and the downstream stereo chain never collapses to mono. **This is the single most important reason the CE-2W is the right split point:** it keeps both legs fed whether the chorus is on or off. (Contrast a true-bypass stereo-out pedal, which could drop one leg when off.)
- **Order relative to the Deco is correct.** Chorus before tape saturation/doubling is the classic order — modulate first, then smear and saturate. The Deco's tape character thickens the already-chorused signal rather than the other way around.

## 6. Source-Specific Notes

- **Baritone Jazzmaster:** the CE-2W's home turf. Standard mode adds the classic shimmer without thinning the low end; the gentle BBD top-roll actually flatters a baritone's darker voice. Keep DEPTH modest so the lows don't pitch-warble into mud.
- **Gold Tone EBM-5 banjo via VG-800:** banjo is bright and transient-heavy. Standard mode (subtle) widens without exaggerating the attack; the CE-1 Vibrato mode on a banjo gets seasick fast — useful for drone passages, distracting for anything rhythmic. Because the split feeds stereo downstream, a banjo run through the wet/dry split spreads beautifully across the stereo field once the Microcosm/Dark Star get hold of it.
- **Modeled VG-800 signal:** the CE-2W sits after the VG-800's summed output, so it's chorusing an already-processed (modeled amp/synth/COSM) signal. On pad/synth patches the CE-1 Chorus or Vibrato mode turns a static pad into a moving, three-dimensional drone — exactly the wall-of-sound aesthetic. No added latency (all analog).
- **Bass (Jazz Bass):** Standard mode with low DEPTH is the safe bass chorus; the wet/dry stereo split is actually *better* for bass than a fully-wet chorus because OUTPUT B preserves a dry low-end anchor while OUTPUT A carries the modulation. Keep DEPTH low to avoid pitch-wobble on the fundamental.

## 7. Famous Users (CE Chorus History)

The CE-1/CE-2 voicing has a deep, *verified* discography — be precise about who used which:

- **John Frusciante (Red Hot Chili Peppers)** — long-time **CE-1** user, roughly 1990 until his 2010 departure and again on the 2022 *Unlimited Love* tour. His lush, rich chorus is the canonical CE-1 sound ([Ground Guitar](https://www.groundguitar.com/john-frusciante-gear/john-frusciantes-boss-ce-1-chorus-ensemble/), [Guitar World](https://www.guitarworld.com/news/behringer-boss-ce-1-chorus-ensemble-clone)). **Directly relevant to this rig:** Frusciante used the CE-1 *primarily as a signal **splitter*** between two amps — his own words (Vintage Guitar, 2009): *"a Boss Chorus Ensemble, which I use to split the signal in my rig."* The canonical CE-1 player is famous partly for using it the exact way the CE-2W functions here — as the stereo/dual-amp split point, with the chorus as a bonus.
- **James Honeyman-Scott (The Pretenders)** — switched to a **CE-2** for his live rig after using an EHX Clone Theory on the first album; his early Pretenders board was all-Boss (CE-2, CS-1, OD-1) ([Guitar World CE-2 history](https://www.guitarworld.com/gear/guitar-pedals/boss-ce-2-chorus-pedal-history)).
- **David Gilmour, Johnny Marr, Robert Fripp, Rory Gallagher, Billy Duffy, John Mayer, Keith Urban** — all named by Guitar World as CE-2 users (Gilmour reportedly used it as a substitute for earlier Uni-Vibes/phasers). The article does not pin specific recordings to each name, so cite them as users, not as specific tracks.

**Correction worth flagging:** Andy Summers and "Walking on the Moon" is *commonly miscredited* to a CE chorus — engineer accounts attribute that specific tone to a **Scamp rack module / Electric Mistress**, not a Boss CE pedal ([MusicRadar](https://www.musicradar.com/news/the-police-walking-on-the-moon-andy-summers-guitar), [Roland Australia](https://rolandcorp.com.au/blog/the-police-walking-on-the-moon-tone-dissected)). Summers did use a CE-1 elsewhere, but don't attribute that song to it. Likewise **Kurt Cobain** used an **EHX Small Clone** on *Nevermind*, not a CE-1/CE-2 — a frequent mix-up.

## 8. Live / Power / I/O

| | |
|---|---|
| **Power** | 9V DC, center-negative, via Boss PSA-series adaptor (or 9V battery) |
| **Current draw** | **25 mA** — low; any isolated supply slot handles it |
| **I/O** | INPUT (mono) · OUTPUT A (MONO) · OUTPUT B (stereo) — all 1/4" |
| **Bypass** | **Buffered** (not true bypass); feeds the same signal to both outputs when off |

Practical live points:
- **INPUT jack doubles as the power switch** — the pedal powers on when a cable is inserted into INPUT and off when unplugged (manual). On a permanently-patched board this is irrelevant; just know it's why it draws nothing until a cable is in.
- **Buffered bypass is a feature here, not a compromise.** As the rig's stereo split, you *want* a buffer feeding both legs — it keeps the downstream stereo chain alive whether the chorus is engaged or not, and presents a low (1 kΩ) output impedance to the long cable run into the Deco/Board 2.
- **1 MΩ input impedance** is high and friendly to whatever's upstream; the Somersault's output sees an easy load.
- Keep the battery out for live use and run it off the isolated supply; the INPUT-as-switch behavior plus a battery is just a drain risk.

## 9. Pairing Recommendations (by name)

- **Into Strymon Deco V2 (immediately downstream):** the intended pairing. Chorus → tape doubling/saturation. Use the wet/dry stereo split so the Deco's two channels diverge. For the degraded aesthetic, push the Deco's wobble — chorus pitch-mod plus tape wow/flutter compounds into genuine seasick motion.
- **Into Board 2 (OBNE Parting → Microcosm → Etherealizer → Dark Star V3):** the stereo split makes all of these wider. Dark Star V3 and Microcosm in particular love a pre-widened stereo source — the chorus gives the granular/reverb engines a moving target.
- **Redundancy with the Caroline Somersault (immediately upstream):** pick a lane. Use the **Somersault for the broken/lo-fi wobble** and keep the CE-2W in **Standard for a clean classic chorus + the stereo split**, or bypass the Somersault and let the CE-2W's **CE-1 Vibrato** be the dramatic modulation. Running both wet at depth = mush. The honest move: most of the time the CE-2W is on *for the split* in Standard mode (subtle), and the Somersault is the one you stomp for character.
- **BF-3 (flanger, upstream):** flanger → chorus is fine; just don't run flanger + chorus + Somersault all at once unless you want full smear.

## 10. Reviews & Demos (real links)

- [Sound on Sound — Boss CE-2W 'Waza'](https://www.soundonsound.com/reviews/boss-ce-2w-waza) — best on the wet/dry stereo behavior and buffered-bypass routing.
- [Premier Guitar — CE-2W review](https://www.premierguitar.com/gear/boss-ce-2w-waza-craft-chorus-review) — best mode-by-mode sonic description (Standard / CE-1 / Vibrato).
- [Guitar World — Waza Craft CE-2W review](https://www.guitarworld.com/gear/review-boss-waza-craft-ce-2w-chorus-pedal) — Platinum award; A/B vs original CE-2.
- [BOSS — A Chorus of Tones: CE-2W Studio Applications](https://articles.boss.info/a-chorus-of-tones-ce-2w-studio-applications/) — Boss's own two-amp stereo recording technique and settings.
- [Guitar World — How the Boss CE-2 took over the world](https://www.guitarworld.com/gear/guitar-pedals/boss-ce-2-chorus-pedal-history) — CE-2 history + verified user list.
- [ElectroSmash — Boss CE-2 circuit analysis](https://www.electrosmash.com/boss-ce-2-analysis) — MN3007 BBD technical teardown of the circuit the Standard mode recreates.

## 11. Mods / Quirks / Known Issues

- **INPUT-as-power-switch** can be a head-scratcher if signal dies — check the input cable is fully seated.
- **Wet/dry (not L/R) stereo** surprises people expecting two modulated channels. It is one wet, one dry. Know this when patching into the Deco.
- **Buffered bypass** means it always colors the signal slightly and always needs power; there's no true-bypass option. For this rig that's desirable (see §8), but a true-bypass purist should know.
- **No tap/MIDI/expression** — set-and-forget. Rate changes are manual only.
- **No widely reported reliability issues.** Standard Boss Waza build, **five-year warranty** (per official page). Made in Japan.
- *Unverified:* internal trimmers / mod points specific to the CE-2W. The classic CE-2 has documented mod communities (depth/rate range, tone), but CE-2W-specific mods are not well documented publicly — flagging rather than inventing.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Modes | Standard (CE-2 chorus), CE-1 Chorus, CE-1 Vibrato |
| Controls | RATE, DEPTH, mode switch, footswitch, CHECK indicator |
| Signal path | All-analog, BBD (bucket-brigade) delay line |
| Nominal input level | -20 dBu |
| Input impedance | 1 MΩ |
| Nominal output level | -20 dBu |
| Output impedance | 1 kΩ |
| Recommended load | 10 kΩ or greater |
| I/O | INPUT · OUTPUT A (MONO) · OUTPUT B (stereo) — all 1/4" |
| Stereo behavior | Output A = chorus only / Output B = direct only (when both used); Output A alone = chorus+direct mixed |
| Bypass | Buffered (feeds same signal to both outputs when off) |
| Power | 9V DC center-negative (PSA series) or 9V battery |
| Current draw | 25 mA |
| Battery life | ~32 h alkaline / ~18 h carbon-zinc |
| Dimensions | 73 (W) × 129 (D) × 59 (H) mm |
| Weight | 450 g (1 lb, incl. battery) |
| Made in | Japan (Waza Craft) |
| Warranty | 5 years (per official page) |

Sources: [BOSS official spec page](https://www.boss.info/us/products/ce-2w/) and the [CE-2W owner's manual](manuals/CE-2W_eng02_W.pdf).

## 13. Starting-Point Settings

Knob positions clock-face from above. Mode = switch position.

**(a) Subtle stereo widener** — the everyday "on for the split" setting
- Mode: Standard (CE-2)
- RATE: 9–10 o'clock (slow)
- DEPTH: just shy of noon
- Wire OUTPUT A → Deco L, OUTPUT B → Deco R. Quiet, classic, three-dimensional. This is the default Board 1 stereo state.

**(b) CE-1 lush** — Frusciante-style deep chorus wash
- Mode: CE-1 Chorus
- RATE: 10 o'clock
- DEPTH: 1–2 o'clock (deeper than the original CE-1 could go)
- Darker, thicker, "queasier." Great on the baritone for sustained chords into the Deco.

**(c) Deep vibrato** — seasick rotary wobble
- Mode: CE-1 Vibrato
- RATE: 11–1 o'clock
- DEPTH: 1–2 o'clock
- True pitch-vibrato, dry signal removed. Drone/psychedelic passages only — too dramatic for rhythm. Pairs with sustained VG-800 pads or Hizumitas walls upstream.

**(d) On-the-wall shimmer** — slow, oceanic, two-amp width
- Mode: Standard or CE-1 Chorus
- RATE: ~9 o'clock (very slow), per Boss's own studio note
- DEPTH: just shy of noon
- Boss's "living wall of sound" stereo technique (their two-amp recommendation, [studio-applications article](https://articles.boss.info/a-chorus-of-tones-ce-2w-studio-applications/)). With the wet/dry split feeding the Deco and Board 2, this is the drone/shoegaze foundation.

## 14. Versus Alternatives — Why It Earns Its Slot

As a *chorus*, there are wider, more programmable options (Strymon Ola/MultiSwitch-class digital choruses, TC Corona, even the Somersault already on the board for the broken stuff). As a *standalone* analog chorus it would be a luxury given the Somersault is right in front of it.

But it does not earn its slot as just a chorus — **it earns it as the rig's mono→stereo split point that also happens to be a world-class analog chorus.** The specific reasons no obvious alternative beats it here:

- **It splits to stereo *and* keeps both legs fed when bypassed** (buffered bypass → same signal to both outs). A passive Y-split or true-bypass stereo pedal would risk dropping a leg or loading the signal badly. The CE-2W's 1 kΩ buffered output is purpose-built to drive the long run into the Deco and Board 2.
- **The wet/dry split is musically useful** rather than a limitation — it gives the Deco two divergent channels for free, which the degraded/tape aesthetic exploits.
- **The voicing is the historically-correct one** — if you're going to put a chorus at the split anyway, the CE-1/CE-2 analog character is the best possible choice for warmth and the drone/shoegaze palette.
- **It's analog, low-noise, and bombproof** — set-and-forget infrastructure you don't have to think about, which is exactly what a split point should be.

Net: a dedicated splitter/buffer would do the routing but add nothing musical; a fancier chorus would add flexibility but a worse split and redundancy with the Somersault. The CE-2W does both jobs in one trustworthy box — that's why it sits 12th on Board 1, right where mono becomes stereo.

## Sources

- [BOSS — CE-2W official product page (US)](https://www.boss.info/us/products/ce-2w/)
- [BOSS — CE-2W owner's manual (local)](manuals/CE-2W_eng02_W.pdf)
- [BOSS Articles — The Legend of the CE-1 and RE-201 Preamps](https://articles.boss.info/the-legend-of-the-ce-1-and-re-201-preamps/)
- [BOSS Articles — A Chorus of Tones: CE-2W Studio Applications](https://articles.boss.info/a-chorus-of-tones-ce-2w-studio-applications/)
- [Sound on Sound — Boss CE-2W 'Waza' review](https://www.soundonsound.com/reviews/boss-ce-2w-waza)
- [Premier Guitar — Boss CE-2W Waza Craft Chorus review](https://www.premierguitar.com/gear/boss-ce-2w-waza-craft-chorus-review)
- [Guitar World — Review: Boss Waza Craft CE-2W Chorus Pedal](https://www.guitarworld.com/gear/review-boss-waza-craft-ce-2w-chorus-pedal)
- [Guitar World — How the Boss CE-2 Chorus pedal took over the world](https://www.guitarworld.com/gear/guitar-pedals/boss-ce-2-chorus-pedal-history)
- [GuitarPlayer — Classic Gear: Boss CE-1 Chorus Ensemble](https://www.guitarplayer.com/gear/classic-gear-boss-ce-1-chorus-ensemble)
- [ElectroSmash — Boss CE-2 circuit analysis](https://www.electrosmash.com/boss-ce-2-analysis)
- [JonDent — Boss CE-1 Chorus Ensemble & the Panasonic BBD](https://djjondent.blogspot.com/2017/10/boss-ce-1-chorus-ensemble-panasonic-bbd.html)
- [Ground Guitar — John Frusciante's Boss CE-1 Chorus Ensemble](https://www.groundguitar.com/john-frusciante-gear/john-frusciantes-boss-ce-1-chorus-ensemble/)
- [Guitar World — Behringer clone of Frusciante's CE-1](https://www.guitarworld.com/news/behringer-boss-ce-1-chorus-ensemble-clone)
- [MusicRadar — The Police 'Walking On The Moon' (not a flanger/chorus pedal)](https://www.musicradar.com/news/the-police-walking-on-the-moon-andy-summers-guitar)
- [Roland Australia — 'Walking On The Moon' tone dissected](https://rolandcorp.com.au/blog/the-police-walking-on-the-moon-tone-dissected)
