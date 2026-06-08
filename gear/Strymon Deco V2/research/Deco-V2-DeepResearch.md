# Strymon Deco V2 — Deep Research

A working dossier for the Deco V2 as the **closer on Board 1** — the last pedal before the rig's signal leaves the front board in stereo. It sits immediately after the CE-2W's stereo split, so it is the first place the dry/chorused front-board voice gets *tape coloration*, and the only tape stage that touches the signal while it's still "guitar." Everything downstream (the Board 2 texture pedals, then the End Board's Generation Loss / PORTA424 / JHS 424 tape stack) is processing a signal that has *already* been through one tape machine. That front-loaded placement is the whole reason this document exists: the Deco is doing wall-thickening, width, and wobble on a source the End Board never gets to touch in its raw state.

## 1. Lineage: Damage Control → Strymon Deco → V2

Strymon began life as **Damage Control Engineering**, founded 2004, building tube-hybrid pedals; in 2009 the company retired the Damage Control product line and rebranded as Strymon ([The Guitar Marketplace](https://theguitarmarketplace.com/the-rise-of-strymon-from-damage-control-to-dsp-pioneer/), [Strymon 10-year blog](https://www.strymon.net/10-year-anniversary-blog/)). The Deco's enclosure still carries the **"© Damage Control Engineering, LLC"** mark on the spec page of the manual — a nod to that origin.

The Deco itself is not a clone of one specific pedal the way the Hizumitas chases the Elk Sustainar. It's a **mechanical model of a pair of vintage reel-to-reel tape machines** — the saturation/preamp behavior of 2-track mastering decks, plus the studio "automatic doubletracking" and tape-flange techniques that engineers built in the 1950s–70s by running two synchronized tape transports and varying the speed of one of them ([Strymon product page](https://www.strymon.net/product/deco/), [Sound on Sound](https://www.soundonsound.com/reviews/strymon-deco)). It's the Strymon take on the same tradition the EP-style/Echoplex preamp lives in — tape as a *sound*, not tape as a *delay*. Premier Guitar's Joe Gore called the original "the most convincing tape sounds I've encountered in a stompbox" ([Premier Guitar](https://www.premierguitar.com/gear/strymon-deco-tape-saturation-doubletracker-review)).

**V1 → V2 — what actually changed** (per [Strymon's "What's new with Deco V2"](https://www.strymon.net/faq/whats-new-with-deco-v2/) and [Guitar.com](https://guitar.com/reviews/effects-pedal/strymon-deco-v2-review/)):

- **TONE knob added** to the Tape Saturation side — V1 had 5 knobs, V2 has 6. You can now shape the EQ of the saturation as you add it (dark → bright), instead of a fixed voicing.
- **CASSETTE voice added** to the VOICE switch — an auto-level-control (ALC) model from high-end cassette decks, giving a compressed, fat alternative to the **classic** 2-track reel-to-reel voicing.
- **Externally mounted mono/stereo INPUT switch** — V2 is **true stereo in / stereo out** (except in Wide Stereo and Bounce modes). The V1 was effectively mono-in.
- **Full MIDI** via the 1/4″ TRS EXP/MIDI jack (or USB-C) — **300 preset locations**, CC control over nearly every parameter, MIDI clock sync.
- **External USB-C** for firmware/MIDI; **new 520MHz ARM Superscalar processor**, 32-bit float, **new discrete Class A JFET input**.

Strymon's own framing: they "preserved the original sound and functions while updating the user interface for expanded I/O and control." For this rig the headline is the stereo I/O and MIDI — both load-bearing, see §5 and §8.

## 2. Controls

Two independent engines, each with its own footswitch and ON LED. **TAPE SATURATION** on the left; **DOUBLETRACKER** on the right. They stack in either order internally and can run together or alone.

**Tape Saturation side:**
- **VOICE** (mini-toggle) — `classic` = 2-track reel-to-reel mastering-deck saturation; `cassette` = ALC-compressed, fat cassette model. Cassette is described by reviewers as "a subtle shift that squashes the sound a little more and adds a roundness" ([Guitar.com](https://guitar.com/reviews/effects-pedal/strymon-deco-v2-review/)) — not a dramatic mode switch.
- **SATURATION** — preamp gain / tape drive. Low = subtle harmonic enhancement; up = dynamic compression and overdrive. Range is rig- and level-dependent: ~40 dB of volume-compensated gain on tap. Single coils get "harmonic enhancement and a lighter overdrive"; hot humbuckers/line signals push into "heavier overdriven harmonics."
- **TONE** (V2 only) — overall EQ of the saturation, dark → bright.
- **VOLUME** — output of the saturation engine.

**Doubletracker side:**
- **TYPE** (3-way) — phase/routing of the two decks: `sum` (Reference + Lag in phase), `invert` (summed out of phase → hollower, scooped low end), `bounce` (right channel of Lag Deck polarity-inverted and bounced to the left input → double-repeat / ping-pong).
- **LAG TIME** — the master control. Sweeps the delay offset between decks across the full tape arc: **tape flange (−.3–3 ms) → tape chorus (3–50 ms) → slapback (50–150 ms) → tape echo (150–500 ms max)**.
- **BLEND** — relative level of the two decks. CCW favors the Reference Deck (tames the effect), CW adds more Lag Deck; 12 o'clock = equal mix (most pronounced flange).
- **WOBBLE** — random modulation on the Lag Deck, modeling tape-speed variation. Low = mild time-varying flange; high = extreme warble, up to random vibrato.

**Secondary / Live Edit functions** (hold the **TAPE SATURATION ON** switch until both LEDs flash):
- **Low Trim** (on the TONE knob) — subtle high-pass to clean up rumble/mud.
- **Auto-Flange Time** (on LAG TIME) — sweep speed for the press-and-hold Auto-Flange.
- **Doubletracker Boost/Cut** (on BLEND) — ±3 dB level match, 12 o'clock = unity.
- **Wide Stereo Mode** (on WOBBLE) — Reference Deck → Left out, Lag Deck → Right out.
- **MIDI Clock Sync** (on TYPE) and **Respond/Ignore MIDI Expression** (on VOICE).

**Auto-Flange:** press and hold the **DOUBLETRACKER ON** footswitch for a momentary, studio-style through-zero flange — a "virtual audio engineer" sweeping the reels. Great as a one-shot transition.

## 3. Sonic Character

Two distinct jobs:

**Saturation as a wall-thickener.** This is the use that matters most in the rig. At low-to-mid SATURATION the Deco fattens and gently compresses without obvious distortion — "undeniable warmth and body," getting "throatier" and "chewier" as you push it ([Guitar.com](https://guitar.com/reviews/effects-pedal/strymon-deco-v2-review/)). After the entire Board 1 dirt stack (Colour Box, 108, Hizumitas, Brothers, Longsword, Oxford), the Deco's job is not *more* gain — it's *glue*: rounding the transient edges of a stacked-fuzz wall and adding the tape "thickness" that makes a doom chord read as one mass instead of layered pedals. The new TONE knob lets you keep that glue dark so the saturation doesn't reintroduce fizz the fuzzes already generate.

**The doubletracker, slapback → chorus → flange.** Driven entirely by LAG TIME. Short = through-zero **tape flange** (the comb-filter sweep); medium = "woozy chorus and psychedelic flange"; longer = "classic tape echoes and 50s-style slapbacks" ([Guitar.com](https://guitar.com/reviews/effects-pedal/strymon-deco-v2-review/)). Premier Guitar describes the arc precisely: a few milliseconds for "organic-sounding flange," lengthening to "several dozen milliseconds for chorused sounds," then "blossoming into audible echoes" ([Premier Guitar](https://www.premierguitar.com/gear/strymon-deco-tape-saturation-doubletracker-review)). The flange here is **summing-based**, not a swept LFO — the character is the comb filter between two decks, which is why it sounds like tape and not like a BBD flanger (and is a different flavor than the BF-3 sitting earlier in the chain).

## 4. Behavioral Notes

- **Flange via summing/cancellation.** The TYPE switch is doing phase math, not adding modulation. `sum` = additive, fullest. `invert` = the decks cancel — "a hollower, more spacious sound with a more controlled low end," and at echo settings it models real wall-reflection inversion. With **WOBBLE at zero** you get a **static comb filter** that "can profitably be used to shape or scoop out heavily distorted signals" ([Sound on Sound](https://www.soundonsound.com/reviews/strymon-deco)) — i.e. a fixed-notch EQ you can park across a fuzz wall.
- **Well-behaved feedback.** Despite being a tape-echo-style engine, it does not run away. SOS notes that even when fed back into itself "it's remarkably well-behaved" and doesn't self-oscillate readily ([Sound on Sound](https://www.soundonsound.com/reviews/strymon-deco)). Don't expect Generation-Loss-style runaway howl from the Deco alone — it's a controlled effect, not a chaos box.
- **Stereo behavior is mode-dependent.** Deco is true stereo in/out **except** in Wide Stereo and Bounce, which intentionally split the decks across L/R. **Wide Stereo is auto-disabled with a mono output** (only Left Out connected); in mono, BLEND acts as a pan/balance between decks. `bounce` mode "is very effective at creating a wide stereo signal from mono sources" — relevant since the CE-2W upstream is producing the stereo field the Deco then sits inside.
- **Through-zero intensity scales with bandwidth.** Strymon explicitly notes through-zero flange effects are "more intense when using distorted guitars or high-bandwidth input signals" — exactly the saturated, full-spectrum wall this rig feeds it.

## 5. Signal-Chain Placement — closing Board 1 in stereo

The order: `… Somersault → CE-2W (stereo split) → Deco V2 → stereo send to Board 2`. Observations for this exact slot:

- **It receives an already-stereo field.** The CE-2W splits to stereo *before* the Deco. With the Deco's INPUT switch set to **STEREO** (TRS), it processes L and R independently and passes a true stereo pair onward. Keep it stereo — collapsing to mono here throws away the CE-2W's width and disables Wide Stereo.
- **Tape-at-front vs tape-at-back.** This is the rig's deliberate two-tape architecture. The Deco is **tape on the source** — it colors and widens the guitar/banjo voice *before* it becomes texture. The End Board (Generation Loss → PORTA424 → JHS 424) is **tape on the result** — degrading and printing the *fully-processed* stereo bus after Board 2's granular/filter pedals have had their way. Two completely different jobs: the Deco thickens and doubles a clean-ish tone; the End Board ruins a finished one. There's no real redundancy — the Deco's saturation feeds the End Board something already warm and dense, which makes Generation Loss's degradation sound *intentional* rather than just lo-fi.
- **Why the closer, not earlier?** Putting tape saturation last on Board 1 means it glues the *entire* front-board dirt+mod stack into one cohesive wall before handoff, and the doubletracker's width is the last thing applied to the dry-ish voice — so Board 2's filters/granular pedals receive a wide, fat, doubled stereo image rather than a thin mono one.
- **Input Mode caution.** The CE-2W's output is instrument-level, so **Normal** input mode is correct here. If you ever insert the Deco into a hot effects-loop or line source, switch to **Studio** mode (+10 dB headroom) to avoid over-driving the input.

## 6. Source-Specific Notes

- **Modeled VG-800 signal (baritone JM + GK-5, EBM-5 banjo + GK-5).** By the time signal reaches the Deco it's already been through the VG-800's amp/cab modeling *and* the full dirt chain — it's a dense, mid-heavy, full-bandwidth source. That's ideal for the through-zero flange (intensity scales with bandwidth) and for the saturation's glue role. Use the TONE/Low Trim controls to keep the tape coloration from re-brightening a banjo voice you've already worked to tame upstream.
- **Banjo brightness.** The Deco won't fix banjo ice-pick the way the Hizumitas's tone stack can — but **Low Trim** plus a darker TONE setting keeps the saturation from adding fizz, and the doubletracker's chorus/wobble does a lot to soften the banjo's hard attack into something that swells.
- **Baritone Jazzmaster.** Home turf for tape saturation — the low end loves the `classic` voice's compression, and `invert` TYPE "controls the low end" if the baritone gets flabby through the chain.
- **Bass (Jazz bass).** The manual explicitly calls out bass as a low-output source that gets "rich harmonic enhancement." If running the bass through this board, `invert` mode for a tighter, more controlled bottom; keep SATURATION modest so the doubletracker doesn't smear pitch definition.

## 7. Famous Users (honest)

The Deco has a broad but diffuse user base — it's a studio-flavor utility, not a signature-artist pedal, so claims are weaker than the Hizumitas/Wata case. Per [Equipboard](https://equipboard.com/items/strymon-deco-tape-saturation-doubletracker): **Toro y Moi (Chaz Bear)**, **Yvette Young (Covet)**, **Ben Howard**, and **Myles Kennedy** have all been documented with a Deco on their boards. These are Equipboard-sourced sightings; treat them as "spotted on the board," not "signature tone." No single artist has claimed the Deco as a defining voice the way Wata claims the Hizumitas. *(Flag: Equipboard sightings are user-submitted and not independently verified beyond that listing.)*

## 8. Live / Power / I/O

| Item | Detail |
|---|---|
| Power | 9VDC, center-negative, **300 mA minimum** |
| Input | High-impedance (1 MΩ), discrete Class A JFET; TRS for stereo in |
| Output | Low-impedance (100 Ω) stereo; Out L for mono |
| Bypass | True bypass (electromechanical relay) by default; buffered bypass selectable via power-up mode |
| MIDI | Full MIDI over 1/4″ TRS (EXP/MIDI jack) or USB-C; 300 presets; MIDI clock sync |
| EXP/MIDI jack modes | Expression / Favorite / Tap / MIDI |

- **Power is the gotcha.** At **300 mA**, the Deco is far hungrier than the analog pedals on Board 1 (the Hizumitas draws 10 mA). Make sure its isolated supply slot can deliver 300 mA — a 100 mA slot will not boot it reliably.
- **MIDI is genuinely useful here.** Board 1 is otherwise mostly stomp-and-go, but the Deco's 300 presets mean you can recall a full saturation+doubletracker scene per song via Program Change — and Wide Stereo, Low Trim, and Boost/Cut are all saved per preset. MIDI clock sync (set on the TYPE knob) locks the echo repeats to the rig's tempo if you're sending clock from the End Board's MIDI brain.
- **MIDI channel default is 1** (set on SATURATION knob, GREEN). Note the manual's gotcha: **MIDI channel assignment and MIDI OUT mode are *not* saved per preset** — set them once via power-up mode.
- **Bypass tip:** the relay true-bypass requires power to pass signal. If you want consistent high-end through the long cable run to Board 2, the **buffered bypass** power-up option may be worth it here.

## 9. Pairing Recommendations (by name)

**Upstream (already in place):**
- **Boss CE-2W → Deco.** Correct. The CE-2W creates the stereo field; the Deco fattens and tape-colors it. Running the Deco's `classic` saturation after the Waza chorus gives the chorus body and tape warmth. If you want extra width, `bounce` mode adds ping-pong on top of the CE-2W's spread.

**Downstream into Board 2:**
- **→ OBNE Parting (filter).** The Deco's saturation gives Parting's filter a harmonically rich source to sweep — more interesting than filtering a clean signal.
- **→ Hologram Microcosm (granular).** Feed the Microcosm a *doubled, wide* signal and its granular textures sound thicker and more stereo. The Deco's slapback/chorus LAG settings give the Microcosm material to granulate.
- **→ Walrus QI Etherealizer / OBNE Dark Star V3.** Saturated, doubled input makes these smear/reverb-adjacent pedals bloom — same logic as the Hizumitas-into-reverb pairing.

**Versus the End Board tape stack:**
- The Deco is the **subtle, musical, source-side** tape voice. **Generation Loss** is the destructive, warbly, degradation-side voice. **PORTA424 / JHS 424** are the final channel-strip "print to cassette" stage. Don't try to make the Deco do Generation Loss's job — it's too well-behaved (§4). Use the Deco for *glue and width up front*, and let the End Board do *ruin and print at the back*.

## 10. Reviews & Demos (real links)

- [Premier Guitar — Strymon Deco review (Joe Gore)](https://www.premierguitar.com/gear/strymon-deco-tape-saturation-doubletracker-review) — "most convincing tape sounds I've encountered in a stompbox"; best on the LAG-TIME arc.
- [Sound on Sound — Strymon Deco review](https://www.soundonsound.com/reviews/strymon-deco) — best technical read on sum/invert/bounce phase behavior, static comb filter, and feedback behavior.
- [Guitar.com — Deco V2 review](https://guitar.com/reviews/effects-pedal/strymon-deco-v2-review/) — best on V2-specific changes (TONE, cassette), "a pedal you could start a band with."
- [Strymon — official Deco V2 product page](https://www.strymon.net/product/deco/) — feature list, $379, processing specs.
- [Strymon — What's new with Deco V2](https://www.strymon.net/faq/whats-new-with-deco-v2/) — authoritative V1→V2 changelist.
- [Strymon — Deco V2 support / manuals / firmware](https://www.strymon.net/support/deco-v2/) — manual, brochure, firmware updates.

## 11. Mods / Quirks / Firmware

- **No analog mods** — it's a DSP pedal (520MHz ARM, 32-bit float). "Mods" here means **firmware** via USB-C and power-up configuration.
- **Power-up modes persist across power cycles, not per preset:** Input Mode (Normal/Studio), Bypass Mode (True/Buffered), EXP/MIDI jack function, MIDI Channel, MIDI OUT mode, MIDI Clock Sync, MIDI Expression respond/ignore.
- **Live Edit secondaries *are* saved per Favorite/MIDI preset:** Low Trim, Auto-Flange Time, Wide Stereo, Doubletracker Boost/Cut.
- **Quirk — cassette is subtle.** Reviewers consistently note the cassette voice is a refinement, not a night-and-day mode. Don't expect dramatic lo-fi from it; that's the End Board's job.
- **Quirk — flange won't self-oscillate.** Deliberately tame; if you want runaway, that's Generation Loss.
- **Factory reset:** hold DOUBLETRACKER ON at power-up, sweep VOLUME 0→100→0 twice.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Engines | Tape Saturation + Doubletracker (independent footswitches) |
| Saturation voices | Classic (2-track reel-to-reel) / Cassette (ALC) |
| Doubletracker types | Sum / Invert / Bounce |
| Lag time range | −.3 ms (flange) to 500 ms (echo) |
| Controls | Saturation, Tone, Volume, Voice; Lag Time, Blend, Wobble, Type (+ Live Edit secondaries) |
| Saturation gain | ~40 dB, volume-compensated |
| Input impedance | 1 MΩ (discrete Class A JFET) |
| Output impedance | 100 Ω |
| Max input level | +10 dBu |
| A/D & D/A | 24-bit / 96 kHz |
| Processor | 520 MHz ARM Superscalar, 32-bit floating point |
| Signal/Noise | 109 dB typical |
| I/O | Stereo in (TRS) / stereo out; mono in or out via Left jack |
| MIDI | Full MIDI via 1/4″ TRS or USB-C; 300 presets; MIDI clock sync |
| External control | EXP / Favorite / Tap / MIDI (EXP/MIDI jack) |
| Bypass | True bypass (relay), or buffered (selectable) |
| Power | 9VDC, center-negative, 300 mA min |
| Dimensions | 4.5″ D × 4″ W × 1.75″ H |
| Price | $379 (Strymon, June 2026) |

Source: [Deco V2 manual Rev B](manuals/Deco_v2_UserManual_RevB.pdf) and [Strymon product page](https://www.strymon.net/product/deco/).

## 13. Starting-Point Settings

Clock-face positions, viewed from above. Both engines on unless noted.

**(a) Subtle tape glue** — the everyday Board-1-closer voice
- Saturation: 9–10 · Tone: 12 · Volume: unity · Voice: classic
- Doubletracker: OFF (or Blend full CCW). Just the saturation, gluing the dirt stack. Low Trim slightly up to keep the bottom tight before the stereo send.

**(b) Wide doubletrack** — fat, stereo, two-players-on-one-part
- Saturation: 9 · Voice: cassette · Lag Time: ~12 (chorus, ~20–40 ms) · Blend: 11 (favor Reference) · Wobble: 9–10 · Type: sum · Wide Stereo: ON
- The thickening width feeding Board 2. Keep Blend left so it doubles rather than warbles.

**(c) Summing-flange wobble** — moving comb filter across the wall
- Saturation: 10 · Lag Time: ~9 (flange, 1–3 ms) · Blend: 12 (50/50, strongest flange) · Wobble: 12–2 · Type: try sum vs invert
- For static notch-EQ on a fuzz wall, set Wobble to 0 (comb filter you can park). Through-zero gets more intense the more saturated the input — feed it the full dirt stack.

**(d) Saturated wall-thickener** — push the tape, doom glue
- Saturation: 1–2 (heavy) · Tone: 11 (dark) · Volume: to taste · Voice: classic
- Doubletracker: slapback (Lag ~50–100 ms), Blend 11, Type bounce for a "3D" double repeat. Max chord density before handoff to the texture boards.

## 14. Versus Alternatives — why it earns the Board-1-closer slot

- **Chase Bliss Generation Loss (End Board).** The obvious "why not just use one tape pedal" question. Generation Loss is *degradation* — warble, dropout, filtered VHS ruin — and it lives at the back to destroy the finished bus. The Deco is *musical tape coloration and doubling* on the live source. They're sequential jobs, not substitutes; the Deco's clean-ish glue is precisely what makes Generation Loss's ruin sound deliberate downstream.
- **JHS 424 / MXNHLT PORTA424 (End Board).** Cassette channel-strip "print" stages — the final lo-fi commit. The Deco's cassette voice overlaps *conceptually* but is far more subtle and, crucially, **stereo + MIDI + doubletracker-equipped**. The 424s can't double or widen a signal; the Deco can.
- **Keeley/Wampler/Origin tape-echo or doubler pedals.** None combine reel-to-reel saturation *and* a true through-zero summing doubletracker *and* stereo I/O *and* MIDI presets in one box at this price.
- **Strymon Volante / El Capistan.** Those are *delay* machines with tape flavor; the Deco is a *saturation + doubler* with delay as a byproduct of the lag. For a *closer* whose job is glue-and-width (not a delay voice — the rig has Big Time and H90 for that), the Deco is the right tool.

In this rig specifically, the Deco earns the slot because it's the **only stereo, MIDI-recallable tape stage that sits on the source** — gluing the entire Board 1 dirt+mod stack into one cohesive, doubled, wide image, and handing the texture boards a fat tape-colored stereo pair instead of a thin mono one. The End Board ruins; the Deco builds. You want both.

## Sources

- [Strymon — Deco V2 product page](https://www.strymon.net/product/deco/)
- [Strymon — What's new with Deco V2](https://www.strymon.net/faq/whats-new-with-deco-v2/)
- [Strymon — Deco V2 support](https://www.strymon.net/support/deco-v2/)
- [Strymon — 10-Year Anniversary / Damage Control history](https://www.strymon.net/10-year-anniversary-blog/)
- [Deco V2 User Manual Rev B (local PDF)](manuals/Deco_v2_UserManual_RevB.pdf)
- [Premier Guitar — Strymon Deco review](https://www.premierguitar.com/gear/strymon-deco-tape-saturation-doubletracker-review)
- [Sound on Sound — Strymon Deco review](https://www.soundonsound.com/reviews/strymon-deco)
- [Guitar.com — Strymon Deco V2 review](https://guitar.com/reviews/effects-pedal/strymon-deco-v2-review/)
- [The Guitar Marketplace — The Rise of Strymon: From Damage Control to DSP Pioneer](https://theguitarmarketplace.com/the-rise-of-strymon-from-damage-control-to-dsp-pioneer/)
- [Equipboard — Strymon Deco users](https://equipboard.com/items/strymon-deco-tape-saturation-doubletracker)
