# Pure LoFi — Usage Guide

Arturia **Pure LoFi** (April 2025) is a lo-fi **synth/sampler** that bakes
degradation *at the source* — not an effect you put on a track. For this rig it's
the one tool that does something the degrade stack (RC-20 / SketchCassette /
Decapitator / Lossy / hardware tape) can't: it **generates** pre-degraded
keys/pads/noise textures to sit *alongside* the banjo. Use it as a sound source,
then (if you want) run its output through the effect chain — its own LoFi Processor
is **not** available as a standalone insert.

> Filed here under Arturia after a repo mis-grouping (`com.arturia.component.Pure-LoFi`);
> see `research/links/purelofi-MISATTRIBUTION-it-is-arturia.md`.

## 1. What it is & signal flow

**2 Engines + a Noise engine → [per-engine EQ → per-engine Hardware mode] → Filter →
LoFi Processor → 4 FX slots → out.** `research/links/purelofi-manual-reference.md`
- **Two engine slots**, each = **Realistic Instrument** (40+ multisamples),
  **Creative Sampler** (5 slots, round-robin/random, loop/reverse, import your own),
  or **LoFi Oscillator** (130+ waves, **Timbre** morph).
- **Per-engine Hardware mode** (digital lo-fi): CMI, Emulator II, Casio SK-1,
  SP-1200, Akai S900, MPC60 + Arturia Deteriorate/Damage/Crush — independent per
  engine.
- **Noise engine:** Texture (looped — rain/vinyl/hiss) or Transient (one-shots);
  190+ noises.
- **Filter:** Clean (Pigments multi-mode) / Analog (Oberheim SEM) / **LoFi**
  (downsampling + Jitter), routable per source.
- **LoFi Processor** (the analog centerpiece, master): 6 coloration modes — Golden
  Age, Velvet Frost, Vintage Glow, Dim Memories, Cathodic Tube, Fuzzy Line — a
  master **LoFi Amount** macro + Drive, Wear, Tone, **Wobble** (wow+flutter),
  Speaker (cab IR), **Vintage** (inter-voice drift).
- **Advanced:** 18 FX (Tape Echo, Trance Gate, Super Unison…), drag-and-drop
  modulators, 4 Macros, MPE. 250+ presets. (Built on the Pigments engine.)

## 2. Essential workflows

- **★ Drone/texture-bed render** (the move that maps to this rig): turn OFF both
  oscillators so only the **Noise engine** sounds → hold a note → continuous
  texture → **bounce to audio** to layer into a wall. Route the per-source filter so
  you *filter the tonal layer but leave the noise unfiltered* ("filter the bass,
  leave the noise frying eggs in the background"). `research/links/purelofi-community-tips-and-presets.md` `research/links/purelofi-arturia-sound-design-presets.md`
- **LoFi-Amount-as-envelope:** drag the amp ADSR onto **LoFi Amount** so degradation
  hits on the transient then clears up (or backs off after attack). `research/transcripts/purelofi-woody-piano-shack-walkthrough.md`
- **Creative Sampler, random-trigger pads:** taped-piano samples, different sample
  per note, vibrato + filter driven by **vinyl-rotation-derived LFO speeds** (~33⅓
  rpm) for expressive, non-static pads. Import your own samples here. `research/links/purelofi-arturia-sound-design-presets.md`

## 3. Signature settings & presets (factory-designer recipes)

`research/links/purelofi-arturia-sound-design-presets.md`
- **Subtle tape warmth** — *Golden Age*, low LoFi Amount, light Wear; or a simple pad
  through **Dim Memories** for density/warmth ("Snow Ghosts" approach).
- **Warped/wobble drone** — *"Somber Mood"*: harp/plucked source → LoFi Processor
  heavy on **Wear + Wobble + Vintage** → long reverb → a **Movement macro**.
- **Washed lo-fi / "recorded-wrong"** — *"Little Pleasures"*: sine + noise texture
  through tape processing, **Timbre macro + aftertouch + mod-wheel** riding the
  degrade.
- **Ambient starting preset** — *"It Blossoms"* (lost-keys pad, slow pitched delays,
  big reverb). `research/links/purelofi-community-tips-and-presets.md`
- **Workflow:** swapping coloration modes **keeps your 6 param values** (changes
  character, not amount); the **per-engine EQ sits *before* the Hardware mode**, so
  it strongly shapes which artifacts appear; combine **different Hardware modes
  across the two engines** for layered grit. `research/transcripts/purelofi-arturia-official-overview.md`

## 4. Power-user tips, tricks & hidden features

- **Timbre / Brightness macros** = a one-knob "more/less degraded" + filter flavor
  (the closest thing to RC-20's Magnitude, but it shapes an *instrument's* output). `research/transcripts/purelofi-sound-test-room-walkthrough.md`
- **An underlined knob = it's being modulated.** Drag-and-drop modulators (ADSR,
  Function, Random, Voice Modulator, Mod Sequencer) onto any param. `research/transcripts/purelofi-catsynth-tv-tutorial.md`
- **Limitation to know:** you **can't modulate a modulator's amount** (Pigments 6
  can) — a real constraint for evolving generative patches. `research/transcripts/purelofi-molten-music-review.md`

## 5. Notable users & techniques

Honest: it's a **2025 instrument with a thin community** — **no verifiable named
drone/doom/shoegaze artist** uses it; usage is hobbyist chillhop/ambient level.
Nothing invented. Relevance is by technique + the factory-designer recipes above. `research/links/purelofi-overview-spec-and-cdm.md`

## 6. Rig-specific recipes (your gear by name)

- **Pre-degraded pad/keys under the banjo** — generate a nostalgic Rhodes/pad here
  (Realistic Instrument → Dim Memories), play it as the bed; the banjo stays the
  lead. The one thing the effect stack can't do (it has no sound of its own).
- **Noise-bed → into the degrade chain** — render the noise-engine texture to audio,
  then treat it like any stem (Decapitator/RC-20/Valhalla) if you want *more* grit —
  but usually it's already enough.
- **Import hardware samples** (OP-1 / Digitakt / MPC / Octatrack one-shots) into the
  **Creative Sampler**, random-trigger them, and degrade at the source — a playable
  lo-fi instrument built from your own rig recordings.

## 7. Best learning resources

1. **CatSynth TV — "embrace imperfection!" (34 min)** — deepest control-by-control.
2. **Molten Music (Robin Vincent) — review (60 min)** — best aesthetic read + the
   "it's a synth / wish the LoFi Processor were a standalone effect / can't-modulate-
   a-modulator" insights.
3. **Arturia official "Pure LoFi — Overview" (Kari, 22 min)** — authoritative; the
   EQ-before-Hardware-mode + combine-Hardware-modes tips.
4. **Woody Piano Shack (27 min)** — the ambient/slow-playing angle + the LoFi-Amount-
   as-envelope trick.
5. **The Sound Test Room (42 min)** — drag-and-drop modulation workflow.

## 8. Common pitfalls / gotchas

- **It's an instrument, not an effect** — there is no master-bus/stem/insert use; the
  **LoFi Processor is NOT a standalone effect** (can't put it on the banjo). `research/transcripts/purelofi-molten-music-review.md`
- **Launch QC drift** — the bundled tutorial demos features that don't behave as
  shown; **Advanced-FX modules can read greyed-out even when powered on**;
  inconsistent UI (double-click to select in Noise, different elsewhere). Use
  external tutorials. `research/links/purelofi-community-tips-and-presets.md`
- **Can't modulate a modulator's amount** (Pigments can) — limits deep generative
  patches.
- **Preset-bank caveat:** the free fan bank ("Purification") was pulled; the official
  "Lofi Explorations" bank is **Pigments**-based — verify Pure LoFi compatibility
  before buying. `research/links/purelofi-overview-spec-and-cdm.md`

## 9. Captured sources

**Transcripts (5)** — `research/transcripts/`: purelofi-arturia-official-overview
(authoritative tutorial) · purelofi-catsynth-tv-tutorial (deepest 3rd-party map) ·
purelofi-molten-music-review (aesthetic read + scope limits) · purelofi-woody-piano-
shack-walkthrough (ambient + LoFi-Amount-envelope) · purelofi-sound-test-room-
walkthrough (drag-and-drop modulation).

**Links (5)** — `research/links/`: purelofi-manual-reference (148-pp manual: full
control set + signal flow) · purelofi-arturia-sound-design-presets (9 named factory
recipes) · purelofi-community-tips-and-presets (noise-bed render trick, UI/QC
gotchas) · purelofi-overview-spec-and-cdm (spec snapshot + editorial) ·
purelofi-MISATTRIBUTION-it-is-arturia (the Arturia-not-Cableguys evidence + scanner
bug trace).

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/`
(first line of each = the original URL). Primary: Arturia manual + official overview,
CatSynth TV, Molten Music Technology, Woody Piano Shack, The Sound Test Room, CDM.
**Honesty flags:** ~2-month-old instrument → thin community, no named drone/ambient
artist verified (relevance by technique + factory recipes); the free fan preset bank
was pulled; the official extra bank may be Pigments-only.
