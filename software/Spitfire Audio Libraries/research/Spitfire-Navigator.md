# Spitfire — Navigator

Which Spitfire library to reach for, and how they actually run on an AU-only Logic
rig with the content on an external drive. The two deep flagships have their own
guides: **`LABS-UsageGuide.md`** and **`Olafur-Arnalds-Cells-UsageGuide.md`**. This
navigator covers the rest + the cross-library "reach-for" map.

## 1. The three-host landscape (knowing which is which is the whole map)

`research/links/spitfire-nav-player-vs-kontakt-split.md`
- **Spitfire's own DEDICATED PLUGIN** (newer libs) — bespoke player with mic mixer,
  macros, the **Evo Grid**; native **AU/VST3**, no Kontakt. **Owned & installed (on
  the system drive):** **BBC Symphony Orchestra · Fractured Strings · Resonate ·
  Ólafur Arnalds Cells · Originals – Rare Flutes · LABS** (= the six CONTENTS
  entries).
- **Free KONTAKT PLAYER** (older "Player" libs) — load in the free Kontakt Player
  (appear in Kontakt's Libraries pane after authorising in Native Access). **Owned
  (on the offline drive):** **Albion Loegria · Orchestral Swarm · Symphonic Strings
  Evolutions · Spitfire Symphony Orchestra.**
- **Full KONTAKT (paid)** — for non-Player content + sample editing. **You own full
  Kontakt 8**, so even that's covered.

**Practical rule (Logic AU):** newer textural/string-colour sound → open the
dedicated plugin directly; **evolving/orchestral WALL libs (Loegria, Swarm, SSEvo,
Symphony) → open Kontakt 8 first, then load the Library** (one Kontakt instance hosts
several).

## 2. External-drive workflow

`research/links/spitfire-nav-app-external-drive.md`
- The **Spitfire Audio app** is the install/update manager. Install to drive:
  **Install → folder icon → browse to drive → Install**; make permanent via
  **Settings → Default Content Path**.
- **Drive must be `Mac OS Extended (Journaled)`** — ExFAT prompts a reformat, FAT32
  is incompatible. SSD preferred; HDD must be 7200 rpm. Budget ~2× listed size during
  install.
- Moving content moves only the *registration* — drag the folder, then per-product
  **cog → Locate** (same machine) / **Repair** (new machine).
- **The AU plugins live on the system drive and always load; only the multi-GB sample
  content needs the drive.** So **mount `PlaySomeGodDamnMusic` BEFORE launching
  Logic**, or libraries show "not found" and need a Locate.

## 3. The reach-for map (which owned library, when)

| The job | Reach for | Host |
|---|---|---|
| **Symphonic evolving STRING WALL** (big, dark, slow crescendos) | **Symphonic Strings Evolutions** | Kontakt |
| **ALIVE, shimmering string bed** (micro-detuned, never still) | **Orchestral Swarm** | Kontakt |
| **Intimate / haunting evolving chamber strings** | **Ólafur Arnalds Cells** *(own guide)* | Dedicated |
| **Glittering, refracting texture / happy accidents** | **Fractured Strings** | Dedicated |
| **Metallic drone / resonant wash / impossible aftershock** | **Resonate** | Dedicated |
| **Believable faint real-orchestra ghost** | **BBC SO** (sul tasto/flautando/harmonics) | Dedicated |
| **Breathy/overblown ethnic-flute mystique** | **Originals – Rare Flutes** | Dedicated |
| **Airy chamber strings + organic synth + odd loops** | **Albion Loegria** | Kontakt |
| **Recognisable full orchestra behaving ethereally** | **Spitfire Symphony Orchestra** (sustains only — now deep-dived: `research/Symphony-Orchestra-UsageGuide.md`, the WET-Lyndhurst counterpart to BBC SO) | Kontakt |
| **Free hidden-gem textures / drones** | **LABS** *(own guide)* | Dedicated |

`research/links/spitfire-nav-symphonic-strings-evolutions.md`, `research/links/spitfire-nav-orchestral-swarm.md`, `research/links/spitfire-nav-loegria.md`, `research/links/spitfire-nav-symphony-orchestra-textures.md`, `research/links/spitfire-nav-originals-rare-flutes.md`

**The three evolving-wall poles you already own:** **SSEvo** (symphonic, *scripted*
Evos), **Orchestral Swarm** (chamber, *human micro-detune shimmer*), **Cells**
(intimate chamber, *generative*) — all feed the layer-under-banjo-into-Valhalla/
EchoBoy/Decapitator workflow.

## 4. Fractured Strings & Resonate (the two on-aesthetic owned ones)

**Fractured Strings** (dedicated plugin) — experimental string *texture*, made with
**Hans Zimmer's Bleeding Fingers** (*Frozen Planet II*). 8-piece ensemble + soloists,
**42 violin "fractures"** with controllable speed, tempo-synced Rotations, trill
"Dispersals," **Scale Mode** (conform to any mode or a custom scale, velocity-
controlled intervals), Evo Grid + randomise. "Glittering and refracting." **Vendor's
own rule: "duck and hide within other arrangements, poking its head out for flavour"
— seasoning, not the dish.** `research/links/spitfire-nav-fractured-strings-sos-review.md`, `research/links/spitfire-nav-fractured-strings-spitfire-product.md`

**Resonate** (dedicated plugin) — experimental percussion-*resonance*, made with
**Dame Evelyn Glennie**. Captures the **reverberations that FOLLOW the strike** of
four resonators (Barrel, Timpani, Water Tank, Thundersheet); 7 mics incl.
**contact + underwater**; five **Warp FX chains** ("gritty/organic → endlessly
resonating reverb") + a **Stretch** timing effect. The **metallic drone / impossible-
aftershock / resonant-wash** generator — a sound-design tool, not a percussion
library. `research/links/spitfire-nav-resonate-cm-review.md`, `research/links/spitfire-nav-resonate-spitfire-product.md`

## 5. BBC SO for this aesthetic (brief)

The realistic orchestra (dedicated plugin), recorded **dry** at Maida Vale — an
advantage here (minimal baked-in hall = more control into Valhalla/EchoBoy). The
patches that serve drone/doom/shoegaze: **Super Sul Tasto** (ultra-soft ghostly — the
single most useful), **Long Flautando, Con Sordino, Harmonics, Sul Tasto.** Reach for
it when you want a **believable faint real-orchestra ghost** under banjo; reach for
Fractured/SSEvo/Swarm when you want *designed* texture over realism. Rarely the
centerpiece. `research/links/spitfire-nav-bbcso-textures.md`

**→ Now fully deep-dived:** `research/BBC-Symphony-Orchestra-UsageGuide.md` (articulation map,
mic guidance, dry→degrade chain, the Jóhannsson method, edition gate Discover/Core/Pro).

## 6. Notable users (sourced, flagged)

- **Ólafur Arnalds** — named collaborator; you own **Cells = his generative-strings
  tool**. (HIGH, vendor.) **Hans Zimmer / Bleeding Fingers** — co-created Fractured
  Strings. (HIGH.) **Dame Evelyn Glennie** — co-created Resonate. (HIGH.) `research/links/spitfire-nav-notable-users-aesthetic.md`
- **Aesthetic lineage** (Max Richter, Nils Frahm, Hildur Guðnadóttir, Ben Frost,
  Jóhann Jóhannsson — the post-classical/Bedroom Community scene): MEDIUM as a scene
  association.
- **Honest gap:** no hard source ties classic drone/shoegaze acts (Stars of the Lid,
  Hammock, Grouper) to these *specific* Spitfire libraries — the citable thread is the
  post-classical/film lineage, not the rock-drone canon.

## 7. Flagship sub-guides

- **`LABS-UsageGuide.md`** — the free texture instrument (4 transcripts + 5 links).
- **`Olafur-Arnalds-Cells-UsageGuide.md`** — the generative chamber-strings engine
  (4 transcripts + 7 links).

## 8. Captured sources

**Navigator links (14)** — `research/links/spitfire-nav-*`: the 3-host split, the
external-drive workflow, Fractured Strings (×2), Resonate (×2), SSEvo, Orchestral
Swarm, Loegria, Symphony Orchestra textures, BBC SO textures, Originals Rare Flutes,
the KVR cross-Evo comparison, notable users. (LABS + Ólafur captures indexed in their
own guides.)

## Sources

All claims cite a captured file in `research/links/` (first line = the original URL).
Primary: Spitfire product pages, Sound on Sound, Computer Music, KVR. **Honesty
flags:** community *usage*-tutorial depth for Loegria/Orchestral Swarm is thin
(sourcing is vendor + magazine reviews — what a navigator needs); the **drive is
offline**, so exact installed sub-products/versions couldn't be confirmed from disk
(owned list = CONTENTS.md dedicated-plugin libs + the inventory note for the Kontakt
libs).
