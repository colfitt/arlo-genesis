# EarthQuaker Devices Hizumitas — Deep Research

A working dossier for slotting the Hizumitas into Board 1 of a hex-pickup banjo/baritone rig. The pedal lives between the MXR 108 silicon Fuzz Face and the Brothers AM drive platform, so a lot of this document is concerned with how it behaves with bright transient sources, with stacked dirt, and with synthesized signal from the VG-800 — not the things the EQD marketing copy is built around.

## 1. Lineage: Elk BM Sustainar → Hizumitas

The Hizumitas exists because of one specific pedal: Wata of Boris's circa-1973 **Elk BM Sustainar**, built in Japan by Elk Gakki Co. The Elk was one of the first non-EHX Big Muff clones in the world, in production from roughly 1973 — only a few years after the [original 1969 Triangle Big Muff Pi](https://www.guitarpedalx.com/news/news/earthquaker-devices-teams-up-with-wata-of-boris-for-her-signature-hizumitas-fuzz-sustainar---based-on-the-legendary-fierce-elk-bm-sustainar-triangle-muff-clone-with-unique-tone-stack). Early units even carried a "Big Muff" logo on the face plate before EHX presumably objected, after which Elk rebranded the same circuit as "Super Fuzz Sustainar" and "Big Mag Sustainar." Wata's reference unit dates to the brazen Big-Muff-logo era.

The Elk is loosely a Triangle clone but takes meaningful liberties. Per the [Guitar Pedal X technical writeup](https://www.guitarpedalx.com/news/news/earthquaker-devices-teams-up-with-wata-of-boris-for-her-signature-hizumitas-fuzz-sustainar---based-on-the-legendary-fierce-elk-bm-sustainar-triangle-muff-clone-with-unique-tone-stack), it uses **NEC A733k46 transistors** in place of the 2N5133s Mullard-era Triangles ran, and — much more importantly — runs an **inverted, more aggressive tone stack** that "retains more high-end frequencies across the sweep/range, and generally delivers more sizzle, alongside some very formidable low-end frequencies." The tone control is wired so that clockwise boosts *bass* and counter-clockwise boosts *treble* — opposite of every EHX-derived Muff variant.

EQD did not blindly clone the Elk. Per Yuichiro Hosokawa (CULT Tokyo, Wata's tech) in [EQD's own development blog](https://www.earthquakerdevices.com/blog-posts/wata-elk-big-muff-sustainar-and-hizumitas), Wata shipped her actual reference pedal to Akron and Jamie Stillman spent over a year matching it — Hosokawa frames the character as **"Fuzz 2.5 / Distortion 7.5"**, where a stock vintage Big Muff is closer to 4/6. That ratio matters: this is not the saggy, splatty fuzz end of the spectrum. It's the dense, distortion-leaning end, which is why EQD calls it a Fuzz *Sustainar* and not a Fuzz Distortion.

The schematic detective work on [vero-p2p.blogspot.com](https://vero-p2p.blogspot.com/2022/01/earthquaker-devices-hizumitas-schematic.html) is more skeptical: the author argues the Hizumitas is "much closer to an EHX Triangle Big Muff from 1972 than it is an Elk Sustainar," with the single biggest deviation being a **3n3 cap (vs the Elk's 330pF) in the tone stack high-pass filter** — a roughly 10x value change that fundamentally rebalances where the tone control's bass/treble pivot sits. Take that read with a grain of salt (the same post admits to incomplete component data), but the 3n3 swap is the most concrete circuit datum publicly available.

Relative to the canonical EHX family — Triangle (1969-73), Ram's Head (1973-77), Civil War (1991 green), Sovtek/Green Russian (Tall Font Bubble Font era), NYC reissue, and Op-Amp (V4) — the Hizumitas sits closest to Triangle in topology but with **sharper highs, more low-end shove, less mid-scoop than Civil War/Russian variants, and noticeably more articulate note separation than a NYC reissue**.

## 2. Circuit and Controls

The face plate has three knobs — **Volume, Sustain, Tone** — and one footswitch. No Filter knob in the literal sense; the "Filter" character the user's brief asks about is what the Tone knob does, and it's the standout control on this pedal.

- **Volume.** Hot output. Unity gain sits around 9–10 o'clock per [EQD's own settings notes](https://www.earthquakerdevices.com/blog-posts/hizumitas-for-noodlers); everything past that is a clean boost into the next pedal/amp.
- **Sustain.** This is the gain control. Per [Premier Guitar](https://www.premierguitar.com/gear/reviews/earthquaker-devices-hizumitas), "starts hot and goes from there — no clean tones available even at minimum." There is no edge-of-breakup floor on this thing; minimum Sustain is already crunchy.
- **Tone.** Inverted bilateral. Clockwise from noon → progressively scooped mids, tamed highs, massive low end. Counter-clockwise from noon → trebly, mid-forward, "near RAT territory" at the extreme per [EQD](https://www.earthquakerdevices.com/blog-posts/hizumitas-for-noodlers). Noon is roughly the flattest spot.

The Tone control is a passive high-pass/low-pass blend with a 3n3 cap on the HPF leg, which is what gives it the unusually wide low-end swing on the clockwise side. The behavior is closer to a **post-distortion EQ tilt** than a typical Muff "scoop slider," and that is why reviewers keep calling it "synth-like" — sustained notes change voicing dramatically as the Tone knob moves, in a way that feels more like sweeping a state-variable filter than adjusting a tone control.

Input impedance is ~150kΩ, output <10kΩ ([EQD spec page](https://www.earthquakerdevices.com/hizumitas)). That input impedance is low for a fuzz front end — important for the buffer discussion below.

## 3. Sonic Character vs Other Muffs

Placement on the three Muff axes:

- **Bright/dark:** Brighter than a Green Russian or Civil War. Roughly in the same brightness zone as a Triangle but with more *upper-mid* bite. Capable of getting darker than most Muffs at full-clockwise Tone (the 3n3 cap really does suck out highs there).
- **Scooped/mid-forward:** **Mid-forward by Muff standards**, especially at noon Tone or below. This is its single biggest tonal signature. A Muffuletta on its Civil War setting will be scoopier; the Hizumitas pushes through a band mix where a Russian-style Muff disappears.
- **Tight/loose low end:** Tight for a Muff. Hosokawa specifically calls out that it keeps "the bottom end that fills up when you palm mute" without going flabby. Tighter than a NYC reissue, looser than a Hoof.

Concrete head-to-head context:

- **EHX Big Muff Pi (NYC reissue):** Hizumitas is brighter, tighter, more articulate, and less mid-scooped. The NYC has more "wool"; the Hizumitas has more "grind."
- **Sovtek/Green Russian:** Russian is fatter, darker, scoopier, looser. Use the Russian for low-string riffs and the Hizumitas when you need the notes to actually punch through.
- **Triangle clones (Wren and Cuff Tri Pie '70, Tone Bender-influenced builds):** Closest sibling. Hizumitas adds more low end and more high-end sizzle simultaneously — it's the Triangle voiced for someone in a doom band who needs the chord to still read.
- **EQD Hoof:** Hoof is Russian-derived with germanium-leaning midrange. Different beast — tighter than Hizumitas in the low mids but never reaches the same wall-of-sound size.
- **EQD Acapulco Gold:** Power-amp emulation, no real tone control. Acapulco is a single-character bludgeon; Hizumitas covers a much wider arc and has actual sustain rather than just saturation.
- **JHS Muffuletta:** Six-Muff selector. The Civil War setting is the closest internal match, but the Muffuletta is voiced safer/cleaner across the board. Hizumitas has more grit-in-the-edges character than any single Muffuletta mode.
- **Wren and Cuff Tri Pie '70:** The most direct topological cousin. Tri Pie '70 is closer to the *unmodified* Triangle voicing; Hizumitas is the Elk re-voicing with more aggressive tone-stack swing.

## 4. Sustain and Dynamic Behavior

"Fuzz Sustainar" (the EQD spelling preserves the Elk's Japanese transliteration) is doing two things: (1) genuine long-decay sustain that holds a note past where most Muffs collapse into mush, and (2) compression behavior that is gentler than a Russian Muff but more obvious than a Triangle. Per the EQD noodlers post, the Sustain knob "kicks up the distortion, adding a hint of compression... but retains enough tightness to keep chords articulate."

Dynamically: it cleans up better than its aesthetic suggests. [Guitar Player](https://www.guitarplayer.com/reviews/earthquaker-devices-hizumitas-fuzz-sustainer-review) specifically calls out that it "cleans up quite well when you lighten up on the attack and/or turn down the guitar volume." This is genuinely useful — roll the volume back to 6–7 and you can get a controlled-crunch tone, even with Sustain at noon. It is *not* a Fuzz Face in terms of volume-knob responsiveness, but it's well ahead of a NYC Big Muff in this regard.

Note decay shape: gated/bit-crushed tail at high Sustain settings, where the sustain runs out and the circuit clamps. This is part of the charm for the user's degradation aesthetic — the decay is not smooth, it has a "ripping speaker on the way out" character.

## 5. Signal Chain Placement (Board 1 specifics)

The user's order is `VG-800 → Polytune → CB Clean → Colour Box V2 → MXR 108 → Hizumitas → Brothers AM → Longsword → Oxford → BF-3 → Somersault → CE-2W → Deco`. A few observations for this exact configuration:

- **CB Clean upstream is fine** — and arguably correct. With 150kΩ input impedance, the Hizumitas is happier seeing a buffered, low-impedance source than a Fuzz Face is. EQD's official guidance ([general note in their FAQs and repeated in reviews](https://www.earthquakerdevices.com/hizumitas)) is that the Hizumitas tolerates buffers in front far better than a vintage-style fuzz. Real-world: you should not hear the thinning that the 108 will exhibit when fed by a buffer.
- **108 immediately upstream is the unusual choice.** A silicon Fuzz Face into a Muff-derivative is a classic recipe but normally the Muff goes *first* (because Muffs are more buffer-tolerant) and the FF goes second. Inverted here, the 108 is essentially acting as a gated, splatty pre-stage that the Hizumitas will smooth out into a sustained wall. That works — but expect the 108 to behave erratically because the Colour Box's buffer is in front of it. If the 108 sounds thin, swap their positions (Hizumitas before 108). The Hizumitas will sound great into the 108's input.
- **Brothers AM downstream as drive platform** — this is the right architecture. Brothers used as a clean-ish boost/EQ shaper after the Hizumitas will tighten the low end and let you sculpt the upper mids that the Hizumitas's Tone control can't quite reach. Run Brothers Channel A clean-ish, Channel B with a small amount of breakup, blend.
- **Longsword after Hizumitas:** stacking high-gain distortion after a Muff is destructive but in a good way. Expect the Longsword to over-saturate; back its gain off significantly (8–10 o'clock max) and use it as a tone-shaping stage rather than additional gain. The Hizumitas already has enough.
- **Oxford after both:** the Oxford's mid character will be doing nothing useful at this point in the chain; consider it a "kill switch for nuance" that turns the whole front-end into a single brick. Useful as a one-button intensifier, not as a tone shaper here.
- **Time/modulation downstream is correct** — BF-3, Somersault, CE-2W, Deco all want a stable, line-level source, which is exactly what the Hizumitas delivers.

## 6. Bright Transient Sources (banjo, baritone)

This is where the Hizumitas earns its slot. The combination of a Roland GK-5-equipped Gold Tone EBM-5 banjo into a VG-800 produces extremely bright, extremely transient signal with very little natural low-end mass. Most Muffs respond to this by amplifying the high-frequency content and turning into ice-pick noise. The Hizumitas has two specific advantages:

1. **The Tone knob's clockwise sweep** is unusually effective at darkening the signal because of the 3n3 HPF cap — it can take a banjo's piercing 2–4kHz content and roll it into the kind of low-mid wall the user is after. Reviewers consistently note this as the pedal's "synth filter" character; for a banjo player it's the difference between a usable fuzz and an unusable one.
2. **The compression/sustain behavior** evens out banjo's notorious attack/decay imbalance. Banjos have very fast attack and very fast decay; the Hizumitas's gentle compression slows the attack curve and the sustain extends the decay, producing notes that behave more like guitar notes.

Practical settings starting point for the banjo: Tone at **1–2 o'clock** (well past noon, into the bass-boost side), Sustain at noon, Volume at 11. If the banjo is still too bright, run the VG-800 with a darker amp model (Tweed or AC-style, treble pulled back) feeding the Hizumitas.

For the baritone Jazzmaster, this is closer to the Hizumitas's home territory. Less Tone-knob compensation needed; noon to 1 o'clock works.

Pickup type doesn't matter as much as input level. The Hizumitas responds well to both single coils and humbuckers per [Guitar Player](https://www.guitarplayer.com/reviews/earthquaker-devices-hizumitas-fuzz-sustainer-review), but it gets noticeably more aggressive with hotter pickups. The GK-5's per-string output is medium-hot; expect Sustain at 10–11 o'clock to feel like a higher setting than it would with a passive Jazzmaster.

## 7. Digital Modeling Sources (VG-800)

There is no published documentation specifically about the Hizumitas with Roland VG-800 or other modelers, so this is inference from circuit behavior:

- **Modeled amp signals:** The Hizumitas will treat a VG-800 amp model the same way it treats any line-level guitar signal — it'll fuzz the modeled cab IR. This is destructive if you wanted clean modeled tones; for the user's aesthetic, it's useful, because you can get unholy textures by fuzzing an already-saturated modeled amp.
- **Synth/COSM patches:** When the VG-800 outputs synth-modeled signal (pad, organ, GR-style synth) the Hizumitas will track it as long as the synth output is a continuous waveform. Expect: pad patches turn into massive distorted drones (good for the user's drone aesthetic), polyphonic guitar-synth patches will artifact heavily because the Muff topology doesn't deal well with multiple simultaneous fundamentals. **This is a feature, not a bug, for the user's "broken/recorded-wrong" preference.**
- **Latency:** None added by the Hizumitas (it's all-analog). VG-800 latency is unaffected.
- **GK divided signal:** The Hizumitas sits after the VG-800's summed output, so the hex separation is already collapsed by the time the fuzz sees it. If the user ever wants per-string fuzz, that would require a different topology entirely.

## 8. Famous Users

The honest answer is that the Hizumitas's discography is **Wata's discography**. She has [replaced her Elk on the touring board with the Hizumitas](https://www.musicradar.com/news/wata-boris-earthquaker-devices-pedalboard), telling [Guitar World](https://www.guitarworld.com/features/wata-boris-eqd-hizumitas) directly: *"The Hizumitas is not inferior to my ELK when I A/B them."* Anything Boris releases from 2022 onward where her main fuzz wall is audible is likely the Hizumitas; older recordings ("Feedbacker" from *Boris at Last - Feedbacker* is the song she explicitly cites in the Guitar World piece) are the original Elk.

Beyond Boris, the pedal is too new to have a developed user mythology — it landed in late 2021. It shows up on shoegaze/doom boards (you'll see it on Reverb listings from doom-adjacent acts and on a lot of post-rock pedalboards) but no other artist has claimed it as a signature voice the way Wata has.

## 9. Live Performance Notes

- **Bypass:** Relay-based true bypass switching per [EQD spec page](https://www.earthquakerdevices.com/hizumitas). Requires power to pass signal — if power dies, the signal dies. Important for live: do not assume the Hizumitas will pass signal at all if the power supply fails.
- **Power:** 9V DC center-negative, standard 2.1mm barrel. **10 mA current draw** — trivially low, any isolated supply slot will handle it.
- **Do not run above 9V.** EQD explicitly warns against it. No 18V trick here.
- **Noise floor:** Quiet for a high-gain Muff. The mid-forward voicing helps because there's less hiss-band content than a scooped Muff. Not gate-required for most settings.
- **Feedback behavior:** Sustains feedback well into amp distance. The compression character keeps controlled feedback from running away — it's predictable, which is unusual for a high-gain fuzz.
- **Dimensions:** 4.75 x 2.50 x 2.25 in. (121 x 64 x 57 mm) with knobs. Standard EQD enclosure. Pedalboard real estate: small.

## 10. Pairing Recommendations

**Before the Hizumitas (boost/octave/filter):**
- A clean boost upstream pushes Sustain harder without raising the noise floor. The user's CB Clean already does this. An octave-up before would be aggressive and ring-modulated (the Muff topology doesn't preserve octave fundamentals cleanly). Octave-down before is more reliable.
- Envelope filter before: works, but the Hizumitas's heavy compression flattens the envelope's dynamic response. Better after.

**After the Hizumitas (time/space):**
- **Long modulated delays** are the canonical pairing. The Hizumitas's sustain gives the delay something to chew on, and the slow modulation breathes life into the sustained wall. CE-2W's chorus into the Deco's tape sim, both downstream, is exactly the right architecture for this.
- **Hall/shimmer reverbs:** Hizumitas + shimmer is a textbook drone-doom recipe. For the user's End Board, **H90** algorithms like CrushedHall, BlackHole, MangledVerb pair extremely well — the sustained fuzz wall gives the reverb a stable input to spectrally process.
- **Granular / glitch:** The Microcosm and Chroma Console will eat sustained Hizumitas signal beautifully. The sustain makes granular sampling sound intentional rather than choppy. The Mood (V1 or II) with mod looper running against sustained Hizumitas chords is a documented Wata-adjacent technique.
- **Blooper (Chase Bliss):** Capture a Hizumitas drone and layer modulations — this is the user's stated aesthetic and the Hizumitas is the right sustained source for it.
- **Big Time / extended delay:** Long delay times work because the Hizumitas's tail is dense enough that delay repeats don't compete with the dry signal — they blend.

## 11. Reviews and Demos

- [Premier Guitar review](https://www.premierguitar.com/gear/reviews/earthquaker-devices-hizumitas) — 4.2/5. Most useful written review; explicitly addresses the synth-filter Tone behavior.
- [Guitar Player review](https://www.guitarplayer.com/reviews/earthquaker-devices-hizumitas-fuzz-sustainer-review) — best on dynamic response and pickup interaction.
- [Mixdown Magazine review](https://mixdownmag.com.au/reviews/review-earthquaker-devices-hizumitas-fuzz-sustainar/) — best on bass guitar use and recording context.
- [EQD's official noodler settings guide](https://www.earthquakerdevices.com/blog-posts/hizumitas-for-noodlers) — start here for knob-position reference.
- [EQD's Wata development blog](https://www.earthquakerdevices.com/blog-posts/wata-elk-big-muff-sustainar-and-hizumitas) — only source for the 2.5/7.5 fuzz/distortion ratio framing.
- [Guitar World Wata interview](https://www.guitarworld.com/features/wata-boris-eqd-hizumitas) — Wata's own A/B verdict, plus her stacking philosophy ("I often use the Hizumitas with a distortion to create more chaotic feel").
- [Reverb — Hizumitas "Tone Report Demo"](https://www.youtube.com/watch?v=qe2o8xfNAzI) — competent dry demo (Andy presenting; hosted on **Reverb's** channel, 2021-11-04 — verified via yt-dlp).
- [We As A Company — Hizumitas vs Triangle Big Muff (+ Boss DS-1), "Sound like Boris"](https://www.youtube.com/watch?v=rTv3vANd65g) — side-by-side that makes the mid-forward character audible; also demos the **Hizumitas + DS-1 stack** for the Boris wall (channel + DS-1 angle verified via yt-dlp).
- [MusicRadar pedalboard tour video](https://www.musicradar.com/news/wata-boris-earthquaker-devices-pedalboard) — Wata's actual touring board with the Hizumitas in context.

## 12. Mods, Quirks, Known Issues

- **The 3n3 tone cap is the obvious mod target.** Swap to 330pF and you have a much closer Elk-faithful build. Swap to something between (e.g. 1nF) for less aggressive low-end swing if you find the clockwise side too dark for your source. This is not officially supported but it's a single-cap swap.
- **No volume-knob attenuation on the bypass side** — relay bypass means even when off, signal is routed through the switching circuit. Quality is fine; just relevant for the rare case of total-power loss on stage.
- **The Tone knob is touch-sensitive.** Small movements have large effects. This bites people who try to dial it in by feel without watching the knob.
- **It does not gate aggressively.** Some users expect a Muff-style noise gate; the Hizumitas doesn't have one. If you need silence between notes, use the BF-3's noise suppression or add a gate.
- No widely reported failures; build quality is standard EQD, which is among the best in the boutique-mass-production tier.

## 13. Spec Sheet

| Spec | Value |
|---|---|
| Power | 9V DC, center-negative, 2.1mm barrel |
| Current draw | 10 mA |
| Max voltage | 9V (do not exceed) |
| Bypass | Relay-based true bypass; requires power to pass signal |
| Input impedance | ~150 kΩ |
| Output impedance | <10 kΩ |
| Signal path | All analog |
| Dimensions | 4.75 x 2.50 x 2.25 in (121 x 64 x 57 mm) with knobs |
| Controls | Volume, Sustain, Tone |
| MIDI | None |
| Warranty | Lifetime (EQD standard) |

Source: [EQD Hizumitas product page](https://www.earthquakerdevices.com/hizumitas).

## 14. Starting-Point Settings

Reference points for day one. Knob positions are clock-face, looking at the pedal from above.

**(a) Doom wall** — sustained, oceanic, single-chord forever
- Volume: 12
- Sustain: 2
- Tone: 2 (bass-boosted side)
- Pair with: long hall verb after, slow chorus before reverb. Use neck pickup, let it ring.

**(b) Sustain pad** — single-note leads that breathe
- Volume: 11
- Sustain: 1
- Tone: 12 (neutral)
- Pair with: modulated delay after. Use volume knob on the instrument to swell into notes.

**(c) Controlled crunch / edge-of-breakup** — rhythm, articulate, mid-forward
- Volume: 11
- Sustain: 9
- Tone: 11 (slightly treble-side of noon)
- Roll the instrument volume to 7–8 to clean further. Works for chord stabs and palm-muted parts.

**(d) Max chaos / runaway** — broken, gated, ripping
- Volume: 2
- Sustain: 5 (maxed)
- Tone: 10 (treble side)
- Pair with: Brothers AM clean channel as boost, granular reverb downstream. Expect feedback; control it with proximity to amp.

## 15. Versus Direct Competitors

- **Wren and Cuff Tri Pie '70** — the closest topological cousin and the most defensible alternative. Tri Pie '70 is faithful to the 1970 Triangle. Reach for it if you want a more "classical" Muff voicing; reach for the Hizumitas if you want the Elk's more aggressive tone-stack swing and tighter low end. The Hizumitas is the more *aesthetically distinct* pedal of the two; the Tri Pie is the more *historically pure*.
- **Wren and Cuff White Elk** — actual Elk clone, $199, more faithful to the original circuit. If absolute Elk fidelity matters, this is the answer. The Hizumitas is voiced *for Wata's specific reference unit* and is the better choice if you want her tone rather than a generic Elk.
- **Stone Deaf PDF-1** — different beast entirely (parametric distortion with sweepable mid). Adjacent only in that it offers Muff-ish heaviness with EQ flexibility. Reach for the PDF-1 if you want surgical mid control; the Hizumitas if you want the synth-filter Tone behavior and the Elk character.
- **JHS Muffuletta** — six Muff voicings in one box. The Civil War mode is the closest match to Hizumitas territory but the Muffuletta is voiced safer across all six modes. Reach for the Muffuletta if you want variety; reach for the Hizumitas if you want a single specific character delivered better.
- **Vick Audio Tree of Life** — Triangle-derived, well-regarded, cheaper. Brighter, less low-end shove than Hizumitas. Reach for the Tree of Life on a budget; reach for the Hizumitas when you specifically need the mid-forward Elk voicing.

In the user's rig — banjo and baritone, drone/doom/shoegaze aesthetic, Brothers AM as drive platform downstream — the Hizumitas is the right call over all of these competitors specifically because of (1) the Tone knob's ability to tame banjo brightness, (2) the mid-forward voicing that survives the dense downstream chain, and (3) the sustain behavior that gives the End Board's granular/reverb pedals something musical to chew on.

## Sources

- [EarthQuaker Devices — Hizumitas product page](https://www.earthquakerdevices.com/hizumitas)
- [EarthQuaker Devices — About Wata's ELK Big Muff Sustainar and Hizumitas](https://www.earthquakerdevices.com/blog-posts/wata-elk-big-muff-sustainar-and-hizumitas)
- [EarthQuaker Devices — Hizumitas For Noodlers And Fuzz Freshman](https://www.earthquakerdevices.com/blog-posts/hizumitas-for-noodlers)
- [Premier Guitar — EarthQuaker Devices Hizumitas Review](https://www.premierguitar.com/gear/reviews/earthquaker-devices-hizumitas)
- [Guitar Player — Hizumitas Fuzz Sustainer Review](https://www.guitarplayer.com/reviews/earthquaker-devices-hizumitas-fuzz-sustainer-review)
- [Mixdown Magazine — Hizumitas Review](https://mixdownmag.com.au/reviews/review-earthquaker-devices-hizumitas-fuzz-sustainar/)
- [Guitar Pedal X — Hizumitas / Elk BM Sustainar lineage writeup](https://www.guitarpedalx.com/news/news/earthquaker-devices-teams-up-with-wata-of-boris-for-her-signature-hizumitas-fuzz-sustainar---based-on-the-legendary-fierce-elk-bm-sustainar-triangle-muff-clone-with-unique-tone-stack)
- [Guitar World — Wata interview on the Hizumitas](https://www.guitarworld.com/features/wata-boris-eqd-hizumitas)
- [MusicRadar — Wata's pedalboard tour](https://www.musicradar.com/news/wata-boris-earthquaker-devices-pedalboard)
- [vero-p2p.blogspot.com — Hizumitas schematic detective post (3n3 cap analysis)](https://vero-p2p.blogspot.com/2022/01/earthquaker-devices-hizumitas-schematic.html)
- [Equipboard — ELK Big Muff Sustainar reference page](https://equipboard.com/items/elk-big-muff-sustainar)
- [PedalPCB Forum — Elk Super Fuzz Sustainar discussion](https://forum.pedalpcb.com/threads/elk-super-fuzz-sustainar-japanese-big-muff-clone.26972/)
- [Super-Freq — Wata's Electro Sound Big Muff context](http://www.super-freq.com/watas-electro-sound-big-muff/)
- [Wren and Cuff — Tri Pie '70 product page](https://www.wrenandcuff.com/products/tri-pie-70)
- [Tone Report Hizumitas YouTube demo](https://www.youtube.com/watch?v=qe2o8xfNAzI)
- [Hizumitas vs Triangle Big Muff YouTube comparison](https://www.youtube.com/watch?v=rTv3vANd65g)
