# Chase Bliss Blooper — Usage Guide

The Blooper is the End board's **looper that ages and degrades** what you feed it — a
"bottomless" looper whose Modifiers, Stability, and additive overdubbing turn a banjo or
baritone phrase into an evolving, tape-worn wall. It's **mono**, so the **Chroma Console
right after it re-expands the loop to stereo** before the reverbs. Get the most out of it by
working the **NORM → ADD** flow (arrange clean, then commit/age), exploiting the
**two-headed-anomaly** mental model to place modifiers precisely, and **clock-syncing it to
the Digitakt** so loops never drift. Channel the co-developer **Andy Othling**: commit
deliberate, separate layers and resample across generations for degradation.

> Firmware: the alternate-bank modifiers (Stretcher, Pitcher, Chromatic Speed, Stopper, etc.),
> the **BLIP** interface, **Additive Assist**, and the **Stability slider** arrived in
> **v3.0 (~March 2021)**; current public build is **v3.2**. A pre-2021 unit has only 8
> modifiers until reflashed. *(elektronauts-blooper, firmware-3-tutorial)*

---

## 1. Essential workflows

### NORM vs ADD (the central concept)
- **NORM:** modifiers + Stability act like *external* pedals after the loop — heard but **not
  baked in**; a clean loop waits underneath. **ADD:** they're inside the feedback loop and
  **get recorded.** Arrange in NORM, flip to ADD only to commit/age. *(knobs-normal-mode, knobs-additive-mode)*
- A **layer commits on the record→playback transition** — "whatever you hear when you press
  play becomes the layer." *(knobs-layers)*

### The two-headed anomaly (place modifiers precisely)
The **record head is always steady; time-based modifiers move only the play head** — so
overdubbing under a time modifier records a *different* part of the loop than you hear.
- **Time-based** (desync the heads): Speed, Trimmer, Stutter, Stretcher, Scrambler, tape-stop.
- **Non-time-based** (heads stay locked — safe to overdub under for pure color): **Dropper,
  Swapper, Filter, Pitcher**, Stopper-fade. Use **Pitcher** as the "safe zone." *(recording-with-modifiers)*

### Printing modifiers cleanly
- **One-shot:** briefly hold the record footswitch → overdubs exactly one loop length, then
  auto-stops and turns the modifier off. **Punch-in:** start overdubbing → briefly engage a
  modifier → stop (audio only changes while engaged) — "great for placing unique moments and
  blips." *(recording-with-modifiers, knobs-footswitches)*
- **Additive Assist** (BLIP toggle): resets the play head when the record head loops, so the
  loop **previews exactly what a one-shot will commit.** ON = predictable prints; OFF =
  happy-accident walls. *(recording-with-modifiers, firmware-3-tutorial)*

### Layers, scenes & delay
- **8 levels of undo/redo** on LAYERS; you can only peel from the **top** of the stack.
  Navigating back + pressing record **erases everything above** (use it to fork). *(knobs-layers)*
- **Loop Capsules:** turn Repeats down so old material fades, record an idea, play (commits an
  unrelated layer) → build distinct scenes (C idea / G idea) and navigate with LAYERS; **ramp
  the LAYERS knob (random) to auto-shuffle** between captured ideas. *(knobs-layers)*
- **Blooper as delay:** Repeats ~50%, leave it recording — initial record = tap-tempo; delay
  up to the full loop length (~30 s); Repeats high = **Frippertronics** fade-looping. *(knobs-repeats)*

### Stability & Sampler
- **Stability** = the tape-aging engine; each additive pass ages more → **"mixed eras"**
  (vintage underneath, modern on top). The **BLIP Stability slider** dials noise content
  separately (pure wow/flutter ↔ full grit). *(knobs-stability, firmware-3-tutorial)*
- **Sampler/Carryover:** build a loop in NORM/ADD → switch to **SAMP** → retrigger (hold right
  = loop vs one-shot; hold left = momentary record). ⚠️ hitting record in SAMP wipes the loop. *(knobs-sampler-mode)*

---

## 2. Modifiers & signature recipes

**Modifier behavior (from KNOBs, the co-designer):**
- **Smooth Speed:** noon = STOPPED, CCW = reverse, extremes = octave up. **Stepped Speed** =
  quantized. **Dropper:** CW = consistent drop pattern, CCW = random, max = granular. **Stepped
  Trimmer:** shortens the loop (loops-within-loops); CW also time-stretches. **Scrambler** (KNOBs'
  favorite): jumps on a **16-slice grid** (stays rhythmic); knob = number of jumps. **Filter:**
  CCW = LP, CW = HP — **the HP is the more useful one for busy multi-layer loops.** *(knobs-modifiers)*
- **Alt bank (v3.0):** Stretcher (condenses → "hidden drums"), **Pitcher** (the overdub-safe
  pitch shift), Chromatic Speed, Stopper, Swapper. **Stretcher & Pitcher are mutually exclusive
  and don't combine with the Speed modifiers.** *(firmware-3-tutorial)*

**Copyable cheat-sheet recipes (official, verbatim):** *(blooper-modifier-cheat-sheet)*
- **GLACIER** (Smooth Speed near noon) — loop almost stopped → slowly shifting drone texture.
- **TAPE STOP** (Smooth Speed near real-time, engage → noon) — rubbery tape-halt.
- **CRUMBLE** (Dropper mild, ADD) — loop slowly falls apart over time.
- **DRONE PATTERN** (Scrambler on sustained chords) — chops a drone into a groovy pattern.
- **ROLLING CLOUDS** (Swapper right side, ADD) — soft swelling/fading landscape.
- **HIDDEN DRUMS** (Stretcher) — condenses a loop to emphasize percussive content.
- **STEP SEQUENCE** (Pitcher alt-bank, ADD on one tone) — one held note → a sequence/pad stack.
- **Chord from one root** (Chromatic Speed in ADD) — punch in major-3rd/5th/oct-down/reverse at
  spots → a strummed chord from a single baritone/banjo root note. *(knobs-modifiers)*
- **Filter + Stability** — narrows the band + adds resonance = compounding lo-fi.

**Presets store AUDIO, not knobs:** 16 loop slots (full layer stacks) recalled via **MIDI PC
0–15**; there is **no knob/dip "preset."** A "recipe" is a written mode+dip+modifier+knob
description (the cheat sheet is the canon). *(blooper-where-to-find-patches)*

---

## 3. Power-user tips, tricks & hidden features

- **Use the two-headed model as a tool:** want color without moving where you record? Overdub
  under **Pitcher / Dropper / Filter / Swapper** (non-time). Want to scatter placement? Use a
  time modifier. *(recording-with-modifiers)*
- **"All slow" (NORM):** record a loop, engage Stepped Speed at half-speed, overdub → the whole
  bed (incl. overdubs) plays at half-speed while your live playing up front stays full speed —
  unique to Blooper. *(recording-with-modifiers)*
- **Ramp the LAYERS knob (random)** to auto-shuffle between captured Loop Capsules — generative
  arrangement with no modifiers. *(knobs-layers)*
- **HP filter on busy loops** "opens things up" (KNOBs). *(knobs-modifiers)*
- **Stability slider (BLIP)** = aged-not-hissy walls (keep flutter, dial out white noise). *(firmware-3-tutorial)*

---

## 4. Notable users & techniques

- **Andy Othling (Lowercase Noises)** — THE Blooper artist (co-development + official "Office
  Hours" teaching). Principles: commit **deliberately distinct, separately-recalled layers**
  (re-tap, don't circle one layer); **pedalboard-as-DAW** with parallel loops; **multi-
  generational resampling/degradation** ("you're hearing the fourth sampling of it") — exactly
  this rig's aesthetic. Live recipes: filter-fade delay (Filter + ADD), pitch cascades
  (Chromatic Speed in ADD), SAMP momentary grabs. *(andy-othling-office-hours, andy-othling-sound-methods)*
- **KNOBs / Scott Harper** — co-designer, CB product-dev director; the "better bloops" video
  manual is the canonical reference. *(knobs-*)*
- *Honest gap:* beyond the design team + Andy Othling there's no marquee signature-Blooper
  record — its reputation is capability + the demo canon. *(blooper-where-to-find-patches)*

---

## 5. Rig-specific recipes & the CB-stack MIDI/clock ecosystem

### Blooper in this rig
- **Banjo/baritone drone wall:** record a sustained phrase → **GLACIER** (near-stop) or
  **Accumulation** (Stability up, keep overdubbing) for a tape-aging bed you can still play
  fresh notes over. *(blooper-modifier-cheat-sheet, recording-with-modifiers)*
- **Doom harmony from one note:** **Chromatic Speed in ADD** punch-ins build a chord from a
  single root — no second instrument. **Scrambler** turns a drone into locked rhythm. *(knobs-modifiers)*
- **Mono is fine here:** degrade/rebuild in the Blooper, let the **Chroma Console re-expand to
  stereo** before the H90. *(guitarpedalx-blooper-vs-mood)*
- **Bench the Onward:** Blooper's **Carryover/SAMP** covers one-shot/sampler duty. *(knobs-sampler-mode)*
- **Aged-not-hissy walls:** ride the **BLIP Stability slider**. *(firmware-3-tutorial)*

### CB-stack MIDI / clock / preset ecosystem  *(SHARED — reusable across all 7 Chase Bliss pedals)*
*Verified against each pedal's MIDI manual + midi.guide (`cb-stack-*` captures).*
- **Wiring:** CB pedals take MIDI on a single 1/4" **TRS jack, RING-active** (= MIDI TRS "Type
  B" mapping). The **Chase Bliss MIDIBox** converts DIN→ring-active TRS, drives up to **4
  pedals**, and **needs its own 9V** (the #1 gotcha). **Exception: the 2026 Big Time uses a
  native 5-pin DIN jack** (and can even be clock master) — connect Digitakt DIN → Big Time
  directly. *(cb-stack-midi-trs-and-midibox)*
- **Default channel = 2** for every CB pedal (change by holding both footswitches at power-up).
- **Clock-sync per pedal (verified):** **Blooper** (synced blooping — arms, starts on next
  pulse), **MOOD MkII** (delay/loop/ramp — **NOT in Synth Mode**), **Big Time** (delay
  subdivisions; can master), **Lost + Found** (gate/trem), **Onward** (GLITCH timing) all sync;
  **Clean** is feature-listed but **unconfirmed** at CC level; **Generation Loss MkII does NOT
  sync — PC/CC only, wow/flutter free-runs** (double-verified). **CC51 = universal clock-ignore**
  (0=ignore, >0=follow) on MOOD/L+F/Onward. *(cb-stack-clock-sync-per-pedal)*
- **One-PC whole-stack scene:** put the CB pedals on a **shared MIDI channel** and save the
  **same preset number** on each for a song → **one Program Change recalls the whole board**.
  (Use distinct channels instead if you want per-pedal CC automation.) Slots: 122 (Blooper/MOOD/
  L+F/Onward), 127 (Big Time), 2 (Gen Loss). *(cb-stack-preset-scene-recall)*
- **Shared CC map:** knobs CC14–20 (CC20=ramp), toggles CC21–23, footswitches CC102–106
  (bypass/engage), tap CC93, expression-over-MIDI CC100. ⚠️ **Dip switches are physical-only —
  NOT MIDI-addressable** (Bank A/B, Dry Kill, Play/Dub, CV-Clock are fixed-setup, not per-song
  recalls). *(cb-stack-preset-scene-recall, elektronauts-blooper)*

---

## 6. Best learning resources

- **Chase Bliss / KNOBs "better bloops"** — the 8-episode official video manual + the Firmware
  3.0 tutorial; demoed by the co-designer. The canonical how-to.
- **Andy Othling (Lowercase Noises)** — Office Hours streams; the ambient/drone Blooper voice.
- **Official docs:** the **modifier cheat sheet** (named knob-position recipes) + the
  **"Recording with Modifiers"** PDF (the two-headed model, one-shot/punch-in/accumulation).
- **Communities:** **r/blooper** (the hub, not r/chasebliss) and the **Elektronauts "Chase Bliss
  Blooper" thread** (best for the Octatrack/Digitakt crowd, MIDI reality, foot-control workarounds). *(knobs-*, andy-othling-*, blooper-cheat-sheet, recording-with-modifiers, elektronauts-blooper)*

---

## 7. Common pitfalls / gotchas

- **#1: Fixed loop length.** Once set, the loop container never changes — slowing playback loses
  half the content when committed; speeding up plays content twice within the container. (Upside
  here: synced loops never drift off the Digitakt clock.) *(guitartonepro-blooper-looping)*
- **Real loop time ~30–32 s**, not the marketed 40 s. *(guitarpedalx-blooper-vs-mood)*
- **Mono in/out** — re-stereoize downstream (Chroma/H90). *(guitarpedalx-blooper-vs-mood)*
- **Not a foot pedal** — it wants a tabletop; for gigs mount at hand height + drive the record
  footswitch with an external momentary. *(elektronauts-blooper)*
- **Dip switches aren't MIDI-addressable** — fixed-setup decisions, not per-song recalls. *(elektronauts-blooper)*
- **Erase-from-earlier-layer trap** — recording after navigating back wipes layers above. *(knobs-layers)*
- **Repeats fades only WHILE recording**, never during plain playback. *(recording-with-modifiers)*
- **Stretcher & Pitcher are mutually exclusive** and don't combine with the Speed modifiers. *(firmware-3-tutorial)*
- **Pre-v3.0 units** have only 8 modifiers + no Additive Assist/Stability-slider until reflashed. *(elektronauts-blooper)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `knobs-better-bloops-normal-mode.md` — NORM vs ADD (effects external vs baked-in)
- `knobs-better-bloops-additive-mode.md` — ADD mode, fixed-measure, precise glitch placement
- `knobs-better-bloops-modifiers.md` — all 6 default-bank modifiers, CW/CCW/noon behavior
- `knobs-better-bloops-stability.md` — Stability quadrants, additive aging, "mixed eras"
- `knobs-better-bloops-layers.md` — 8-layer undo/redo, Loop Capsules, ramp LAYERS
- `knobs-better-bloops-repeats.md` — Blooper-as-delay, Frippertronics, delay↔stutter
- `knobs-better-bloops-footswitches.md` — 5 footswitch commands, external switch, one-shot print
- `knobs-better-bloops-sampler-mode.md` — SAMP commands, Carryover
- `chase-bliss-blooper-firmware-3-tutorial.md` — v3.0 alt modifiers + BLIP + Additive Assist + Stability slider
- `andy-othling-office-hours-blooper.md` — Andy's live teaching (layering, Stability, pitch cascades, SAMP)
- `andy-othling-office-hours-blooper-vs-capistan.md` — rig/volume workflow, Blooper-vs-MOOD/Capistan degradation

**Links** (`research/links/`)
- `chasebliss-blooper-modifier-cheat-sheet.md` — official named knob-position recipes (GLACIER, etc.)
- `chasebliss-blooper-recording-with-modifiers-guide.md` — two-headed model, time-vs-non-time, one-shot/punch-in/accumulation/all-slow
- `blooper-where-to-find-patches-recipes-community.md` — where recipes live + the no-knob-presets caveat
- `andy-othling-sound-methods-ambient-technique.md` — Andy's looping/resampling/degradation philosophy
- `andy-othling-strymon-pedalboard-feature.md` — his ambient-looping method/pedigree
- `guitartonepro-blooper-normal-looping-gotcha.md` — the fixed-loop-length gotcha + plain looping
- `guitarpedalx-blooper-vs-mood-trifecta.md` — ~32 s real loop time, mono, not-a-foot-pedal, MOOD→Blooper
- `elektronauts-blooper-thread.md` — dip-switches-not-MIDI, foot-control workaround, firmware drift
- `cb-stack-midi-trs-and-midibox.md` — **[CB-stack]** ring-active TRS, MIDIBox, Big Time DIN exception, channels
- `cb-stack-clock-sync-per-pedal.md` — **[CB-stack]** verified 7-pedal clock table + CC numbers
- `cb-stack-preset-scene-recall.md` — **[CB-stack]** preset model, one-PC scene recall, shared CC/bypass map

## Sources

Video (YouTube): KNOBs "better bloops" `l9xfq38bTNc`, `YmwMDU2JdRM`, `f0HgKuovId0`, `fydnSMVtxSY`,
`-yAf4Y0lBvA`, `P3D5rqJa5Z0`, `TPlX1ehN5eE`, `Li5aLdOXxEI` · CB Firmware 3 `a_WeN71oAPA` · Andy
Othling `2oUlQwi4JRo`, `u02L-aiZ6Og`.
Official docs: blooper.chasebliss.com (modifier cheat sheet, recording-with-modifiers PDF,
resources) · chasebliss.com (MIDIBox).
Community: elektronauts.com (Chase Bliss Blooper t/76484) · r/blooper · guitartonepro.com ·
guitarpedalx.com · TGP / TalkBass (fetch-blocked, via cross-reference).
CB-stack MIDI: each pedal's official MIDI manual · midi.guide · Morningstar forum · Perfect Circuit.
Artists: andrewtasselmyer.substack.com · strymon.net (Andy Othling).
