# Chase Bliss Big Time — Deep Research

A working dossier for the **Big Time** as it lives 2nd on Board 3 (End / Time → Tape), wedged between the Generation Loss and the MOOD MkII — the primary delay of the End Board and the rig's designated live delay workhorse. This is not the "stereo dotted-eighth machine" the marketing leans on; in this rig it's the saturating, self-disintegrating hybrid echo that takes an already-degraded stereo wash and either smears it into ambient haze or rips it into harmonic chaos. Most of this document is about how it behaves *after* a Generation Loss, *into* a MOOD/Blooper/Chroma/H90 stack, and *under* one MIDI clock shared with a board full of Chase Bliss pedals.

## 1. Lineage: what it actually is

The Big Time is a **Chase Bliss × Electronic Audio Experiments hybrid analog/digital delay** in the **Automatone** auto-slider format — co-designed with **John Snyder of EAE**. It was announced late April 2026, priced **$999 USD / €1,099 EU** (Chase Bliss's most expensive pedal to date), with first units shipping **June 2026** ([Chase Bliss product page](https://www.chasebliss.com/big-time), [gearnews](https://www.gearnews.com/chase-bliss-big-time/), [EAE blog](https://www.electronicaudioexperiments.com/blog/2026/4/29/big-time)). The owned manual's cover code is **"CBA+EAE ref 2026 – BT001"** ([Big Time Field Guide](manuals/Big+Time_Manual_Chase+Bliss.pdf)), which confirms the exact unit.

The concept, per the manual's Overview, is "an exploration of the mixed-up circuitry found in rackmount delays from the early 80s," where digital was "in its infancy... it needed help, so analog circuitry made up the difference — instead of digital or analog, you got both" ([manual p.4](manuals/Big+Time_Manual_Chase+Bliss.pdf)). It has **two separate sources of analog coloration: an analog preamp at the input, and a clipping limiter inside the feedback loop**. EAE's John Snyder names the specific reference units in his [development blog](https://www.electronicaudioexperiments.com/blog/2026/4/29/big-time): the **Lexicon PCM42** (whose mis-calibrated limiter inspired Big Time's Compressed/"Blue Mode" state) and the **Ursa Major Space Station** (which inspired the Cluster slider). He also notes it carries circuit blocks from prior EAE pedals — **Sending, Clean, Halberd, Glaive** — and "is partly a love letter to my old circuit-bent PDS 20/20."

> **Manual-vs-web flag.** Several news outlets ([gearnews](https://www.gearnews.com/chase-bliss-big-time/), aggregators) cite the **Lexicon PCM 70 and Korg SDD-3000** as inspirations. The **manual does not name specific units**, and EAE's own blog names the **PCM42 and Ursa Major Space Station**. Treat the PCM70/SDD-3000 attributions as journalist framing; the PCM42 + Space Station lineage is first-party.

Relation to Chase Bliss's other delays: GuitarPedalX hears "elements of **Tonal Recall and Thermae** in here (albeit not the BBDs!)" ([GPX writeup](https://www.guitarpedalx.com/news/gpx-blog/chase-bliss-rolls-out-another-interesting-variant-of-its-automatone-auto-slider-format-the-big-time-hybrid-echo-delay-in-collaboration-with-eaes-john-snyder)). The Thermae DNA is most audible in the pitched/sequenced **SCALE** behavior; the Tonal Recall DNA in the warm, analog-voiced repeats. Unlike Thermae/Tonal Recall, Big Time is **fully digital at its core** (32-bit / 48kHz, [spec sheet p.46](manuals/Big+Time_Manual_Chase+Bliss.pdf)) with the analog character living in the preamp and feedback limiter rather than a BBD line. It is the format sibling of the **Preamp MkII** and **MOOD MkII** — same Automatone slider chassis, no screen.

## 2. Controls, buttons, and Alt menu

**Six faders** (manual p.12):
- **COLOR** — gain of the analog preamp. Two things happen as it rises: the preamp saturates, and the limiter's effects intensify *instantly*. This is the single most important control for the rig's aesthetic — it sets how hard the signal bumps into the limiter inside the delay line.
- **TIME** — clock control for delay time. Interacts with **MODE** (range) and **SCALE** (smooth vs. musical steps). Snaps to center when tap tempo is used or a loop is deleted, so you can speed up/slow down by equal amounts and find the original speed again.
- **CLUSTER** — gradually blends in additional delay taps and diffusion (modeled on the Ursa Major Space Station). Also one of Big Time's generators of stereo image.
- **TILT EQ** — splits the spectrum in half; push up to cut lows, down to cut highs. Noon = no effect. The **CROSSOVER** alt control sets the pivot point.
- **FEEDBACK** — gain of the feedback loop. More repeats, and the limiter intensifies over time.
- **WET** — output loudness of the effect. *Pull WET all the way down to turn Big Time into a standalone stereo analog preamp* (manual p.24).

**Five buttons** (manual p.14):
- **SCALE** — how TIME and MOTION respond: smooth, or in tuned steps. Cycles **Chromatic / Oct+4+5 / Octave** (manual p.30). Off = a normal pitch-detuning delay.
- **MOTION** — turns on modulation and selects type: **Sine** (smooth), **Square** (choppy/atonal), **Env** (envelope-controlled time bends). Hold 2s to reset to a pleasing default. DEPTH/RATE alt controls shape it.
- **MODE** — sets delay range *and* footswitch behavior: **Mod / Short / Long / Loop**. Hold 2s to reset to a simple delay.
- **VOICING** — core tone character, independent of TILT EQ. Cycles **HiFi / Focus / Warm / Analog** fixed-filter arrangements (manual p.38).
- **STATE** — sets the limiter's role: **Digital / Compressed / Saturated / #!&%** (misbias). The **TEXTURE** alt control tunes each (manual p.34).

**Two footswitches** (manual p.16) — TEMPO (left) and BYPASS (right), with behavior that changes per MODE (tap tempo, record/play, motion toggle, hold/overload/delete, preset menu access).

**Alt menu** (hold SHIFT, manual p.18) exposes six alt faders — **TEXTURE, RATE, DEPTH, CROSSOVER, DIFFUSE, DRY** — plus four alt buttons: **SPREAD** (stereo: off = subtle widening, on = ping-pong), **0.5X** (drops bit depth 32→12 and halves sample rate for early-80s lo-fi), **DIFFUSE TYPE**, and **+12dB** (extra preamp gain for quiet inputs).

**Options menu** (tap both footswitches, manual p.40) holds the global prefs that matter for this rig: **SCALE IGNORE** (let MOTION stay smooth while TIME does scaled transposition), **TRAILS** (echoes fade after bypass), **DRY KILL** (remove dry — important; see §5), **DRY CLEAN** (dry bypasses the preamp), and **BALANCED/UNBALANCED** I/O.

## 3. Sonic character: clean → tape/lo-fi → ambient/self-osc

Big Time is loudness-driven. The whole pedal is "all about loudness, controlled by three interconnected faders" — COLOR (preamp in), FEEDBACK (loudness within the loop), WET (out) (manual p.10). The defining behavior: **with each repeat, the digital echo collides with the analog limiter and takes on more analog character**. *How* it degrades is the STATE button's job.

- **Clean / HiFi:** STATE = Digital removes the limiter entirely — clean, stable, steady repeats. With VOICING = HiFi this is the closest Big Time gets to a transparent stereo digital delay. Good for steady ambient beds you don't want to disintegrate.
- **Tape / lo-fi:** STATE = Saturated (its "default state," per manual p.35) + VOICING = Warm or Analog + the **0.5X** alt button = murky, modulated, bit-reduced echoes that crumble — the "Crushed Analog" factory voice. This is the rig's bread-and-butter setting, designed to feed a tape-print board.
- **Ambient / self-oscillating:** FEEDBACK above COLOR makes echoes "gradually climb... until they encounter the limiter and begin to transform into a maximum loudness" (manual p.25). Crank DIFFUSE + CLUSTER in LONG mode for "long-form ambient haze." STATE = #!&% (misbias) gives "raw, electric... broken and obliterated soundscapes."

VOICING shapes the base tone independent of TILT EQ (manual p.38): **HiFi** clear/pure; **Focus** "shaves both highs and lows over time to create focused floating repeats"; **Warm** "emulates the filtering techniques of primitive digital rack delays, with their signature elliptical ripple"; **Analog** "dark and rich... BBD-based analog delay."

## 4. Behavioral notes: self-oscillation, ramping, holds, stereo

- **Self-oscillation / runaway:** Not a clean sine runaway — Big Time *transforms into the limiter*. High FEEDBACK + low COLOR makes a slowly-climbing wall that "can be real loud and scary if you're not expecting it" (manual p.25). The limiter is what keeps it from a digital scream; it clips and mangles instead.
- **OVERLOAD ramp:** In Long mode, **HOLD RIGHT ramps both COLOR and FEEDBACK to max** ("beware volume levels!") — a performative one-stomp swell into chaos (manual p.16/26).
- **HOLD (infinite):** HOLD RIGHT in Short/Long "loops and preserves the current sound infinitely. You can play overtop without being recorded" (manual p.16) — a sustain pad you solo over.
- **Tap-tempo snap:** TIME snaps to center on tap so you can warp speed and return to the tapped value (manual p.17). This matters live when slaving to MIDI clock (see §8).
- **Stereo:** Big Time is a **true stereo device**. **SPREAD** off = subtle widening; on = **ping-pong** for wide panning echoes. **CLUSTER** also generates stereo image — "bump it up if your stereo field is feeling narrow" (manual p.36). Three I/O configs: mono, full stereo, or **MISO** (mono in / stereo out, auto-engaged when only IN L is used).

## 5. Signal-chain placement — the End-Board delay

In this rig Big Time sits: `…Dark Star V3 (stereo) → CB Generation Loss → **CB Big Time** → CB MOOD MkII → CB Blooper → Chroma Console → Eventide H90 → PORTA424 → JHS 424 → Apollo/FOH`. It's the **second pedal on Board 3** and the **primary, always-available delay**.

- **After Generation Loss (correct):** Generation Loss already degrades and warbles the stereo signal (VHS-style). Feeding that into Big Time means the delay's *repeats* inherit pre-broken source material, and Big Time's own limiter/0.5X bit-crush then re-degrades the repeats on top. This is the rig's "degraded-then-re-degraded" aesthetic in two boxes. Keep COLOR moderate here — the source is already saturated, so a little preamp gain goes a long way before the limiter gets ugly.
- **Stereo integrity:** Both Generation Loss and Big Time are true-stereo, so the L/R image from the CE-2W split (Board 1) is preserved through the delay. Use **SPREAD = ping-pong** sparingly — there are five more stereo pedals downstream that will smear the panning anyway.
- **DRY routing:** Because Big Time has an **analog dry-thru** and the downstream MOOD/Chroma/H90 will each re-process the dry+wet, decide *per patch* whether Big Time's dry should pass. For pure ambient washes, consider **DRY KILL** (Options menu) so Big Time outputs only wet repeats and the dry stays clean upstream — prevents the dry from being preamp-colored four times over before tape.

**Labor division by name on the End Board:**
- **Big Time** = the *primary musical delay* — rhythmic repeats, dotted-eighth, sequenced/pitched echoes, the saturating ambient wash. It is the "front of house" delay.
- **MOOD MkII** (right after) = micro-looping / time-warp / loop-mangling — Big Time's repeats become MOOD's micro-loop source. Big Time makes the echo; MOOD captures and warps a slice of it.
- **Blooper** = full song-length looping + collaged modifiers — the *composition* layer, not a delay. Capture a Big Time phrase and stack.
- **H90** = the *second delay engine* and the reverb engine — algorithmic/reverse/shimmer delays Big Time can't do, plus all reverb. The two delays split duties (see §9, §14).
- **Chroma Console** = post-delay texture/character (tape, drive, filter) before tape print.

Big Time *can* loop (variable-length, up to 3.2 min), but with Blooper, MOOD, and the OP-1/Octatrack/Onward-class samplers in the room, its looper is best used as a **performative phrase-freeze** mid-song, not the main looper.

## 6. Source-specific behavior

- **Baritone Jazzmaster (magnetic + GK-5 → VG-800):** Big Time sees the *summed, modeled, already-effected stereo* signal at the very end of the chain, not the raw guitar. Low-string baritone content benefits from **TILT EQ pushed up slightly to cut mud** out of the repeats (manual p.39 explicitly suggests "cut the mud from your bass"). Warm/Analog voicing flatters the dark baritone tone.
- **EBM-5 banjo (GK-5 → VG-800):** The banjo's fast, bright transients are perfect fuel for **MOTION = Env** (envelope-controlled time bends) and **SCALE = Octave/Oct+4+5** sequencing — pluck a banjo line and let Big Time pitch-step it into a Thermae-style arpeggiated cascade. This is the "banjo-as-lead" use case: the repeats do the melodic work.
- **VG-800 modeled/synth patches:** Pad and synth COSM patches sustain, so they sit beautifully under HOLD/infinite feedback and DIFFUSE for drones. Polyphonic guitar-synth feeds the SCALE pitch-stepping cleanly because the source is already a stable waveform.
- **Bass (Jazz bass) / SG / Jazzmaster (non-GK):** These enter upstream of the VG-800 chain or via other routing; by the time they reach Big Time they're line-level stereo. **DRY CLEAN** (dry bypasses preamp) keeps a clean bass fundamental while only the repeats saturate — useful if Big Time is ever used on bass-forward material.

> No published source documents Big Time with banjo, GK-5, or VG-800 specifically — the above is inference from the manual's control behavior plus the rig's signal flow.

## 7. Famous users (honest)

The pedal shipped in **June 2026**, so there is **no developed artist mythology yet**. What's verifiable: it was co-designed by **John Snyder (EAE)** with Chase Bliss (Joel Korte, "Knobs," and engineer Charlie); the foreword is signed by Snyder ([manual p.3](manuals/Big+Time_Manual_Chase+Bliss.pdf)). Early reception is review/demo-driven rather than artist-driven (see §10). Given Chase Bliss's customer base, expect it to surface on ambient/experimental, post-rock, and drone/shoegaze boards — exactly this rig's lane — but **do not attribute it to any specific famous player; none is confirmed.**

## 8. Live, power, and I/O

- **Power:** **9V DC center-negative, ~1A (400mA nominal, 1A for startup surge / large slider movements)**. Higher than 9V risks damage. It ships with a high-amperage 9V brick **and a current-doubling merger cable** to combine two 500mA outputs on an existing supply (manual p.6). This is the practical headache: on a board already feeding many Chase Bliss pedals, Big Time alone wants its own ~1A — plan the power supply accordingly.
- **I/O:** True stereo, two ins / two outs, **TRS balanced or unbalanced** (selectable, Options menu). 1MΩ input (single-ended), 50Ω output. **Analog dry-thru, true bypass.** TRAILS optional (Options menu).
- **MIDI:** **5-pin MIDI IN and THRU.** "Every aspect of Big Time can be controlled via MIDI, including syncing to an external clock. You also have the option to **output Big Time's own clock**, letting you sync other devices to your loops and echoes" (manual p.42). This is the keystone for this rig — see below.
- **CV / Expression / AUX:** CV range 0–5V; expression or CV can control any/all faders with chosen range and direction; any normally-open momentary footswitch (e.g. Boss FS-6) into AUX for Preset/Fun/Desktop remote modes (manual p.42).
- **Presets:** **10 internal, 127 via MIDI.** Preset menu reachable in every mode via the same footswitch gesture — usable as a performance warp tool.

**MIDI clock in this rig:** With a board of MIDI-capable Chase Bliss pedals (Generation Loss, MOOD MkII, Blooper) plus Microcosm, Chroma Console, and H90, Big Time should **slave to one master MIDI clock** so its TIME divisions lock to the rig tempo and the looper/sequence stays in time. Alternatively, Big Time can be the **clock master** and feed everything else — useful when its sequenced SCALE/MOTION patterns drive the groove. Pick one master; don't loop clock. (Detailed CC/PC mapping is in the separate [Big Time MIDI Manual](https://www.chasebliss.com/s/Big-Time_MIDI-Manual_Chase-Bliss.pdf), not the field guide.)

## 9. Pairing recommendations (by name)

- **After Generation Loss (upstream):** Let GenLoss do the wow/flutter and HF roll-off; keep Big Time's COLOR modest so you're not double-saturating into harshness. Use Big Time's VOICING = Warm to complement GenLoss's tape character without fighting it.
- **Into MOOD MkII (downstream):** Big Time's infinite-HOLD or a synced repeat makes ideal raw material for MOOD's micro-loop/time-warp. Run Big Time rhythmic, MOOD as the glitch/stutter on top.
- **Into Blooper (downstream):** Freeze or sequence a Big Time phrase, then commit it to Blooper for song-length layering with modifiers.
- **Into Chroma Console (downstream):** Chroma's tape/character modules re-color Big Time's already-degraded repeats just before print — stack degradation deliberately, not accidentally.
- **With H90 (downstream):** Divide labor. Big Time = analog-voiced, self-degrading rhythmic/ambient delay; H90 = reverse, shimmer, pitched, algorithmic delays **and** all reverb (Blackhole, etc.). Run Big Time's wet into an H90 reverb for the classic "saturated echo into a huge space" doom recipe.
- **Vs the benched Strymon TimeLine:** see §14 — the rig sheet's "Big Time + H90 delays cover the live needs" is the explicit reason TimeLine is off-board.

## 10. Reviews and demos (real links)

- [Chase Bliss — Big Time product page](https://www.chasebliss.com/big-time) — first-party specs, $999, June 2026 ship.
- [Electronic Audio Experiments — Big Time blog (John Snyder)](https://www.electronicaudioexperiments.com/blog/2026/4/29/big-time) — the only first-party source for the PCM42 / Ursa Major Space Station / EAE-circuit-block lineage.
- [gearnews — "The Ultimate '80s Voiced Rack Delay Pedal?"](https://www.gearnews.com/chase-bliss-big-time/) — best on the four modes, 3.2-min looping, fader layout.
- [GuitarPedalX — Automatone-format Big Time writeup (Stefan Karlsson)](https://www.guitarpedalx.com/news/gpx-blog/chase-bliss-rolls-out-another-interesting-variant-of-its-automatone-auto-slider-format-the-big-time-hybrid-echo-delay-in-collaboration-with-eaes-john-snyder) — best on Thermae/Tonal-Recall lineage and Automatone-format critique; calls it "a nice-to-have rather than a must-have."
- [Sonicstate — Big Time announcement](https://sonicstate.com/news/2026/05/01/big-time-from-chase-bliss-/) — concise overview.
- [Guitar Bomb — "The 'Big Time' Has Arrived"](https://guitarbomb.com/chase-bliss-big-time/) — launch coverage, EAE collaboration framing.
- [Chase Bliss × EAE — BIG TIME Full Demo (YouTube, stereo)](https://www.youtube.com/watch?v=cHQzpkalwS0) — the official stereo demo; hear the Compressed/Saturated/misbias states in motion.
- [Elektronauts thread](https://www.elektronauts.com/t/chase-bliss-effects-pedals/31096) and [The Gear Forum thread](https://thegearforum.com/threads/chase-bliss-big-time-collab-with-eae.11307/) — owner/early-adopter discussion.

## 11. Mods, quirks, firmware

- **No mods / no schematic published** (it's a 2026 digital pedal). The "mod" surface is firmware + the deep Alt/Options menus, not soldering.
- **Quirk — the Automatone format has no screen.** Reviewers note the slider format "serves the preamp well" but a delay this deep "could probably do with some sort of screen" ([GPX](https://www.guitarpedalx.com/news/gpx-blog/chase-bliss-rolls-out-another-interesting-variant-of-its-automatone-auto-slider-format-the-big-time-hybrid-echo-delay-in-collaboration-with-eaes-john-snyder)). Motorized faders recall saved positions, which mitigates this, but deep editing is gesture-driven.
- **Quirk — loud surprises.** The low-COLOR / high-FEEDBACK climb and the OVERLOAD ramp can spike output hard (manual warns twice). Set WET conservatively before tape print.
- **Quirk — power-hungry (~1A).** Plan supply headroom; the included current-doubler exists for a reason.
- **Quirk — Loop mode switches to digital feedback behind the scenes**, so STATE/TEXTURE changes aren't heard until you overdub again (manual p.29). For stable traditional looping use the Digital state.
- **Firmware:** none documented beyond ship firmware as of June 2026; Chase Bliss historically ships updates — watch their site.

## 12. Spec sheet

| Spec | Value |
|---|---|
| Type | Hybrid analog/digital stereo delay (Automatone format) |
| Designers | Chase Bliss × Electronic Audio Experiments (John Snyder) |
| Processing | 32-bit, 48kHz A/D |
| Modes | Mod (3–46 ms), Short (46–736 ms), Long (736 ms–12.2 s), Loop (variable; up to 3.2 min @ ~11kHz, 48s @ 44kHz, 12s @ 172kHz) |
| States (limiter) | Digital, Compressed, Saturated, #!&% (misbias) |
| Voicings | HiFi, Focus, Warm, Analog |
| Motion | Sine, Square, Env (DEPTH/RATE alt) |
| Scales | Off, Chromatic, Oct+4+5, Octave |
| Faders | Color, Time, Cluster, Tilt EQ, Feedback, Wet (+ alt: Texture, Rate, Depth, Crossover, Diffuse, Dry) |
| Stereo | True stereo; mono / stereo / MISO; SPREAD widening + ping-pong |
| I/O | 2 in / 2 out, TRS balanced or unbalanced (selectable) |
| Input / Output Z | 1 MΩ single-ended (20kΩ balanced) / 50 Ω |
| Dry path | Analog dry-thru, true bypass; optional Trails |
| Preamp gain | 0 to +20dB, or +12 to +32dB (+12dB mode) |
| Noise | Dry path −100dBV; delay path −94dBV |
| MIDI | 5-pin IN + THRU; clock in/out, PC, CC |
| Control | CV (0–5V), expression, AUX footswitch |
| Presets | 10 internal, 127 via MIDI |
| Power | 9V DC center-negative, ~1A (400mA nominal); over-volt + reverse-polarity protected to ±20V |
| Dimensions | 5.75" × 6.5" × 2.5" |
| Price | $999 USD / €1,099 EU |
| Released | June 2026 |

Sources: [manual spec sheet p.46 + modes/states/voicings pp.26–38](manuals/Big+Time_Manual_Chase+Bliss.pdf); [Chase Bliss product page](https://www.chasebliss.com/big-time); [gearnews](https://www.gearnews.com/chase-bliss-big-time/).

## 13. Starting-point settings

Fader positions referenced low→high; buttons by selected option.

**(a) Clean stereo delay** — steady, transparent, locked to clock
- MODE: Short · STATE: Digital · VOICING: HiFi · SCALE: off · MOTION: off
- COLOR: low · TIME: to taste (or MIDI clock) · FEEDBACK: ~30% · WET: ~40% · CLUSTER: 0 · TILT EQ: noon
- SPREAD: subtle widening. Use as the "delay you can always reach for."

**(b) Tape / lo-fi echo** — murky, degraded, the End-Board signature
- MODE: Short or Long · STATE: Saturated · VOICING: Warm or Analog · **0.5X: on** (bit-crush)
- COLOR: ~50% · FEEDBACK: ~50% · WET: ~45% · CLUSTER: ~25% · TILT EQ: slightly up (cut mud)
- Sits perfectly after Generation Loss; let repeats crumble before tape print.

**(c) Self-oscillating drone** — oceanic, single-chord-forever
- MODE: Long · STATE: #!&% (misbias) or Saturated · VOICING: Analog · MOTION: Sine (slow)
- FEEDBACK: high (above COLOR) · COLOR: ~30% · DIFFUSE: high · CLUSTER: high · WET: set carefully (loud!)
- Pull HOLD RIGHT to freeze; play overtop. Feed into H90 hall for the doom wall.

**(d) Rhythmic dotted-eighth** — the live workhorse
- MODE: Short · STATE: Compressed · VOICING: Focus · SCALE: off · MOTION: off
- TIME: dotted-eighth via tap/MIDI · FEEDBACK: ~35% · WET: ~40% · CLUSTER: low · SPREAD: ping-pong
- Compressed keeps repeats punchy and articulate in a dense mix.

## 14. Versus alternatives — why it earns the slot (and benches the TimeLine)

- **vs Strymon TimeLine (benched):** The TimeLine is the more *versatile, screen-driven, preset-deep* delay — 12 machines, deep MIDI, reverse/tape/ice. But the rig sheet's logic is explicit: **"Big Time + H90 delays cover the live needs."** Big Time owns the *analog-voiced, self-degrading, saturating* delay character the TimeLine can only approximate digitally, and the **H90** owns the *clean algorithmic, reverse, shimmer, pitched* delays plus all reverb. Between the two there's no live delay the TimeLine uniquely provides — so it comes off-board. Big Time also matches the all-Chase-Bliss End Board's shared MIDI-clock / Automatone workflow, which the TimeLine sits outside of.
- **vs Eventide H90 (on-board, complementary not redundant):** Not a competitor — a co-worker. H90 does the surgical/algorithmic/reverb work; Big Time does the warm, dirty, hands-on, fader-driven echo. Run them in series.
- **vs the rest of Chase Bliss's catalog:** Thermae (pitch-shifting BBD delay) and Tonal Recall (analog BBD delay) are the spiritual ancestors, but both are mono-ish BBD boxes; Big Time is true-stereo, digital-core, deeper, and the only one with the EAE saturation/limiter character. MOOD MkII overlaps only on micro-looping, not on primary delay.
- **vs other boutique hybrids (e.g. Mentha Works Monk Echo, Blue FX Cassetta — cited by GPX as preferable):** A fair caveat — some reviewers prefer purer tape-delay voices. But none of those integrate into *this* rig's all-CB, MIDI-synced, stereo, tape-print End Board the way Big Time does. In context, the integration is the differentiator, not just the tone.

The honest summary: Big Time is the End Board's **primary, character-forward, MIDI-synced stereo delay** — the box that takes a pre-degraded stereo wash and either keeps time cleanly or rips it into harmonic ambience, with an analog limiter doing the dirty work. That specific job — and its native fit alongside Generation Loss, MOOD, Blooper, Chroma, and H90 — is why it's bolted to the board and the TimeLine is on the bench.

## Sources

- [Chase Bliss — Big Time product page](https://www.chasebliss.com/big-time)
- [Big Time Field Guide (owned manual PDF)](manuals/Big+Time_Manual_Chase+Bliss.pdf)
- [Big Time MIDI Manual (Chase Bliss)](https://www.chasebliss.com/s/Big-Time_MIDI-Manual_Chase-Bliss.pdf)
- [Electronic Audio Experiments — Big Time blog (John Snyder)](https://www.electronicaudioexperiments.com/blog/2026/4/29/big-time)
- [gearnews — Chase Bliss Big Time: The Ultimate '80s Voiced Rack Delay Pedal?](https://www.gearnews.com/chase-bliss-big-time/)
- [GuitarPedalX — Big Time Automatone-format writeup](https://www.guitarpedalx.com/news/gpx-blog/chase-bliss-rolls-out-another-interesting-variant-of-its-automatone-auto-slider-format-the-big-time-hybrid-echo-delay-in-collaboration-with-eaes-john-snyder)
- [Sonicstate — Big Time from Chase Bliss](https://sonicstate.com/news/2026/05/01/big-time-from-chase-bliss-/)
- [Guitar Bomb — The "Big Time" Has Arrived](https://guitarbomb.com/chase-bliss-big-time/)
- [Chase Bliss × EAE — BIG TIME Full Demo (YouTube, stereo)](https://www.youtube.com/watch?v=cHQzpkalwS0)
- [Elektronauts — Big Time discussion thread](https://www.elektronauts.com/t/chase-bliss-effects-pedals/31096)
- [The Gear Forum — Big Time (collab with EAE) thread](https://thegearforum.com/threads/chase-bliss-big-time-collab-with-eae.11307/)
