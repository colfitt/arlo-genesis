# ARLO — The Persona Roast

*Five target users react to the current interface (Rig canvas, Gear viewer, Big
Time profile/research). Grounded in the actual screens. In their own voices.
Purpose: surface flow, placement, and sizing pitfalls before the next design
pass — and feed a redesign brief. Companion to [personas.md](personas.md).*

> **Tension worth noting up front:** the biggest single issue — *creation
> happens in the `./arlo` terminal, the GUI mostly views* — splits the room.
> Maya, Deacon and June hate it. Fitz defends it. Ori is mixed. That
> disagreement is the map of who you're really building for.

---

## 1. Maya — the texturalist
*"Your pitch to me is 'never lose a sound.' So why is the sound-catcher a baseboard?"*

**The roast — flow, placement, size**
- The one box that captures a sound — **`Ask ARLO for a sound…`** — is a skinny
  line pinned to the very bottom, same visual weight as a browser URL bar. That
  should be *the room*, not the trim.
- I nudged the Microcosm and every knob reads **`12:00 · 64`** — MIX, TIME,
  REPEATS, all identical. Is that my sound, the factory default, or a
  placeholder? The numbers are decoration, not memory. I can't tell what's live
  vs saved.
- There's a **photo of my Microcosm** on the board and, wired right next to it, a
  **black rectangle** that says "OBNE Dark Star V3." Two different visual
  languages on the same cable. It looks like two apps holding hands.
- **`Set up session`** vs **`Ask`** — two buttons, same corner, and I don't know
  which one gets me a sound and which one signs me up for something.
- That **teal bar** at the top of the pedal panel has no label. Gain? A record
  meter? Vibes? I'm guessing.

**What I can't do that I want to**
- Hit one glowing **Save this sound** from the board — right now, at 1am, named
  "thursday drone" — *without alt-tabbing to a terminal to type `./arlo`.*
- Scrub my session back: **"what did the board look like 20 minutes ago?"** A
  visual history/undo of the rig, not just a saved file.
- **Pin the take to the settings.** My recording's in Voice Memos and the knobs
  are nowhere. Put the audio and the patch in the *same object.*

**What I like — but fix it**
- The living-pedalboard idea and the deep gear writing are genuinely lovely. But
  the board is 80% empty black with two nodes floating in it — make it feel like
  *my* room, my layout, warm, not a void with two icons.

**First thing I'd change:** *Make catching a sound the center of the screen, not the footer.*

---

## 2. Deacon — the operator (live)
*"I'd never open this on a Sunday. It's all Thursday."*

**The roast — flow, placement, size**
- Everything is **mouse-sized.** The knobs, `TAP`, `BYPASS` — I'm in low light
  with in-ears in. I need targets I can hit with a boot, not a cursor.
- **Where's the set?** You gave me a 15-pedal board and a signal-chain list and
  nothing that says "Song 3." My whole job is song-to-song recall and there's no
  setlist, no scene buttons, no "next."
- The loudest, greenest thing on screen is **`✓ board saved`**, top-right. But
  "saved" isn't what I'm scared of. I'm scared of **firing the wrong preset in
  front of a room.** Show me what's *armed* and on *what channel* — loud.
- Every node shouts a **`CC` count** — `30 CC`, `0 CC`, `43 CC`. Between songs
  that's noise, and the `0 CC` ones read as *broken.*
- The `Ask ARLO` bar and `Set up session` sit bottom-center, where my eyes never
  are mid-set.

**What I can't do that I want to**
- A **LIVE / PERFORMANCE mode**: giant per-song scene tiles, *now* + *next*, one
  tap to fire, a huge **PANIC.** The build view is fine for Thursday; give me a
  Sunday view.
- A **setlist** that maps songs → scenes, reorderable, with a visible "now
  playing."
- **Arm-then-fire** confirmation and a visible **"Channel 16 / looper safe"**
  light so I trust it won't eat my loop live.

**What I like — but fix it**
- The signal-chain reorder list is good, and one clear serial path is right. But
  show **signal direction** (arrows) and **engaged vs bypassed at a glance** — I
  currently can't tell what's even *on.*

**First thing I'd change:** *Build the Sunday view. All of this is Thursday.*

---

## 3. June — the hybridist
*"Your magic is whispering in a grey pill. Why?"*

**The roast — flow, placement, size**
- The single most interesting thing in the whole app —
  **`describe a vibe → 3 grounded patch candidates`** — is a tiny grey
  *placeholder pill* in the toolbar next to a sparkle I nearly missed. That's the
  headline. Why is it hiding?
- Then the app tells me to **"run `./arlo` in a terminal"** to actually set up a
  patch. You lost me. The second I leave the app to type commands, the song is
  dead — that's the exact setup-admin hour that kills my ideas, and you built it
  *into* the product.
- I describe a vibe and I get… "candidates." **Show me.** Where do the three
  land, how do I audition them, how do I commit one to the board? The flow ends
  at the pill.
- The thing I came for — **conversation about my sound** — has the least room on
  screen (a cramped rail + a bottom line). The gear *list* has more real estate
  than the gear *dialogue.*

**What I can't do that I want to**
- Go **vibe → an actual set-up chain on the board → audition → keep**, end to
  end, **without a terminal.**
- Save a **whole song's setup** (guitar chain + synth + vocal-fx idea) as one
  recallable thing, with the **reference track pinned** to it.
- Type **"sounds like ___"** as a real input — throw "mk.gee Alesis haze" at it
  and watch my own gear get arranged for it.

**What I like — but fix it**
- It's genuinely **grounded in my actual gear** — the 41-device library is real,
  the Big Time write-up clearly *knows* the pedal. But that grounding is
  invisible until I go digging. When it suggests something, **tell me why** —
  "your Deco into Lost & Found because…"

**First thing I'd change:** *Make "describe a vibe" the front door — and let it finish the job in the GUI.*

---

## 4. Ori — the designer (precision)
*"I'm a composer, not your file system."*

**The roast — flow, placement, size**
- **`no MIDI output ports found`** sits at the top of the Big Time profile like a
  wound. Error? State? Should I care? No label, no fix, no dismiss — just
  anxiety hanging there.
- The **Research tab** shows me `research/links/cb-big-time-where-recipes-live.md`
  and nine more **raw file paths.** I should never see a directory in a music
  app. Titles, not paths.
- **`12:00 · 64`** — a clock position *and* a number. Which one is truth? When a
  director says "recall cue 14 *exactly*," I need the exact value and *proof*
  it's exact — not a knob drawing pointing at noon.
- A dropdown labelled **`— device —`** next to a **completely blank dropdown.** A
  blank dropdown is a bug that shipped.
- The writing is excellent and jammed **wall-to-wall** at an exhausting measure.
  Long-form deserves a real reading column.

**What I can't do that I want to**
- **Named, versioned recall with a diff** — "what changed between v1 and v3 of
  this pad" — and a guarantee it restores *exactly.*
- Actually **organize 400 presets**: tags, folders, search by *character*
  ("darker"), not an alphabetical brand list.
- See **provenance as citations** — titled sources, not `.md` filenames.

**What I like — but fix it**
- I respect the **depth and the sourcing** — the "manual-vs-web flag" that flags
  which attributions are journalist framing vs first-party is *exactly* the rigor
  I want. But present it like a **reference document** — headings, a table of
  contents, a readable column — not a dumped markdown file.

**First thing I'd change:** *Delete every filename and raw status string from the UI. Speak in music, not paths.*

---

## 5. Fitz — the systems mind (the contrarian)
*"Decide what the GUI is FOR. Right now it's a viewer cosplaying as an editor."*

**The roast — flow, placement, size**
- Everyone's mad about **"run `./arlo` in a terminal."** I'm not — it's the best
  call in here. But you **half-hide it in grey helper text** like you're
  embarrassed. Own the CLI or bin it; don't apologize for it.
- You've got **two sources of truth fighting**: a GUI that mostly *views* and a
  CLI that *does.* The GUI is a read-only mirror with **knobs I can't trust.**
  Either it writes back to the same markdown the CLI does, or it's a demo.
- **"Drop a saved pedalboard.app HTML page onto the board to import its pedals"**
  is genuinely clever — and buried at the bottom of a panel. Where's the
  documented format? Where's **export**? If I can drop HTML *in*, let me get my
  scene *out* as JSON/markdown.
- The **board and the numbered signal-chain list are the same data twice.** On a
  15-pedal rig that's a lot of duplicated pixels. One should do something the
  other can't.
- **`120 / ▶ sync`** floats top-right with zero context — the most
  powerful-looking control and the least explained.

**What I can't do that I want to**
- Have **everything the GUI shows be keyboard-driven and scriptable**, backed by
  a **documented file format** for scenes/rigs — with **export**, not just
  import.
- See the **data model**: this pedal node *is* this markdown file — let me
  click through to the source. (Ironically the Research tab leaks paths while the
  Rig nodes, which *should* link out, don't.)
- **Native version history** — it's already markdown in a git repo. Show me the
  diffs.

**What I like — but fix it**
- Local-first, markdown-canonical, the drag-HTML import, the CLI — all correct.
  But the **GUI↔CLI seam is unfinished.** Make the GUI a first-class *editor* of
  the same files, or explicitly brand it a **read-only dashboard** and stop
  teasing editable knobs.

**First thing I'd change:** *Pick a job for the GUI — editor or dashboard — and commit.*

---

## Redesign backlog (synthesized)

Ranked, each tagged with who's yelling and the screen it lives on. This is the seed for the design pass.

| # | Redesign target | Who's yelling | Where |
|---|---|---|---|
| 1 | **Promote the core loop.** Move "Ask ARLO / describe a vibe" from footer + toolbar pill to a primary surface. The conversation *is* the product and it has the least real estate. | Maya, June | Rig footer, Gear toolbar |
| 2 | **Live / Performance mode.** Setlist → scene tiles, now/next, giant fire + PANIC, engaged + channel-16-safe indicators, touch-sized. | Deacon | new view |
| 3 | **In-GUI capture & save-scene.** One action to snapshot board + knobs into a named scene, no terminal; attach a take/reference. | Maya, June | Rig |
| 4 | **Trustworthy state.** Replace `12:00 · 64` with clear live-vs-saved values; show engaged/bypassed at a glance; a recall-proof / byte-identical badge. | Maya, Ori, Deacon | pedal panel, nodes |
| 5 | **De-jargon the surface.** Hide/rename `CC` counts, `MIDI bypass`, `no MIDI output ports found`, raw file paths → human titles; label the mystery controls (`120 / sync`, `— device —`, the teal bar). | all (Ori, Deacon loudest) | everywhere |
| 6 | **Finish vibe → chain → audition → commit.** Complete the flow the "describe a vibe" pill starts, entirely in-GUI, showing the grounding ("why *your* Deco"). | June, Maya | Gear |
| 7 | **Reading/reference redesign.** Long-form profile & research as a real document: reading column, titled sources / ToC — not a raw `.md` dump with path chips. | Ori, Maya | Gear viewer |
| 8 | **Resolve board-vs-list redundancy + mixed visual language.** One coherent node style (drop the photo/rectangle clash), signal-direction arrows, and give the second view a distinct job. | Maya, Fitz, Deacon | Rig |
| 9 | **Kill dead idle states.** `NO PEDAL SELECTED` and the empty Gear viewer should show a board summary, recent scenes, or the vibe box — not a black void. | all | Rig panel, Gear viewer |
| 10 | **Declare & finish the GUI↔CLI seam.** GUI writes back to the same markdown (+ export, + click-through to source), or explicitly brand it read-only. | Fitz, Ori | architecture-wide |

---

## Paste-ready brief for the design pass

> Redesign 5–10 areas/workflows of ARLO, a local-first macOS studio app that
> knows a musician's boutique rig and recalls whole "scenes" (synth patch +
> pedal presets + controller state). Current UI has two views — **Rig** (a node
> board + signal-chain list + a per-pedal control panel) and **Gear** (a device
> library + long-form profile/research reader) — plus a thin "Ask ARLO" chat
> footer. Creation currently happens in a `./arlo` terminal; the GUI mostly
> views.
>
> Prioritise these problems (see backlog): (1) the core conversational loop is
> demoted to a footer/pill; (2) no live/performance mode for gigging recall;
> (3) no in-GUI way to capture/save a sound — it needs the terminal; (4) control
> state (`12:00 · 64`) doesn't distinguish live vs saved and shows no recall
> proof; (5) developer jargon leaks everywhere (`CC` counts, `no MIDI output
> ports found`, raw `.md` file paths, unlabeled `120 / sync` and `— device —`);
> (6) the "describe a vibe → grounded patches" flow dead-ends; (7) long-form
> reading is an unstyled markdown dump; (8) board and signal-chain list duplicate
> each other and mix a photo-pedal with abstract node boxes; (9) idle states are
> dead black space; (10) the GUI↔CLI seam is undeclared.
>
> Produce redesigns as distinct workflows using the elements we already have
> (nodes, signal chain, control panel, library, reader, chat). For each: the
> problem it solves, which user it's for (Maya/ambient-capture,
> Deacon/live-recall, June/vibe-to-track, Ori/precision-recall,
> Fitz/local-first-power), and the before→after of the flow.
