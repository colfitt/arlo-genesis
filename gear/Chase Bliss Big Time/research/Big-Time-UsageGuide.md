# Chase Bliss Big Time — Usage Guide

The Big Time (2026 Chase Bliss × **Electronic Audio Experiments** stereo delay, Automatone
motorized-fader format) is built to be **an instrument you make music *with*, not a utility
delay** — CB/EAE literally market it as "the perfect centerpiece." That suits the plan here:
make it the **centerpiece**, feed it **one source (a fuzz, maybe a glitch pedal), and play the
COLOR → FEEDBACK → STATE engine** to get a whole song's worth of range from one box. Both the
designer and the community say the same thing — **"feed it one source and stay minimal or the
texture gets lost"** — so the minimal-chain approach is the *correct* approach, not a compromise.

> New-product honesty: it shipped **June 2026**, so there's **no seasoned-owner tip culture,
> no firmware lore, and no community recipe library yet** — the canon is the **10 factory
> presets**, the designer (John Snyder, EAE) in interviews, and a couple of deep demos. Early
> firmware updates are expected (Snyder said they were "working out the final couple of bugs"
> at ship). It has **no dip switches** — the deep layer is the **Alt menu** + **Options page**.

---

## 1. Essential workflows

### The engine you "play" (COLOR → FEEDBACK → STATE)
- **COLOR** = how hot you hit the input preamp + limiter; **FEEDBACK** = how hard you keep
  hitting them. **The COLOR-vs-FEEDBACK rule:** high COLOR = echoes bonk the limiter instantly;
  **low COLOR + high FEEDBACK = echoes climb to max loudness with the most change over time.** *(cb-big-time-factory-presets, official-walkthrough)*
- **STATE** (the limiter — "the most important button"): **Digital** (no limiter, clean,
  runaway risk; TEXTURE = bit-reduction/aliasing) · **Compressed** (VCA comp → ducking echoes;
  the safe self-oscillating PCM42 wall) · **Saturated** (soft-clip; TEXTURE = DC-bias asymmetry
  = "misbiased console / BBD needing calibration") · **#!&% / misbias** ("exploitative" sag-and-
  return disintegration; TEXTURE = misbias amount). *(superbooth-snyder, mark-johnston)*
- **+12dB** is "the second most important button" — Big Time is built to *add* gain (handles
  line-level synths → quiet guitars); use it to push the limiter harder. *(forums, superbooth-snyder)*
- **Reset/panic:** **hold the center MODE button → clean simple delay** from any chaos; Preset 0
  is the other home base. *(centerpiece-big-time-as-song-centerpiece)*

### Modes, freeze, ramps, pitch
- **MODES:** MOD (~3–46 ms) / SHORT (46–736 ms) / LONG (736 ms–12.2 s; ~24 s with 0.5X) / LOOP.
  *(Manual figures are canonical — Snyder verbally swaps short/mod in one interview.)* *(video)*
- **Infinite HOLD / freeze:** hold the RIGHT footswitch → non-degrading pad to solo over. In
  Long, holding RIGHT also = a one-stomp **OVERLOAD** ramp (max COLOR+FEEDBACK) into a wall —
  "beware volume." *(centerpiece, video)*
- **Pitch:** TIME is a clock control → **dragging TIME = pitch dives/rises**; **SCALE
  (Octave / Oct+4+5 / Chromatic) + square-wave MOTION + STEP mode** (tap LEFT to step through
  the scale) = clean "**mature stereo Thermae**" arpeggiated cascades off single notes (the
  banjo-as-lead move). Oct+4+5 "maps to traditional tap subdivisions." *(video, superbooth-snyder)*
- **CLUSTER = a continuous "arrangement" fader:** single head → multi-tap rhythm → washy
  diffusion → almost-a-reverb (with DIFFUSE / DIFFUSE TYPE); the added taps can ping-pong. *(official-walkthrough, forums)*
- **0.5X** = halve the sample rate (doubles max delay time) + **12-bit** reduction = built-in
  lo-fi/generation-loss (first-party "12-bit," not the "16-bit" one demo claimed). *(superbooth-snyder, video)*

### The deep layer & the feedback-loop EQ
- **Alt menu:** hold the far-left SHIFT button → faders fly to alt positions (COLOR→TEXTURE,
  TIME→RATE, CLUSTER→DEPTH, TILT→CROSSOVER, FEEDBACK→DIFFUSE, WET→DRY; MOTION→SPREAD, MODE→0.5X,
  VOICING→DIFFUSE TYPE, STATE→+12dB). **Options page:** double-tap both footswitches (subdivision
  lives here — hold SCALE, TIME fader sets it, unlabeled). *(video)*
- **TILT EQ sits *inside* the feedback loop** → boosting lows raises loop volume = more/longer
  repeats; CROSSOVER sets the pivot. **VOICING** filter slopes: HiFi (flat) / Focus (gentle
  bandpass) / Warm (~10k brickwall) / Analog (~4k gentle — a callback to the EAE Sending V2). *(video, eae-lineage)*
- **Looper:** HiFi + TIME noon ≈ 45 s pristine; TIME max = 3+ min lo-fi; Warm/Analog = sound-on-
  sound degrade. *(centerpiece, mark-johnston)*

---

## 2. Signature presets & settings

**The 10 factory presets ARE the recipe canon** — the motorized faders fly to saved positions,
so loading a preset and reading the sliders *is* the recipe. *(cb-big-time-factory-presets)*

`0 NICE DELAY` · `1 COMPRESSED CHORUS` · `2 SLAP/DOUBLE` · `3 SAGGING ECHOES` · `4 BOUNCY
THERMAE` · `5 BROKEN DYNAFLANGE` · `6 CLUSTER$%&!` · `7 CRUSHED ANALOG` · `8 NOSTALGIC REPEATER`
· `9 LOOP DIFFUSER`.

**Most on-rig (drone/doom/shoegaze):** **#7 Crushed Analog** (murky/modulated/saturated — the
bread-and-butter post-Gen-Loss delay), **#9 Loop Diffuser** (slowly dissolving infinite-feedback
drone wall), **#8 Nostalgic Repeater** (no dry signal, Frippertronics looping that crumbles),
**#6 Cluster$%&!** (misbiased swirling clusters), **#4 Bouncy Thermae** (banjo-as-lead pitched
cascade). Restore factory presets: hold MOTION+VOICING in the Preset Menu. *(cb-big-time-factory-presets)*

**Tape/lo-fi recipe (rig signature):** STATE = Saturated + VOICING = Warm/Analog + **0.5X on**. *(video)*

**Four centerpiece patches** (craft agent — save each to a preset slot): a **drone bed**, a
**Thermae lead**, a **lo-fi rhythmic groove**, and a **one-stomp climax** (OVERLOAD ramp). *(centerpiece-big-time-as-song-centerpiece)*

---

## 3. Power-user tips, tricks & hidden features

- **Punch-in-clean-then-destroy (Snyder's headline move):** in **#!&% or Saturated + long TIME**,
  the bias-sag attack/recovery is slower than the repeats — play gently and a loop stays clean,
  then **dig in to crumble it later** (William-Basinski-style decay you trigger by dynamics). *(forums, superbooth-snyder)*
- **Compressed = live rhythmic delay** — ducking echoes that stay out from under your attack. *(forums)*
- **Hold MODE = instant clean reset** from any chaos (your safety net). *(centerpiece)*
- **AUX-in** takes an external floor footswitch ("Fun mode": LEFT = 0.5X half-time drop, RIGHT =
  clear buffer); an **optional flip-up fader cover** protects the faders if floor-mounted. *(video, modwiggler)*

---

## 4. Notable users & techniques

- **Honest:** no confirmed Big Time artists yet — too new. The instructive frame is the **EAE
  lineage** (likely early-adopter pool). Verified EAE roster: **Kurt Ballou (Converge), Chelsea
  Wolfe, Touché Amoré, Unwound, Foxing, Yvette Young, Pile**, and more; named EAE collabs include
  Mirror House (Rick Maguire/Pile) and Limelight (Touché Amoré). *(eae-lineage)*
- **Circuit DNA you can borrow technique from:** the Compressed/"Blue Mode" limiter = a misused
  **Lexicon PCM42**; CLUSTER = an **Ursa Major Space Station**; Analog voicing = the **EAE
  Sending V2**. Snyder's house style — a colored preamp/saturation stage feeding a delay that
  **disintegrates gracefully as you push it** — *is* Big Time's COLOR→limiter. *(eae-lineage)*
- The deepest first-party design talk: **John Snyder on the Object Worship podcast** (host = Andy
  Othling / Lowercase Noises) — a high-value un-mined audio lead. *(object-worship-podcast)*

---

## 5. Centerpiece & rig integration (the headline use)

### Carry a song on the one pedal
Use Big Time's own range instead of more pedals: **self-oscillation/feedback walls** (STATE +
COLOR/FEEDBACK), **freeze pads** (hold RIGHT), **pitch ramps** (drag TIME) and **Thermae
cascades** (SCALE + STEP), **CLUSTER** as the arrangement fader (tap → diffusion), **0.5X +
Warm** for built-in generation-loss, and **presets for song sections** (footswitch or MIDI
recall). The variety comes from STATE / VOICING / MODE / SCALE / CLUSTER, not added boxes. *(centerpiece-big-time-as-song-centerpiece)*

### Minimal chains in (just a fuzz, maybe a glitch)
- **Fuzz → Big Time:** keep **COLOR modest** so the already-hot fuzz doesn't clamp the limiter to
  mud; **STATE = Compressed** holds a sustaining fuzz together; cut mud with **TILT up + Focus**.
  By owned fuzz: **Hizumitas** = sustaining ambient/drone walls; **MXR 108** = spitty rhythmic
  stabs for CLUSTER to echo; **EAE Longsword** = tightest/most controllable (**same builder** —
  active EQ + boost to set the slam). Mono fuzz → IN-L auto-engages **MISO** (mono-in/stereo-out). *(centerpiece-minimal-chains)*
- **One glitch, one direction:** Onward/Microcosm → Big Time (glitch = the event, delay = the
  space; clock them together), *or* Big Time → glitch to re-chop the repeats. Pick one per song. *(centerpiece-minimal-chains)*

### Sampler integration (OP-1 / Digitakt / MPC)
- **Feeding in:** OP-1 → **EHX Effects Interface** → Big Time (OP-1 out is line-level; the FXI is
  the rig's confirmed matcher); DT2/MPC line out → Big Time stereo ins with **COLOR low + DRY
  KILL** for a clean wet send. *(centerpiece-minimal-chains)*
- **Clock:** native **5-pin DIN** (no MIDIBox). DT2 master → Big Time follows (**CC111** ignore,
  **CC54** subdivision); or **Big Time as master via CC110** (60–240 BPM) to clock the rig from
  its echoes. ⚠️ **The MPC Sample distorts when slaved** (fw 1.2.1) — run it as master or verify a
  1.3.x fix. *(centerpiece-minimal-chains, cb-stack-clock-sync-per-pedal)*
- **Preset scenes:** Big Time on shared ch.2 → one Program Change from the DT2 timeline recalls a
  whole song section across Big Time + the CB stack (save over MIDI via CC27/28). *(cb-stack-preset-scene-recall)*
- **Generation-loss resampling:** freeze/print Big Time's wet → into the OP-1 (EAR, ~20 s, +8
  vol) / DT2 (MAIN INPUT → slice → comb → bit-crush, disable TO MAIN) / MPC (rear in → chop →
  resample twice). The sketch→finish handoff runs the whole song through Big Time as the unifying
  delay. *(centerpiece-minimal-chains)*
- **Don't over-saturate:** Big Time sits *after* Generation Loss in the rig — its analog character
  is strong, so feeding it an already-degraded source "sounds awful" if COLOR is high. Keep COLOR
  modest there. *(forums)*

---

## 6. Best learning resources

- **Mark Johnston / Secret Weapons** (~1h52m) — by far the deepest parameter-by-parameter tutorial; THE reference.
- **Chase Bliss (official)** — Walkthrough (architecture) + Preset Play + "The Quest for Big Time" (collab story / EAE philosophy).
- **Sonicstate / Superbooth 26 — John Snyder (EAE) interview** — best first-party per-STATE/circuit explanation; and the **Object Worship podcast** (Andy Othling host) for the deepest design talk.
- **Harp Lady (Emily Hopkins)** — highest-viewed player demo + Thermae comparison; **ambienttrash** — 31m stereo ambient/shoegaze demo (closest to this rig; no captions).
- **Communities:** TheGearPage "THIS IS NOT A DRILL! — Big Time" (~65 pp, most manual-literate);
  the **Elektronauts "Chase Bliss effects pedals" megathread** (~p.137 — the *standalone* Big Time
  thread the dossier links is dead); MOD WIGGLER (ergonomics/lineage); Reddit r/guitarpedals +
  r/chaseblissaudiophiles (snippet-level). *(mark-johnston, official-walkthrough, the-quest, superbooth-snyder, object-worship, harp-lady, ambienttrash-NOTES, thegearpage, elektronauts-megathread, modwiggler, reddit-roundup)*

---

## 7. Common pitfalls / gotchas

- **NOT a dual-independent delay** — despite "two delay lines," it's one shared-control stereo
  engine; you can't set fully independent time/feedback per output. *(thegearpage)*
- **Lacks:** reverse, random modulation, a ms display, and an FX loop. *(thegearpage)*
- **#!&% mode + cranked feedback/drive = "scary loud" / can be a mess** — set WET conservatively. *(forums)*
- **No screen → deep edits are gesture-driven** (subdivisions unlabeled in the Options page);
  motorized faders mitigate *recall* but live editing is fiddly. *(forums)*
- **Don't over-saturate an already-degraded source** (keep COLOR modest after Gen Loss); **feed it
  ONE source** or the texture gets lost/samey. *(forums)*
- **Early firmware** (shipped with "final couple of bugs" being worked out) — expect updates; no
  changelog yet. *(forums)*
- **0.5X = 12-bit** (first-party), not 16-bit; the manual's time ranges are canonical over a verbal
  interview slip. *(video, superbooth-snyder)*

---

## 8. Captured sources

*(Note: the Video and Centerpiece agents each captured 3 of the same source videos — a raw
`centerpiece-` transcript + a distilled workflow version. Both kept; listed once below by source.)*

**Transcripts** (`research/transcripts/`)
- `mark-johnston-secret-weapons-big-time-deep-dive.md` (+ `centerpiece-…` raw) — the 1h52m deep-dive; every STATE/VOICING/MODE with settings
- `chasebliss-official-big-time-walkthrough.md` (+ `centerpiece-…` raw) — official architecture walkthrough
- `harp-lady-big-time-player-demo.md` (+ `centerpiece-…` raw) — player demo + Thermae comparison
- `sonicstate-superbooth-john-snyder-eae-interview.md` — first-party EAE design/character per-STATE
- `chasebliss-the-quest-for-big-time-collab-story.md` — collab story / CLUSTER continuum / "safe center"
- `ambienttrash-big-time-full-demo-stereo-NOTES.md` — rig-relevant ambient demo (no captions; notes-only)

**Links** (`research/links/`)
- `cb-big-time-factory-presets-recipes.md` — all 10 factory presets + STATE×TEXTURE + COLOR/FEEDBACK gain rules
- `cb-big-time-where-recipes-live.md` — coverage map + Snyder design-intent quotes
- `eae-lineage-artists-and-design.md` — EAE roster + circuit lineage (PCM42 / Space Station / Sending V2)
- `centerpiece-big-time-as-song-centerpiece-one-pedal.md` — the carry-a-song-on-one-pedal playbook + 4 patches
- `centerpiece-minimal-chains-and-sampler-integration.md` — fuzz→/glitch pairings + OP-1/DT2/MPC feed+clock+resample
- `thegearpage-bigtime-thread.md` — manual-literate architecture clarification (not dual-independent; what it lacks)
- `elektronauts-cb-megathread-bigtime.md` — megathread reaction + the dead-dossier-URL correction
- `modwiggler-bigtime-thread.md` — desktop/floor ergonomics, AUX-in, EAE Halberd lineage
- `reddit-bigtime-threads-roundup.md` — Reddit snippet roundup (unfetchable here)
- `object-worship-podcast-john-snyder-big-time.md` — annotated lead for the deepest design podcast
- *(MIDI/clock: reuse `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`)*

## Sources

Video (YouTube): Mark Johnston `2kfrZbEbRY8` · CB official `QY389WFTXgY`, Preset Play, `vYclV_Obd-k`
(Quest) · Sonicstate/Superbooth Snyder `1E06eN0A-vM` · Harp Lady `adgcUZ8JJOg` · ambienttrash
`cHQzpkalwS0`.
Official: chasebliss.com/big-time + Big Time manual PDF (10 presets) · electronicaudioexperiments.com/blog (Big Time).
Community: thegearpage.net (Big Time thread) · elektronauts.com (CB megathread t/31096 p.137) ·
modwiggler.com · reddit r/guitarpedals + r/chaseblissaudiophiles (snippet-level) · Object Worship
podcast (John Snyder). CB-stack MIDI: `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`.
