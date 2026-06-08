https://www.youtube.com/watch?v=g5v11gs8MXc
Dave Mech · Digitakt II OS 1.10 is here! // Deep Dive · 2025-03-21

> Source captions: YouTube auto-generated, cleaned to prose. ~20m. DIGITAKT II specific — walks the OS 1.10 feature additions. Dave Mech also sells a 17-hour DT2 course; this is his free OS-update breakdown.

## What OS 1.10 added (the headline list)
- **Mono sampling**: SAMPLE page → B encoder now offers **Stereo / Left-Right / Mono L / Mono R**. Also fixed a bug where an imported Digitone-1 project got stuck in mono-dual-global mode.
- **Comb+ filter**: joins the existing Comb− (Comb− = more "tube-like"; Comb+ = more "string-like"). Demo: with feedback high, low-pass open, scrolling through it sounds immediately metallic/string-like; works as a delay too. Taken from the Digitone II.
- **Track Swap**: FUNC + FLTR → setup → **Track Swap**. Hold two tracks to swap their contents (e.g. swap kick on track 1 with a sound on track 7), and swap back.
- **Key-tracking modulation matrix** (from Digitone II): set up to **4 modulation destinations** with +/- depths; the note you play scales the modulation depth. Example: negative LP4 frequency → higher notes close the filter; positive → higher notes open it.
  - **Playable Comb+**: set Comb+ FREQUENCY as a key-track destination at depth **8** → each note maps to the 12-note system, so you can *play the comb filter*. Make the sample very short (a "blip") to excite it; LP filter sets how plucky vs stringy, feedback sets how long it rings. Add FX = "brilliant".
- **P-lock all active trigs**: hold a trig + TRACK → adds (or, push encoder, removes) parameter locks across **all** active trigs at once (e.g. lock filter cutoff to the whole track). Also works per page: hold + PAGE. Big workflow speed-up, especially removal.
- **Persistent pattern mutes**: the purple pattern-mute mode now survives a power cycle (it used to revert to global mute on boot).
- **Base-width filter routing pre/post filter** (from Digitone II): place the base-width filter before or after the main filter — solves low-frequency build-up. Called "one of the best features they could have added".
- **Overdrive routing pre/post filter**: route a resonant filter *through* the overdrive (post) for "very nasty" boosting around the cutoff. Pre = the old behaviour.
- **UI/contrast improvements** for color-blindness/dark rooms; clearer page-hold "fill" indication.
- **Kit → Load to Empty**: pattern/kit menu → manage kit → select kit → right-arrow → **Load to Empty** loads the kit into all *empty* patterns (great for building a template project).
- **New velocity curve**: an extra exponential curve with a **higher starting point** (the old exponential was nearly inaudible in its first half).
- **Sample → Load to Track**: in the +Drive sample browser you can now **Load to Track N** directly, not just Load to Project.
- **MOD destinations categorized**: the MOD destination list is grouped into categories; FUNC snaps between categories.

## Personalize menu (from the Octatrack)
- **Live-record overdub**: live recording now adds notes to existing trigs rather than replacing. Minor for DT2 mono audio tracks; big for **MIDI tracks** (record chords on top of existing trigs).
- **Per-live-record p-lock mode**: ALL = creates lock-trigs alongside note-trigs as before; **TRIG** = only adds p-locks to *already-existing* trigs (no weird in-between changes). Combine with the Euclidean generator to add e.g. decay/reverb changes only to the generated trigs.
- **Track Select behaviour**: NORMAL (pressing a trig also plays it; hold TRACK to select silently), **SILENT** (selecting a track never sounds — good live), **MANUAL** (a selected track stays selected so you can trigger other sounds without changing selection — e.g. live-record p-locks on one track while drumming a hat on another), **INVERTED**.

Dave Mech's framing: "small but very significant" changes; many pulled across from the Digitone II to bring the DT2 to parity.
