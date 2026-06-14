Sources (5 packs):
https://brucemenace.gumroad.com/l/drowned  (cross-ref — BASSMAYHEM same author)
https://www.elektronauts.com/t/bassmayhem-vol-1-for-digitakt-ii-probably-the-first-pack-ever-for-dtii/212724
https://yougottas.gumroad.com/l/DT2WORKSHOP
https://jamesorvis.com/product/substance-digitaktii/  (synthackers SUBSTANCE)
https://substan.gumroad.com/l/digisphere2  +  https://www.elektronauts.com/t/digisphere-ii-digitakt-ii-ambient-sound-pack-by-substan/222758
gumroad.com / jamesorvis.com / elektronauts.com · boorch, yougottas, synthackers, substan · 2024–2025

# Third-party Digitakt II PRESET packs (DT2-native .dt2pst, beyond Elektron's own store)

These are PRESET packs (the .dt2pst sound objects with the actual LFO/filter/FX p-locks
baked in), not just WAV sample packs — so loading them gives you finished patches to reverse-
engineer. Complements the existing Elektron-official + Isotonik/ELECTRONISOUNDS sample-pack
files. The first two are by **boorch (Bruce Menace)** — the DROWNED! drone-pack author.

## BASSMAYHEM Vol.1 — boorch (Bruce Menace) · $8.99 · 2024-04-28 · "probably the first DT2 pack ever"
- DT2-native **.dt2pst** presets + a demo project **BASSMAYHEM V1.dt2prj** + samples.
- Defining feature: **chromatic SAMPLE CHAINS** played on the **Grid machine with slice
  select** (the "32" suffix = a 32-note chromatic chain; "1S" = one-shot).
- **⚠️ Concrete gotcha: set the chromatic presets' root note to C1** (NOT the default) or
  they play at the wrong octave. Chain presets are large: **17 MB–25 MB each**.
- Stereo content in the upper register, **low end kept MONO "for your convenience"** (mono
  bass = no phase issues on a doom/sub layer — directly useful for the baritone sub voice).
- Uses **LFO for randomization**, plus envelope + filter shaping.
- Includes a **"RANDO" pattern built with the OS 1.15 "Create Random Locks"** slice feature
  (instant rearrangement of the chain — amen→jungle style).

## DROWNED! — boorch · Gumroad (already deep-captured separately) — cross-ref
- 50 drone presets (Clean + Headcrusher) + 50 stereo samples. Method = slow LFOs→Filter/Pitch,
  Random LFOs w/ slow Slew, Comb filter, resample-through-Headcrusher-rack. See
  `elektronauts-drowned-dt2-drone-preset-pack.md`. (Same author as BASSMAYHEM → consistent,
  on-aesthetic sound-design language.)

## Digitakt II WORKSHOP — yougottas · PAY-WHAT-YOU-WANT · Gumroad
- **68 presets, all built from the 16 INIT samples** — i.e. it shows how far DT2 synthesis/
  modulation takes a single raw sample (the most instructive teardown pack here).
- Breakdown: **16 Bass · 21 Drum one-shots & "loops" · 26 Synths/pads/leads/DRONES · 5 FX/
  textures.**
- "Most sounds use modulation extensively" and lean on **velocity modulation + keytracking**
  (DT2 expression features). Good source for drone + texture patches at zero cost.

## SUBSTANCE — synthackers (James Orvis) · jamesorvis.com · 2025
- **64 Bass & Synth presets** for DT2 (+ a live-jam demo). Walkthrough video:
  youtube.com/watch?v=uWlCHyDUcnI. Bass/synth-leaning (less drone than DROWNED/DigiSphere)
  but a clean source of playable, key-tracked synth voices for the banjo-lead register.

## DigiSphere II — substan · €15 · Gumroad/Patreon · 2024-10-30 · DT2-ONLY
- **121 "lively and atmospheric" ambient sounds**; a SOUND pack (presets), not a sample pack.
- **Ships a PROJECT FILE whose Bank-A patterns carry substan's preferred reverb + delay
  settings** — load it and the sends are already dialed for depth/size (the author warns the
  DEFAULT delay/reverb make the sounds "lack a lot of depth and size," so the project's
  pre-set sends are the point). Best ready-made FX-send reference pack for this rig.
- Built to put "as much of 'substan sound' as possible" into the DT2's bigger toolset (the
  OG DigiSphere had to "work around the limitations" — mono/RAM; DigiSphere II uses the full
  stereo + 3-LFO + comb engine).
- ⚠️ Known firmware-cosmetic bug: a few preset names get prefixed "X" (through OS 1.10A).
- OG DigiSphere (100 sounds) still loads on DT2 "without problems" but not guaranteed 1:1.

## Free patches note
- presetpatch.com/synth/elektron-digitakt hosts ~50 FREE single-sound files (`.dtsnd`,
  e.g. mz412ooo's H001_ARCTIC_PAD, maxime862a's "PULSAR" bass/kick series, junjunjun's
  H007_ARP2600_SQUARE "square wave with filter env") — but these are **OG Digitakt .dtsnd**,
  named only, with **no parameter values exposed in the listing**, so they're a download
  source rather than a documented-recipe source.

NOTE: counts/prices/dates per vendor pages + the Elektronauts release threads at capture.
The two boorch packs + DigiSphere II are the most on-aesthetic (drone/atmospheric);
WORKSHOP is the best free teardown; SUBSTANCE covers playable bass/lead. DigiSphere II's
project-embedded send settings are the closest thing to a published FX-send patch.
