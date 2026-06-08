# ARLO Songwriting Craft & Workflows — Research Plan

A craft-focused research pass that teaches ARLO **how working songwriters actually finish songs.** Every file in this stream is evaluable against one question: *does this help a stuck musician get unstuck and finish?* Academic theory for its own sake does not belong here; named, citable, working-practitioner craft does. The general corpus established the vocabulary (object writing, prosody, hook construction, song forms); this stream establishes the moves a writer reaches for at the workbench — the workflows, the stall-recovery playbooks, the lyric-craft disciplines, the harmonic/melodic moves, the form decisions, and the psychology of finishing.

The patchbay-ai north star is **finishing songs**. ARLO is built to be the assistant a working songwriter has open while writing, and the corpus this stream produces is what ARLO retrieves when the user is stuck. If a file doesn't move the needle on completion, it doesn't belong.

---

## Sourcing philosophy

Same tiering as the existing streams (S/A/B/C/NOT). The craft-specific extras: **prefer named working practitioners over anonymous tip aggregations**, and **be honest about subjectivity** — craft is more contested than DAW documentation, and files should name the school of thought rather than pretending a technique is universal.

| Tier | Source type | Why it's useful |
|---|---|---|
| **S** | Pat Pattison's Berklee lyric-writing lectures + books (*Writing Better Lyrics*, *Songwriting Without Boundaries*, *Lyric Form and Structure*, *The Essential Guide to Rhyming*) | The single most-cited working teacher in modern songwriting craft. Methodology is testable. |
| **S** | Jimmy Webb — *Tunesmith*; Sheila Davis — *The Craft of Lyric Writing*; Paul Zollo — *Songwriters on Songwriting* | Three canonical books. Zollo's interview format gives direct quotes from named writers. |
| **S** | Brian Eno — *A Year With Swollen Appendices* (on user's P3 acquisition list); Eno + Schmidt's *Oblique Strategies* card deck history | Primary source on Eno's process; foundational for the constraint-cards workflow. |
| **S** | David Lynch — *Catching the Big Fish*; Rick Rubin — *The Creative Act* | Both are working-artist primary sources on creative process. Lynch is canonical for ideational practice; Rubin for reduction philosophy. |
| **A** | Sodajerker on Songwriting (Simon Barber & Brian O'Connor interview podcast — 200+ working-songwriter episodes) | Long-form, transcribed/show-noted. The gold standard for working-songwriter interviews. |
| **A** | Tape Notes (John Kennedy interview podcast) | Production-and-craft hybrid; complements Sodajerker. |
| **A** | Switched On Pop (Charlie Harding & Nate Sloan) | Musicological analysis of contemporary pop with cited examples. Strong for Bucket D and E moves. |
| **A** | Strong Songs (Kirk Hamilton) | Per-song deep dives. Useful for surfacing the verifiable craft move inside a famous song. |
| **A** | Rick Beato — *What Makes This Song Great* series; Adam Neely (theory + craft hybrid) | YouTube but working-musician credentials; cite specific episode + timestamp. |
| **A** | Holly Gleason — *Woman Walk the Line*; Holly Gleason's interview archive | Strong on Nashville Music Row co-writing protocols and the practitioner-women perspective on craft. |
| **B** | Tape Op archives (production + writing process interviews) | Print-format interviews with named engineers/writers. Slow-decay quality. |
| **B** | Sound on Sound craft features and Inside Track series | Citable, edited, sometimes contains the actual craft move. |
| **B** | Working-musician blogs and Substacks with named-author credentials (Damian Keyes, Joel Beckerman, etc.) | Concrete moves; verify the credentials before citing. |
| **C** | Wikipedia entries on songwriters (orientation only) | Used to find the verifiable primary source, never cited directly. |
| **NOT** | Generic AI-generated "songwriting tips" sites | Filler. Often actively misattributes techniques. |
| **NOT** | Genre-fan blogs without verifiable authorial expertise | Untraceable claims. |
| **NOT** | YouTube content from non-working-musician creators | "Aspiring producer" channels — high noise, no signal. |
| **NOT** | Any "10 tips for writing better songs" listicle | Aggregation slop. |

The **master anti-hallucination rule** from the existing streams holds verbatim: *"If you cannot verify a specific number, setting, technique, or attribution with web research, OMIT it. Do not guess."*

### Craft-specific honesty rule

Craft is more subjective than DAW documentation. Files in this stream **must be honest about this:**

- When a technique is **one school of thought** (not universal), say so and name the school. "Pattison teaches X" beats "the right way to write a chorus is X."
- When working writers **disagree**, surface the disagreement. *"Pattison advocates object-writing as the seed of every lyric session; Aimee Mann describes starting with a single concrete image and excavating. Both work."*
- When a "rule" is **genre-bound**, name the genre. "8-bar choruses dominate contemporary radio pop" beats "choruses should be 8 bars."
- Prefer **"this is how [named practitioner] teaches it"** over **"this is how it works."**
- When a technique requires the user to **try it once to know if it fits**, say so. "This won't be obvious from reading; spend one session trying it before deciding it's not for you."

---

## The taxonomy — 6 buckets, 51 corpus files + 15 workflow templates

Each row produces one focused markdown file at the listed path. Word target per corpus file is 1500–2500 words (same chunk shape as existing streams). Bucket A additionally produces 15 workflow templates at `arlo/workflows/<slug>.md` — a NEW destination this stream introduces. Bucket B's stall files have a structured frontmatter shape so ARLO can detect-and-route from a stall signal to the right playbook.

All corpus files end with the standard Cited Retrieval Topics + Sources + See-also footer.

### A. Workflow Recipes (15 files, dual output) — `corpus/songwriting/workflows/` + `arlo/workflows/`

**Why this bucket is highest leverage:** workflow recipes are the most direct mission-fit. A stuck musician who switches workflow (rather than trying to push through the current one) often unsticks immediately. Each file documents a *named, attributable* writing method used by working professionals.

**Dual output explained:**

Each Bucket-A prompt produces TWO files:
1. **`corpus/songwriting/workflows/<slug>.md`** — a standard 1500–2500-word ARLO corpus chunk: front-matter, 8–15 H2 sections, Cited Retrieval Topics, Sources, See-also. The same shape as every other ARLO corpus file. This is what ARLO retrieves when the user asks about the technique.
2. **`arlo/workflows/<slug>.md`** — a structured workflow template ARLO offers when the user opts in via their song's `ARLO.md` frontmatter (`workflow: <slug>`). This is shorter and operational — fewer words, more prescriptive, designed to be *executed* not just read.

**Required shape for the workflow template** (the corpus chunk follows the standard ARLO front-matter):

```
---
name: <slug>
origin: <person or tradition>
type: lyrics-first | music-first | beat-first | production-first | exploring
applicable_when: "<one-line trigger condition>"
duration_estimate: "<rough wall-clock>"
---

# Workflow: <human-readable name>

## The premise
## When ARLO should offer this
## The steps
## ARLO prompts for each step (verbatim)
## When to abandon this workflow
## Sources
```

**Files:**

| # | Slug | Origin | Type |
|---|---|---|---|
| A1 | `nick-cave-letter-method` | Nick Cave | lyrics-first |
| A2 | `david-lynch-catching-big-fish` | David Lynch | exploring |
| A3 | `eno-oblique-strategies` | Brian Eno + Peter Schmidt | exploring |
| A4 | `bowie-burroughs-cut-up` | David Bowie (William Burroughs–derived) | lyrics-first |
| A5 | `rubin-reduction-philosophy` | Rick Rubin | exploring |
| A6 | `waits-break-the-demo` | Tom Waits | production-first |
| A7 | `aimee-mann-specificity-first` | Aimee Mann | lyrics-first |
| A8 | `beat-first-topline-workflow` | Hip-hop / pop-topline tradition (Max Martin school) | beat-first |
| A9 | `stems-first-production-first` | Modern bedroom-producer school | production-first |
| A10 | `tom-cosm-8-bar-loop-cycle` | Tom Cosm / Ill Gates | production-first |
| A11 | `spoon-two-demos-a-week` | Britt Daniel / Spoon | music-first |
| A12 | `joni-mitchell-alternate-tuning-first` | Joni Mitchell | music-first |
| A13 | `dylan-notebook-cassette-discipline` | Bob Dylan | lyrics-first |
| A14 | `sufjan-research-then-write` | Sufjan Stevens | exploring |
| A15 | `nashville-co-writing-protocol` | Nashville Music Row standard practice | varies (co-write) |

### B. Stalling-Point Recovery (8 files) — `corpus/songwriting/stalls/`

**Why this bucket is direct mission-fit:** stalls are where songs die. A file per stall, each ending with **verbatim Socratic prompts ARLO uses** when it detects the stall signal in conversation.

**Required frontmatter shape:**

```
---
problem: "<short name>"
common_signals: [bulleted list of phrases the user types when this stall is happening]
recovery_moves: <int count of moves the file contains>
---
```

Then the standard ARLO body:

```
# Stall: <name>

## Why it stalls
## Six (or N) recovery moves
## Socratic prompts ARLO uses verbatim
## When to abandon and re-arrange
## Sources
```

| # | Slug | Stall signal example |
|---|---|---|
| B1 | `the-bridge-problem` | "I don't know what to do for the bridge" / "the bridge isn't working" |
| B2 | `the-second-verse-problem` | "I have a verse and chorus but the second verse is the same as the first" |
| B3 | `the-chorus-isnt-lifting` | "my chorus doesn't feel like a chorus" / "the chorus is flat" |
| B4 | `the-demo-trap` | "I keep tweaking the mix and not writing" / "I can't move on from this demo" |
| B5 | `the-arrangement-freeze` | "I have too many ideas and can't pick" / "every section sounds different" |
| B6 | `lyric-doesnt-mean-anything` | "I don't know what this song is about anymore" |
| B7 | `i-hate-this-song-now` | "I used to like this song and now I hate it" |
| B8 | `abandoning-vs-persisting` | "should I keep going or scrap this" |

### C. Lyric Craft — Practical (10 files) — `corpus/songwriting/lyric/`

**Goes deeper than the general-corpus `corpus/lyrics/` files.** General corpus established vocabulary (object writing, rhyme types, POV, prosody); this bucket establishes the *moves at the workbench* a writer reaches for when revising a draft.

| # | Slug | Focus |
|---|---|---|
| C1 | `show-dont-tell-concrete-noun-discipline` | Aimee Mann / Lucinda Williams school; the noun-verb-noun test |
| C2 | `specificity-vs-abstraction-when-each-lands` | When concrete detail lands and when abstraction does (the Eilish / Swift cases) |
| C3 | `revision-discipline-the-dylan-arc` | Dylan's draft-and-redraft archive; revision as the craft (not the inspiration phase) |
| C4 | `internal-rhyme-slant-multi-syllabic` | Hip-hop rhyme schemes; multi-syllabic and chain rhyme patterns |
| C5 | `meter-prosody-syllable-stress` | Stress against the bar line; syllable counts; landing the strong word on the strong beat |
| C6 | `image-stacking-technique` | Sufjan / Andrew Bird / Joanna Newsom school of stacked sensory images |
| C7 | `narrative-voice-pov-decisions` | First / second / third / direct address; when each fits and the trap of switching |
| C8 | `theme-consistency-checks` | Declaring the song's theme and stress-testing every line against it |
| C9 | `refrain-construction-earning-the-title` | The line that earns the title; the title as the refrain; the title-elsewhere trick |
| C10 | `co-writing-lyric-dynamics` | The Nashville co-write room; veto vs build; how to hold the pen vs hand it off |

### D. Melodic & Harmonic Moves (8 files) — `corpus/songwriting/melodic-harmonic/`

**Goes deeper than the general-corpus `corpus/melody/` and `corpus/harmony/` files.** General corpus established function and contour; this bucket establishes the moves a writer reaches for when a section needs a specific feeling.

| # | Slug | Focus |
|---|---|---|
| D1 | `modal-interchange-by-mood` | What ♭III, ♭VI, ♭VII, minor iv each *feel* like; the move-to-mood map |
| D2 | `modulation-moves-between-sections` | Half-step up, fifth up, parallel key, deceptive — when each fits |
| D3 | `hook-construction-patterns` | Repetition with variation, the answer-phrase, post-chorus hooks |
| D4 | `vocal-range-management` | Writing for the singer's actual range; pre-chorus as range-launcher |
| D5 | `melodic-contour-shapes` | Arch / descent / plateau / ascent — section-by-section contour planning |
| D6 | `pedal-tones-drones-anchoring` | Pedal point as glue; drone as ground; modal-vs-tonal anchoring |
| D7 | `voice-leading-basics-for-chord-writers` | Common-tone connection, contrary motion, smooth bass — for songwriters not composition students |
| D8 | `chord-substitutions-for-mood-shift` | Jazz-derived subs in pop (tritone, ♭II°7, the IV-becomes-iv move) |

### E. Form Decisions (5 files) — `corpus/songwriting/form/`

**Goes deeper than the general-corpus `corpus/structure/` files.** General corpus established what each section does; this bucket establishes the *decision frameworks* for choosing a form.

| # | Slug | Focus |
|---|---|---|
| E1 | `aaba-vs-verse-chorus-decision` | When each form fits the material; Beatles AABA holdovers; verse-chorus default in radio pop |
| E2 | `section-lengths-by-genre-and-era` | 8-bar vs 12-bar vs 16-bar; how streaming shortened songs; intro length trends |
| E3 | `modern-forms-post-chorus-drop-beat-switch` | Post-chorus (the Eilish / Charli / Carpenter move); drop architecture; beat-switch (Travis Scott); bridge-as-outro |
| E4 | `intro-outro-discipline` | Cold open vs. instrumental intro; outro fade vs. cold cut vs. tag; streaming-era 7-second intro pressure |
| E5 | `through-composed-song-construction` | Joanna Newsom / Big Thief / Bowie *Station to Station* — when through-composing beats verse-chorus |

### F. Finishing Psychology (5 files) — `corpus/songwriting/finishing/`

**Direct mission-fit.** The psychology files are about the *human* obstacles to finishing. These are highest-retrieval-value when the user is stuck in a way no playbook fixes.

| # | Slug | Focus |
|---|---|---|
| F1 | `why-songs-dont-get-finished` | Creative-psychology research on completion (Oettingen on goal-pursuit; Cal Newport on shallow vs. deep; specific to creative work) |
| F2 | `done-better-than-perfect-frameworks` | Voltaire / Cain / Dennis DeSantis / Ira Glass — the canonical "done is better" voices and their concrete frameworks |
| F3 | `finish-ugly-school` | "Commit the demo as the master" — the Daniel Johnston / Guided By Voices / lo-fi school; when ugly IS the finish |
| F4 | `80-20-finishing-rule-mix-master` | The last-20%-of-polish-is-80%-of-time rule; how to know when to ship |
| F5 | `when-to-abandon-and-start-over` | Frameworks for the call; the "graveyard folder" practice; abandoning the song vs. abandoning the take |

---

## Cross-stream boundaries — what this stream does NOT own

| Topic | Owning stream | Resolution |
|---|---|---|
| Artist-specific deep dives (Bon Iver's vocal layering, LCD's live rig) | **Aesthetic stream** | When a workflow recipe names an artist (Cave, Lynch, Dylan, Joni, Sufjan), the *workflow* is in scope here; the artist's broader career and aesthetic is in the Aesthetic stream's anchor file. Cross-link. |
| Album production stories (*Loveless*, *Kid A*, *Bitches Brew*) | **Albums stream** | Songwriting Craft files never narrate an album's production history. |
| DAW workflows and production technique (Ableton Session view, freezing, warp modes) | **DAW: Ableton stream** | Tom Cosm's 8-bar loop appears in both (`A10` here, `I13` there). The Songwriting Craft file focuses on the *songwriting decision* (when to break out of the loop into a song); the DAW file focuses on the *session-view mechanics*. Cross-link. |
| General mixing / mastering / signal flow | **General stream** | F4 (80/20 finishing rule for mixing) cross-links the general-corpus mixing files; doesn't re-cover EQ or compression. |

### Cross-references to existing general-corpus files

This stream goes deeper than these general-corpus files; each should cross-link via See-also rather than re-research:

| Existing general-corpus file | Songwriting-Craft file that builds on it |
|---|---|
| `corpus/lyrics/object-writing-and-sensory-imagery.md` | C1 show-don't-tell; C6 image-stacking |
| `corpus/lyrics/rhyme-types-and-cadence-function.md` | C4 internal-rhyme / multi-syllabic |
| `corpus/lyrics/point-of-view-tense-and-narrator.md` | C7 narrative-voice POV |
| `corpus/lyrics/prosody-and-form-content-alignment.md` | C5 meter / prosody |
| `corpus/lyrics/sos-pattison-writing-better-lyrics-interview.md` | reference cited throughout C bucket |
| `corpus/melody/melodic-contour-and-motif-development.md` | D5 melodic-contour shapes |
| `corpus/melody/hook-construction.md` | D3 hook-construction patterns |
| `corpus/harmony/modal-interchange-and-borrowed-chords.md` | D1 modal interchange by mood |
| `corpus/harmony/voice-leading-for-songwriters.md` | D7 voice-leading basics for chord-writers |
| `corpus/harmony/pop-chord-progressions-by-function.md` | D8 chord substitutions for mood-shift |
| `corpus/harmony/secondary-dominants-and-applied-chords.md` | D8 mood-shift moves |
| `corpus/structure/pop-song-forms.md` | E1 AABA vs verse-chorus |
| `corpus/structure/section-function-verse-prechorus-chorus-bridge.md` | E2 section lengths; B1 the-bridge-problem; B3 chorus-isn't-lifting |
| `corpus/structure/arrangement-arcs-and-transitions.md` | E3 modern forms |
| `corpus/workflow/finishing-work-and-completion.md` | F2 done > perfect; F4 80/20; F5 when to abandon |
| `corpus/workflow/session-methodology.md` | most of A bucket |
| `corpus/workflow/preproduction-and-demo-handoff.md` | A6 break-the-demo; B4 demo-trap |
| `corpus/daw/ableton/timeless/eight-bars-first-discipline.md` | A10 Cosm 8-bar loop (mutual cross-link) |

### Cross-references to other ARLO streams

When a workflow recipe in Bucket A names an artist that has an Aesthetic-stream anchor, the See-also footer should link to it. Examples: A4 Bowie cut-up → `corpus/artists/bowie-*` (if/when written); A12 Joni → Joni anchor (TBD); A14 Sufjan → Sufjan anchor (TBD). Where the Aesthetic-stream anchor doesn't exist yet, omit the link cleanly.

---

## Target file count

| Bucket | Corpus files | Workflow templates | Notes |
|---|---|---|---|
| A. Workflow Recipes | 15 | 15 | Dual output — every prompt writes both |
| B. Stalling-Point Recovery | 8 | 0 | Stalls have structured frontmatter but stay as corpus files |
| C. Lyric Craft | 10 | 0 | |
| D. Melodic & Harmonic Moves | 8 | 0 | |
| E. Form Decisions | 5 | 0 | |
| F. Finishing Psychology | 5 | 0 | |
| **Total** | **51 corpus files** | **15 workflow templates** | **66 artifacts** |

At 1500–2500 words per corpus file and 8–15 retrieval chunks per file, the stream produces an estimated **~450–700 chunks** in `corpus/songwriting/`. The 15 workflow templates are short and operational (target ~600–1000 words each) and live in `arlo/workflows/` for direct opt-in use.

---

## Tagging conventions for the stream

Every corpus file in this stream gets at minimum these tags:

- `songwriting-craft` (the stream marker)
- `finishing-songs` (north-star marker — retrievable when user signals completion stress)
- Bucket tag: `workflow-recipe`, `stall-recovery`, `lyric-craft`, `melodic-harmonic`, `form-decision`, or `finishing-psychology`
- Topic-specific tags as appropriate (`co-writing`, `revision`, `modal-interchange`, `bridge`, etc.)
- Practitioner tags when the file is named-method (`cave`, `lynch`, `eno`, `bowie`, `rubin`, `waits`, `mann`, `dylan`, `joni`, `sufjan`, `cosm`, etc.)

Workflow templates in `arlo/workflows/` use the frontmatter spec above (`name`, `origin`, `type`, `applicable_when`, `duration_estimate`) — these become the directly-queryable fields ARLO uses to match the workflow to the user's context.

---

## Anti-hallucination notes — craft-specific

1. **Name the practitioner before attributing the technique.** "Pat Pattison teaches object writing" is verifiable. "Songwriters use object writing" is vague to the point of useless.
2. **Cite primary-source quotes when possible.** Zollo's *Songwriters on Songwriting* is the easiest path to verified primary quotes. Sodajerker transcripts are the modern equivalent.
3. **Schools of thought, not universal rules.** A claim like "every bridge should change the key" is suspect on its face. A claim like "Pattison teaches that a strong bridge contrasts harmonically, melodically, or lyrically — usually one of the three, not all three" is the kind of nuanced craft assertion this stream wants.
4. **Genre boundedness.** Nashville co-writing protocols don't apply to bedroom indie. Hip-hop multi-syllabic rhyme doesn't apply to folk. Name the genre or context.
5. **Dated techniques.** If a technique is associated with a specific era (Brill Building, Nashville circa 1995, post-streaming 2020+), name the era. The "8-bar verse" assumption is era-bound.
6. **When working writers disagree, name both sides.** Pattison's object-writing-first vs. Mann's image-first vs. Cave's letter-method — these are different schools. Don't flatten.
7. **Don't invent quotes.** If a working writer's quote can't be sourced to a specific interview/book/talk, omit it.

---

## What this stream does NOT cover

Out of scope, by user instruction and by mission-fit:

- **Artist career narratives** — the Aesthetic stream owns. Workflow recipes touch the artist's method, not their biography.
- **Album production stories** — the Albums stream owns.
- **DAW workflows** — the DAW: Ableton stream owns. Songwriting-Craft files name the workflow at the conceptual level; the DAW stream covers the keystrokes.
- **General mixing / mastering / signal flow** — the General stream owns. F4 cross-links rather than re-covers.
- **Music theory for its own sake** — the General-corpus harmony files cover the theory vocabulary. This stream applies theory to *songwriting decisions* (mood-shift moves, modulation-between-sections, voice-leading for songwriters) not to academic analysis.
- **Performance technique** — out of scope. Vocal technique, guitar playing, etc.
- **Music business** — out of scope. Publishing splits, sync placements, etc.

The Songwriting Craft stream is *the assistant a working songwriter has open while writing.* Anything that doesn't help the user finish a song is out of scope.
