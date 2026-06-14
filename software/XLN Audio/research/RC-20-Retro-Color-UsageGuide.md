# RC-20 Retro Color — Usage Guide

RC-20 is the **overt lo-fi *suite*** of this rig — six character modules behind one
**Magnitude** master knob, the "how much lo-fi" macro you automate from clean to
"full-blast wobbly distorted mayhem." Reach for it when you want *obvious,
cartoon, statement* degradation (or its built-in Space reverb) on a per-track
stamp or a whole-bus morph — and reach for **SketchCassette II** when you want
believable cassette nobody clocks as a plugin, **Decapitator** for intentional
analog *harmonic* color, and the **hardware** (Generation Loss / Big Time) for
real-time degradation you play into. It's the breadth tool: one box covering
~95% of audio-destruction jobs, deliberately *not* the most authentic at any one
of them. `research/links/rc20-internet-tattoo-lofi-plugins.md`, `research/links/rc20-elektronauts-reels-echomelt-comparison.md`, `research/links/rc20-kvr-effects-thread.md`

> **Two naming corrections vs common web sources (verified):**
> (1) **Magnitude is the MASTER wet/dry slider, NOT a module.** The 6th module is
> **Magnetic** (tape volume-wear/dropouts). Several blogs conflate the two.
> (2) **Module order is FIXED, not reorderable** — signal flows Noise → Wobble →
> Distort → Digital → Space → Magnetic, with the *one* exception that **Noise can
> be routed to the very end (post-Master-EQ)** to stay unprocessed. The task
> brief's "reorderable" assumption is wrong; only Noise's post-routing moves.
> `research/links/rc20-manual-reference.md`, `research/links/rc20-musicradar-review.md`

## 1. Essential workflows

- **Per-track character stamp.** The everyday use across every source: drop RC-20
  on one drone layer, banjo/baritone stem, drum loop, or texture aux; pick the
  module(s) that source needs; balance with the big knobs. Noise on drum loops,
  Wobble small on a bed / extreme on a single synth, Distort on bass for grit,
  Digital for 12-bit hat character, Magnetic for "cassette demo-tape" vocals. `research/links/rc20-audioblob-review.md`, `research/transcripts/rc20-producergrind-on-everything.md`
- **The Magnitude morph (the signature move).** Put RC-20 on a stem *or the
  master bus* and automate the single **Magnitude** parameter to morph **lo-fi →
  hi-fi** (or dry → "full-blast mayhem") across a section — intro/outro/drop. One
  automation lane instead of riding six knobs; this is RC-20's headline workflow
  edge over every rival. Unlike SketchCassette, RC-20 *has* a true global wet/dry,
  so master-bus use is sanctioned here. `research/links/rc20-elektronauts-reels-echomelt-comparison.md`, `research/links/rc20-tapeop-review.md`, `research/links/rc20-musicradar-review.md`
- **Load a preset, then pull Magnitude back.** Factory/3rd-party presets are
  heavy-handed; the standard fix is load the vibe, then drop **Magnitude** to make
  it subtle while keeping the preset's character balance. `research/links/rc20-lofi-weekly-tips.md`
- **Bus glue across a group.** One RC-20 across a *group/bus* of melodic
  instruments to unify them under a single lo-fi color (Nick Chen's closing
  demo). `research/transcripts/rc20-nick-chen-walkthrough.md`
- **Build from INIT.** To learn or sound-design from scratch, load the **INIT
  preset** (everything zeroed/off — modules grey out) and turn modules on
  left-to-right in signal order. `research/transcripts/rc20-nick-chen-walkthrough.md`

## 2. The 6 modules explained (with sub-params & ranges)

Each module = one big **Amount** knob (0 = bypassed) + a per-module on/off button
+ a **Flux** slider + module-specific controls. `research/links/rc20-manual-reference.md`, `research/links/rc20-musicradar-review.md`, `research/transcripts/rc20-xnb-full-control-walkthrough.md`

1. **Noise** (generator) — **16 noise types**: vinyl crackle, tape hiss, ambient
   studio noise, electric hum, stompbox static, VHS, DC/transformer, "JP8" synth
   white noise, **Big Muff noise**, 8-bit computer, etc. **Tone** = noise
   frequency balance (right = high-end crackle, left = low-mid). **Follow** =
   envelope follower (noise rides the input, decays with it). **Duck** = inverse
   compressor (noise gets *out of the way* of the source — "great on drums," and
   the route to that SP-404 / J-Dilla ducked-vinyl feel). **POST routing** =
   move noise to the very end so the Master EQ doesn't touch it.
2. **Wobble** (wow & flutter — **PITCH** modulation) — **Wow↔Flutter** slider:
   **Wow 0.1–4 Hz** (slow pitch drift), **Flutter 6–20 Hz** (fast; pure-flutter
   goes much faster). **Rate** per side. **Stereo** = separate wow/flutter L/R =
   "massive stereo spread." **CHORUS TRICK:** lower **Mix** to ~50% with Stereo on
   → a lush chorus. Small = subtle lo-fi; extreme = "seasick synth nightmare."
3. **Distort** (saturation/distortion) — **6 algorithms**: valve/tube,
   transformer, broken speaker, + three waveshapers. **Focus filter** =
   band-target the drive (keep the low fundamental clean, dirty the low-mids/highs
   — great on bass). **Mix** = parallel saturation. Mild warmth → raging fuzz.
4. **Digital** (degrader/bitcrusher) — **Rate↔Bits** slider (sample-rate
   reduction vs bit-depth reduction; bit-side = "a full wall of harsh noise").
   **Smooth** = soften the artifacts. **Focus** with a **Cut** option (Cut removes
   freqs *outside* the band; Focus crushes *inside*, passes the rest). The fast
   route to 8-bit / 12-bit drum-machine character.
5. **Space** (reverb/resonator, "12-note resonator") — **Decay** (tail length),
   **Pre-delay**, **Stereo** (default on), **Focus** (which freqs get reverb /
   damping). Large, shimmer-ish, lo-fi-leaning. **Honest:** the weakest module —
   "unremarkable / superfluous" as a standalone reverb, but fine *blended* under
   the others. For serious tails use Valhalla; use Space for an in-box wash. `research/links/rc20-musicradar-review.md`
6. **Magnetic** (tape wear — **VOLUME** modulation, NOT pitch) — **Wear↔Flutter**
   knob: **Wear** = slow volume fluctuation from tape wear ("how many times
   you've played it"); **Flutter** = faster volume artifact from the capstan pinch
   (**Rate 6–30 Hz**). **Dropouts** = extreme, more-random volume drops ("needle
   skipping" / cassette demo vibe — a standout competitors lacked). **Stereo**
   (independent L/R). `research/links/rc20-kvr-effects-thread.md`

**Flux (per module, the analog-mojo engine):** NOT a dry/wet — from the manual it
"adds organic, non-linear fluctuations under the hood, customized per module"
(random overdrive on Distort, pre-delay mod on Space, random volume/dropouts
elsewhere). Turns the dead-consistent LFOs into tape-like unpredictability. Best
used at the *end* of sound-design or when fast-auditioning. `research/transcripts/rc20-nick-chen-walkthrough.md`, `research/links/rc20-musicradar-review.md`

## 3. Global wet/dry, dice & presets

- **Magnitude** (top) = the global Dry/Wet macro — scales all six Amount knobs +
  the master-section controls 0–100% of their set values. 0% = instant bypass
  A/B; 100% = full. The prime automation target. = the "how much lo-fi" master. `research/links/rc20-manual-reference.md`, `research/transcripts/rc20-nick-chen-walkthrough.md`
- **Master section:** Input gain (drive harder = more saturation reaction; **no
  auto-gain** — ride In/Out yourself), EQ (low-cut shelves incl. a resonant-bump
  option; high-cut soft/steeper), **Tone** (high-shelf or narrow-mid tilt),
  **Width** (stereo widener, scaled by Magnitude), Output gain. Default low/high
  cuts keep it musical even at extremes — which also means it's *hard to make it
  sound genuinely broken/ugly* without disabling them (a lo-fi-rig caveat). `research/links/rc20-tapeop-review.md`, `research/links/rc20-musicradar-review.md`
- **The "dice":** RC-20's randomizer is a **preset-NAME generator** when saving a
  user preset — not a full patch-randomizer. The per-module **Flux** is the actual
  "randomize the sound" engine. `research/transcripts/rc20-xnb-full-control-walkthrough.md`
- **Presets:** factory banks by source (drums, keys, guitars, bass, full mix,
  post) + cassette/noise/digital/space/vinyl. Big 3rd-party economy: free —
  Adieu "Timeless" (40+), LoFi Weekly ("LoFi Light," "Tunnel Vision," "Feeling
  Lost," "LoFi Tapestry"); paid — ADSR, ProducerGrind "Crypto" (75). Modular
  toggles let you keep one module from a preset and drop the rest. `research/links/rc20-free-preset-packs.md`, `research/links/rc20-audioblob-review.md`

## 4. Signature settings & presets (copyable values)

Concrete starting points (relative settings; ride **Magnitude** to taste after).

- **Vinyl crackle floor** — Noise: type *Vinyl*, Amount to taste, **Tone** mid,
  **Follow** low (constant floor) or **Duck** up if you want it to dip under the
  source. Route **POST** if you don't want the Master EQ to thin it. Add light
  Flux for a less-looped, more random crackle. `research/transcripts/rc20-xnb-full-control-walkthrough.md`
- **Warped tape / wobble drone** — Wobble: slider ~70% toward **Wow**, slow Rate,
  Amount moderate, **Flux** up for natural drift; small Magnetic **Wear** under
  it. Keep it subtle on a sustained bed; push Wobble hard only on a *single* synth
  layer (extreme = seasick). `research/links/rc20-audioblob-review.md`, `research/transcripts/rc20-vs-retrofi-vs-izotope-vinyl.md`
- **Broken radio / AM bandpass** — Master EQ: hard low-cut + high-cut to a
  midrange band; add Noise (hum/static) + Magnetic Dropouts; small Distort. (The
  "Tunnel Vision" free preset is this — wide ambient radio coloration.) `research/links/rc20-free-preset-packs.md`
- **Bitcrush / 8-bit** — Digital: drag toward **Rate** for sample-rate crush or
  **Bits** for a harsher wall; **Focus** on the highs for "crystal crunch,"
  **Smooth** up to tame harshness; Mix to blend. "12-bit drum-machine character on
  hi-hats." `research/transcripts/rc20-nick-chen-walkthrough.md`, `research/links/rc20-audioblob-review.md`
- **Washed-out ambient (RC-20's own Space)** — Space: **Decay** long, **Pre-delay**
  small, **Focus** to top-end, Stereo on; pair with light Magnetic flutter + low
  Noise. (= the "Feeling Lost" free preset's flutter + reverb + 8-bit + noise — the
  most drone-relevant factory recipe.) `research/links/rc20-free-preset-packs.md`
- **"Old sample" hip-hop** — Noise *Duck* + Magnetic **Wear** (the SP-404 vinyl-sim
  / J-Dilla ducked feel) + light Distort (tube) + Digital rate-crush; this is the
  whole lo-fi-beat school's RC-20 chain. `research/links/rc20-lofi-weekly-tips.md`, `research/transcripts/rc20-producergrind-on-everything.md`
- **Lo-fi bus on a full mix** — gentle Noise floor + small Distort (warmth) +
  light Magnetic + EQ low/high cut; keep **Magnitude** ~30–50% and automate it up
  for the lo-fi sections. Master-bus use is sanctioned (it has a real global
  wet/dry). `research/links/rc20-musicradar-review.md`, `research/links/rc20-elektronauts-reels-echomelt-comparison.md`
- **Subtle everyday color ("LoFi Light")** — light Noise (vinyl) + a touch of
  Digital rate reduction (sampler aliasing); the gentle, always-usable stamp. `research/links/rc20-free-preset-packs.md`

## 5. RC-20 vs SketchCassette II / Decapitator (division of labor)

These three barely overlap — don't stack them fighting. `research/links/rc20-internet-tattoo-lofi-plugins.md`, `research/links/rc20-elektronauts-reels-echomelt-comparison.md`

- **RC-20 = the overt lo-fi SUITE + the Magnitude macro + built-in Space reverb.**
  Reach for it for *cartoon/statement* degradation, the one-knob dry→destroyed
  morph (incl. on the master bus), bitcrush, and an in-box wash. It is explicitly
  "not subtle or even realistic" — that's the point. `research/links/rc20-internet-tattoo-lofi-plugins.md`
- **SketchCassette II = believable cassette REALISM** (authentic tape distortion +
  wow/flutter, per-track only, no master use). Reach for it when the degradation
  should *not* read as a plugin. RC-20 owners on KVR literally wish RC-20 "had
  more of the tape sound so I won't need a specific tape plugin" — SketchCassette
  *is* that plugin. `research/links/rc20-kvr-effects-thread.md`, `research/links/rc20-internet-tattoo-lofi-plugins.md`
- **Decapitator = intentional analog HARMONIC color** (5 hardware-modeled
  saturation styles, the parallel Mix knob) — warmth/tone-shaping, not motion.
  RC-20's Distort is broader/cartoonier; Decapitator is the *nicer-sounding*
  saturator when you want analog glue, not destruction.
- **Don't double-degrade the same motion:** pick RC-20 *or* SketchCassette *or* a
  hardware tape pedal per layer for the wow/flutter — two wobble engines on one
  source = mush. Likewise don't run RC-20 Distort *and* Decapitator hard on the
  same source. **Rough labor split:** RC-20 = overt suite/morph; SketchCassette =
  realistic cassette; Decapitator = analog harmonics; hardware (Generation Loss /
  Big Time) = played-in real-time tape. `research/links/rc20-elektronauts-reels-echomelt-comparison.md`

## 6. Notable users & techniques (sourced, flagged)

- **Official artist-preset collaborators (HIGH that they made presets):** **Bad
  Snacks** — the most rig-relevant (lush "evolving noise textures," riser/
  transition FX); **The Kount** (punchy saturated drums), **K Fresh** (808s/trap),
  **Johnnybgood** (Game-Boy crunch). `research/links/rc20-artists-sourced.md`
- **Endorsements (vendor/marketing → MEDIUM):** **Diplo** ("perfect to bring all
  my new sounds into a vintage feel"); a community claim that RC-20 was on Ariana
  Grande's "Thank U, Next" (unverified, off-aesthetic — listed for completeness). `research/links/rc20-artists-sourced.md`
- **Lo-fi-beat heartland (HIGH as a class):** named-but-garbled producers incl.
  **Frank Dukes** (the credible one — vintage-sample sound for Drake/Weeknd/Travis
  Scott). RC-20 is a staple on melodies/drums/808s/vocals in that world. `research/transcripts/rc20-producergrind-on-everything.md`
- **Drone/ambient signal (capability, NOT a credit):** KVR users say RC-20 *alone*
  can emulate **William Basinski** and **The Caretaker** "without additional
  plugins" — the decay/loop-degradation drone aesthetic, exactly this rig. This is
  a forum capability claim, **not** evidence either artist uses RC-20. `research/links/rc20-kvr-effects-thread.md`
- **Honest gap:** **no verifiable NAMED drone/doom/shoegaze artist** uses RC-20
  specifically. Closest real signals = the Bad Snacks texture bank + the Basinski/
  Caretaker emulation claims. None invented. `research/links/rc20-artists-sourced.md`

## 7. Rig-specific recipes (your gear by name)

- **Banjo/baritone-as-lead "found in the dirt":** RC-20 on the stem — Noise (vinyl,
  Duck) + Magnetic Wear + small Distort (tube, Focus off the low fundamental) +
  Space short. Automate **Magnitude** up where the lead should sound "recorded
  wrong." `research/links/rc20-audioblob-review.md`
- **vs the hardware tape pedals (Generation Loss / Big Time):** use the **pedals
  live/on the way in** (real-time wobble you commit to the take); use **RC-20 in
  the box, after the fact**, on stems for recallable/automatable lo-fi and the
  Magnitude morph. Don't print both the same wow/flutter on one layer. `research/links/rc20-elektronauts-reels-echomelt-comparison.md`
- **Reamping the board into RC-20:** record the pedalboard clean(ish), then reamp
  the studio character with RC-20 on the return — instance freely, recall, automate
  (the back-end vs the committed front-end pedals). `research/links/rc20-elektronauts-reels-echomelt-comparison.md`
- **Sampling hardware (OP-1 / Digitakt / MPC / Octatrack) into Logic/Kontakt:** run
  the recorded sample through RC-20 for the "old sample" stamp (Noise Duck +
  Magnetic + Digital rate-crush) before chopping — the documented lo-fi-beat move. `research/transcripts/rc20-producergrind-on-everything.md`
- **In Logic (AU):** RC-20 is the AU; automate **Magnitude** for the dry→destroyed
  morph; **freeze/commit** heavy patches before tracking over (CPU is low — see
  below — so this is for recall/latency hygiene, not load). For long ambient tails
  prefer Valhalla over Space; use RC-20's Space only as a blended wash. `research/links/rc20-musicradar-review.md`
- **In Ableton Live 12 Lite (secondary):** RC-20 works as VST3/AU; the Magnitude
  morph automates cleanly on a clip/scene; bounce/resample heavy chains to stay
  inside Lite's track ceiling. `research/links/rc20-manual-reference.md`

## 8. Power-user tips, tricks & hidden features

- **Noise POST routing** = the only way to "move" a module — push noise past the
  Master EQ so EQ/cuts don't thin your crackle, or run RC-20 as a standalone noise
  machine. `research/transcripts/rc20-xnb-full-control-walkthrough.md`
- **Wobble chorus:** Mix ~50% + Stereo on = an instant lush chorus (works as a
  legit modulation FX, not just degradation). `research/transcripts/rc20-wobble-module.md`, `research/transcripts/rc20-nick-chen-walkthrough.md`
- **Focus filters everywhere:** Distort and Digital can band-target — distort/crush
  only the highs and keep the low fundamental clean (de-mud bass, "crystal crunch"
  hats). `research/transcripts/rc20-nick-chen-walkthrough.md`
- **MIDI-automate any param** for creative control; **Magnitude** is the headline
  automation lane. `research/links/rc20-kvr-effects-thread.md`
- **Flux last:** dial the patch, then add Flux per module for the non-looped
  analog wobble; the Space-flux is the least audible. `research/transcripts/rc20-xnb-full-control-walkthrough.md`
- **Default cuts protect you** — crank anything and it stays musical; to get
  genuinely ugly/broken, you must fight those default low/high cuts. `research/links/rc20-tapeop-review.md`

## 9. Best demos & channels (ranked by depth)

1. **XNB — "the best LOFI plugin you can buy" (27 min)** — deepest single
   control-by-control walkthrough: every sub-param, the Noise EQ-routing, Follow/
   Duck, Focus filters, Flux on each module, Magnitude-as-master. `research/transcripts/rc20-xnb-full-control-walkthrough.md`
2. **Splice / Nick Chen — "Use Retro Color LIKE A PRO" (19 min)** — cleanest UI
   architecture + exact ranges (Wow 0.1–4 Hz, Flutter to ~600), the chorus trick,
   bus-glue demo. The canonical walkthrough. `research/transcripts/rc20-nick-chen-walkthrough.md`
3. **Will Hatton — "Retro-Fi vs RC-20 vs FREE [iZotope Vinyl]" (19 min)** — the
   positioning/division-of-labor demo; shows RC-20's no-delay gap and its breadth. `research/transcripts/rc20-vs-retrofi-vs-izotope-vinyl.md`
4. **XLN Audio official — "Using The Wobble Module"** — the chorus trick straight
   from the vendor (short). `research/transcripts/rc20-wobble-module.md`
5. **ProducerGrind (skit + preset pack)** — low-signal but confirms the "on
   everything" preset-driven workflow + the named-producer heartland. `research/transcripts/rc20-producergrind-on-everything.md`
- **Text:** Tape Op (Hidek) review, MusicRadar review, KVR megathread,
  Elektronauts "which lo-fi tool when," Internet Tattoo "7 lo-fi plugins,"
  AudioBlob (per-source + CPU), LoFi Weekly tips, free preset packs. (See §11.)

## 10. Common pitfalls / gotchas

- **It's "cartoony," not realistic** — by design. For believable tape, that's
  SketchCassette / the hardware, not RC-20. `research/links/rc20-internet-tattoo-lofi-plugins.md`
- **Overused factory presets** — "Vinyl 1" etc. get instantly recognizable; load a
  preset and pull **Magnitude** back, or build from INIT. `research/links/rc20-internet-tattoo-lofi-plugins.md`, `research/links/rc20-lofi-weekly-tips.md`
- **No auto-gain** — output jumps as you push Input/Distort; ride In/Out manually. `research/links/rc20-tapeop-review.md`
- **Fixed module order** — only Noise can be repositioned (post-EQ); plan the chain
  around Noise→Wobble→Distort→Digital→Space→Magnetic. `research/links/rc20-manual-reference.md`
- **Space is the weak module** — fine blended, not a standalone reverb; for the
  drone walls use Valhalla. `research/links/rc20-musicradar-review.md`
- **No delay** — unlike Waves Retro-Fi; pair with EchoBoy/hardware for echoes. `research/transcripts/rc20-vs-retrofi-vs-izotope-vinyl.md`
- **Digital module is basic** — beyond bit/rate, precision-bitcrush users prefer
  Plogue chipcrusher. `research/links/rc20-elektronauts-reels-echomelt-comparison.md`
- **CPU is LOW** ("barely moved the meter even with multiple instances"; ~7–10%
  for 3 active modules) — so freezing is for recall/latency hygiene, not load.
  **Online-only installer** (a documented annoyance). VST/VST3/AU/AAX. `research/links/rc20-audioblob-review.md`, `research/links/rc20-kvr-effects-thread.md`

## 11. Captured sources

**Transcripts (5)** — `research/transcripts/`: rc20-xnb-full-control-walkthrough
(27-min deepest control map) · rc20-nick-chen-walkthrough (Splice canonical, exact
ranges + chorus trick + bus demo) · rc20-vs-retrofi-vs-izotope-vinyl (positioning/
division of labor) · rc20-wobble-module (official XLN chorus-trick clip) ·
rc20-producergrind-on-everything (preset-driven "on everything" + producer names).

**Links (10)** — `research/links/`: rc20-manual-reference (authoritative params +
fixed-order + Noise-POST + Magnitude-vs-Magnetic correction) · rc20-musicradar-
review (exact ranges/algorithm counts, weak-Space) · rc20-tapeop-review (Magnitude
morph, default-cuts, no-auto-gain) · rc20-kvr-effects-thread (one-box 95% claim,
Basinski/Caretaker emulation, wants-more-tape) · rc20-elektronauts-reels-echomelt-
comparison (Magnitude-on-master morph, reach-elsewhere map) · rc20-internet-tattoo-
lofi-plugins (cartoony-vs-realistic) · rc20-audioblob-review (per-source uses +
low CPU) · rc20-lofi-weekly-tips (Magnitude-subtle trick, ducking) · rc20-artists-
sourced (collaborators + honesty gap) · rc20-free-preset-packs (named free-preset
recipes by module).

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/`
(first line of each = the original URL). Primary: XLN official manual/blog,
Sweetwater quickstart, Tape Op (Dave Hidek), MusicRadar, KVR megathread,
Elektronauts, Internet Tattoo, AudioBlob, LoFi Weekly, Adieu/ADSR/ProducerGrind
preset pages, XNB, Splice/Nick Chen, Will Hatton, ProducerGrind. **Honesty flags:**
(1) Magnitude≠a module / order-is-fixed corrected against the manual; (2) no named
drone/doom/shoegaze artist verified — relevance is by technique + the Basinski/
Caretaker *capability* claim; (3) ProducerGrind producer names auto-sub-garbled
(only Frank Dukes confirmed credible); (4) several link pages 402/403'd to direct
fetch and were distilled from search snippets (flagged in-file).
