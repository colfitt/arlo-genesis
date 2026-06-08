# Strymon Iridium — Deep Research

A working dossier for a pedal that doesn't make the boards. The Iridium is a genuinely excellent amp + IR cab modeler — three classic amps, premium impulse responses, a hybrid room — but in *this* rig it sits **on the bench**, and the rig sheet's reason is one line: *"VG-800 covers cab/amp modeling."* That's true as far as it goes, and this document's job is to take it the rest of the way: document what the Iridium actually does, compare it honestly to the [Boss VG-800](../../Roland%20VG-800/research/VG-800-DeepResearch.md) that benches it, and pin down the specific situations where the Iridium is unambiguously the better tool — the owner's magnetic-pickup guitars, a clean DI, a travel rig, and failover. It's not a redundant pedal. It's a *deliberately-not-needed-right-now* pedal, which is a different thing.

## 1. Lineage — what it actually is

The Iridium is Strymon's 2019 entry into the "amp-in-a-box, but digital and serious" category. It is three things in one enclosure: a **Matrix Modeled™ tube-amp emulator** (three amps), an **IR cab loader** (nine onboard 24-bit/96kHz impulse responses, plus user IRs), and a **DI/headphone box** with a hybrid IR/algorithmic room. The intent, per [Strymon](https://www.strymon.net/product/iridium/), is to "leave your amps at home and connect Iridium directly to the house PA system" or a recording interface — it is built to *replace* the amp/mic/cab signal chain, not sit in front of an amp.

The three amps (manual pp.6–7, [Strymon product page](https://www.strymon.net/product/iridium/)):

- **Round** — based on a **Fender Deluxe Reverb** (Normal channel): clean, bright, mid-scooped, lots of headroom. Strymon added a MIDDLE control the real Deluxe doesn't have (noon = the original fixed-resistor value).
- **Chime** — based on the **Brilliant channel of a Vox AC30 Top Boost**: jangly, airy, bites when you dig in. Here the MIDDLE knob acts as a *high-cut* (per the AC30TB design), and the top of the DRIVE range adds a frequency-shaped front-end boost that tightens lows while pushing into saturation.
- **Punch** — based on a **Marshall Plexi (Super Lead model 1959)**: meatier, higher-gain, powerful mids. DRIVE around 2 o'clock is the original Plexi ceiling; past 2 o'clock accesses custom hot-rodded Plexi gain Strymon added.

This is the same Matrix Modeling engine Strymon later spread across the **Sunset/Riverside** generation and the bigger **Volante/Iridium-adjacent** DSP boxes; the closest siblings are the single-amp [UAFX Ruby/Dream/Lion](https://www.uaudio.com/) and the [Walrus ACS1](https://www.walrusaudio.com/) (three-amp, three-cab, the Iridium's most direct competitor). Within Strymon's own line it's the "amp" specialist the way the BigSky is the "reverb" specialist — one job, done deeply.

**Firmware** is mature and worth tracking ([Strymon release notes](https://www.strymon.net/faq/iridium-firmware-revision-release-notes/)): latest is **Rev 1.33 (Nov 2024)** ("compatibility with Nixie 2.0," requires Nixie 2.2.0 to update). The single most rig-relevant update is **Rev 1.32 (Oct 2023)**, which added the **AMP DISABLE** Live Edit function (run cab + room on a non-guitar source, e.g. a synth or a bass DI) and made LEVEL TRIM persist through power cycles. Earlier milestones: 1.19 added MIDI volume-pedal CC#9; 1.12 fixed ROOM-ambience distortion and added USB MIDI preset saving.

## 2. Controls — the amp/cab/room/IR system

Eight knobs, two switches, two footswitches (manual pp.6–12):

- **AMP** (3-position toggle) — round / chime / punch.
- **CAB** (3-position toggle) — a / b / c. Each amp gets three cabs (see §3). Each cab is a stereo pair of 24-bit/96kHz **500ms** IRs; mono cabs load the same IR both sides.
- **DRIVE** — gain into both the analog JFET input stage *and* the modeled preamp. As DRIVE rises, LEVEL auto-compensates so output stays put. Up to **22 dB** of pure analog front-end gain (manual p.34).
- **LEVEL** — master out (controls OUT L, OUT R, and headphone).
- **BASS / MIDDLE / TREBLE** — a proper interactive tone stack. MIDDLE behaves differently per amp (tone-stack mids on Round/Punch; high-cut on Chime — see §1).
- **ROOM** — level of a **hybrid room**: 256ms real-room IRs blended with algorithmic reverb for extended decay. Room *size* (small/medium/large) is a Live Edit on the ON footswitch + ROOM knob; **the IR portion of the room is not user-replaceable** (manual p.9).
- **FAV footswitch** — recalls one stored Favorite (all knob + switch positions). Save: hold FAV until it blinks blue, press again.
- **ON footswitch** — enables amp/cab/room; LED color shows Output mode (red = Normal).

**IR loading** is the headline flexibility. The nine factory IRs can be swapped for any **24-bit/96kHz WAV** IR via Strymon's free **Impulse Manager** software over USB ([Impulse Manager support](https://www.strymon.net/support/impulse-manager/)). And per the manual (p.5), you can load *any* 24-bit/96kHz WAV as an "IR" — bass cabs, acoustic body resonance, even music samples — which, combined with AMP DISABLE, turns the Iridium into a general-purpose convolution box, not just a guitar-cab loader.

**Power Up Modes** (held footswitch + DRIVE knob at power-on, manual pp.16–17) set three global behaviors that matter for this rig:
- **Output Mode** — Normal / Cab Bypass (amp + room, no cab — feed a real power amp/FX return) / Amp Bypass (cab + room only — load an external preamp pedal like a Riverside into the IR engine).
- **Input Level** — Instrument (default) or **Line (+10 dB headroom)** — critical, because a pedalboard or the VG-800's line output can clip the Instrument input.
- **EXP Jack** — Expression (knob-morph), Volume Pre/Post, Digital (MultiSwitch Plus = 3 presets, or MIDI EXP cable = 300 presets).

## 3. Sonic character — the three voices and the IRs

The consensus from the written reviews ([Guitar Player](https://www.guitarplayer.com/reviews/strymon-iridium-amp-and-ir-cab-pedal-review), [MusicRadar](https://www.musicradar.com/reviews/strymon-iridium), [Premier Guitar](https://www.premierguitar.com/gear/strymon-iridium-review), [Guitar World](https://www.guitarworld.com/reviews/strymon-iridium-review)) is unusually unanimous: the three amp models are *realistic*, touch-sensitive, and the clean-to-clipping transition feels like a real amp — slightly smoother on Chime and Punch than on Round. Reviewers repeatedly note the models "hold their own against any rival products," and the cab sims are the part everyone singles out as best-in-class.

The amps:
- **Round (Deluxe Reverb)** — the clean platform. Big headroom, glassy top, scooped mids at noon MIDDLE. The single best amp on the pedal for a *pristine DI* — pedals in front, clean modeled cab behind. Turn MIDDLE up for tweedier grit.
- **Chime (AC30TB)** — jangle and air, the most "alive" of the three at low volume, and the one that rewards a light pick attack. The DRIVE-range front-end boost lets it get genuinely saturated without turning to mush.
- **Punch (Plexi)** — the rock amp. Smooth, buttery overdrive at moderate DRIVE; hot-rodded gain past 2 o'clock. Best mid presence of the three, which matters in a dense mix.

The nine factory IRs (manual p.7 / [Appendix 2]) come from four respected vendors — **OwnHammer, Celestion, cabIR.eu, Valhallir.at** — and are based on:
- **Round:** a) 1x12 Fender Deluxe Reverb, b) 1x12 Fender Blues Junior, c) 2x10 Fender Vibrolux
- **Chime:** a) 2x12 Vox AC30-6 open-back fawn, b) 1x12 custom w/ Celestion Blue AlNiCo, c) 4x12 Mesa/Boogie Half-Back
- **Punch:** a) 4x12 Marshall w/ Celestion G12M-25s, b) 2x12 custom w/ Celestion Vintage 30s, c) 8x12 Marshall w/ Celestion T652s

The IR quality is the Iridium's actual edge over the VG-800: full **stereo, 24-bit/96kHz, 500ms** convolution from premium third-party vendors, versus the VG-800's internally-modeled (and, per its reviewers, *weaker*) amp/cab section. If the job is "the most natural-sounding direct amp tone in the rig," the Iridium wins that contest cleanly.

## 4. Behavioral notes — DI, stereo room, headroom, latency

- **DI use.** This is what it's *for*. Output impedance 100 Ω, max input level +8 dBu, A/D & D/A at 24-bit/96kHz, S/N 110 dB typical (manual p.35). It is a studio-grade DI front-to-back; into an Apollo x8 line input it needs nothing else. Strymon explicitly markets the headphone jack for "latency-free monitoring" ([product page](https://www.strymon.net/product/iridium/)).
- **Stereo room.** MONO in / **stereo out** is the native mode (rear switch: MONO / STEREO / SUM). The hybrid room is genuinely stereo and is the secret weapon for the owner's drone/wall aesthetic — a sustained chord through Round + a large room blooms into a wide, ambient pad with zero added pedals. Note the rig is mostly mono until the CE-2W split, so a stereo Iridium would either need to live *after* that split or run mono (OUT L).
- **Headroom.** The 22 dB JFET front end plus Line input mode (+10 dB) means it tolerates hot sources without clipping — relevant if it ever takes the VG-800's line output (set Input Level = Line).
- **Latency.** Strymon markets "latency-free" monitoring and no reviewer reports perceptible lag; treat it as imperceptible-but-nonzero (it's a SHARC DSP convolution box — 1585 MegaFLOPS, 32-bit float, manual p.34). **No millisecond figure is published — flag as unverified**, but it is not a pitch-tracking device, so there's none of the VG-800's tracking-wobble caveat. It just converts and convolves.
- **Bypass.** Buffered bypass (manual p.35) — requires power to pass signal, like most DSP pedals. Not relevant on the bench, relevant if it's ever in a live failover chain.

## 5. Bench placement — why it's off the board, and when it shouldn't be

**Why it's benched.** The rig sheet says *"VG-800 covers cab/amp modeling,"* and architecturally that's correct: the VG-800 sits dead-first, reads the GK-5 divided pickup off the baritone Jazzmaster and the EBM-5 banjo, and outputs a modeled/synth/alt-tuned signal that already includes amp + cab. Putting the Iridium *after* the VG-800 would be a second cab sim stacked on the first — redundant and muddy. And the VG-800 is the only box that can read the GK-5 at all, so it *has* to be first; the Iridium can't take its slot. As the [VG-800 dossier](../../Roland%20VG-800/research/VG-800-DeepResearch.md) puts it: the VG-800 owns cab/amp duty *because* it also owns everything the Iridium can't — alt tuning, per-string processing, synth, pitch-to-MIDI. You want a shape-shifter, so the shape-shifter wins the slot.

**But here's the honest other half**, and it's the reason this pedal stays in the studio rather than getting sold:

1. **The magnetic-pickup guitars.** The owner's **Gibson SG, MIJ Jazzmaster, and Jazz Bass** do *not* have GK-5 pickups. They can't feed the VG-800 meaningfully (only via its NORMAL magnetic blend, which isn't its purpose). For those instruments, the VG-800 is the wrong tool and **the Iridium is the natural one** — plug the SG straight in, pick an amp, get a great direct tone to the Apollo with zero tracking caveats. This is the Iridium's strongest claim on a permanent role.
2. **Simple DI / "I just want a good amp tone."** When the goal is a pristine Deluxe clean or a Plexi crunch printed direct — no synth, no granular, no wall — the Iridium does it more naturally than the VG-800's amp section (which its own reviewers rank below dedicated modelers and call "harsh/digital" into a real amp). The [VG-800 dossier](../../Roland%20VG-800/research/VG-800-DeepResearch.md) concedes this directly: *"If you only wanted a great direct amp tone, the Iridium would be the pick."*
3. **Travel / fly rig.** A pedalboard-sized DI that turns any magnetic guitar into a full amp+cab+room into FOH or an interface is the ideal grab-and-go. Pair with the **UAFX Del-Verb** (also benched "travel board only") and a tuner and you have a complete gig.
4. **Failover.** If the VG-800 dies on stage or in a session, the Iridium is the instant amp/cab substitute for any non-GK guitar — drop it in, keep playing.

So: benched for the *main* GK-driven board, but the better tool the moment a normal guitar is in hand or the goal is a clean direct amp tone.

## 6. Source-specific behavior

**Gibson SG / MIJ Jazzmaster (magnetic, NO GK-5).** Home turf. Straight into the Iridium's 1 MΩ instrument input. The SG's humbuckers love **Punch** (Plexi mids); the Jazzmaster's single-coils sparkle through **Chime** (AC30) or stay clean and wide through **Round** (Deluxe) + a large room. Input Level = Instrument. This is the use case the VG-800 simply can't serve well, and it's why the Iridium earns studio space.

**Baritone Jazzmaster (its magnetic pickups, not the GK path).** The baritone's low fundamentals suit **Punch** or **Round** with BASS pulled back a touch to keep it from flubbing. Note: the baritone normally feeds the VG-800 via GK-5 — but its *magnetic* output is available too, and the Iridium is the right destination for it when you want the real instrument rather than a model of it.

**Jazz Bass.** With **AMP DISABLE** (firmware 1.32+) you can run the Iridium as a cab + room *only* on the bass — load a bass-cab WAV via Impulse Manager and the Iridium becomes a clean bass DI with a real cab IR and room. Or use **Punch** lightly for a grindy bass-amp tone. Either way it's a legitimate bass DI, which the VG-800 isn't really built to be for a passive Jazz Bass.

**NOT the GK-5 divided path.** The Iridium takes a normal summed magnetic input. It has no concept of per-string data, alt tuning, or synth — anything hex-divided must go through the VG-800. The Iridium and the GK path never meet.

## 7. Famous users (honest)

The Iridium is a *ubiquitous studio/fly-rig tool* rather than a signature-artist pedal — it's the kind of box that lives on thousands of pro boards as the silent DI, not the thing anyone's tone is "named after." But — correcting this dossier's original "no marquee user surfaced" note (revised during the usage-research pass, see `research/links/artist-notable-users.md`) — there *are* **verified** touring users (all use it as a direct-amp/FOH tool, none has a tone named after it):

- **Chris Shiflett (Foo Fighters)** — used the Iridium **instead of an amp** on his UK/Ireland solo tour, leaning on the **Round** (Deluxe) voice ([MusicRadar](https://www.musicradar.com/news/chris-shiflett-was-using-a-strymon-iridium-pedal-on-his-uk-tour-instead-of-an-amp)).
- **Mark Bowen (IDLES)** — the most rig-relevant: runs **two Iridiums** for all cab emulation on a noise/experimental board, even cabbing the **drummer's signal** (a real AMP-DISABLE-on-non-guitar use; [Premier Guitar Rig Rundown 2024](https://www.premierguitar.com/videos/rig-rundown/idles-2024)).
- **Larkin Poe (Rebecca & Megan Lovell)** — wired in "as a redundancy, and to provide sonic options for our front-of-house engineer" — the canonical failover/FOH role ([Guitar World](https://www.guitarworld.com/features/larkin-poe-rebecca-lovell-pedalboard)).

**Refuted:** an early search hit linked **Russian Circles' Mike Sullivan** to the Iridium, but his actual rig is **Verellen Meat Smoke / Loucks tube heads** — do *not* attribute. It's also heavily adopted in worship/modern-church circles and among gigging players flying direct-to-FOH. There is still no "Wata's Hizumitas"-style signature claim — but the marquee-user list is no longer empty.

## 8. Live / power / I/O

- **Power:** 9 VDC center-negative, **500 mA minimum** (manual p.35, [product page](https://www.strymon.net/product/iridium/)). This is a thirsty digital pedal — needs a dedicated high-current isolated slot, not a daisy-chain. Power supply *not* included.
- **I/O:** **IN** (1 MΩ instrument input; TRS adapter for stereo in), **OUT L / OUT R** (stereo out; OUT L = mono), rear **MONO/STEREO/SUM** input selector, **EXP** multifunction jack, **USB** (IR loading + firmware via Impulse Manager/Nixie), and a **stereo 1/8" headphone out** (voiced for 25–70 Ω phones; shares the main signal, LEVEL controls it).
- **MIDI:** No 5-pin DIN — MIDI runs over the **EXP jack** via a Strymon MIDI EXP cable or a MIDI→TRS interface (the rig's bench **EHX Effects Interface** is relevant here as a level/utility box, though MIDI specifically wants a TRS-MIDI adapter). Full MIDI: **300 presets** (3 banks), PC + CC. Key CCs (manual p.32): Amp = CC19 (1=round, 2=chime, 3=punch), Cab = CC20, Room Size = CC18, Drive = CC13, Level = CC12, Bass/Mid/Treble = CC14/15/16, Amp Disable = CC21, Bypass = CC102, Expression = CC100. So an H90 or a Blooper on the boards *could* flip Iridium presets if it were ever in the chain.
- **Expression:** TRS exp pedal → volume (pre or post amp), or knob-morph between two settings, or MultiSwitch Plus → 3 presets.
- **Bypass:** buffered.
- **Footprint:** 4.5" deep × 4" wide × 1.75" tall (11.4 × 10.2 × 4.4 cm) — small, fly-rig-friendly.
- **Price:** ~$399 ([Strymon](https://www.strymon.net/product/iridium/)).

## 9. Pairing recommendations (by name)

- **vs / alongside the VG-800:** don't stack them. If the VG-800 is doing amp+cab, run the Iridium in **Cab Bypass** or bypassed, or don't use it. The one sane *combined* move: VG-800 in **FX BYPASS** (raw model, no Boss cab) → Iridium IR engine, letting Strymon's superior IRs cab the Boss model. Niche, but it's the only non-redundant pairing.
- **As a DI into the Apollo x8:** the canonical role. SG/Jazzmaster → Iridium → Apollo line in. Print the clean modeled cab; re-amp later if wanted. This is the Iridium at its best in *this* studio.
- **Travel board:** Iridium + Polytune 3 + UAFX Del-Verb (bench mate) → interface or FOH. Complete amp+verb fly rig, no real amp.
- **Iridium → the End-Board reverbs (studio experiment):** a sustained Round/large-room chord into the **H90** (CrushedHall/Blackhole) or **Dark Star V3** is a ready-made drone source — the Iridium's clean stereo bloom gives the smear pedals something pristine to wreck, exactly the role the VG-800 dossier assigns to clean models.
- **External preamp into the IR engine:** **Amp Bypass** mode + a drive pedal (e.g. JHS Colour Box V2 or a Riverside-style preamp) → Iridium cabs the pedal. Turns the Iridium into a standalone IR loader for any dirt box.

## 10. Reviews & demos (real links)

- [Guitar Player — Iridium review](https://www.guitarplayer.com/reviews/strymon-iridium-amp-and-ir-cab-pedal-review) — best on amp realism and touch sensitivity.
- [MusicRadar — Iridium review](https://www.musicradar.com/reviews/strymon-iridium) — strong on the three voices and cab quality.
- [Premier Guitar — Iridium review](https://www.premierguitar.com/gear/strymon-iridium-review) — DI/recording context.
- [Guitar World — Iridium review](https://www.guitarworld.com/reviews/strymon-iridium-review) — concise verdict on versatility.
- [guitar.com — Iridium review](https://guitar.com/reviews/effects-pedal/review-strymon-iridium/) — UK perspective, IR discussion.
- [Pedal Battle: Walrus ACS1 vs Strymon Iridium (YouTube)](https://www.youtube.com/watch?v=2CFDEEvfopk) — the key A/B against its closest competitor.
- [UA Dream vs Walrus ACS1 vs Strymon Iridium (YouTube)](https://m.youtube.com/watch?v=AB_byXIXhVw) — three-way amp-modeler shootout.
- [Strymon — Using Iridium On Stage](https://www.strymon.net/iridium-live/) — official direct-to-PA workflow.
- [Strymon — Impulse Manager support](https://www.strymon.net/support/impulse-manager/) — custom IR loading.

## 11. Mods / quirks / firmware

- **No hardware mods** — sealed DSP box. "Mods" here means **custom IRs** (Impulse Manager) and firmware. The IR system *is* the mod surface: load any 24-bit/96kHz WAV, including non-cab impulses (bass cabs, acoustic body, music samples — manual p.5).
- **Firmware:** keep on **Rev 1.33** (Nov 2024); the must-have is **1.32**'s AMP DISABLE (cab/room on any source) and persistent LEVEL TRIM ([release notes](https://www.strymon.net/faq/iridium-firmware-revision-release-notes/)). Updating now uses the **Nixie 2.x** app rather than the old standalone updater.
- **Input Level trap:** default is Instrument; feeding it a hot/line source (a loud pedalboard, the VG-800's line out) without switching to **Line mode (+10 dB)** will clip the front end. Easy to miss.
- **Room IR is fixed** — only the room *size* and *level* are adjustable; you cannot replace the 256ms room IRs (manual p.9).
- **MIDI needs an adapter** — no DIN jack; everything rides the EXP/TRS jack. Plan cabling accordingly.
- **Power draw is real** — 500 mA minimum; underpowering it causes glitches. Don't daisy-chain.
- No widely reported reliability issues; standard Strymon build quality (made in USA).

## 12. Spec sheet

| Spec | Value |
|---|---|
| Type | Amp + IR cab modeler / DI (Matrix Modeled™ + convolution) |
| Amp models | Round (Fender Deluxe Reverb), Chime (Vox AC30TB Brilliant), Punch (Marshall Plexi 1959) |
| Cab IRs | 9 onboard (3 per amp), stereo 24-bit/96kHz 500ms; vendors OwnHammer, Celestion, cabIR.eu, Valhallir.at; user IRs loadable |
| Room | Hybrid 256ms IR + algorithmic reverb; small/medium/large; IR portion not replaceable |
| Controls | Drive, Level, Bass, Middle, Treble, Room; AMP + CAB toggles; FAV + ON footswitches |
| Output modes | Normal / Cab Bypass / Amp Bypass (global) |
| Input level | Instrument or Line (+10 dB) |
| Input impedance | 1 MΩ |
| Output impedance | 100 Ω |
| A/D & D/A | 24-bit / 96 kHz |
| Max input level | +8 dBu |
| Frequency response | 20 Hz – 20 kHz |
| Signal-to-noise | 110 dB typical |
| Analog front-end gain | up to 22 dB (discrete JFET) |
| DSP | SHARC, 1585 MegaFLOPS, 32-bit float |
| Latency | Marketed "latency-free"; no ms figure published (unverified) |
| I/O | IN (1 MΩ; TRS for stereo), OUT L/R, MONO/STEREO/SUM switch, EXP, USB, stereo 1/8" headphone |
| MIDI | Via EXP/TRS (no DIN); 300 presets, PC + CC |
| Bypass | Buffered |
| Power | 9 VDC center-negative, **500 mA min** (supply not included) |
| Dimensions | 4.5" D × 4" W × 1.75" H (11.4 × 10.2 × 4.4 cm) |
| Firmware (verified) | Rev 1.33 (Nov 2024) |
| Price | ~$399 US |

Sources: [Strymon product page](https://www.strymon.net/product/iridium/), [firmware release notes](https://www.strymon.net/faq/iridium-firmware-revision-release-notes/), Iridium User Manual Rev D (`manuals/`).

## 13. Starting-point settings

Clock-face, viewed from above. Output Mode = Normal unless noted.

**(a) Round clean DI** — pristine direct, pedals in front, the SG/Jazzmaster role
- AMP: round · CAB: a (1x12 Deluxe) · DRIVE: 9 · LEVEL: to taste
- BASS 12 · MIDDLE 11 · TREBLE 1 · ROOM 10 (small)
- Input Level: Instrument. Into Apollo line in. The cleanest, most "real amp" tone in the rig.

**(b) Chime jangle** — AC30 sparkle, light touch, single-coils
- AMP: chime · CAB: a (2x12 AC30 fawn) · DRIVE: 10–11 · LEVEL: to taste
- BASS 11 · MIDDLE 1 (high-cut up = darker; down = brighter) · TREBLE 12 · ROOM 11 (medium)
- Pick lightly for air; dig in for bite. Jazzmaster's bridge pickup shines here.

**(c) Punch wall** — Plexi mids into a big room, doom-adjacent direct tone
- AMP: punch · CAB: c (8x12 w/ T652s) · DRIVE: 2 o'clock+ (hot-rodded) · LEVEL: to taste
- BASS 1 · MIDDLE 1 · TREBLE 12 · ROOM 2 (large)
- SG humbuckers → sustained chord blooms into a wide ambient wall with no extra pedals. Run stereo out if after the CE-2W split.

**(d) Travel amp** — grab-and-go fly rig, any magnetic guitar → FOH
- AMP: round or punch · CAB: b · DRIVE: noon · ROOM: 12 (medium)
- Store as FAV. Iridium + Polytune + Del-Verb = complete gig. Headphone out for silent practice.

## 14. Versus alternatives — Iridium vs VG-800, and the bench verdict

**vs Boss VG-800 (the box that benches it).** Staying consistent with the [VG-800 dossier](../../Roland%20VG-800/research/VG-800-DeepResearch.md): the VG-800 is the *shape-shifter* — it reads the GK-5 divided pickup, models whole instruments, alt-tunes per string, synthesizes, and does pitch-to-MIDI, all in the first slot of Board 1. The Iridium does **none** of that. But the Iridium is the **better amp/cab modeler** in the narrow sense that matters: premium third-party stereo IRs (OwnHammer/Celestion/cabIR/Valhallir) and Matrix-Modeled amps that reviewers rank as genuinely amp-like, versus the VG-800's internally-modeled amp section that *its own* reviewers call the weak link and "harsh/digital" into a real amp. The VG-800 dossier states the trade plainly: *"It models amps arguably more naturally than the VG-800… If you only wanted a great direct amp tone, the Iridium would be the pick; you want a shape-shifter, so it isn't."* This dossier agrees and adds the corollary: **for the owner's non-GK guitars (SG, Jazzmaster, Jazz Bass), the VG-800 is the wrong tool and the Iridium is the right one** — there the comparison inverts entirely.

**vs Walrus ACS1.** The Iridium's closest direct competitor — also three amps, three cabs, stereo, DI. The ACS1 is the main A/B in every shootout ([Pedal Battle](https://www.youtube.com/watch?v=2CFDEEvfopk)). Differences are a matter of voicing taste, not capability; the Iridium's room and IR vendor pedigree are its edge, the ACS1's preset-per-amp memory is its. Either would serve the magnetic-guitar/DI role; the owner already has the Iridium, so it's moot.

**vs UAFX Ruby/Dream/Lion.** Single-amp boxes with speaker/room and (newer) DI'ing into the UA ecosystem. More specialized, arguably even more realistic per-amp, but you'd need three pedals to match the Iridium's three voices. No reason to add one when the Iridium covers all three.

**vs a real amp + mic.** The thing the Iridium replaces. In this all-direct, print-to-tape studio it's no contest — the Iridium *is* the amp, and there's no amp in the rig to mic.

**Bottom-line verdict on the bench decision: correct, with a permanent studio role.** Benching the Iridium for the *main GK-driven board* is the right call — the VG-800 has to be first (only it reads the GK-5), it already provides amp+cab, and stacking the Iridium behind it would be redundant. The rig sheet's one-liner holds. But the Iridium should **never leave the studio**: it is the natural, better-sounding amp/cab/DI for every magnetic-pickup guitar the owner plays that *doesn't* go through the VG-800, the simplest path to a great direct tone, the obvious travel rig, and the instant failover if the VG-800 dies. It's not a benched-because-redundant pedal; it's a benched-because-the-other-board-doesn't-need-it pedal — and it's the single most useful thing on the bench the moment an SG or a Jazzmaster is plugged in.

## Sources

- [Strymon — Iridium product page](https://www.strymon.net/product/iridium/)
- [Strymon — Iridium Firmware Revision Release Notes](https://www.strymon.net/faq/iridium-firmware-revision-release-notes/)
- [Strymon — Impulse Manager support](https://www.strymon.net/support/impulse-manager/)
- [Strymon — Using Iridium On Stage](https://www.strymon.net/iridium-live/)
- [Strymon — Iridium support hub](https://www.strymon.net/support/iridium/)
- [Guitar Player — Strymon Iridium review](https://www.guitarplayer.com/reviews/strymon-iridium-amp-and-ir-cab-pedal-review)
- [MusicRadar — Strymon Iridium review](https://www.musicradar.com/reviews/strymon-iridium)
- [Premier Guitar — Strymon Iridium review](https://www.premierguitar.com/gear/strymon-iridium-review)
- [Guitar World — Strymon Iridium review](https://www.guitarworld.com/reviews/strymon-iridium-review)
- [guitar.com — Review: Strymon Iridium](https://guitar.com/reviews/effects-pedal/review-strymon-iridium/)
- [Equipboard — Strymon Iridium](https://equipboard.com/items/strymon-iridium-amp-ir-cab)
- [YouTube — Pedal Battle: Walrus ACS1 vs Strymon Iridium](https://www.youtube.com/watch?v=2CFDEEvfopk)
- [YouTube — UA Dream vs Walrus ACS1 vs Strymon Iridium](https://m.youtube.com/watch?v=AB_byXIXhVw)
- Iridium User Manual Rev D (local `manuals/` — primary source for controls, IR list, Power Up Modes, MIDI CC table, full specs)
- [Boss VG-800 Deep Research dossier](../../Roland%20VG-800/research/VG-800-DeepResearch.md) (in-repo, for the cab/amp comparison)
