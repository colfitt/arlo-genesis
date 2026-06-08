# JHS Colour Box V2 — Deep Research

A working dossier for the Colour Box V2 (10th-anniversary edition) as it sits 4th on Board 1 — after CB Clean, *before* the MXR 108 fuzz and the EQD Hizumitas. In this rig it is not an effect, it's a front-end: a Neve-console-voiced preamp/EQ that pre-shapes everything the fuzz wall is about to chew on, and a one-box DI/console-print stage that pairs conceptually with the tape emulation (PORTA424, JHS 424) and Apollo print at the end of the chain. The rig notes mark it "always-on when able" — so most of this document is about what it does to a signal *before* distortion, and how its EQ steers the 108 and Hizumitas.

> **Correction up front:** the GearProfile lists `io: stereo-in/stereo-out` and the rig brief says "the V2 added stereo." **This is wrong — the Colour Box V2 is a mono device.** JHS's own product page lists it as mono in/mono out. The "two outputs" people mistake for stereo are a 1/4" jack and an XLR jack carrying the *same mono signal* to two destinations in parallel (e.g. amp + FOH). It splits, it does not pan. Everything below treats it as mono. (Flagged so the GearProfile metadata gets fixed.)

## 1. Lineage: Neve 1073 in a Box → V1 → V2

The Colour Box is JHS's attempt to put the front end of a vintage recording console — specifically the [Neve 1073](https://jhspedals.info/products/colour-box-v2) discrete mic-pre + EQ — at your feet. The pitch JHS leans on is the classic "plug a guitar straight into the console" sound: the [Beatles' "Revolution," Led Zeppelin's "Black Dog," the Byrds' "Mr. Tambourine Man," Chic's "Le Freak"](https://www.premierguitar.com/gear/jhs-colour-box-review) — direct-in tones where the preamp itself, driven hard, *is* the distortion. There's no amp, no fuzz circuit; it's a clean gain stage overloaded into "broken console" territory.

The **original Colour Box (V1, 2014)** built this around a **Lundahl transformer** ("a marquee component" per [Premier Guitar](https://www.premierguitar.com/gear/jhs-colour-box-review)), two cascaded gain stages, a five-step gain switch (+18 to +39 dB), a fixed three-band EQ and a sweepable high-pass. It ran on **18V** and had **seven controls** in a smaller box. JHS describes the topology as derived from the discrete gain stage in the 1073, "but with two gain stages in series instead of one." Treat the "Neve" framing as inspiration, not a literal 1073 clone — it's a JHS interpretation that gets convincingly in the neighborhood.

The **V2 (the unit here, a 10th-anniversary edition with the deep-navy chassis)** keeps all the V1 functionality and adds, per [JHS](https://jhspedals.info/products/colour-box-v2):

- An **output transformer** (the V1's transformer was on the input/power side; V2 adds iron on the output).
- **48V phantom power pass-through** — you can now run a real condenser into the XLR input.
- **EQ "Shift" knobs** — each of the three bands now sweeps its center frequency instead of being fixed.
- A **Hi/Lo gain toggle** for selectable clean headroom vs. distortion.
- **Silent (relay) switching** and a lower noise floor.
- A **larger enclosure, ten knobs**, and — notably — a switch to **9V power** from the V1's 18V. (Don't read 9V as "less hungry"; see §8.)

## 2. Controls (every knob and switch, from the manual)

The face splits into a red **Gain** section and a blue **EQ** section, plus side-mounted utility switches.

**Gain (red):**
- **MASTER** — overall output volume, after everything. Works in tandem with PRE-VOL. For clean tones: MASTER high, PRE-VOL low. Use it to claw back the volume jump as you add gain.
- **PRE-VOL** — the "gain/drive" knob. Sits *between the two gain stages* and sets how hard the first stage slams the second. This is where grit → distortion → console-fuzz lives.
- **STEP** — a five-position stepped gain switch setting each preamp stage's base gain: **1st +18 dB, 2nd +23 dB, 3rd +28 dB, 4th +33 dB, 5th +39 dB** (per the manual). This is your coarse gain; PRE-VOL is the fine drive within it.

**EQ (blue) — "highly modified Baxandall type," updated for V2:**
- **TREBLE / MIDDLE / BASS** — **TREBLE ±15 dB, MIDDLE ±10 dB, BASS ±15 dB**, flat at noon (per JHS's current official product page).
- **TREBLE SHIFT / MID SHIFT / BASS SHIFT** — sweep the center frequency each band acts on. **Per JHS official:** TREBLE **2 kHz–30 kHz**, MIDDLE **150 Hz–2.4 kHz**, BASS **20 Hz–440 Hz** (these match WaveInformer's measured ranges).
  > **Spec reconciliation (corrected 2026-06):** an earlier draft of this dossier cited a manual figure of **±17 dB** and fixed centers (Treble 10 kHz / Mid 1 kHz / Bass 120 Hz). JHS's **current official product page** + WaveInformer + the on-screen manual in the Produce Like A Pro video all agree instead on the **±15/±10 dB** swing and the sweep ranges above — so those are the authoritative spec; the ±17 dB / fixed-center figures were likely a V1 or draft-manual carryover. Verify against the physical unit if it matters.

**Filter:**
- **HI-PASS** — a **2nd-order, 12 dB/octave** high-pass, cutoff sweepable **160 Hz–650 Hz**, with its own **on/off toggle** below the knob (per JHS official; an earlier draft said "60–800 Hz, 6 dB/oct" — corrected). Rolls off lows. This is your single most useful control in this rig — see §5.

**Mode toggle:**
- **HI / LO** — V2 addition. **LO** = higher clean headroom, better for clean preamp/DI work. **HI** = hotter circuit, easier to reach overdrive/distortion/fuzz.

**Side utility switches:**
- **INST / XLR** — selects input type. *Pedal passes no signal if set wrong.*
- **PAD** — 20 dB pad for the XLR input only; works pedal on or off; does nothing on the INST input.

## 3. Sonic Character: console sheen → crunch → broken console

Three zones along the gain arc:

- **Clean preamp (LO mode, low STEP, PRE-VOL down):** "hi-fi and pristine" with "subtle analog coloration" ([WaveInformer](https://waveinformer.com/2025/06/11/jhs-colour-box-v2/)). The classic Colour Box trick is that even "clean" isn't sterile — there's transformer weight and a forward, present midrange that makes a DI'd guitar sound *recorded* rather than plugged-in. This is the "console front end" tone.
- **Console crunch (HI mode, STEP 2–3, PRE-VOL noon):** edge-of-broken-console grit — gritty, mid-forward, with a saturating compression that sounds like an overloaded vintage channel. Not amp-like distortion; it's solid-state-into-transformer distortion, which is its own flavor.
- **Full distortion / "broken console" (HI, STEP 4–5, PRE-VOL up):** [Premier Guitar](https://www.premierguitar.com/gear/jhs-colour-box-review) called the V1's extreme "blistering solid-state fuzz" with "anarchic pumping/gulping effects." This is a genuinely ugly, splatty, gated fuzz — and in a doom/shoegaze context that ugliness is a feature.

The EQ is the real instrument here. Because every band sweeps and swings ±17 dB, you can do surgical *and* brutal moves: scoop a honking 1 kHz, lift 120 Hz into a wall, or — the demo party trick — set all three SHIFTs to a midrange frequency and boost all three for a "snarly, honking" telephone-radio voice ([WaveInformer](https://waveinformer.com/2025/06/11/jhs-colour-box-v2/)). For this rig the EQ matters most as a *pre-fuzz filter* (§5).

## 4. Dynamic Behavior / Gain Staging

The PRE-VOL ↔ MASTER relationship is the whole game. PRE-VOL determines distortion *and* level; MASTER trims level back. So:

- **Clean, loud:** STEP low, PRE-VOL low, MASTER high, LO mode. Maximum headroom, transformer color only.
- **Dirty, unity:** STEP high, PRE-VOL up, MASTER down, HI mode. Same output level, way more saturation.

STEP is a stepped (not continuous) control, so gain comes in audible jumps — handy for repeatability, less so for fine dialing; do the fine work with PRE-VOL. It responds to input level: hotter sources (the GK-5's medium-hot per-string output, a hot Jazz bass) hit the first stage harder and distort sooner, so you'll back PRE-VOL off vs. a passive single-coil. Guitar-volume cleanup is real but limited — this is a preamp, not a Fuzz Face; rolling back tames the grit but doesn't fully clean a high-STEP/HI setting. Plan to clean up with the controls, not the volume knob.

## 5. Signal-Chain Placement — why it sits before the fuzzes

Order: `VG-800 → Polytune → CB Clean → Colour Box V2 → MXR 108 → Hizumitas → Brothers AM → Longsword → Oxford → BF-3 → Somersault → CE-2W → Deco`. The Colour Box is the **tone-and-gain-shaping front end for the entire fuzz wall.** That's the right slot, and here's how to use it:

- **It's a buffered, low-impedance, EQ'd source feeding the 108.** A silicon Fuzz Face *can* misbehave behind a buffer (thinning), and CB Clean is already buffering upstream — so the 108 is seeing a hard-buffered signal regardless. The Colour Box's job is to make that buffered signal *worth* fuzzing: pre-EQ it, pre-saturate it, and tame the highs before the 108 turns them into ice-pick. If the 108 sounds thin or splatty, the fix is in the Colour Box's HI-PASS and TREBLE, not in moving pedals.
- **The HI-PASS is your most important pre-fuzz control.** Fuzz multiplies low-end mush. Roll the HI-PASS up to ~100–200 Hz *before* the 108/Hizumitas and the fuzz wall tightens dramatically — the chord reads instead of turning to mud. This is the single best reason it lives in front of the fuzzes. The Hizumitas's own Tone control can darken but can't high-pass; the Colour Box can.
- **The MID band steers what the fuzz emphasizes.** Boost 1 kHz before the 108 and the fuzz gets more aggressive, present, cutting. Scoop it for a darker, more "behind-the-wall" doom tone. You're choosing the fuzz's voice from in front of it.
- **STEP/PRE-VOL as a clean-ish boost into the fuzz:** even in LO with modest gain, the Colour Box's output is hot and forward, which slams the 108 harder for more sustain and a denser Hizumitas wall. Used this way it's a colored boost, not just an EQ.
- **Always-on logic:** because it's "on when able," the rest of Board 1 is voiced *through* it. Set the Colour Box's EQ as your baseline tone, then let the 108/Hizumitas/Longsword stack on top. When you bypass it, expect the whole front end to get brighter, looser, and less mid-forward — so its bypassed tone is the "raw" reference, the engaged tone is home base.

## 6. Source-Specific Use

The Colour Box is famously *better* on non-guitar sources than on guitar, which matters in a rig fed by banjo, baritone, bass, acoustic, violin, and a modeler.

- **EBM-5 banjo (via GK-5 → VG-800):** banjo is all 2–4 kHz attack and almost no low-mid body. The Colour Box is the right tool to fix that *before* the fuzz: pull TREBLE down (SHIFT toward ~6–10 kHz), boost BASS/low-MID to fake body, engage HI-PASS only lightly. This turns a piercing banjo into a usable fuzz source. Of everything on Board 1, this is the pedal that makes the banjo-into-fuzz idea work.
- **Baritone Jazzmaster:** home territory. Use the HI-PASS to keep the low B from flubbing the fuzz, modest mid lift for cut. Less corrective EQ needed than the banjo.
- **Acoustic (Taylor 814ce / Yamaha FG730S) & violin:** this is where it shines as a *sweetener/DI* rather than a fuzz feeder. LO mode, low STEP, gentle BASS lift + TREBLE air via the SHIFT, into the XLR out — instant "recorded through a console" acoustic. For violin, the transformer warmth tames the bowed top-end harshness; treat it as a print-stage DI, likely bypassing the fuzz section of the board entirely.
- **Bass (Fender Pro Jazz):** the Colour Box V2 is a [bass favorite](https://bassmusicianmagazine.com/2025/07/review-jhs-colour-box-v2-a-neve-preamp-in-a-pedal/) — saturation + EQ + DI in one box. Use it as an always-on bass DI into the Apollo: LO mode for clean tracking, or PRE-VOL up for grindy console-bass distortion. The XLR out (lower noise floor per the manual) straight to the interface needs no separate DI box.
- **VG-800 modeled output:** the Colour Box sees the VG-800's summed line-level output as just another signal and re-colors the modeled cab/amp. For clean modeled tones, run LO and use it as EQ only; for the aesthetic, push PRE-VOL and let it saturate an already-modeled amp into "recorded-wrong" territory. Note the VG-800 is line level — if you ever feed it in via the Effects Interface utility, watch input level / use the PAD logic accordingly.
- **Standalone DI/mic-pre into Apollo/RME:** with phantom power pass-through, the XLR input takes a real condenser (KM184, AT2020) and the XLR output goes straight to the Apollo x8 or Babyface — a Neve-flavored channel strip for tracking vocals, room mics, amp mics. This is a legitimate use, not a stretch; it's what the original Colour Box was reviewed *as* by [Tape Op](https://tapeop.com/reviews/gear/107/colour-box-preampeq-pedal).

## 7. Famous Users / Recording History

Careful here, because JHS's marketing does a subtle thing: when it says the sound "can be heard on dozens of recordings from [U2, Wilco, The National, Spoon, Collective Soul, Muse, The War on Drugs, Phantogram, Beck, Mac DeMarco, St. Vincent, Foo Fighters](https://jhspedals.info/products/colour-box-v2)," it's largely describing the *Neve-console direct-in technique* those artists used — the thing the pedal emulates — not always the pedal itself. Accurate framing: the Colour Box recreates a documented studio sound (Beatles "Revolution," Zeppelin "Black Dog," Motown, Steely Dan, Tom Petty, Nirvana all feature direct-into-Neve guitar) and has since been adopted by recording/touring artists who want that without a console. It is a well-established studio tool reviewed seriously by [Tape Op](https://tapeop.com/reviews/gear/107/colour-box-preampeq-pedal).

> **Update (2026-06) — verified pedal-namers found** (resolving this dossier's earlier open question): **Mac DeMarco** named the **Colour Box (V1)** in a 2019 Reverb interview — *"If you wanna get nasty, you get the Colour Box"* (Ground Guitar / Equipboard). And **Black Pumas run the V2 on camera** in Premier Guitar's Rig Rundown — both **Eric Burton** (guitar board) and bassist **Brendan Bond** (who uses it "as a simple overdrive"). So touring artists do visibly use the V2; the big "U2 / Wilco / The National / Spoon / Muse / War on Drugs / Phantogram" roster, by contrast, remains a description of the **Neve direct-in *technique*** the pedal emulates, not verified pedal owners — cite it as such.

## 8. Live / Power / I/O Notes

- **Power: 9V DC center-negative, and it draws 193 mA** ([manual](manuals/ColourBoxV2.pdf); corroborated by [Guitar Chalk](https://www.guitarchalk.com/jhs-colour-box-v2-preamp-power-requirements/)). **This is the gotcha.** 193 mA is enormous for a 9V pedal — most isolated supply outputs are 100 mA. You need a single isolated output rated **≥193 mA** (e.g. a high-current/500 mA port on a Strymon Zuma, CIOKS, or MXR Iso-Brick). Do not daisy-chain it, and do not assume a stock 100 mA slot will run it. **Do not exceed 9V.** (The V1 ran 18V; the V2 trades voltage for current — different supply requirement entirely if you're migrating.)
- **I/O:** combo XLR + 1/4" input (INST/XLR switch). Independent **1/4" and XLR outputs run in parallel** (same mono signal to two places — e.g. amp + FOH, or amp-track + DI-track). The **XLR output only passes when the pedal is ON**; the 1/4" passes effected signal when on and (in XLR input mode) clean-bypass when off. The XLR out has a slightly lower noise floor for line-in to an interface/mixer.
- **Phantom power** passes through (V2 only) for condensers.
- **Bypass:** V2 has upgraded silent switching.
- **Enclosure:** larger than V1 (~5.7 × 3.75 × 1.85 in per [JHS](https://jhspedals.info/products/colour-box-v2)); ten knobs — it eats real estate on Board 1.

## 9. Pairing Recommendations (this rig, by name)

**Into the fuzz wall (its main job):**
- **→ MXR 108 + Hizumitas:** use HI-PASS (~100–200 Hz) + a mid voice to pre-tighten and pre-shape. The Colour Box decides whether the fuzz wall is "tight and present" or "dark and oceanic." Treat its EQ as the fuzz tone control the 108 and Hizumitas don't have.
- **→ Brothers AM / Longsword / Oxford downstream:** the Colour Box already adds gain and color, so back these off — they're stacking on a hot, saturated, EQ'd source. Especially the Oxford (another JHS) will over-compound; use it as an intensifier, not added gain.

**As a console-print stage (the rig's "console-to-tape" philosophy):**
- The Colour Box is the *front* of the console; **PORTA424 → JHS 424** is the *tape* at the back. Conceptually they bookend the chain exactly like a real console-to-tape print: Neve-style preamp coloration in, Tascam/Porta tape saturation out, then **printed to the Apollo x8.** For a deliberate "recorded-wrong" print, push the Colour Box into console-crunch and let the 424/PORTA424 degrade the result.
- **As a DI into Apollo/RME:** XLR out → interface for bass, acoustic, violin, vocals. The lower-noise XLR out makes it a real channel strip, not a compromise.

**On the bench / studio:**
- Pull it off the board entirely to track vocals or a mic'd amp through its mic-pre — it's a Neve-flavored channel strip when you need one, and the JHS ecosystem (Oxford, Kilt, 424) already lives in this studio.

## 10. Reviews & Demos

- [Premier Guitar — JHS Colour Box (V1) review](https://www.premierguitar.com/gear/jhs-colour-box-review) — best on the original's character and the direct-into-Neve history.
- [Tape Op — Colour Box preamp/EQ review](https://tapeop.com/reviews/gear/107/colour-box-preampeq-pedal) — the studio/engineer's-eye take; treats it as real outboard.
- [WaveInformer — Colour Box V2 review](https://waveinformer.com/2025/06/11/jhs-colour-box-v2/) — most detailed V2 control walkthrough (clean→fuzz, Hi/Lo, Shift ranges, DI use).
- [Bass Musician Magazine — Colour Box V2 review](https://bassmusicianmagazine.com/2025/07/review-jhs-colour-box-v2-a-neve-preamp-in-a-pedal/) — best on bass DI/saturation use.
- [JHS Pedals — official Colour Box V2 page](https://jhspedals.info/products/colour-box-v2) — spec source and V1→V2 change list.
- [Guitar Chalk — Colour Box V2 power requirements](https://www.guitarchalk.com/jhs-colour-box-v2-preamp-power-requirements/) — confirms the 193 mA / 9V supply demand.
- [Jorb — "JHS Colourbox V2 // I want to use this with every instrument I own" (YouTube)](https://www.youtube.com/watch?v=GK-nmmcGOrQ) — multi-instrument demo. *(Verified via yt-dlp: channel is **Jorb**, NOT JHS — earlier draft mislabeled it.)*
- [The Bass Channel — "JHS 10th Anniversary Colourbox Bass Demo" (YouTube)](https://www.youtube.com/watch?v=fnkU8aMF2Tg) — bass-specific *(channel = **The Bass Channel**, not JHS — verified)*.

## 11. Mods / Quirks / Known Issues

- **The 193 mA current draw is the #1 real-world issue.** It will brown out or fail to power from an undersized isolated slot, and it cannot be daisy-chained sanely. This is the single most common Colour Box support question. Verified from the manual and corroborated externally.
- **Stereo myth:** people (and this rig's metadata) assume the dual outputs = stereo. They don't. Mono device, parallel mono outs. Fix the GearProfile.
- **Wrong-input silence:** if INST/XLR is set wrong, *no signal passes at all.* Easy to panic-debug; check the side switch first.
- **STEP is stepped:** no smooth gain sweep — gain jumps between five values. Repeatable, but you do fine drive on PRE-VOL.
- **XLR out is off when bypassed (in INST mode):** if you're feeding FOH off the XLR, killing the pedal kills the FOH feed. Plan around it for always-on use.
- **Loud volume jumps:** because PRE-VOL sets both gain and level, every gain change needs a MASTER trim or it'll jump in volume. Normal, but worth muscle-memory.
- No widely reported reliability failures; build is standard JHS.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Type | Studio-grade preamp / EQ / DI (Neve 1073-inspired) |
| Power | **9V DC center-negative ONLY** (do not exceed 9V) |
| Current draw | **193 mA** (high — needs a dedicated ≥193 mA isolated output) |
| Channels | **Mono** (mono in, parallel mono outs — *not* stereo) |
| Inputs | Combo XLR + 1/4" (INST/XLR select switch) |
| Outputs | Independent 1/4" + XLR, run in parallel (same signal) |
| Phantom power | 48V pass-through (V2 addition) |
| Pad | 20 dB, XLR input only, works on/off |
| Gain (STEP) | 5 steps: +18 / +23 / +28 / +33 / +39 dB |
| Gain mode | HI / LO toggle (V2 addition) |
| EQ | 3-band Baxandall-type; **Treble ±15 dB, Mid ±10 dB, Bass ±15 dB** + sweepable Shift (JHS official) |
| EQ shift ranges | Treble 2 k–30 kHz · Mid 150 Hz–2.4 kHz · Bass 20 Hz–440 Hz (JHS official) |
| High-pass | **160 Hz–650 Hz, 2nd-order 12 dB/oct**, on/off toggle (JHS official) |
| Transformer | Lundahl (V1); V2 adds an output transformer |
| Bypass | Silent switching (V2) |
| Dimensions | ~5.7 × 3.75 × 1.85 in |
| Edition | 10th-anniversary (deep navy chassis) |

Sources: [JHS Colour Box V2 manual](manuals/ColourBoxV2.pdf), [JHS product page](https://jhspedals.info/products/colour-box-v2), [Guitar Chalk power note](https://www.guitarchalk.com/jhs-colour-box-v2-preamp-power-requirements/).

## 13. Starting-Point Settings

Clock-face positions, viewed from above. STEP given as position 1–5; HI/LO and HI-PASS as stated.

**(a) Clean Neve color** — always-on tone-shaping, transparent-ish
- Mode: **LO** · STEP **1** · PRE-VOL **9** · MASTER **1–2 o'clock** (set unity)
- EQ: TREBLE +slight (SHIFT ~8 kHz), MID flat, BASS +slight (SHIFT ~120 Hz) · HI-PASS **off** or ~60 Hz
- Use: baseline rig voice. Adds weight and presence without obvious distortion.

**(b) Console-crunch into the fuzz wall** — pre-shape for the 108/Hizumitas
- Mode: **HI** · STEP **2–3** · PRE-VOL **12** · MASTER to taste
- EQ: MID **+** at 1 kHz (cut/presence), TREBLE **−** (tame for the fuzz), BASS modest · **HI-PASS ON ~120–200 Hz**
- Use: tightens and voices everything the 108 + Hizumitas chew on. The key always-on setting in this rig.

**(c) DI / console print** — bass, DI guitar, or print stage into Apollo
- Input: INST (or XLR for mic) · Mode: **LO** · STEP **1** · PRE-VOL **8–10** · MASTER unity
- EQ: gentle BASS lift + TREBLE air · HI-PASS **off** · XLR out → Apollo/RME (use PAD if XLR clips)
- Use: clean console-flavored DI; push PRE-VOL for grindy console-bass. Pairs with PORTA424/JHS 424 → tape print.

**(d) Acoustic / violin sweetener** — DI, no fuzz
- Input: INST or XLR · Mode: **LO** · STEP **1** · PRE-VOL low · MASTER unity
- EQ: BASS +slight, MID flat-to-cut (de-honk), TREBLE +air (SHIFT high) · HI-PASS ~80–100 Hz to clean rumble
- Use: "recorded through a console" acoustic/violin straight to the interface. Likely bypass the fuzz section.

## 14. Versus Alternatives — why it earns the always-on slot

- **Original Colour Box (V1):** same DNA, but 18V, fixed EQ (no Shift), no phantom power, no Hi/Lo, no silent switching, smaller. If you already own a V1 the V2's case is the sweepable EQ + phantom + headroom switch — meaningful upgrades for a do-everything front end. The V1 is the cheaper used route if you only need the core preamp/fuzz.
- **JHS Colour Box "10" / branding:** the unit here is the V2 sold as the 10th-anniversary edition — same circuit, anniversary cosmetics.
- **Other Neve-style preamp pedals** — e.g. dedicated DI/console boxes from other makers — generally give you the transformer color but *not* the sweepable three-band EQ, the broad high-pass, and the full clean→fuzz gain range in one box. The Colour Box's edge for *this* rig is precisely that combination: it's a fuzz-shaping EQ *and* a DI *and* a saturating preamp.
- **Why it earns "always-on when able" here:** nothing else on Board 1 can high-pass and parametrically pre-EQ the signal *before* the fuzzes, and nothing else doubles as a Neve-flavored DI/print stage that conceptually completes the rig's console-to-tape arc (Colour Box front end → PORTA424/JHS 424 tape → Apollo print). The 193 mA appetite is the price of admission; budget the power and it stays on.

## Sources

- [JHS Pedals — Colour Box V2 product page](https://jhspedals.info/products/colour-box-v2)
- [JHS Colour Box V2 manual (local)](manuals/ColourBoxV2.pdf)
- [Premier Guitar — JHS Colour Box (V1) review](https://www.premierguitar.com/gear/jhs-colour-box-review)
- [Tape Op — Colour Box preamp/EQ review](https://tapeop.com/reviews/gear/107/colour-box-preampeq-pedal)
- [WaveInformer — JHS Colour Box V2 review](https://waveinformer.com/2025/06/11/jhs-colour-box-v2/)
- [Bass Musician Magazine — JHS Colour Box V2 review](https://bassmusicianmagazine.com/2025/07/review-jhs-colour-box-v2-a-neve-preamp-in-a-pedal/)
- [Guitar Chalk — Colour Box V2 power requirements](https://www.guitarchalk.com/jhs-colour-box-v2-preamp-power-requirements/)
- [JHS Colourbox V2 multi-instrument demo (YouTube)](https://www.youtube.com/watch?v=GK-nmmcGOrQ)
- [JHS 10th-Anniversary Colourbox bass demo (YouTube)](https://www.youtube.com/watch?v=fnkU8aMF2Tg)
