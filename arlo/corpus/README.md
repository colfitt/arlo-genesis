# ARLO Corpus

Local-first knowledge base for the ARLO songwriting/production assistant.

This directory is the **source-document corpus** — raw PDFs and markdown captures of canonical references. ARLO's ingest pipeline parses these into citable chunks tagged by scope.

---

## Folder Taxonomy

```
corpus/
├── recording/         # tracking, mic placement, signal flow, room
├── mixing/            # EQ, compression, reverb, automation, translation
├── mastering/         # mastering chain, LUFS, delivery, QC
├── synthesis/         # subtractive, FM, wavetable, patch recipes
├── sampling/          # chopping, warping, resampling, electronic arrangement
├── rhythm/            # drum programming, groove, swing, bass
├── structure/         # song forms, arrangement, transitions
├── harmony/           # chord progressions, voice leading, modal interchange
├── melody/            # contour, motif, hook, topline
├── lyrics/            # craft, rhyme, prosody, POV, imagery
├── workflow/          # session methodology, finishing, preproduction
└── reference/         # platform specs (LUFS targets, ISRC, etc.)
```

---

## Currently In Corpus (Auto-Downloaded 2026-05-24)

| Path | Source | Format | Size | Status |
|------|--------|--------|------|--------|
| `recording/yamaha-sound-reinforcement-handbook.pdf` | Davis & Jones, Yamaha SR Handbook (2nd ed.) | PDF | 558 MB | ✅ Full text from Internet Archive |
| `mixing/izotope-mixing-guide.pdf` | iZotope, Mixing Guide: Principles, Tips, Techniques | PDF | 8.4 MB | ✅ Official, free |
| `mastering/izotope-ozone-help.pdf` | iZotope, Ozone 5 Help Documentation | PDF | 10 MB | ✅ Official; covers mastering concepts plugin-agnostically |
| `sampling/elektron-digitakt-ii-manual.pdf` | Elektron, Digitakt II User Manual | PDF | 7.6 MB | ✅ Official, free |
| `mixing/sos-inside-track-billie-eilish-bad-guy.md` | Sound on Sound, Inside Track | Markdown | — | ✅ Article scraped to markdown |
| `workflow/sos-inside-track-lewis-capaldi-someone-you-loved.md` | Sound on Sound, Inside Track | Markdown | — | ✅ Article scraped to markdown |
| `lyrics/sos-pattison-writing-better-lyrics-interview.md` | Sound on Sound, Pat Pattison interview | Markdown | — | ✅ Article scraped to markdown |
| `reference/spotify-loudness-normalization.md` | Spotify for Artists official docs | Markdown | — | ✅ Article + cross-platform LUFS table |
| `harmony/open-music-theory-v2-index.md` | Open Music Theory v2 (Pressbooks) | Markdown | — | ✅ ToC + ingestion-priority index pointer (full text TBD) |

**Total currently on disk:** ~584 MB across 9 documents.

---

## Could NOT Auto-Download (Manual Action Required)

### Welsh's Synthesizer Cookbook (HIGH PRIORITY)
- **URL:** http://www.synthesizer-cookbook.com/SynCookbook.pdf
- **Issue:** Site uses JavaScript-based redirect to `/lander` that `curl` cannot execute. The download is technically free but gated behind a browser-only handshake.
- **Workaround:** Visit https://synthesizer-cookbook.com in a real browser; click through to the PDF; save to `corpus/synthesis/welsh-synthesizer-cookbook.pdf`.

### Open Music Theory v2 — Full Text
- **URL:** https://viva.pressbooks.pub/openmusictheory/
- **Issue:** Pressbooks site, content rendered per-chapter. Auto-grabbing the full ~100 chapters needs a chapter-by-chapter scrape, not a single fetch.
- **Workaround:** See `harmony/open-music-theory-v2-index.md` for prioritized chapter list. Recommend scripting a fetch loop targeting the Unit VII (Popular Music) and Unit VI (Jazz) chapters first.

---

## Recommended Next Acquisitions (Paid / Borrow)

These need to be purchased or borrowed because they're not freely distributable.

### P1 (highest leverage — buy first)
| Title | Author | ISBN | Path target | Source |
|-------|--------|------|-------------|--------|
| Mixing Secrets for the Small Studio (3rd ed.) | Mike Senior | 978-1032840451 | `mixing/` | Routledge / Amazon |
| Recording Secrets for the Small Studio | Mike Senior | 978-0415716703 | `recording/` | Routledge / Amazon |
| Recording Engineer's Handbook (5th ed.) | Bobby Owsinski | 978-1946837110 | `recording/` | bobbyowsinski.com |
| Mastering Audio (3rd ed.) | Bob Katz | 978-0240818962 | `mastering/` | Available on Internet Archive borrow: https://archive.org/details/masteringaudioar0000katz |
| Hooktheory I + II | Carlton & Carlton | — | `harmony/` | hooktheory.com/books/buy (~$25) |
| Songwriting Secrets of the Beatles | Dominic Pedler | 978-0711981676 | `structure/` | Internet Archive borrow: https://archive.org/details/songwriting-secrets-of-the-beatles |

### P2 (second wave)
| Title | Author | ISBN | Path target | Source |
|-------|--------|------|-------------|--------|
| Great Songwriting Techniques | Jack Perricone | 978-0199967650 | `structure/` | Oxford UP |
| The Craft of Lyric Writing | Sheila Davis | 978-0898791495 | `lyrics/` | Used / abebooks |
| The Essential Guide to Rhyming | Pat Pattison | 978-1480342576 | `lyrics/` | Berklee Press |
| Zen and the Art of Producing | Mixerman | 978-1458402882 | `workflow/` | Hal Leonard |
| Secrets of Dance Music Production | Attack Magazine | — | `rhythm/` | store.attackmagazine.com |

### P3 (depth-fill)
| Title | Author | Path target | Source |
|-------|--------|-------------|--------|
| Beato Book 4.0 | Rick Beato | `harmony/` | rickbeato.com |
| Mixing Engineer's Handbook (4th ed.) | Bobby Owsinski | `mixing/` | Amazon |
| Tunesmith | Jimmy Webb | `lyrics/` | IA borrow: https://archive.org/details/tunesmith00jimm |
| Behind the Glass Vol 1 | Howard Massey | `recording/` | IA borrow: https://archive.org/details/behindglasstopre00mass |

---

## Internet Archive Borrow-Only Items

These are visible on archive.org but are *controlled-digital-lending* items — you can borrow them in a browser (1-hour or 14-day loan), but `curl` cannot grab the protected PDF. For ingestion, the workflow is:

1. Visit the archive.org URL in a browser
2. Click "Borrow for 14 days"
3. Use archive.org's built-in download for ACSM (then convert with Adobe Digital Editions or similar)

Affected titles in the P1/P3 lists above:
- Bob Katz, *Mastering Audio*
- Dominic Pedler, *Songwriting Secrets of the Beatles*
- Jimmy Webb, *Tunesmith*
- Howard Massey, *Behind the Glass*

Yamaha SRH was an *unrestricted* archive.org item (no DRM), which is why we got it directly.

---

## Ingestion Notes per Document

### `yamaha-sound-reinforcement-handbook.pdf` (558 MB)
- This is a high-resolution scan; OCR may be needed depending on your ingest pipeline.
- **For ARLO, only the following sections are valuable:**
  - Chapter 2: Signal Flow
  - Chapter 3: Decibels & Gain
  - Chapter 12: Cables & Connectors
  - Chapter 13: Grounding & Hum
- **Skip:** loudspeaker-array math, PA system design, room acoustics for large venues
- Tags: `signal-flow`, `gain-staging`, `cabling`, `monitoring`, `reference-fact`

### `izotope-mixing-guide.pdf` (8.4 MB)
- 60+ pages, modern (current edition); section-by-section is roughly chunk-shaped
- Pull from: subtractive EQ, dynamics, time effects, mix bus
- Skip: software-specific Neutron screenshots
- Tags: `mixing`, `EQ`, `compression`, `reverb`, `principle`

### `izotope-ozone-help.pdf` (10 MB)
- Ozone 5 era — older but the *concepts* are timeless (multiband, dither, limiting, stereo image)
- Pull from: limiter, multiband sections, dither chapter
- Skip: GUI screenshots, preset descriptions
- Tags: `mastering`, `limiting`, `multiband`, `dither`, `principle`

### `elektron-digitakt-ii-manual.pdf` (7.6 MB)
- Chunk *concepts* (p-locks, trig conditions, fill mode, song mode), not button paths
- Even non-Digitakt users benefit from these concepts as a general sequencing vocabulary
- Tags: `hardware-workflow`, `sampling`, `sequencer`, `performance`

### Sound on Sound articles (`*.md`)
- Already pre-chunked by section in the markdown
- High retrieval value because they're specific real-world examples
- Tags vary per file — see the front-matter of each

### `spotify-loudness-normalization.md`
- The cross-platform LUFS table at the bottom is the highest-retrieval chunk in the corpus
- Tag every chunk in this file with `reference-fact` so ARLO cites it authoritatively
- Tags: `mastering`, `LUFS`, `streaming`, `reference-fact`

---

## Acquisition Script

To re-run the auto-downloads (e.g., on another machine):

```bash
# From corpus/ root
curl -L -o mixing/izotope-mixing-guide.pdf \
  "https://downloads.izotope.com/guides/iZotope-Mixing-Guide-Principles-Tips-Techniques.pdf"

curl -L -o mastering/izotope-ozone-help.pdf \
  "https://help.izotope.com/docs/izotope-ozone5-help.pdf"

curl -L -o sampling/elektron-digitakt-ii-manual.pdf \
  "https://www.elektron.se/wp-content/uploads/2025/07/Digitakt-2-User-Manual_ENG_OS1.15A_250708.pdf"

curl -L -o recording/yamaha-sound-reinforcement-handbook.pdf \
  "https://archive.org/download/YamahaSoundReinforcementHandbookByGaryDavisRalphJones/Yamaha%20Sound%20Reinforcement%20Handbook%20by%20Gary%20Davis%20%26%20Ralph%20Jones.pdf"

# Welsh requires browser — see "Could NOT Auto-Download" section above.
```

---

## Provenance Note

All auto-downloaded items are either:
- Officially distributed free by the publisher (iZotope, Elektron)
- Hosted on Internet Archive as unrestricted public items (Yamaha SRH)
- Public web articles archived as markdown for offline use (Sound on Sound, Spotify)

Nothing in this corpus was obtained via DRM circumvention or pirate mirrors.
