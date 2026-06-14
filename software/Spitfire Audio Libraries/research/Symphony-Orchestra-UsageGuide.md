# Spitfire Symphony Orchestra (SSO) — Usage Guide

SSO is the rig's **lush, already-drenched real-orchestra ghost layer** — the wet-hall
counterpart to BBC SO. It is the big drive-resident Kontakt library: seven sub-libraries
(Symphonic Strings, Brass, Woodwinds, Percussion, Harp, Orchestral Grand Piano, Curated
Ensembles), ~345 GB, recorded at **AIR Studios Lyndhurst Hall** — the room behind Gladiator,
The Dark Knight, Harry Potter, How To Train Your Dragon. The single thing to internalise:
**with SSO the hall IS the sound.** Where BBC SO hands you a dry Maida Vale source to build
your own space around, SSO arrives pre-bloomed in "a gentle reverberation that just adds
beauty to literally anything you play" — Spitfire's own framing.
[transcripts/sso-pro-official-walkthrough-mics.md] So the workflow flips: less "make it your
own space," more "recognisable orchestra behaving ethereally, already wet" — then degrade the
*character* (tape/saturation/lo-fi), not primarily the *space*.

> **The differentiating quote (Spitfire's Paul Thomson, official Pro walkthrough):** "It's
> very hard to make samples that are recorded in a dry room sound like this, because the room
> is bound to the players — the players respond to the room, the instruments vibrate in
> sympathy with it. The room you record in has such an enormous effect on the end result."
> That is exactly why you reach for SSO over BBC SO when you want the *sound of the score* (the
> Lyndhurst bloom) baked in, and BBC SO when you want a dry skeleton to wreck.
> [transcripts/sso-pro-official-walkthrough-mics.md]

> **⚠️ Format & host (confirm on disk).** SSO is **not** a dedicated AU plugin — it loads
> **inside Kontakt**. The 2024-relaunch "Symphony Orchestra" runs in full **Kontakt 8** or the
> **free Kontakt Player 7.5.2+**; the older "Player" sub-libraries (Symphonic Strings/Brass/
> Woodwinds, recorded 2016) use Spitfire's Player engine that also opens in Kontakt. The rig
> owns full Kontakt 8, so every edition is covered. **You open Kontakt 8 first, then load the
> library from its Libraries pane** — unlike BBC SO which loads natively in Logic. (See the
> Kontakt 8 guide for the host basics; this guide is SSO-specific.)

---

## 1. Essential workflows

**A. The lush ghost-bed (core recipe — and how it differs from BBC SO).**
1. Load a string section **Long**, then switch to the ethereal patches in the **extended /
   decorative techniques folder**: **Super Sul Tasto** ("really, really, really gentle"),
   **Sul Tasto**, **Flautando** (flotando — "light, airy"), **Con Sordino** (muted; a "slightly
   fizzy top edge" from the mute), **Sul Ponticello / Con Sordino Sul Pont** (scratchy bridge
   tone + the gentleness of the mute), **Harmonics**, **Tremolo / Tremolo Sul Pont / measured
   tremolo / Tremolo Con Sordino**. [transcripts/sso-pro-official-walkthrough-mics.md;
   transcripts/sso-sampleist-overview-editions-ram.md]
2. **Set the dynamics control (mod wheel) right down** to grab the softest, breathiest layer,
   then **shape the level with the Expression slider** — the SSO/Symphonic-Strings team's own
   "very, very delicate sound" trick: "set the mod wheel right down so you're getting the
   softest sample, then just control the volume with Expression."
   [transcripts/sso-symphonic-strings-purge-mics-dynamics.md] On these libraries mod wheel =
   **Dynamics** (a pp→ff crossfade between separately-recorded layers, so low = genuinely
   darker/breathier, not just quieter), **Expression = overall level**, and a third **Vibrato**
   slider crossfades vibrato amount. Keep dynamics low, vibrato low, for the ghost.
   [transcripts/sso-symphonic-strings-purge-mics-dynamics.md]
3. **Choose the mic balance toward the bloom, not against it** (this is the inversion vs BBC
   SO — see §4). For the drenched ghost, lean on **Tree + Ambient (+ a touch of Outriggers/
   Gallery)** and let the hall ring. Only pull in **Close** when you want the degrade chain to
   bite on something drier. Mic control lives on the **Spanner page** (a simple close-to-far
   slider on the easy page, full mic faders under the hood).
   [transcripts/sso-symphonic-strings-purge-mics-dynamics.md]
4. Degrade the **character**, not the space: into **EchoBoy / Decapitator** (tape wow-flutter /
   saturation — make the lush orchestra sound "recorded-wrong") → optionally a *little*
   **VintageVerb/Valhalla** to glue, but you are adding colour on top of an already-wet source,
   not building the room from scratch. Then banjo/baritone over the top.

**B. Evolving without re-attacking.** Drift the Dynamics control under a held cluster and
stagger section entrances so attacks never line up. For *genuinely* evolving symphonic motion
without playing it by hand, reach for **Symphonic Strings Evolutions (SSSE)** — the EVO-grid
sibling (own note below, §3) — which is the same 60-piece string section in the same Lyndhurst
hall, but scripted to evolve. [transcripts/sso-symphonic-strings-evolutions-evogrid.md]

**C. Bounce-to-wall.** Bounce a held SSO bed to audio (frees RAM/streaming off the offline
drive), loop it, or PaulStretch it into a forever-drone, then play over it. Same offline-wall
habit as the BBC SO / Cells / LABS guides — and arguably *more* useful with SSO because the big
all-mics library is RAM-heavy to leave live (see §5).

**D. Layer sustain + a soft attack, then commit.** Blend a quiet attack articulation into a
sustain and bounce to audio. Note SSO's **Performance Patches** (designed by Andrew Blaney) do
some of this for you: one patch blends long/legato/short and switches articulation by how you
play, so you don't have to stack as many patches or build expression maps.
[transcripts/sso-guy-michelmore-full-tutorial-performance-patches.md]

**E. Brass/woodwind drone beds (not fanfare).** Low-dynamic section longs in the hall are a
documented "beautiful" use even from Spitfire: 12 horns on the **Motif Brass** low level
"just really sounds beautiful," gentle trombone longs have "almost a woodwindy warmth,"
and bass woodwinds/low brass "really resonate the room." See §3.
[transcripts/sso-motif-brass-2025-update.md; transcripts/sso-guy-michelmore-full-tutorial-performance-patches.md;
transcripts/sso-pro-official-walkthrough-mics.md]

**F. Play it as a pad (soft velocity + long releases).** SSO's default sustains have an
**auto-crescendo/swell attack (~1 s)** — so **playing softly makes every note swell *in***;
**avoid high-velocity triggers** (they fire the hard attack and break the pad). Open the
**Release** (smooth mode, ~CC17 on older patches) so chords bleed into each other, and
**stagger entrances** so swells never line up = motion without a new transient. The **Curated
Ensembles** sustains (ex-"Masse") are the fastest route to a single-patch wall — up to
**300+ layered players** in one patch. [links/sso-syntheticorch-performing-pads.md;
links/sso-apg-relaunch-close-mic-room.md]

---

## 2. Articulation map for this rig

The ethereal/ghost textures, by section. (All in the **decorative / extended-techniques**
folder on the newer SSO; the same articulations exist as separate patches on the older
Symphonic Strings/Woodwinds.) [transcripts/sso-pro-official-walkthrough-mics.md;
transcripts/sso-sampleist-overview-editions-ram.md]

**Strings — the core of the ghost layer:**
- **Super Sul Tasto** — *the* #1 ghost patch: "really, really gentle," extremely soft. The
  wet-hall version of BBC SO's super sul tasto, but already bloomed.
- **Sul Tasto** — warm, very quiet, bow over the fingerboard; "very beautiful" even with the
  small chamber-strings section.
- **Flautando (flotando)** — light, airy, breathy; the reviewer's "I use flautando a lot."
- **Con Sordino** (muted long) + **Tremolo Con Sordino** — soft/veiled with a faint "fizzy"
  top edge from the mute.
- **Con Sordino Sul Ponticello** — combines the scratchy bridge tone of sul pont with the
  gentleness of the mute; the less-realistic, metallic-leaning colour.
- **Harmonics** (long + short) — glassy/ethereal top (range is limited, as on the woodwinds).
- **Tremolo / Tremolo Sul Pont / measured tremolo** — played *quietly* these give a delicate
  "scattery double-bowing" shimmer rather than a horror-trailer swell.
- **Doom foundations** — basses "really growl" down low; combine con-sordino low fifths with
  the room resonance for weight. [transcripts/sso-sampleist-overview-editions-ram.md]

**Woodwinds — breathy air and soft low beds:**
- **Hollow Long** — "a lovely lovely soft sound," explicitly flagged as beautiful/soft.
- **Flutter tongue** (flute/oboe/clarinet) — air and noise for texture.
- **Bass flute** — "wonderful and haunting"; **bass/contrabass clarinet & contrabassoon** as
  very soft long basses that "resonate the room" (the contrabassoon's bottom Bb "is like an amp
  signal" in the hall). Harmonics present but limited range.
  [transcripts/sso-symphonic-woodwinds-textures.md; transcripts/sso-pro-official-walkthrough-mics.md]

**Brass — quiet beds, not fanfare:**
- **Gentle trombone longs** — "almost a woodwindy warmth," really soft and lovely.
- **Horn longs at low dynamic** (incl. Motif Brass F4 = 12 horns) — "just really sounds
  beautiful" pulled back; choral pad material.
- **Chimbasso / contrabass trombone / contrabass tuba** — capable of "very delicate textures"
  and bottom-end resonance, not just rasp; impact/low-drone colour.
  [transcripts/sso-pro-official-walkthrough-mics.md; transcripts/sso-motif-brass-2025-update.md]

**Percussion as texture (the most SSO-specific trick):** the percussion "wallows in the
amazing reverb of the galleried Lyndhurst Hall" — marimba/tubular bells/cymbal swells as
*reverb-tail textures*, not rhythm. A single mallet hit blooms into the room; bounce and stretch
it. (This is the angle the dry libraries genuinely can't fake.)
[links/spitfire-nav-symphony-orchestra-textures.md]

---

## 3. The seven sub-libraries — which serve texture

| Sub-library | Texture role on this rig |
|---|---|
| **Symphonic Strings** | The workhorse ghost layer: super sul tasto / flautando / con sordino / harmonics / quiet trem. The first place you go. |
| **Symphonic Woodwinds** | Breathy air + soft low beds (hollow long, flutter, bass flute, contrabassoon "amp" low end). |
| **Symphonic Brass** | Quiet horn/trombone choral pads; chimbasso/contrabass low drones. Avoid the fanfare patches. |
| **Percussion** | Reverb-tail textures (marimba/bells/cymbal swells blooming in the gallery). Rarely rhythm here. |
| **Harp** | Single plucks/gliss blooming in the hall → loopable shimmer; layer under strings. |
| **Orchestral Grand Piano** | Lush, distant Lyndhurst piano — sustain-pedal washes, felt-ish soft beds; degrade for lo-fi. |
| **Curated Ensembles** | Pre-balanced whole-section/whole-orchestra patches — "Christian loads ensembles first to write with." Fastest way to a one-patch lush bed; lower voice count. [transcripts/sso-pro-official-walkthrough-mics.md] |

**Symphonic Strings Evolutions (SSSE)** is the *evolving* companion (own navigator note;
already owned). Same 60-piece section, same hall = "beautiful, massive, lush sound," but the
EVO grid (orchestrated by Ben Foster) scripts each long note to evolve and loop — vanilla
evolutions (pulsing bows, ponts) through episodic/shudder to "modestly extreme" (bends,
phasing, cross-string). Reach for SSSE over manual CC-rides when you want symphonic motion that
plays itself; reach for plain SSO when you want a still, controllable bed.
[transcripts/sso-symphonic-strings-evolutions-evogrid.md; transcripts/sso-how-it-works-evolutions-short.md]

---

## 4. Working WITH the wet Lyndhurst hall (the key difference vs BBC SO)

BBC SO's guidance was "favor the dry Close mic, feed reverb the dry mics, the baked hall mics
ring metallically." **SSO inverts this**, because the hall is the asset:

- **Mic positions (newer SSO ~345 GB):** **Close, Tree, Ambient, Outriggers, Lead** — 5
  signals. [transcripts/sso-sampleist-overview-editions-ram.md] **SSO Pro (600+ GB)** adds the
  full palette: **Decca Tree, Outriggers, three Jake-Jackson Stereo Mixes (fine/medium/broad),
  Stereo Stage (ST), Galleries (G — "very, very distant," 3D spaciousness from mics up in the
  architectural galleries), Close Ribbon (CR — warmer/fuller, "slightly vintage" rounded top),
  and Leader (L — focuses one player's vibrato, "like laying a solo violin over the section").**
  [transcripts/sso-pro-official-walkthrough-mics.md]
- **Mic character:** **Close** = intimate/defined, the *relatively* driest option — **but
  still roomy**: unlike BBC SO's genuinely dry Maida Vale close, even SSO's close mic carries the
  hall's early reflections, so "you're more or less stuck with it" — there is **no truly dry
  signal to isolate**. Push Close when you want the degrade chain to bite, but don't expect
  BBC-SO-level control. [links/sso-vicontrol-too-much-room-baked-in.md; links/sso-apg-relaunch-close-mic-room.md] **Tree** = the spacious all-rounder. **Ambient /
  Gallery** = the distant bloom — *embrace* these for the ghost, don't kill them. **Outriggers**
  = a sideways extension of the Decca Tree that widens the stage; "add to taste." **Close Ribbon
  (Pro)** = the lo-fi-friendly one (warm, vintage, rounded top — pairs well with con sordino's
  fizz). **Leader (Pro)** = sneak a single soloist's vibrato over the section for emotion.
  [transcripts/sso-pro-official-walkthrough-mics.md]
- **How it changes the degrade approach vs BBC SO:** with BBC SO you build the space; with SSO
  the space is *already there and gorgeous*, so:
  1. **Don't fight the reverb with more reverb.** The forum rule: "these samples are really wet
     by nature — tame the room and use a **feather** reverb instead of painting over it"; a
     double-hall = mush, and "there is no way to match the baked-in Lyndhurst reverb." So a
     *little* Valhalla/VintageVerb to glue is fine, but the move is to degrade the **character** —
     bounce the held bed → (optionally PaulStretch) → **EchoBoy/Decapitator/RC-20** for tape wow,
     wobble, saturation, bitcrush, rolled highs — so a recognisable, drenched orchestra sounds
     "recorded-wrong." Reverb only as a feather tail or a deliberately-wrong second colour
     (Supermassive smear), never a realistic room. [links/sso-vicontrol-reverb-for-spitfire-orchestra.md; links/sso-degrade-wet-bed-rig-recipe.md]
  2. **If you need control back** (e.g. to add your *own* invented space), **pull the Ambient/
     Gallery/Outriggers down and push Close** — the closest SSO gets to BBC SO's dry workflow.
     SSSE's walkthrough does exactly this: "switch off the outriggers, put the close mics up" to
     hear inside the sound. [transcripts/sso-symphonic-strings-evolutions-evogrid.md]
  3. **The bloom is itself a texture.** Hold a quiet sul-tasto chord, ride the Ambient/Gallery
     up, and the hall tail becomes the pad. Percussion/harp single hits blooming in the gallery
     are pure tail-texture — bounce + stretch them.
- **Forum note:** because SSO is "already wet," users add only a little reverb on top — mainly
  to *match* a drier library to SSO's room, not to make SSO bigger.
  [links/spitfire-nav-symphony-orchestra-textures.md]

---

## 5. Kontakt mechanics — loading, purge, RAM, multi-out

- **It's a Kontakt library, not a plugin.** Open **Kontakt 8** as an AU in Logic, then load SSO
  from Kontakt's **Libraries** pane (authorise once in Native Access / Spitfire app). Free
  **Kontakt Player 7.5.2+** runs the newer SSO too; full Kontakt 8 adds editing + non-Player
  content. The rig owns full Kontakt 8, so no Player limits bite. (Don't confuse with BBC SO,
  which is a *native AU* and never touches Kontakt.)
- **Mic count = the RAM multiplier.** Every mic position is a separately-streamed layer, so an
  all-mics SSO session balloons fast. **The single biggest CPU/RAM win: don't load every mic.**
  Spitfire's own advice — "if you have a lower-resource system, don't load all the mics
  separately, go straight to the **Mixes** to get three pre-balanced mixes that cover 99% of
  scoring and use **one voice per note**." [transcripts/sso-pro-official-walkthrough-mics.md]
  For the ghost workflow, **1–2 mics (or a single Mix) is plenty.**
- **Purge unused** (Kontakt / Spitfire engine): with "Purge unused" dialled in, the patch
  **only loads samples you actually play**, so it loads faster and uses far less RAM; the
  **memory-chip icon** unloads/reloads samples on demand. Use this on big multi-articulation
  patches so you're not holding 600 articulations' worth of samples for a bed that uses one.
  [transcripts/sso-symphonic-strings-purge-mics-dynamics.md] (In full Kontakt you also get the
  standard **Purge All Samples / preload-buffer** controls — drop the preload buffer for an
  SSD/offline drive to reclaim RAM.)
- **Total footprint:** the relaunched **Symphony Orchestra ≈ 345 GB**; the separate **Pro**
  collection is **600+ GB**, and *everything combined* (all sub-libraries + legacy) is **~700–
  750 GB** — the size delta is almost entirely the extra **mic mixes** (Stereo Stage/Gallery/
  Close Ribbon/Leader from Jake Jackson). [transcripts/sso-sampleist-overview-editions-ram.md]
- **Multi-out in Logic:** load Kontakt as a **multi-output** instrument and assign mics (or
  whole sections) to separate Kontakt outputs → Logic aux channels. Route the **Close** mic to
  its own channel to degrade it hard while leaving the Tree/Ambient bloom clean — the wet-hall
  equivalent of BBC SO's per-mic multi-out trick. (General Kontakt mechanic; not SSO-specific —
  see the Kontakt 8 guide.)
- **Offline-drive gotcha:** content lives on `PlaySomeGodDamnMusic`. **Mount the drive before
  launching Logic/Kontakt**, or the library shows "samples missing" → relink via the Spitfire
  app (Repair) or Kontakt's batch-resave/Locate. Streaming a 345 GB library off an external
  drive worsens dropouts → **bounce held beds to audio** (also frees the RAM). [SoftwareProfile.md]

---

## 6. SSO vs BBC SO — when to reach for which

| | **Spitfire Symphony Orchestra (SSO)** | **BBC Symphony Orchestra (BBC SO)** |
|---|---|---|
| Room | **AIR Lyndhurst Hall — wet, lush, blooming** | Maida Vale — relatively **dry** |
| Host | **Kontakt 8 / free Kontakt Player** (drive-resident, 345 GB) | **Native AU** in Logic (system drive) |
| The asset | **The hall.** Already-drenched real orchestra | **The dryness.** A blank space to invent around |
| Degrade approach | Degrade the **character** (tape/sat/lo-fi); *don't* pile on reverb | Build the **space** (Valhalla→VintageVerb) *then* degrade |
| Reach for it when | You want the **sound of the score** — a recognisable orchestra behaving ethereally, *already wet*; percussion/harp blooming in the gallery; the lush film-score signature | You want a **controllable dry skeleton** to wreck into your own invented space; tight control over the room |
| The decision in one line | "I want the gorgeous hall baked in" → **SSO** | "I want to build the space myself" → **BBC SO** |

Both are the *realism* tools (recognisable orchestra), used **sparingly as a ghost under the
banjo/baritone**, never the centerpiece. When you want texture that needn't read as a real
orchestra at all, skip both and reach for the **designed-texture libs you own** — Orchestral
Swarm (granular shimmer), SSEvo/SSSE (scripted evolving walls), Ólafur Cells (generative
chamber), Fractured Strings (refracting texture). In practice the orchestral forums **almost
never reach for a realism library when someone asks for "a soft pad"** — that's a tell that SSO
is the heavyweight you pull *only* when realism + the wet hall are the point.
[research/Spitfire-Navigator.md; research/BBC-Symphony-Orchestra-UsageGuide.md; links/sso-vicontrol-calm-soft-pads-reach-for.md; links/sso-vs-lco-textures-swarms-reach-for.md]

---

## 7. Common pitfalls / gotchas

- **Loading all mics by reflex = RAM death.** It's the #1 SSO mistake; use a single **Mix** or
  1–2 mics, and **Purge unused**. [transcripts/sso-pro-official-walkthrough-mics.md;
  transcripts/sso-symphonic-strings-purge-mics-dynamics.md]
- **Don't double the reverb.** SSO is already wet — adding a big hall on top muddies it; degrade
  character instead, or pull Close up if you need dry. [links/spitfire-nav-symphony-orchestra-textures.md]
- **It's not a plugin.** No native AU — must go through Kontakt. (Easy to forget after BBC SO.)
- **A2 vs A6 / ensemble sizes:** the section patches let you pick how many players (e.g. horns
  A2 = 2 per note vs A6 = 6); stacking the big ensembles can pile up unrealistic player counts
  and muddy a quiet bed — keep numbers small for the ghost.
  [transcripts/sso-guy-michelmore-full-tutorial-performance-patches.md]
- **Offline drive:** mount before launching; bounce beds to dodge external-drive streaming
  dropouts. [SoftwareProfile.md; links/sso-kontakt-purge-ram-streaming.md]
- **Footprint figure to reconcile on disk:** the relaunched library is reported as **~345 GB**
  (existing note) vs **~368 GB** (2025 update) — verify on the drive. [links/sso-kontakt-purge-ram-streaming.md]
- **Two different "Swarm" products — don't conflate:** Spitfire **Swarms** (harps/marimbas/
  mandolins) ≠ the rig's **Orchestral Swarm** (micro-detune string divisi — see the Navigator).
  [links/sso-vs-lco-textures-swarms-reach-for.md]
- **Performing CCs vary by patch generation:** CC16/CC17 (Expression/Release) come from the
  older SSO patch architecture and **may differ on the relaunched/Curated patches** — verify on
  disk. [links/sso-syntheticorch-performing-pads.md]

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`):
- `sso-pro-official-walkthrough-mics` — ★ the mic & articulation reference (Spitfire/Paul
  Thomson; full Pro mic palette, the dry-room-can't-fake-this quote, extended techniques).
- `sso-sampleist-overview-editions-ram` — ★ independent 50-min overview (The Sampleist; the
  345 GB / 5-mic vs Pro / ~700–750 GB combined picture, decorative techniques, "use flautando
  a lot," effects-over-a-drone).
- `sso-symphonic-strings-purge-mics-dynamics` — ★ the mechanics reference (Spitfire; Spanner
  page mics, mod-wheel-down + Expression "very delicate" trick, Purge unused / memory-chip).
- `sso-symphonic-woodwinds-textures` — breathy/soft woodwind textures (hollow long, flutter,
  bass flute, contrabassoon).
- `sso-symphonic-strings-evolutions-evogrid` — SSSE EVO grid (evolving symphonic walls, mic
  thinning, modestly-extreme phasing).
- `sso-guy-michelmore-full-tutorial-performance-patches` — composition walkthrough
  (performance patches, A2/A6 realism, mod wheel = dynamics, gentle trombone).
- `sso-motif-brass-2025-update` — 2025 free brass update (12-horn low-dynamic "beautiful"
  texture; "if you've heard film music in 10 years you've heard SSO").
- `sso-how-it-works-evolutions-short` — short EVO-grid explainer.

**Links** (`research/links/`):
- `sso-vicontrol-too-much-room-baked-in` — the wet-hall thread: even the close mic is roomy
- `sso-vicontrol-reverb-for-spitfire-orchestra` — how much reverb to add on top (mostly none); "feather, don't paint over"
- `sso-apg-relaunch-close-mic-room` — relaunch review; close mic still roomy; Curated Ensembles = instant 300-player pad
- `sso-syntheticorch-performing-pads` — soft-release/auto-swell pad playing; avoid high velocity
- `sso-kontakt-purge-ram-streaming` — Kontakt Player vs full, 368 GB, Technique-Editor purge, DFD preload, offline-drive relink
- `sso-sos-textural-articulations` — Sound on Sound: the textural sustain set + percussion-as-texture
- `sso-vicontrol-calm-soft-pads-reach-for` — the forum rarely reaches for a realism lib when asked for pads
- `sso-vs-lco-textures-swarms-reach-for` — SSO (realistic) vs designed-texture engines; the two-"Swarm" trap
- `sso-degrade-wet-bed-rig-recipe` — degrading a pre-reverbed source with the owner's plugins
- (Builds on the existing `links/spitfire-nav-symphony-orchestra-textures.md`.)

**QC / honesty flags:**
- **No dedicated "SSO for drone/doom/shoegaze" tutorial exists** — like BBC SO, the ghost-layer
  workflow is assembled from the official articulation/mic/dynamics mechanics + the rig's
  degrade chain. The PaulStretch / bounce-to-wall / EchoBoy-Decapitator-over-the-bloom steps are
  **inferred applications** of documented general methods, not a single "do this" source.
- **Edition / mic-count on disk unconfirmed** (offline drive). §4 names both the 5-mic relaunch
  set and the full Pro palette; which you actually have decides whether Gallery/Close Ribbon/
  Leader are available. The auto-captions occasionally mangle terms (flautando→"flotando/
  flando", chimbasso→"chambasso", Decca→"deku/decker", con sordino→"consort") — corrected here.
- **No verified drone/doom/shoegaze artist credit for SSO specifically** — it's a media-composer
  realism library; the citable lineage is the same neoclassical-ambient/film scene as BBC SO.

## Sources
See §8 for local captures (URL on line 1 of each). Originals: youtube.com (Spitfire Audio
official, The Sampleist, Guy Michelmore), soundonsound.com, spitfireaudio.com.
