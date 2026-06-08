# Chase Bliss Clean — Usage Guide

The name lies: the Clean is a **VCA-based two-stage stereo compressor** (compressor → output
limiter), not a clean boost — and it's the rig's **always-on cornerstone at the front of Board
1** (after the Polytune, feeding the Colour Box V2). The one thing to internalize, from the
maker's own video manual: **you set it by ear against the left LED, and SENSITIVITY is the
master control you re-set per instrument** — the divided-pickup banjo (GK-5) and the passive
baritone Jazzmaster will never share a setting. Keep it in its lane (dynamics + level + a touch
of motion), let the Colour Box do tone, and it becomes the stable anchor the whole board's
gain-staging hangs off. *(daily-clean-dialing-in, chase-bliss-clean-official-video-manual)*

> Since this is the owner's favorite/most-used pedal, this guide leads with daily-use craft.
> Coverage is moderate (Nov-2024 release) — the authoritative source is CB's own video manual;
> there's **no signature-artist mythology yet**. MIDI = ch.2, PC/CC, 2 presets; **clock-synced
> "Bounce" is feature-listed but CC-unconfirmed** — don't assume it locks to the grid (cb-stack). *(community-clean-value, cb-stack-clock-sync-per-pedal)*

---

## 1. Essential workflows

### The controls (verified across the manual + Doug Hanson + BachelorMachines)
- **SENSITIVITY = inverse threshold (the master).** Turn it up until the **left red LED moves
  on your peaks** at real playing volume (brighter = more compression). **Re-set per instrument.**
  If *either* Sensitivity or Dynamics is fully CCW, stage-1 does nothing. *(video-manual, doug-hanson)*
- **DYNAMICS = ratio:** **7:00 = 1:1 · 10:00 ≈ 4:1 · noon = ∞:1** → noon–3:00 blends feedback→
  feedforward limiting (smooth → snappy) → **past 3:00 = Sag** (inverts dynamics; tube-overload). *(video-manual, bachelormachines)*
- **WET / DRY:** unity ≈ noon, both **boost well past** (make-up gain / parallel blend). **Attack**
  0.5–300 ms (no look-ahead → extreme settings let transients escape, normal). **Release** ~50 ms
  fast / ~1.5 s slow / middle = user-set. *(video-manual)*
- **EQ (noon = off, wet-only):** CCW removes highs, CW removes lows; **Left = Shifty** (envelope-
  filter sweep), **Right = Modulated** (harmonic tremolo, rate = Attack). **Physics:** left wobble /
  middle stable / right glitch. **MOTION** = dynamic tremolo (Dynamics = depth, Attack = rate). *(geardead, bachelormachines)*
- **DUSTY** = the 2nd-stage limiter set loose into a **blooming overdrive** (Sensitivity becomes its
  amount); hits the dry signal too, and any comp/EQ/mix change reshapes it. *(video-manual, rhett-shull)*

### Hidden options & dips
- **Envelope Balance** (hidden, on EQ): a sidechain-style **HPF on the *control* signal only**
  (audio unaffected) → the comp tracks the upper register, ignoring lows. **The banjo tool.** *(video-manual, daily-clean-dialing-in)*
- **Spread Routing** (hidden, on Physics): assign SPREAD to EQ *or* to volume-effects independently.
  **Envelope Type** (hidden, on Release): Analog / Adaptive / Combo. (GuitarPedalX also lists an "EQ
  Direction" option — confirm against the printed manual.) *(guitarpedalx, elektronauts)*
- **Swell:** hold both footswitches → **WET = swell-in, DRY = swell-out** (100 ms–4 s; both fastest
  = "BLIPS"). **MISO** dip = mono→stereo; **SPREAD** = per-effect stereo motion. *(video-manual)*

---

## 2. Daily-use playbook (always-on cornerstone)

**"Home Base" everyday setting** *(daily-clean-dialing-in, video-manual)*: Sensitivity set by LED
movement · **Dynamics ~10:00 (≈4:1)** · **Wet ~noon (unity / make-up)** · Dry off (or up for
parallel) · Release middle · **EQ noon (off — let the Colour Box do tone)** · Physics center · all
CUSTOMIZE dips off. It's **dead quiet even with Wet/Dry gained up**, so it's safe as a permanent
front-end level/dynamics anchor.

**The maker's 3 named recipes** *(cb-manual-clean-compression-recipes)*:
- **TRANSPARENT ENHANCER** — ~2:1, slow Attack, slow Release: thickens/focuses/extends, pick attack
  uncompressed. (Leads / all-around starter.)
- **TIGHT & LIVELY** — ~4:1, fast Attack, fast Release: absorbs everything but the first pick
  transient. (Chords / dense playing.)
- **PARALLEL POP** — Dry up + Wet up + extreme Dynamics/Sensitivity, fast attack: big/punchy with
  articulation blended back. (Bass/drums/thickening.)

### Compression & boost craft for THIS rig
- **Even the banjo (EBM-5/GK-5):** it's all-attack/no-sustain. The **transient-designer method**
  (BachelorMachines): push **DRY** to engage the 2nd-stage limiter for body, use stage-1 purely to
  shape — **slower Attack (~1:00)** lets the pluck spike through, **slow Release (~1.5 s)** extends
  decay into guitar-like sustain — and turn on **Envelope Balance** so it reacts to the bright
  register, not phantom lows. *(bachelormachines, daily-clean-dialing-in)*
- **Sustain the baritone drone:** full-range envelope, slightly faster Attack to catch heavier
  transients, slow Release + limiting (Dynamics near noon) for a sustained wall. *(daily-clean-stereo-spread)*
- **Push the fuzzes (108 / Hizumitas / Longsword):** high **Sensitivity + Dynamics toward noon
  (limiting)** so even quiet picking triggers full saturation — the "always-on huge" doom feeder;
  back Dynamics down to let the fuzz breathe with your attack. (Honest: Wet/Dry is comp make-up
  gain, not a pristine clean-boost — plenty hot to slam the next pedal, just not transparent.) *(daily-clean-dialing-in)*
- **Dusty as pre-dirt:** crank Dynamics → boost Wet → roll back Sensitivity = blooming OD that
  sputters when you dig in (on-brand degradation into the fuzzes; a flavor, not a default). *(video-manual, rhett-shull)*

---

## 3. Power-user tips, tricks & hidden features

- **Set everything by the left LED** — it flashes only when compression is actually acting. *(video-manual)*
- **Preset strategy for a cornerstone** (Bass Fox): presets save dip states too → **left = transparent
  leveler, right = Dusty pre-dirt, middle (live) = creative/Sag/tremolo**; recall via MIDI PC. *(bassfox)*
- **Sag as a swell/slapback designer** — slow-attack/fast-release in Sag adds a transient boost +
  slapback tail; on sustained sources it makes swelling pads. *(bachelormachines)*
- **Pseudo-sidechain / ducking** — feed a kick (Digitakt/MPC) into the **1/8" sidechain jack** → the
  stereo bus/pad ducks on every kick (Ricky Tinez); a hardware pump with no DAW. *(ricky-tinez, bassfox)*
- **Noise gate** (hidden) — Sensitivity = threshold, Dynamics = release; **keep the threshold low or
  it eats lightly fingerpicked banjo notes.** *(elektronauts, daily-clean-dialing-in)*

---

## 4. Notable users & techniques

- **Honest:** no signature artist (Nov-2024 release) — coverage is demo-creators, not players.
- **Ricky Tinez** (electronic/house) — Clean **end-of-chain on a drum/synth bus**: live limiter
  dial-in (Dry off, into limiting, fast/fast) + the **pseudo-sidechain** kick-duck. Most relevant to
  the rig's modeled VG-800 source + Elektron/MPC boxes. *(ricky-tinez)*
- **Devin Belanger** — Clean on *every track* (Dusty on drums, Modulated-EQ stereo "Leslie" on pads,
  mono→stereo creative comp). *(devin-belanger)*
- **Rhett Shull** — the best "who it's for" framing (sound-design/mixing users, not basic-comp users)
  + **Dusty-as-standalone-overdrive**. **Gear Dead** — the guitarist always-on take. *(rhett-shull, geardead)*

---

## 5. Stereo, chain integration & MIDI

- **Stereo (MISO/SPREAD):** MISO (TS-in/TRS-out + dip) splits mono → stereo; **SPREAD default is
  "wild/weird widening," not subtle** — but **mono-safe (no phasing)**. For *tasteful* width:
  spread-route **SPREAD to EQ only** (identical comp both sides), keep **Physics centered**, blend
  **Dry up the middle** for a mono core. *(daily-clean-stereo-spread, video-manual)*
- **Placement (this rig):** it sits **front of Board 1, mono**, so MISO/SPREAD/Bounce are dormant —
  correct for its level/dynamics job. The stereo features only pay off if redeployed **end-of-chain
  as a stereo bus comp/widener** (Tape Op's preferred use). *(daily-clean-stereo-spread)*
- **MIDI:** ch.2, PC/CC, **2 presets** for scene recall (the one-PC whole-stack scene). **Bounce** =
  continuous LFO motion (knob → Sweep → Sensitivity = ramp rate); **clock-sync UNCONFIRMED** at the
  CC level — treat tempo-synced Bounce as probable-but-unverified. *(cb-stack-preset-scene-recall, cb-stack-clock-sync-per-pedal)*

---

## 6. Best learning resources

- **Chase Bliss "Clean — Video Manual"** — authoritative; exact ratio positions + all hidden options.
- **BachelorMachines "Compressor Science"** (~39 min) — the deepest "how to use it": VCA theory +
  demonstrated drum/Sag/EQ-tremolo/Dusty recipes (the transient-designer method).
- **compressorpedalreviews.com deep dive** — best specialist tips (4:1@10:00, Envelope Balance, Dusty).
- **Ricky Tinez** — end-of-chain bus limiter + pseudo-sidechain (production angle). **Rhett Shull** —
  who-it's-for + Dusty-as-boost. **Doug Hanson** — concise control/dip quick reference.
- **Elektronauts "Clean — the creative compressor" thread** — best real-world owner workflow (Dusty
  advocacy, noise-gate gotcha). TGP/TalkBass are paywalled/403. *(video-manual, bachelormachines, compressorpedalreviews, ricky-tinez, rhett-shull, doug-hanson, elektronauts)*

---

## 7. Common pitfalls / gotchas

- **Noise gate eats quiet notes** — turn its threshold fully down for the dynamic banjo. *(elektronauts)*
- **Power: ≥300 mA is critical for noise performance**; 9V center-negative only. **CV: 0–5 V only —
  over-voltage OR negative voltage can damage it.** *(compressorpedalreviews)*
- **No look-ahead** — extreme Attack lets transients escape (normal). *(bachelormachines)*
- **Sag and Dusty hit the dry signal too** — they're not wet-only flavors. *(video-manual)*
- **Single compression LED** — less precise than multi-LED comps; you dial by feel. *(community-clean-value)*
- **EQ-tilt direction confusion** — one demo (Bass Fox) reversed it; **trust the manual** (CCW removes
  highs, CW removes lows). *(bassfox, video-manual)*
- **Complexity** ("not for the faint of heart") — mitigate by saving the 2 presets / MIDI recall. *(community-clean-value)*
- **Clock-synced Bounce is unverified** — don't rely on it locking to the Digitakt grid. *(cb-stack-clock-sync-per-pedal)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `chase-bliss-clean-official-video-manual.md` — authoritative control + hidden-options walkthrough
- `bachelormachines-compressor-science-deep-dive.md` — deepest workflow video (transient designer, Sag, Dusty)
- `bassfox-quincas-moreira-studio-tool-sidechain.md` — studio tool, sidechain ducking, preset/live strategy
- `ricky-tinez-clean-live-limiter-pseudo-sidechain.md` — end-of-chain bus limiter + pseudo-sidechain
- `rhett-shull-clean-who-its-for-dusty-boost.md` — who-it's-for + Dusty-as-overdrive
- `geardead-fun-creative-compression-guitar.md` — guitarist always-on take (EQ-trem, Physics, Dusty)
- `doug-hanson-control-runthrough-demo.md` — concise control + dip quick reference
- `devin-belanger-clean-most-useful-pedal.md` — Clean on every track (Dusty drums, stereo "Leslie" pads)

**Links** (`research/links/`)
- `cb-manual-clean-compression-recipes.md` — the 3 named recipes + Dusty/Swell/Motion/Spread/Gate values
- `daily-clean-dialing-in-everyday-compression.md` — everyday dial-in (Sensitivity-by-LED, 4:1@10:00, parallel, make-up gain)
- `daily-clean-stereo-spread-miso-and-chain-placement.md` — stereo MISO/SPREAD/Bounce + tasteful-vs-gimmick + placement
- `compressorpedalreviews-clean-deep-dive.md` — specialist settings, Envelope Balance, Dusty/Sag, power/CV pitfalls
- `elektronauts-clean-creative-compressor-thread.md` — owner workflow, Dusty advocacy, noise-gate gotcha
- `elektronauts-clean-community-recipes.md` — community Dusty/Motion shares, Octatrack/end-of-chain use
- `guitarpedalx-clean-hidden-options-map.md` — full knob/toggle hidden-options map
- `community-clean-value-and-bass-consensus.md` — value/"enjoy not need" debate, single-LED + complexity notes
- `clean-demos-artists-index.md` — demo index + honest artist reality check
- *(MIDI/clock: reuse `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`)*

## Sources

Video (YouTube): CB official manual `26AH-aL4b6Q` · BachelorMachines `cMQYERrLV2Y` · Bass Fox
`bVq8W3dz6Ww` · Ricky Tinez `Y6RGAi91Ggk` · Rhett Shull `63-1X006UyU` · Gear Dead `klQIQsFAXcU` ·
Doug Hanson `KQy1xcVlhgM` · Devin Belanger.
Official: chasebliss.com/clean + the Clean manual ("Compression Ideas" pp.22–23) · firmware.chasebliss.com.
Community: compressorpedalreviews.com · elektronauts.com (Clean creative-compressor thread) ·
guitarpedalx.com · tapeop.com · TGP/TalkBass (paywalled, paraphrase-level).
CB-stack MIDI: `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`.
