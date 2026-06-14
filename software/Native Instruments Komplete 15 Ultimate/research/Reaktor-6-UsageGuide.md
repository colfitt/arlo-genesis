# Reaktor 6 — Usage Guide

NI's modular powerhouse — and the bundle's best **generative-drone, granular, and self-
patching** engine for this rig. The user has the **full** Reaktor (via Komplete 15
Ultimate), which is what unlocks the Factory instruments, the **User Library** (the single
biggest free ambient resource), and Blocks Primes. The workflow ethos for all of it: **let
it run, record the output, then quantize/EQ the bit you liked.**

## 1. What Reaktor 6 is

`research/links/km-reaktor-blocks-base-and-player.md`, `research/links/km-reaktor-factory-roster.md`
- **Full Reaktor vs the free Player:** Player only *runs* commercial ensembles + Blocks Base;
  **full Reaktor (owned)** adds the **70+ factory instruments**, the build environment, **User
  Library access**, and Blocks Primes. Every free User-Library drone/granular ensemble below
  needs the full version.
- **Primary vs Core** = the two build layers — **Primary** (high-level modules: oscillators/
  filters/envelopes) is all ambient/drone work ever needs; **Core** = sample-by-sample DSP.
- **Factory Library (drone-relevant):** **SpaceDrone** (flagship self-playing drone, 96 voices,
  Geiger-counter random triggering), **Metaphysical Function** (generative "evolving walls"),
  **Newscool** (generative groovebox), **Travelizer** (the granular Sample-Transformer on the
  Grain Cloud module), Photone/Carbon 2/Razor/Prism (pads/metallic).
- **Blocks** = rack-style modular: **30+ Blocks** ship; **Blocks Base** = 24 free modules
  (runs in Player); **Blocks Primes** = premium, free with full Reaktor. Front-panel patching
  since v6.3.

## 2. Generative-drone technique + best ensembles

- **★ The universal recipe:** *generate random control data (sample-and-hold / clocked random)
  → tame it back to musical (note quantizer; coincidental triggers for accents).*
  **Randomize-then-quantize** is the spine of every generative Blocks patch. `research/links/km-reaktor-generative-sequencers.md`
- **Driving SpaceDrone:** for **evolving** → slow the LFO *Speed*, reduce *Dynamic* range,
  raise *Resonance*; for **static pads** → *Density* high, *Rnd* low, *Dynamic* maxed. The
  **Geiger macro** is the self-generating engine. `research/links/km-reaktor-spacedrone-deep-dive.md`
- **★ iorie's capture workflow:** "let it run and record the output until I hear something
  cool, then quantize it and EQ it a little." Use **Metaphysical Function A&B**, change sample
  selection *manually*, and **low-cut** (generative sounds carry subharmonic mud). `research/links/km-reaktor-iorie-generative-workflow.md`
- **Best self-running ensembles:** factory **SpaceDrone** / **Metaphysical Function**; User-
  Library **CRUDE** (Krell buttons → hands-off generative doom-drone + onboard bitcrush/
  distortion), **Space Modulator** ("SpaceDrone on steroids"), **System Flow** / **Drone-E**
  (granular drones). `research/links/km-reaktor-crude-krell-drone.md`, `research/links/km-reaktor-dark-ambient-community.md`

## 3. Processing your own sound (granular + FX ensembles)

- **★ Granular your banjo:** **Travelizer** — double-click the sample window → Sample Map →
  load your audio; the Grain Cloud "explodes the sample into a cloud of grains you move
  around," with **Jitter** on Pitch/Position/Length/Pan (low = frozen drone, high = shimmer).
  Pre-built alternatives: **System Flow**, **GRIP**. `research/links/km-reaktor-travelizer-grain-cloud-granular.md`, `research/transcripts/km-reaktor-grain-cloud-build.md`
- **FX ensembles:** **Molekular** (4-module modular multi-FX + morph/XY — runs in Player too),
  **Flesh** (Tim Exile resynth: analyzes input → re-synthesizes into chords), **The Finger**
  (per-key glitch/stutter/tape-stop). `research/links/km-reaktor-fx-ensembles-molekular-flesh.md`

## 4. Copyable recipes

1. **Instant generative drone (factory):** **SpaceDrone** → slow Speed, low Dynamic, raise
   Resonance → record stereo out → Valhalla VintageVerb + EchoBoy → bed under banjo.
2. **Generative wall (iorie method):** **Metaphysical Function A&B** → let it run, record →
   low-cut the subs, light EQ. (Pair with **Fast FX** = "ambient loop machine.")
3. **Self-patched Blocks drone:** Clock → Clock Divider → Random Gates → **CFG quad envelopes**
   → Low-Pass Gate; **Quad Mod → Quantizer → Dual Waveform Gen** for pitch; cross-feed via
   **Ring Mod**; sum → Reverb. **Slow the Clock + stretch the CFG envelopes → drone, not
   sequence.** Add **Flip Flop (S&H)** / Krell logic for self-running motion. `research/transcripts/km-reaktor-blocks-polyrhythmic-generative.md`
4. **Granular-cloud a banjo:** banjo sample → **Travelizer** → low Position Jitter + long
   grains (sustained) or high Jitter (shimmer) → hold a chord → high reverb → bounce.

## 5. Best demos + User-Library picks

**Video:** ADSR/Salamander Anagram — Grain Cloud build (deepest granular how-to) · Shiro
Fujioka — Blocks polyrhythmic generative · BoBSwanS — Blocks "Distorted Drone Experiment."
**User-Library (full Reaktor only), ranked for this aesthetic:** `research/links/km-reaktor-userlib-picks-scifi-film.md`
1. **CRUDE** (generative doom-drone, Krell + bitcrush) · 2. **SpaceDrone MOD+++** ("Loscil/Ben
Frost walls of noise") · 3. **Drone-E** (granular drone) · 4. **System Flow** (32-grain
granular) · 5. **Space Modulator** · 6. **Cloudlab 200t V2** (Buchla-style) · degrade FX:
**VHS Audio Degradation Suite**, **Grungelator**, **Tape Mate**. **Community consensus: learn
the factory library deeply before chasing User-Library uploads.**

## 6. Pitfalls / gotchas

- **The free Player can't open the User Library or build** — you need the full Reaktor (owned);
  every drone ensemble above requires it. `research/links/km-reaktor-blocks-base-and-player.md`
- **Generative output carries subharmonic mud** — always low-cut.
- **Generative = capture-don't-recreate** — record the run you like (you can't exactly re-roll).
- **CPU** with 96-voice SpaceDrone / big Blocks racks → freeze.

## 7. Captured sources

**Transcripts (2)** — `research/transcripts/`: km-reaktor-grain-cloud-build ·
km-reaktor-blocks-polyrhythmic-generative.
**Links (13)** — `research/links/`: factory-drone-synths · modular-ensembles · granular-system-flow
· spacedrone-deep-dive · crude-krell-drone · generative-sequencers · userlib-picks-scifi-film ·
blocks-base-and-player · fx-ensembles-molekular-flesh · travelizer-grain-cloud-granular ·
iorie-generative-workflow · dark-ambient-community · factory-roster.

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/` (first line =
the original URL). Primary: ADSR/Salamander Anagram, Shiro Fujioka, iorie, 344 Audio, KVR
community, NI factory docs. **Honesty flags:** NI Blocks product/comparison pages 403'd
(recovered via search summaries) — exact Sample-Transformer folder contents + Blocks Primes
module count are best-effort, not manual-verified.
