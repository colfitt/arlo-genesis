# 03 — Seed Data (the asset)

You already have all of this. It is the moat. It is portable markdown + frontmatter, so it survives any engine/UI choice. Paths are absolute on the current machine — **make these configurable** in the real project (see [07-RISKS-OPEN-QUESTIONS.md](07-RISKS-OPEN-QUESTIONS.md)).

---

## 1. Gear — `/Users/cfitt/Dev/Pedalxly/Gear`

- **44 device folders** (pedals, synths, samplers, interfaces): Chase Bliss (Blooper, MOOD MkII, Generation Loss, …), Strymon (Big Sky, TimeLine, Iridium, Deco), Eventide H90, Hologram (Microcosm, Chroma Console), OBNE, EHX, JHS, Elektron (Digitakt/Octatrack), Boss, Roland VG-800, RME/Radial interfaces, etc.
- **"Constantly compiling gear deep research"** — the `research/` folders grow over time. A live engine should re-read, not cache forever.
- **Per-device layout:**
  ```
  <Device Name>/
    GearProfile.md      ← frontmatter + summary (41/44 present; 3 missing → fall back to folder name)
    manuals/            ← PDFs (46 total across the tree)
    presets/
    research/           ← deep-research markdown (the growing part)
  ```
- **`GearProfile.md` frontmatter schema:**
  ```yaml
  name: Blooper
  brand: Chase Bliss
  category: pedal
  subcategory: looper
  format: pedal
  power: 9V-center-neg-150mA
  midi: true
  expression: true
  io: mono-in/mono-out
  status: owned
  tags: []
  related: []
  ```
- **Counts:** 343 `.md`, 46 `.pdf`.

## 2. Software — `/Users/cfitt/Dev/Pedalxly/Software`

- **18 vendor folders:** Valhalla DSP, Soundtoys, iZotope, Arturia V Collection 11, Native Instruments (Komplete 15, Kontakt 8), Celemony Melodyne, Antares Auto-Tune, Cableguys, Devious Machines, Goodhertz, Neural DSP, Aberrant DSP, XLN, Spitfire, Ableton Live 12 Lite, Apple Logic Pro, Reverb Machine sample packs.
- **Parallel structure to Gear:** each vendor folder has `SoftwareProfile.md` (18) + `research/` + `presets/`; some `CONTENTS.md` (13). Plus a top-level **`_inventory.json`** (~150 KB) — a machine-readable inventory.
- **`SoftwareProfile.md` frontmatter schema:**
  ```yaml
  name: Kontakt 8
  brand: Native Instruments
  category: software
  subcategory: sampler
  formats: [vst3, au, standalone]
  host_in: [logic, ableton]
  installed: true
  install_path: /Library/Audio/Plug-Ins/Components/Kontakt 8.component
  version: latest
  status: owned
  tags: []
  related: []
  ```

## 3. ARLO knowledge — `/Users/cfitt/Dev/patchbay-ai/arlo`

The "how to make music" brain. **Not songs** — knowledge, taste, and workflows.

- **`corpus/`** — production/craft knowledge organized by topic: `recording, mixing, mastering, synthesis, sampling, rhythm, structure, harmony, melody, lyrics, workflow, reference, artists, albums, techniques, daw, songwriting`. (General-corpus stream complete; aesthetic + albums streams planned/ready.)
- **`chunks.jsonl`** — **5.6 MB** of chunked corpus content for retrieval/citation. This is the citation backbone. *Too large to dump into context — must be retrieved, not pasted.*
- **`arlo/taste-profile/spotify-taste-profile.md`** — your listening/taste profile.
- **`arlo/workflows/`** — **20+ songwriting/production methods**, one file each: eno-oblique-strategies, rubin-reduction-philosophy, bowie-burroughs-cut-up, dylan-notebook-cassette-discipline, joni-mitchell-alternate-tuning-first, nick-cave-letter-method, beat-first-topline, stems-first-production-first, lo-fi-prolific-volume, etc.
- **Research dispatchers** (how the corpus is *generated*): `PROMPTS.md` / `RESEARCH-PLAN.md` / `SESSIONS.md` triples for three streams (general ✅ done; **AESTHETIC** and **ALBUMS** "ready to fire"). `README.md` documents "how to dispatch a batch." → This is the **claude-seeding mechanism** (see [04](04-USING-IT-WITH-CLAUDE.md) / [06](06-BUILD-PLAN.md)).
- **`scripts/export_chunks.py`** — produces `chunks.jsonl` from the corpus.
- **Counts:** ~340 `.md`, `chunks.jsonl`, scripts.

---

## Reading rules for any engine

- **Profiles → structured records.** Parse YAML frontmatter; the body is the human description. Fall back to folder name when a profile is missing.
- **`research/` → grounding text.** Largest and most valuable for "expert" answers; re-scan because it grows.
- **`chunks.jsonl` → retrieval only.** Embed/index it; never inline the whole thing.
- **`workflows/` + `taste-profile/` → persona/voice.** These shape *how* ARLO answers, not just facts.
- **Keep canonical = markdown.** Any derived index (vector DB, JSON cache) is rebuildable from the markdown.
