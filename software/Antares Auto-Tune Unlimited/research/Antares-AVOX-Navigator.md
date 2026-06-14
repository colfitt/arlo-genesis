# Antares Auto-Tune Unlimited — Bundle Navigator

The reach-for map across the **22 installed plugins** (not 41 — see correction below) for a
drone/doom/shoegaze rig. These are vocal processors, but the rig uses them **creatively on
any source** — banjo lead, baritone, synth, drones, vocals. The creative-angle intro lives
in `Antares-UsageGuide.md`; this is the "what's in the box / which to open" layer. Four
flagships get their own deep-dive guides (marked **DD**).

> **Roster correction (2026-06-11):** the plan/memory said "41-component AVOX roster." The
> actual installed bundle (CONTENTS.md) is **22 plugins** — 8 AVOX modules + Harmony Engine
> 4x + Mic Mod + Auto-Key + 6 Auto-Tune editions + Slice + SoundSoap + Vocal Comp/EQ/
> De-Esser/Reverb + Vocodist. The marketing "11 AVOX / Sybil de-esser" framing does **not**
> match the install — the installed de-esser is the standalone **Vocal De-Esser**; **Sybil
> is not present**.

Reach-for key: **GOLD** = aesthetic centerpiece · **SIT** = situational · **SKIP** =
corrective/redundant for this rig.

## The 22-tool map

### Pitch / tuning
| Tool | Job | This rig | Note |
|---|---|---|---|
| Auto-Tune **Pro X** | Full Auto + **Graph** pitch/time draw, Classic Mode | **GOLD** | The one to open. **Graph mode** = draw a mono banjo/synth to *wrong* targets = designed alien melody. Retune Speed 0 + Classic = hard robotic snap. |
| Auto-Tune **EFX+** | Effect-first tuner + **Auto-Motion** pattern generator + 4 FX | **GOLD** | Held note → auto-generated stepped robotic arpeggio. The creative wildcard. |
| Auto-Tune **Slice** | Transient-slice + tune ANY phrase into a playable kit; 14 FX (ring mod, tube, chorus) | **GOLD** | Hidden gem — **sidesteps the mono-input limit**; chop banjo/vocal/found-sound into a tuned MIDI chop-instrument. Pairs with the MPC / 61SL workflow. |
| Auto-Tune **Access** | Basic auto-tune; lightest CPU | SIT | The CPU-saver tuner when a Choir/Harmony session redlines. 3 ms "Fast" = its hardest snap. |
| Auto-Tune **Artist** | Pro minus Graph | SKIP | Pro-minus-the-fun-part; Graph is the reason to use Pro. |
| **Auto-Key** | Key/scale detector → pushes to the tuners | SIT | Utility; or set the wrong key on purpose. |

### Harmony / ensemble / voices
| Tool | Job | This rig | Note |
|---|---|---|---|
| **Harmony Engine 4x** | 4 harmony voices + per-voice Choir + Throat + Freeze; MIDI-playable; works on instruments | **GOLD · DD** | Played choral/drone beds from the 61SL; **Freeze** = held wall. → `Harmony-Engine-UsageGuide.md` |
| AVOX **Choir** | 1 → up to 32 unison voices + variation + spread | **GOLD · DD** | One held note → shimmering detuned choir wall. → `AVOX-Choir-UsageGuide.md` |
| AVOX **Duo** | One automatic double + pitch/timing/vibrato/pan | SIT | Tight widener; lighter than Choir. |

### Timbre / formant / character
| Tool | Job | This rig | Note |
|---|---|---|---|
| AVOX **Throat** | Physical vocal-tract reshape, beyond-anatomy formants | **GOLD · DD** | Impossible/gender-wrong formant drones. → `AVOX-Throat-UsageGuide.md` |
| AVOX **Mutator** | Ring-mod (24 mutations) + throat + Alienize reverse-chop | **GOLD · DD** | #1 alien/monster/destroyed texture. → `AVOX-Mutator-UsageGuide.md` |
| **Vocodist** | 20-model vocoder + carrier + sat/ring-mod/chorus | **GOLD · DD** | Machine-choir on a drone carrier; internal carrier (Voice/Key-track) = no routing, no Logic AU blocker. → `Vocodist-UsageGuide.md` |
| AVOX **Articulator** | 2-input talkbox/vocoder | SIT | Older/lighter vocoder — Vocodist is deeper; pick one. |
| AVOX **Warm** | Tube saturation (Velvet/Crunch) on any source | SIT–GOLD | Clean, polite tube colour vs Decapitator's aggression. Same engine inside Mic Mod. |
| **Mic Mod** | 125+ mic models = mic-shaped EQ + proximity + tube sat | SIT | Coloration on any clean source; model a cheap/lo-fi mic for "recorded-wrong" character *(extrapolated)*. |

### Dynamics / intelligibility / clean-up — mostly SKIP in a drone rig
| Tool | Job | This rig | Note |
|---|---|---|---|
| AVOX **Aspire** | Add/subtract breath noise | SKIP | RC-20/SketchCassette do air/noise better. |
| AVOX **Punch** | Vocal impact enhancer | SKIP | Lead-vocal loudness glue; opposite of a smeared wall. |
| **Vocal Compressor** | AI vocal comp | SKIP | Corrective lead-vocal glue. |
| **Vocal EQ** | AI voice corrective EQ | SKIP | Stock EQ covers it. |
| **Vocal De-Esser** | AI sibilance reducer | SKIP | Pure corrective, vocal-only. |
| **SoundSoap** | Noise removal / restoration | SKIP* | Opposite of the aesthetic; *one perverse "over-scrub to a hollow husk" angle (speculative). |
| **Vocal Reverb** | Vocal reverb — Hall/Plate/Room + 2 delays + pre-FX Pitch/Throat/**Reverse** | SKIP* | Valhalla wins tails; *only earns a slot for its **Reverse/Pitch/Throat** pre-verb tricks in one box. |

Apps: **Auto-Tune Central** (license/install manager) · **Vocal Prep** (chain front-end; instrument-irrelevant — skip).

## Reach-for by job (this rig)
- **Drone/choir wall from one held note** → **Choir** (16/32) · or **Harmony Engine 4x + Freeze**.
- **Played choral bed from the 61SL controller** → **Harmony Engine 4x** (MIDI Omni + Choir multiplier).
- **Alien / monster / metallic / backwards mangle** → **Mutator**.
- **Impossible / gender-wrong formant drone colour** → **Throat**.
- **Robotic hard-tune (voice or mono banjo/synth)** → **Auto-Tune Pro X** (Retune 0, Classic on).
- **Designed inhuman melody you draw** → **Auto-Tune Pro X Graph** (only Pro has it).
- **Generative robotic arpeggio from a held note** → **EFX+ Auto-Motion**.
- **Machine-choir / talking-pad over a drone carrier** → **Vocodist** (or Articulator for a lighter talkbox).
- **Chop a recorded phrase into a tuned playable instrument** → **Auto-Tune Slice** (no mono limit).
- **Tube warmth on any source** → **Warm**. **Mic-shaped / lo-fi colour** → **Mic Mod**.

## Overlaps / what to skip vs the rig's existing tools
- **Vocal Reverb → Valhalla VintageVerb/Room wins.** Vocal Reverb only for its baked-in Reverse/Pitch/Throat pre-verb tricks.
- **Warm / Mic Mod tube sat overlaps Decapitator** (Warm = clean/polite, Decap = aggressive); Mic Mod overlaps RC-20/SketchCassette for "make it worse."
- **Articulator overlaps Vocodist** — Vocodist is the keeper.
- **Vocal Comp / EQ / De-Esser / SoundSoap / Punch / Aspire** = corrective pop-vocal chain; redundant or anti-aesthetic.
- **Auto-Tune Artist** redundant with Pro; **Hybrid** (Avid DSP) is not installed.

## Universal gotchas
- **Most AVOX timbre/harmony tools are MONO-INPUT** (Throat, Mutator, Harmony Engine voices, Choir's source) — comp a clean single-note take; strums/double-stops won't track. **Auto-Tune Slice** is the exception (it slices any source).
- **All AU + VST3** → fine in Logic (AU-only). In **Ableton Live 12 Lite**, bounce/resample heavy returns to stay under the track ceiling.
- **Subscription** (Unlimited) — lapse = plugins stop authorizing.
- Physical-model/pitch-track/ring-mod tools (Throat, Mutator, Harmony Engine) are **CPU-heavy → print/freeze**.

## Flagship deep-dive index
- `Harmony-Engine-UsageGuide.md` — played harmony beds, Prismizer wall, Freeze
- `AVOX-Choir-UsageGuide.md` — one-note → 32-voice wall
- `AVOX-Throat-UsageGuide.md` — physical-tract re-voicing, impossible formants
- `AVOX-Mutator-UsageGuide.md` — ring-mod / Alienize / destroyed textures
- `Vocodist-UsageGuide.md` — 20-model vocoder; machine-choir / talking-drone; Logic carrier routing

## QC notes
22-tool count verified against CONTENTS.md. Antares' own pages are JS-walled (titles only to
the fetcher) — Vocal Reverb/Comp/EQ specifics triangulated from search summaries + Recording
Magazine; niche AVOX (Articulator/Aspire/Punch) have near-zero tutorial coverage, sourced
from product copy. **No verified drone/doom/shoegaze artist credit exists for any AVOX tool**
— reach-for verdicts are by capability + technique (the one documented experimental credit,
the **Prismizer** for Harmony Engine, is in that flagship's guide). SoundSoap-as-texture and
Mic-Mod-as-lo-fi are extrapolated/labeled speculative.

**Sources:** `links/avox-nav-*.md` (autotune-tier-comparison, niche-avox-modules,
vocal-chain-utilities, mic-mod, autotune-slice) + `transcripts/avox-nav-autotune-versions-compared.md`,
plus the existing `links/antares-bundle-roster-and-reach-for.md`, `antares-avox-sos-review.md`,
`antares-vocodist-review.md`. URLs on line 1 of each file.
