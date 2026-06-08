# Chase Bliss Generation Loss MKII — Deep Research

A working dossier for the **first pedal on Board 3 (End / Time → Tape)** of a stereo banjo/baritone rig. The stereo signal arrives here straight from Board 2's OBNE Dark Star V3 smear, and the Generation Loss is the gate everything passes through before the delays, looper, and reverb get their turn. The whole End Board's job is "Delay · Loop · Reverb · Print" *through tape*, so this pedal is the marquee degradation engine that stamps the VHS/cassette character onto the signal up front — and it does so in a rig that already carries three or four other tape voices, which is most of what this document is about: where each tape voice belongs and why this one earns the opener slot.

> **Profile correction.** The on-disk `GearProfile.md` is stale: it says "Board 2" and "*(add to manuals/)*". The current `rig-design.html` map puts Generation Loss **first on Board 3**, and a manual **is** on disk (`manuals/Generation+Loss+MKII_Manual_Pedal_Chase+Bliss.pdf`, CBA ref 2022-GEN02). This dossier treats that manual as authoritative.

## 1. Lineage: Cooper FX VHS Simulator → CB × Cooper FX → MKII

The Generation Loss began as a one-man pedal: **Tom Majeski's Cooper FX** of Fort Collins, Colorado (founded 2015, named after his dog), whose very first product was the original **Generation Loss VHS Simulator** — random pitch fluctuations, bandwidth-cutting filters, sample-rate reduction, and noise, all bundled to fake a broken VHS deck without owning one ([Guitar.com on Cooper FX](https://guitar.com/news/gear-news/cooper-fx-announces-it-will-no-longer-be-making-pedals-after-some-seven-years-in-operation/)). Chase Bliss and Cooper FX first collaborated on a limited reissue around 2019, then Majeski released a **Generation Loss V2** (separate Wet/Dry knobs, presets, an extra footswitch for Tape Stop / Garbled / Freeze, limited to 500 units) before **shutting Cooper FX down in 2021 to join the Chase Bliss design team full-time** ([Guitar Pedal X on the V2](https://www.guitarpedalx.com/news/news/tom-majeski-expands-and-refines-his-cooper-fx-generation-loss-with-the-launch-of-the-immediately-sold-out-v2-edition), [Guitar World on the CB/Cooper FX partnership](https://www.guitarworld.com/news/chase-bliss-audio-cooper-fx)).

The **MKII (2022)** is not a port of the old circuit — per Chase Bliss they "decided to start from scratch this time and really explore what tape is all about" ([Chase Bliss product page](https://www.chasebliss.com/generation-loss-mkii)). The manual frames it as two pedals in one box (manual pg. 2–3): a **Classic mode** that resurrects the original Cooper FX/CB Generation Loss voice as "a work of fiction, based on nothing in particular" (manual pg. 34–35), and the new **MKII mode** built "through study and analysis" — a library of *real* tape machines EQ-profiled from frequency analysis of physical hardware. The marketing one-liner is "a VCR deconstructed": it takes each oddity a tape machine imparts — wow, flutter, saturation, dropouts, hiss, EQ color — and gives you an independent knob for each (manual pg. 2–3). The headline MKII additions over the originals: **stereo** (Chase Bliss's first stereo pedal in the classic format), the 12-model tape library, the customizable **Failure** knob, and full MIDI/CV/expression with presets and internal modulation (manual pg. 42; [Chase Bliss page](https://www.chasebliss.com/generation-loss-mkii)).

## 2. Controls & Dip Switches (from the manual)

**Knobs (manual pg. 6–9):**

- **A — Wow.** Depth of slow, smooth, *random* pitch modulation — classic tape vibrato that's "random and rubbery." Around 10 o'clock is the nuanced sweet spot; higher evokes struggling machinery and melted tape (manual pg. 16). *(Classic mode: this knob is **LP**, a resonant low-pass cutoff — roll CCW to remove highs.)*
- **B — Volume.** Wet output level. **Noon is unity, max is +2x boost.** If ramping is engaged, this knob's *value* is remembered but it instead sets ramp **speed** (manual pg. 7, 41).
- **C — Model.** Steps through the 12-model tape library (see §3). *(Classic mode: this knob is **GEN** — sets sample rate; CCW to degrade and introduce digital aliasing.)*
- **D — Flutter.** Fast, twitchy random modulation affecting **both amplitude and pitch** — quivering/trembling tape. Best partnered with Wow for a convincing tape effect; a tiny bit of Flutter alone is "a secret ingredient" when using Gen Loss as an overdrive/EQ/chorus (manual pg. 8, 18–19).
- **E — Saturate.** A modeled **magnetic hysteresis loop** — the tape's magnetic structure shifting and distorting future signal. Subtle through most of the sweep, gnarly/mis-biased at the extreme. **Saturate and Model are interactive** — each tape model exaggerates and suppresses different parts of the distortion (manual pg. 24, 26–27).
- **F — Failure.** A multi-effect of small tape malfunctions: **drops** (playhead losing contact → brief silences), **snags** (abrupt pitch spikes from tape sticking), and **crinkles & pops** (shaky, crumbling micro-disturbances). Also the **key to stereo processing** (manual pg. 9, 28–31). *(Classic mode: this knob is **HP**, a resonant high-pass — CW to remove lows.)*

**Toggles (manual pg. 10–11):**

- **Aux** — selects which performance effect the left footswitch fires (Stop / Filter / Fail; plus a hidden Freeze). Onset speed is set in the hidden menu.
- **Dry** — **None** (pure tape machine) / **Small** (a touch of clean preserved, keeps tape dominant but bigger) / **Unity** (clean matches input level — needed for chorusing and "sun-soaked" modulation; flick to Unity to expand Wow chorus, manual pg. 17).
- **Noise** — introduces hiss + mechanical noise; the level of each source is set independently in hidden options.
- **Presets** — center is live/current; left and right footswitch positions store one preset each (hold-to-save; **2 presets** at the pedal).

**Dip switches — top row "Customize" (manual pg. 36–37):** **MISO** (Mono In → Stereo Out), **SPREAD** (unique L/R stereo processing — a *malfunctioning* stereo image in MKII, a smooth WOW-driven pan in Classic), **DRY TYPE** (applies all effects except Wow/Flutter to the dry signal → saturated/malfunctioning chorus), **DROP BYP** (removes drops from Failure), **SNAG BYP** (removes snags from Failure), **HUM BYP** (removes mechanical noise from the Noise toggle). Plus a **CLASSIC** dip and the **ramping/bounce/sweep/polarity/random** dips (manual pg. 38–39).

**Hidden options** (hold both footswitches; manual pg. 14–15): **Aux Onset** (Wow knob), **Hiss Level** (Flutter knob), **Mechanical Noise Level** (Saturate knob — noon = 0, CW = hum, CCW = VCR noise), **Crinkle/Pop Level** (Failure knob), **Bypass Type** (Model knob — CW past noon = clickless **DSP bypass**, CCW = true bypass), **Input Gain** (Dry toggle — Line / Instrument / High-Gain; matches saturation to source but louder inputs can introduce digital aliasing).

## 3. The 12 Tape Models & Sonic Character (manual pg. 20–23)

The **Model** knob is the pedal's EQ-color library, each profile frequency-analyzed from real hardware. **Position 0 = OFF** (full CCW) = unfiltered/bypass the model. The rest:

| # | Model | Type | Character |
|---|---|---|---|
| 1 | CPR-3300 Gen 1 | VHS | An old VCR in rough shape |
| 2 | CPR-3300 Gen 2 | VHS | A copy of #1 (copy of a copy) |
| 3 | CPR-3300 Gen 3 | VHS | A copy of #2 (copy of a copy of a copy) — the literal "generation loss" |
| 4 | Portamax-RT | Cassette | Desktop all-in-one 4-track |
| 5 | Portamax-HT | Cassette | The same, played back at **half-speed** |
| 6 | CAM-8 | Cassette | Camcorder, sampled via built-in mic |
| 7 | Dictatron-EX | Cassette | Handheld voice recorder, built-in speaker + external mic |
| 8 | Dictatron-IN | Cassette | Handheld voice recorder, built-in speaker + internal mic |
| 9 | Fishy 60 | Toy | Toy recorder, built-in speaker + internal mic |
| 10 | MS-Walker | Cassette | Portable personal music player (designed by BlankFor.ms) |
| 11 | AMU-2 | NA | Imaginary model — deteriorated tape + barely functioning recorder (designed by AMULETS) |
| 12 | M-PEX | ¼″ Reel | Reel-to-reel on old, brittle tape (designed by Marcus Fischer) |

Sonically the pedal spans **subtle tape age → full VHS destruction**. At low settings (Wow ~10, Flutter just below audible, light Saturate) it's a wistful, "recorded a while ago" patina — the manual's own first demo setting is described as "nice and wistful" (manual pg. 4). Push Wow/Flutter and it becomes seasick, melted, struggling-machine warble. Crank Failure and you get genuine dropouts and pitch snags — the signal *stutters and skips* like a worn cassette. Reviewers confirm the breadth: beyond VHS it makes "strangely scuzzy variants on chorus, phasing, sample-and-hold filtering," and the controls interact in ways that are "quite discombobulating" ([Guitar.com review, 8/10](https://guitar.com/reviews/effects-pedal/chase-bliss-generation-loss-mkii-review/)). The standing joke — noted by basically every reviewer — is that "a gleamingly digital pedal should be so good at making things sound raggedly analogue."

## 4. Behavioral Notes

- **Drops & snags are non-periodic.** Failure malfunctions fire randomly, so no two passes are identical — great for the "broken/recorded-wrong" aesthetic, less great if you need a repeatable part. Bypass drops/snags via dip switches when you want only the gentle crinkle texture.
- **Stereo lives inside Failure.** SPREAD reads the Failure knob to build a moving, malfunctioning stereo image; drops are the most pronounced (most stereo movement), so bypass drops for subtler stereo deviation (manual pg. 30–31). A creative trick: turn on **SNAG BYP + SPREAD + MISO** and turn the other knobs down and the signal "skitters randomly left to right but otherwise sounds clean" — an unpredictable auto-panner/stereo-splitter (manual pg. 31).
- **It's a chorus/EQ in disguise.** Dry → **Unity** + Wow makes a tape chorus; a hair of Flutter under any clean tone is "vintage but not broken" (manual pg. 17, 19). Saturate-only with everything else off = a tape overdrive (manual pg. 27).
- **Hiss is aggressive.** Reviewers warn the background hiss gets "extremely annoying after not very long" — leave Noise off (or hiss low in hidden options) unless you specifically want it ([Guitar.com](https://guitar.com/reviews/effects-pedal/chase-bliss-generation-loss-mkii-review/)). The pitch-warp side "can get nauseating," so restraint helps.
- **Self-modulation / ramping.** Knobs can **bounce** (continuous triangle or random LFO) or **ramp** (one-time move on engage) without external gear (manual pg. 38–41) — e.g. bounce the **Model** knob with **RANDOM** for a "Tape Hopper" that jumps between machines, or bounce **Failure** for an ever-changing "Maintenance Phase" of malfunction.
- **DSP latency (measured).** It's a digital pedal; community measurement puts it at **≈25 ms wet / ≈9 ms dry (~16 ms skew)**, so the internal Dry blend is **not phase-coherent on percussive/transient material** (kick "flaming"). Fine for synths/ambient/sustained guitar; for tight parallel work use a DAW insert + latency comp, or flash the optional **low-latency firmware (1.1.0)** which halves it (trade: stereo goes chorus-y → flange-y). ([latency measurement](https://www.youtube.com/watch?v=7HuHyHSX8d8); see the UsageGuide.)

## 5. Signal-Chain Placement — Board 3 Opener, and the Tape-Voice Labor Division

Board 3 receives **stereo** from Board 2 (Dark Star V3 out), and Generation Loss is first. That position is deliberate and correct for three reasons:

1. **It sets tape character *before* the time effects, not after.** Real generation loss happens at the *source* of a recording, so degrading first means the Big Time delays, MOOD MkII micro-loops, Blooper layers, and H90 reverbs all chew on already-tape-warped material — the repeats and reverb tails inherit the wow/flutter and dropout instead of being cleanly added on top. This is the "print, then delay" logic of analog tape rigs.
2. **It's the rig's only *true-stereo, MISO-capable* degrader at the head of the End Board.** With MISO it can take a mono feed and fan it into a malfunctioning stereo image — but here the feed is already stereo, so it runs stereo-in/stereo-out and the SPREAD failure-panning becomes a width tool the downstream stereo pedals preserve.
3. **It MIDI-syncs and preset-recalls with the four Chase Bliss pedals right behind it** (Big Time, MOOD MkII, Blooper, plus the others on Boards 1–2), so a single scene can recall a Gen Loss tape character alongside delay/loop states.

**The multi-tape-voice division of labor (the central question in this rig):**

- **Strymon Deco V2 (Board 1, before stereo split)** = *warm analog tape saturation + doubletracker* at the **front** of the chain, on the dry instrument. It's gentle, musical, "tube tape" coloration applied to the raw guitar/banjo before any texture. Think: subtle thickening, not destruction. It is **not** a wow/flutter/dropout pedal — Generation Loss does what Deco can't.
- **CB Generation Loss (Board 3 opener)** = the **deliberate degradation engine**: VHS/cassette EQ color, wow/flutter wobble, dropouts, snags, hiss. This is the *character-defining* tape voice and the only one with dropout/failure modeling. It belongs first on the End Board so the time/space effects degrade with it.
- **Hologram Chroma Console (Board 3, mid)** = a *multi-character* color box (it has its own tape/filter/drive/modulation "characters"). Overlaps with Gen Loss on tape coloration, but Chroma is better used downstream as a *texture-morphing* layer over the delays/loops rather than the primary degrader. Avoid stacking both on heavy tape settings or you double the wow and it turns to mush — pick one as the "tape" and let the other do something else (filter, lo-fi reverb-ish smear).
- **MXNHLT PORTA424 + JHS 424 (end of Board 3)** = the **final Tascam-Porta tape *print*** — channel-strip saturation/EQ (PORTA424, a Tascam Porta MK1 recreation) into the 424 Drive ("always on") as the last word before Apollo/FOH. This is the "summing to a 4-track cassette" stage: it glues the *entire* stereo bus, including all the upstream tape voices, into one cohesive lo-fi bounce. It is mastering-bus tape, not effect tape.

So the chain reads, front to back: **Deco = warm the source → Generation Loss = break the source → Chroma = morph the textures → PORTA424/424 = print the whole thing to cassette.** Four tape voices, four distinct jobs, almost no wasted overlap — provided you don't run Gen Loss *and* Chroma both as heavy tape at once.

**One more overlap to manage: the owner's CB Lost & Found (Board 2) has a "Gen Lite" mode** — a mini Generation Loss baked into that pedal. It's a convenience voice for adding a little VHS wobble *earlier* in the chain (mid-board, pre-delay) when you don't want to commit the full Gen Loss. Treat Gen Lite as a "sketch" and the real Gen Loss as the "render": if you're already running Gen Loss on Board 3, leave Lost & Found's Gen Lite off (or very subtle) to avoid two wow engines fighting. Gen Lite is most useful as a quick texture when Gen Loss is dialed for something specific you don't want to disturb.

## 6. Source-Specific Notes (banjo, baritone, modeled VG-800, bass)

- **GK-5 banjo (EBM-5) via VG-800.** Banjo is bright, percussive, fast-decay. Generation Loss is a *gift* here: the low-/mid-focused tape models (4–8, the Portamax/Dictatron cassette voices) roll off the banjo's piercing top and the wow/flutter smears its staccato attack into something that *sustains* and *blurs* — exactly the "banjo-as-lead, recorded-wrong" texture the rig is built around. Start with Model 4–5, Wow ~10–11, light Flutter, Failure low. The half-speed **Portamax-HT (5)** is especially evocative for slow drone banjo.
- **Baritone Jazzmaster.** Lots of low-end mass; watch Saturate (the model interaction can get flubby on bass-heavy material). The VHS models (1–3) keep more lows and suit baritone drones; reel-to-reel **M-PEX (12)** gives the cleanest, biggest "tape" without much color when you want size over destruction.
- **Modeled VG-800 signal.** Since Gen Loss EQ-colors and degrades *after* the VG-800's modeled amp/cab, it's perfect for de-perfecting digital modeling — fuzz the IR's sterility into a worn cassette of an amp. Pad/synth COSM patches turn into convincing "found-tape" drones. Mind the **Input Gain** hidden option (Line/Instrument/High-Gain): the VG-800 outputs near line level, so set input gain accordingly or you'll get extra digital aliasing on loud signals (manual pg. 15).
- **Bass (Jazz bass).** Use sparingly. Keep Dry on **Small** or **Unity** to preserve low-end fundamental, lean on VHS models for low retention, keep Saturate modest. Failure dropouts on bass can sound like a dying cable — sometimes the point, usually not.

## 7. Famous Users (honest)

Newer pedal, but real credits exist. **St. Vincent (Annie Clark)** has cited using the Generation Loss MKII in the studio on *All Born Screaming*. **Mike Stringer (Spiritbox)** shows it on his board in a Premier Guitar Rig Rundown. **Josh Carter (Phantogram)** told Chase Bliss they "messed a lot with the Generation Loss." Danish jazz guitarist **Jakob Bro** has run it on his Pedaltrain ([usage roundup via Equipboard](https://equipboard.com/items/chase-bliss-audio-generation-loss-mkii)). Lineage-wise, the original Cooper FX Generation Loss developed a cult following on ambient/shoegaze/lo-fi boards well before the MKII; the **collaborators on the MKII models themselves** — BlankFor.ms, AMULETS, Marcus Fischer — are respected ambient/experimental artists, which tells you the target audience. *Unverified:* specific touring deployments beyond the above are hard to confirm; treat any "X uses it live" claim skeptically unless it's in a Rig Rundown.

## 8. Live / Power / I/O

| Item | Detail |
|---|---|
| Power | 9V DC center-negative, **~250 mA** (manual pg. 1; [CB page](https://www.chasebliss.com/generation-loss-mkii)) — a heavy draw; needs a high-current isolated slot |
| I/O | True stereo in / stereo out; mono-in→stereo-out via **MISO** dip |
| MIDI | Yes — via Chase Bliss **Midibox** (TRS jack converts MIDI; PC for presets, CC for deep control of knobs/dips/hidden options) (manual pg. 42–43) |
| CV / Expression | EXP/CV jack — TRS for expression, floating-ring TRS→TS for CV (0–5V; **negative voltage can damage it**); controls any chosen knob(s), defaults to Volume (manual pg. 42–43) |
| Aux jack | The MIDI jack doubles as an **external footswitch** input for the Aux effect (any normally-open momentary) (manual pg. 43) |
| Presets | 2 at the pedal (L/R footswitch slots); more via MIDI |
| Bypass | Default **true bypass with analog dry thru**; switchable to clickless **DSP bypass** (digital thru) via hidden option; per-channel behavior varies with MISO/DSP state (manual pg. 13, 44–45) |
| Latency | Digital — **measured ≈25 ms wet / ≈9 ms dry (~16 ms skew)**; dry blend not phase-coherent on transients; optional low-latency firmware (1.1.0) halves it |
| Dimensions/weight | Standard Chase Bliss enclosure (*manual does not state exact dims — unverified here*) |

**Live cautions:** the **250 mA draw** is the big one — do not share a 100 mA daisy-chain slot; give it a dedicated high-current isolated output. With **DSP bypass** off it's true bypass, so on total power loss you still pass dry signal on the analog thru (good fail-safe) — but if you've set DSP bypass for clickless switching, power loss kills the signal. Decide which you want for the gig.

## 9. Pairing Recommendations (by name)

- **→ CB Big Time (next in chain):** degrade first, delay second. The wow/flutter rides *into* the repeats; for long ambient delays this is the canonical move. Sync via MIDI so a scene recalls both.
- **→ CB MOOD MkII:** micro-looped/mangled slices of already-tape-warped audio = deeply broken granular tape. MOOD's loop layer will capture Gen Loss dropouts as part of the texture.
- **→ CB Blooper:** capture a Gen Loss drone (with Failure bouncing for evolving malfunction) and stack modulated layers — the stated rig aesthetic. Gen Loss is the ideal *source* for Blooper loops.
- **→ Hologram Chroma Console:** powerful but redundant if both run heavy tape. Best split: Gen Loss = tape EQ + wow/dropout; Chroma = a *different* character (filter sweep, lo-fi space, drive) layered over the time effects. Don't double the wow.
- **→ Eventide H90:** Gen Loss's degraded, dropout-laden signal gives H90 reverbs/pitch algorithms gnarly material to spectrally process — CrushedHall / MangledVerb / Blackhole over a worn-cassette source is a textbook doom-ambient recipe.
- **vs Strymon Deco V2 (upstream):** complementary, not redundant — Deco warms the *clean source* at the front; Gen Loss *breaks* it at the End Board. Run both.
- **vs PORTA424 + JHS 424 (downstream print):** complementary — those are the final cassette **bounce** of the whole bus; Gen Loss is a mid-chain *effect*. If the mix gets too lo-fi, pull Gen Loss's Model toward OFF/0 and Saturate down rather than touching the print stage.
- **vs CB Lost & Found "Gen Lite" (Board 2):** redundant by design — Gen Lite is a pocket Gen Loss for early wobble. With the real Gen Loss active on Board 3, keep Gen Lite off or barely-there.
- **MIDI scene recall:** with the owner's stack of MIDI Chase Bliss pedals (Clean, Brothers AM, Big Time, MOOD MkII, Blooper) plus Microcosm/Chroma/H90, a single program-change scene can recall a Gen Loss tape preset alongside delay/loop/reverb states. Map presets so each "song scene" sets the tape character first.

## 10. Reviews & Demos

- [Guitar.com — Generation Loss MkII review (8/10)](https://guitar.com/reviews/effects-pedal/chase-bliss-generation-loss-mkii-review/) — best written review; honest about hiss and pitch-warp fatigue.
- [AudioNewsRoom — "Beauty in Imperfection" review](https://audionewsroom.net/2024/03/beauty-in-imperfection-chase-bliss-generation-loss-mkii-review.html) — workflow-focused.
- [Chase Bliss — official product page](https://www.chasebliss.com/generation-loss-mkii) — specs, demos, sound clips.
- [Martin Yam Møller — demo of all 12 tape models](https://martinyammoller.com/youtube/chase-blisse-generation-loss-mkii-demo-of-the-12-tape-models/) — the single most useful video for hearing the Model knob A/B'd.
- [Chase Bliss Generation Loss MKII Sound Demo (no talking) — via MATRIXSYNTH](https://www.matrixsynth.com/2024/03/chase-bliss-generation-loss-mkii-sound.html) — dry sound demo.
- [Delicious Audio — Generation Loss MkII overview](https://delicious-audio.com/chase-bliss-audio-generation-loss-mkii/) — concise feature rundown.
- [Effects Database — model entry](https://www.effectsdatabase.com/model/chasebliss/generationloss) — spec/version cross-reference.

## 11. Mods / Quirks / Firmware

- **No user mods** — it's a digital DSP pedal; "modding" = the dip switches, hidden options, and firmware. Behavior is changed in software, not soldering.
- **Firmware updates** ship from Chase Bliss over USB/MIDI historically; check [chasebliss.com](https://www.chasebliss.com/generation-loss-mkii) for the current version. *(Specific firmware changelog unverified here.)*
- **Quirks:** hiss is louder than people expect (leave Noise off by default); Failure's randomness makes parts non-repeatable; Saturate + bassy sources can flub; the SPREAD stereo image is *intentionally* unstable (it's failure-driven), which can read as "broken" on a clean signal — that's the design.
- **Manual vs web flag:** the manual labels current draw "~250 mA" (pg. 1) and the CB page agrees; some third-party listings round differently — trust the manual/CB figure. Lineage dates vary slightly across outlets (2019 CB/Cooper FX collab vs 2021 V2 vs 2022 MKII) — the MKII itself is **2022** (manual ref CBA 2022-GEN02).

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Type | Stereo digital tape/VHS degradation (wow, flutter, saturate, failure, EQ models) |
| Power | 9V DC center-negative, ~250 mA |
| Max voltage | 9V (standard Chase Bliss; do not exceed) |
| I/O | Stereo in / stereo out; MISO mono-in→stereo-out |
| Signal path | Digital DSP; analog dry-thru available |
| Bypass | True bypass w/ analog dry thru (default) or clickless DSP bypass |
| Presets | 2 at pedal (more via MIDI) |
| MIDI | Yes, via Chase Bliss Midibox (TRS; PC + CC) |
| CV / Expression | Yes (0–5V CV, TRS exp); Aux footswitch input on MIDI jack |
| Controls | Wow, Volume, Model, Flutter, Saturate, Failure + Aux/Dry/Noise/Presets toggles + dip switches |
| Tape models | 12 (VHS / cassette / dictaphone / toy / reel-to-reel) + OFF |
| Modes | MKII (study-based) + Classic (original Gen Loss recreation) |
| Self-modulation | Ramp + Bounce (triangle/random) on any knob, no external gear |
| Format | Chase Bliss "classic" enclosure (first stereo CB in this format) |

Source: manual (CBA 2022-GEN02) + [Chase Bliss product page](https://www.chasebliss.com/generation-loss-mkii). Input/output impedance and exact dimensions are **not published** — unverified.

## 13. Starting-Point Settings

Clock-face positions, viewing the pedal from above.

**(a) Subtle tape age** — wistful, "recorded a while ago," nearly always-on
- Wow 10 · Flutter just below audible · Saturate 9 · Failure 8 · Model 4 (Portamax-RT) · Dry: Small · Noise: off
- The manual's "nice and wistful" home base (pg. 4). Use as the default tape patina under banjo/baritone.

**(b) Seasick wow/flutter** — drunken, melted-tape drone
- Wow 1–2 o'clock · Flutter 12 · Saturate 11 · Failure 9 · Model 5 (Portamax-HT, half-speed) · Dry: None
- Pair into Big Time long delay + H90 hall. Let chords ring; the warble does the rest.

**(c) VHS dropout chaos** — broken, skipping, glitched
- Wow 11 · Flutter 1 o'clock · Saturate 1 o'clock · Failure 2–3 o'clock · Model 1–3 (CPR-3300 VHS) · SPREAD on · Dry: None
- Failure drops/snags fire and pan in stereo. Aux footswitch on **Stop** for tape-halt punctuation. Genuinely unpredictable — record it.

**(d) Filtered lo-fi bed** — dark, narrow, "small speaker" texture under everything
- Wow 9 · Flutter 8 · Saturate 10 · Failure low · Model 7–8 (Dictatron) or 9 (Fishy 60 toy) · Dry: Small
- The cassette/dictaphone models roll off highs and lows for a band-limited mid-forward wash. Great pad/ambient bed; lets the H90 reverb shine on top.

## 14. Versus Alternatives — Why It Earns the Board-3 Opener Slot

- **Strymon Deco V2** — warm tape *saturation + doubletracker*, all-analog, musical. No wow/flutter/dropout, no models, no stereo failure imaging. It belongs at the *front* warming the source; it cannot do what Gen Loss does at the End Board. Complementary, already in the rig.
- **Hologram Chroma Console** — multi-character color/texture box with a tape voice among others. More of a *Swiss-army texture morpher*; less specialized as a pure degrader, and stacking its tape with Gen Loss's doubles the wow. Better used downstream on the time effects. Also in the rig — division of labor handles the overlap.
- **MXNHLT PORTA424 / JHS 424** — Tascam-Porta channel-strip *print*. That's a mastering-bus cassette bounce of the whole stereo signal at the chain's end, not a mid-chain effect with dropouts and a 12-model library. Different job entirely; both already terminate Board 3.
- **CB Lost & Found "Gen Lite"** — a pocket Gen Loss for early-chain wobble. Convenient, but no full model library, no independent Failure, no true-stereo failure imaging, no presets dedicated to tape. Use it as a sketch when Gen Loss is committed elsewhere.
- **Chase Bliss MOOD / generic lo-fi pedals (Hungry Robot, Zvex Instant Lo-Fi, etc.)** — fun, but none combine *real-hardware-modeled EQ profiles + independent wow/flutter/saturate/failure + true stereo + full MIDI/preset recall* the way Gen Loss does.

In this rig — drone/doom/shoegaze, banjo-as-lead, a stereo End Board themed "Delay · Loop · Reverb · Print" — Generation Loss earns the **Board-3 opener** slot for three reasons no other pedal here covers at once: (1) it's the only **dropout/failure-modeling** degrader, so the time/space effects can chew on genuinely *broken* audio; (2) it's a **true-stereo, MISO-capable** width tool whose SPREAD imaging the downstream stereo pedals preserve; and (3) it's a **MIDI/preset** citizen that scene-recalls in lockstep with the four Chase Bliss pedals right behind it. Deco warms the source, Gen Loss breaks it, Chroma morphs the textures, and PORTA424/424 print the whole thing to cassette — four tape voices, four jobs, and Gen Loss owns the one that matters most: deciding *how broken* the recording is before anyone gets to play with the echoes.

## Sources

- Manual: `Generation+Loss+MKII_Manual_Pedal_Chase+Bliss.pdf` (CBA ref 2022-GEN02) — on disk, authoritative.
- [Chase Bliss — Generation Loss MKII product page](https://www.chasebliss.com/generation-loss-mkii)
- [Guitar.com — Generation Loss MkII review (8/10)](https://guitar.com/reviews/effects-pedal/chase-bliss-generation-loss-mkii-review/)
- [Guitar.com — Cooper FX / Chase Bliss Generation Loss MKII VHS Duplicator news](https://guitar.com/news/gear-news/chase-bliss-cooper-fx-generation-loss-mkii-vhs-duplicator-tone-degradation/)
- [Guitar.com — Cooper FX winds down after seven years](https://guitar.com/news/gear-news/cooper-fx-announces-it-will-no-longer-be-making-pedals-after-some-seven-years-in-operation/)
- [Guitar Pedal X — Cooper FX Generation Loss V2 launch](https://www.guitarpedalx.com/news/news/tom-majeski-expands-and-refines-his-cooper-fx-generation-loss-with-the-launch-of-the-immediately-sold-out-v2-edition)
- [Guitar World — Chase Bliss Audio joins forces with Cooper FX](https://www.guitarworld.com/news/chase-bliss-audio-cooper-fx)
- [AudioNewsRoom — Generation Loss MkII review](https://audionewsroom.net/2024/03/beauty-in-imperfection-chase-bliss-generation-loss-mkii-review.html)
- [Delicious Audio — Generation Loss MkII overview](https://delicious-audio.com/chase-bliss-audio-generation-loss-mkii/)
- [Effects Database — Generation Loss model entry](https://www.effectsdatabase.com/model/chasebliss/generationloss)
- [Equipboard — Generation Loss MKII (users/where-to-buy)](https://equipboard.com/items/chase-bliss-audio-generation-loss-mkii)
- [Martin Yam Møller — demo of all 12 tape models](https://martinyammoller.com/youtube/chase-blisse-generation-loss-mkii-demo-of-the-12-tape-models/)
- [MATRIXSYNTH — Generation Loss MKII sound demo (no talking)](https://www.matrixsynth.com/2024/03/chase-bliss-generation-loss-mkii-sound.html)
- [Gearnews — Generation Loss MKII 2-in-1 stereo magnetiser](https://www.gearnews.com/chase-bliss-generation-loss-mkii-2-in-1-stereo-magnetiser/)
