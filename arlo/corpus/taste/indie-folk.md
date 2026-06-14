---
title: Indie-folk / confessional — Cluster Index (Track B2)
cluster: indie-folk-confessional
anchors: [Bon Iver, Sufjan Stevens, Big Thief / Adrianne Lenker]
focus_artist: Bon Iver
focus_songs: ["22 (OVER S∞∞N)", "715 - CRΣΣKS", "Death with Dignity", "Carrie & Lowell room", "Not"]
generated: 2026-06-14
derived_patches: 13
documented_green: 0
emulated_purple: 13
index_only_count: 1
lens: Research/Taste-Profile/taste-profile.md
tags: [taste-profile, track-b, bon-iver, sufjan, big-thief, indie-folk, prismizer, vocal-halo, banjo, close-mic]
---

# Indie-folk / confessional — Bon Iver / Sufjan / Big Thief cluster index

> **What this is.** The cross-rig view of every patch derived this wave from the indie-folk /
> confessional lens, anchored on Bon Iver's **vocal-halo** ("22 (OVER S∞∞N)" / "715 - CRΣΣKS"),
> Sufjan's **banjo + intimate room** (Carrie & Lowell, Seven Swans) and Big Thief's **raw live
> room** ("Not"). Patches that live on a gear sheet are appended there too (single source of truth);
> the **Antares Prismizer** has no gear sheet and is documented **here only** (index-only).
>
> **Provenance honesty (the headline).** **Every patch is 🟣 designed-to-emulate.** The actual
> methods here are a laptop + two Auto-Tunes + an **Eventide H8000** (the Messina), the **Antares
> Harmony Engine** played from a MIDI keyboard (the Prismizer), a **Shure SM7/SM57** close-mic'd
> falsetto, a **Deering Goodtime banjo** fingerpicked like a 4-string guitar, and an **iPhone Voice
> Memos** capture — **none of the user's pedals were ever used by these artists, and no artist
> setting exists for any of them.** So there are **0 🟢 documented settings and 14 🟣 emulations**,
> by design and flagged per the lens. The Refs name the real sound/record each patch chases; the
> *settings* are first-principles from each unit's own patch sheet + manual + the cited sources.
> No artist attribution is fabricated.
>
> **The hardest approximation flag — the vocal halo.** The Prismizer/Messina halo is a
> **MIDI-played, polyphonic, formant-shifted harmony cloud around one voice**. NO pedal the user
> owns can be MIDI-played into chords against the dry voice in real time. The **QI Etherealizer is
> the named hardware approximation** (a pitched grain-freeze cloud + chorus), and Dark Star's dual
> ±2-oct shifters / the VG-800 ALT-TUNE HARMONY give *fixed* pitched voices — they chase the
> RESULT (a halo of pitched copies), **not the method** (played harmony). Said explicitly per patch.

## How the artists actually get these sounds (research summary)

Captured to `Research/Taste-Profile/sources/`:

- **The vocal halo IS a Prismizer/Messina.** Bon Iver's "22 (OVER S∞∞N)" / "715 - CRΣΣKS" halo =
  Chris Messina's custom rig: voice → **Ableton + TWO Auto-Tunes** (one tunes hard, one outputs the
  **tonic**), tonic + a **MIDI keyboard** feed an **Eventide H8000** harmony program that spits up
  to **4 (semi-random) harmony notes**; the sum of dry + tuned + tonic + 4 harmonies = the choir-of-
  one-voice. The H8000's **artifacts/distortion are kept**; on "715" they **"hit it harder for more
  distortion."** ("It's not a thing… many things working together.")
  (`messina-prismizer-22-a-million-chain.md`, `messina-715-creeks-one-take.md`)
- **The Prismizer proper** = **Antares Harmony Engine Evo** run as a **MIDI-controlled instrument**
  (Harmony Source = MIDI Omni), **chords played live** over the vocal → 4 pitched layers, with a
  **LONG glide** (the slur) and **throat-length/formant** per register (shorter = cartoonish-up,
  longer = down). Prism + harmonizer; Francis Starlite's invention. (`prismizer-harmony-engine-recipe.md`)
- **Intimacy = close, dry, layered.** *For Emma* = one **SM57** for guitar AND voice, **stacked
  falsetto layers** to build a self-choir; later records = **SM7**, different distances per layer.
  The voice is **close and dry-forward**, space added later — never a hall swallowing it.
  (`bon-iver-sm7-close-mic-layered-falsetto.md`)
- **Sufjan's banjo** = **Deering Goodtime** (open-back), **played like a 4-string guitar**, mostly
  **fingerpicked rolling arpeggios** (folk, not Scruggs). Banjo leads *Seven Swans*; on *Carrie &
  Lowell* it enters under "Should Have Known Better." **Honesty correction:** "Death with Dignity"
  is fingerpicked **guitar**, not banjo. (`sufjan-banjo-deering-four-string-fingerpick.md`)
- **Carrie & Lowell room** = literally **iPhone Voice Memos** in hotel rooms (A/C hiss left in),
  produced by **Thomas Bartlett** who kept it sparse — the lo-fi capture IS the intimacy; reverb is
  a halo, not a hall; harmonies "echoes of the past." (`sufjan-carrie-lowell-iphone-bartlett-intimate.md`)
- **Big Thief "Not"** = **live in the room, no overdubs, live vocal** (Sonic Ranch; producer
  **Andrew Sarlo**). *Two Hands* is the deliberately raw "earth twin" to *U.F.O.F.*'s spectral
  overdubs. Sarlo: capture-the-performance, **leave the accidents in** (kept an accidental fade-in),
  and **EchoBoy slapback to "mimic my Space Echo"** on the vocal. (`big-thief-not-live-room-sarlo.md`,
  `andrew-sarlo-echoboy-imperfection-philosophy.md`)

> **Cluster tension worth naming.** Two modes live here: the **bare/raw** mode (Big Thief "Not,"
> Sufjan's whisper + iPhone) and the **halo/spectral** mode (Bon Iver, U.F.O.F. overdubs). The
> making-aesthetic tie-breaker pushes toward sustained/degraded — so most patches below build the
> halo/wall, but the **degrade is the intimate "recorded-wrong" kind (cassette/iPhone), not doom
> fuzz**, and CB Clean + a present dry source stays underneath. Keep the voice close.

---

## Patches on gear sheets (appended there too)

### Walrus QI Etherealizer — the hardware Prismizer-halo approximation  (3 patches)

> The named hardware approximation of the vocal halo. It chases the RESULT (a pitched harmony cloud
> around one voice) — it CANNOT be MIDI-played into chords like the real Prismizer, so the cloud is
> fixed/drifting, not played harmony. RIG-CRITICAL: pad/reamp the VG-800 line level (no level switch).

| # | Patch | Ref (artist sound) | Prov |
|---|-------|--------------------|------|
| QI-TB1 | **Prismizer Halo Freeze Cloud** ⭐ | Bon Iver "22 (OVER S∞∞N)"/"715" Prismizer halo | 🟣 |
| QI-TB2 | **Layered-Falsetto Self-Choir Pad** ⭐ | Bon Iver stacked-SM7 falsetto self-choir | 🟣 |
| QI-TB3 | **iPhone-Intimate Faint Wash** ⭐ | Carrie & Lowell close/dry voice, halo-not-hall | 🟣 |

- **QI-TB1:** Flow **Parallel** (live banjo stays present on top, like the dry vocal). Grain mode
  **Grain Cloud**, Grain Mix **1–2:00**, X **~11:00**, **Playback x2 (+1 oct)** for the bright
  prism-up layer. Chorus **Tri**, Mix **~11:00**, Rate **9**, Depth **11** (the slur/glide stand-in
  for the Prismizer's long glide). Delay Mix off. Space **10–11:00** (modest — Dark Star owns space).
  Tone **~1:00** (roll the banjo ice-pick). Play a chord/banjo roll → **short-press Freeze** = the
  grain cloud loops = a pitched harmony cloud around the held note; play the lead over it. For the
  "715 hit-it-harder" distortion, push the VG-800/Board-1 source hot before the (padded) input.
  **Approximation flag:** fixed pitched cloud, NOT MIDI-played 4-note harmony — chases the result.
- **QI-TB2:** Flow **Parallel**. Grain **Grain Cloud**, Mix **noon**, Playback **x1** (unison
  thickening, not an interval). Chorus **Tri**, Mix **~1:00** (dominant — the "many voices"),
  **Rate ~10, Depth ~1:00** (lush detune = the stacked-layer beating). Tone **noon**. Space
  **9–10:00**. Freeze a sung/banjo chord → the looping unison-grain + heavy chorus = a self-choir of
  one source. The unison-x1 + chorus is the literal stand-in for "stack falsetto layers."
- **QI-TB3:** Flow **Parallel**, **Mix/Dry HIGH** (mostly dry — the voice stays close/present).
  Grain Mix **~10:00** (faint), **Grain Cloud**, x1. Chorus low (**~9:00**). Delay off. Space
  **9:00** (a halo, not a hall). Tone **~11:00**. The texture sits *behind* a dry-forward source —
  the documented Carrie & Lowell "close, dry, space-added-faintly" balance. The restraint patch.
- **Refs:** `messina-prismizer-22-a-million-chain.md`, `prismizer-harmony-engine-recipe.md`,
  `bon-iver-sm7-close-mic-layered-falsetto.md`, `sufjan-carrie-lowell-iphone-bartlett-intimate.md`

### Roland VG-800 — banjo-as-lead + the played-harmony halo  (3 patches)

> The string source. VG-TB1 is the closest the rig gets to the Prismizer *method* — a played
> diatonic harmony voice on the banjo — but it's ONE fixed interval, not 4 MIDI-played notes.

| # | Patch | Ref (artist sound) | Prov |
|---|-------|--------------------|------|
| VG-TB1 | **Banjo Halo Harmony Drone** ⭐ | Bon Iver halo / Sufjan layered-harmony "echoes" | 🟣 |
| VG-TB2 | **Sufjan Fingerpicked Banjo Lead** ⭐ | Sufjan Deering Goodtime, banjo-as-lead, Seven Swans | 🟣 |
| VG-TB3 | **iPhone-Intimate Clean Acoustic Bed** ⭐ | Carrie & Lowell fingerpicked guitar/banjo, Big Thief "Not" dry | 🟣 |

- **VG-TB1:** Recall **GK SETTING slot 1 (EBM5 BANJO)**. `INST = E.GUITAR` (or VIO for attackless).
  `ALT TUNE SW = ON`, `ALT TUNE MODE = HARMONY`, `HARMONY = +1 oct` **or** a `USER SCALE` diatonic
  **3rd/5th** (set `KEY` to the tune's key). `NORMAL MIX ~30%` (keep the dry banjo under the
  harmony). Optional `SUSTAIN`/`SLOW GEAR` for a drone entry. This is the rig's nearest analogue to
  the Prismizer's *played* harmony — a banjo lead with a fixed diatonic voice stacked on it.
  **Approximation flag:** one fixed interval, NOT the 4-note MIDI-played, formant-shifted cloud —
  layer QI-TB1/QI-TB2 downstream for the cloud, this for the played voice. (Builds on VG sheet #30.)
- **VG-TB2:** Recall **EBM5 BANJO**. `INST = E.GUITAR` or `ACOUSTIC`, **5th string excluded**
  (`STRING MUTE 5` / `STRING LEVEL 5 = 0`, keep the real 5th drone via `NORMAL MIX ~20–40%`) =
  Sufjan's "banjo as a 4-string guitar." Bright/clean, no dirt, `NORMAL MIX` moderate so the real
  pluck/finger noise stays. Onboard REV/DLY off. Fingerpick rolling arpeggios — the lead voice for
  the whole cluster.
- **VG-TB3:** `INST = ACOUSTIC` (J-45 / D-28). `ALT TUNE TYPE = OPEN D` or `OPEN G` (circular open
  tunings, Sufjan-style) **or** standard. Minimal/no dirt, `NORMAL MIX` low, onboard FX off — a
  pristine, present, close source. Keep ACOUSTIC RESONANCE OFF if you want downstream per-string
  pan. Feed this into the iPhone-degrade chain (Chroma CASSETTE) or leave dry for the "Not" raw bed.
- **Refs:** `sufjan-banjo-deering-four-string-fingerpick.md`,
  `prismizer-harmony-engine-recipe.md`, `big-thief-not-live-room-sarlo.md`

### Hologram Microcosm — orchestral/electronic wash around a single voice  (2 patches)

| # | Patch | Ref (artist sound) | Prov |
|---|-------|--------------------|------|
| MC-TB1 | **Glacial Halo Bed (Haze)** ⭐ | Bon Iver/U.F.O.F. spectral wash around the voice | 🟣 |
| MC-TB2 | **Banjo Fingerpick Onset-Halo (Strum/Mosaic)** ⭐ | Sufjan fingerpicked banjo → harmony "echoes" cloud | 🟣 |

- **MC-TB1:** Global Config baseline (Stereo in, Line, Buffered+Trails). Engine **HAZE (Granules)
  variation B or D** (the glacial grain-wash; D = +half-speed octave-down for body). Activity
  **~1:00** (density), Shape **~1:00** (slow envelope), Filter **11–12** (tame banjo top), Space
  **~2:00** (mostly wet), Mix **~11:00** (sits *behind* the dry voice — like the faint C&L wash). A
  glacial diffuse bed around a single close source; hand it to QI-TB3 / Dark Star. (Microcosm sheet
  #11 / #27.) **Keep Mix modest** — this is the halo-not-hall move, not a takeover.
- **MC-TB2:** Engine **STRUM (Granules) variation B** (onset chains — many copies of the most-recent
  pluck overlap into phasing/cascading runs) **or MOSAIC A** (octave-up harmony loops). Feed
  fingerpicked banjo plucks; the engine chains them into a cloud of pitched copies = a granular
  stand-in for the "intertwining harmony echoes." Filter **noon** (tame 2–4 kHz), Mix **noon** (dry
  banjo lead present). For the brighter prism-up colour use Mosaic A (octave-up). (Microcosm #13 / #6.)
  **Approximation flag:** a granular pitch-cloud, not played harmony.
- **Refs:** `prismizer-harmony-engine-recipe.md`, `sufjan-banjo-deering-four-string-fingerpick.md`,
  `bon-iver-sm7-close-mic-layered-falsetto.md`

### Hologram Chroma Console — the iPhone / cassette intimate-degrade + room  (2 patches)

| # | Patch | Ref (artist sound) | Prov |
|---|-------|--------------------|------|
| CC-TB1 | **iPhone Voice-Memo Cassette Capture** ⭐ | Carrie & Lowell iPhone Voice Memos, A/C-hiss-left-in | 🟣 |
| CC-TB2 | **Live-Room Slapback Glue (EchoBoy-style)** ⭐ | Big Thief "Not" / Sarlo EchoBoy "mimic my Space Echo" | 🟣 |

- **CC-TB1:** The cluster's true "recorded-wrong" patch — but the *intimate/lo-fi* kind, not doom.
  TEXTURE **CASSETTE**, AMOUNT **~10–11 o'clock** (wow/flutter/hiss = the iPhone-in-a-hotel-room
  degrade). CHARACTER **SWEETEN** both ~**9–10** (gentle preamp lift so the close source still
  reads present). MOVEMENT **VIBRATO**, RATE **~9**, AMOUNT **~8**, secondary **DRIFT ~9** (subtle
  pitch warble = "wrong machine"). DIFFUSION bypassed or **SPACE** tiny (halo, not hall). **MIX
  ~65–70%**. Don't double Gen Loss tape — pick this OR Gen Loss as "the tape." (Chroma sheet #2 / #4.)
- **CC-TB2:** DIFFUSION **REELS** (tape echo) set to a short **slapback** TIME, AMOUNT (feedback)
  low (one-two repeats), secondary **DRIFT ~50** (aged/flutter — the Space-Echo character Sarlo
  chased). CHARACTER **SWEETEN** light glue. Keep MIX modest so it's a glue texture on the close
  voice, not a wash — the documented EchoBoy-on-lead-vocal move. Mono→stereo re-expansion: run
  **Buffered+Trails**, both outs connected. (Chroma sheet #1 / DRIFT cheat-sheet.)
- **Refs:** `sufjan-carrie-lowell-iphone-bartlett-intimate.md`,
  `andrew-sarlo-echoboy-imperfection-philosophy.md`, `big-thief-not-live-room-sarlo.md`

### OBNE Dark Star V3 — pitched halo + orchestral wash terminus  (2 patches)

> Dark Star's dual ±2-oct shifters give two FIXED pitched voices — a hardware echo of the halo's
> pitched copies (not played harmony). Board-2 terminus: Stereo, trails on.

| # | Patch | Ref (artist sound) | Prov |
|---|-------|--------------------|------|
| DS-TB1 | **Halo Shimmer Pad (dual-pitch glide)** ⭐ | Bon Iver Prismizer halo / pitched-up cloud | 🟣 |
| DS-TB2 | **Orchestral Halo Freeze Bed** ⭐ | Bon Iver/Sufjan orchestral-electronic wash around one voice | 🟣 |

- **DS-TB1:** Routing **Stereo**, trails on. **Pitch 1 = +1 oct (L) · Pitch 2 = detune just off
  unity (R)** (a bright prism-up voice + a chorused near-unity drop — mirrors the Prismizer's
  up-harmony + slurred body). Use the **"a in Dark"** off-noon trick to seat unity, then nudge Pitch
  2 a hair for chorused width. **Crush = ~12** (clean — this is the intimate, not doom lane, but pull
  to ~11 for a light degraded edge). **Filter = ~1 (HPF, glassy)** so the up-voice floats; favor the
  **LPF side** if it ice-picks over banjo. Decay **mid-high**, Multiply **low-mid** (no runaway),
  Mix **mostly wet but under the dry voice**. (Dark Star sheet #4 / #6 / #25.) **Approximation flag:**
  two fixed pitched voices, not the played 4-note halo.
- **DS-TB2:** Build a wide pad (**Pitch 1 = +1 oct, Pitch 2 = −1 oct** opposed split = orchestral
  spread; or both detuned for a chorused cloud), **Decay high**, **Lag low**, **Multiply ~noon**,
  **Mix high**, **Crush ~11** (faint lo-fi). Assign **Aux = Hold**; play a banjo roll / VG pad →
  **freeze** → a static orchestral halo bed; solo the banjo over it. ⚠️ Hold passes new notes
  BONE-DRY — that's fine here (the dry banjo lead sits in front, exactly the close-voice-over-halo
  balance). (Dark Star sheet #13 / #24.)
- **Refs:** `messina-prismizer-22-a-million-chain.md`, `prismizer-harmony-engine-recipe.md`,
  `sufjan-carrie-lowell-iphone-bartlett-intimate.md`

---

## Index-only patch — software, no gear sheet

### Antares Prismizer (Antares Harmony Engine Evo) — the vocal-halo recipe  🟣⭐ (INDEX-ONLY)

> **The actual software effect** behind the whole cluster's signature sound. Documented HERE ONLY —
> it has no gear sheet (it is not one of the user's pedals). The **QI Etherealizer is the rig's
> hardware approximation** (see QI-TB1/QI-TB2 above) of the *result*; nothing the user owns
> reproduces the *method* (a MIDI-played, formant-shifted, polyphonic harmony cloud).

| Patch | Ref | Settings (the documented software recipe) | Prov |
|-------|-----|-------------------------------------------|------|
| PRZ-TB1 **Vocal Halo (Prismizer)** ⭐ | Bon Iver "22 (OVER S∞∞N)" / "715 - CRΣΣKS"; Francis & the Lights; Frank Ocean *Blonde* | **Antares Harmony Engine Evo** as a **MIDI-controlled instrument**; **Harmony Source = MIDI Omni**; **sidechain to the dry vocal**. **Play chords on a MIDI keyboard** while the vocal plays → up to **4 pitch-shifted harmony layers**. **Glide/transition = LONG** (the signature slur). **Throat length** per register: shorter = brighter/up, longer = down. For the full Messina: chain **2× Auto-Tune** (hard-tune + tonic-extractor) feeding an **Eventide H8000** harmony program; keep the artifacts; "hit it harder" for more distortion. | 🟣 |
| Refs | | `prismizer-harmony-engine-recipe.md`, `messina-prismizer-22-a-million-chain.md`, `messina-715-creeks-one-take.md` | |

- **Provenance honesty:** even the software recipe is 🟣 here — it's the *published method*, but the
  user's exact MIDI-chord choices, key, and glide are theirs to dial; no single "Bon Iver preset"
  with numeric Harmony Engine values exists. The user could run this **in the DAW on the banjo/voice**
  for the genuine article, then **the pedals only approximate it live** (QI freeze-cloud + chorus
  for the cloud; Dark Star dual-pitch for the pitched copies; VG-800 ALT-TUNE HARMONY for one played
  voice).

---

## Chain recipes (putting it together)

- **The vocal halo, in the box (genuine):** banjo/voice → **DAW: Antares Harmony Engine (PRZ-TB1)**
  played from a MIDI keyboard → long glide → light EchoBoy slapback. This is the only way to get the
  *real* halo. Everything below is the live-rig approximation.
- **The vocal halo, on the rig (approximation):** banjo via **VG-TB1** (one played diatonic voice) →
  CB Clean (present) → **QI-TB1** Prismizer-halo grain-freeze cloud (Parallel, x2 + chorus glide) →
  **DS-TB1** dual-pitch shimmer pad → trails to Board 3. Flag: fixed cloud, not played 4-note harmony.
- **Sufjan banjo + intimate room:** **VG-TB2** fingerpicked banjo (5th excluded) → CB Clean →
  **MC-TB2** onset-halo (dry banjo present, granular harmony cloud behind) → **CC-TB1** iPhone
  cassette degrade (halo-not-hall) → faint **QI-TB3** wash. Close, dry, recorded-wrong-but-intimate.
- **Big Thief "Not" raw mode (restraint):** **VG-TB3** clean acoustic/banjo → CB Clean → **CC-TB2**
  light EchoBoy-style slapback glue → (texture pedals barely on). Capture the performance; leave the
  finger noise. The deliberately under-processed anchor.
- **Orchestral wash around one voice (U.F.O.F. spectral side):** VG pad/banjo → **MC-TB1** glacial
  Haze bed → **DS-TB2** orchestral halo freeze → solo the banjo over the frozen bed.

## Honesty ledger

- **Documented 🟢:** 0. (No Bon Iver / Sufjan / Big Thief artist setting exists for any of the
  user's pedals — they used a laptop + 2 Auto-Tunes + an Eventide H8000, the Antares Harmony Engine,
  a Deering banjo, SM7/SM57 mics, and an iPhone.)
- **Emulated 🟣:** 13 — **12 on gear sheets** (QI Etherealizer ×3, VG-800 ×3, Microcosm ×2, Chroma
  Console ×2, Dark Star ×2) **+ 1 index-only software patch** (Antares Prismizer). Index-only count = **1**.
- **Approximation flags (critical):** the **vocal halo cannot be reproduced on the rig** — the
  Prismizer/Messina is a **MIDI-played, formant-shifted, polyphonic** harmony cloud; the QI
  Etherealizer (named approximation) gives a *fixed/drifting pitched cloud*, Dark Star gives *two
  fixed pitched voices*, the VG-800 gives *one played diatonic voice*. All chase the RESULT, not the
  METHOD — only the in-the-box Antares Harmony Engine (PRZ-TB1) gets the genuine article. The
  **degrade in this cluster is the intimate iPhone/cassette kind, NOT doom fuzz** — CB Clean and a
  present dry banjo/voice stay underneath every patch. "Death with Dignity" corrected to fingerpicked
  guitar (not banjo). All flagged inline.
