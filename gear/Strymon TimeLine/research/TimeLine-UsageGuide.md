# Strymon TimeLine — Usage Guide

The TimeLine is the End board's **deep delay workstation** — 12 machines, 200 presets, a
30-second looper, and per-preset MIDI clock. In this rig it's a **Digitakt-clocked, Nixie-
managed** instrument: set it to follow the Digitakt's tempo globally, build/organize presets
offline in **Nixie 2**, and lean on its degraded machines (dTape, Lo-Fi, dBucket, Ice) for the
"recorded-wrong" wall. The clearest mental model comes from Richard DeHove's complete
walkthrough; the most on-aesthetic technique from **Hammock** (run it on **Lo-Fi, last after
the reverb, riding the knobs by hand**). Pair it with the Big Time via **per-preset tap
divisions** (eighth on one, dotted-eighth on the TimeLine, off the one shared clock).

> Front-panel constants to memorize (DeHove): **MIX 3:00 = 50/50** (not noon); **REPEATS 3:00 =
> the self-oscillation ceiling**; **FILTER full-left = OFF, noon = darkest, full-right adds highs**;
> knob positions (SPEED/DEPTH/FILTER/GRIT) have **memory** and carry between machines. Firmware
> is frozen at **v1.88**; the TimeLine **only receives MIDI clock — it's always a slave.**

---

## 1. Essential workflows

### The 12 machines (signature settings)
- **dTape** — Tape Speed Fast(hi-fi)/Normal(lo-fi); bottom knobs re-map to **Tape Age** (L=new,
  R=old), **Tape Bias** (9:00=balanced), **Crinkle** (R=mangled), **Wow & Flutter**. Frippertronics
  wall (Chords of Orion): longest time ~2.5 s, lots of repeats, heavy decay/grunge. *(richard-dehove, chords-of-orion)*
- **dBucket** — Single (1 chip) / **Double** (2 chips, cleaner); GRIT = Bucket Loss (more = more
  degraded). Voices like a Memory Man — dark/warbly, warmer baritone repeats. *(mscarney302, richard-dehove)*
- **Digital** — Smear, **High Pass (off→900 Hz)**, Repeat Dynamics. Rhett Shull's "fake chorus":
  max TIME, REPEATS fully down, mod depth full, speed ~11:00. *(rhett-shull, richard-dehove)*
- **Dual** — Time 2 (ratio of main), Config Series/**Parallel** (keep Parallel for L/R spread —
  the U2 dotted-eighth + quarter). *(richard-dehove)*
- **Pattern** — 16 patterns; **#16 = early reflections** → faux reverb with Smear maxed. *(richard-dehove, community-hidden-features)*
- **Reverse** — best on big chords / slow ambient. **Ice** — Interval (−1 to +2 oct), Slice,
  **Blend** (a secondary dry↔ice mixer), Smear ~halfway; drone = upper voice a **5th above root**,
  very smeared. (Quirk: at full-Ice, SPEED/DEPTH do nothing.) *(richard-dehove, chords-of-orion)*
- **Duck** (Normal vs **Gate**), **Swell** (Rise up to ~2 s, add Smear), **Trem** (LFO shape, Speed
  as a *ratio of BPM*), **Filter** (LFO + polarity + Q + **pre/post-delay location**). *(richard-dehove)*
- **Lo-Fi** — nasty at **Sample ≤4 kHz**, **Bits 8** = classic; Vinyl off/Dynamic/Static; **8 gadget
  filters** (intercom, phonograph, megaphone, cell phone…). *(richard-dehove)*

### Hidden features & the feedback-loop insert
- **HP filter (off→900 Hz) is the fix for boomy banjo/baritone repeats** — set ~80–160 Hz. *(mscarney302, community-hidden-features)*
- **Feedback-loop insert (rear switch):** RIGHT IN/OUT become a send/return *inside the delay
  feedback path* — drop a fuzz/filter there to re-process every repeat (runaway grit; costs stereo). *(community-hidden-features)*
- **EP SET** maps the expression pedal to multiple knobs with independent ranges (a morph/dive). *(community-hidden-features)*

### Looper & MIDI clock (the rig setup)
- **Infinite repeats / freeze = HOLD the active preset footswitch** (A or B) — hold a wall, play
  over, release to decay. *(community-hidden-features)*
- **Clock master = the Digitakt (DeHove's globals, verbatim):** time units **BPM**, **Spillover ON**,
  **MIDI Clock Reset OFF** (critical — ON fights manual tweaks), per-preset **Tap = Global** so every
  preset inherits the incoming clock. Use **per-preset MIDICL** (OFF for free-running presets) to
  avoid a global tap overwriting saved tempos. *(richard-dehove, morningstar-midi-clock-tap)*
- **Looper in perfect sync:** drive it from the Digitakt over MIDI **Notes (0=Record, 2=Play,
  4=Stop, 14=Reverse, 16=Half-Speed)**; **LP LOC Post** bakes the wet tail in (better for ambient).
  Silent-loop drone: looper Post → Record + count → overdub onto silence → swell Ice in → Play. *(richard-dehove-looping, chords-of-orion)*

---

## 2. Signature presets & settings

**Presets share as `.syx` (SysEx)** — the universal currency for every Strymon blog preset, paid
pack, and trade. Manage with **Nixie 2** (current editor/librarian; legacy Nixie + Preset Librarian
read the same format). ⚠️ **No USB on the pedal — MIDI only, and most plug-and-play interfaces FAIL**
(use Roland UM-ONE MKII, iConnectivity MIO, or the Strymon Conduit; Globals: MIDI PA/CT ON, TH MERGE,
ST OFF). Import: File → Presets → Import (or drag the `.syx`), write to a slot. There's **no in-app
marketplace** — sharing is passing `.syx` files. *(strymon-nixie-preset-sharing-import, strymon-nixie-editor-librarian)*

**Copyable factory values** (verbatim from the factory card): *(strymon-factory-presets-full-list)*
- **Degraded (25A) — dTape:** TIME 1000 ms, TP SPD Normal.
- **Wowywowwowwow (03B) — dTape:** TIME 370 ms, TP SPD Fast.
- **Intercom (25B) — Lo-Fi:** TIME 500 ms, Sample 6 kHz, 10-bit, Filter 8.
- **8Bit Vinyl (17A) — Lo-Fi:** TIME 350 ms, Sample 1.5 kHz, 8-bit, Vinyl on.
- **Fizifths (06A) — Ice:** TIME 900 ms, Interval Oct+5th, Slice Short, Blend→dry.
- **Infinite Swell (26A) — Swell:** TIME 470 ms, Rise 0.50, Smear high, HiPass 350 Hz.
- **Verby (12A) — Pattern 16** (faux reverb): TIME 220 ms, Smear high, HiPass 500 Hz.

**Free `.syx` from Strymon "This Week's Preset"** (the best free source): **Corrupted Flowers** (Lo-Fi,
4 kHz/10-bit/intercom, clean blended under) · **Bokeh Bells** (dTape, Wow&Flutter maxed, Crinkle near-
max, Age ~2:00). *(strymon-twp-corrupted-flowers, strymon-twp-bokeh-bells)*

**Preset organization (Wittek/mscarney):** build a **small/medium/large brightness ladder** of tape
presets, each duplicated across **A = quarter / B = dotted-eighth** — flexible, not song-specific. *(sam-wittek, mscarney302)*

---

## 3. Power-user tips, tricks & hidden features

- **Pattern 16 + Smear maxed = a usable fake reverb** (no second pedal). *(community-hidden-features)*
- **Save the vanilla starter to BOTH A and B** of a machine's bank (A = clean reference, B =
  experiment); the engine LED goes off-color when modified-unsaved. *(richard-dehove)*
- **Subdivision A/B within one bank** (quarter vs dotted-eighth) to flip feel without scrolling. *(sam-wittek)*
- **Trem/Filter Speed as a *ratio of BPM*** — pick a ratio that isn't the pattern's so it doesn't
  get lost. *(richard-dehove)*
- **The looper can be a second sequenced looper** alongside MOOD/Blooper — triggered in sync from
  the Digitakt via MIDI notes, with Reverse/Half-Speed as performable mangles. *(richard-dehove-looping)*

---

## 4. Notable users & techniques

- **Hammock** (THE rig-relevant find) — on *Mysterium* the main machine was **Lo-Fi**, with one
  player riding the Lo-Fi knobs (and **unplugging cables mid-decay**) to mangle the tail; they run the
  TimeLine **last, after the BigSky** (wash-on-wash). Pure "recorded-wrong." *(hammock-timeline-lofi)*
- **David Helpling** — uses **Dual** as two independent modulation delays panned hard L/R (not
  ping-pong), performing SPEED/DEPTH live; "play sparsely, leave room" — a banjo-as-lead-over-drone
  blueprint. *(david-helpling-timeline-dual)*
- **Native Suns (Jason Mays)** — TimeLine as primary post-rock delay (EITS/TWDY/Sigur Rós targets);
  **Chords of Orion** — the silent-loop + Ice-swell drone method. *(native-suns, chords-of-orion)*
- **Jonny Greenwood / Bon Iver** — real sightings but illustrative-of-ubiquity, not deep signature
  uses (Greenwood swapped his for a DD-200 quickly). *(greenwood-bon-iver)*

---

## 5. Rig-specific recipes

- **Clock master from the Digitakt:** adopt DeHove's globals (BPM, **MIDI Clock Reset OFF**, Tap=Global)
  → every preset follows the Digitakt tempo. *(richard-dehove, morningstar-midi-clock-tap)*
- **Dotted-eighth + eighth with the Big Time:** set the TimeLine's **B side to dotted-eighth** (per-
  preset Tap Division), run the Big Time at the eighth off the shared clock — the rig's U2-style trick. *(sam-wittek)*
- **Banjo-as-lead pad:** **Ice** (upper voice a 5th above root, smeared) **swelled in with volume** +
  **HP ~80–160 Hz** so bright banjo repeats don't ice-pick; or a silent-loop drone. *(chords-of-orion, mscarney302)*
- **Baritone degraded wall:** **dTape** (Wow&Flutter up, Tape Age CW, longest time + high repeats) for
  the seasick shoegaze smear; **dBucket Double** for warmer repeats that don't fight the lows. *(chords-of-orion, richard-dehove)*
- **Runaway grit:** put a fuzz in the **feedback-loop insert** so every repeat re-degrades. *(community-hidden-features)*
- **Wash-on-wash (Hammock):** place the TimeLine **after the Big Sky / H90** and ride the Lo-Fi knobs. *(hammock-timeline-lofi)*
- **Feed it at the right level:** the VG-800's hot line-level output can distort/drop a channel —
  go through the **EHX Effects Interface** (the rig already does this). *(community-gotchas)*

---

## 6. Best learning resources

- **Richard DeHove** (intelligent-machinery) — *the* TimeLine educator: the 65-min complete walkthrough
  (globals + all 12 machines with values) + the looping-in-perfect-sync tutorial (MIDI-note control).
- **Chords of Orion** — ambient/drone method (silent-loop + Ice swell + dTape Frippertronics).
- **Rhett Shull** — 5 practical delay tricks (fake chorus, sub-audible solo delay, self-oscillation).
- **Sam Wittek** — preset-organization strategy (the brightness/subdivision ladder).
- **Strymon "This Week's Preset"** (free `.syx` + settings images) and the **factory-preset PDF** — the
  best concrete recipe sources; **Nixie 2** is the librarian.
- **Communities:** the **Morningstar forum** (the richest MIDI-clock lore) and **Strymon firmware release
  notes** (settles old-vs-new "bugs"). TGP paywalled; Reddit doesn't index to search. *(richard-dehove, chords-of-orion, rhett-shull, sam-wittek, strymon-twp-index, morningstar-midi-clock-tap, strymon-firmware-release-notes)*

---

## 7. Common pitfalls / gotchas

- **5-second spillover rule:** trails only spill if a preset's been active ~5 s — fast stomps cut the
  tail; **Persist=ON forces buffered bypass** (no trails + true bypass together). *(community-gotchas, strymon-looping)*
- **MIDI clock / tap / preset-BPM conflict** — a global tap overwrites clock-following presets' saved
  tempos; fix with per-preset **MIDICL**. The TimeLine **never sends clock** (always slave). *(morningstar-midi-clock-tap)*
- **Power: 300 mA, never exceed 9 V** (won't run on some Voodoo PP2+ outlets). *(community-gotchas)*
- **Hot/line-level inputs distort/drop a channel** — use the EHX FXI for the VG-800. *(community-gotchas)*
- **Two-footswitch bank scrolling is awkward live** — use a MIDI controller / MultiSwitch. *(community-gotchas)*
- **Nixie needs a real MIDI interface** (no USB on the pedal); most plug-and-play interfaces fail. *(strymon-nixie-preset-sharing-import)*
- **Myth-busts:** the **"Golden Ratio" tap division is DIG-only, NOT on the TimeLine**; the circulating
  **"CC#97 = infinite repeats" is unverified** (it's a footswitch HOLD, not a confirmed CC). *(community-gotchas, strymon-midi-cc-map)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `richard-dehove-timeline-complete-walkthrough.md` — globals + all-12-machine starter build with values
- `richard-dehove-timeline-looping-in-perfect-sync.md` — MIDI-note looper control, clocked in sync
- `chords-of-orion-timeline-drone-machine.md` — silent-loop + Ice swell + dTape Frippertronics drone
- `rhett-shull-timeline-5-delay-tricks.md` — dotted-eighth, sub-audible solo delay, reverse, fake chorus, self-osc
- `sam-wittek-timeline-preset-showcase.md` — small/med/large + dotted-eighth/eighth preset ladder
- `mscarney302-timeline-dtape-dbucket-digital-settings.md` — A=quarter/B=dotted-eighth layout + HP-filter banjo note
- `matt-trojak-timeline-self-oscillation-demo.md` — self-oscillation across Digital/Analog/Tape (notes-only)

**Links** (`research/links/`)
- `strymon-factory-presets-full-list.md` — all 100 factory presets w/ exact settings + on-aesthetic subset
- `strymon-twp-corrupted-flowers-lofi.md` · `strymon-twp-bokeh-bells-dtape.md` — free `.syx` Lo-Fi/dTape presets
- `strymon-twp-index-and-video-presets.md` — "This Week's Preset" index
- `strymon-nixie-preset-sharing-import.md` — `.syx` sharing/import workflow
- `strymon-nixie-editor-librarian.md` — Nixie/Nixie 2 editor + MIDI-interface gotcha
- `strymon-looping-with-timeline.md` — looper modes, LP LOC pre/post, LPEXIT
- `strymon-firmware-release-notes.md` — full firmware rev history (old-vs-new)
- `strymon-midi-cc-map-looper-controls.md` — verified CC map + looper CCs
- `morningstar-timeline-midi-clock-tap-conflict.md` — per-preset MIDICL / tap-vs-clock fix
- `community-timeline-hidden-features-oscillation.md` — infinite-hold, feedback-loop insert, secondary params
- `community-timeline-gotchas-pitfalls.md` — power, spillover, MIDI, input-level, golden-ratio myth
- `community-timeline-u2-dual-and-ambient-recipes.md` — Edge/Streets Dual + Swell/Ice/Reverse recipes
- `hammock-timeline-lofi-ambient.md` — Hammock Lo-Fi knob-riding + chain (after BigSky)
- `david-helpling-timeline-dual-modulation.md` — Dual L/R modulation approach
- `native-suns-timeline-postrock.md` — Jason Mays post-rock use
- `greenwood-bon-iver-timeline-users.md` — Greenwood/Bon Iver sightings (caveated)
- `timeline-preset-packs-paid.md` — paid pack survey

## Sources

Video (YouTube): Richard DeHove `rUkuktFkSLw`, `FwxTZfshTDs` · Chords of Orion `ZZNukHx6vL0` · Rhett
Shull `v8Kbmcvnmf0` · Sam Wittek `V1MkMQBKNN4` · mscarney302 `T8DoWR1IUeE` · Matt Trojak `SsjFr5Eju4w`.
Official: strymon.net (TimeLine product, looping guide, firmware release notes, factory-preset PDF,
"This Week's Preset", Nixie 2 support) · midi.guide/d/strymon/timeline.
Community: forum.morningstar.io · thefretboard.co.uk · seymourduncan · TGP (paywalled).
Artists: strymon.net pedalboard features (Hammock, Helpling, Native Suns) · thekingofgear.com (Greenwood).
