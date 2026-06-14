https://support.spitfireaudio.com/en/articles/11816117-kontakt-vs-kontakt-player-the-differences
Spitfire Audio Help Centre · support article · accessed 2026-06-10
(+ https://pluginoise.com/native-instruments-vs-spitfire/ · context)
(+ https://www.spitfireaudio.com/en-us/collections/instruments?plugin_types=kontakt+player · Kontakt Player filter)

# The Spitfire engine split — dedicated plugin vs Kontakt vs Kontakt Player

Spitfire libraries run in one of **three** hosts. Knowing which is which matters for the rig (Logic AU, external drive).

## 1. Spitfire's own DEDICATED PLUGIN (newer libraries)
A bespoke Spitfire player — minimalist UI, frozen-landscape art, mic mixer, macro faders, and the **Evo Grid**. Installs as standalone **AU / VST / VST3** (no Kontakt needed). Praised as "a joy to use, super intuitive and smooth."
**Owned & in this category:** **BBC Symphony Orchestra, Fractured Strings, Resonate, Ólafur Arnalds Cells, Originals – Rare Flutes, LABS.** (These are the six showing up as `.component`/`.vst3` in CONTENTS.md — each is its own AU plugin.)

## 2. Free KONTAKT PLAYER (older "Player" libraries)
Older Spitfire libraries are NCW sample sets that load in the **free Kontakt Player** (no full-Kontakt purchase needed) — they appear in Kontakt's **Libraries** pane after authorising in **Native Access**. More keyswitching for articulations vs the dedicated plugin. Full access to all sounds + front-panel params.
**Owned & in this category (on the drive):** **Albion Loegria, Orchestral Swarm, Symphonic Strings Evolutions, Spitfire Symphony Orchestra** — all run in **Kontakt / Kontakt Player 5.6.8+ (Symphony Orchestra needs 7.5.2+)**.

## 3. Full KONTAKT (paid)
Only needed for non-Player libraries with no serial (loaded via Kontakt's *file browser*, not the Libraries pane) and for editing individual samples inside patches. **The user owns full Kontakt 8** — so even non-Player content is covered, and they can dig into sample-level editing if wanted.

## Why it matters for THIS rig
- **Logic is AU-only.** The dedicated-plugin libs load as native AU. The Kontakt libs load **inside the Kontakt AU** (one Kontakt instance can host several). Either way, everything is reachable in Logic.
- **The split decides where to look for a sound:** newer textural/percussion/string colour = open the dedicated plugin directly; the *evolving/orchestral wall* libraries (Loegria, Swarm, SSEvo, Symphony) = open **Kontakt 8** first, then the Library.
