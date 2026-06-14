# BBC Symphony Orchestra (BBC SO) — Usage Guide

BBC SO is the rig's **realistic-orchestra "ghost layer"** — a real orchestra (Maida Vale
Studios, a relatively *dry* room) playing as soft as possible, then degraded through Valhalla
/ EchoBoy / Decapitator into your own invented space. It is rarely the centerpiece; it's the
believable faint strings/brass *under* the banjo/baritone. The dry source is the asset —
less baked-in hall = more control to make it sound "recorded-wrong." When you want a texture
that needn't read as a real orchestra, reach instead for the owned designed-texture libs
(Orchestral Swarm / SSEvo / Cells / Fractured Strings).

> **⚠️ Edition gate (confirm this).** The installed edition isn't recorded and the content
> drive is offline, so I can't verify it. It changes everything: **Discover (free) has Longs
> only — no Sul Tasto / Flautando / Con Sordino / Harmonics**, so the signature ghost patches
> below are **Core/Pro only**. If you're on Discover, you get a plain sustained bed (still
> usable) and should substitute **LABS Frozen Strings** for the super-sul-tasto colour. See §6.

---

## 1. Essential workflows

**A. The degraded ghost-string bed (core recipe).**
1. Load strings (Violins/Violas/Cellos/Basses) **Long**, or stack sections. For the ethereal
   core switch to **Super Sul Tasto / Sul Tasto** (warm, very quiet, bow over the fingerboard),
   **Long Flautando** (light/airy), or **Long Con Sordino** (muted). [transcripts/bbcso-core-walkthrough-articulations.md]
2. **Ride the mod wheel** on held chords — on BBC SO long patches the mod wheel = **Dynamics**,
   a crossfade between *separately-recorded* pp→ff layers, so riding it **low gives a genuinely
   breathier/darker pp timbre**, not just a quieter loud sample. Keep it down for the ghost; use
   **CC11 (Expression)** to set how far back it sits. [links/bbcso-cc1-dynamics-pad-technique.md; transcripts/bbcso-dynamics-modwheel-cc.md]
3. **Turn the in-plugin Reverb all the way down** — keep it dry, add your own space downstream.
   [transcripts/bbcso-ultimate-guide-editions-mics-cpu.md]
4. Degrade: into **Valhalla Room** (short early-reflections) → **VintageVerb** (long, degraded
   tail) → **EchoBoy / Decapitator** (tape wow-flutter / saturation). See §5.

**B. Evolving without re-attacking.** Slowly drift the mod wheel/Dynamics (~15↔45) under a
held cluster, and **stagger section entrances** so attacks never line up — motion without a new
transient. (BBC SO has **no built-in arpeggiator/"Ostinatum"** — evolution comes from CC rides
+ layering + round-robins.) [links/bbcso-cc1-dynamics-pad-technique.md; links/bbcso-bounce-to-wall-evolving-technique.md]

**C. Bounce-to-wall.** Bounce a held chord to audio (frees RAM/streaming), then loop it, or
**PaulStretch 8–20×** into "an atmospheric drone that loops forever" (small grains = choppy,
large = silky), then play banjo/baritone over it. Same offline-wall habit as the Cells/LABS
guides. [links/bbcso-bounce-to-wall-evolving-technique.md]

**D. Layer + crossfade articulations.** Layer a soft attack (Marcato) into a sustain and
**bounce to audio** to blend them by hand. [transcripts/bbcso-blending-layering-articulations.md]

**E. Multi-output mics in Logic (Pro only).** Route **Close / Tree / Outrigger / Ambient** to
separate channels → degrade the **Close** mic, keep or drop the rest. [transcripts/bbcso-logic-multi-output-mics.md]

---

## 2. Articulation map for this rig

The textural patches that give the ghost/ethereal colour (all **Core/Pro**; absent in Discover):
- **Super Sul Tasto** — *the* #1 ghost patch: "quiet, beautifully tentative and delicate." [links/bbcso-textural-articulations-sos.md]
- **Sul Tasto (Long)** — warm, very quiet, over the fingerboard. [transcripts/bbcso-core-walkthrough-articulations.md]
- **Long Flautando** — "very light, gentle"; **bass long flautando = "particularly beautiful and haunting."**
- **Con Sordino (muted Long)** + **Tremolo con sordino** — soft, veiled.
- **Harmonics (long + short)** — glassy/ethereal top.
- **Long Sul Ponticello / Tremolo sul ponticello** — crisp, nasal, **metallic** colour for the less-realistic end.
- **Brass drones** — solo horn + section longs as quiet chords = "lovely quiet choral stuff"; 3 trombones/bass trombones "very quietly, really down low." Soft beds without the fanfare.
- **Woodwind longs** — flute/clarinet/bassoon; **bassoons-a3 = "chorus-like richness" low down**; flutter for air.
- **Doom foundations** — **double-bass con-sordino low fifths**; **solo cello sul tasto played chordally** = a drone. [links/bbcso-textural-articulations-sos.md]

---

## 3. Mic-mix guidance

- **Discover = 1 baked mix** (no mic control). **Core = 1 curated mix** (front-weighted, no
  mic control). **Pro = 20 signals / 11 mic positions + Mix 1 / Mix 2 presets.** [transcripts/bbcso-ultimate-guide-editions-mics-cpu.md]
- Mic characters: **Close** = intimate/dry/"gritty" (the one to isolate and degrade); **Tree**
  (Decca Tree) = best all-rounder; **Outrigger** = space; **Ambient/Balcony** = distant/roomy.
  **Mix 1** balanced, **Mix 2** hyped. [transcripts/bbcso-logic-multi-output-mics.md; links/bbcso-mic-positions-dry-vs-distant.md]
- **For this rig: favor the Close (dry) signal** into the FX chain — and the forum's hard rule:
  **feed reverb the DRY mics; the baked hall mics "generate too much metallic ringing"** under a
  reverb. Roll bass + harsh highs off the close mic. [links/bbcso-vicontrol-dry-reverb-workflow.md]
- **CPU:** each mic is a separately streamed layer — all-mics sessions hit ~40 GB and forum
  users report dropouts at ~4 mics. **Load 1–2 mics** (the ghost workflow wants no more). [links/bbcso-gotchas-drive-cpu-ram.md]

---

## 4. Notable users & techniques

Honest: **no verified drone/doom/shoegaze artist uses BBC SO specifically** — it's a
media-composer / realism tool. The citable lineage is the **neoclassical-ambient scene**
(**Jóhann Jóhannsson, Ólafur Arnalds, Max Richter, Ryuichi Sakamoto**) and its documented
method: slow pad-like sustains, **flautando + sul tasto**, crossfaded articulations for a
"woozy" feel, then **tape saturation** — which is exactly EchoBoy/Decapitator + Valhalla on
BBC SO sul-tasto. Note: of the owner's Spitfire set the *direct* artist ties are **Cells =
Arnalds**, Fractured = Zimmer/Bleeding Fingers, Resonate = Glennie — none is BBC SO, which
reinforces "BBC SO = realism; the texture libs = the artist-branded ambient engines."
[links/bbcso-artists-aesthetic-lineage.md; links/bbcso-dry-make-it-your-own-workflow.md]

---

## 5. Rig-specific recipes

- **Dry → degrade chain:** load **Close (+ a little Leader/spill or Mono) only**, kill
  Ambient/Balcony → **Super Sul Tasto, mod wheel low** → **Valhalla Room** (short ER) →
  **VintageVerb** (long, degraded tail) → **EchoBoy / Decapitator** (tape/wow/saturation). The
  dry Maida Vale source is the asset *because* it lets you invent the space. [links/bbcso-vicontrol-dry-reverb-workflow.md; links/bbcso-mic-positions-dry-vs-distant.md]
- **The Jóhannsson move (closest documented analogue):** sustained sul-tasto/flautando strings,
  crossfade articulations, then tape saturation → woozy faint orchestra. [links/bbcso-dry-make-it-your-own-workflow.md]
- **Ghost under banjo (bounce-to-wall):** bounce the held bed → loop / PaulStretch → degrade →
  play banjo/baritone over it.
- **BBC SO vs designed texture — the decision:** want *realism* in the drone (recognisable real
  strings behaving ethereally) → **BBC SO** + bounce/stretch to make it evolve; want an alive
  bed that needn't read as orchestra → reach straight for **Orchestral Swarm** (granular cloud),
  **SSEvo**, or **Cells** and skip the bounce labour. [links/bbcso-bounce-to-wall-evolving-technique.md; links/bbcso-artists-aesthetic-lineage.md]

---

## 6. Editions — what you actually have (CRITICAL, unconfirmed)

| Edition | For this rig |
|---|---|
| **Discover** (free, ~200–360 MB) | 34 grouped instruments, **~2 articulations each — Longs + shorts ONLY** (strings add pizz/trem), **one fixed mix, no mic control, no legato, single dynamic layer, not multitimbral.** **No Sul Tasto / Flautando / Con Sordino / Harmonics.** Still does a **plain sustained pad bed** (reviews: "excels at sustained, pad-like textures beneath electronic layers") — usable, just lacking the breathy colours. **Substitute: LABS Frozen Strings** for super-sul-tasto. Small enough to live on the system drive (skip the offline drive). |
| **Core** (~$500) | **All articulations Pro has** — the full textural set (sul tasto, flautando, con sordino, harmonics). Still **one mix, no mic control, no solos/leaders.** **→ The sweet spot for this rig:** every ghost patch; the single dry-ish mix is fine since you degrade downstream anyway. |
| **Pro** (~$1000, 600+ GB) | Adds **20 mic signals, string leaders/soloists, extended low instruments** (bass clarinet/contrabassoon), more techniques. Only needed here for **Close-mic isolation** or leader-vs-section layering. |

**Action:** confirm the installed edition when the drive is mounted (Spitfire app shows it) —
it decides whether the §2 patches name something you actually own. [links/bbcso-discover-edition-reality.md; transcripts/bbcso-discover-free-edition-sketch.md]

---

## 7. Common pitfalls / gotchas

- **Offline-drive relink:** mount **`PlaySomeGodDamnMusic` before launching Logic**, or the
  library shows "not found" — relink via the Spitfire app → Repair, or per-product cog →
  Locate. (Discover is small enough to skip this.) The AU plugin itself always loads. [links/bbcso-gotchas-drive-cpu-ram.md]
- **Mic count = RAM multiplier** — each mic ~doubles load; all-mics ≈ 40 GB; dropouts at ~4
  mics. **2–3 mics max**, and the ghost workflow wants 1–2. External-drive streaming worsens
  dropouts → bounce held beds. [links/bbcso-gotchas-drive-cpu-ram.md]
- **CC labelling:** treat **mod wheel = CC1 = Dynamics** (the dynamic-layer crossfade) as
  canonical; **Expression = CC11** (a level/distance control). Some reviewers mislabel CC1 as
  plain volume — it isn't on the long patches. [transcripts/bbcso-dynamics-modwheel-cc.md; links/bbcso-cc1-dynamics-pad-technique.md]
- **No "Ostinatum"** in BBC SO (that's a different Spitfire product) — motion comes from CC
  rides + layering + round-robins.
- **Logic:** native AU, loads clean (no Kontakt). **Ableton Lite:** hosts the AU/VST3 fine; the
  constraint is Lite's track/return ceiling, not the plugin. [transcripts/bbcso-cpu-ram-purge-multitimbral-trick.md]

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`): `bbcso-core-walkthrough-articulations` (★ the
textural reference), `bbcso-interface-ui-basics`, `bbcso-dynamics-modwheel-cc`,
`bbcso-logic-multi-output-mics`, `bbcso-blending-layering-articulations`,
`bbcso-cpu-ram-purge-multitimbral-trick`, `bbcso-ultimate-guide-editions-mics-cpu` (clearest
edition tiers), `bbcso-discover-free-edition-sketch`, `bbcso-discover-official-contents`
(caption-thin → contents only).

**Links** (`research/links/`): `bbcso-textural-articulations-sos`, `bbcso-cc1-dynamics-pad-technique`,
`bbcso-mic-positions-dry-vs-distant`, `bbcso-vicontrol-dry-reverb-workflow`,
`bbcso-dry-make-it-your-own-workflow`, `bbcso-bounce-to-wall-evolving-technique`,
`bbcso-discover-edition-reality`, `bbcso-gotchas-drive-cpu-ram`, `bbcso-artists-aesthetic-lineage`.
(Builds on the existing `links/spitfire-nav-bbcso-textures.md`.)

**QC notes:** 18 new sources (9 transcripts + 9 links). **No dedicated "BBC SO for
drone/doom/shoegaze" tutorial exists** — the ghost-layer workflow is assembled from the
official articulation/dynamics/mic mechanics + the rig's degrade chain + the documented
neoclassical-ambient method; it's sound but **inferred**, not a single "do this" source. The
CC1-drift, PaulStretch, and Valhalla/EchoBoy/Decapitator stage-mapping are **inferred
applications** of documented general methods. **VI-Control 403s all bots** → its threads are
triangulated from search snippets (labeled per file). **No BBC-SO ambient-artist credit
exists** (genuine gap). **Owner's edition unconfirmed** — §2 recipes assume Core/Pro.

## Sources
See §8 for local captures. Originals: youtube.com (Spitfire Audio official, Tom Harrold, Cmd
Shift New, ThinkSpace, Alexandre David, Protoculture), spitfireaudio.com, soundonsound.com,
vi-control.net, kvraudio.com, skippystudio.nl. URLs on line 1 of each captured file.
