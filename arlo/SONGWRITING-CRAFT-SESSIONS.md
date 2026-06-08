# ARLO Songwriting Craft — Batch Execution Plan

This file defines **8 numbered batches (S1–S8)** that together produce all 51 corpus files + 15 workflow templates (66 artifacts) for the Songwriting Craft & Workflows stream. Each batch is a single paste-able kickoff message you fire into a fresh Claude Code session — the agent reads `SONGWRITING-CRAFT-PROMPTS.md`, executes the listed prompts, and writes outputs to `corpus/songwriting/{bucket}/` and (for Bucket A) `arlo/workflows/`.

---

## How to run

### Serial (one session at a time)

1. Open a fresh Claude Code chat.
2. Copy the kickoff message for the batch.
3. Paste and send.
4. Wait for completion (~7–10 min per prompt; Bucket A is slower because it writes two files per prompt).
5. Confirm files landed in the right folders.
6. Move to the next batch.

### Parallel (multiple sessions at once)

1. Open N Claude Code tabs.
2. Paste a different batch kickoff into each.
3. Let them run concurrently.

**All 8 batches are independent.** Every batch reads `SONGWRITING-CRAFT-PROMPTS.md` and writes to a different set of files. There are no cross-batch dependencies.

### Practical parallelism limit

3–4 simultaneous batches is the comfortable sweet spot to stay under Anthropic web-search rate limits. The aggressive plan below pushes to all 8 simultaneously and is fine on Max 20× — be prepared to re-dispatch one or two that hit transient errors.

### Minimal-kickoff form

```
Run batch {BATCH_ID} for ARLO Songwriting Craft.
Read /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-SESSIONS.md, find the "Batch {BATCH_ID}" heading, follow the kickoff message verbatim. Begin.
```

---

## Batch Overview

| # | Batch | Prompts | Files written | Est. time |
|---|-------|---------|---------------|-----------|
| S1 | Workflow Recipes A (dual output) | A1–A8 | 8 in `corpus/songwriting/workflows/` + 8 in `arlo/workflows/` = **16 files** | ~75 min |
| S2 | Workflow Recipes B (dual output) | A9–A15 | 7 in `corpus/songwriting/workflows/` + 7 in `arlo/workflows/` = **14 files** | ~65 min |
| S3 | Stalling-Point Recovery | B1–B8 | 8 in `corpus/songwriting/stalls/` | ~60 min |
| S4 | Lyric Craft A | C1–C5 | 5 in `corpus/songwriting/lyric/` | ~40 min |
| S5 | Lyric Craft B | C6–C10 | 5 in `corpus/songwriting/lyric/` | ~40 min |
| S6 | Melodic & Harmonic Moves | D1–D8 | 8 in `corpus/songwriting/melodic-harmonic/` | ~60 min |
| S7 | Form Decisions | E1–E5 | 5 in `corpus/songwriting/form/` | ~40 min |
| S8 | Finishing Psychology | F1–F5 | 5 in `corpus/songwriting/finishing/` | ~40 min |

**Totals:** 8 batches, 51 prompts producing 66 files (51 corpus + 15 workflow templates), ~7 hours of total Claude compute. With 3–4 parallel sessions, wall-clock drops to ~2–3 hours. Fully parallel (all 8 at once), wall-clock is **~60–80 minutes** dominated by S1 (the largest Bucket-A batch with dual output per prompt).

---

## Pacing options

### Day-1 validation pacing (recommended)

Don't fire all 8 at once on day 1. Validate the prompt-and-output shape first.

**Session 1 — validation:** Fire batch **S1** (Workflow Recipes A — 8 prompts producing 16 files). Wait for completion. Spot-check 2 corpus files AND 2 workflow templates: confirm front-matter is correct, no AI-tutorial citations, the workflow templates have the required frontmatter (name/origin/type/applicable_when/duration_estimate), the corpus files are version-appropriate length and structure. ~75 minutes wall.

**If output passes spot-check:** proceed to the aggressive parallel path below.

**If output fails:** the stream-specific clauses in `SONGWRITING-CRAFT-PROMPTS.md` need tightening. Likely failure modes: (a) agent treated Bucket A as single-output instead of dual; (b) workflow template frontmatter missing or wrong; (c) named-school-of-thought discipline not honored (claims "the right way" instead of "Pattison teaches"); (d) cited AI-tutorial sites or generic listicles. Fix the addendum at the top of `SONGWRITING-CRAFT-PROMPTS.md`, then re-run S1.

### Aggressive parallel pacing

After S1 validates, fire S2 through S8 in parallel from a single dispatcher session (or 7 separate sessions).

**Wall time estimate:** ~50–60 minutes for the slowest batch (S2 — Bucket-A dual output for 7 prompts). Total stream complete in roughly **~2 hours** including the S1 validation. Expect 1–2 batches to hit a transient web-search rate-limit error; re-dispatch those.

### Conservative serial pacing

If you'd rather watch each batch land:

- **Hour 1:** S1 (validation)
- **Hour 2:** S2, S3 (parallel — different buckets)
- **Hour 3:** S4, S5, S6 (parallel — lyric + harmonic)
- **Hour 4:** S7, S8 (parallel — form + finishing)

Total wall-time: ~4 hours, with spot-check time between waves.

---

## Kickoff Messages

For each batch, copy the **entire** message in the code block below into a fresh Claude Code chat.

---

### Batch S1 — Workflow Recipes A (dual output)

```
Run research batch S1 for ARLO Songwriting Craft.

You are a research-and-write agent producing seed knowledge-base entries for ARLO, a local-first AI songwriting/production assistant whose mission is to help musicians FINISH SONGS. Output files will be ingested into ARLO's retrieval corpus.

Read /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-PROMPTS.md (stream addendum + Bucket-A dual-output spec + topic rows), /Users/cfitt/Dev/arlo/PROMPTS.md (base master template), and /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-RESEARCH-PLAN.md (sourcing philosophy + cross-stream boundaries).

This batch is BUCKET A, which is DUAL OUTPUT. For each prompt — A1, A2, A3, A4, A5, A6, A7, A8 — you write TWO files:
1. The corpus chunk at /Users/cfitt/Dev/arlo/corpus/songwriting/workflows/<slug>.md (1500–2500 words, standard ARLO chunk format)
2. The workflow template at /Users/cfitt/Dev/arlo/arlo/workflows/<slug>.md (target 600–1000 words, with the required frontmatter: name / origin / type / applicable_when / duration_estimate, and the required body sections: The premise / When ARLO should offer this / The steps / ARLO prompts for each step (verbatim) / When to abandon this workflow / Sources)

For each prompt in order:

1. Substitute the row's variables (Title, Slug, Origin, Type, Applicable_when, Duration estimate, Coverage points, Canonical references, Tags) into the standard ARLO master template, including the stream addendum's clauses (north-star check, source preference, honesty about subjectivity, cross-link existing corpus, default tags).
2. Execute deep research with WebSearch and WebFetch. Prefer named working practitioners with citable interviews/books per the source-tier in the plan.
3. Write the corpus chunk first, then derive the workflow template from it (the template should be operational, prescriptive, ready to execute — not a rewrite of the chunk).
4. Both files end with Sources. The corpus chunk also has "Cited Retrieval Topics" and "See also:" footers.

A1 = Nick Cave's letter method
A2 = David Lynch's catching the big fish
A3 = Eno's Oblique Strategies
A4 = Bowie's Burroughs cut-up
A5 = Rick Rubin's reduction philosophy
A6 = Tom Waits "break the demo"
A7 = Aimee Mann specificity-first
A8 = Beat-first / topline-over-beat

Mandatory rules:
- Mission-fit: every section must help a stuck musician finish a song. Cut anything that doesn't.
- Honesty about subjectivity: "Pattison teaches X" beats "the right way is X." When schools disagree, surface the disagreement.
- Anti-hallucination is absolute. If a quote, technique, or attribution can't be verified, OMIT it. Made-up attributions to working writers will poison ARLO's retrieval especially badly.
- Source preference: Pattison, Webb, Davis, Zollo, Rubin, Lynch, Eno's published primary sources, Sodajerker, Tape Notes, Switched On Pop, Strong Songs, Rick Beato (cited episode), Adam Neely (cited episode). REFUSE: AI-tutorial sites, generic listicles, genre-fan blogs.
- Cross-link existing general-corpus files via See-also footer. Look for `corpus/lyrics/`, `corpus/melody/`, `corpus/harmony/`, `corpus/structure/`, `corpus/workflow/`, and `corpus/daw/ableton/timeless/eight-bars-first-discipline.md` (for A10 in next batch but worth being aware of).
- Default tags include `songwriting-craft`, `finishing-songs`, `workflow-recipe`, plus practitioner tag and topic tags.

After all 8 prompts complete (16 files total), list both directories with `ls -lh` and report total word count.

Begin.
```

---

### Batch S2 — Workflow Recipes B (dual output)

```
Run research batch S2 for ARLO Songwriting Craft.

You are a research-and-write agent producing seed knowledge-base entries for ARLO. This is the second half of Bucket A — dual-output workflow recipes.

Read /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-PROMPTS.md (stream addendum + Bucket-A dual-output spec + topic rows), /Users/cfitt/Dev/arlo/PROMPTS.md (base master template), and /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-RESEARCH-PLAN.md.

DUAL OUTPUT. For each prompt — A9, A10, A11, A12, A13, A14, A15 — write TWO files:
1. Corpus chunk at /Users/cfitt/Dev/arlo/corpus/songwriting/workflows/<slug>.md (1500–2500 words)
2. Workflow template at /Users/cfitt/Dev/arlo/arlo/workflows/<slug>.md (600–1000 words, with required frontmatter)

A9 = Stems-first / production-first (bedroom-producer school)
A10 = Tom Cosm's 8-bar loop cycle
A11 = Spoon's two-demos-a-week
A12 = Joni Mitchell alternate-tuning-first
A13 = Bob Dylan notebook + cassette discipline
A14 = Sufjan research-then-write
A15 = Nashville co-writing protocol

For each prompt:
1. Substitute variables into the master template + stream addendum.
2. Deep research with WebSearch/WebFetch. Named-practitioner-first sourcing.
3. Write corpus chunk first, then derive operational template.
4. Standard ARLO footer on both (Sources; corpus chunk also gets Cited Retrieval Topics + See-also).

Specific stream guidance for this batch:
- **A10 (Tom Cosm 8-bar loop) MUST cross-link** to /Users/cfitt/Dev/arlo/corpus/daw/ableton/timeless/eight-bars-first-discipline.md. That file covers the Session-view mechanics; A10 covers the songwriting decision (when to break out of the loop into an arrangement). Make the cross-link explicit in both directions of framing.
- **A13 (Dylan notebook)** — the Bob Dylan Archive in Tulsa has documented Dylan's process; cite the archive's published materials and Cameron Crowe's *Rolling Stone* interview as primary sources.
- **A14 (Sufjan)** — the *Carrie & Lowell* and *Illinois* processes are well-documented in *Pitchfork*, *The Believer*, *Paste*; cite specific interviews.
- **A15 (Nashville co-writing)** — Holly Gleason archive, Jason Blume's *Six Steps*, NSAI materials are primary. The split-sheet protocol is contractual and worth being precise about.

Mandatory rules (same as S1):
- Mission-fit, anti-hallucination, source preference, school-naming honesty.
- Cross-link general-corpus files via See-also.
- Default tags: `songwriting-craft`, `finishing-songs`, `workflow-recipe`, plus practitioner tag.

After all 7 prompts complete (14 files), list both directories with `ls -lh` and report total word count.

Begin.
```

---

### Batch S3 — Stalling-Point Recovery

```
Run research batch S3 for ARLO Songwriting Craft.

You are a research-and-write agent producing seed knowledge-base entries for ARLO. This batch is BUCKET B — STALLING-POINT RECOVERY PLAYBOOKS that ARLO reaches for when it detects a stall signal.

Read /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-PROMPTS.md (stream addendum + Bucket-B frontmatter spec + topic rows), /Users/cfitt/Dev/arlo/PROMPTS.md (base master template), and /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-RESEARCH-PLAN.md.

For each prompt — B1, B2, B3, B4, B5, B6, B7, B8 — write the corpus file at /Users/cfitt/Dev/arlo/corpus/songwriting/stalls/<slug>.md with:

1. The Bucket-B frontmatter shape (problem / common_signals / recovery_moves) ADDITIONAL to the standard ARLO front-matter
2. Body sections: Why it stalls / The N recovery moves (each as an H3) / Socratic prompts ARLO uses verbatim / When to abandon and re-arrange / Sources / Cited Retrieval Topics / See also
3. The Socratic prompts section is operationally critical — these are the prompts ARLO will paste into conversation when it detects the stall. They should be ready-to-use, in question form, 5–10 per file. Examples of what good ones look like:
   - "What was this song about when you started? Read me the first verse out loud."
   - "If you weren't allowed to add anything to the bridge, what would you cut from the verse?"
   - "Who would notice if this song never came out — name three people."

B1 = the bridge problem
B2 = the second-verse problem
B3 = the chorus-isn't-lifting
B4 = the demo trap
B5 = the arrangement freeze
B6 = lyric-doesn't-mean-anything
B7 = "I hate this song now"
B8 = abandoning vs persisting

Each file is 1500–2500 words.

Stream guidance:
- The common_signals list in frontmatter should be REAL phrases — natural language a user would type when stuck. Not categorization; actual user speech.
- The recovery_moves count in frontmatter is the integer count of moves in the body. Honor it (if you say 6, write 6).
- Each move is concrete, actionable, named — not abstract advice.
- The "When to abandon and re-arrange" section is mission-critical: the user should know when to stop trying to fix this song and start the next one. Cross-link B8 from every other Bucket-B file.
- Cross-link existing general-corpus files (`corpus/structure/section-function-verse-prechorus-chorus-bridge.md` for B1 + B3; `corpus/lyrics/object-writing-and-sensory-imagery.md` for B6; `corpus/workflow/finishing-work-and-completion.md` for B4 + B8).

Mandatory rules:
- Mission-fit: this bucket IS the mission. Every move should help unstuck → finish.
- Anti-hallucination, named-school honesty.
- Source preference per the plan.
- Default tags: `songwriting-craft`, `finishing-songs`, `stall-recovery`, plus stall-specific tag.

After all 8 files complete, list with `ls -lh` and report total word count.

Begin.
```

---

### Batch S4 — Lyric Craft A

```
Run research batch S4 for ARLO Songwriting Craft.

You are a research-and-write agent producing seed knowledge-base entries for ARLO. This batch is BUCKET C — LYRIC CRAFT, part A.

Read /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-PROMPTS.md (stream addendum + topic rows), /Users/cfitt/Dev/arlo/PROMPTS.md (base master template), and /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-RESEARCH-PLAN.md.

For each prompt — C1, C2, C3, C4, C5 — write the corpus file at /Users/cfitt/Dev/arlo/corpus/songwriting/lyric/<slug>.md using the standard ARLO chunk shape (1500–2500 words, 8–15 H2 sections, Cited Retrieval Topics, Sources, See-also footer).

C1 = show don't tell, concrete-noun discipline (Mann / Williams / Prine school)
C2 = specificity vs abstraction — when each lands
C3 = revision discipline — the Dylan arc
C4 = internal rhyme, slant rhyme, multi-syllabic schemes
C5 = meter, prosody, syllable stress against the bar line

Stream guidance:
- These files go DEEPER than the general-corpus `corpus/lyrics/` files (object-writing, rhyme-types, prosody). General corpus established vocabulary; this bucket establishes the moves at the workbench. Cross-link the corresponding general-corpus file in each See-also footer.
- C1, C2 build on `corpus/lyrics/object-writing-and-sensory-imagery.md`
- C3 cross-links A13 (Dylan notebook workflow) — the discipline of revision IS the Dylan method applied
- C4 builds on `corpus/lyrics/rhyme-types-and-cadence-function.md`
- C5 builds on `corpus/lyrics/prosody-and-form-content-alignment.md`
- Pattison is the primary source across this bucket. *Writing Better Lyrics*, *The Essential Guide to Rhyming*, *Lyric Form and Structure*. Cite chapter, not just the book.
- Aimee Mann, Lucinda Williams, John Prine for C1's school identification.
- Hip-hop rhyme tradition (Edwards' *How to Rap*) for C4's multi-syllabic section.

Mandatory rules:
- Honesty about subjectivity: name the school. "Pattison teaches concrete-noun-first as the cure for vague lyrics" beats "good lyrics use concrete nouns."
- Anti-hallucination: don't invent Pattison quotes; cite the specific book/chapter.
- Source preference per plan.
- Default tags: `songwriting-craft`, `finishing-songs`, `lyric-craft`, plus topic tag and practitioner tag where named.

After all 5 files complete, list with `ls -lh` and report total word count.

Begin.
```

---

### Batch S5 — Lyric Craft B

```
Run research batch S5 for ARLO Songwriting Craft.

You are a research-and-write agent producing seed knowledge-base entries for ARLO. This batch is BUCKET C — LYRIC CRAFT, part B.

Read /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-PROMPTS.md, /Users/cfitt/Dev/arlo/PROMPTS.md, and /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-RESEARCH-PLAN.md.

For each prompt — C6, C7, C8, C9, C10 — write the corpus file at /Users/cfitt/Dev/arlo/corpus/songwriting/lyric/<slug>.md (standard ARLO chunk shape, 1500–2500 words).

C6 = image-stacking technique (Sufjan / Andrew Bird / Joanna Newsom school)
C7 = narrative voice — POV decisions (first / second / third / direct address)
C8 = theme consistency checks
C9 = refrain construction — earning the title
C10 = co-writing lyric dynamics (the room)

Stream guidance:
- C6: Sufjan interviews in *The Believer* and *Pitchfork*; Andrew Bird in *Bandcamp Daily*; Joanna Newsom interview archive. Build on `corpus/lyrics/object-writing-and-sensory-imagery.md`.
- C7: build on `corpus/lyrics/point-of-view-tense-and-narrator.md`. Randy Newman and Father John Misty as the unreliable-narrator / character-songwriting examples.
- C8: Pattison's theme-consistency framework; Jimmy Webb's *Tunesmith* on the title-as-theme test.
- C9: Webb's *Tunesmith* (title chapters); Pattison; Switched On Pop episodes on title craft.
- C10: cross-link A15 (Nashville co-writing protocol). Holly Gleason and Jason Blume as primary. This is the lyric-specific complement to A15's session-mechanics framing.

Mandatory rules:
- Honesty about subjectivity, schools-of-thought naming, anti-hallucination, source preference.
- Default tags: `songwriting-craft`, `finishing-songs`, `lyric-craft`, plus topic tag.
- Cross-link general-corpus files in See-also footer.

After all 5 files complete, list with `ls -lh` and report total word count.

Begin.
```

---

### Batch S6 — Melodic & Harmonic Moves

```
Run research batch S6 for ARLO Songwriting Craft.

You are a research-and-write agent producing seed knowledge-base entries for ARLO. This batch is BUCKET D — MELODIC & HARMONIC MOVES.

Read /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-PROMPTS.md, /Users/cfitt/Dev/arlo/PROMPTS.md, and /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-RESEARCH-PLAN.md.

For each prompt — D1, D2, D3, D4, D5, D6, D7, D8 — write the corpus file at /Users/cfitt/Dev/arlo/corpus/songwriting/melodic-harmonic/<slug>.md (standard ARLO chunk shape, 1500–2500 words).

D1 = modal interchange by mood (the move-to-mood map)
D2 = modulation moves between sections
D3 = hook construction patterns
D4 = vocal-range management for the singer's actual range
D5 = melodic contour shapes (arch / descent / plateau / ascent)
D6 = pedal tones and drones as anchoring devices
D7 = voice leading basics for chord-writers (not composition students)
D8 = chord substitutions for mood-shift (jazz-derived moves in pop)

Stream guidance:
- These files go DEEPER than the general-corpus `corpus/melody/` and `corpus/harmony/` files. General corpus established function and contour; this bucket establishes the MOVES a writer reaches for when a section needs a specific feeling. Cross-link the corresponding general-corpus file in each See-also footer.
- D1 builds on `corpus/harmony/modal-interchange-and-borrowed-chords.md`
- D3 builds on `corpus/melody/hook-construction.md`
- D5 builds on `corpus/melody/melodic-contour-and-motif-development.md`
- D7 builds on `corpus/harmony/voice-leading-for-songwriters.md`
- D8 builds on `corpus/harmony/modal-interchange-and-borrowed-chords.md` and `corpus/harmony/secondary-dominants-and-applied-chords.md`
- Primary sources: Dominic Pedler's *Songwriting Secrets of the Beatles*; Rick Beato's *The Beato Book* and *What Makes This Song Great* episodes; Switched On Pop; Open Music Theory v2; Jack Perricone's *Great Songwriting Techniques* and *Melody in Songwriting*; Jimmy Webb's *Tunesmith* (D4 range chapters).
- The MOVE-TO-MOOD framing is the differentiator: every section should give the user a concrete move plus the emotional effect to expect, not just theory exposition.
- For D4 (vocal range) — Jimmy Webb's range chapters; voice-teacher resources (Jeannie Deva, Seth Riggs).

Mandatory rules:
- Mission-fit: a stuck songwriter should leave each file with a specific move they can try in the next 30 minutes.
- Anti-hallucination, school-naming honesty, source preference.
- Default tags: `songwriting-craft`, `finishing-songs`, `melodic-harmonic`, plus topic tag.

After all 8 files complete, list with `ls -lh` and report total word count.

Begin.
```

---

### Batch S7 — Form Decisions

```
Run research batch S7 for ARLO Songwriting Craft.

You are a research-and-write agent producing seed knowledge-base entries for ARLO. This batch is BUCKET E — FORM DECISIONS.

Read /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-PROMPTS.md, /Users/cfitt/Dev/arlo/PROMPTS.md, and /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-RESEARCH-PLAN.md.

For each prompt — E1, E2, E3, E4, E5 — write the corpus file at /Users/cfitt/Dev/arlo/corpus/songwriting/form/<slug>.md (standard ARLO chunk shape, 1500–2500 words).

E1 = AABA vs verse-chorus — the decision framework
E2 = section lengths by genre and era
E3 = modern forms (post-chorus, drop, beat-switch, bridge-as-outro)
E4 = intro and outro discipline
E5 = through-composed song construction (Joanna Newsom, Big Thief, Bowie)

Stream guidance:
- These files go DEEPER than the general-corpus `corpus/structure/` files. General established what each section DOES; this bucket establishes the DECISION FRAMEWORKS for choosing a form. Cross-link `corpus/structure/pop-song-forms.md`, `section-function-verse-prechorus-chorus-bridge.md`, `arrangement-arcs-and-transitions.md` in See-also.
- E1: Pattison's *Lyric Form and Structure*; Perricone; Allan Moore's *Song Means*.
- E2: John Seabrook's *The Song Machine* on the song-machine era; Switched On Pop episodes on streaming-era song shortening; *Billboard* analyses of song-length trends.
- E3: Switched On Pop is the gold-standard source for post-chorus / drop / beat-switch analysis. Seabrook. Specific examples — Eilish post-chorus, Travis Scott beat-switch, EDM drop architecture.
- E4: streaming-era 7-second skip threshold is well-documented; *Music Business Worldwide* and *Billboard* coverage of skip-rate research.
- E5: Allan Moore's *Song Means*; Switched On Pop on Joanna Newsom; Sodajerker on Big Thief. Bowie's *Station to Station* title track as canonical example.

Mandatory rules:
- Each file should give the writer a decision framework — when is THIS form the right choice? — not just a description of the form.
- Era-bound and genre-bound claims must be named as such.
- Anti-hallucination, source preference per plan.
- Default tags: `songwriting-craft`, `finishing-songs`, `form-decision`, plus topic tag.

After all 5 files complete, list with `ls -lh` and report total word count.

Begin.
```

---

### Batch S8 — Finishing Psychology

```
Run research batch S8 for ARLO Songwriting Craft.

You are a research-and-write agent producing seed knowledge-base entries for ARLO. This batch is BUCKET F — FINISHING PSYCHOLOGY. The mission-direct bucket about the HUMAN obstacles to finishing.

Read /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-PROMPTS.md, /Users/cfitt/Dev/arlo/PROMPTS.md, and /Users/cfitt/Dev/arlo/SONGWRITING-CRAFT-RESEARCH-PLAN.md.

For each prompt — F1, F2, F3, F4, F5 — write the corpus file at /Users/cfitt/Dev/arlo/corpus/songwriting/finishing/<slug>.md (standard ARLO chunk shape, 1500–2500 words).

F1 = why songs don't get finished (a diagnostic)
F2 = "done > perfect" frameworks for songwriting
F3 = the finish-ugly school (commit the demo as the master)
F4 = the 80/20 finishing rule applied to mix and master
F5 = when to abandon and start over

Stream guidance:
- This is the mission-direct bucket. Files should be highly retrievable for the stuck-musician state ARLO most needs to handle.
- F1: Pressfield's *The War of Art* (Resistance framework); Cal Newport's *Deep Work*; Csikszentmihalyi's *Flow*; Ira Glass's "taste gap" talk; Dennis DeSantis's *Making Music* (the finishing chapters). Build a diagnostic tree — which category is the user in? what's the move per category?
- F2: trace "done > perfect" through its actual lineage (often misattributed to Voltaire; popularized by Sandberg in tech); Ira Glass; DeSantis; the operational versions.
- F3: Daniel Johnston, Guided By Voices, Springsteen's *Nebraska*, Johnny Cash *American Recordings*, mk.gee aesthetic. The case + the trap. Genre-boundedness.
- F4: Pareto applied to songwriting polish. The "outside ear" threshold rule. Cross-link general-corpus mixing files (which own the mixing principles).
- F5: cross-link B8 (abandoning vs persisting stall file) — F5 is the framework; B8 is the playbook ARLO reaches for. The graveyard-folder practice. The partial-rescue option.

Mandatory rules:
- Mission-direct: every section should help a stuck musician make peace with shipping.
- Honesty about subjectivity: name the school. The "finish ugly" school and the "polish-until-shipping" school disagree; surface that.
- Anti-hallucination: don't invent Ira Glass quotes or Pressfield aphorisms; cite the specific talk or book.
- Source preference per plan.
- Cross-link to `corpus/workflow/finishing-work-and-completion.md`.
- Default tags: `songwriting-craft`, `finishing-songs`, `finishing-psychology`, plus topic tag.

After all 5 files complete, list with `ls -lh` and report total word count.

Begin.
```

---

## Post-batch verification

After each batch completes, run this quick check from a terminal:

```bash
# Confirm corpus files landed in the right place
find ~/Dev/arlo/corpus/songwriting -name "*.md" -newer ~/Dev/arlo/SONGWRITING-CRAFT-PROMPTS.md -type f | sort

# Bucket A only — confirm workflow templates landed
find ~/Dev/arlo/arlo/workflows -name "*.md" -newer ~/Dev/arlo/SONGWRITING-CRAFT-PROMPTS.md -type f | sort

# Sanity-check sizes (corpus chunks 5–12 KB; workflow templates 2–4 KB)
find ~/Dev/arlo/corpus/songwriting ~/Dev/arlo/arlo/workflows -name "*.md" -newer ~/Dev/arlo/SONGWRITING-CRAFT-PROMPTS.md -type f -exec ls -lh {} \;

# Confirm Bucket-A workflow templates have the required frontmatter
for f in ~/Dev/arlo/arlo/workflows/*.md; do
  echo "--- $f ---"
  head -10 "$f"
  echo ""
done

# Confirm Bucket-B stall files have the required frontmatter
for f in ~/Dev/arlo/corpus/songwriting/stalls/*.md; do
  echo "--- $f ---"
  awk '/^---$/{count++; if (count==2) exit} {print}' "$f"
  echo ""
done

# Verify no AI-tutorial sites cited
grep -rEi "chatgpt|claude\.ai|bard\.google|copilot\.microsoft|perplexity\.ai/articles" ~/Dev/arlo/corpus/songwriting/ ~/Dev/arlo/arlo/workflows/ 2>/dev/null && echo "FAIL — AI-tutorial sites cited" || echo "OK — no AI-tutorial citations"

# Verify See-also footers present on corpus files
grep -rLE "See also|## See also" ~/Dev/arlo/corpus/songwriting/ 2>/dev/null && echo "missing See-also" || echo "all corpus files have See-also"
```

---

## Tracking what's done

Append to this checklist as batches complete.

- [x] Batch S1 — Workflow Recipes A *(A1–A8: 8 corpus chunks + 8 workflow templates = 16 files)*
- [x] Batch S2 — Workflow Recipes B *(A9–A15: 7 corpus chunks + 7 workflow templates = 14 files)*
- [x] Batch S3 — Stalling-Point Recovery *(B1–B8: 8 files)*
- [x] Batch S4 — Lyric Craft A *(C1–C5: 5 files)*
- [x] Batch S5 — Lyric Craft B *(C6–C10: 5 files)*
- [x] Batch S6 — Melodic & Harmonic Moves *(D1–D8: 8 files)*
- [x] Batch S7 — Form Decisions *(E1–E5: 5 files)*
- [x] Batch S8 — Finishing Psychology *(F1–F5: 5 files)*

When all 8 are checked, the corpus has **51 new songwriting-craft corpus files + 15 workflow templates** = **66 artifacts**.

---

## After all batches complete

Four follow-ups worth doing once the stream is complete:

1. **Workflow-template frontmatter validation.** The `arlo/workflows/*.md` templates have a strict frontmatter schema (name / origin / type / applicable_when / duration_estimate). ARLO will key off these fields to match workflows to user context. Run a frontmatter-parser pass and confirm every template parses cleanly.

2. **Stall-file common_signals harvest.** Each Bucket-B file has a `common_signals` array of actual user phrases. Collect these across all 8 stall files into a single `corpus/songwriting/stalls/SIGNAL-INDEX.md`. ARLO's stuck-detector will use this index to match incoming user utterances to the right playbook.

3. **Source-school cross-tabulation.** Many files cite the same practitioners (Pattison, Webb, Davis, Rubin, DeSantis). When you acquire the canonical books from the user's P3 list, replace the deep-research-synthesis chunks with direct-extract chunks. Update the `Source:` line accordingly.

4. **The `arlo/workflows/` README.** Write a short README at `arlo/workflows/README.md` documenting how ARLO opt-in works: the user sets `workflow: <slug>` in their song's ARLO.md frontmatter, ARLO loads the matching template, and the template's "ARLO prompts for each step (verbatim)" section becomes ARLO's conversational script. This README pairs with `corpus/daw/README.md` as the second new directory introduced by this round of streams.
