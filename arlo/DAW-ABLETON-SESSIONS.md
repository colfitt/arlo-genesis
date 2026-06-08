# ARLO DAW: Ableton — Batch Execution Plan

This file defines **10 numbered batches (D1–D10)** that together produce all 62 corpus files for the DAW: Ableton stream. Each batch is a single paste-able kickoff message you fire into a fresh Claude Code session — the agent reads `DAW-ABLETON-PROMPTS.md`, executes the listed prompts, and writes the rendered files to `corpus/daw/ableton/{area}/`.

---

## How to run

### Serial (one session at a time)

1. Open a fresh Claude Code chat.
2. Copy the kickoff message for the batch.
3. Paste and send.
4. Wait for completion (rough estimate: 7–10 minutes per prompt; multiply by the batch's prompt count).
5. Confirm files landed in `corpus/daw/ableton/{area}/`.
6. Move to the next batch.

### Parallel (multiple sessions at once)

1. Open N Claude Code tabs.
2. Paste a different batch kickoff into each.
3. Let them run concurrently.

**All 10 batches are independent.** Every batch reads `DAW-ABLETON-PROMPTS.md` and writes to a different set of files. There are no cross-batch dependencies.

### Practical parallelism limit

3–4 simultaneous batches is the sweet spot to stay clear of Anthropic web-search rate limits. The aggressive plan below pushes to 10 simultaneously and is fine on Max 20× — be prepared to re-dispatch one or two that hit transient errors.

### Minimal-kickoff form

If you'd rather not paste the full kickoff body, use:

```
Run batch {BATCH_ID} for ARLO DAW: Ableton.
Read /Users/cfitt/Dev/arlo/DAW-ABLETON-SESSIONS.md, find the "Batch {BATCH_ID}" heading, follow the kickoff message verbatim. Begin.
```

---

## Batch Overview

| # | Batch | Prompts | Files written | Est. time |
|---|-------|---------|---------------|-----------|
| D1 | Fundamental Workflows | A1, A2, A3, A4, A5, A6, A7 | 7 files in `corpus/daw/ableton/workflows/` | ~50 min |
| D2 | Stock Devices: Mixing Tools | B1, B2, B3, B4, B5, B6 | 6 files in `corpus/daw/ableton/devices/` | ~45 min |
| D3 | Stock Devices: Color + Synths + Samplers | B7, B8, B9, B10, B11 | 5 files in `corpus/daw/ableton/devices/` | ~40 min |
| D4 | Live 12 Features | C1, C2, C3, C4, C5, C6, C7 | 7 files in `corpus/daw/ableton/live-12/` | ~55 min |
| D5 | Production Patterns | D1, D2, D3, D4, D5, D6, D7 | 7 files in `corpus/daw/ableton/patterns/` | ~55 min |
| D6 | Comping and Editing | E1, E2, E3, E4 | 4 files in `corpus/daw/ableton/editing/` | ~30 min |
| D7 | Frictions + Shortcuts + Logic Parity | F1, F2, F3, F4, F5, G1, H1 | 7 files in `corpus/daw/ableton/{friction,reference}/` | ~55 min |
| D8 | Timeless A: Resampling, Racks, Grooves | I1, I2, I3, I4, I5, I6, I7 | 7 files in `corpus/daw/ableton/timeless/` | ~55 min |
| D9 | Timeless B: Sidechain, Parallel, Performance | I8, I9, I10, I11, I12, I13 | 6 files in `corpus/daw/ableton/timeless/` | ~45 min |
| D10 | Timeless C: Sound Design, Library, Mixing | I14, I15, I16, I17, I18, I19 | 6 files in `corpus/daw/ableton/timeless/` | ~45 min |

**Totals:** 10 batches, 62 prompts, ~8 hours of total Claude compute time. With 3–4 parallel sessions, wall-clock time drops to ~2–3 hours. Fully parallel (all 10 at once), wall-clock is **~50–60 minutes** dominated by the longest batch.

---

## Pacing options

### Day-1 validation pacing

Don't fire all 10 at once on day 1. Validate the prompt-and-output shape first.

**Session 1 — validation:** Fire batch **D1** (Fundamental Workflows, 7 files). Wait for completion. Spot-check 2 files against the Live 12 Reference Manual: confirm front-matter is correct, no Live-11 features mis-claimed as Live 12, citations are real URLs. ~50 minutes wall.

**If output passes spot-check:** proceed to the aggressive parallel path below.

**If output fails:** the prompt-row text in `DAW-ABLETON-PROMPTS.md` needs tightening. Likely failure modes are (a) agent didn't version-stamp claims, (b) cited Reddit/forums as primary sources, (c) retrofitted Live-12 features into pre-Live-12 contexts. Fix the master-template addendum at the top of `DAW-ABLETON-PROMPTS.md`, then re-run D1.

### Aggressive parallel pacing

After D1 validates, fire D2 through D10 in parallel from a single dispatcher session (or 9 separate sessions).

**Wall time estimate:** ~50–60 minutes for the slowest batch (D4 or D5). Total stream complete in roughly **70–90 minutes** including the D1 validation. Expect 1–2 batches to hit a transient web-search rate-limit error; re-dispatch those.

### Conservative serial pacing

If you'd rather watch each batch land:

- **Hour 1:** D1
- **Hour 2:** D2, D3 (in parallel — small batch sizes)
- **Hour 3:** D4, D6 (in parallel)
- **Hour 4:** D5, D7 (in parallel)
- **Hour 5:** D8, D9, D10 (in parallel — all timeless, no dependencies)

Total wall-time: ~5 hours, with verification time built in between each.

---

## Kickoff Messages

For each batch, copy the **entire** message in the code block below into a fresh Claude Code chat.

The opening line of every kickoff reminds the agent of the stream-specific rules from `DAW-ABLETON-RESEARCH-PLAN.md` — version-stamping, anti-hallucination for Live-12-only features, source preference for Ableton's official manual.

---

### Batch D1 — Fundamental Workflows

```
Run research batch D1 for ARLO DAW: Ableton.

Read /Users/cfitt/Dev/arlo/DAW-ABLETON-PROMPTS.md to load the stream-specific master-template addendum and the topic variable rows. Also read /Users/cfitt/Dev/arlo/PROMPTS.md for the base master template (the addendum supplements it, doesn't replace it).

For each of these prompts in order — A1, A2, A3, A4, A5, A6, A7 — do the following:

1. Find the topic row in DAW-ABLETON-PROMPTS.md and substitute its variables (Title, Scope, Folder, Filename, Subtopics, Live version, Canonical references, Tags) into the master template, including the stream addendum's extra Content-Requirements clauses (Live version targeting, source preference, cross-link existing corpus, default tags).
2. Execute deep research using web search. Follow the content requirements: concrete over abstract, inline citations, anti-hallucination guard, version-stamp every device/feature claim, prefer the Ableton Live 12 Reference Manual as primary source.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/daw/ableton/workflows/{filename}.md following the exact output format — front-matter block, 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography, plus a See-also footer if a related general-corpus file exists.
4. Move to the next prompt.

After all 7 files are written, list them with sizes and give a one-sentence summary of each.

Stream reminders:
- Target Live version is 12.x (as of 2026-05). Name the Live version inline for every device/feature claim ("Hybrid Reverb (Live 11+)", "the Envelope Follower modulator (Live 12+)").
- If a tutorial source predates Live 12 and you cannot verify the technique still works as described, OMIT it. Do not retrofit older content into Live-12 wording.
- Prefer Ableton's official Live 12 Reference Manual, Release Notes, and Learn Live videos as primary citations. Refuse to cite AI-generated tutorial sites. Use forums only to triangulate — never as the cited source.
- Cross-link existing general-corpus files via a See-also footer when the DAW-agnostic concept already has a file (search corpus/ before writing).
- Every file gets at minimum tags `daw-ableton`, `live-12`, plus the area tag.
```

---

### Batch D2 — Stock Devices: Mixing Tools

```
Run research batch D2 for ARLO DAW: Ableton.

Read /Users/cfitt/Dev/arlo/DAW-ABLETON-PROMPTS.md (stream addendum) and /Users/cfitt/Dev/arlo/PROMPTS.md (base master template).

For each of these prompts in order — B1, B2, B3, B4, B5, B6 — do the following:

1. Substitute the row's variables into the master template, including the stream-specific Content-Requirements clauses.
2. Execute deep research with web search. Prefer the Live 12 Reference Manual entries for each device. Cite version-stamped tutorials only when they verifiably reflect Live 12 behavior.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/daw/ableton/devices/{filename}.md with the standard structure (front-matter, 8–15 H2 sections, Cited Retrieval Topics, Sources, See-also footer if applicable).
4. Move to the next prompt.

After all 6 files are written, list them with sizes and give a one-sentence summary of each.

Stream reminders:
- For devices that were renamed or unified across Live versions (the unified Delay device in Live 11+; Hybrid Reverb in Live 11+; Roar, Drift, Meld, Granulator III, Auto Shift, EQ Controls in Live 12+) — name the version they shipped in. Do not present Live-12-only devices as if they exist in older versions.
- For the Compressor/Glue/Multiband/Drum Buss file (B2), the Live 12 Reference Manual entries on each are the primary source. Do not invent parameter ranges; check the manual.
- Default tags include `daw-ableton`, `live-12`, `device`, plus the device-specific tag.
```

---

### Batch D3 — Stock Devices: Color, Synths, Samplers

```
Run research batch D3 for ARLO DAW: Ableton.

Read /Users/cfitt/Dev/arlo/DAW-ABLETON-PROMPTS.md (stream addendum) and /Users/cfitt/Dev/arlo/PROMPTS.md (base master template).

For each of these prompts in order — B7, B8, B9, B10, B11 — do the following:

1. Substitute the row's variables into the master template with the stream addendum.
2. Execute deep research with web search. Live 12 Reference Manual is primary. Sound on Sound *Synth Secrets* (Gordon Reid) is the gold-standard secondary source for synthesis-fundamentals claims.
3. Write to /Users/cfitt/Dev/arlo/corpus/daw/ableton/devices/{filename}.md with the standard output structure.
4. Move to the next prompt.

After all 5 files are written, list them with sizes and give a one-sentence summary of each.

Stream reminders:
- B10 (Wavetable/Drift/Meld) — Drift and Meld are Live 12+. Wavetable arrived in Live 10. Do not conflate.
- B11 (Sampler/Simpler/Drum Rack/Granulator III) — Granulator III shipped with Live 12. The older Granulator (Robert Henke Max device) was different — don't conflate them.
- B9 (Operator/Analog) — Operator's 11 algorithms and Analog's structure are stable across many Live versions; cite the Live 12 manual for the current parameter set.
- For each synth, include a brief patch-design starting point (bass / lead / pad / pluck) but defer deeper sound-design technique to the Timeless I16 (Operator FM) and D7 (Sound Design with Stock Synths) files.
```

---

### Batch D4 — Live 12 Features

```
Run research batch D4 for ARLO DAW: Ableton.

Read /Users/cfitt/Dev/arlo/DAW-ABLETON-PROMPTS.md (stream addendum) and /Users/cfitt/Dev/arlo/PROMPTS.md (base master template).

For each of these prompts in order — C1, C2, C3, C4, C5, C6, C7 — do the following:

1. Substitute the row's variables into the master template with the stream addendum.
2. Execute deep research. PRIMARY SOURCES for this batch are Ableton's official Live 12 launch materials, Live 12 Reference Manual, and the Live 12 dot-release notes (12.0, 12.1, 12.2, etc.). Secondary: Ableton Learn Live videos with timestamps, Ableton Loop talks, version-stamped creator tutorials posted in 2024 or later.
3. Write to /Users/cfitt/Dev/arlo/corpus/daw/ableton/live-12/{filename}.md.
4. Move to the next prompt.

After all 7 files are written, list them with sizes and give a one-sentence summary of each.

Stream reminders:
- This batch is the LIVE-12-ONLY batch. Every feature claim must verify against Ableton's official Live 12 release materials. If a feature is rumored but not in a shipped release note, OMIT it.
- C5 (Stem Separation) is Live 12.1+, not 12.0. Confirm the point release.
- C6 (Push 3 standalone) — distinguish standalone from tethered Push 3. Standalone has feature limits (third-party plugins not supported) that must be named.
- C7 (Live 12 point-releases changelog) — pull only verified additions from official release notes. Do not invent feature additions. If a feature is "expected in 12.x" but not yet shipped, OMIT it.
- C1 (Modulators) is the highest-leverage file in this batch — it's the single biggest workflow change in Live 12 and the file most likely to retrieve. Make it strong.
- Default tags include `daw-ableton`, `live-12`, `live-12-feature`, plus the topic tag.
```

---

### Batch D5 — Production Patterns

```
Run research batch D5 for ARLO DAW: Ableton.

Read /Users/cfitt/Dev/arlo/DAW-ABLETON-PROMPTS.md (stream addendum) and /Users/cfitt/Dev/arlo/PROMPTS.md (base master template).

For each of these prompts in order — D1, D2, D3, D4, D5, D6, D7 — do the following:

1. Substitute the row's variables into the master template with the stream addendum.
2. Execute deep research. Mix Mike Senior's *Mixing Secrets* and Sound on Sound Inside Track features (DAW-agnostic principle layer) with Ableton-specific implementation citations from the Live 12 Reference Manual and Ableton Learn Live.
3. Write to /Users/cfitt/Dev/arlo/corpus/daw/ableton/patterns/{filename}.md.
4. Move to the next prompt.

After all 7 files are written, list them with sizes and give a one-sentence summary of each.

Stream reminders:
- These are the HIGHEST-LEVERAGE files for retrieval (users phrase questions as "how do I do parallel comp in Live", "vocal chain in Ableton"). Make the recipes concrete: name the devices in chain order, give starting parameters, give the rationale.
- D2 (sidechain ducking) explicitly compares the classic Compressor-sidechain approach to the Live 12 Envelope Follower modulator. The Timeless I8 file goes deeper on the classic approach; cross-link.
- D3 (vocal chain) — cross-link to the general-corpus `corpus/mixing/vocal-mixing.md` for the DAW-agnostic principle layer.
- D6 (mastering in Live) — be honest about what Live can't do well (DDP, true 2-pass). Don't oversell.
- Default tags include `daw-ableton`, `live-12`, `production-pattern`, `recipe`, plus the pattern-specific tag.
```

---

### Batch D6 — Comping and Editing

```
Run research batch D6 for ARLO DAW: Ableton.

Read /Users/cfitt/Dev/arlo/DAW-ABLETON-PROMPTS.md (stream addendum) and /Users/cfitt/Dev/arlo/PROMPTS.md (base master template).

For each of these prompts in order — E1, E2, E3, E4 — do the following:

1. Substitute the row's variables into the master template with the stream addendum.
2. Execute deep research. The Live 12 Reference Manual entries on Comping, Warping, and Slicing are primary.
3. Write to /Users/cfitt/Dev/arlo/corpus/daw/ableton/editing/{filename}.md.
4. Move to the next prompt.

After all 4 files are written, list them with sizes and give a one-sentence summary of each.

Stream reminders:
- E1 (Comping) — Live 11+ takes-lane comping is the modern workflow. The pre-Live-11 manual-duplicates workflow is covered in Timeless I (not this batch). Do not conflate.
- E2 (Warp modes by ear) — be specific about audible artifacts per mode. The Live 12 manual gives the parameter set; the audible-difference claims need to be triangulated from version-stamped Sound on Sound articles or current creator demos.
- E4 (Slicing) — cross-link the existing `corpus/sampling/chopping-resampling-and-warping.md` (already Ableton-flavored). Don't re-cover the same material; go deeper on the slicing-mode trade-offs and sensitivity tuning.
- Default tags include `daw-ableton`, `live-12`, `editing`, plus the topic tag.
```

---

### Batch D7 — Frictions + Shortcuts + Logic Parity

```
Run research batch D7 for ARLO DAW: Ableton.

Read /Users/cfitt/Dev/arlo/DAW-ABLETON-PROMPTS.md (stream addendum) and /Users/cfitt/Dev/arlo/PROMPTS.md (base master template).

For each of these prompts in order — F1, F2, F3, F4, F5, G1, H1 — do the following:

1. Substitute the row's variables into the master template with the stream addendum.
2. Execute deep research. Ableton Help Center articles are the primary source for the friction files (F1–F5). Ableton's official keyboard-shortcuts appendix is primary for G1. The Live 12 Reference Manual + Apple Logic Pro 11 User Guide are primary for H1.
3. Write to:
   - F1, F2, F3, F4, F5 → /Users/cfitt/Dev/arlo/corpus/daw/ableton/friction/{filename}.md
   - G1, H1 → /Users/cfitt/Dev/arlo/corpus/daw/ableton/reference/{filename}.md
4. Move to the next prompt.

After all 7 files are written, list them with sizes and give a one-sentence summary of each.

Stream reminders:
- F1 (silent track) is one of the highest-retrieval-value files in the whole stream. Build it as a decision-tree the reader can walk top-down.
- F4 (CPU optimization) — Hyper-Threading toggle behavior on macOS changed across Live versions. Verify current state in Live 12 before claiming.
- G1 (Keyboard shortcuts) — both macOS and Windows forms must be given where they differ. The list should focus on the shortcuts that actually move the needle, not the long tail.
- H1 (Logic parity) — be explicit when Logic has NO direct equivalent (Session view, Drum Rack chain-selectors, Modulators-as-track-devices). Useful for ARLO when the user identifies as a Logic user.
- This batch is larger than most (7 prompts). If you start running low on context, complete the in-flight prompt fully, then summarize remaining work for the user to continue in a new session.
```

---

### Batch D8 — Timeless A: Resampling, Racks, Grooves, Audio-to-MIDI

```
Run research batch D8 for ARLO DAW: Ableton.

Read /Users/cfitt/Dev/arlo/DAW-ABLETON-PROMPTS.md (stream addendum) and /Users/cfitt/Dev/arlo/PROMPTS.md (base master template).

For each of these prompts in order — I1, I2, I3, I4, I5, I6, I7 — do the following:

1. Substitute the row's variables into the master template with the stream addendum.
2. Execute deep research. For this section, prefer older long-form creator tutorials with the Live version stamped (Mad Zach, Slynk, Ill Gates, Mr. Bill, Tom Cosm, Andrew Huang, Ned Rush) AND a Live 12 verification citation (manual section, or current tutorial confirming the technique still works). Sound on Sound's archived Ableton columns going back to Live 8 are also primary for this section.
3. Write to /Users/cfitt/Dev/arlo/corpus/daw/ableton/timeless/{filename}.md.
4. Move to the next prompt.

After all 7 files are written, list them with sizes and give a one-sentence summary of each.

Stream-specific reminders for TIMELESS files:
- EVERY citation must include the Live version the source was produced in (e.g., "Mad Zach, 'Drum Rack Multisamples', YouTube 2018 — demonstrated in Live 10").
- Pre-Live-12 content is welcome — but each claim must also carry a Live 12 verification: either a current tutorial demonstrating the same technique in Live 12, or a citation to the Live 12 Reference Manual section that confirms the parameter/device still exists.
- Where a Live-12 tool partially supersedes the timeless technique (Modulators superseding LFO-Tool workarounds; MIDI Generators superseding some Scale-Random-NoteLength chains), the file should show BOTH approaches with notes on when to reach for which. Don't downrank the timeless technique unless the Live-12 version is clearly better in every dimension.
- I1 (resampling) is the foundational file of this section. Make it strong — this is the single most-used producer technique in Live and deserves the deepest coverage.
- Default tags include `daw-ableton`, `live-12`, `daw-ableton-timeless`, plus the topic tag. The `daw-ableton-timeless` tag lets ARLO favor older-but-verified techniques when the user asks for a "classic" Live workflow.
```

---

### Batch D9 — Timeless B: Sidechain, Parallel Bus, Performance

```
Run research batch D9 for ARLO DAW: Ableton.

Read /Users/cfitt/Dev/arlo/DAW-ABLETON-PROMPTS.md (stream addendum) and /Users/cfitt/Dev/arlo/PROMPTS.md (base master template).

For each of these prompts in order — I8, I9, I10, I11, I12, I13 — do the following:

1. Substitute the row's variables into the master template with the stream addendum.
2. Execute deep research with the TIMELESS-section discipline: version-stamp the original source; provide a Live 12 verification source; show both timeless and Live-12 paths when a newer tool partially supersedes the technique.
3. Write to /Users/cfitt/Dev/arlo/corpus/daw/ableton/timeless/{filename}.md.
4. Move to the next prompt.

After all 6 files are written, list them with sizes and give a one-sentence summary of each.

Stream reminders:
- I8 (classic sidechain) is the partner file to D2 (Production-Patterns sidechain). I8 covers the pre-Modulator approach in depth — Audio From routing, Compressor sidechain settings, kick-key-then-mute trick. D2 compares classic vs. Modulator. Cross-link.
- I9 (send-return parallel bus) — Mike Senior's *Mixing Secrets* parallel-bus chapters are the DAW-agnostic principle; cross-link to general-corpus mixing files. The Ableton-specific angle here is how Return tracks work, Pre vs. Post sends, and the "color Return" pattern.
- I11 (classic MIDI effect chains) — explicit contrast with C3 (Live 12 MIDI Generators/Transformations). Cross-link C3.
- I12 (Live as looper/performance) — this is Live's original 2001 pitch. Ableton Loop talks on live setups are great sources. Working performers' rig walkthroughs (Ableton Certified Trainers, Mad Zach live shows) are secondary.
- I13 (eight-bars-first) — Tom Cosm is the canonical voice for this discipline. Ill Gates also wrote about it. Methodology file, not a parameter file — content should be philosophical/strategic, not knob-twist.
- Default tags include `daw-ableton`, `live-12`, `daw-ableton-timeless`, plus the topic tag.
```

---

### Batch D10 — Timeless C: Sound Design, Library, Mixing

```
Run research batch D10 for ARLO DAW: Ableton.

Read /Users/cfitt/Dev/arlo/DAW-ABLETON-PROMPTS.md (stream addendum) and /Users/cfitt/Dev/arlo/PROMPTS.md (base master template).

For each of these prompts in order — I14, I15, I16, I17, I18, I19 — do the following:

1. Substitute the row's variables into the master template with the stream addendum.
2. Execute deep research with the TIMELESS-section discipline (version-stamp + Live 12 verification).
3. Write to /Users/cfitt/Dev/arlo/corpus/daw/ableton/timeless/{filename}.md.
4. Move to the next prompt.

After all 6 files are written, list them with sizes and give a one-sentence summary of each.

Stream reminders:
- I14 (Bounce in Place commit discipline) is the producer-judgment companion to A6 (the technical-mechanism file). I14 is about WHEN to commit; A6 is about HOW. Cross-link.
- I16 (Operator FM sound design) — Sound on Sound *Synth Secrets* (Gordon Reid) FM articles are gold for the principle layer. Welsh's *Synthesizer Cookbook* gives canonical FM patches. The Live-specific layer is the Operator algorithm choice and parameter mapping. Cross-link to B9 (Operator/Analog devices) and to the general-corpus `corpus/synthesis/fm-and-wavetable-synthesis.md`.
- I17 (Wavetable MPE) — confirm any Live 12 MPE workflow improvements before claiming. The Live 11+ MPE-on-Wavetable feature set is stable but Live 12 may have added per-note expression editing improvements.
- I19 (Live mixing discipline — Utility everywhere) — cross-link to the general-corpus `corpus/recording/signal-flow-and-gain-staging.md` for the DAW-agnostic gain-staging foundation. The Live-specific angle is Utility as the everywhere-device and Master section conventions.
- This is the final batch of the stream. After completion, the corpus has 62 new files in `corpus/daw/ableton/` — roughly 600–900 chunks of Ableton-specific retrieval surface.
- Default tags include `daw-ableton`, `live-12`, `daw-ableton-timeless`, plus the topic tag.
```

---

## Post-batch verification

After each batch completes, run this quick check from a terminal:

```bash
# Confirm files landed in the right places
find ~/Dev/arlo/corpus/daw/ableton -name "*.md" -newer ~/Dev/arlo/DAW-ABLETON-PROMPTS.md -type f | sort

# Sanity-check sizes (should be 5–12 KB each)
find ~/Dev/arlo/corpus/daw/ableton -name "*.md" -newer ~/Dev/arlo/DAW-ABLETON-PROMPTS.md -type f -exec ls -lh {} \;

# Confirm front-matter on a random new file
head -10 ~/Dev/arlo/corpus/daw/ableton/<area>/<filename>.md

# Quick check that "Live 12" appears in the new files (version-stamp signal)
grep -L "Live 12" ~/Dev/arlo/corpus/daw/ableton/**/*.md 2>/dev/null
# (files listed here are MISSING the version stamp — investigate)
```

---

## Tracking what's done

Append to this checklist as batches complete.

- [x] Batch D1 — Fundamental Workflows *(7 files, 14,209 words — clean; surfaced 5-track-type and 16-Macro additions)*
- [x] Batch D2 — Stock Devices: Mixing Tools *(6 files, 11,474 words — caught 5 plan-doc errors: Channel EQ not EQ Controls; Delay 3 modes Live 10.1+; Hybrid Reverb Vintage param; Auto Shift 12.1+)*
- [x] Batch D3 — Stock Devices: Color, Synths, Samplers *(5 files, 10,036 words — caught Drift is Live 11.3+)*
- [x] Batch D4 — Live 12 Features *(7 files, 13,249 words — caught Stem Separation 12.3+; Note Modulator nonexistent; verified Generators/Transformations lists; tuning per-project)*
- [x] Batch D5 — Production Patterns *(7 files, 14,339 words — surfaced classic+modulator hybrid sidechain pattern)*
- [x] Batch D6 — Comping and Editing *(4 files, 9,478 words — covered Leader/Follower rename and Live 12.1 slicing preset redesign)*
- [x] Batch D7 — Frictions + Shortcuts + Logic Parity *(7 files, 15,134 words — verified Apple Silicon P-core default; macOS-only shortcuts)*
- [x] Batch D8 — Timeless A: Resampling, Racks, Grooves *(7 files, 15,135 words — documents both 8-Macro legacy and 16-Macro current)*
- [x] Batch D9 — Timeless B: Sidechain, Parallel Bus, Performance *(6 files, 14,165 words — explicit Velocity Shaper / classic-chain contrasts)*
- [x] Batch D10 — Timeless C: Sound Design, Library, Mixing *(6 files, 12,348 words — Chowning FM, MPE-Wavetable lineage)*

**Stream complete:** 62 files, **129,567 words** in `corpus/daw/ableton/`. Approximately **600–900 chunks** of Ableton-specific retrieval surface ready for ARLO ingestion.

---

## After all batches complete

Three follow-ups worth doing once the DAW: Ableton stream is complete:

1. **Version-stamp validation pass.** Grep the new files for any feature claim that lacks a Live-version annotation. The pattern is `(Live 12+)` or `(Live 11+)` or `(Live 12.1+)` or similar inline. Files that mention Hybrid Reverb, the unified Delay, Modulators, scale-aware MIDI, Drift, Meld, Roar, Auto Shift, Granulator III, stem separation, or Note Modulator without a version stamp need fixing.

2. **Cross-link audit.** Confirm the See-also footers actually point at existing files. Run:
   ```bash
   grep -h "See also:" ~/Dev/arlo/corpus/daw/ableton/**/*.md | sort -u
   ```
   Verify each referenced path exists.

3. **Logic parity follow-up.** H1 (Ableton-to-Logic parity map) becomes the seed for a future Logic-Pro DAW stream. When/if that stream is planned, H1 is the natural index.

When Ableton ships Live 13, the version-stamping discipline pays off: a regex search across the corpus identifies every Live-12-only claim that needs re-verification.
