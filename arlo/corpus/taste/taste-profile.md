---
title: Taste-Profile Lens
purpose: The single consolidated lens for Track B (taste-profile) patch research. Downstream patch agents read THIS file to know what the user's records sound like and how to translate that to the rig.
sources:
  - arlo/arlo/taste-profile/spotify-taste-profile.md (10 yrs, 31,106 streams; read-only)
  - Plan/patch-research.md § "The taste-profile lens"
generated: 2026-06-14
tags: [taste-profile, lens, track-b, drone, doom, shoegaze]
---

# Taste-Profile Lens

> **What this is.** Track B works *backward from the user's actual listening* to
> patches on *this* rig. This file is the shared lens: (1) the 5 listening
> clusters with anchors + how the records actually sound, (2) the making
> aesthetic, (3) per-cluster "translate to the rig" notes, (4) how patch agents
> use it. Derived from a 10-year Spotify export and the plan's cluster→gear map.
> Keep patches honest — if the rig can only *approximate* a sound, say so.

## Rig context (so the translate-notes make sense)

Three pedalboards in series, signal flows **Front/Strings → Middle/Texture →
End/Time→Tape**. Sources include guitar, **banjo and baritone via Roland GK-5 →
Boss/Roland VG-800** (the VG models/synths the strings; banjo is treated as a
lead voice, not a novelty). Two cornerstones:

- **CB Clean = always-on favorite** — the unity-gain glue cornerstone; most
  signature beds start by assuming Clean is already in the chain.
- **CB Big Time = centerpiece** — minimal chains *into* it; played live with
  OP-1 / Digitakt / MPC. Favor centerpiece + integration recipes.

---

## The making aesthetic (how the user wants to *make* things)

This is the second lens, orthogonal to the clusters. It biases every cluster's
patches toward a specific character:

- **Drone / doom / shoegaze** — sustained, slow-moving sound. Walls over riffs.
  Long verbs, infinite holds, octave/sub weight, saturated guitar/strings that
  bloom rather than chug.
- **Banjo-as-lead** — the banjo (via GK-5 → VG-800) carries melody and lead
  lines. Translate "lead guitar" or "lead synth" ideas onto the banjo voice
  where it fits; lean on its attack/pluck for clarity inside a wall.
- **Degraded / "recorded-wrong"** — tape flutter, wow, dropouts, cassette hiss,
  bit/sample-rate crush, mis-biased saturation. The imperfection is the point;
  prefer the version that sounds *captured on the wrong machine* over the clean
  one.
- **Sustained walls** — feedback loops, freeze/hold, swells, layered drones.
  Build density and let it ring; gate/dynamics for the *build*, not for
  tightness.
- **Baritone weight** — low, heavy fundamentals from the VG-800 baritone model;
  pairs with the drone/doom lean.

> **Default lean:** when a cluster's signature sound *could* be rendered clean or
> degraded, render it degraded/sustained. The user's making-voice is the
> tie-breaker.

---

## The 5 listening clusters

Each cluster: anchor artists (from the user's top-listened), what those records
*actually sound like / how they're made*, then a concrete **translate to the
rig** note. Stable across the decade; recent window leans folk (Sufjan, Bon
Iver) and post-punk (Swans, Adrianne Lenker) up.

### 1. Art-rock / studio-as-instrument — `art-rock-studio-as-instrument`
**Anchors:** Radiohead *(#1 all-time by 2×)*, Talking Heads, David Bowie.

**What it sounds like / how it's made.** The studio *is* the instrument — songs
emerge from sound-design and re-contextualization, not from a band playing a
chart. Signature textures: **reverse and glitch/granular delays**, **modulated
reverbs** (verb that moves and detunes), **tape flutter and wow**, **Ondes-
Martenot / theremin-style lead voices**, processed/affected vocals, abrupt
arrangement cuts and stutters. Beauty and unease held together; the "wrong" or
broken-sounding part is often the hook (e.g. the looped-and-layered build of
"Let Down," the glitch-rhythm of "Ful Stop").

**Translate to the rig.** Reverse + glitch on **Eventide H90** and **CB
Blooper** (granular/reverse loop layers); modulated wash on **Strymon Big Sky**;
tape flutter via **CB Generation Loss**; Ondes-style melodic lead on **OP-1** or
the **VG-800** synth/string models (banjo can carry the Ondes line). Build the
"Let Down" stack as layered loops; let modulated verb detune underneath.
*Target gear:* H90, Blooper, Big Sky, OP-1, VG-800, Gen Loss.

### 2. Indie-folk / confessional — `indie-folk-confessional`
**Anchors:** Bon Iver, Sufjan Stevens, Big Thief / Adrianne Lenker.

**What it sounds like / how it's made.** Lyric-and-intimacy-first: capture the
performance, build outward sparingly. Close-mic'd, breathy, *in-the-room*
recordings. The signature modern-folk move is the **vocal halo** — Bon Iver's
Prismizer / Messina rig stacking pitch-shifted harmony clouds around a single
voice. Sufjan layers banjo, fragile falsetto, and orchestral/electronic washes;
Big Thief / Lenker keep it raw, intimate, tape-warm, with the room and finger
noise left in. Banjo and fingerpicked beds are core, not decoration.

**Translate to the rig.** Vocal-halo / Prismizer-style harmony stacks on
**Antares Prismizer** (software — document in the cluster index, no gear sheet)
and approximate on **Walrus QI Etherealizer** (pitched shimmer cloud); intimate
ambient room on **Hologram Microcosm** and **Chroma Console**; warm string/
banjo beds on the **VG-800** (banjo model fingerpicked); diffuse bloom on
**OBNE Dark Star V3**. Keep it close and dry-forward, then halo around it.
*Target gear:* Antares Prismizer, Microcosm, Chroma Console, Dark Star, QI,
VG-800.

### 3. Electronic / groove-first — `electronic-groove-first`
**Anchors:** LCD Soundsystem, Daft Punk, The Postal Service.

**What it sounds like / how it's made.** Groove-first, loop-and-arrangement
driven — the rhythm section *is* the hook. **Sequenced analog/synth lines**,
**filtered loops** that open and close over long builds, **vocoder / talkbox**
vocals, four-on-the-floor and motorik pulses, sidechain pump, drum-machine
backbone. Arrangement is additive: a riff/loop locked, then layers stacked and
filtered in/out across minutes (LCD's long builds; Daft Punk's filter-house;
Postal Service's glitchy programmed beats under soft vocals).

**Translate to the rig.** Sequenced lines and filtered loops on **Digitakt 2**
and **Octatrack MkII**; drum/loop backbone on **MPC Sample**; synth leads/bass
on **OP-1** and the **VG-800** synth engine (baritone as analog-bass voice);
sequence and CC automation from **Novation 61SL MkIII** (template/sequence
recipes, not sounds). Vocoder is an approximate — note where it's only partial.
Build patches as evolving filter sweeps over a locked loop.
*Target gear:* Digitakt, Octatrack, MPC, OP-1, 61SL, VG-800 synth.

### 4. Lo-fi / prolific — `lo-fi-prolific-volume`
**Anchors:** Car Seat Headrest, Modest Mouse.

**What it sounds like / how it's made.** Volume and speed over polish — the demo
*is* the song. **Bedroom/4-track cassette degrade**, clipped and overloaded
preamps, **room-mic'd amps** bleeding into everything, blown-out drums, vocals
pushed into distortion. Modest Mouse adds jangly, brittle clean tones and odd
tunings; Car Seat Headrest layers crunchy guitars and lo-fi production warts left
audible. Imperfection is identity — this cluster is the *most direct* expression
of the "recorded-wrong" aesthetic.

**Translate to the rig.** Cassette degrade on **MXNHLT PORTA424** and **CB
Generation Loss**; preamp crunch / console overload on **JHS Colour Box V2** and
the **drives** (Oxford Drive, JHS 424, Longsword, Kilt v10); room-amp / tape
saturation on **Strymon Deco V2**. Push gain stages past clean; leave the warts.
This is where the user's degrade chain lives most naturally.
*Target gear:* PORTA424, Gen Loss, Colour Box V2, drives, Deco.

### 5. Post-punk / experimental — `post-punk-texture-dynamics`
**Anchors:** Swans, Black Country New Road, Joy Division.

**What it sounds like / how it's made.** Texture, repetition, dynamics and build
over verse-chorus. **Drone walls** that rise over long durations (Swans'
crushing, sustained crescendos), **brittle/atonal guitar textures**, **dynamic
builds** from near-silence to overwhelming, motorik repetition, cavernous or
gated reverbs (Joy Division's Hannett production — separated, spacious, cold),
chamber-rock builds (BC,NR). This cluster *is* the drone/doom making aesthetic in
listening form.

**Translate to the rig.** Saturated drone walls on **EQD Hizumitas** and **MXR
M173 108 Fuzz** (fuzz sustain into the wall); brittle dissonant texture on
**Longsword**; diffuse/atonal bloom and reverse swells on **OBNE Dark Star V3**;
pitched/granular shimmer wall on **Walrus QI Etherealizer**. Use freeze/feedback
for the sustained crescendo; baritone (VG-800) for the low crush. Dynamics are
for the *build* — start quiet, let the wall consume.
*Target gear:* Hizumitas, 108, Longsword, Dark Star, QI Etherealizer.

---

## How patch agents use this

1. **Pick the cluster** for your wave (B1 Art-rock → B2 Indie-folk → B3
   Electronic → B4 Lo-fi → B5 Post-punk). Read that cluster's "what it sounds
   like" + "translate to the rig" note plus the making aesthetic above.
2. **Research the anchors' real tones** — records, rigs, documented gear/
   settings, interviews — then capture sources to
   `Research/Taste-Profile/sources/<slug>.md` (URL, then `site · author · date`,
   then distilled concrete settings). Gear-specific sources go in that gear's
   `research/links/` or `research/transcripts/` per the repo conventions.
3. **Translate each signature sound to a concrete patch** on the user's OWN gear
   (use the cluster's target list). Each patch = control-by-control values for
   the specific unit + a `ref:` to the artist/record + a provenance tag.
4. **Apply the making-aesthetic tie-breaker** — when a sound could be clean or
   degraded, render it degraded/sustained. Lean drone/doom/shoegaze; route leads
   to the banjo voice where it fits; assume CB Clean is always-on and bias
   centerpiece recipes into CB Big Time.
5. **Provenance + honesty (non-negotiable):**
   - 🟢 factory/artist (named, cited) · 🔵 community (cited) · 🟣 DOUG-designed
     (synthesized — never presented as found) · ⭐ = signature-fit overlay.
   - Track B patches are the deeply-cited ⭐ patches. **Never fabricate an artist
     attribution** — inferred settings are 🟣.
   - Where the rig can only *approximate* a sound (e.g. vocoder, Prismizer halo
     on hardware), **say so explicitly**.
6. **Write outputs two places:** (a) append/insert the ⭐ patches into the
   relevant `Gear/<Item>/presets/<Item>-Patches.md` sheets (single source of
   truth, with the `ref:` line); (b) index every derived patch in
   `Research/Taste-Profile/<cluster>.md` (the cross-rig view).
   **Software-only sounds** (e.g. Antares Prismizer) have no gear sheet —
   document them in the cluster index only.
