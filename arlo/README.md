# ARLO Planning Directory

This directory contains the **planning artifacts** for ARLO's knowledge corpus. The actual ingestable content lives in `corpus/`. The files here describe what to research, how to organize it, and how to dispatch batched agents that produce the corpus content.

## File map

```
~/Dev/arlo/
├── README.md                       ← this file
├── PROMPTS.md                      ← Original 38-prompt general corpus
├── SESSIONS.md                     ← 12-batch dispatcher for PROMPTS.md
├── AESTHETIC-RESEARCH-PLAN.md      ← Strategic source map (24 artist anchors)
├── AESTHETIC-PROMPTS.md            ← 44-prompt aesthetic corpus (38 active + 6 deprecated)
├── AESTHETIC-SESSIONS.md           ← 12-batch dispatcher for AESTHETIC-PROMPTS.md
├── ALBUMS-RESEARCH-PLAN.md         ← 89-album expansion plan
├── ALBUMS-PROMPTS.md               ← 89 album-anchored prompt rows
├── ALBUMS-SESSIONS.md              ← 18-batch dispatcher for ALBUMS-PROMPTS.md
└── corpus/                         ← Output: where agents write seed documents
    ├── artists/                    ← Artist-anchored chunks
    ├── albums/                     ← Album-anchored chunks
    ├── techniques/                 ← Technique-anchored chunks
    ├── recording/                  ← General-corpus recording files
    ├── mixing/                     ← General-corpus mixing files
    ├── mastering/                  ← General-corpus mastering files
    ├── synthesis/                  ← General-corpus synthesis files
    ├── sampling/                   ← General-corpus sampling files
    ├── rhythm/                     ← General-corpus rhythm files
    ├── structure/                  ← General-corpus structure files
    ├── harmony/                    ← General-corpus harmony files
    ├── melody/                     ← General-corpus melody files
    ├── lyrics/                     ← General-corpus lyrics files
    ├── workflow/                   ← General-corpus workflow files
    └── reference/                  ← Cross-platform reference cards (LUFS targets, etc.)
```

## Three research streams

ARLO's corpus is built in three streams, each with its own PLAN / PROMPTS / SESSIONS triple:

### Stream 1 — General corpus (`PROMPTS.md` + `SESSIONS.md`)
- **Status:** ✅ Complete. All 12 batches fired, 38 files written (Nov 2026)
- **Scope:** Generic production technique — EQ, compression, mastering chain, song forms, harmony, etc.
- **Output:** `corpus/{recording,mixing,mastering,synthesis,sampling,rhythm,structure,harmony,melody,lyrics,workflow,reference}/`
- **Provenance tag:** "Deep-research synthesis (2026-05)"

### Stream 2 — Aesthetic corpus (`AESTHETIC-RESEARCH-PLAN.md` + `AESTHETIC-PROMPTS.md` + `AESTHETIC-SESSIONS.md`)
- **Status:** 📋 Plan complete, prompts complete, sessions complete. Ready to fire.
- **Scope:** 24 artist anchors + 8 technique anchors covering Bon Iver, LCD, Charli XCX, mk.gee, Bluegrass-prog trio, Talking Heads, Ry Cooder, Radiohead, Sufjan, Dijon, Big Thief, CSH, BCNR, Andrew Bird, Father John Misty, Cameron Winter/Geese, Vulfpeck, Animal Collective, Knopfler, Zevon, Prine, Bowie + Auto-Tune, vocal stacking, reamping, hyperpop, modal bluegrass, etc.
- **Batches:** 12 total (A1–A10 + T1 + T2)
- **Output:** `corpus/artists/` and `corpus/techniques/`
- **Deprecated overlaps:** 4 prompts (#19, #24, #33, #43) are deprecated because the albums corpus covers them at the album level.

### Stream 3 — Albums corpus (`ALBUMS-RESEARCH-PLAN.md` + `ALBUMS-PROMPTS.md` + `ALBUMS-SESSIONS.md`)
- **Status:** 📋 Plan complete, prompts complete, sessions complete. Ready to fire.
- **Scope:** 89 canonical albums, album-anchored production deep-dives.
- **Batches:** 18 total (AL1–AL18)
- **Output:** `corpus/albums/`
- **Includes:** Phase 1 starter pack of 10 high-value albums (Joy Division *Unknown Pleasures*, MBV *Loveless*, Talking Heads *Remain in Light*, Beatles *Abbey Road*, Bowie *Station to Station*, Miles *Bitches Brew*, Radiohead *Kid A*, Beasties *Paul's Boutique*, Björk *Vespertine*, Tom Waits *Rain Dogs*).

## How to dispatch a batch (the mechanic)

Each batch has a paste-able kickoff message in its respective SESSIONS file. To run one:

1. Open `AESTHETIC-SESSIONS.md` or `ALBUMS-SESSIONS.md`
2. Find the heading `### Batch {ID}` for the batch you want
3. Copy the contents inside the fenced ```` ``` ```` code block
4. Open a fresh Claude Code session
5. Paste. Send. Agent reads the corresponding PROMPTS file from disk, executes the listed prompts, writes files to the target paths.

Or use the minimal-kickoff form (3 lines, agent reads the full kickoff from the file):

```
Run batch {BATCH_ID} for ARLO. Read /Users/cfitt/Dev/arlo/{AESTHETIC|ALBUMS}-SESSIONS.md, find the "Batch {BATCH_ID}" heading, follow the kickoff message verbatim. Begin.
```

## Recommended pacing

### Day 1 — Validation (2 sessions in parallel)
- Session 1: `AL1` (5 album files, ~15 min wall)
- Session 2: `A1` (4 artist files, ~10 min wall)

After ~15 min, spot-check output, then commit to fanning out.

### Day 2 — Aesthetic-corpus baseline (5 sessions in parallel)
- `AL2`, `A2`, `A3`, `T1`, `T2` — completes aesthetic Phase 1 + Phase 1 albums
- 17 more files

### Day 3 — Aesthetic expansion + Albums hip-hop (7 sessions in parallel)
- `A4`, `A5`, `A6` + `AL3`, `AL4`, `AL5` (28 files)

### Day 4 — Aesthetic secondary-promotion + Albums art-rock+punk (8 sessions in parallel)
- `A7`, `A8`, `A9`, `A10` + `AL6`, `AL7`, `AL8`, `AL9` (28 files)

### Day 5 — Remaining albums (9 sessions in parallel)
- `AL10`–`AL18` (35 files)

At day 5 complete: ~130 production-deep-dive files in the corpus, ready for ARLO ingestion.

### Aggressive alternative

Fire all 30 batches (12 aesthetic + 18 album) in parallel from a single session that spawns 30 sub-agents. Max 20x has the rate-limit headroom. Wall time: ~30–60 min for the entire corpus build. Higher chance of one or two batches hitting transient errors; just re-dispatch those.

## Tracking

Each SESSIONS file has a tracking checklist at the end. Check off batches as they complete.

## After all batches complete — followup tasks

1. **Cross-link album files to artist files.** Files in `corpus/albums/` that have related artist files (Bon Iver, LCD, Bowie, Radiohead, Talking Heads, Postal Service, NMH, etc.) need a manual "See also" footer linking the two. Roughly 15 cross-links to make.

2. **Spot-check high-risk files.**
   - `corpus/artists/mk-gee-di-direct-philosophy.md` (thin documentation)
   - `corpus/albums/threebrain-weeeeee.md` (X-tier cult album, sparse sources)
   - `corpus/albums/clipse-let-god-sort-em-out.md` (recent 2025 release, less mature documentation)
   - Any pre-1975 album file with engineer attribution

3. **Acquire books, then re-process.** Three high-leverage acquisitions:
   - Brian Eno, *A Year With Swollen Appendices* — diary covering Talking Heads, Bowie, Coldplay sessions
   - Brian Coleman, *Check the Technique* Vol 1 + Vol 2 — track-by-track hip-hop production interviews
   - Howard Massey, *Behind the Glass* Vol 1 — already on P3 list; Eno chapter is high-leverage
   - When each arrives, re-process the relevant corpus files with direct-quote chunks replacing the synthesis paraphrases.

4. **Harvest `RETRIEVAL-INDEX.md`.** Every generated file ends with 5–10 "Cited Retrieval Topics" lines. Collect them all into a single `corpus/RETRIEVAL-INDEX.md` test set. Estimate: ~900 test queries across the full corpus. This becomes the validation harness when you stand up the ARLO ingest+retrieval pipeline.

## Provenance & honesty principles baked into the prompts

Every file generated by these prompts will include:
- **Source line** in front-matter: `Deep-research synthesis (2026-05) — verify before treating as authoritative`
- **Inline citations** as markdown links within sentences
- **Cited Retrieval Topics** footer (5–10 conversational query phrases)
- **Sources** bibliography of every URL linked above

The anti-hallucination guard is the master rule: "If you cannot verify a specific number, setting, technique, or attribution with web research, OMIT it. Do not guess." Agents are instructed to prefer qualitative claims over fabricated specifics. Files honest about their gaps are more useful than files that pad with speculation.

## Status of corpus content at time of writing

| Stream | Plan | Prompts | Sessions | Files written |
|--------|------|---------|----------|---------------|
| General | ✅ | ✅ (38) | ✅ (12) | ✅ 38 |
| Aesthetic | ✅ (24 anchors) | ✅ (44 rows, 38 active) | ✅ (12 batches) | ⏳ 0 — not yet fired |
| Albums | ✅ (89 albums) | ✅ (89 rows) | ✅ (18 batches) | ⏳ 0 — not yet fired |

Total potential corpus files at full ingest: **~165** (38 general + 38 aesthetic + 89 album). Estimated total chunks: **~3,000**.

The general stream is done. The aesthetic and albums streams are fully planned and ready for batch dispatch.
