# 02 — Use Cases

The workflows ARLO must support. Each is phrased as something you say, what ARLO does, and which seed data it leans on. These are the acceptance targets for "the engine works."

## A. Gear-grounded recommendations

1. **"What chain should I use for a washed-out ambient guitar?"**
   ARLO proposes a signal chain *from gear you actually own* (e.g., `OBNE Dark Star V3 → Chase Bliss MOOD MkII → Strymon Big Sky`), explains the role of each, and cites each pedal's profile/research.
   → *Gear profiles + research.*

2. **"How do I dial in the Blooper for a bottomless layered loop?"**
   ARLO answers from that device's `manuals/` and `research/`, not generic web knowledge.
   → *Gear `manuals/` + `research/` for the named device.*

3. **"Which of my reverbs is best for a vocal throw vs a pad?"**
   ARLO reasons over the *subset you own* and contrasts them.
   → *Gear + Software profiles (category/subcategory).*

## B. Software / plugin choices

4. **"Pick a plugin from my library to glue a drum bus."**
   ARLO recommends from `Pedalxly/Software` (e.g., a specific iZotope/Soundtoys/Cableguys tool you own), with host compatibility (`host_in`).
   → *Software profiles (`formats`, `host_in`, `installed`).*

5. **"What do I already own that overlaps with X?"**
   Inventory-aware answers so you stop buying duplicates (a known recurring need — "did you finish a track before buying another pedal").
   → *Software `_inventory.json` + profiles; Gear profiles.*

## C. Song setup

6. **"Set up a skeleton for a 3-minute post-punk track."**
   ARLO drafts sections/parts (Intro/Verse/Chorus/…), suggests instrumentation against your rig, and notes a workflow to follow.
   → *arlo `workflows/` (e.g., post-punk-texture-dynamics) + taste profile.*

7. **"Give me a starting point in the style of [artist/album]."**
   ARLO draws on the aesthetic/albums corpus to propose structure and production moves.
   → *arlo `corpus/artists`, `corpus/albums`, `corpus/structure`.*

## D. Knowledge / craft, with citations

8. **"What LUFS should I target for streaming, and how?"**
   Cited answer from the corpus reference cards.
   → *arlo `corpus/mastering`, `corpus/reference`, `chunks.jsonl`.*

9. **"Teach me a songwriting method that fits how I work."**
   ARLO surfaces a workflow (Eno oblique strategies, Rubin reduction, beat-first, etc.) matched to your taste profile.
   → *arlo `workflows/` + `taste-profile/`.*

## E. Taste-aware framing

10. **"Is this idea 'me'?"**
    ARLO reflects your `spotify-taste-profile.md` and aesthetic corpus to keep suggestions in your lane.
    → *arlo `taste-profile/` + `corpus/`.*

## Cross-cutting requirements

- **Grounded, not generic.** Every answer should prefer *your* data over generic model knowledge, and say when it's falling back to generic.
- **Cited.** Instructional claims link to a source (manual, profile, corpus chunk).
- **Inventory-honest.** ARLO only recommends gear/software you actually own (unless explicitly asked "what should I buy").
- **Conversational + iterative.** This is a "shaping project" — the persona and answers improve as you correct ARLO.

## The single acceptance test for the engine

> Open `claude` as ARLO, ask use-case **#1**, and get a chain built only from gear in `Pedalxly/Gear`, with at least one citation to a real file — *without* you pasting any data into the prompt.

If that works, the engine is real. Everything else is breadth and UI.
