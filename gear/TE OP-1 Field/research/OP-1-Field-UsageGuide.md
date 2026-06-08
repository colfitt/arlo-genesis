# TE OP-1 Field — Usage Guide

In this rig the OP-1 Field is **not** a live guitar processor — it's the portable
sketchpad and the sampler/mangler that *feeds* the boards. You get the most out of
it two ways: build or sample a sound on-box (banjo roll, baritone drone, a found
sample) and degrade it on tape, then either bounce the sketch out **OP-1 → EHX
Effects Interface → Board 1** to fuzz it, or play it back as a chromatic
instrument. Treat it the way Shane Becker and Andreas Roman do — **OP-1 as the
DAW**, with real instruments and boutique pedals feeding in, not the other way
round.

> ⚠️ **Firmware note (this doc vs the dossier):** the `*-DeepResearch.md` dossier is
> keyed to manual OS 1.5.7 and says tape is "destructive-ish, no real undo." Later
> firmware **added tape UNDO (7 levels) + REDO, a metronome COUNT-IN, and a new
> "amp" synth engine** (amp/comp/tone/distortion + tuner + phaser, works on any
> input incl. the mic). Those are used throughout this guide. The dossier's §4 was
> patched to match (2026-06-03); §11's "no project recall" is still correct, since
> undo ≠ recall. *(source: `ollieloops-...tape-workflow`)*

---

## 1. Essential workflows

### The 4-track tape
- **Overdub stacks, it doesn't overwrite** — record 2–3 guitars onto one track to
  free the others. Tape is the "uncut gem." *(ollieloops)*
- **UNDO / REDO (new):** hold `[Tape]`+LEFT to undo (7 levels), `[Tape]`+RIGHT to
  redo. This changes the risk math on every destructive move below. *(ollieloops)*
- **Land on beat 1, two ways:** *record-on-note* — hold `[Record]`, then play a
  note and recording starts on that note (tight downbeats); or *count-in* —
  `[Shift]+[Record]` to arm, `[Play]` for a 4-beat count. *(ollieloops)*
- **Loop a section to build a song:** preset `[3]` toggles looping; `[Shift]`+arrows
  scrub a snapping grid; preset `[1]` = loop in, `[2]` = loop out; `[Shift]+[Stop]`
  cycles grid resolution (whole→½→¼→⅛). Work in 4-bar sections. *(ollieloops)*
- **Edits:** `[Lift]` removes + copies to buffer, `[Drop]` pastes at the playhead
  (repeatable); scissors `[Split]` to chop; `[Shift]+[Lift]` lifts all 4 tracks;
  **lift-then-drop onto a track = merge down**; `[Shift]+[Split]` merges tape
  pieces. *(ollieloops)*
- **Character is baked in AT RECORD TIME.** Vintage/Porta/MiniDisc colour is applied
  only while recording — to get Porta wobble you must *record* to the Porta tape;
  lifting Porta audio onto a Studio reel keeps the wobble. A project commits to one
  tape style (can't swap mid-project), and **each overdub pass stacks more noise.**
  Preview the noise without recording via `[Shift]+[Record]+[Stop]`. *(adg, loopop)*
- **`[Shift]+Orange` sets the record PAN to tape** — record a mono source hard-L on
  one pass, hard-R on a second, and two mono takes become a wide stereo double.
  Rig-native for the baritone/banjo. *(github-ratbag98-op1tips)*

### Bounce / merge all 4 tracks → 1 (three methods)
1. **Resample to a tape track** (easiest): `[Shift]+[Lift]` all 4 (drops a backup),
   MUTE the destination track, set record source to the **EAR** icon, record+play.
   Turn DOWN master overdrive/comp first or it re-stacks. *(gavinvickery)*
2. **Lift → DRUM sampler** (cleanest, gives a backup): extend the loop into an empty
   bar for a clean tail, lift, drop on the first key — comes out quieter, so bump
   sample volume **+8** to match. ~20 s cap on the Field. *(gavinvickery, sonwu)*
3. **Album → loopback** (long ambient material only): `[Com]` → record album → loop
   it back to tape. Timing alignment is painful — avoid for drums. *(gavinvickery)*

### lift/drop sampling + building drum kits (Cuckoo's canonical method)
- **Synthesize each drum on-box, then sample the row.** KICK = Phase engine, very
  short snap + Nitro filter low + **Unison** for fatness; SNARE = same, Nitro shifted
  up; HAT = Digital engine's noise played in the 4th octave; tuned perc/gong = Face
  engine; bass = Cluster; a usable acoustic-ish noise lives in the **String engine in
  Unison, tuned up.** Record them in a *tight row* on tape (≤20 s Field). *(cuckoo)*
- **Sample the row in:** FADE off, source = **EAR** (not the mic → feedback), hold
  the sample button + play the tape. Trim slices to **zero crossings** (low levels
  aren't silent — Nitro is noisy). *(cuckoo)*
- **Double-compression gotcha:** sounds are recorded with master-comp settings, then
  hit the comp *again* on playback. Watch levels. *(cuckoo)*

### The two samplers (Field specifics)
- **Synth sampler:** one note → chromatic across the keys (original pitch maps to the
  held key — play C while holding C). Loop start/end for infinite sustain;
  `[Shift]+GRAY` crossfade to de-click the loop. No time-stretch (pitch up = shorter).
  `[Shift]` = reverse / volume / tune. *(sonwu)*
- **Drum sampler:** records ≤20 s, **auto-slices into 16 (lower keys) + 8 (upper,
  2× longer)** — record an in-time 4-bar loop so slices land on the grid. Per-slice:
  pitch, start/end, play modes (hold / play-to-end / **choke group** via arrow+G /
  loop), attack (de-click). Last knob = pan (L/R) **or** `[Shift]`-press → **A/B
  stack-morph** between two layered samples (drum-sampler only). Press the **BLUE
  encoder to ZOOM** the waveform. *(sonwu, adg)*

### The sequencers (what each is actually for)
- **Arpeggio** — more than an arp: trigger modes add chord tones, trigger pattern
  inserts rests or skips steps, swing; change note value *while recording* for
  morphing hats. *(digiphex, ollieloops)*
- **Endless** (SH-101-like, 128 steps) — `[Shift]`+keys to enter, arrows = rests,
  play forward/reverse/random. A single note here = play any one-shot **chromatically**
  (banjo roll → playable instrument). *(digiphex)*
- **Finger** (14 patterns, 2-note) — each key is its own sequence; play two together
  for an emergent 3rd sequence; works for drums too. *(digiphex)*
- **Pattern** (16 steps) — triggers on vertical lines; `[Shift]`+orange = forward /
  forward-back / reverse. *(digiphex)*
- **Sketch** — draw lines (horizontals play); shake to erase. *(digiphex)*
- **Tombola** — physics: drop note-balls, set hexagon speed + ball weight, release via
  GRAY; `[Shift]+blue` = hand crank. Great on FM bells. *(digiphex)*
- **Hold (new)** — really a performance tool: set a break point, latch notes below it
  as a **drone** while you solo above; GRAY transposes the held chord in key. Poly or
  mono. *(adg, loopop)*

### Field-only connectivity tricks
- **USB-C as HOST:** powers + connects an external MIDI controller directly (tested:
  Launchpad Pro, KeyStep). **Velocity** from external MIDI works even though the keys
  aren't velocity-sensitive — route the **velocity LFO to filter cutoff** so harder
  hits open up. *(loopop)*
- **FM:** press the radio encoder IN to auto-seek; the FM TX broadcasts the OP-1's own
  name as the station. Bare radio is weak — plug any cable into OUT as a transmit
  antenna, or into REC IN for reception. *(adg, op-forums-fm-transmitter)*
- **out-in loopback** is a valid input source for on-box resampling; **USB input**
  samples a computer/TX-6 over USB-C. *(adg)*
- **Disable charging** (press the orange knob on the Com page) to kill ground-loop
  noise when plugged in. *(adg)*

---

## 2. Signature patches & settings

**Cuckoo "Opines Collection"** (op1.fun, free) — 15 patches, all 13 synth patches on
the **DR Wave** engine, chiptune-flavoured. Verified per-patch from the op1.fun UI:
- `slot_piano` — DR Wave, oct +1, **delay + random LFO**
- `paper_keys` — DR Wave, oct 0, **spring reverb + value LFO**
- `plinka` / `feena` — DR Wave, oct 0/+1, **delay + tremolo**
- `bass_buzzer` / `brinsting` — DR Wave, **oct -2** (basses)
- `opines_a` / `opines_b` — drum kits on the **DBox** physical-model drum synth
- **Pattern to copy:** delay is the default FX; tremolo/value/random LFOs; basses at
  oct -2, leads at +1. *(op1fun-cuckoo-opines-collection)*

**Real dumped parameter sets** (from teoperator's source — actual extracted patches,
usable as starting points if you build/import via the tools in §6):
- *Cluster:* `adsr [64,64,0,64,14336,64,4000,4000]`, `fx_type nitro`,
  `fx_params [64,-14337,4515,7232,0,0,0,0]`, `knobs [3072,0,512,3,0,0,0,0]`,
  `lfo_type value`.
- *Sampler:* `adsr [64,10746,32767,10000,4000,64,4000,4000]`, `base_freq 440.0`,
  `fx_type delay`, `lfo_type tremolo`.
- *Drum kit "boombap1":* `drum_version 2`, 24-element `start/end/pitch/playmode/volume`
  arrays (8192 = neutral). *(op1-patch-file-format)*

**Honesty flag:** op1.fun's web UI exposes engine / octave / FX type / LFO type per
patch but **not** the numeric `knobs`/`adsr`/`fx_params` arrays — those only come from
downloading the `.aif` and running `op1-dump`. The format is documented in §6 so you
can extract any patch's exact values yourself; we did not bulk-dump the library.

**On-box FX recipes** worth saving as user patches: chorus = CWO freq 0 / delay 28 /
fb 15 + value LFO; SP-303-style vinyl = master Drive max + Punch (power 99, punch 0,
rounds 5); a "free" fake delay (saves the one FX slot) = Tremolo LFO 100 % square on a
percussive sound. *(github-ratbag98-op1tips)*

---

## 3. Power-user tips, tricks & hidden features

- **TE-Boot menu:** hold `COM` while powering on = firmware/reset; `[Shift]+COM` on
  boot = diagnostics (Shift-2 motherboard test, Shift-3 colour-bar/loopback).
  *(github-thie1210)*
- **`[Shift]+Tape` = ERASE tape** — destructive; know it so you don't fire it by
  accident (undo now covers most slips, but not a full erase confidently).
  *(op-forums-all-key-combinations)*
- **Stereo drums (Field-only): `[Shift]+Ochre`** opens stacked channels A and B —
  load two different samples into one stacked kit (e.g. a banjo one-shot + a
  fuzz-wall hit). *(musicradar-8-ways)*
- **Chromatic one-shots:** Endless sequencer with a single note plays any one-shot
  across the keys. *(github-ratbag98-op1tips)*
- **G-sensor modulation:** Element LFO, G-force source, depth ±100 → tilt the unit to
  modulate. *(github-ratbag98-op1tips)*
- **Armed/paused record:** `[Shift]+Rec` arms with the reels paused so you can switch
  modes before pressing Play. *(github-ratbag98-op1tips)*
- **Wireless sampling:** broadcast a phone/computer through a cheap FM transmitter,
  sample it off the OP-1's receiver — cable-free capture. *(op-forums-fm-transmitter)*
- **Detune for fake-analog drift:** `[Shift]+Tempo` detunes in cents; double a track
  slightly detuned to thicken like a second oscillator. *(github-ratbag98-op1tips)*
- **Preserve EQ on copy/paste:** include an empty (silent) track in the loop selection
  before copying, then `[Shift]+paste` — otherwise EQ is dropped.
  *(github-ratbag98-op1tips)*
- **New "amp" engine:** amp/comp/tone/distortion + tuner + phaser, works on *any*
  input including the mic — i.e. on-box grit before anything leaves the unit.
  *(ollieloops)*

---

## 4. Notable users & techniques

- **Shane Becker** (@shanebeckermusic) — the studio's reference. Thesis stated in
  nearly every post: **"OP-1 Field as the DAW."** Builds whole tracks in/through it:
  records himself with a **TP-7** field recorder then pitches/flips the sample on the
  OP-1; mics real drums/vocals with the **built-in mic** *or* a **CM-15** condenser,
  both often "run thru the clean and MOOD" (Chase Bliss MOOD); plays Prophet 6 / Juno
  / DX7 for chords+bass (bass distorted with a Nudistort, chords summed through a
  Franklin SS-6); guitar goes through a **Hologram Chroma Console** + drive *before*
  the OP-1, with heavy gated reverb + chorus as treatment. *Caveat:* this is distilled
  from his reel **captions** — the on-box button-level technique (which engines/
  sequencers) is not visible in what we could capture. *(shanebecker-op1-workflow-distilled)*
- **Justin Vernon / Bon Iver (*22, A Million*)** — the canonical capture-and-mangle
  blueprint: radio sampling (WCFW 105.7), a sampled cymbal-scrape one-shot "played at
  different pitches," a sped-up choir sample as a reverb wash, songs built around
  deliberately "cruddy" OP-1 samples. *(bon-iver-justin-vernon-op1-techniques)*
- **Andreas Roman** (made a full album on the Field) — **most rig-relevant:** one-note
  polyphonic sampling (single C3 → played polyphonically), Studio-tape capture then
  re-print to Vintage/cassette, **Tombola on FM bells**, and sending audio out to
  **Chase Bliss MOOD / Blooper + Generation Loss MkII** then resampling — the exact
  pedals in this rig. *(cdm-op1-field-album-workflow)*
- **Hainbach** — "super Casio SK-1"; degrades the source on tape/mic *before*
  sampling; composes parts imagining the half-speed result.
  *(op1-demo-educators-hainbach-cuckoo-rmr)*
- **Cuckoo & Red Means Recording (Jeremy Blake)** — the defining educators; Cuckoo's
  sampler-as-synth-cloner packs (e.g. "OP-6" = 40 patches sampled off an OB-6), RMR's
  full-sketch-on-tape workflow + his Field packs. *(op1-demo-educators-hainbach-cuckoo-rmr)*

---

## 5. Rig-specific recipes (using gear actually owned)

- **OP-1 → EHX Effects Interface → Board 1 (the headline trick, now confirmed
  correct).** Community testing shows the OP-1's OUT is **line level**, so straight
  into a fuzz it goes "farty/muddy/quiet" — you need a line→instrument box, and the
  **EHX Effects Interface is exactly that.** Keep it stereo, pad the level into the
  fuzz. Then layer the **new amp engine** for *two stages* of grit (amp engine on-box
  → MXR M108 / EAE Longsword on the board) for the "recorded-wrong" wall.
  *(op-forums-op1-into-guitar-pedals, ollieloops)*
- **Generation-loss loop:** record the banjo/baritone to a **Porta** tape (warmth +
  wobble baked in) → `[Lift]` → drop into the synth or drum sampler → re-record. Undo
  now lets you take risks while stacking degradation passes. *(cuckoo, adg, ollieloops)*
- **Banjo-as-keyboard / 808:** sample an EBM-5 banjo roll into the **synth sampler**
  and play it chromatically (dossier §13a); or drop a single roll loop into the
  **drum sampler** and let the auto-16-slice carve it. *(ollieloops, sonwu)*
- **Banjo drone bed for doom:** the **Hold** sequencer latches a low note as a drone
  while the banjo is played as a lead on top — fits "banjo-as-lead / sustained walls."
  *(adg, loopop)*
- **Varispeed doom / mickey-mouse:** tape-reel white-knob `-1` for a sub-octave dark
  drone on a baritone, `+1/+2` for sped-up textures. *(liamkillen)*
- **Wide stereo double:** `[Shift]+Orange` pan + two mono passes of the same
  baritone/banjo part (hard-L, hard-R). *(github-ratbag98-op1tips)*
- **Run it as a 44.1 k interface into the Apollo/Babyface**, not over USB into the
  Elektrons (see §7). As a *device* it's a clean 2-in/2-out — the reliable capture
  path. *(op-forums-op1-field-usb-c-audio-what-works)*

---

## 6. Best learning resources

**Video channels**
- **Cuckoo (True Cuckoo)** — definitive OP-1 educator; on-box sound design / building
  kits from synth engines. Mostly OG-era but technique transfers.
- **Ollie Loops** — *current (2026)* and Field-specific; best modern tape workflow +
  the new amp engine + undo/count-in.
- **ADG** — most exhaustive Field walkthrough (~71 min); tape styles, baked-in
  behaviour, input/album/loopback, connectivity.
- **loopop** — the definitive analytical review; stereo, limitations, "where it fits."
- **SON WU (Sam Woo)** — clean modern Field tutorial series (samplers, engines).
- **Gavin Vickery** — concise practical technique (the 3 bounce methods).
- **Liam Killen** — loose/degraded sampling ethos; OP-1-as-sketch.

**Communities & references**
- **op-forums.com (the op1.fun forum)** — the central, deepest community; the "Tricks
  and Tips" subforum is the canonical knowledge base.
- **github.com/ratbag98/op1tips** — distilled, searchable digest of the giant tips
  megathread; best single starting point.
- op-forums threads: **All Key Combinations** (t/4338) · **Tape Track Bouncing
  Megathread** (t/18951) · **OP-1 Field Workflows** (t/24567).
- **thie1210 troubleshooting gist** — won't-charge/boot/reset survival doc.

**Patches & tools**
- **op1.fun** — the patch/drum/synth hub; download `.aif`, load via disk mode or the
  op1.fun Mac menubar app, or audition via Web MIDI.
- **Patch format + extraction tools** — libop1 / `op1-dump`, teoperator, op1tools
  (read the exact numeric params out of any `.aif`). *(op1-patch-file-format)*
- TE official sound packs; op1.center; SoundGhost (Field).

---

## 7. Common pitfalls / gotchas

- **USB-C audio is 44.1 kHz ONLY — no 48 k.** This breaks clean interop with the 48 k
  Elektron gear over USB; plan digital sessions at 44.1 k or capture via analog/the
  interface instead. **Key constraint for this rig.** *(op-forums-op1-field-usb-c-audio-what-works)*
- **USB host audio is one-way** (as host it receives in, can't send out — no
  bidirectional OP-1f↔OP-Z). As a *device* into Logic/Live/iPad it's a normal
  2-in/2-out. *(op-forums-op1-field-usb-c-audio-what-works)*
- **Can't reliably charge AND pass MIDI on the single USB-C port.** Run on battery
  (~24 h) with USB-C for MIDI, or use a USB-C→TRS MIDI adapter to free the port for
  charging. *(op-forums-op1-field-power-and-midi-over-usb-c)*
- **OP-1 OUT → guitar pedals is a line-vs-instrument mismatch** → use the EHX Effects
  Interface (see §5). Raw, fuzz sounds bad. *(op-forums-op1-into-guitar-pedals)*
- **OP-1 as a *live* guitar-FX processor is weak** (one FX slot, rigid) — process
  guitar in the pedals; use the OP-1 to sample the wall and as a source.
  *(op-forums-op1-field-as-pedal-for-guitar)*
- **Sampler bounce length cap ~20 s (Field)** — a multi-minute tape won't fit a
  sampler bounce. *(gavinvickery)*
- **Double compression** on sample-in (master comp at record + comp again on
  playback) — trim levels. *(cuckoo)*
- **Tape character can't be changed after recording, and every overdub stacks noise.**
  Commit to the right tape style up front. *(adg, loopop)*
- **Field-incompatibility:** some original-OP-1 patches won't load on the Field
  (~7 synth patches in RMR Vol.1 fail). *(op1fun-rmr-pack-vol1)*
- **Battery:** a drained Li cell can read as "won't turn on" — leave it on USB,
  powered off, for hours; TE says recharge at least every 6 months. *(github-thie1210)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `ollieloops-op1-field-improved-tape-workflow.md` — current Field tape workflow + new undo/count-in/amp engine
- `adg-op1-field-full-walkthrough-for-owners.md` — exhaustive feature walkthrough; tape character, input/album/loopback, Hold seq
- `loopop-op1-field-review-vs-laptop-og-mpc.md` — definitive review; stereo, tape styles, limitations
- `sonwu-op1-field-sampler-engine-tutorial.md` — every parameter of the synth + drum samplers (Field)
- `digiphex-op1-field-sequencers-tutorial.md` — all sequencers (arpeggio/endless/finger/hold/pattern/sketch/tombola)
- `gavinvickery-op1-3-ways-bounce-merge-tracks.md` — the 3 bounce/merge methods + gotchas
- `cuckoo-op1-drumkit-build-and-sample-tutorial.md` — build-a-kit-on-box-then-sample-it (canonical)
- `liamkillen-op1-sampling-combining-processing.md` — loose sampling / groove technique
- `shanebecker-ig-reel-*.md` (×7) + `shanebecker-yt-*.md` (×2) — his OP-1 reels/videos (captions/desc captured; frames need direct view)

**Links** (`research/links/`)
- `op1-patch-file-format.md` — full `.aif`/`APPL`/JSON patch format + extraction tools
- `op1fun-library-and-import.md` — op1.fun overview + 3 import methods
- `op1fun-cuckoo-opines-collection.md` — 15 named patches w/ engine/octave/FX/LFO
- `op1fun-rmr-pack-vol1.md` — RMR pack contents + Field-incompatibility note
- `te-official-soundpack-install.md` — official drag-drop install steps
- `op1-patch-sources-to-follow.md` — annotated patch-source index
- `op1-demo-educators-hainbach-cuckoo-rmr.md` — Hainbach/Cuckoo/RMR techniques + packs
- `bon-iver-justin-vernon-op1-techniques.md` — Vernon's sampling techniques
- `cdm-op1-field-album-workflow.md` — Andreas Roman full-Field album workflow (→ Chase Bliss/Gen Loss)
- `op1-field-tips-shortcuts-graham-english.md` — save/rename/import/tape shortcuts
- `github-ratbag98-op1tips-distilled.md` — distilled hidden-feature/tape/sampler/FX combos
- `op-forums-all-key-combinations.md` — full shortcut reference incl. hidden/destructive combos
- `op-forums-tape-track-bouncing-megathread.md` — all bounce/merge methods + gotchas
- `op-forums-op1-field-workflows-tips.md` — Field-specific workflows (pan-to-tape, MIDI sync)
- `op-forums-op1-into-guitar-pedals.md` — line/instrument fix (validates the EHX FXI path)
- `op-forums-op1-field-as-pedal-for-guitar.md` — guitar IN → OP-1 as FX (verdict: don't)
- `op-forums-op1-field-usb-c-audio-what-works.md` — USB-C audio compat + 44.1k-only gotcha
- `op-forums-op1-field-power-and-midi-over-usb-c.md` — charge-vs-MIDI conflict + workarounds
- `op-forums-fm-transmitter.md` — FM TX weakness + antenna/wireless-sampling hacks
- `github-thie1210-op1-troubleshooting.md` — TE-Boot, charge/boot recovery, battery recalibration
- `musicradar-8-ways-op1-field.md` — Field-only tips from TE (stereo drums, Mother reverb)
- `shanebecker-profiles-index.md` · `shanebecker-op1-workflow-distilled.md` · `shanebecker-soundbetter-profile.md` · `shanebecker-jerseyindie-interview.md` — Shane Becker enumeration + distilled workflow + gear/credits

## Sources

Video (YouTube): Ollie Loops `tW5IOnCLTyg` · ADG `AYXjDsDSyK8` · loopop `eR9dbJ5DreM` ·
SON WU `md2Ecg8G6pI` · Digiphex `tod6GrSDsc8` · Gavin Vickery `6JJB1C14_ro` · Cuckoo
`vJwU8utM7iE` · Liam Killen `mNorFB_0q1o`.
Community: op-forums.com (t/4338, t/18951, t/24567, t/2837, t/24829, t/22655, t/25896,
t/22785) · github.com/ratbag98/op1tips · gist thie1210 · musicradar.com/news/8-things-op-1-field.
Patches/tools: op1.fun · github.com/blattm/op1tools · github.com/padenot/libop1 ·
schollz.com/posts/op1 · teenage.engineering/downloads/op-1/sound-packs.
Artists: soundonsound.com (Bon Iver *22, A Million*) · cdm.link (Field album review) ·
perfectcircuit.com (Field review) · instagram.com/shanebeckermusic ·
soundbetter.com/profiles/469950-shane-becker · jerseyindie.com.
