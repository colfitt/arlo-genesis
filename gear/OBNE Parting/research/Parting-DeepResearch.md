# Old Blood Noise Endeavors Parting — Deep Research

A working dossier for the OBNE x Emily Hopkins **Parting** as it opens Board 2 (Middle / Texture). Important correction up front: despite the rig art tagging this slot **"Filter · EXP,"** Parting is **not a filter pedal**. The manual and OBNE's own copy confirm it is a **stereo glitch delay / reverb / "crushing" modulation device** — a chance-driven, generative engine with a *post-dissolve* state-variable filter as just one of its sections. In this rig it is the first thing Board 1's stereo signal (Deco V2 out) hits before CB Lost & Found, Hologram Microcosm, Walrus QI Etherealizer, and OBNE Dark Star V3. So its real job here is not "front-end filter sculpt" — it's to inject probabilistic glitch, reverse, bit-crush, tremolo/vibrato, and smear *at the head of the texture stage*, where everything downstream then re-mangles its output. The Filter knob and the EXP jack are real and useful; they just aren't the whole story.

## 1. Lineage: OBNE's design ethos and what Parting actually is

Old Blood Noise Endeavors was founded in Oklahoma City in 2014 by Brady Smith and Seth McCarroll, who met at the University of Oklahoma. Smith had prior bench time at [Keeley Electronics and Walrus Audio](https://www.musiciansfriend.com/thehub/building-old-blood-noise-endeavors-brady-smith) before launching OBNE with the Black Fountain Delay. The house design philosophy is explicitly cinematic — per the [Chicago Music Exchange OBNE Q&A](https://www.chicagomusicexchange.com/blogs/news/inside-old-blood-noise-endeavors), they "align every one of these sounds with a picture," and every pedal carries commissioned artwork (Parting's floral/illustrated face is by **James Roo** per the [OBNE product page](https://oldbloodnoise.com/parting)). That ethos matters because Parting is sold as a *feeling* — "a box of pleasant surprises" — not a utility.

**What it is:** Parting is the OBNE x Emily Hopkins collaboration, released **January 2026** at **$329**, and per [Guitar Pedal X](https://www.guitarpedalx.com/news/news/old-blood-noise-endeavors-collaborates-with-emily-hopkins-on-the-parting-glitch-delay-reverb-crushing-modulation-device) it is the fifth pedal in OBNE's larger square-format series (the lineage that includes the Stereo **Dark Star**). Emily Hopkins — the Long Island electroacoustic harpist and prolific pedal-demo creator whose first YouTube video was a [Chase Bliss MOOD review](https://www.gearnews.com/old-blood-noise-endeavors-debut-parting/), and who has scored for Ubisoft and DreamWorks — shaped it around her taste for "glitch, signal crushing, and ambient sounds." The OBNE one-liner from the manual is the clearest description: *"Moments of chance will give bursts of a glitch delay that can smear into a reverb, modulated by tremolo or vibrato, filtered, and, most importantly, dissolved into lo-fi aliasing or stretched out reverse."* No version history yet — this is a first-run, single-version pedal as of mid-2026.

The pedal is organized into three colored sections (visible on the face): **Modulation** (red), **Glitch Delay / Reverb** (blue), and **Dissolve** (green), plus **Misc** switches (purple) and the additional Filter/Mix controls.

## 2. Controls — every knob, switch, and the expression behavior

From the [manual](manuals/OBNE%20Parting.pdf), there are eight knobs, three small toggles, and two footswitches.

**Modulation (red):**
- **Rate** — speed of the modulation LFO, which *also* sets the trigger frequency for "moments of chance." Alt control (hold Aux + turn): **Rate Subdivisions** — ÷4, ÷3, ÷2, x1, x2, x3, x4 (saved per preset; default x1).
- **Depth** — LFO depth. Alt control (hold Aux + turn): **Width** — the stereo spread of the modulation, from mono up to wide stereo. (Directly relevant to a stereo board — see §5.)
- **Shape** — LFO shape: Sine, Square, Reverse Saw, Saw, Random Sine, Random Square, **Envelope**. In Envelope mode the LFO follows a sine *and* your playing dynamics determine when signal enters the delay/reverb buffer (instead of random triggering). An LED near Shape shows live LFO position.
- **Mod switch** (next to Time) — Tremolo (LED off) or Vibrato (LED on).

**Glitch Delay / Reverb (blue):**
- **Chance** — probability that bits of signal enter the delay/reverb buffer per LFO cycle. Below noon: 0→100% chance, with a 50/50 split between *new* (input) and *old* (last output) signal. Above noon: new signal always passes, and the chance of feeding back *old* signal climbs 0→100% — at max it becomes a chaotic sound-on-sound looper. **Set to noon for a constant, surprise-free delay/reverb.** In Envelope Shape mode, Chance becomes an envelope **sensitivity** control.
- **Smear** — adds diffusion and feedback to the delay lines, blooming them into lush reverb as you turn up. This is the delay→reverb morph control.
- **Glitch** — clock subdivision chaos. Below noon: sets LFO + delay/reverb clock to half / normal / double speed (subdivided tempos + octave jumps). Above noon: introduces a 0→100% chance that, at the top of each LFO cycle, that value is *randomly* reassigned, and randomly halves/doubles the Dissolve sample rate.
- **Time** — delay/reverb time, and the reverse time. Alt control (hold Aux + turn): **Time Subdivisions** — 16th, dotted 16th, 8th, triplet, dotted 8th, quarter (default quarter).

**Dissolve (green):**
- **Dissolve** — the signature control. Below noon: progressive **sample-rate reduction** (bit-crush / lo-fi aliasing). Above noon: **reverse**, repeatedly halving the reverse clock as you turn up → increasingly long, degraded reverse trails.

**Additional controls:**
- **Filter** — cutoff of the **post-dissolve** filter. The toggle sets type: **low pass** (LED off, 0→13 kHz) or **high pass** (LED on, 2 kHz→0). State-variable, **12 dB/octave**. *This is the "Filter" the rig art refers to — a single sweepable cutoff on the wet path, not a resonant standalone filter.*
- **Mix** — dry/wet blend with a twist toggle. **Standard** (LED off): analog dry CCW → wet CW. **Modified** (LED on): dry *and* wet both pass through dissolve/mod/filter (blend happens *before* those stages), and during reverse it parallels in some dry signal on the lower knob sweep.
- **Volume** — hidden alt control via MIDI CC 27 (not a front-panel knob).

**Footswitches & Aux:**
- **On/Off** — tap to latch, hold for momentary.
- **Aux** — assignable to one of three global behaviors: **Tap Tempo**, **Half Speed** (half/normal clock), or **Preset switching**. You pick by holding Aux + pressing On/Off (tap), Mod (half speed), or Preset (presets).

**Expression:** The EXP jack maps a TRS expression pedal to **any combination of knobs at once**. You assign it by holding On/Off and sweeping the knob(s) you want — the position when you press is the heel, the position when you release is the toe; unmoved knobs are unaffected. **Expression settings save per preset.** This is the deep, defining feature for this rig (see §4, §13). The jack can alternately accept a momentary footswitch (e.g. OBNE Scooch) as external tap.

## 3. Sonic character

Parting does not have one voice; it has a probability distribution of voices. The constants:

- **Glitch delay core** — short bursts and stutters rather than a clean repeating delay, unless you park Chance at noon and Glitch below noon, which yields a more conventional (still characterful) delay.
- **Smear → reverb** — turning Smear up diffuses the delay taps into a genuinely lush, blooming reverb. The delay/reverb boundary is a continuum, not a mode switch.
- **Dissolve degradation** — the sonic signature Hopkins pushed for. Below noon it is a sample-rate crusher (gritty, aliased, "recorded-wrong"); above noon it's reverse that stretches and degrades — exactly the [Russo Music reviewer's](https://www.russomusic.com/blogs/reviews/old-blood-noise-endeavors-parting-glitch-device-review) "warped blinks in the time-space continuum" and "long and degrading reverse trails."
- **Modulation color** — tremolo (chop, Boss Slicer–adjacent at fast rates per Russo) or vibrato (pitch warble), with random LFO shapes that make the chops/warbles unpredictable.

Reviewers reach for words like "celestial," "twinkling, whistling harmonic peculiarities," "resonant, grumbling," and "busy pile-ups of sound" ([Russo Music](https://www.russomusic.com/blogs/reviews/old-blood-noise-endeavors-parting-glitch-device-review)). The honest summary: it is a **generative, chance-forward ambient/glitch texture box**, closer in spirit to a Hologram Microcosm or Chase Bliss MOOD than to any filter or delay you'd reach for to "sit in a mix."

**On the Filter specifically:** it is a clean, musical 12 dB/oct low-pass or high-pass on the wet signal. It tames the brightness of bit-crushed/reverse content and can roll the whole wet wash dark or thin it out. It is *not* resonant and does *not* self-oscillate — so it is not the "resonant drone filter" the brief speculated about. Treat it as a tone-tilt on the texture, swept beautifully by expression.

## 4. Behavioral notes — chance, feedback, envelope, expression

- **Self-oscillation:** The *filter* does not self-oscillate. The *feedback path* absolutely can run away — Chance past noon climbs toward 100% old-signal feedback, which the manual calls "something like a chaotic sound-on-sound looper" at max. That is the runaway mode here: a feedback/looping bloom, not filter resonance.
- **Chance/randomness:** The core behavior. Triggers fire at the LFO rate (watch the LED above Aux, which pulses at that rate). Two random layers stack: Chance (whether/what enters the buffer) and Glitch's upper range (random clock reassignment + random sample-rate halving). The pedal genuinely surprises you — design intent.
- **Envelope/dynamic mode:** Setting Shape to **Envelope** turns Parting reactive — your attack determines when signal enters the buffer, and Chance becomes sensitivity. This is the most "playable" mode and the one that responds to dynamics from the baritone or banjo.
- **Expression sweep:** Because EXP can map *any combination of knobs*, you can build a single-pedal performance gesture — e.g. heel = clean-ish delay, toe = full reverse + bit-crush + Smear-to-reverb + filter-closed. This is where the rig's "EXP" tag earns its keep; it's a morph controller, more than a wah-style filter sweep.
- **Tap & clock:** Tap tempo (Aux or external Scooch), MIDI clock in/out, and per-preset subdivisions mean it can lock to the rest of a MIDI rig.

## 5. Signal-chain placement — front of Board 2, filtering the stereo wall before granular/smear

The rig order is `[Board 1 → Deco V2 stereo out] → **Parting** → CB Lost & Found → Hologram Microcosm → Walrus QI Etherealizer → OBNE Dark Star V3 → [Board 3]`. Observations for this exact slot:

- **Stereo routing must be set correctly.** Parting defaults can be Mono / Mono-In-Stereo-Out / **Stereo** (set by holding On/Off + pressing Preset). Board 2 is stereo and Parting receives a true stereo pair from the Deco. **Set Parting to full Stereo** so it preserves the L/R image arriving from Board 1 and hands a stereo pair to Lost & Found / Microcosm. If it's left in Mono or MISO, you collapse the Deco's stereo width at the very top of the texture board. This is the single most important setup step.
- **Trails vs. true bypass.** Parting can be true-bypass or trails (set while assigning routing). For ambient use at the head of a wash, **trails on** keeps reverse/Smear tails alive when you disengage — usually what you want here.
- **It's first for a reason.** Putting the chance/glitch/reverse engine *before* the granular (Microcosm) and smear (Dark Star) means everything downstream re-samples and re-diffuses Parting's already-degraded, already-glitched output. Reverse trails get granularized; bit-crushed bursts get smeared into Dark Star's pad reverb. That compounding is the entire point of Board 2.
- **The Filter as a front-end tone-tilt is legitimate** — just understand it only filters Parting's *wet* path (or, in Modified Mix mode, the blended dry+wet). It is not an EQ on the whole board's dry signal. If you want to darken the *entire* stereo wall, that's a Mix=Modified + Filter LP move, accepting that your dry also gets dissolved/modulated.
- **Feedback discipline:** With Lost & Found's randomness and Microcosm's loops downstream, keep Parting's Chance near noon for predictable behavior unless you specifically want stacked chaos. Three random pedals in a row (Parting Chance + Lost & Found + Microcosm modes) can become unmusical fast.

## 6. Source-specific notes (banjo, baritone, modeled VG-800, bass)

All sources reach Parting *after* the VG-800 has summed the GK-5 hex signal and Board 1 has shaped it — so Parting always sees a full-range, line-level stereo guitar/banjo signal, not divided pickup data.

- **Baritone Jazzmaster:** Home territory. Long sustained baritone chords feed the Smear→reverb bloom beautifully, and the low fundamentals survive Dissolve's bit-crush as satisfying grit. Use Envelope Shape so your picking dynamics gate the glitches.
- **Gold Tone EBM-5 banjo (GK-5 → VG-800):** Banjo's fast attack/fast decay is ideal trigger fodder for chance-based glitching — each pluck is a clean transient the Envelope mode can latch onto. The reverse function (Dissolve above noon) turns banjo rolls into stretched, backwards arpeggios, and the post-dissolve **low-pass Filter** is genuinely useful here to roll off banjo's piercing 2–4 kHz before it gets granularized downstream. Banjo-as-lead through Parting in reverse + Smear is a signature texture this rig can produce.
- **Modeled VG-800 signals:** Parting treats a modeled amp/cab or COSM/synth patch like any line input. Pad/drone patches from the VG-800 are excellent Parting fodder — sustained continuous tone gives the chance engine and Smear something to build a wash from. Polyphonic guitar-synth patches will artifact under Dissolve's sample-rate crush, which suits the "broken" aesthetic.
- **Jazz bass / Jazz bass-modeled:** The low-pass Filter and Mix control matter more here — keep the dry low end intact (Standard Mix) so bit-crushed/reverse wet doesn't swamp the fundamental. Bass into reverse-Dissolve is a strong sub-drone source.

No published source documents Parting with a VG-800 specifically; the above is inference from its signal behavior and is flagged as such.

## 7. Famous users — honest assessment

Parting is brand-new (Jan 2026) and boutique, so there is no developed user mythology. The one genuine, verifiable association is **Emily Hopkins** herself — co-designer and the artist whose harp-and-pedals YouTube work the pedal is built around; her demos *are* the reference recordings. Beyond Hopkins, claims of "famous users" would be invented — **flag as unverified.** Expect it to surface on ambient/experimental and harp/electroacoustic boards as coverage grows, but as of this writing no notable artist has publicly claimed it as a signature voice.

## 8. Live, power, and I/O

- **Power:** 9V DC center-negative, 2.1mm barrel, **350 mA** ([OBNE](https://oldbloodnoise.com/parting)). This is a **hungry digital pedal** — far above the 10–100 mA analog pedals on the board. Budget an isolated 350 mA+ supply slot; do not daisy-chain it with other digital boxes on a marginal output.
- **Routing / I/O:** Full **stereo in / stereo out**, switchable Mono / Mono-In-Stereo-Out / Stereo. Analog dry-through. **Confirmed stereo** — correct for Board 2.
- **Bypass:** Soft-touch relay switching; selectable **true bypass or trails**. (As with relay bypass generally, it needs power to pass signal.)
- **Expression jack:** TRS; maps any combination of knobs, or accepts a momentary footswitch (Scooch) as external tap with a TRS cable.
- **MIDI:** 3.5mm TRS Type A **In and Out** (Out acts as Thru and can send clock). Full CC control of every parameter (see §12), PC for presets, MIDI clock in/out with selectable clock modes. Default Channel 1, changeable via CC 102.
- **Presets:** 3 onboard slots + live mode via the Preset switch; **127 presets total addressable over MIDI PC** (PC 128 = live mode). (Note: OBNE's webstore copy says "8 presets" — the manual's 3-onboard / 127-via-MIDI is authoritative and is what's documented here.)
- **Dimensions:** 4.25"W × 5"H × 2"D per [OBNE](https://oldbloodnoise.com/parting). Larger square format — plan board real estate accordingly.
- **USB:** Present but currently **no function** (reserved for future firmware).

## 9. Pairing recommendations by name

- **Into CB Lost & Found (immediately after):** Lost & Found's random momentary engagement pairs naturally with Parting's chance bursts — but stack deliberately. Use Parting for *sustained* generative texture and let Lost & Found punch holes/variations in it, rather than running both at max randomness.
- **Into Hologram Microcosm:** The headline pairing. Parting's reverse trails and bit-crushed glitch are ideal granular source material — Microcosm re-samples Parting's already-degraded output into loops and grains. Park Parting's Chance near noon for a steady wash that Microcosm can reliably capture, or push Chance high for chaos Microcosm then freezes.
- **Into Walrus QI Etherealizer:** Etherealizer's harmonic/shimmer processing will gild Parting's Smear-reverb bloom. Keep Parting's Filter as a low-pass tilt so Etherealizer isn't fed harsh aliasing.
- **Into OBNE Dark Star V3 (same maker, end of Board 2):** The OBNE-ecosystem pairing. Both share the same platform DNA — stereo, dry-through, trails/TB, **expression over every knob**, MIDI, presets ([Dark Star Stereo](https://oldbloodnoise.com/pedals/p/dark-star-stereo)). Parting's reverse + Dark Star's lo-fi pad reverb is a deep ambient well; Dark Star will smear and pitch-shift whatever Parting hands it into a sustained wall. Two OBNE boxes bookending the texture board is a coherent sonic signature.
- **Expression strategy across the board:** Map Parting's EXP to a heel=delay / toe=reverse+crush+Smear morph; this single gesture reshapes the entire downstream texture chain in real time — the most powerful performance move this pedal enables in this rig.

## 10. Reviews & demos

- [OBNE official product page](https://oldbloodnoise.com/parting) — specs, copy, colorways (Green/Purple/Stone/Basic), James Roo art.
- [Guitar Pedal X — Parting announcement / writeup](https://www.guitarpedalx.com/news/news/old-blood-noise-endeavors-collaborates-with-emily-hopkins-on-the-parting-glitch-delay-reverb-crushing-modulation-device) — best on lineage (5th square-format pedal) and section breakdown.
- [Russo Music — Parting Glitch Device review](https://www.russomusic.com/blogs/reviews/old-blood-noise-endeavors-parting-glitch-device-review) — most useful hands-on prose on the actual sounds.
- [Gearnews — Parting debut](https://www.gearnews.com/old-blood-noise-endeavors-debut-parting/) — Emily Hopkins background and context.
- [Synth Anatomy — Parting overview](https://synthanatomy.com/2026/01/obne-parting-a-colorful-glitchy-delay-reverb-pedal-in-collaboration-with-emily-hopkins.html) — concise feature summary.
- [Guitarbomb — "Glitch-Ambient Powerhouse"](https://guitarbomb.com/blood-noise-endeavors-parting-emily-hopkins/) — editorial overview.
- [Old Blood Noise x Emily Hopkins — Parting](https://www.youtube.com/watch?v=rayDmE0T78o) — the reference demo. *(Hosted on Emily Hopkins's own "Harp Lady" channel, 2026-01-21 — i.e. the co-designer's own harp demo, not OBNE's channel; verified via yt-dlp.)*
- [OBNE — "LIVE: Dan Explains It All ft. Emily Hopkins"](https://www.youtube.com/watch?v=wqKU6eFSW-s) — the authoritative OBNE-channel knob-by-knob walkthrough (2026-01-28).
- [Sound Study // OBNE x Emily Hopkins — Parting (YouTube)](https://www.youtube.com/watch?v=Y02HdE3_k-c) — extended sound exploration.
- [OBNE Parting Glitch Delay/Reverb Modulator Demo (YouTube)](https://www.youtube.com/watch?v=S1BBPUYf-TE) — control walkthrough.
- [PedalScapes — Parting unboxing / first play (YouTube)](https://www.youtube.com/watch?v=V9K2Hc1OLH8) — ambient-focused first impressions.

## 11. Mods, quirks, and known issues

- **No mods documented** — it's a digital DSP pedal; there's no analog tone cap to swap. Firmware is the only future variability (USB reserved, no updates yet as of mid-2026).
- **Preset-count discrepancy:** marketing says "8 presets," manual says 3 onboard + live (127 via MIDI). Trust the manual.
- **Chance is genuinely random** — two identical knob settings will not produce identical output. This is a feature, not a fault, but it means Parting is hard to use for parts that need to be repeatable take-to-take. For consistency, park Chance at noon and Glitch below noon.
- **350 mA draw** is the practical gotcha — undersized/daisy-chained power will cause dropouts or refusal to boot. Most-reported "issue" with pedals like this.
- **Filter is non-resonant / no self-oscillation** — don't expect a screaming resonant sweep; it's a clean tilt. (Corrects the rig-art "Filter" framing.)
- **Stereo width on modulation** (Depth alt-control = Width) can collapse to mono if set low — easy to leave narrow by accident on a stereo board.
- Build quality is standard OBNE hand-assembled; no widely reported reliability failures (pedal is too new for long-term data — flag as not-yet-established).

## 12. Spec sheet

| Spec | Value |
|---|---|
| Type | Stereo glitch delay / reverb / "crushing" modulation device (digital DSP) |
| Maker | Old Blood Noise Endeavors x Emily Hopkins |
| Released / Price | January 2026 / $329 USD |
| Power | 9V DC center-negative, 2.1mm, **350 mA** |
| Routing | **Stereo** in/out; switchable Mono / Mono-In-Stereo-Out / Stereo; analog dry-through |
| Bypass | Soft relay; selectable true bypass or trails |
| Controls | Rate, Depth, Shape, Chance, Smear, Glitch, Dissolve, Time, Filter, Mix (+ Volume via MIDI) |
| Switches | Mod (trem/vib), Filter (LP/HP), Mix (std/mod), Aux (tap/half-speed/preset) |
| Filter | State-variable 12 dB/oct; LP 0–13 kHz or HP 2 kHz–0; non-resonant |
| Modulation | Tremolo / Vibrato; LFO shapes: Sine, Square, Rev Saw, Saw, Random Sine, Random Square, Envelope |
| Expression | TRS; maps any combination of knobs; per-preset; or external momentary tap (Scooch) |
| MIDI | 3.5mm TRS Type A In/Out; full CC, PC presets, clock in/out |
| Presets | 3 onboard + live mode; 127 addressable via MIDI PC |
| USB | Present, no current function (future firmware) |
| Dimensions | 4.25"W × 5"H × 2"D |
| Art | James Roo |

Sources: [OBNE Parting page](https://oldbloodnoise.com/parting); [Parting manual](manuals/OBNE%20Parting.pdf).

## 13. Starting-point settings

Knob positions are clock-face from above. Set **Routing = Stereo** and **Trails = on** first.

**(a) Static texture tilt** — clean-ish delay/reverb to sit under everything (the "use it like a tone-shaped delay" setting)
- Chance: 12 · Glitch: 10 (below noon, normal clock) · Smear: 1 · Dissolve: 12 (no crush/reverse)
- Filter: 1–2 o'clock, **LP** · Mix: ~11, Standard · Shape: Sine · Mod switch: Tremolo, Depth low
- Predictable, no surprise feedback. Good bed for Microcosm/Dark Star downstream.

**(b) Expression morph (the "EXP" setting the rig art wants)** — heel = bed, toe = full chaos
- Base (heel): settings from (a). Assign EXP (hold On/Off, sweep): **Dissolve 12→3 o'clock** (into reverse), **Smear 1→3**, **Filter open→half-closed LP**, **Chance noon→2 o'clock**.
- One expression pedal sweeps the whole texture stage from clean wash to reverse/crushed feedback bloom.

**(c) Resonant-drone substitute** — sustained, oscillating wall (achieved via feedback, not filter resonance)
- Chance: 2–3 o'clock (high old-signal feedback) · Smear: max · Dissolve: 1 o'clock (light reverse) · Glitch: 12
- Filter: 12, LP · Mix: 1 o'clock · Mod: Vibrato, slow/shallow · Shape: Random Sine
- Builds a self-sustaining looped wall. Watch runaway; ride Mix or Chance to tame. Feed Dark Star V3 after.

**(d) Pre-granular shaping** — degraded reverse/bit-crush fodder for Microcosm
- Dissolve: 3 o'clock (long reverse) OR 9 o'clock (heavy bit-crush) · Chance: 12 · Smear: 11 · Glitch: 11
- Filter: 1 o'clock **LP** (tame aliasing) · Mix: 12 · Shape: **Envelope** (dynamics gate the glitches) · Mod: Tremolo
- Hand Microcosm a steady stream of reverse/crushed grains. Best with banjo or baritone transients driving the envelope.

## 14. Versus alternatives — why it earns the Board-2 opener slot

- **Hologram Microcosm** (downstream in this rig): the obvious comparison — both are generative, stereo, granular/glitch ambient engines. Microcosm is loop/granular-led; Parting is chance/delay/reverse/crush-led. They're complementary, not redundant, which is exactly why Parting *opens* and Microcosm *follows* — Parting generates degraded source, Microcosm granularizes it.
- **Chase Bliss MOOD MkII** (on Board 3): MOOD is a micro-looper/modified-delay with a "loop vs live" split; Parting overlaps on lo-fi/reverse character but is more chance-forward and has true stereo plus a proper Smear-reverb. Putting Parting on Board 2 and MOOD on Board 3 keeps their roles distinct (texture generation vs. loop/print).
- **OBNE Dark Star V3** (same board, after Parting): Dark Star is a pad/reverb-led lo-fi engine; Parting is delay/glitch-led. Same platform, opposite ends of the texture board — Parting throws the dice, Dark Star catches and smears them.
- **Generic filter pedal (what the rig art implies):** if the goal were literally "filter the stereo wall," a dedicated resonant/envelope filter (or even the VG-800's own filtering) would do it better. Parting earns the opener slot **not** as a filter but because it's the rig's chance/degradation/reverse generator — the one box that injects unpredictability and lo-fi reverse at the head of the chain so everything downstream has something broken and evolving to work on. Its expression-mapped morphing and stereo routing make it a performance front-end, not a static EQ. That's the real justification for slot #1 on Board 2.

## Sources

- [Old Blood Noise Endeavors — Parting product page](https://oldbloodnoise.com/parting)
- [Parting instruction manual (local PDF)](manuals/OBNE%20Parting.pdf)
- [Guitar Pedal X — OBNE x Emily Hopkins Parting writeup](https://www.guitarpedalx.com/news/news/old-blood-noise-endeavors-collaborates-with-emily-hopkins-on-the-parting-glitch-delay-reverb-crushing-modulation-device)
- [Russo Music — Parting Glitch Device review](https://www.russomusic.com/blogs/reviews/old-blood-noise-endeavors-parting-glitch-device-review)
- [Gearnews — Emily Hopkins & OBNE debut Parting](https://www.gearnews.com/old-blood-noise-endeavors-debut-parting/)
- [Synth Anatomy — Parting overview](https://synthanatomy.com/2026/01/obne-parting-a-colorful-glitchy-delay-reverb-pedal-in-collaboration-with-emily-hopkins.html)
- [Guitarbomb — Parting "Glitch-Ambient Powerhouse"](https://guitarbomb.com/blood-noise-endeavors-parting-emily-hopkins/)
- [Perfect Circuit — Parting product listing](https://www.perfectcircuit.com/old-blood-noise-parting.html)
- [Chicago Music Exchange — Inside OBNE Q&A with Brady Smith](https://www.chicagomusicexchange.com/blogs/news/inside-old-blood-noise-endeavors)
- [Musician's Friend — Building OBNE with Brady Smith](https://www.musiciansfriend.com/thehub/building-old-blood-noise-endeavors-brady-smith)
- [OBNE — Dark Star Stereo (ecosystem context)](https://oldbloodnoise.com/pedals/p/dark-star-stereo)
- [Old Blood Noise x Emily Hopkins — Parting (official YouTube)](https://www.youtube.com/watch?v=rayDmE0T78o)
- [Sound Study // OBNE x Emily Hopkins — Parting (YouTube)](https://www.youtube.com/watch?v=Y02HdE3_k-c)
- [OBNE Parting Glitch Delay/Reverb Modulator Demo (YouTube)](https://www.youtube.com/watch?v=S1BBPUYf-TE)
- [PedalScapes — Parting unboxing / first play (YouTube)](https://www.youtube.com/watch?v=V9K2Hc1OLH8)
