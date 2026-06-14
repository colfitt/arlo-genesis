# Antares Auto-Tune Unlimited — Usage Guide (creative / sound-design angle)

Auto-Tune Unlimited is the rig's **vocal-tech-as-sound-design** axis — a subscription bundle
of 22 plugins whose pop-vocal job (transparent tuning) is *not* why it's interesting here. For
a drone/doom/shoegaze rig the value is the **off-label** use: Auto-Tune-as-effect (the
robotic snap) on voice **or a monophonic banjo/synth line**, and the **AVOX** suite + **Harmony
Engine** + **Vocodist** as texture/drone/choir generators that turn one held note into a wall.
Honest scope: ~90% of all Antares docs assume a rap/pop lead vocal — the creative recipes below
are supported by the engines but are genuinely under-documented (no verified drone/doom/shoegaze
artist credits found). Tier-C single-pass; relevance is by *capability + technique*, not a
genre-peer endorsement. `research/links/antares-bundle-roster-and-reach-for.md`

## 1. The bundle — what's installed (creative reach-for map)
From `CONTENTS.md`: 22 plugins (AU + VST3) + 2 apps. By job, with ★ = reach-for creatively:

- **Pitch engines:** ★ Auto-Tune **Pro X** (flagship; Auto + Graph, Classic Mode) · ★ **EFX+**
  (effect-first, fastest robotic) · Artist / Access (slimmer tiers) · ★ **Slice** (slice+pitch
  a phrase into a playable instrument) · **Auto-Key** (key/scale detector).
- ★ **AVOX suite (the prize):** ★★ **MUTATOR** (alien/monster — ring-mod + throat + reverse-chop)
  · ★★ **THROAT** (beyond-anatomy formant reshaping) · ★★ **CHOIR** (1 → up to 32 unison voices)
  · ★ **DUO** (auto double) · ★ **ARTICULATOR** (2-input vocoder) · ASPIRE (breath) · PUNCH (comp)
  · ★ **WARM** (tube/tape sat — usable on anything).
- ★ **Standalone creative:** ★★ **Harmony Engine 4x** (4-voice harmony + per-voice choir
  multiplier + freeze; works on instruments) · ★★ **Vocodist** (20-model vocoder + carrier synth)
  · ★ **Mic Mod** (mic-modelling coloration).
- **Vocal-mix utilities (mostly skip):** Vocal Compressor / EQ / De-Esser / Reverb / SoundSoap
  (denoise) / Vocal Prep app — competent but the rig already has Valhalla/Decapitator/etc.

Reach-for-by-job table: `research/links/antares-bundle-roster-and-reach-for.md`.

## 2. Auto-Tune AS AN EFFECT (the hard-retune / robotic move)
The audible part of Auto-Tune is the *transition between notes* — so the effect is loudest on
glides, scoops, and short/sloppy notes, quietest on long held ones. The recipe (Pro X / Artist /
EFX+): `research/links/antares-autotune-as-effect-recipe.md`

- **Retune Speed = 0** (fastest) — THE setting. Zero smoothing → instant snap to the scale note,
  stepped/synth-like. (20–40+ = natural; 0 = robot.)
- **Flex-Tune = 0** (no note protection) · **Humanize = 0** · **Natural Vibrato = 0** — kill
  every "make it natural" control.
- **Classic Mode = ON** — brighter tone + prominent attack/transition at fast speeds = "extremely
  robotic."
- **Scale/Key:** tight major/minor snaps hard; **remove notes** from the scale to force bigger
  jumps = more dramatic stepping; **Chromatic** = least. Use **Auto-Key** to detect, or set wrong
  on purpose for designed alien melodies.
- **Technique > settings:** add scoops between notes, don't hold sustains, push the input off-
  pitch — the further from the scale note, the bigger the snap. Bounce-and-re-run for double steps.

**On non-vocal sources (the rig angle):** the engine tracks any **monophonic** signal — a synth
lead, a single-note banjo/baritone line, a slide swell, fretless bass. Forum consensus: auto-tuned
fretless "sounds synthy," and "used abusively for effect" it gets alien/funky. **Needs a clean
mono signal** (no chords, minimal bleed) — banjo *strums* won't track; single-note picking/slides
will. Mutator's input control even labels the range "vocal **or instrument**."
`research/links/antares-autotune-as-effect-recipe.md`, `research/transcripts/antares-mutator-wavy-wayne.md`

## 3. ★ AVOX + Harmony Engine for sound design / drones

### MUTATOR — alien / monster / inhuman texture (the #1 sound-design tool)
Three sections (`research/transcripts/antares-mutator-wavy-wayne.md`, `research/links/antares-avox-sos-review.md`):
- **Voice Design:** Pitch Shift (±24 semitones / ±2 oct) · **Throat Length** (lengthen→formants
  down) · **Throat Width** (narrow/widen→formants move). Input range = vocal *or instrument*.
- **Mutation:** one knob steps through **24 pitch-tracking ring-modulation** mutations (metallic,
  inharmonic, robotic) + a **Mutant Mix** wet/dry blend.
- **Alienize:** on/off, **tempo-syncable**; a **Dialect** control sets the length of speech
  segments that get **time-reversed** and blended back → chopped/backwards/glitch texture.
- *Use:* Darth-Vader (pitch + mutation), full alien (everything up), monster growl. On a sustained
  drone or banjo drone, low Mutant Mix + a subtle mutation + Alienize off = a metallic detune that
  sits *under* the wall; everything up + Alienize on = a backwards-glitch creature bed.

### THROAT — designed / impossible formants
Neutralises the source tract, then **stretch/shorten/widen/constrict** a modelled one; a
**5-point graphical throat display** (cords→throat→mouth→lips) + **glottal waveform** +
**breathiness** noise. Controls go **beyond human anatomy** → vocal-tract timbres that don't
exist. Pair with pitch-shift to hold (or deliberately wrong) the formants. Great for morphing a
voice/instrument into a gendered-wrong, hollow, or vowel-locked drone colour.
`research/links/antares-avox-sos-review.md`

### CHOIR — one note → choir/drone wall
**Choir Size 4/8/16/32** unison voices from one mono source; **Pitch / Timing / Vibrato Variation**
(tight double → swimmy detuned wall) + **Stereo Spread**. Hold one sustained note (banjo, voice,
synth), Choir at 16/32 with moderate variation = a shimmering self-detuned bed; multiple instances
on different held pitches = a stacked choral chord. Push variation for a chorused, almost-granular
wash. `research/transcripts/antares-choir-evo-demo.md`, `research/links/antares-avox-sos-review.md`

### HARMONY ENGINE 4x — playable choral / drone beds (works on instruments)
Four Harmony Voices, each w/ its own **interval (±2 octaves)**, character/throat, vibrato, pan,
formant, mute. **Control modes:** Fixed/Scale Interval (set key+scale like Auto-Tune) · Chord
Degrees · Chord Name (inversions) · Chord-by-MIDI · **MIDI Omni** (play the 4 voices like a synth)
· MIDI Channel (one voice/channel). Built-in **Choir** multiplies *each* voice ×2/4/8/16, **Throat**
modelling per voice, and a **Freeze** (Formant-Only or Formant+Pitch) to sustain. Harmonises a
single **vocal OR monophonic instrument** → feed a banjo/synth line and get an instant 4-part (or
choir-multiplied = up to 64-voice) bed; or play clusters from the 61SL MkIII in MIDI Omni and
**Freeze** them into a held drone-choir. `research/transcripts/antares-harmony-engine-full-tutorial.md`, `research/links/antares-avox-sos-review.md`

### VOCODIST — synthetic talking-instrument / machine-choir
Vocoder (20 vintage models) + **internal MIDI synth carrier** (8-voice, dual-osc) OR **external
side-chain carrier** OR **voice-pitch-tracking** carrier; **band count, min/max freq, 4 filter
shapes, Q, Stretch, Slide**; **saturation, ring-mod, chorus, noise** on the output; automatable
X-Y pad. Feed a **drone/pad/hardware-synth chord as the external carrier** and a voice or banjo as
the modulator → a robotic, vowel-shaped texture that follows the played line. Few bands + slow
attack/release + chorus/sat = an evolving metallic "machine-choir." `research/links/antares-vocodist-review.md`

### Supporting: DUO (single tight double) · ARTICULATOR (2-input talkbox vocoder) · WARM (tube
"Velvet"/valve "Crunch" saturation on any source) · ASPIRE (breath add/subtract) · MIC MOD (model a
weird/cheap mic onto a clean source as EQ-with-attitude). `research/links/antares-avox-sos-review.md`

## 4. Copyable recipes (creative, this rig)
1. **Hard-tune-as-effect (voice or mono line):** Auto-Tune Pro X / EFX+ → Retune Speed **0**,
   Flex-Tune **0**, Humanize **0**, Natural Vibrato **0**, **Classic Mode ON**, tight or sparse
   scale. Print it; for double-step artifacts, bounce and re-run. Best on a single-note banjo/synth
   slide, not chords.
2. **Choir/drone wall:** sustained source → **CHOIR**, Size **32**, Pitch+Timing+Vibrato Variation
   moderate-high, Stereo Spread wide. Layer 2–3 instances on different held notes for a chord. Add
   Valhalla VintageVerb (long decay) after for the shoegaze smear.
3. **Played choral bed (Harmony Engine):** Harmony Engine 4x in **MIDI Omni**, play a cluster from
   the 61SL MkIII, turn each voice's **Choir** multiplier to 8/16, hit **Freeze (Formant+Pitch)** →
   a held, breathing drone-choir from one banjo/synth input.
4. **Alien / inhuman texture (Mutator):** **MUTATOR** → step the **Mutation** knob to a metallic
   ring-mod variety, dial Throat Length/Width for the inhuman vowel, **Alienize ON + tempo-synced**
   with a short **Dialect** for backwards-chop glitch. Low Mutant Mix to sit it under a drone, full
   for a foreground creature.
5. **Vocodist machine-choir:** route a **drone/pad** to Vocodist's **external carrier** side-chain,
   modulator = voice/banjo; few bands, slow attack/release, add **chorus + a little ring-mod**.
6. **Designed alien melody:** Auto-Tune Pro X **Graph mode** — draw notes to *wrong* targets / a
   custom scale so the source steps through an inhuman melody.

## 5. Best demos / resources (honest: pop-vocal-skewed)
1. **Wavy Wayne — "Introduction to Antares Mutator"** (official) — clean control-by-control tour of
   Voice Design / 24 Mutations / Alienize; confirms vocal-OR-instrument input. The best Mutator
   reference. `research/transcripts/antares-mutator-wavy-wayne.md`
2. **Justin Elmo — "How To Use Antares Harmony Engine Evo (Full Tutorial)"** — long, thorough run
   through every control mode, the per-voice Choir, glide/timing, Freeze, instrument harmonising.
   `research/transcripts/antares-harmony-engine-full-tutorial.md`
3. **Music Tech Help Guy — "Antares CHOIR Evo"** — practical 4/8/16/32 + variation/spread demo on a
   real mix. `research/transcripts/antares-choir-evo-demo.md`
4. **Antares "How to get the signature Auto-Tune effect" + HomeMusicCreator/Audio Sorcerer/Nail The
   Mix** — the converging hard-retune recipe. `research/links/antares-autotune-as-effect-recipe.md`
5. **Sound On Sound "AVOX 2" review** — the per-module "beyond-natural / special-effect" verdicts.
   `research/links/antares-avox-sos-review.md`
6. **SoundOnSound / Mixonline "Vocodist" reviews** — full vocoder + carrier-synth control set.
   `research/links/antares-vocodist-review.md`

## 6. Rig-specific recipes & pitfalls
- **Logic Pro (AU):** all 22 are AU. Auto-Tune/Mutator/Throat track a **mono** insert — print the
  effect (or freeze the track) since pitch-tracking + ring-mod are CPU-heavier than a static plugin.
  Choir/Harmony Engine multiply voices = watch CPU at 32-voice / choir-multiplied settings; freeze.
- **Banjo-as-lead / baritone:** single-note picking or slides track fine; **strums/double-stops
  won't** (mono engine). Comp a clean mono lead take, then hard-tune or Mutator it; for chords, use
  Choir/Harmony Engine (which *generate* the harmony) instead of trying to tune a chord.
- **Hardware front-end / reamping:** record the pedalboard or OP-1/Digitakt/MPC/Octatrack clean,
  then add Auto-Tune/Mutator/Choir on the return as the *synthetic* layer the analog chain can't
  make. Vocodist's external-carrier side-chain is perfect for vocoding a played part onto a
  hardware-synth drone (VG-800 / S08).
- **61SL MkIII:** drive Harmony Engine (MIDI Omni / Chord-by-MIDI) and Vocodist's internal synth
  from the controller to *play* the choral/vocoded beds.
- **Ableton Live 12 Lite (secondary):** works as VST3/AU; bounce/resample heavy multi-voice chains
  to stay under Lite's track ceiling.
- **Gotchas:** subscription-only (lapse = plugins stop authorizing); ~all presets/tutorials are
  pop-vocal so creative use is DIY; the mono-tracking limit is the big one; vocal-mix utilities
  (Comp/EQ/De-Esser/Reverb) are redundant with the rig's existing tools.

## 7. Captured sources
**Transcripts (3)** — `research/transcripts/`: antares-mutator-wavy-wayne (official control tour,
vocal-OR-instrument) · antares-harmony-engine-full-tutorial (deep: every control mode, Choir
multiplier, Freeze, instrument harmonising) · antares-choir-evo-demo (4/8/16/32 + variation/spread).
**Links (4)** — `research/links/`: antares-autotune-as-effect-recipe (hard-retune values + non-vocal
use) · antares-avox-sos-review (per-module controls + beyond-natural verdicts) · antares-vocodist-
review (vocoder + carrier-synth control set) · antares-bundle-roster-and-reach-for (installed roster
+ reach-for-by-job map + honesty flags).

## Sources
Primary: Antares official product/effect pages (Mutator, Throat, Choir, Harmony Engine, Vocodist,
Auto-Tune-effect guide — JS-rendered, distilled via search summaries + the captured videos), Sound
On Sound (AVOX 2, Vocodist), Mixonline, Synth & Software, HomeMusicCreator, Audio Sorcerer, Nail The
Mix, Sweetwater/SoundTools quickstart, TalkBass/Gearspace (non-vocal forum lore), and the three
captured YouTube tutorials. **Honesty flags:** (1) overwhelmingly pop/rap-vocal documentation — the
creative/drone/non-vocal recipes are extrapolated from engine capabilities + general technique, not
genre-specific tutorials; (2) **no verified drone/doom/shoegaze artist credit** for any of these
tools — relevance is by capability, not endorsement; (3) Antares' own pages are JS-walled so several
product-spec details were cross-confirmed via SoS/retailer summaries + the captured videos rather
than fetched directly; (4) the "Mutator: Extreme Voice Designer" promo clip was found but discarded
(71-word advert, no usable instruction); (5) Mic Mod / Hybrid specifics are light — included from the
roster but with thinner sourcing than the headline AVOX modules.
