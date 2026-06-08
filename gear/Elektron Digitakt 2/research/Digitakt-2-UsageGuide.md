# Elektron Digitakt II — Usage Guide

In this rig the Digitakt II plays two roles at once: it's the **groove/drum/sample
brain** that turns a sampled fuzz-wall, banjo run, or VG-800 texture into an evolving
sequenced part, *and* it's the **MIDI clock master** that drives the rest of the rig —
clock-syncing the Chase Bliss stack, sequencing the VG-800, partnering the Octatrack,
and streaming multitrack stems into Logic/Ableton over Overbridge. You get the most
out of it by leaning on p-locks + the three LFOs + conditional trigs for never-quite-
repeating drone/doom patterns, and by treating **resampling its own master output**
(through Grid-slice → Comb filter → bit-crush) as the on-box "recorded-wrong" engine.

> Scope note: this guide is for the **Digitakt II** (2024, stereo, +Drive, new FX).
> Where a technique originates on the **OG mono Digitakt** it's flagged *(OG)* with a
> note on whether it transfers. Features are tied to firmware where it matters — the
> box gained mono sampling, the playable Comb+ filter, and a key-tracking mod matrix
> in **OS 1.10**, and the manual **Slice machine** in **OS 1.15**.

---

## 1. Essential workflows

### Parameter locks (the core Elektron move)
- **P-lock:** in grid record, **hold a trig (don't release)** and turn any encoder —
  the trig blinks and locked param pages glow red. **Yellow blink = lock-only step
  (no note); red = note + lock.** Remove a lock: re-enter the step, or **hold `NO` +
  the locked encoder** to erase it. *(xnb)*
- **OS 1.10 — p-lock ALL active trigs at once:** hold a trig + press `TRACK` to add/
  remove a lock across every active trig (push the encoder to remove); per-page with
  hold + `PAGE`. Huge time-saver for dialling a whole pattern. *(davemech-os110)*

### Preset / sound locks (one track, many sounds)
1. Add presets to the **preset pool** (`PRESET` → manage → "Add presets to pool") so
   the samples preload for instant per-step switching.
2. **Hold a trig + turn the LEVEL encoder** to lock a different preset to that step.
   *(cuckoo, xnb; the OG equivalent is the "sound pool" workflow — nixienoise (OG))*

### Conditional & Euclidean trigs
- TRIG-page conditional knob: `1:2`, `1:4`, etc. for non-repeating loops. *(cuckoo, opto)*
- **New DT2 conditionals (not on OG):** **`NOT x:y`** (subtract trigs) and **`LAST` /
  `NOT LAST`** — `LAST` fires only on the final pass before a *queued pattern change*.
  Put fills/risers on `LAST`, the main groove on `NOT LAST`, and pattern transitions
  become hands-free. *Caveat:* step-1/2 trigs miss the cued pass — use a **pattern
  chain** for a step-1 riser. *(hexwave)*
- **Euclidean** (`FUNC`+`AMP`): two pulse generators + rotation (`ro`/`TRO`), combinable
  with **OR / XOR / AND / SUB** operators; bake to the grid with `FUNC`+EUC OFF. *(xnb)*

### Retrig & LFOs
- **Retrig** (TRIG page 2): toggle on, `RATE` = subdivision, `LEN` = step count, `VFAD`
  = −fade-out / +fade-in. *(xnb)*
- **3 LFOs per audio track** (2 per MIDI track). `DEST` → `DEPTH` (nothing happens till
  ≠0) → waveform. **Random waveform + the trig-restart waveform** for per-hit variation;
  set the modulated param to a mid value because random swings ±. Stack LFOs (e.g.
  LFO2 → `SRC TUNE`). *(cuckoo)*
- **OS 1.10 key-tracking mod matrix** (4 dests, ±depth scaled by note) → the **playable
  Comb+**: set Comb+ `FREQUENCY` as a key-track dest at **depth 8** so notes map to the
  12-tone scale and you *play* the comb filter. Excite it with a short "blip" sample;
  LP filter sets plucky↔stringy, feedback sets ring length. *(davemech-os110)*

### Resampling (the on-box mangle loop)
- **Sample the DT2's own master:** `SAMPLE` → clear buffer → scroll `INPUT` past L/R to
  **MAIN INPUT** (the master bus). Push it with **Master Overdrive** + the master
  compressor. Arm + record-on-play. **Disable OD/comp on later passes** so you don't
  stack them. *(opto-resampling)*
- **Capture a live performance:** `INPUT = MAIN`, sample `LENGTH = Max`, arm, `PLAY`,
  then twist controls live — it records all the motion. Then slice (Grid, 16 slices) +
  random LFO → slice-select + Comb/HP filter + bit-crush, and resample again. Iterate.
  *(opto-resampling)*

### Sampling architecture (new vs OG)
- **16 tracks, each freely audio OR MIDI** (vs the OG's fixed 8 audio + 8 MIDI). *(cuckoo, xnb)*
- **Set tempo BEFORE sampling** — it governs the tempo-synced machines. Record modes:
  **Threshold** (gate) vs **Play** (transport + pre-roll; hold `RECORD`+`PLAY` for a
  count-in). `FUNC`+`YES` previews the buffer, `FUNC`+`NO` clears it. *(opto-sampling)*
- **SAMPLE page `B` encoder = Stereo / L-R / Mono L / Mono R** — *mono sampling was
  added in OS 1.10*; the box launched stereo-only. *(davemech-os110, opto-sampling)*
- **SRC machines:** Oneshot (hits; lengthen track + AMP release to loop), **Werp** (warp,
  clicky on tonal), **Stretch** (time-stretch to tempo, some artifacts), **Repitch**
  (turntable, artifact-free), **Grid** (slices across the keys), **Slice** (OS 1.15). *(cuckoo, opto, xnb)*
- **Slice machine (OS 1.15):** `SRC`→Slice→`YES`→Create Slice Grid (e.g. 32) with
  **`DIRT` = transient/zero-cross detection** to kill clicks; dedicated editor (zoom,
  snap-to-zero-cross, split/remove); **trig-mode Slice** maps 16 keys to slices;
  **Create Linear/Random Locks** for instant rearrangements (amen→jungle). *(davemech-slices)*

### Send FX, drive & master compressor
- FX page per track = **Bit Reduction / Overdrive / Sample-Rate Reduction** + the 3 send
  levels. Send engines: widen/ping-pong the delay, lengthen reverb `DECAY` for "epic"
  tails. The dossier names them **Supervoid reverb / Panoramic chorus / Saturator
  delay** — videos treat them generically, so the dossier is the naming authority. *(cuckoo)*
- **OS 1.10 routing:** base-width filter **pre/post** main filter (fixes low-end
  buildup); **overdrive pre/post filter** (post = run a resonant filter *through* the
  OD). Comb+ (string-like) / Comb− (tube-like) filters added. *(davemech-os110)*
- **Master Compressor:** side-chain `SOURCE` = any track or ext L/R, side-chain HPF, and
  **compressor routing** (`FUNC`+setup) to include/exclude tracks — e.g. pump everything
  off the kick but exclude the kick itself; `NOT-COMP` inverts. *(cuckoo, xnb, opto)*

### +Drive sample management
- Two load paths: SRC sample-select (one slot) vs **`FUNC`+`SAMPLES`** batch (check many
  → Load to Project, target bank A–H; **OS 1.10: Load to Track N** directly). **Free
  RAM:** `FUNC`+`SAMPLES` → Project RAM → **Select Unused** → Unload. Rough figures: 20 GB
  +Drive, ~400 MB RAM, ~1016 sample slots, 2048 presets, 1024 kits. *(xnb)*

---

## 2. Signature sound-design & sound packs

**The on-aesthetic standout — DROWNED!** (boorch / Bruce Menace, Gumroad, 2024): **50
drone presets** each in Clean + "Headcrusher" variants + 50 stereo source samples. Built
exactly the way this rig wants: **slow LFOs → Filter (and sometimes Pitch), plus Random
LFOs with slow Slew** for unpredictability, Comb filter, stereo sources; the Headcrusher
tones are made by **resampling through a free Ableton rack**. DT2-native (OG gets the
samples only). *(elektronauts-drowned, elektronauts-generative-and-drone)*

**Official Elektron packs** (load via Transfer → +Drive): **Reduktion** (110 stereo,
most abstract/textural), **HexCells** (203 stereo + 86 DT2 presets, granular percussion),
**Drench Case** (Mick Harris — 261 mono industrial grit, loads on OG + DT2). *(elektron-official-packs)*

**Third-party:** **Broken FM** (Yves Big City — ~1 GB stereo DX7/Digitone FM one-shots +
400 glitch loops + 16 DT2 patterns) is the best metallic-drone source. *(isotonik-electronisounds)*

**EZBOT's generative-ambient recipe** (real values, full transcript captured):
- Track-scaling `reset = INFINITY`, scale = **harmonic minor**, keyboard fold ON.
- Wavetable on a **Grid machine, `GRID = 64`**, LFO → sample `START` to scan it.
- **7 trigs**, track **probability ≈ 20 %**; duplicate the track, offset one step, pan L/R.
- LFO: **`MULT 1`, `SPEED 16`, `TRIANGLE`, FREE-run → multimode-filter freq**; copy to
  track 2 at a different speed. FX: **delay ping-pong send ≈ 88**, **reverb send ≈ 90**,
  tempo **80 BPM**.
- Resample MAIN OUTS via `PLAY`-record (quantized from bar 1, captures FX), 4 bars →
  Repitch/reverse; two Oneshot copies looping + offset = **Steve Reich phasing**; bit/SRR
  reduction adds harmonics for crush. *(ezbot-recipe, ezbot transcript)*

**Amiva (minimalist):** no sequencer, one pattern, **AMP `DECAY = INF` on every track**,
trigger long samples by hand, and **route only through the reverb/delay sends (skip dry)**
for all-wet beds. *(isotonik-amiva)*

**Comb+ for banjo/strings (DT2-only):** `Comb+` is the filter that makes plucked-string/
harp tones; turn on **key-tracking (filter page 2)** so it tracks pitch — feed a real
banjo pluck through it for a detuned metallic resonator. Exact ADSR/feedback values
aren't posted; dial by ear. *(elektronauts-comb-filter, davemech-os110)*

---

## 3. Power-user tips, tricks & hidden features

- **Save a trig (with all its p-locks) as a Preset:** hold trig → `PRESET`/`KIT` → "Save
  new preset." Turns a crushed/filtered fuzz-wall step into a reusable instrument.
  *(elektronauts-tips)*
- **Preset Pool / Preset Keyboard mode** (`FUNC`+down → Preset Pool): play pooled presets
  across the trig keys, Octatrack-slots-style. DT2-only. *(elektronauts-overlooked)*
- **Step-record jump** (`RECORD`/`STOP`/`STOP`): auto-advances by trig length (1/4 lands
  on 1, 5, 9, 13) — ideal for laying out sample chains. *(elektronauts-overlooked)*
- **`LAST` / `NOT-LAST` auto-fills** for pattern-change transitions, leaving `FILL` free. *(elektronauts-overlooked)*
- **Selective USB audio output** — send only one track (a stereo pair or two monos) out
  for external FX/resampling. *(elektronauts-overlooked)*
- **Page loop / page mute** in grid record: hold `PAGE` → trigs 1–8 select, 9–16 mute. *(elektronauts-overlooked)*
- **Scale-constrained entry:** push DATA encoder A (`NOTE`) to step only in-scale; can be
  the default with push-for-chromatic. *(elektronauts-tips)*
- **128 steps = 64 steps at Speed ×2** ("d'n'b territory"); populate with the per-track
  Euclidean generator, then bake. *(elektronauts-tips)*
- **Fake chords** via `CTRL`-`SEL` multi-track editing (audio tracks are monophonic). *(elektronauts-tips)*

---

## 4. Notable users & techniques

- **Abre Ojos — "Travails"** (best rig analog): industrial doom-drone at **46 BPM**, DT2 +
  DSI Mono Evolver + Resolume. He **samples the mono Evolver into the DT2**, then uses the
  **Grid machine + Euclidean sequencing** to layer it into a "Poly Evolver" wall — exactly
  the move of sampling the baritone/banjo-through-pedals and Euclidean-sequencing the
  captures. *(matrixsynth-travails)*
- **EZBOT (Matthew Piecora)** — Seattle hardware educator; the go-to DT2 ambient + dub-
  techno source (DT2 + Digitone II + Octatrack-as-mixer). *(ezbot-recipe)*
- **Amiva (Alex)** — Elektron-spotlighted ambient producer; the INF-decay / all-wet
  manual-trigger method above. *(isotonik-amiva)*
- *Honest note:* the Digitakt II is young (2024) — there's no single canonical artist
  endorsement yet; these are the most *instructive* verified users.

---

## 5. Rig-specific recipes (using gear actually owned)

### The DT2 as the rig's MIDI / clock brain
- **Assign a MIDI track:** `FUNC`+`SRC` → SRC category → **MIDI** → `YES`. Each MIDI track
  sends a 4-note chord, PB/AT/MW/BC, and **16 freely assignable CCs** (VAL/SEL 1–8 on
  FLTR, 9–16 on AMP). **MIDI Learn:** hold `FUNC`+DATA on FLTR/AMP page 2, send a CC from
  the device, the slot captures it. *(rig-midi-tracks)*
- **Recall external presets in time:** drop a **trigless trig** and p-lock `BANK`/`SBNK`/
  `PROG` on it — that's how you fire VG-800 / pedal preset changes on a step. **Auto
  Channel** lets the Novation 61SL MkIII (or VG-800 pitch-to-MIDI) play the active track. *(rig-midi-tracks)*
- **Clock master:** `MIDI CONFIG > SYNC` → `CLOCK SEND` + `TRANSPORT SEND` ON. Chase Bliss
  pedals take **MIDI over 1/4" TRS** (TRS adapter or the CB MIDIBox). *(rig-clock-master-slave)*

**Verified clock-sync table** *(rig-clock-sync-pedals — checked against each maker's MIDI docs):*

| Device | Syncs to DT2 clock? | Notes |
|---|---|---|
| CB Blooper | ✅ | auto-adopts incoming MIDI channel |
| CB MOOD MkII | ✅ | ⚠️ clock ignored in **Synth Mode** |
| CB Big Time | ✅ | delay subdivisions |
| CB Lost & Found | ✅ | tap disabled while synced |
| CB Onward | ✅ | GLITCH timing |
| CB Clean | ✅ | Bounce/stereo modulation (exact synced params unconfirmed) |
| **CB Generation Loss MkII** | ❌ | **PC + CC only, NO clock** — wow/flutter free-runs; recall presets via PC, modulate via CC p-locks |
| **CB Brothers AM** | ❌ (n/a) | gain pedal, no time param; PC/CC use only |
| Strymon TimeLine | ✅ | delays sync per-preset (`MIDICL=ON`); ⚠️ **looper does NOT sync** |
| Strymon Big Sky | ✅ | Pre-Delay only (per-preset, fw 1.44+) |
| Eventide H90 | ✅ | Tempo Source = MIDI, per-program; DIN or USB |
| Hologram Microcosm | ✅ | auto-engages on MIDI Start; tap disabled while synced |
| Hologram Chroma Console | ✅ | DIN + USB-C MIDI (exact synced params unconfirmed) |

### Resample & mangle chains
- **Banjo/baritone → MAIN-INPUT resample:** print the Board-1 fuzz/banjo, resample the
  DT2 master through **Grid-slice → random LFO → slice-select → Comb filter → bit-crush**
  — the "recorded-wrong" finish without a computer. *(opto-resampling)*
- **Playable Comb+ banjo resonator:** key-track Comb+ at depth 8, excite with a short
  banjo-pluck blip; feedback = ring length → detuned metallic drones from one sample. *(davemech-os110)*
- **Ambient bed for the Apollo:** Stretch/Grid on a sustained baritone drone + slow random
  LFO → Comb filter + long Supervoid reverb send, single 128-step pattern. *(cuckoo, opto)*

### Hands-free live build-ups
- **`LAST` / `NOT-LAST` transitions** let the DT2 play its own fills on pattern change, so
  both your hands are free to ride the Microcosm / H90 / Chroma Console for the wall-of-
  sound build. *(hexwave)*

### Digitakt ↔ Octatrack & the DAW
- **DT2 = clock+transport master, OT = slave** (DT2 MIDI OUT → OT MIDI IN; OT
  `PROJECT>MIDI>SYNC` receive ON) — the DT2 carries per-pattern tempo the OT arranger
  doesn't. Audio: DT2 OUT → OT IN A/B; OT Thru/Flex/Pickup to live-mangle and sum to the
  Apollo. **Overbridge the DT2, keep the OT analog** (OT's OB support is thinner). *(rig-octatrack-combo)*
- **Overbridge into Logic/Ableton:** install the OB suite → DT2 `SETTINGS > SYSTEM > USB
  CONFIG > Overbridge` → drop the DT2 plugin on a track → enable sync + **PDC/delay
  compensation**. Streams **42 inputs** (Main L/R + 16 stereo tracks + 3 stereo FX busses
  + line-in). ⚠️ **Per-track stems are DRY (pre-send-FX)** — reverb/delay only via the FX
  busses or Main. ⚠️ Default DAW view shows only 15 of 16 tracks until you reassign
  outputs in the OB app. *(rig-overbridge)*

---

## 6. Best learning resources

**Video**
- **Dave Mech** — the most rigorous DT2 educator; free OS-update deep-dives (1.10, 1.15
  slices) + a paid course. Best for "exactly what each new feature does."
- **Cuckoo (True Cuckoo)** — definitive long-form beginner→intermediate walkthrough; best
  mental model of the memory/architecture.
- **XNB** — longest structured DT2 "course" (chaptered ~2 hr); best menu-by-menu reference.
- **Optoproductions (Melvin)** — short, practical sampling + resampling technique.
- **Hexwave** — sharp feature spotlights; excellent on the new conditional-trig transitions.
- **Nixienoise** — thoughtful management/workflow deep-dives, but the captured one is
  **OG Digitakt** — verify against the DT2.

**Communities & references**
- **Elektronauts** — the hub. Key threads: **DT2 Tips & Tricks** (t/212556), **Overlooked
  new features** (t/213177), **DT2 bug reports** (t/216060), **random/generative
  processes** (t/217473), **Projects Sharing** (t/222284).
- **DT2 Cheat Sheet** (davemech) — printable shortcut reference.

**Packs & tools**
- Elektron Transfer (load samples/packs to the +Drive); Elektron sound packs; DROWNED!,
  Broken FM, ELECTRONISOUNDS (third-party); the `.dt2prj` project-share format (DT2-only —
  does **not** load on the OG).

---

## 7. Common pitfalls / gotchas

- **OG→DT2 migration:** importing an OG project lands its **bottom 8 tracks as MIDI-only**
  — convert each (tracks 9–16) to an audio machine (seconds per track). And **kits don't
  transfer** with the project (Transfer has no kit export) — save sounds as presets first. *(elektronauts-bug-reports)*
- **Chorus collapses to MONO when sent into the Reverb** ("flange-y/phase-y") — for wide
  ambient run chorus + reverb in **parallel**, not chorus-into-reverb. *(elektronauts-send-fx)*
- **Resampling feedback:** with monitoring ON, the source also hits Main Out, so re-amping
  through pedals loops back. Disable `TO MAIN` (sample blind) or monitor via an external
  mixer/USB loop. *(elektronauts-resampling)*
- **Firmware caution:** pattern/+Drive corruption reports around early firmware (largely
  fixed by 1.02). Community rule: **don't upgrade right before a gig**, and **back up
  projects + the +Drive first.** *(elektronauts-bug-reports)*
- **Overbridge stems are DRY (pre-send-FX)** on both OG and DT2; FX only come via the FX
  busses or Main mix. *(rig-overbridge)*
- **Not everything clock-syncs:** **Generation Loss MkII** has no MIDI clock (warble
  free-runs), the **Strymon TimeLine looper** doesn't sync, and **MOOD MkII ignores clock
  in Synth Mode** — see the table in §5. *(rig-clock-sync-pedals)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `cuckoo-dt2-beginners-mega-tutorial.md` — full DT2 beginner→intermediate walkthrough
- `xnb-dt2-deep-dive-guide.md` — deepest menu-by-menu DT2 reference course
- `davemech-dt2-os110-deep-dive.md` — OS 1.10 (mono sampling, Comb+, mod matrix, pre/post routing, p-lock-all)
- `davemech-dt2-slice-machine-os115.md` — OS 1.15 manual Slice machine (amen→jungle)
- `optoproductions-dt2-creative-resampling.md` — resample-the-master sound-design loop
- `optoproductions-dt2-sampling-tutorial.md` — stereo sampling, SRC machines, build
- `hexwave-dt2-new-conditional-trigs.md` — NOT / LAST / NOT-LAST conditionals + chains
- `ezbot-dt2-ambient-music-tutorial.md` — full ~9,700-word ambient build transcript
- `youtube-ezbot-generative-sample-chains-dt2.md` — button-by-button generative slicer
- `nixienoise-OG-digitakt-sample-sound-management.md` — *(OG)* sample/sound/kit hierarchy
- `rig-dt2-overbridge-ableton-walkthrough.md` — OB→Ableton workflow + send-FX behaviour

**Links** (`research/links/`)
- `elektronauts-dt2-tips-tricks-thread.md` — master tips thread
- `elektronauts-dt2-overlooked-features.md` — hidden/overlooked DT2-only features
- `elektronauts-dt2-bug-reports-and-og-migration.md` — bugs, firmware lore, OG→DT2 migration
- `elektronauts-dt2-send-fx-chorus-reverb.md` — chorus→reverb routing + mono-collapse gotcha
- `elektronauts-dt2-resampling-through-fx.md` — re-amp/resample-through-pedals + feedback fixes
- `elektronauts-dt2-generative-and-drone.md` — generative/random processes + drone recipe
- `elektronauts-dt2-cheat-sheet.md` — community cheat-sheet reference
- `elektronauts-dt2-comb-filter-plucked-string-recipe.md` — Comb+ string/banjo technique
- `elektronauts-drowned-dt2-drone-preset-pack.md` — DROWNED! 50-drone pack
- `elektronauts-dt2-projects-sharing-thread.md` — `.dt2prj` project shares
- `elektronauts-ambient-drone-with-the-dt-recipes.md` — community drone recipes *(mostly OG, flagged)*
- `elektron-official-dt2-sound-packs.md` — Reduktion/HexCells/Drench Case/etc.
- `isotonik-amiva-ambient-digitakt-workflow.md` — Amiva INF-decay / all-wet method
- `isotonik-electronisounds-third-party-dt2-packs.md` — Broken FM + ELECTRONISOUNDS banks
- `matrixsynth-travails-abreojos-dt2-doom-drone.md` — Abre Ojos doom-drone DT2+Evolver set
- `ezbot-dt2-ambient-tutorial-recipe.md` — distilled EZBOT recipe w/ real values
- `rig-dt2-midi-tracks-sequencing-external.md` — DT2 MIDI tracks, 16 CCs, MIDI Learn, p-locking PC/CC
- `rig-dt2-clock-master-slave-sync.md` — sync switches, master/slave decisions vs OT/Novation/DAW
- `rig-dt2-clock-sync-pedals-verified.md` — per-pedal clock-sync verification + table
- `rig-dt2-octatrack-combo.md` — DT↔OT clocking, audio routing, role division
- `rig-dt2-overbridge-logic-ableton.md` — OB setup, 42-input map, dry/FX gotcha

## Sources

Video (YouTube): Cuckoo `651_lCCJ1-w` · XNB `8zXBNqRstxQ` · Opto `pvR1gMepME0`, `wi-DCA-uyO8`
· Dave Mech `g5v11gs8MXc`, `sSEMZsMSjd4` · Hexwave `DLi1B6ia-_M` · EZBOT `4xBD3wQRR3I`,
`9bJpBYmoUMw` · Nixienoise (OG) `UwnXAs66B7k` · OB walkthrough `rZdrlpz3MOo`.
Community: elektronauts.com (t/212556, t/213177, t/216060, t/217473, t/217570, t/213230,
t/218343, t/222328, t/220614, t/222284, t/41776, t/84027) · davemech cheat sheet.
Packs/artists: elektron.se/shop/soundpacks · isotonikstudios.com (Amiva, Broken FM,
ELECTRONISOUNDS) · matrixsynth.com (Abre Ojos "Travails").
Rig integration: Digitakt II User Manual OS 1.15A · elektron.se/explore/digitakt-ii ·
elektron.se/support-downloads/overbridge · each pedal's MIDI manual + midi.guide ·
gearnews.com Digitakt II Overbridge.
