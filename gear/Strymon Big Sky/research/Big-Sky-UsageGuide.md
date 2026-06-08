# Strymon Big Sky — Usage Guide

The Big Sky is the End board's **reverb workstation** — 12 machines, 300 presets, deep
per-machine params, and the rig's core ambient/shimmer wall. The throughline from every
on-aesthetic user (Hammock, Andy Othling) is the same: **run it last in the chain, stack
delays into it, map EXP/MIDI to its parameters, and play 100% wet + Freeze to turn the
banjo/baritone into a pad.** It pairs with the TimeLine for wash-on-wash, follows the
Digitakt's clock (Pre-Delay), and is managed offline in **Nixie 2** (`.syx`). The clearest
machine-by-machine reference is Rabea Massaad's official 14-part series; the best drone
technique is Antoine Michaud's Freeze/Infinite + frozen-wall videos.

> Front-panel: **MIX 3:00 = 50/50** (25–40% for subtle ambience); per-machine the two PARAM
> knobs + a hidden menu carry deep params; firmware is frozen at **v1.49 (Mar 2019)**.
> **Hold is per-preset: Freeze vs Infinite (see §1).** The original Big Sky is **single-engine,
> no USB** (Nixie needs a real MIDI interface).

---

## 1. Essential workflows

### The 12 machines (PARAM maps + signature settings)
- **Room** — PARAM1 Low End, PARAM2 Size (Studio/Club); menu Diffusion + Boost. **Hall/Plate/
  Spring** = the naturalistic cores. *(rabea-overview)*
- **Swell** — brings the reverb in behind the dry; **Mode = swell the reverb (subtle) OR swell
  the dry INTO the reverb ("Dry mode" — hides the pick attack entirely)**. The banjo-pluck eraser. *(rabea-swell)*
- **Bloom** — PARAM1 Low End, PARAM2 Length; menu **Feedback** sets bloom size. You hear the
  attack, then it blooms around everything — stays uncluttered with fuzz in front. *(rabea-bloom)*
- **Cloud** — PARAM1 Low End, PARAM2 Diffusion; the Strymon "signature" smooth wash, deliberately
  sparse; great at **zero dry** as a synth-pad. *(rabea-cloud)*
- **Chorale** — vowel/choir machine (PARAM1 Vowel, Reso); Hammock's *Mysterium* go-to. *(chords-of-orion)*
- **Shimmer** — **two fully tunable voice intervals** (PARAM1/PARAM2) + menu **Amount** + **Mode
  (Input / Regeneration / In+Reg)**; REGEN "finds the harmonies you play" and **swells after the
  attack**. Play in-key or freeze a fifth as a drone. *(rabea-shimmer)*
- **Magneto** — multi-head tape delay-reverb: menu **Heads 3/4/6** + **Spacing Even (rhythmic) /
  Uneven (textural)**; **Pre-Delay = Feedback** (toward max = sustained drone); pair with a delay
  footswitched on/off. *(rabea-magneto)*
- **Nonlinear** — menu **Shape** (Ramp/Reverse/…), **Late Decay + Late Level** (a 2nd reverb
  underneath), **Mod Speed**; **Decay = Time, Pre-Delay = Feedback** here. The drone-wall engine. *(antoine-trippy-frozen)*
- **Reflections** — 250-tap psychoacoustic small room (Loc X/Y, Shape). *(dossier §; see QC note)*

### Hold: Freeze vs Infinite (the key distinction)
Push VALUE → past Boost/Persist → **Hold → Freeze or Infinite** (per preset). **Infinite** =
held pad PLUS everything you play is added → goes chaotic fast. **Freeze** = held pad, but your
playing on top is **completely dry** (clean to solo over). Two fixes for the "dry on top"
problem — **both rig-critical:**
1. **Put a reverb/delay BEFORE the Big Sky**, Freeze the chord, and the lead on top gets ambience
   from the upstream unit (e.g. the TimeLine feeding a frozen Cloud/Bloom).
2. **Looper AFTER the Big Sky:** Freeze → record the frozen pad → release → change patches and jam
   over the captured loop. *(antoine-infinite-vs-freeze)*

### The drone wall (Antoine "Trippy Frozen Reverbs")
**Nonlinear, Ramp shape, Time + Feedback + Mix maxed, 100% wet, very long decay, dark Tone**, add
slow **Mod**; **volume-swell in** with the guitar volume; **Freeze + loop** underneath. Turning
Decay/Time live = morphing motion. Space chords apart — long tails go dissonant fast. *(antoine-trippy-frozen)*

---

## 2. Signature presets & settings

**Sharing format = `.syx`** (same ecosystem as the TimeLine); manage with **Nixie 2** (backup/
organize/import/firmware). ⚠️ **Original Big Sky has no USB — Nixie needs a real MIDI interface**
(Roland UM-ONE MKII / iConnectivity mio / Strymon Conduit); GLOBLS **MIDI PA=ON, CT=ON, TH=MERGE,
ST=OFF**. Import: File → Presets → Import → write to a slot (no in-app cloud browser on the
original). *(strymon-nixie2-preset-sharing-import)*

**Official "This Week's Preset" (free `.syx`, with stated settings):** *(strymon-bigsky-this-weeks-preset-series)*
- **Ever After (Shimmer)** — Shift1 **+2 OCT**, Shift2 **−1 OCT**, Decay **13.7 s**, Amount ~50%, Mode **INPUT** (great on a synth/VG-800 pad).
- **Star Cloud (Cloud)** — **Mod 2:00** (max depth/slowest speed), played **zero dry**, EXP→Tone.
- **Falling Angel (Shimmer)** — **Mode REGEN**, Tone cranked, Mod ~halfway → descending shimmer; EXP→Mix.
- **Late Bloomer (Bloom)** — Pre-Delay high, Length long, Mix ~3:00; raise Feedback+Decay for bigger.

**Factory presets (exact machine + decay):** Cloud **"For Days" = 50.0 s + Freeze** (instant drone),
Shimmer **"Detune Verb" = ±10 cents detune** (the manual's detune trick baked in), Shimmer
"Stardust" Oct5th/+Oct REGEN 13.7 s, Magneto "6 Marblet" 6-heads/Uneven. *(strymon-bigsky-factory-presets)*

**Chords of Orion Chorale swell (verified from video):** Chorale, Decay ~6 s, Pre-Delay 10:00, Mix
~noon, **Vowel = "HA"**, Reso Medium, Mod noon–1:00 — the "synthy choir behind a reverb." *(chords-of-orion)*

**Where to get more:** the **factory-preset PDF** (free, on-aesthetic starting library), **TWP**
(free official), and paid `.syx` packs (Tone Shepherd, Sam Wittek, and the **Hillsong Hendroff/Peter
James** pack — worship-ambient but the swell/pad machines transfer to drone). *(bigsky-community-preset-packs)*

---

## 3. Power-user tips, tricks & hidden features

- **Star Cloud move:** Cloud, **Mod at 2:00** = max depth + slowest speed = deep shimmer without
  obvious wobble; run zero dry as a pad. *(strymon-this-weeks-preset-ambient-recipes)*
- **Magneto drone:** crank the **Pre-Delay knob (= Feedback)** toward max for a sustained drone;
  high Diffusion smears the multi-head echo into reverb. *(community-magneto-cloud-drone)*
- **Shimmer REGEN swells after the attack** — ideal for held drone chords; **freeze a tuned fifth**
  as a bed under a banjo lead. *(rabea-shimmer)*
- **Bloom EXP→Tone** (Tone is a synth-like resonant filter cutoff in Bloom) for a sweepable wash. *(strymon-this-weeks-preset-ambient-recipes)*
- **Bloom/Swell are reversible** for backwards pedal-steel effects. *(sos-soundonsound-review)*
- **MIDI infinite-hold latch** from a controller (Toggle mode) so you don't have to hold the switch. *(strymon-midi-clock-predelay-sync)*

---

## 4. Notable users & techniques

- **Hammock (Marc Byrd / Andrew Thompson)** — the rig's blueprint: Big Sky + TimeLine + Deco + Flint;
  **Chorale** was the *Mysterium* go-to. Technique: **two-person live knob manipulation as
  performance** (one plays, one rides knobs / unplugs cables), **stereo doubling** (stereo wash +
  mono-right trip + dry-ish mono-left), 12+ multitracked "guitar symphony" parts — and they play
  **baritone + Jazzmaster** (your instruments). *(hammock-bigsky-ambient-technique)*
- **Andy Othling (Lowercase Noises)** — Big Sky **last after the TimeLine**, MIDI-controlled with
  **EXP mapped to parameters**; philosophy = "**non-guitar, even non-musical** sounds to fill the
  space," stacking 2–3 delays into a soupy wall. *(lowercase-noises-bigsky-ambient-technique)*
- **Strymon ambient roster** (Todd Madson — end-of-chain; Forum/Tyler — Big Sky on glockenspiel;
  Ethan Tufts — authored Ever After/Late Bloomer). *(strymon-ambient-artists-feature)*
- **Throughline:** Big Sky **last in chain, delays stacked into it, EXP/MIDI on params live, 100%
  wet + Freeze** to turn the source into a pad.

---

## 5. Rig-specific recipes

- **Wash-on-wash with the TimeLine:** Hammock run the delay *after* the Big Sky (smear the wall);
  Antoine's Freeze fix runs a reverb/delay *before* (ambience on top of a frozen pad). **Both work**
  — after = wash-on-wash smear; before = leads-over-Freeze get ambience. *(hammock, antoine-infinite-vs-freeze)*
- **Banjo-as-lead pad:** **Swell in Dry mode** erases the EBM-5's pluck → instant pad; under it,
  **freeze a Shimmer fifth** (REGEN) as a drone bed. *(rabea-swell, rabea-shimmer)*
- **Baritone drone wall:** the **Nonlinear Ramp + maxed + Freeze + volume-swell + dark Tone + slow
  Mod** recipe; dark Tone tames the baritone's long-tail metallic buildup. *(antoine-trippy-frozen)*
- **Clock from the Digitakt:** Big Sky follows incoming clock on **Pre-Delay** (per-preset); on
  Magneto/Nonlinear the clock drives **Decay** instead. Leave **MIDI CL OFF** on fixed-Pre-Delay
  drone presets so a transport PLAY doesn't reset them. *(strymon-midi-clock-predelay-sync)*
- **Feed it at the right level:** the VG-800's hot line-level output **clips the +8 dBu input (no
  input trim)** — attenuate upstream / use the **EHX Effects Interface**. *(strymon-input-level-clipping-line-level)*
- **Magneto + a footswitched delay** (TimeLine/Big Time) = rhythmic broken/degraded textures
  (Rabea's explicit recommendation), on-brand for the tape-print philosophy. *(rabea-magneto)*

---

## 6. Best learning resources

- **Strymon (official) — Rabea Massaad 14-part series** — the canonical per-machine reference (PARAM
  maps, each machine cleanly).
- **Antoine Michaud** — the best *technique* videos (Freeze vs Infinite; the frozen drone-wall recipe).
- **Chords of Orion** — ambient swells + the Chorale patch; on-aesthetic.
- **Strymon "This Week's Preset"** (free `.syx` + stated settings) + the **factory-preset PDF** — best
  concrete recipes; **Nixie 2** is the librarian.
- **Communities:** **Morningstar forum** (MIDI infinite-hold latching, tap/Pre-Delay conflicts),
  **Strymon firmware notes**, **Sound on Sound** review (deep feature detail). TGP/gearspace gated;
  Reddit doesn't index to search. *(rabea-*, antoine-*, chords-of-orion, strymon-this-weeks-preset, strymon-midi-clock-predelay-sync, sos-soundonsound-review)*

---

## 7. Common pitfalls / gotchas

- **5-second spillover rule:** a preset must be active ~5 s before its tail spills into the next —
  fast stomps cut trails. **Persist=ON forces buffered bypass.** *(strymon-spillover-persist-freeze)*
- **Input clipping on hot/line-level sources** (+8 dBu max, **no input trim**) — attenuate the VG-800
  upstream / EHX FXI. *(strymon-input-level-clipping-line-level)*
- **Bypass LED goes dark** — you can't see the loaded preset; live recall leans on the MIDI
  controller's display. *(sos-soundonsound-review)*
- **Magneto/Nonlinear remap the knobs** (Pre-Delay→Feedback, Decay→Time) — surprises muscle memory. *(strymon-midi-clock-predelay-sync)*
- **MIDI transport PLAY + clock can reset hand-dialed Pre-Delay** — leave MIDI CL OFF on fixed-Pre-
  Delay drone presets. *(strymon-midi-clock-predelay-sync)*
- **No USB on the original** — Nixie needs a real MIDI interface (most plug-and-play cables fail). *(strymon-nixie2-preset-sharing-import)*
- **Long Nonlinear/Shimmer tails go dissonant** if chords overlap — space them harmonically. *(antoine-trippy-frozen)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `rabea-massaad-bigsky-pedal-overview.md` — front-panel/menu/workflow (VALUE, PARAM menu, Persist/Hold/Spillover)
- `rabea-massaad-bigsky-swell-reverb.md` — Swell reverb-swell vs dry-swell modes
- `rabea-massaad-bigsky-bloom-reverb.md` — Bloom PARAM map + attack-then-bloom behavior
- `rabea-massaad-bigsky-cloud-reverb.md` — Cloud PARAM map + signature wash
- `rabea-massaad-bigsky-shimmer-reverb.md` — Shimmer two tunable voices, Amount, Input/Regen modes
- `rabea-massaad-bigsky-magneto-reverb.md` — Magneto Heads/Spacing, Pre-Delay=Feedback, delay-pairing
- `antoine-michaud-bigsky-infinite-vs-freeze.md` — Freeze vs Infinite + the two ambience fixes
- `antoine-michaud-bigsky-trippy-frozen-reverbs.md` — full drone-wall recipe (Nonlinear Ramp, freeze+loop)
- `chords-of-orion-bigsky-timeline-ambient-swells.md` — Chorale swell patch (exact) + TimeLine pairing

**Links** (`research/links/`)
- `strymon-bigsky-factory-presets.md` — full factory catalog (machine/decay/menu params), drone subset called out
- `strymon-bigsky-this-weeks-preset-series.md` — official named presets w/ stated settings (Ever After, etc.)
- `strymon-this-weeks-preset-ambient-recipes.md` — Star Cloud / Bloombient / Falling Angel recipe detail
- `strymon-nixie2-preset-sharing-import.md` — Nixie 2 `.syx` import + non-USB MIDI connection
- `strymon-nixie-editor-librarian.md` — Nixie editor/librarian capabilities (original Big Sky)
- `bigsky-community-preset-packs.md` — paid/community `.syx` pack survey (incl. Hillsong)
- `strymon-bigsky-product-machine-descriptions.md` — official Cloud/Bloom/Shimmer/Magneto + zero-dry-pad
- `strymon-firmware-revision-history.md` — full 1.15→1.49 changelog + the Reflections-claim flag
- `strymon-midi-clock-predelay-sync.md` — clock→Pre-Delay/Decay, CC map, infinite-hold latch, transport-reset
- `strymon-input-level-clipping-line-level.md` — line-level/synth clipping gotcha + fixes (VG-800)
- `strymon-spillover-persist-freeze-behavior.md` — 5-sec rule, Persist vs Spillover, Freeze vs Infinite
- `community-magneto-cloud-drone-techniques.md` — Magneto-drone, Cloud diffusion, Shimmer self-build
- `sos-soundonsound-review-deep-features.md` — analog dry path, per-machine character, LED quirk
- `strymon-ambient-artists-feature.md` — ambient-artist roundup running Big Sky
- `hammock-bigsky-ambient-technique.md` — Hammock Chorale + two-person knob manipulation + stereo doubling
- `lowercase-noises-bigsky-ambient-technique.md` — Andy Othling end-of-chain/textural/EXP-mapped technique
- `guitar-chalk-bigsky-settings.md` — 5 starting-point patches (QC-flagged SEO-generic)

## Sources

Video (YouTube): Rabea/Strymon `G2Y-UYboLes`, `0HxOKRh9jyo`, `U4fPrQWF35Y`, `VEZb_dk_xRE`,
`BsOeuN9dRco`, `sRXEQExqsdc` · Antoine Michaud `GYo2VkFiYYE`, `Te_Ma0gX9g8` · Chords of Orion `zl9QcSEHB8w`.
Official: strymon.net (Big Sky product, factory-preset PDF, "This Week's Preset", Nixie 2 support,
firmware release notes) · midi.guide. Community: forum.morningstar.io · soundonsound.com · guitarchalk.com.
Artists: strymon.net pedalboard features (Hammock, Andy Othling) + ambient artists feature.
Presets: `.syx` via Nixie 2 (shared ecosystem with the TimeLine).
